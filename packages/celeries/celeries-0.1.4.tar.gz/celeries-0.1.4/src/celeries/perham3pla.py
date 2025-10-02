# Copyright 2016-2025 Jérémy Couturier, Jean-Baptiste Delisle
# Licensed under the EUPL-1.2 or later
from . import laplace as lp
from . import mpfrac as mf
from . import perham as ph
from . import prime as pm
from . import series as se


class _PerHam3pla:
  def __init__(
    self,
    degree,
    ang2pla=(),
    n0=(),
    ev=False,
    spatial=False,
    keplerian=False,
    disregard13=False,
    disregardInd=False,
    takeout_kn=False,
    verbose=True,
  ):
    self.degree = degree
    self.ang2pla = ang2pla
    self.n0 = n0
    self.ev = ev
    self.spatial = spatial
    self.keplerian = keplerian
    self.disregard13 = disregard13
    self.disregardInd = disregardInd
    self.takeout_kn = takeout_kn
    self.verbose = verbose

    self.km_max = 32  # km_max = 32 might not be enough. Will be increased if needed
    self.Hp = ph.LazyPerHam(
      degree=self.degree + 1, km_max=self.km_max, spatial=self.spatial
    )
    self.max_s = (
      degree + degree % 2 + 3
    )  # max_s is the largest value of s such that a serie can depend on b_s/2^k

    self.alpha = se.Var('alpha')
    self.sqalp = se.Var('sqalp')
    self.X1 = se.Var('X1')
    self.X2 = se.Var('X2')
    self.Xb1 = se.Var('Xb1')
    self.Xb2 = se.Var('Xb2')
    self.Y1 = se.Var('Y1')
    self.Y2 = se.Var('Y2')
    self.Yb1 = se.Var('Yb1')
    self.Yb2 = se.Var('Yb2')
    self.xi = se.Var('xi')
    self.xj = se.Var('xj')
    self.xbi = se.Var('xbi')
    self.xbj = se.Var('xbj')
    self.yi = se.Var('yi')
    self.yj = se.Var('yj')
    self.ybi = se.Var('ybi')
    self.ybj = se.Var('ybj')
    self.lbdi = se.Angle('lbdi')
    self.lbdj = se.Angle('lbdj')
    self.Lbdi = se.Var('Lbdi')
    self.Lbdj = se.Var('Lbdj')
    self.sq2Li = se.Var('sq2Li')
    self.sq2Lj = se.Var('sq2Lj')
    self.kdotn = se.Var('kdotn')
    self.alphas = [
      [se.Var('alpha11'), se.Var('alpha12'), se.Var('alpha13')],
      [se.Var('alpha21'), se.Var('alpha22'), se.Var('alpha23')],
      [se.Var('alpha31'), se.Var('alpha32'), se.Var('alpha33')],
    ]
    self.sqalps = [
      [se.Var('sqalp11'), se.Var('sqalp12'), se.Var('sqalp13')],
      [se.Var('sqalp21'), se.Var('sqalp22'), se.Var('sqalp23')],
      [se.Var('sqalp31'), se.Var('sqalp32'), se.Var('sqalp33')],
    ]
    self.xs = [se.Var('x1'), se.Var('x2'), se.Var('x3')]
    self.xbs = [se.Var('xb1'), se.Var('xb2'), se.Var('xb3')]
    self.Xs = [se.Var('X1'), se.Var('X2'), se.Var('X3')]
    self.Xbs = [se.Var('Xb1'), se.Var('Xb2'), se.Var('Xb3')]
    self.ys = [se.Var('y1'), se.Var('y2'), se.Var('y3')]
    self.ybs = [se.Var('yb1'), se.Var('yb2'), se.Var('yb3')]
    self.Ys = [se.Var('Y1'), se.Var('Y2'), se.Var('Y3')]
    self.Ybs = [se.Var('Yb1'), se.Var('Yb2'), se.Var('Yb3')]
    self.lbds = [se.Angle('lbd1'), se.Angle('lbd2'), se.Angle('lbd3')]
    self.vrps = [se.Angle('vrp1'), se.Angle('vrp2'), se.Angle('vrp3')]
    self.Lbds = [se.Var('Lbd1'), se.Var('Lbd2'), se.Var('Lbd3')]
    self.ms = [se.Var('m1'), se.Var('m2'), se.Var('m3')]
    self.sq2Ls = [se.Var('sq2L1'), se.Var('sq2L2'), se.Var('sq2L3')]
    self.ns = [se.Var('n1'), se.Var('n2'), se.Var('n3')]

    if self.ev and self.n0 == ():
      raise Exception(
        'The nominal mean motion were not given as argument in class PerHam3pla. '
        'No evaluation can be done.'
      )
    if self.ev and (self.n0[0] <= self.n0[1] or self.n0[1] <= self.n0[2]):
      raise Exception(
        'The nominal mean motion must verify n1 > n2 > n3 in class PerHam3pla.'
      )


class PerHam3pla(_PerHam3pla):
  r"""
  Perturbative part of the 4-body (3-planet) Hamiltonian to second order in mass.

  Computes the perturbative part of the Hamiltonian of 3-planet angles
  of the form k1*lbd1 + k2*lbd2 + k3*lbd3 at order degree
  in eccentricity and inclination.
  These angles appear in the Hamiltonian at second order in mass
  of a Lie series expansion after averaging out
  some or all 2-planet angles at first order in mass.

  Refer to https://jeremycouturier.com/3pla/SecondOrderMass.pdf
  for the mathematical details

  If ev is True, the semi-major axes and mean motions are evaluated
  to their nominal values.
  n0 = (1., n2/n1, n3/n1) contains the nominal mean motions ratios
  and needs to be given only if ev is True.
  Can also be given as n0 = (n1, n2, n3) in whatever units.
  The nominal semi-major axes do not need to be given
  as they are obtained from a_i/a_j = (n_j/n_i)^(2/3).
  If ev is False, a large serie should be expected as output,
  especially if degree is high.
  It is recommended to set celeries.series.backtoline(True).

  ang2pla = [(i1, j1, p1, q1), ..., (iN, jN, pN, qN)] is a list of 4-tuples
  indicating 2-planet angles that must not be averaged.
  (ik, jk) with 1 <= ik < jk <= 3 indicates the pair of planet
  and (pk, qk) indicates that the angle pk*lbd_ik + qk*lbd_jk should not be averaged.
  The Lie series expansion to second-order in mass is performed
  by not averaging over these 2-planets angles and their harmonics,
  which remain at first order in mass in the Hamiltonian.
  For example, for the 3-planet angle 2lbd1 - 4lbd2 + 3lbd3 formed by the difference
  of 2-planet angles (2lbd1 - 3lbd2) - (lbd2 - 3lbd3),
  if the system is still close from the 2-planet
  resonances, ang2pla can be set to [(1, 2, 2, -3), (2, 3, 1, -3), (1, 3, 2, -9)].
  If the system is far from any low-order 2-planet resonance, ang2pla can be left to ().
  By default, ex2pla = () and all 2-planet angles are averaged.
  Only the fundamental of an angle or its opposite should be mentionned in ex2pla.
  ang2pla = [(1, 2, 2, -3), (1, 2, -2, 3)], ang2pla = [(1, 2, 2, -3), (1, 2, 4, -6)],
  ang2pla = [(1, 2, 4, -6)] are all invalid

  If keplerian is True, the equality k1*n1 + k2*n2 + k3*n3 = 0 is used to make sure
  that denominators of the form p*ni + q*nj are expressed with n2 and n3 only.
  This roughly halves the number of terms in the serie.
  This parameter is irrelevant when ev is True.

  Many authors (e.g. A. Quillen, 2011 or A. Petit, 2020, 2021)
  disregard contributions from pair (1, 3).
  This can be achieved by setting disregard13 to True.
  Many authors also disregard indirect contributions (due to the star's reflex motion).
  This can be achieved by setting disregardInd to True.
  Many authors sometimes assume that the denominator k.n is a constant
  and take it out of the Poisson bracket, even though it explicitly depends on Lambda.
  Deriving this denominator with respect to Lambda yields terms of order 2 in mass,
  and cannot be disregarded a priori.
  The boolean takeout_kn controls this.

  Parameters
  ----------
  degree : Positive integer
    Degree of the development in eccentricity and inclination.
  ang2pla : List of 4-tuples of integers
    2-planet angles that should not be averaged out during the Lie series expansion.
  n0 : 3-tuple of float
    The nominal mean motion ratios (1., n2/n1, n3/n1).
    Does not need to be specified if ev is False.
  ev : bool
    Determines if the semi-major axes and mean motions should be evaluated
    to their nominal values in the returned serie.
  spatial : bool
    Determines if the Hamiltonian is 3D or coplanar.
  keplerian : bool
    Determines if the equality k1*n1 + k2*n2 + k3*n3 = 0 should be assumed true
    to simplify the returned serie. Irrelevant when ev is True.
  disregard13 : bool
    Determines if Poisson brackets involving the pair (1, 3) should be disregarded.
  disregardInd : bool
    Determines if indirect terms of the Hamiltonian are disregarded.
  takeout_kn : bool
    Determines if the denominator k.n is taken out of the Poisson brackets
    before computing them.
  verbose : bool
    Determines if the computed Poisson brackets are printed.
  """

  def __init__(
    self,
    degree,
    ang2pla=(),
    n0=(),
    ev=False,
    spatial=False,
    keplerian=False,
    disregard13=False,
    disregardInd=False,
    takeout_kn=False,
    verbose=True,
  ):
    super().__init__(
      degree,
      ang2pla,
      n0,
      ev,
      spatial,
      keplerian,
      disregard13,
      disregardInd,
      takeout_kn,
      verbose,
    )

  def angle(self, k):
    r"""
    Returns the perturbative part of the Hamiltonian
    for the 3-planet angle k1*lbd1 + k2*lbd2 + k3*lbd3.
    A factor (m1/m0)*(m2/m0)*n3*Lbd3*expi(k1*lbd1 + k2*lbd2 + k3*lbd3),
    common to all terms of the returned serie, is left out.

    The returned serie depends on Xi, Yi, Xbi, Ybi, for 1 <= i <= 3.
    These quantities are defined in Laskar&Robutel, 1995 (Eq. 13 and Appendix).
    If ev is False, the returned serie also depends on
    alphaij = ai/aj and sqalpij = sqrt(ai/aj) for 1 <= i < j <= 3,
    as well on the Laplace coefficients
    bs0_ij = b_s/2^(0) (ai/aj) and bs1_ij = b_s/2^(1) (ai/aj)
    where s is an odd integer verifying 1 <= s <= degree + (degree mod 2) + 3.
    If ev is False, the returned serie also depends on the mean motions nj
    (only n2 and n3 if keplerian is True).
    The equalities alpha13 = alpha12*alpha23 and sqalp13 = sqalp12*sqalp23
    are used to remove dependency on alpha13 and sqalp13.
    If disregardInd is True, then the returned serie does not depend on sqalp23
    (but it may still depend on sqalp12
    due to the substitution Lbd1/Lbd2*m2/m1 = sqalp12).

    Parameters
    ----------
    k: Tuple of int
      Coefficients k = (k1, k2, k3) of the mean longitudes for the 3-planet angle.

    Returns
    -------
    R : Series
      The contribution to the perturbative part of the Hamiltonian
      for the required 3-planet angle.
    """
    H = 0
    k1, k2, k3 = k
    if k1 * k2 * k3 == 0:
      raise Exception('None of the angle coefficients can be zero in PerHam3pla.angle.')
      # Note : The possibility of allowing one or several of the kj to be zero requires
      # much more work as infinitely many Poisson brackets yield the required angle.
      # I currently limit myself to the case where none of the kj is 0.
    if self.keplerian:
      if (
        k1 * k2 > 0 and k1 * k3 > 0 and k2 * k3 > 0
      ):  # k1, k2 and k3 all have the same sign
        raise Exception(
          'You speficied keplerian = True in PerHam3pla.angle '
          'but k1*n1 + k2*n2 + k3*n3 cannot be zero '
          'when k1, k2 and k3 all have the same sign.'
        )
      if (
        abs(k1) == abs(k2)
        and abs(k2) == abs(k3)
        and (
          (k1 > 0 and k2 < 0 and k3 > 0)
          or (k1 > 0 and k2 > 0 and k3 < 0)
          or (k1 < 0 and k2 > 0 and k3 < 0)
          or (k1 < 0 and k2 < 0 and k3 > 0)
        )
      ):
        raise Exception(
          'You speficied keplerian = True in PerHam3pla.angle '
          'but k1*n1 + k2*n2 + k3*n3 cannot be zero '
          f'when (k1,k2,k3) = ({k1},{k2},{k3}) because n1 > n2 > n3.'
        )
      if k1 + k2 + k3 == 0 and (k1 == k2 or k2 == k3):
        raise Exception(
          'You speficied keplerian = True in PerHam3pla.angle '
          'but k1*n1 + k2*n2 + k3*n3 cannot be zero '
          f'when (k1,k2,k3) = ({k1},{k2},{k3}) because n1 > n2 > n3.'
        )

    # Defining pairs of planets on each side of the Poisson bracket
    if self.disregard13:
      brackets = [((1, 2), (2, 3)), ((2, 3), (1, 2))]
    else:
      brackets = [
        ((1, 2), (1, 3)),
        ((1, 3), (1, 2)),
        ((1, 3), (2, 3)),
        ((2, 3), (1, 3)),
        ((1, 2), (2, 3)),
        ((2, 3), (1, 2)),
      ]

    # Getting all relevant Poisson brackets
    Tuples = [self._get_brackets_for_3pla_angle(k, pairs) for pairs in brackets]

    # Computing all the relevant Poisson brackets
    for bracket, tuples in zip(brackets, Tuples):
      inner_pair, outer_pair = bracket
      i, j = inner_pair
      I, J = outer_pair
      if self.verbose:
        print(f'Doing brackets of the form {{{i}{j}, {I}{J}}}')
      for tpl in tuples:
        p, q, r, s = tpl
        if self.verbose:
          if q < 0 and s < 0:
            print(
              f'    Doing bracket {{expi({p} lbd{i} - {-q} lbd{j}), '
              f'expi({r} lbd{I} - {-s} lbd{J})}}'
            )
          elif q < 0 and s > 0:
            print(
              f'    Doing bracket {{expi({p} lbd{i} - {-q} lbd{j}), '
              f'expi({r} lbd{I} + {s} lbd{J})}}'
            )
          elif q > 0 and s < 0:
            print(
              f'    Doing bracket {{expi({p} lbd{i} + {q} lbd{j}), '
              f'expi({r} lbd{I} - {-s} lbd{J})}}'
            )
          else:
            print(
              f'    Doing bracket {{expi({p} lbd{i} + {q} lbd{j}), '
              f'expi({r} lbd{I} + {s} lbd{J})}}'
            )
        if (
          abs(p) + abs(q) > self.km_max or abs(r) + abs(s) > self.km_max
        ):  # Hp needs to be recomputed with higher km_max
          self.km_max *= 4
          self.Hp = ph.LazyPerHam(
            degree=self.degree + 1, km_max=self.km_max, spatial=self.spatial
          )
        Chi = (
          self._get_Hamiltonian_term(p, q) / self.Lbdj**2
        )  # Generator. Factor -i/k.n will be added further down
        H1 = self._get_Hamiltonian_term(r, s) / self.Lbdj**2  # H1
        ctb = mf.Fraction(1, 2) * self._poisson_bracket(
          Chi, H1, inner_pair, outer_pair, tpl
        )  # H2 = 1/2*{Chi, H1 + H1_bar}
        if self.ang2pla != []:
          # Checking if that term of H1 is also in H1_bar.
          # Doubling the contribution if so
          for tpl1 in self.ang2pla:
            ik, jk, pk, qk = tpl1
            if ik == I and jk == J:
              for K in range(1, self.degree + 2):
                if (K * pk == r and K * qk == s) or (-K * pk == r and -K * qk == s):
                  ctb *= 2
        for l in range(3):  # X = sq2L*x  Y = 1/2*sq2L*y
          ctb = ctb.subst(self.xs[l], self.Xs[l] / self.sq2Ls[l])
          ctb = ctb.subst(self.xbs[l], self.Xbs[l] / self.sq2Ls[l])
          if self.spatial:
            ctb = ctb.subst(self.ys[l], 2 * self.Ys[l] / self.sq2Ls[l])
            ctb = ctb.subst(self.ybs[l], 2 * self.Ybs[l] / self.sq2Ls[l])
        Gmimj_aj = se.Var(f'm{i}') / se.Var('m0') * self.ns[j - 1] * self.Lbds[j - 1]
        GmImJ_aJ = se.Var(f'm{I}') / se.Var('m0') * self.ns[J - 1] * self.Lbds[J - 1]
        ctb = ctb * self.Lbds[j - 1] ** 2 * self.Lbds[J - 1] ** 2
        # Adding back the two factors that were left out
        # when calling function _get_Hamiltonian_term
        ctb = ctb * Gmimj_aj * GmImJ_aJ
        for l in range(3):
          ctb = ctb.subst(
            self.sq2Ls[l], 2 / self.Lbds[l], power=2, negative=True
          )  # sq2L**2 = 2/Lbd
        ctb = ctb.subst(
          self.alphas[0][2], self.alphas[0][1] * self.alphas[1][2]
        )  # alpha13 = alpha12*alpha23
        ctb = ctb.subst(
          self.sqalps[0][2], self.sqalps[0][1] * self.sqalps[1][2]
        )  # sqalp13 = sqalp12*sqalp23
        ctb = ctb.subst(
          self.Lbds[1], self.Lbds[0] * self.ms[1] / self.ms[0] / self.sqalps[0][1]
        )  # Lbd2 = Lbd1*m2/m1*sqalp12**-1
        if self.ev:
          ctb = ctb.evalnum(
            {self.sqalps[0][1]: (self.n0[1] / self.n0[0]) ** (1.0 / 3.0)}
          )
          ctb = ctb / (mf.i)
          n3_over_k_dot_n = 1.0 / (
            p * self.n0[i - 1] / self.n0[2] + q * self.n0[j - 1] / self.n0[2]
          )
          ctb = ctb * n3_over_k_dot_n / self.ns[2]  # Chi = H1/(i*k.n)
          ctb = ctb.subst(self.ns[0], self.ns[2] * self.n0[0] / self.n0[2])
          ctb = ctb.subst(self.ns[1], self.ns[2] * self.n0[1] / self.n0[2])
        else:
          ctb = ctb.subst(
            self.sqalps[0][1], self.alphas[0][1], power=2, negative=True
          )  # sqalp12**2 = alpha12
          ctb = ctb.subst(
            self.sqalps[1][2], self.alphas[1][2], power=2, negative=True
          )  # sqalp23**2 = alpha23
          # Using equality k1n1 + k2n2 + k3n3 = 0 to get rid of divisors involving n1.
          # This roughly halves the number of terms in the serie.
          if i == 1 and self.keplerian:
            ctb *= k1
            if not self.takeout_kn:
              ctb = ctb.subst(self.kdotn, self.kdotn / k1)
            if j == 2:
              P = k1 * q - p * k2
              Q = -p * k3
            else:
              P = -p * k2
              Q = k1 * q - p * k3
          else:
            P = p
            Q = q
          # Making sure that all divisors P*ni + Q*nj verify the three conditions
          # 1) i < j
          # 2) P >= 0
          # 3) gcd(P, Q) = 1
          # If keplerian is True, then (i,j) = (2,3)
          if P < 0:
            ctb = -ctb
            if not self.takeout_kn:
              ctb = ctb.subst(self.kdotn, -self.kdotn)
            P = -P
            Q = -Q
          if P == 0:
            ctb = ctb / Q
            if not self.takeout_kn:
              ctb = ctb.subst(self.kdotn, Q * self.kdotn)
            Q = 1
          if Q == 0:
            ctb = ctb / P
            if not self.takeout_kn:
              ctb = ctb.subst(self.kdotn, P * self.kdotn)
            P = 1
          gcd = pm.gcd([abs(P), abs(Q)])
          P = P // gcd
          Q = Q // gcd
          ctb = ctb / gcd
          if not self.takeout_kn:
            ctb = ctb.subst(self.kdotn, gcd * self.kdotn)
          if i == 1 and self.keplerian:
            k_dot_n = self._get_k_dot_n(P, Q, (2, 3))
          else:
            k_dot_n = self._get_k_dot_n(P, Q, inner_pair)
          if not self.takeout_kn:
            ctb = ctb.substvars({self.kdotn: k_dot_n})
          ctb = ctb / (mf.i * k_dot_n)  # Chi = H1/(i*k.n)
        ctb = ctb / (
          self.ms[0]
          * self.ms[1]
          / (se.Var('m0') ** 2)
          * self.Lbds[2]
          * self.ns[2]
          * (k1 * self.lbds[0] + k2 * self.lbds[1] + k3 * self.lbds[2]).expi()
        )  # Removing a factor (m1/m0)*(m2/m0)*n3*Lbd3*expi(k1*lbd1 + k2*lbd2 + k3*lbd3)
        H += ctb
    return H

  # Hidden methods
  def _get_Hamiltonian_term(self, p, q):
    # Get the inequality (p, q) in the perturbative part
    # of the Hamiltonian for a pair of planet.
    # A factor G**2*m0*mi*mj**3/Lbdj**2 = G*mi*mj/aj = mi/m0*nj*Lbdj is left out.

    angle = p * self.lbdi + q * self.lbdj
    term = 0

    # Direct part
    coef = self.Hp.direct([p, q])
    coef = coef.subst(self.X1, self.xi * self.sq2Li)
    coef = coef.subst(self.X2, self.xj * self.sq2Lj)
    coef = coef.subst(self.Xb1, self.xbi * self.sq2Li)
    coef = coef.subst(self.Xb2, self.xbj * self.sq2Lj)
    if self.spatial:
      coef = coef.subst(self.Y1, self.yi * self.sq2Li / 2)
      coef = coef.subst(self.Y2, self.yj * self.sq2Lj / 2)
      coef = coef.subst(self.Yb1, self.ybi * self.sq2Li / 2)
      coef = coef.subst(self.Yb2, self.ybj * self.sq2Lj / 2)

    term -= coef * angle.expi()

    # Indirect part
    if not self.disregardInd:
      coef = self.Hp.indirect([p, q])
      coef = coef.subst(self.X1, self.xi * self.sq2Li)
      coef = coef.subst(self.X2, self.xj * self.sq2Lj)
      coef = coef.subst(self.Xb1, self.xbi * self.sq2Li)
      coef = coef.subst(self.Xb2, self.xbj * self.sq2Lj)
      if self.spatial:
        coef = coef.subst(self.Y1, self.yi * self.sq2Li / 2)
        coef = coef.subst(self.Y2, self.yj * self.sq2Lj / 2)
        coef = coef.subst(self.Yb1, self.ybi * self.sq2Li / 2)
        coef = coef.subst(self.Yb2, self.ybj * self.sq2Lj / 2)
      term += 1 / self.sqalp * coef * angle.expi()

    term = se.Series(term)
    return term

  def _d_Lbdi(self, S):
    # Differentiates serie S with respect to Lbdi
    # S can depend on Lbdi, on sq2Li = sqrt(2/Lbdi), on alpha = ai/aj,
    # on sqalp = sqrt(alpha) and on b_s_k(alpha)

    # Derivation with respect to Lbdi
    t1 = S.deriv(self.Lbdi)

    # Derivation with respect to sq2Li
    t2 = S.deriv(self.sq2Li) * (-1 / (self.Lbdi**2 * self.sq2Li))

    # Derivation with respect to alpha
    t3 = S.deriv(self.alpha) * (2 * self.alpha / self.Lbdi)

    # Derivation with respect to sqalp
    t4 = S.deriv(self.sqalp) * (self.sqalp / self.Lbdi)

    # Derivation with respect to b_s^(0) and b_s^(1)
    t5 = 0
    for s in range(1, self.max_s + 1, 2):
      b1 = se.Var(f'b_{s}_1')
      b0 = se.Var(f'b_{s}_0')
      t5 += S.deriv(b0) * lp.formal_deriv_b(s, 0)
      t5 += S.deriv(b1) * lp.formal_deriv_b(s, 1)
    t5 *= 2 * self.alpha / self.Lbdi

    return t1 + t2 + t3 + t4 + t5

  def _d_Lbdj(self, S):
    # Differentiates serie S with respect to Lbdj
    # S can depend on Lbdj, on sq2Lj = sqrt(2/Lbdj), on alpha = ai/aj,
    # on sqalp = sqrt(alpha) and on b_s_k(alpha).

    # Derivation with respect to Lbdj
    t1 = S.deriv(self.Lbdj)

    # Derivation with respect to sq2Lj
    t2 = S.deriv(self.sq2Lj) * (-1 / (self.Lbdj**2 * self.sq2Lj))

    # Derivation with respect to alpha
    t3 = S.deriv(self.alpha) * (-2 * self.alpha / self.Lbdj)

    # Derivation with respect to sqalp
    t4 = S.deriv(self.sqalp) * (-self.sqalp / self.Lbdj)

    # Derivation with respect to b_s^(0) and b_s^(1)
    t5 = 0
    for s in range(1, self.max_s + 1, 2):
      b1 = se.Var(f'b_{s}_1')
      b0 = se.Var(f'b_{s}_0')
      t5 += S.deriv(b0) * lp.formal_deriv_b(s, 0)
      t5 += S.deriv(b1) * lp.formal_deriv_b(s, 1)
    t5 *= -2 * self.alpha / self.Lbdj

    return t1 + t2 + t3 + t4 + t5

  def _generic2actual(self, S, k):
    # The serie S is given with the generic pair (i, j).
    # Variables will be substituted to the actual pair (k1, k2).

    i, j = k
    R = S.substvars(
      {
        self.xi: self.xs[i - 1],
        self.xj: self.xs[j - 1],
        self.xbi: self.xbs[i - 1],
        self.xbj: self.xbs[j - 1],
        self.Lbdi: self.Lbds[i - 1],
        self.Lbdj: self.Lbds[j - 1],
        self.lbdi: self.lbds[i - 1],
        self.lbdj: self.lbds[j - 1],
        self.sq2Li: self.sq2Ls[i - 1],
        self.sq2Lj: self.sq2Ls[j - 1],
        self.alpha: self.alphas[i - 1][j - 1],
        self.sqalp: self.sqalps[i - 1][j - 1],
      }
    )
    if self.spatial:
      R = R.substvars(
        {
          self.yi: self.ys[i - 1],
          self.yj: self.ys[j - 1],
          self.ybi: self.ybs[i - 1],
          self.ybj: self.ybs[j - 1],
        }
      )
    for s in range(1, self.max_s + 1, 2):
      b1 = se.Var(f'b_{s}_1')
      b0 = se.Var(f'b_{s}_0')
      b1_ij = se.Var(f'b{s}1_{i}{j}')
      b0_ij = se.Var(f'b{s}0_{i}{j}')
      R = R.substvars({b1: b1_ij, b0: b0_ij})

    return R

  def _eval_sma(self, S, k):
    # Evaluates the serie S at alpha = a_I/a_J where k = (I, J).
    # The serie S is still relative to the generic pair (i, j)
    # when this function is called.

    I, J = k
    alp = (self.n0[J - 1] / self.n0[I - 1]) ** (2.0 / 3.0)
    sqalpha = (self.n0[J - 1] / self.n0[I - 1]) ** (1.0 / 3.0)
    R = S.evalnum({self.alpha: alp, self.sqalp: sqalpha})
    for s in range(1, self.max_s + 1, 2):
      b1 = se.Var(f'b_{s}_1')
      b0 = se.Var(f'b_{s}_0')
      R = R.evalnum({b0: lp.b(s / 2, 0, alp), b1: lp.b(s / 2, 1, alp)})
    return R

  def _poisson_bracket(self, F, G, kf, kg, tpl):
    # Computes and returns the Poisson bracket {F, G}
    # truncated at order self.degree in eccentricity/inclination.
    # The argument kf = (kf1, kf2) indicates the pair of planets
    # that the serie F is relative to with 1 <= kf1 < kf2 <= 3.
    # The argument kg = (kg1, kg2) indicates the pair of planets
    # that the serie G is relative to with 1 <= kg1 < kg2 <= 3.
    # The series F and G are given with the generic pair (i, j).
    # The returned serie will contain variables subscripted by kf and kg
    # tpl = (p, q, r, s) is such that the bracket is
    # {expi(p*lbd_kf1 + q*lbd_kf2), expi(r*lbd_kg1 + s*lbd_kg2)}.

    fg = 0

    kf1, kf2 = kf
    kg1, kg2 = kg
    rdm = se.Var('random')
    p, q, r, s = tpl
    ecc_order = abs(p + q) + abs(r + s)

    # (Lbdl, lbdl)
    if ecc_order <= self.degree:
      for l in range(1, 4):
        if kf1 == l and kg1 == l:
          dFdL = self._d_Lbdi(F)
          dFdl = F.deriv(self.lbdi)
          dGdL = self._d_Lbdi(G)
          dGdl = G.deriv(self.lbdi)
        elif kf1 == l and kg2 == l:
          dFdL = self._d_Lbdi(F)
          dFdl = F.deriv(self.lbdi)
          dGdL = self._d_Lbdj(G)
          dGdl = G.deriv(self.lbdj)
        elif kf2 == l and kg1 == l:
          dFdL = self._d_Lbdj(F)
          dFdl = F.deriv(self.lbdj)
          dGdL = self._d_Lbdi(G)
          dGdl = G.deriv(self.lbdi)
        elif kf2 == l and kg2 == l:
          dFdL = self._d_Lbdj(F)
          dFdl = F.deriv(self.lbdj)
          dGdL = self._d_Lbdj(G)
          dGdl = G.deriv(self.lbdj)
        else:
          dFdL = rdm
          dFdl = rdm
          dGdL = rdm
          dGdl = rdm
        if dFdL != rdm:
          if self.spatial:
            se.settrunc(
              [
                self.xs[0],
                self.xs[1],
                self.xs[2],
                self.xbs[0],
                self.xbs[1],
                self.xbs[2],
                self.ys[0],
                self.ys[1],
                self.ys[2],
                self.ybs[0],
                self.ybs[1],
                self.ybs[2],
              ],
              self.degree,
            )
          else:
            se.settrunc(
              [
                self.xs[0],
                self.xs[1],
                self.xs[2],
                self.xbs[0],
                self.xbs[1],
                self.xbs[2],
              ],
              self.degree,
            )
          if not self.takeout_kn:  # Deriving denominator k.n with respect to Lambda
            if self.ev:
              if kf1 == l:
                if p != 0:
                  dFdL += (
                    3.0
                    / (1.0 + q * self.n0[kf2 - 1] / (p * self.n0[kf1 - 1]))
                    * F
                    / self.Lbdi
                  )
              else:
                if q != 0:
                  dFdL += (
                    3.0
                    / (1.0 + p * self.n0[kf1 - 1] / (q * self.n0[kf2 - 1]))
                    * F
                    / self.Lbdj
                  )
            else:
              if kf1 == l:
                dFdL += 3 * (p * self.ns[kf1 - 1] / self.kdotn) * F / self.Lbdi
              else:
                dFdL += 3 * (q * self.ns[kf2 - 1] / self.kdotn) * F / self.Lbdj
          if self.ev:
            dFdL = self._eval_sma(dFdL, kf)
            dFdl = self._eval_sma(dFdl, kf)
            dGdL = self._eval_sma(dGdL, kg)
            dGdl = self._eval_sma(dGdl, kg)
          dFdL = self._generic2actual(dFdL, kf)
          dFdl = self._generic2actual(dFdl, kf)
          dGdL = self._generic2actual(dGdL, kg)
          dGdl = self._generic2actual(dGdl, kg)
          fg += dFdL * dGdl - dFdl * dGdL
          se.unsettrunc()
    # (xl, xbl)
    for l in range(1, 4):
      if kf1 == l and kg1 == l:
        dFdx = F.deriv(self.xi)
        dFdxb = F.deriv(self.xbi)
        dGdx = G.deriv(self.xi)
        dGdxb = G.deriv(self.xbi)
      elif kf1 == l and kg2 == l:
        dFdx = F.deriv(self.xi)
        dFdxb = F.deriv(self.xbi)
        dGdx = G.deriv(self.xj)
        dGdxb = G.deriv(self.xbj)
      elif kf2 == l and kg1 == l:
        dFdx = F.deriv(self.xj)
        dFdxb = F.deriv(self.xbj)
        dGdx = G.deriv(self.xi)
        dGdxb = G.deriv(self.xbi)
      elif kf2 == l and kg2 == l:
        dFdx = F.deriv(self.xj)
        dFdxb = F.deriv(self.xbj)
        dGdx = G.deriv(self.xj)
        dGdxb = G.deriv(self.xbj)
      else:
        dFdx = rdm
        dFdxb = rdm
        dGdx = rdm
        dGdxb = rdm
      if dFdx != rdm:
        if self.spatial:
          se.settrunc(
            [
              self.xs[0],
              self.xs[1],
              self.xs[2],
              self.xbs[0],
              self.xbs[1],
              self.xbs[2],
              self.ys[0],
              self.ys[1],
              self.ys[2],
              self.ybs[0],
              self.ybs[1],
              self.ybs[2],
            ],
            self.degree,
          )
        else:
          se.settrunc(
            [self.xs[0], self.xs[1], self.xs[2], self.xbs[0], self.xbs[1], self.xbs[2]],
            self.degree,
          )
        if self.ev:
          dFdx = self._eval_sma(dFdx, kf)
          dFdxb = self._eval_sma(dFdxb, kf)
          dGdx = self._eval_sma(dGdx, kg)
          dGdxb = self._eval_sma(dGdxb, kg)
        dFdx = self._generic2actual(dFdx, kf)
        dFdxb = self._generic2actual(dFdxb, kf)
        dGdx = self._generic2actual(dGdx, kg)
        dGdxb = self._generic2actual(dGdxb, kg)
        fg += mf.i * (dFdx * dGdxb - dFdxb * dGdx)
        se.unsettrunc()
    # (yl, ybl)
    if self.spatial:
      for l in range(1, 4):
        if kf1 == l and kg1 == l:
          dFdy = F.deriv(self.yi)
          dFdyb = F.deriv(self.ybi)
          dGdy = G.deriv(self.yi)
          dGdyb = G.deriv(self.ybi)
        elif kf1 == l and kg2 == l:
          dFdy = F.deriv(self.yi)
          dFdyb = F.deriv(self.ybi)
          dGdy = G.deriv(self.yj)
          dGdyb = G.deriv(self.ybj)
        elif kf2 == l and kg1 == l:
          dFdy = F.deriv(self.yj)
          dFdyb = F.deriv(self.ybj)
          dGdy = G.deriv(self.yi)
          dGdyb = G.deriv(self.ybi)
        elif kf2 == l and kg2 == l:
          dFdy = F.deriv(self.yj)
          dFdyb = F.deriv(self.ybj)
          dGdy = G.deriv(self.yj)
          dGdyb = G.deriv(self.ybj)
        else:
          dFdy = rdm
          dFdyb = rdm
          dGdy = rdm
          dGdyb = rdm
        if dFdy != rdm:
          se.settrunc(
            [
              self.xs[0],
              self.xs[1],
              self.xs[2],
              self.xbs[0],
              self.xbs[1],
              self.xbs[2],
              self.ys[0],
              self.ys[1],
              self.ys[2],
              self.ybs[0],
              self.ybs[1],
              self.ybs[2],
            ],
            self.degree,
          )
          if self.ev:
            dFdy = self._eval_sma(dFdy, kf)
            dFdyb = self._eval_sma(dFdyb, kf)
            dGdy = self._eval_sma(dGdy, kg)
            dGdyb = self._eval_sma(dGdyb, kg)
          dFdy = self._generic2actual(dFdy, kf)
          dFdyb = self._generic2actual(dFdyb, kf)
          dGdy = self._generic2actual(dGdy, kg)
          dGdyb = self._generic2actual(dGdyb, kg)
          fg += mf.i * (dFdy * dGdyb - dFdyb * dGdy)
          se.unsettrunc()
    if fg == 0:
      print(
        f'Warning : {{expi({p}*lbd{kf1} + {q}*lbd{kf2}), '
        f'expi({r}*lbd{kg1} + {s}*lbd{kg2})}} = 0 in function _poisson_bracket'
      )
    return fg

  def _get_brackets_for_3pla_angle(self, angle, pairs):
    # With angle = (k1, k2, k3) and pairs = ((i, j), (I, J)), this function
    # returns a list of 4-tuple
    # [(p1, q1, r1, s1), (p2, q2, r2, s2), ..., (pN, qN, rN, sN)],
    # such that, for 1 <= k <= N,
    # the Poisson bracket {expi(pk*lbdi + qk*lbdj), expi(rk*lbdI + sk*lbdJ)}
    # is relevant for the 3-planet angle k1*lbd1 + k2*lbd2 + k3*lbd3.
    # A bracket is deemed relevant if :
    # - It makes the 3-planet angle appear, that is,
    #   pk*lbdi + qk*lbdj + rk*lbdI + sk*lbdJ = k1*lbd1 + k2*lbd2 + k3*lbd3,
    # - It is of degree self.degree or less in eccentricity/inclination.

    out = []
    inner_pair, outer_pair = pairs
    i, j = inner_pair
    I, J = outer_pair
    k1, k2, k3 = angle
    d = self.degree + 1

    if i + j + I + J == 7:
      if j == 2:
        q = k2
        s = k3
      else:
        s = k2
        q = k3
      for p in range(-q - d, -q + d + 1):
        r = k1 - p
        ecc_order = abs(p + q) + abs(r + s)
        if p + q != 0 and r + s != 0:
          # Can Poisson bracket with respect to (x, xb) or (y, yb)
          # allowing the eccentricity/inclination order to be decreased by 2
          ecc_order = ecc_order - 2
        if abs(p + q) <= d and abs(r + s) <= d and ecc_order <= self.degree:
          out.append((p, q, r, s))
    elif i + j + I + J == 9:
      if i == 1:
        p = k1
        r = k2
      else:
        p = k2
        r = k1
      for q in range(-p - d, -p + d + 1):
        s = k3 - q
        ecc_order = abs(p + q) + abs(r + s)
        if p + q != 0 and r + s != 0:
          ecc_order = ecc_order - 2
        if abs(p + q) <= d and abs(r + s) <= d and ecc_order <= self.degree:
          out.append((p, q, r, s))
    elif i + j + I + J == 8:
      if i == 1:
        p = k1
        s = k3
        for q in range(-p - d, -p + d + 1):
          r = k2 - q
          ecc_order = abs(p + q) + abs(r + s)
          if p + q != 0 and r + s != 0:
            ecc_order = ecc_order - 2
          if abs(p + q) <= d and abs(r + s) <= d and ecc_order <= self.degree:
            out.append((p, q, r, s))
      else:
        q = k3
        r = k1
        for p in range(-q - d, -q + d + 1):
          s = k2 - p
          ecc_order = abs(p + q) + abs(r + s)
          if p + q != 0 and r + s != 0:
            ecc_order = ecc_order - 2
          if abs(p + q) <= d and abs(r + s) <= d and ecc_order <= self.degree:
            out.append((p, q, r, s))

    # Excluding 2-planet angles that should not be averaged upon
    if self.ang2pla != []:
      buff = []
      for tpl in out:
        buff.append(tpl)
      for tpl1 in self.ang2pla:
        ik, jk, pk, qk = tpl1
        if ik == i and jk == j:
          for tpl2 in out:
            p, q, r, s = tpl2
            for K in range(1, self.degree + 2):
              if (K * pk == p and K * qk == q) or (-K * pk == p and -K * qk == q):
                buff.remove(tpl2)
      out = buff
    return out

  def _get_k_dot_n(self, p, q, inner_pair):
    # Returns a variable whose name represents k.n with k = (p, q)
    # and inner_pair = (i, j).

    i, j = inner_pair
    if p == 0 and q == 1:
      return se.Var(f'n{j}')
    elif p == 1 and q == 0:
      return se.Var(f'n{i}')
    elif p == 1 and q == 1:
      return se.Var(f'(n{i} + n{j})')
    elif p == 1 and q == -1:
      return se.Var(f'(n{i} - n{j})')
    elif p == 1 and q > 1:
      return se.Var(f'(n{i} + {q}*n{j})')
    elif p > 1 and q == 1:
      return se.Var(f'({p}*n{i} + n{j})')
    elif p == 1 and q < -1:
      return se.Var(f'(n{i} - {-q}*n{j})')
    elif p > 1 and q == -1:
      return se.Var(f'({p}*n{i} - n{j})')
    elif p > 0 and q > 0:
      return se.Var(f'({p}*n{i} + {q}*n{j})')
    elif p > 0 and q < 0:
      return se.Var(f'({p}*n{i} - {-q}*n{j})')
    else:
      raise Exception('Error in function _get_k_dot_n')
