from deltapv import objects, residual, linalg, physics, scales, util
from jax import numpy as jnp, jit, custom_jvp, jvp, vmap, lax
from typing import Tuple

import logging
logger = logging.getLogger("deltapv")

PVCell = objects.PVCell
LightSource = objects.LightSource
Potentials = objects.Potentials
Boundary = objects.Boundary
Array = util.Array
f64 = util.f64
i64 = util.i64
n_lnsrch = 500


def vincr(cell: PVCell, num_vals: i64 = 20) -> f64:
    # TODO: cell unused
    dv = 1 / num_vals / scales.energy

    return dv


def eq_guess(cell: PVCell, bound_eq: Boundary) -> Potentials:

    N = cell.Eg.size
    phi_guess = physics.EF(cell)
    pot_guess = Potentials(phi_guess, jnp.zeros(N), jnp.zeros(N))

    return pot_guess


def ooe_guess(cell: PVCell, pot_eq: Potentials) -> Potentials:

    Ec = -cell.Chi - pot_eq.phi
    Ev = -cell.Chi - cell.Eg - pot_eq.phi
    pot_guess = Potentials(pot_eq.phi, Ec, Ev)

    return pot_guess


@jit
def logdamp(move: Array) -> Array:

    damped = jnp.where(
        jnp.abs(move) > 1,
        jnp.log(1 + jnp.abs(move) * 1.72) * jnp.sign(move), move)

    return damped


@jit
def scaledamp(move: Array, threshold: f64 = 50) -> Array:

    big = jnp.max(jnp.abs(move))
    gamma = jnp.maximum(big, threshold)
    damped = threshold * move / gamma

    return damped


@jit
def pot2vec(pot: Potentials) -> Array:

    n = pot.phi.size
    vec = jnp.zeros(3 * n)
    vec = vec.at[0::3].set(pot.phi_n)
    vec = vec.at[1::3].set(pot.phi_p)
    vec = vec.at[2::3].set(pot.phi)

    return vec


@jit
def vec2pot(vec: Array) -> Potentials:

    return Potentials(vec[2::3], vec[0::3], vec[1::3])


@jit
def modify(pot: Potentials, move: Array) -> Potentials:

    phi_new = pot.phi + move[2::3]
    phi_n_new = pot.phi_n + move[::3]
    phi_p_new = pot.phi_p + move[1::3]
    pot_new = Potentials(phi_new, phi_n_new, phi_p_new)

    return pot_new


@jit
def residnorm(cell, bound, pot, move, alpha):

    pot_new = modify(pot, alpha * move)
    F = residual.comp_F(cell, bound, pot_new)
    Fnorm = jnp.linalg.norm(F)

    return Fnorm


@jit
def linesearch(cell: PVCell, bound: Boundary, pot: Potentials,
               p: Array) -> Array:

    alphas = jnp.linspace(0, 2, n_lnsrch)
    R = vmap(residnorm, (None, None, None, None, 0))(cell, bound, pot, p,
                                                     alphas)
    alpha_best = alphas[n_lnsrch // 10:][jnp.argmin(R[n_lnsrch // 10:])]

    return alpha_best


@jit
def fwdlnsrch(cell: PVCell,
              bound: Boundary,
              pot: Potentials,
              p: Array,
              gamma: f64 = 1.1) -> Array:

    pair_ini = 1., gamma

    def cond_fun(pair):
        alpha0, alpha1 = pair
        R0 = residnorm(cell, bound, pot, p, alpha0)
        R1 = residnorm(cell, bound, pot, p, alpha1)
        return R0 > R1

    def body_fun(pair):
        _, alpha1 = pair
        pair_new = alpha1, gamma * alpha1
        return pair_new

    alpha_best, _ = lax.while_loop(cond_fun, body_fun, pair_ini)

    return alpha_best


def linguess(pot: Potentials, potl: Potentials):

    return Potentials(2 * pot.phi - potl.phi, 2 * pot.phi_n - potl.phi_n,
                      2 * pot.phi_p - potl.phi_p)


def genlinguess(pot: Potentials, potl: Potentials, dx1: f64, dx2: f64):

    return Potentials(pot.phi + (pot.phi - potl.phi) * dx2 / dx1,
                      pot.phi_n + (pot.phi_n - potl.phi_n) * dx2 / dx1,
                      pot.phi_p + (pot.phi_p - potl.phi_p) * dx2 / dx1)


def quadguess(pot: Potentials, potl: Potentials, potll: Potentials):

    f, fn, fp = pot.phi, pot.phi_n, pot.phi_p
    fl, fnl, fpl = potl.phi, potl.phi_n, potl.phi_p
    fll, fnll, fpll = potll.phi, potll.phi_n, potll.phi_p

    return Potentials(3 * f - 3 * fl + fll, 3 * fn - 3 * fnl + fnll,
                      3 * fp - 3 * fpl + fpll)


@jit
def step_eq_dense(cell: PVCell, bound: Boundary,
                  pot: Potentials) -> Tuple[Potentials, f64]:

    Feq = residual.comp_F_eq(cell, bound, pot)
    spJeq = residual.comp_F_eq_deriv(cell, bound, pot)
    Jeq = linalg.sparse2dense(spJeq)
    p = jnp.linalg.solve(Jeq, -Feq)

    error = jnp.max(jnp.abs(p))
    resid = jnp.linalg.norm(Feq)
    dx = logdamp(p)

    pot_new = Potentials(pot.phi + dx, pot.phi_n, pot.phi_p)

    stats = {"error": error, "resid": resid}

    return pot_new, stats


@jit
def step_eq(cell: PVCell, bound: Boundary,
            pot: Potentials) -> Tuple[Potentials, f64]:

    Feq = residual.comp_F_eq(cell, bound, pot)
    spJeq = residual.comp_F_eq_deriv(cell, bound, pot)
    p = linalg.linsol(spJeq, -Feq, tol=1e-6)

    error = jnp.max(jnp.abs(p))
    resid = jnp.linalg.norm(Feq)
    dx = logdamp(p)

    pot_new = Potentials(pot.phi + dx, pot.phi_n, pot.phi_p)

    stats = {"error": error, "resid": resid}

    return pot_new, stats


def solve_eq_dense(cell: PVCell, bound: Boundary,
                   pot_ini: Potentials) -> Potentials:

    pot = pot_ini
    error = 1
    niter = 0

    while niter < 100 and error > 1e-6:

        pot, stats = step_eq_dense(cell, bound, pot)
        error = stats["error"]
        resid = stats["resid"]
        niter += 1
        logger.info("    iteration {:3d}    |p| = {:.2e}    |F| = {:.2e}".format(  # noqa
            niter, error, resid))

        if jnp.isnan(error) or error == 0:
            logger.critical("    Dense solver failed! It's all over.")
            raise SystemExit

    return pot


@custom_jvp
def solve_eq(cell: PVCell, bound: Boundary, pot_ini: Potentials) -> Potentials:

    pot = pot_ini
    error = 1
    niter = 0

    while niter < 100 and error > 1e-6:

        pot, stats = step_eq(cell, bound, pot)
        error = stats["error"]
        resid = stats["resid"]
        niter += 1
        logger.info("    iteration {:3d}    |p| = {:.2e}    |F| = {:.2e}".format(  # noqa
            niter, error, resid))

        if jnp.isnan(error) or error == 0:
            logger.error("    Sparse solver failed! Switching to dense.")
            return solve_eq_dense(cell, bound, pot_ini)

    return pot


@solve_eq.defjvp
def solve_eq_jvp(primals, tangents):

    cell, bound, pot_ini = primals
    dcell, dbound, _ = tangents
    sol = solve_eq(cell, bound, pot_ini)

    zerodpot = Potentials(jnp.zeros_like(sol.phi), jnp.zeros_like(sol.phi_n),
                          jnp.zeros_like(sol.phi_p))

    _, rhs = jvp(residual.comp_F_eq, (cell, bound, sol),
                 (dcell, dbound, zerodpot))

    spF_eq_pot = residual.comp_F_eq_deriv(cell, bound, sol)
    F_eq_pot = linalg.sparse2dense(spF_eq_pot)
    dF_eq = jnp.linalg.solve(F_eq_pot, -rhs)

    primal_out = sol
    tangent_out = Potentials(dF_eq, jnp.zeros_like(sol.phi_n),
                             jnp.zeros_like(sol.phi_p))

    return primal_out, tangent_out


@jit
def similarity(v1, v2):
    sim = jnp.dot(v1, v2) / (
        jnp.maximum(jnp.linalg.norm(v1), jnp.linalg.norm(v2))**2 + 1e-3)
    return sim


@jit
def acceleration(p, pl, dxl, beta):

    sim = jnp.maximum(similarity(p, pl), 0)
    dx = p + beta * sim * dxl

    return dx


@jit
def step_dense(cell: PVCell,
               bound: Boundary,
               pot: Potentials,
               pl: Array,
               dxl: Array,
               beta: f64 = 0.9) -> Tuple[Potentials, dict]:

    F = residual.comp_F(cell, bound, pot)
    spJ = residual.comp_F_deriv(cell, bound, pot)
    J = linalg.sparse2dense(spJ)
    p = logdamp(jnp.linalg.solve(J, -F))
    dx = acceleration(p, pl, dxl, beta)
    pot_new = modify(pot, dx)

    error = jnp.max(jnp.abs(p))
    resid = jnp.linalg.norm(F)
    stats = {"error": error, "resid": resid, "p": p, "dx": dx}

    return pot_new, stats


def solve_dense(cell: PVCell, bound: Boundary,
                pot_ini: Potentials) -> Potentials:

    pot = pot_ini
    error = 1
    niter = 0
    pl = jnp.zeros(3 * pot.phi.size)
    dxl = jnp.zeros(3 * pot.phi.size)

    while niter < 100 and error > 1e-6:

        pot, stats = step_dense(cell, bound, pot, pl, dxl)
        error = stats["error"]
        resid = stats["resid"]
        pl = stats["p"]
        dxl = stats["dx"]
        niter += 1
        logger.info("    iteration {:3d}    |p| = {:.2e}    |F| = {:.2e}".format(  # noqa
            niter, error, resid))

        if jnp.isnan(error) or error == 0:
            logger.critical("    Dense solver failed! It's all over.")
            raise SystemExit

    return pot


@jit
def step(cell: PVCell,
         bound: Boundary,
         pot: Potentials,
         pl: Array,
         dxl: Array,
         beta: f64 = 0.9) -> Tuple[Potentials, dict]:

    F = residual.comp_F(cell, bound, pot)
    spJ = residual.comp_F_deriv(cell, bound, pot)
    p = logdamp(linalg.linsol(spJ, -F, tol=1e-6))
    dx = acceleration(p, pl, dxl, beta)
    pot_new = modify(pot, dx)

    error = jnp.max(jnp.abs(p))
    resid = jnp.linalg.norm(F)
    stats = {"error": error, "resid": resid, "p": p, "dx": dx}

    return pot_new, stats


@custom_jvp
def solve(cell: PVCell, bound: Boundary, pot_ini: Potentials) -> Potentials:

    pot = pot_ini
    error = 1
    niter = 0
    pl = jnp.zeros(3 * pot.phi.size)
    dxl = jnp.zeros(3 * pot.phi.size)

    while niter < 100 and error > 1e-6:

        pot, stats = step(cell, bound, pot, pl, dxl)
        error = stats["error"]
        resid = stats["resid"]
        pl = stats["p"]
        dxl = stats["dx"]
        niter += 1
        logger.info("    iteration {:3d}    |p| = {:.2e}    |F| = {:.2e}".format(  # noqa
            niter, error, resid))

        if jnp.isnan(error) or error == 0:
            logger.error("    Sparse solver failed! Switching to dense.")
            return solve_dense(cell, bound, pot_ini)

    return pot


@solve.defjvp
def solve_jvp(primals, tangents):

    cell, bound, pot_ini = primals
    dcell, dbound, _ = tangents
    sol = solve(cell, bound, pot_ini)

    zerodpot = Potentials(jnp.zeros_like(sol.phi), jnp.zeros_like(sol.phi_n),
                          jnp.zeros_like(sol.phi_p))

    _, rhs = jvp(residual.comp_F, (cell, bound, sol),
                 (dcell, dbound, zerodpot))

    spF_pot = residual.comp_F_deriv(cell, bound, sol)
    F_pot = linalg.sparse2dense(spF_pot)
    dF = jnp.linalg.solve(F_pot, -rhs)

    primal_out = sol
    tangent_out = Potentials(dF[2::3], dF[0::3], dF[1::3])

    return primal_out, tangent_out
