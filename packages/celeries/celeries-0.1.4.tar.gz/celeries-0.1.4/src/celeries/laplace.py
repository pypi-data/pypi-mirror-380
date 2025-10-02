# Copyright 2016-2025 Jean-Baptiste Delisle, Jérémy Couturier
# Licensed under the EUPL-1.2 or later
from .mpfrac import Fraction, getctx
from .series import Series, Var


def b(s, k, alpha):
  r"""
  Laplace coefficient b_s^(k) (alpha).

  Parameters
  ----------
  s : float
  k : int
  alpha : float

  Returns
  -------
  b : float
    Laplace coefficient.
  """
  if k < 0:
    return b(s, -k, alpha)
  ctx = getctx()
  skkfac = ctx.fprod([ctx.fdiv(s + j, 1 + j) for j in range(k)])
  bska = 2 * skkfac * alpha**k * ctx.hyp2f1(s, s + k, k + 1, alpha**2)
  return bska


def deriv_b(s, k, alpha):
  r"""
  Derivative of the Laplace coefficient b_s^(k) (alpha) with respect to alpha.

  Parameters
  ----------
  s : float
  k : int
  alpha : float

  Returns
  -------
  db : float
    Derivative Laplace coefficient.
  """
  return s * (
    b(s + 1, k - 1, alpha) + b(s + 1, k + 1, alpha) - 2 * alpha * b(s + 1, k, alpha)
  )


def formal_deriv_b(s, k):
  r"""
  Formal derivative of the Laplace coefficient b_s/2^(k) (alpha) with respect to alpha.

  Parameters
  ----------
  s : int
  k : int

  Returns
  -------
  R : Series
    Derivative of b_s/2^(k) (alpha) with respect to alpha.
  """
  if k < 0:
    return formal_deriv_b(s, -k)

  b_sp2_km1 = Var(
    f'b_{s + 2}_{abs(k - 1)}'
  )  # A Laplace coefficient that the derivative depends upon
  b_sp2_k = Var(
    f'b_{s + 2}_{abs(k)}'
  )  # A Laplace coefficient that the derivative depends upon
  alpha = Var('alpha')
  return Series(
    Fraction(s**2, s - 2 * k) * b_sp2_km1
    + (Fraction(s**2 - k * s, 2 * k - s) * alpha + Fraction(k * s, 2 * k - s) / alpha)
    * b_sp2_k
  )


def formal_dderiv_b(s, k):
  r"""
  Formal second derivative of the Laplace coefficient b_s/2^(k) (alpha)
  with respect to alpha.

  Parameters
  ----------
  s : int
  k : int

  Returns
  -------
  R : Series
    Second derivative of b_s/2^(k) (alpha) with respect to alpha.
  """
  if k < 0:
    return formal_dderiv_b(s, -k)

  b_sp2_k = Var(f'b_{s + 2}_{abs(k)}')
  alpha = Var('alpha')
  db_sp2_km1 = formal_deriv_b(s + 2, k - 1)
  db_sp2_k = formal_deriv_b(s + 2, k)
  return Series(
    Fraction(s**2, s - 2 * k) * db_sp2_km1
    + Fraction(s**2 - k * s, 2 * k - s) * (b_sp2_k + alpha * db_sp2_k)
    + Fraction(k * s, 2 * k - s) * (db_sp2_k / alpha - b_sp2_k / alpha**2)
  )


def rec_b(s, k):
  r"""
  Gives the Laplace coefficient b_s/2^(k) (alpha) as a function of alpha,
  b_s/2^(0), and b_s/2^(1) only.

  Parameters
  ----------
  s : int
  k : int

  Returns
  -------
  R : Series
    Laplace coefficient b_s/2^(k) (alpha) given as a function of alpha,
    b_s/2^(0), and b_s/2^(1) only
  """
  if k < 0:
    return rec_b(s, -k)
  if k < 2:
    return Series(Var(f'b_{s}_{k}'))

  alpha = Var('alpha')
  return Series(
    Fraction(2 * k - 2, 2 * k - s) * (alpha + alpha**-1) * rec_b(s, k - 1)
    - Fraction(2 * k + s - 4, 2 * k - s) * rec_b(s, k - 2)
  )
