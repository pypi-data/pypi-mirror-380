import random

import celeries.laplace as lp
import celeries.perham3pla as ph3
import celeries.series as se


def test_3pla():
  # Compares the output of PerHam3pla.angle with Eq. 43 of
  # https://jeremycouturier.com/3pla/SecondOrderMass.pdf.
  # The analytical expressions are evaluated numerically before comparison.
  # Otherwise, it is difficult to compare them due to recurrence relations
  # in the Laplace coefficients that can make two equal expressions look different.

  H3 = ph3.PerHam3pla(
    degree=0,
    ang2pla=[],
    n0=(),
    ev=False,
    spatial=False,
    keplerian=True,
    disregard13=True,
    disregardInd=True,
    takeout_kn=False,
    verbose=False,
  )

  for _ in range(5):
    # Choosing p, q, alpha12 and alpha23 at random while ensuring
    # p*n1 - (p+q)*n2 + q*n3 = 0
    alp12 = 1.0
    alp23 = 1.0
    while alp12 > 0.75 or alp12 < 0.25 or alp23 > 0.75 or alp23 < 0.25:
      p = random.randint(1, 9)
      q = random.randint(1, 9)
      alp12_min = (p / (p + q)) ** (2.0 / 3.0)
      alp12 = (1.0 - alp12_min) * random.random() + alp12_min
      n1 = 1.0
      n2 = alp12**1.5
      n3 = ((p + q) * n2 - p * n1) / q
      alp23 = (n3 / n2) ** (2.0 / 3.0)

    print(f'Using (p, q, alp12, alp23) = ({p}, {q}, {alp12}, {alp23})')

    PerHam3 = H3.angle((p, -p - q, q))

    alpha12 = se.Var('alpha12')
    alpha23 = se.Var('alpha23')
    b10_12 = se.Var('b10_12')
    b11_12 = se.Var('b11_12')
    b10_23 = se.Var('b10_23')
    b11_23 = se.Var('b11_23')
    b30_12 = se.Var('b30_12')
    b31_12 = se.Var('b31_12')
    b30_23 = se.Var('b30_23')
    b31_23 = se.Var('b31_23')
    b1012 = lp.b(0.5, 0, alp12)
    b1112 = lp.b(0.5, 1, alp12)
    b1023 = lp.b(0.5, 0, alp23)
    b1123 = lp.b(0.5, 1, alp23)
    b3012 = lp.b(1.5, 0, alp12)
    b3112 = lp.b(1.5, 1, alp12)
    b3023 = lp.b(1.5, 0, alp23)
    b3123 = lp.b(1.5, 1, alp23)
    b1p = lp.b(0.5, p, alp12)
    b1q = lp.b(0.5, q, alp23)
    db1p = lp.deriv_b(0.5, p, alp12)
    db1q = lp.deriv_b(0.5, q, alp23)

    # Terms proportional to n2/(n2 - n3)
    ByHand = 0.5 * (alp12 * b1q * db1p + b1p * b1q + p / q * alp23 * b1p * db1q)
    TBCW = PerHam3.coefext({H3._get_k_dot_n(1, -1, (2, 3)): -1}) / H3.ns[1]
    TBCW = TBCW.evalnum(
      {
        alpha12: alp12,
        alpha23: alp23,
        b10_12: b1012,
        b10_23: b1023,
        b11_12: b1112,
        b11_23: b1123,
        b30_12: b3012,
        b30_23: b3023,
        b31_12: b3112,
        b31_23: b3123,
      }
    )
    TBCW = TBCW.toConst()
    assert abs(ByHand - TBCW) < 1.0e-8

    # Terms proportional to n2^2/(n2 - n3)^2
    ByHand = 3 * p / (4 * q) * b1p * b1q
    TBCW = PerHam3.coefext({H3._get_k_dot_n(1, -1, (2, 3)): -2}) / H3.ns[1] ** 2
    TBCW = TBCW.evalnum(
      {
        alpha12: alp12,
        alpha23: alp23,
        b10_12: b1012,
        b10_23: b1023,
        b11_12: b1112,
        b11_23: b1123,
        b30_12: b3012,
        b30_23: b3023,
        b31_12: b3112,
        b31_23: b3123,
      }
    )
    TBCW = TBCW.toConst()
    assert abs(ByHand - TBCW) < 1.0e-8

    # Terms proportional to n2/((q-1)*n2 - q*n3)
    ByHand = -0.25 * (
      q * (2 * p + 1) * b1p * b1q
      + alp23 * (0.5 + p) * b1p * db1q
      + q * alp12 * b1q * db1p
      + 0.5 * alp12 * alp23 * db1p * db1q
    )
    if q > 1:
      TBCW = PerHam3.coefext({H3._get_k_dot_n(q - 1, -q, (2, 3)): -1}) / H3.ns[1]
    else:
      TBCW = -PerHam3.coefext({H3._get_k_dot_n(0, 1, (2, 3)): -1}) / H3.ns[1]
    TBCW = TBCW.evalnum(
      {
        alpha12: alp12,
        alpha23: alp23,
        b10_12: b1012,
        b10_23: b1023,
        b11_12: b1112,
        b11_23: b1123,
        b30_12: b3012,
        b30_23: b3023,
        b31_12: b3112,
        b31_23: b3123,
      }
    )
    TBCW = TBCW.toConst()
    assert abs(ByHand - TBCW) < 1.0e-8

    # Terms proportional to n2/((q+1)*n2 - q*n3)
    ByHand = 0.25 * (
      q * (2 * p - 1) * b1p * b1q
      + alp23 * (0.5 - p) * b1p * db1q
      - q * alp12 * b1q * db1p
      + 0.5 * alp12 * alp23 * db1p * db1q
    )
    TBCW = PerHam3.coefext({H3._get_k_dot_n(q + 1, -q, (2, 3)): -1}) / H3.ns[1]
    TBCW = TBCW.evalnum(
      {
        alpha12: alp12,
        alpha23: alp23,
        b10_12: b1012,
        b10_23: b1023,
        b11_12: b1112,
        b11_23: b1123,
        b30_12: b3012,
        b30_23: b3023,
        b31_12: b3112,
        b31_23: b3123,
      }
    )
    TBCW = TBCW.toConst()
    assert abs(ByHand - TBCW) < 1.0e-8
