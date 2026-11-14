:navigation: footer
:nav_title: Glossary

.. _glossary:

========
Glossary
========

Algebraic definitions and quadratic invariants referenced across the 28
principles of the **GEOMETOR Wildberger** codex.

.. glossary::
   :sorted:

   quadrance
      The exact quadratic separation :math:`Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2` (or :math:`(A_2 - A_1)^T M (A_2 - A_1)` under a general symmetric bilinear form :math:`M`), replacing irrational Euclidean distance over any field :math:`F` (:math:`\operatorname{char} F \neq 2`).

   spread
      The algebraic separation :math:`s(\ell_1, \ell_2) = (a_1 b_2 - a_2 b_1)^2 / ((a_1^2 + b_1^2)(a_2^2 + b_2^2))` between two unoriented non-null lines (equal to :math:`\sin^2\theta` over :math:`\mathbb{R}`), vanishing when parallel and equaling :math:`1` when perpendicular.

   cross
      The complementary line invariant :math:`c(\ell_1, \ell_2) = 1 - s(\ell_1, \ell_2) = (a_1 a_2 + b_1 b_2)^2 / ((a_1^2 + b_1^2)(a_2^2 + b_2^2))` (equal to :math:`\cos^2\theta` over :math:`\mathbb{R}`).

   twist
      The ratio :math:`t(\ell_1, \ell_2) = s(\ell_1, \ell_2) / c(\ell_1, \ell_2)` for two non-perpendicular non-null lines (equal to :math:`\tan^2\theta` over :math:`\mathbb{R}`).

   turn
      The signed rational tangent :math:`u(\ell_1, \ell_2) = (a_1 b_2 - a_2 b_1)/(a_1 a_2 + b_1 b_2)` between two ordered lines, whose square is the twist :math:`t = u^2` and which satisfies :math:`u_1 + u_2 + u_3 = u_1 u_2 u_3`.

   null line
   isotropic line
      A line :math:`\langle a : b : c \rangle` whose quadratic norm :math:`a^2 + b^2` (or :math:`Q_M(u)`) vanishes, occurring in Euclidean geometry over fields containing :math:`\sqrt{-1}` (such as :math:`\mathbb{F}_{13}`) and along light cones in Red/Green relativistic metrics.

   quadrea
   Archimedes' function
      The symmetric quadratic polynomial :math:`\mathcal{A}(Q_1, Q_2, Q_3) = (Q_1 + Q_2 + Q_3)^2 - 2(Q_1^2 + Q_2^2 + Q_3^2)` of a triangle's side quadrances, equal to :math:`16 \Delta^2` over :math:`\mathbb{R}`.

   Triple Quad Formula
      Law II of Rational Trigonometry: three points with pairwise quadrances :math:`Q_1, Q_2, Q_3` are collinear if and only if :math:`\mathcal{A}(Q_1, Q_2, Q_3) = 0`.

   Spread Law
      Law III of Rational Trigonometry: in any non-null triangle, :math:`s_1 / Q_1 = s_2 / Q_2 = s_3 / Q_3 = 1 / (4 K)`.

   Cross Law
      Law IV of Rational Trigonometry: :math:`(Q_1 + Q_2 - Q_3)^2 = 4 Q_1 Q_2 (1 - s_3) = 4 Q_1 Q_2 c_3`, replacing the Law of Cosines without angle-sign ambiguity.

   Triple Spread Formula
      Law V of Rational Trigonometry: three coplanar non-null lines have pairwise spreads satisfying :math:`(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3`.

   Quadruple Quad Formula
      The symmetric degree-4 relation :math:`Q(a, b, c, d) = ((a+b+c+d)^2 - 2(a^2+b^2+c^2+d^2))^2 - 64 a b c d = 0` satisfied by sequential quadrances of four collinear points.

   Quadruple Spread Formula
      The degree-8 self-dual polynomial relation :math:`R(s_{12}, s_{23}, s_{34}, s_{14}) = 0` governing four coplanar lines, identically invariant under :math:`s_{ij} \leftrightarrow 1 - s_{ij}`.

   spread polynomial
   spread polynomials
      Wildberger's universal integer-coefficient polynomial family :math:`S_n(s) \in \mathbb{Z}[s]` satisfying :math:`S_0(s) = 0`, :math:`S_1(s) = s`, :math:`S_n(s) = 2(1 - 2s)S_{n-1}(s) - S_{n-2}(s) + 2s`, and semigroup composition :math:`S_n(S_m(s)) = S_{nm}(s)`.

   Pentagonal spread
   Pentagonal spreads
      The two golden roots :math:`\alpha = (5 - \sqrt{5})/8 = (3 - \phi)/4` and :math:`\beta = (5 + \sqrt{5})/8 = (2 + \phi)/4` of :math:`S_5(s)/s = (16 s^2 - 20 s + 5)^2 = 0`, with exact ratio :math:`\beta / \alpha = \phi^2`.

   golden ratio
   divine proportion
      The positive root :math:`\phi = (1 + \sqrt{5})/2` of :math:`\phi^2 = \phi + 1`, governing Kepler's Golden Right Triangle (:ref:`W.11 <w-11>`), pentagonal spreads (:ref:`W.19 <w-19>`), and icosahedral/dodecahedral coordinates (:ref:`W.27 <w-27>`).

   vertex bisector
   square vertex
      A line of equal quadrance :math:`Q(X, \ell_1) = Q(X, \ell_2)` to two intersecting lines; exists over :math:`F` iff the vertex is a *square vertex* where :math:`(a_1^2 + b_1^2)(a_2^2 + b_2^2)` is a square in :math:`F`.

   incenter
   inquadrance
      One of the four symmetric points :math:`I_0, I_1, I_2, I_3` equidistant in quadrance (:math:`R_i`) from all three sidelines of a triangle whose vertices are square over :math:`F`.

   centroid
      The affine, metric-independent center :math:`G = (A_1 + A_2 + A_3)/3` (:math:`X(2)` when :math:`\operatorname{char} F \neq 3`) where the three medians and all three Chromogeometry Euler lines concur.

   circumcenter
   circumquadrance
      The unique intersection :math:`C` (:math:`X(3)`) of the side perpendicular bisectors of a non-null triangle, having equal quadrance :math:`K = Q_1 Q_2 Q_3 / \mathcal{A}` (*circumquadrance*) to all three vertices.

   orthocenter
      The unique intersection :math:`O` (:math:`X(4)`) of the three altitudes of a non-null triangle.

   nine-point circle
      The universal circle centered at :math:`N = (C + O)/2` (:math:`X(5)`) of quadrance :math:`K_9 = K / 4` passing through the three side midpoints, three altitude feet, and three Euler midpoints.

   Stewart's theorem
      The exact quadratic cevian identity relating :math:`Q(A_3, D)` for any point :math:`D` on :math:`A_1 A_2` to the side quadrances :math:`Q_1, Q_2, Q_3` and segment quadrances on :math:`A_1 A_2`.

   ribbon
      The degree-2 conic locus :math:`Q(X, \ell) = R` of points having constant quadrance :math:`R` to a fixed non-null line.

   parabola
      The metrical conic locus :math:`Q(X, F_0) = Q(X, \ell_{\text{dir}})` of points equidistant in quadrance from a focus :math:`F_0` and a non-null directrix :math:`\ell_{\text{dir}}`.

   quadrola
      Wildberger's irreducible bifocal conic :math:`\mathcal{A}(Q(X, F_1), Q(X, F_2), S) = 0`, unifying classical ellipses (:math:`S > Q(F_1, F_2)`) and hyperbolas (:math:`0 < S < Q(F_1, F_2)`) into one algebraic curve.

   grammola
      The metrical conic locus :math:`Q(X, \ell_1) \pm Q(X, \ell_2) = R` relative to two non-null lines.

   Chromogeometry
      Wildberger's triality of planar geometries acting on the same coordinates: Blue Euclidean (:math:`\Delta x^2 + \Delta y^2`), Red Minkowski (:math:`\Delta x^2 - \Delta y^2`), and Green hyperbolic (:math:`2 \Delta x \Delta y`).

   Hansen's problem
      Peter Andreas Hansen's 1841 geodetic problem of determining all quadrances among two known landmarks :math:`A, B` and two unmeasured observer stations :math:`C, D` from baseline :math:`Q(A, B)` and four spreads at :math:`C, D`.

   dihedral spread
      The spread :math:`S(\Pi_1, \Pi_2) = 1 - (n_1 \cdot n_2)^2 / ((n_1 \cdot n_1)(n_2 \cdot n_2))` between two planes in 3D space, equal to pure rationals :math:`(8/9, 1, 8/9, 4/9, 4/5)` across all five Platonic solids.

   ellipson
      The compact cubic algebraic surface inside :math:`[0, 1]^3` defined by the Triple Spread Formula :math:`(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3`.
