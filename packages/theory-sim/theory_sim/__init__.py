"""Invisible Pressure / DUP (Dimensional Unifying Pressure) simulation package.

Implements the theory's core equations as falsifiable models:
  - DUP pressure:        P = rho * v^2
  - Pressure gradient:   F = -grad(P)  (replaces Newtonian F = G m1 m2 / r^2)
  - Orbital prediction:  v ~ 1/r (DUP) vs v ~ 1/sqrt(r) (Kepler/Newton)

HONESTY: this package is a *comparative test harness*. It computes both the
Newtonian and DUP predictions and reports residuals against real data, so the
theory's distinguishing prediction can be evaluated by peer review.
"""
