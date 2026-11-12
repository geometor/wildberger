"""Catalog definitions for Principles `W.01` through `W.14` (Parts I, II & early III).

Covers foundational planar line proportions, reflections, quadrance, spread,
spread polynomials (including Pentagonal Golden Spreads), the Five Fundamental
Laws of Rational Trigonometry, Kepler's Golden Right Triangle, vertex bisectors
and incenters, Stewart's/median laws, and Menelaus/Ceva quadrance theorems.
"""

from __future__ import annotations

from geometor.wildberger.catalog import PrincipleSpec

PART_I = "Part I: Preliminaries & Foundational Invariants"
PART_II = "Part II: The Five Fundamental Laws"
PART_III = "Part III: Universal Triangle, Conic & Chromogeometry"

PRINCIPLES_A: tuple[PrincipleSpec, ...] = (
    PrincipleSpec(
        num=1,
        code="W.01",
        slug="w-01",
        part=PART_I,
        category="Affine & Projective Incidence",
        tags=("proportions", "lines", "determinants", "collinearity", "concurrency", "altitude"),
        title="Planar Points, Line Proportions & Incidence Determinants",
        subtitle="Field-Independent Coordinate Incidence, Parallels, and Altitudes",
        enunciation=(
            "Over any field F of characteristic not equal to 2, a planar point is an ordered pair "
            "A = [x, y] and a planar line is a homogeneous 3-proportion l = <a : b : c> with (a, b) != (0, 0) "
            "representing a*x + b*y + c = 0; three points are collinear and three lines are concurrent "
            "if and only if their respective 3x3 coordinate determinants vanish."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "l_3 = line(A_1, A_2)",
            "p_3 = parallel(l_3, A_3)",
            "n_3 = altitude(l_3, A_3)",
            "F_3 = meet(l_3, n_3)",
        ),
        synthesis=(
            "In :person:`Norman J. Wildberger <wildberger>`'s algebraic foundation (:cite:`Wildberger2005`), "
            "classical continuum postulates are replaced by arithmetic over an arbitrary field :math:`F` "
            "(:math:`\\operatorname{char} F \\neq 2`). Two distinct points :g:`A_1` :math:`= [x_1, y_1]` and "
            ":g:`A_2` :math:`= [x_2, y_2]` determine a unique line proportion "
            ":g:`l_3` :math:`= \\langle y_1 - y_2 : x_2 - x_1 : x_1 y_2 - x_2 y_1 \\rangle`, while two "
            "non-parallel lines meet at a unique rational point given by Cramer's determinant ratios.",
            "Parallelism (:math:`a_1 b_2 - a_2 b_1 = 0`) and Euclidean perpendicularity "
            "(:math:`a_1 a_2 + b_1 b_2 = 0`) are purely polynomial conditions. Given an external point "
            ":g:`A_3` and a non-:term:`null line` :g:`l_3`, both the parallel line :g:`p_3` and the altitude "
            ":g:`n_3` meeting :g:`l_3` at its foot :g:`F_3` are obtained by exact rational expressions without "
            "square roots or compass arcs—bridging :person:`René Descartes <descartes>`' coordinate algebra "
            "directly to projective incidence in ``geometor/pappus``.",
        ),
        math_blocks=(
            r"\ell(A_1, A_2) = \langle y_1 - y_2 : x_2 - x_1 : x_1 y_2 - x_2 y_1 \rangle, \qquad "
            r"\ell_1 \cap \ell_2 = \left[\frac{b_1 c_2 - b_2 c_1}{a_1 b_2 - a_2 b_1},\; "
            r"\frac{a_2 c_1 - a_1 c_2}{a_1 b_2 - a_2 b_1}\right]",
            r"F_3 = \left[\frac{b^2 x_3 - a b y_3 - a c}{a^2 + b^2},\; "
            r"\frac{-a b x_3 + a^2 y_3 - b c}{a^2 + b^2}\right], \qquad "
            r"\det\begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{pmatrix} = 0",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.11`, :ref:`I.12`, :ref:`I.31` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.1`, :ref:`G.3`, :ref:`G.4`"),
            ("GEOMETOR Fundamentals", ":ref:`F.14 Conway Notation <f-14>` (:cite:`SeeligNotebooks`)"),
            ("Sister Codices", "``geometor/pappus`` (projective collinearity & concurrency determinants)"),
        ),
        depends_on=(),
    ),
    PrincipleSpec(
        num=2,
        code="W.02",
        slug="w-02",
        part=PART_I,
        category="Isometries & Lineations",
        tags=("reflections", "rotations", "lineations", "symmetry", "isometries"),
        title="Lineations, Central Rotations & Reflections in Lines",
        subtitle="Square-Root-Free Point and Line Reflections Across Arbitrary Non-Null Axes",
        enunciation=(
            "For any non-null line l = <a : b : c> over a field F (char F != 2), the reflection sigma_l "
            "maps every point A = [x, y] and every line m = <a_2 : b_2 : c_2> to exact rational images "
            "whose denominators depend only on the quadratic norm a^2 + b^2, without radicals or angles."
        ),
        signature_given=(
            "P_1 : Point",
            "P_2 : Point",
            "A : Point",
            "B : Point",
        ),
        signature_steps=(
            "l = line(P_1, P_2)",
            "F = foot(A, l)",
            "A_r = reflect_point(A, l)",
            "m = line(A, B)",
            "m_r = reflect_line(m, l)",
        ),
        synthesis=(
            "Classical orthogonal reflection across an oblique axis typically invokes unit normal vectors "
            "containing :math:`\\sqrt{a^2 + b^2}` or trigonometric double-angle matrices. In Universal "
            "Geometry (:cite:`Wildberger2005`, :cite:`SnapperTroyer1971`), because the foot :g:`F` of the "
            "altitude from :g:`A` to :g:`l` is rational in :math:`(a, b, c)`, the reflected point :g:`A_r` "
            ":math:`= 2 F - A` is **always rational** over the ground field :math:`F`!",
            "Even more remarkably, reflecting an entire line :g:`m` across :g:`l` produces the reflected "
            "line :g:`m_r` :math:`= \\Sigma_l(m)` via homogeneous quadratic polynomials in :math:`(a, b)`. "
            "Iterating line reflections generates cyclic reflection sequences that directly govern "
            ":term:`spread polynomials` and regular star symmetries over both :math:`\\mathbb{Q}` and finite fields.",
        ),
        math_blocks=(
            r"\sigma_\ell([x, y]) = \left[\frac{(b^2 - a^2)x - 2 a b y - 2 a c}{a^2 + b^2},\; "
            r"\frac{-2 a b x + (a^2 - b^2)y - 2 b c}{a^2 + b^2}\right]",
            r"\Sigma_\ell(\langle a_2 : b_2 : c_2 \rangle) = \langle (a^2 - b^2)a_2 + 2 a b b_2 :\; "
            r"2 a b a_2 - (a^2 - b^2)b_2 :\; 2 c(a a_2 + b b_2) - (a^2 + b^2)c_2 \rangle",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.9`, :ref:`I.10`, :ref:`I.12` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`"),
            ("GEOMETOR Fundamentals", ":ref:`F.5 Centers of Similitude <f-05>`"),
            ("Metric Affine Canon", ":cite:`SnapperTroyer1971` (Orthogonal reflections over general fields)"),
        ),
        depends_on=("W.01",),
    ),
    PrincipleSpec(
        num=3,
        code="W.03",
        slug="w-03",
        part=PART_I,
        category="Foundational Quadratic Invariants",
        tags=("quadrance", "midpoint", "parallelogram", "perpendicular bisector", "null line"),
        title="Quadrance, Midpoints & Point-to-Line Separation",
        subtitle="Replacing Irrational Euclidean Distance with Exact Quadratic Point Separation",
        enunciation=(
            "The quadrance between A_1 = [x_1, y_1] and A_2 = [x_2, y_2] is the quadratic form "
            "Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2; midpoint M divides the quadrance by 4, "
            "the locus Q(X, A_1) = Q(X, A_2) is the linear perpendicular bisector, and the quadrance "
            "from A_0 to a non-null line l = <a : b : c> is (a*x_0 + b*y_0 + c)^2 / (a^2 + b^2)."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_0 : Point",
        ),
        signature_steps=(
            "l = line(A_1, A_2)",
            "M = midpoint(A_1, A_2)",
            "b_12 = perp_bisector(A_1, A_2)",
            "F_0 = foot(A_0, l)",
        ),
        synthesis=(
            ":term:`Quadrance` is the primary point-separation invariant of Rational Trigonometry "
            "(:cite:`Wildberger2005`). Because :math:`Q(A_1, A_2)` avoids square roots, points in "
            ":math:`F^2` always have separation in :math:`F`. Scaling a displacement by :math:`\\lambda` "
            "multiplies its quadrance by :math:`\\lambda^2`, so the midpoint :g:`M` of :g:`A_1` and :g:`A_2` "
            "satisfies :math:`Q(A_1, M) = Q(M, A_2) = Q(A_1, A_2)/4`.",
            "Equating quadrances :math:`Q(X, A_1) = Q(X, A_2)` cancels the quadratic terms :math:`x^2 + y^2`, "
            "yielding the linear perpendicular bisector :g:`b_12` even when :math:`Q(A_1, A_2)` is not a "
            "square in :math:`F`! Similarly, the quadrance from an external point :g:`A_0` to line :g:`l` "
            "equals :math:`Q(A_0, F_0)`, and in any parallelogram the diagonal quadrances sum to twice "
            "the sum of adjacent side quadrances. Over fields where :math:`-1 = i^2` (such as :math:`\\mathbb{F}_{13}` "
            "with :math:`5^2 \\equiv -1`), non-coincident points along a :term:`null line` satisfy :math:`Q(A_1, A_2) = 0`.",
        ),
        math_blocks=(
            r"Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2, \qquad "
            r"Q(A_1, M) = Q(M, A_2) = \frac{Q(A_1, A_2)}{4}",
            r"Q(A_0, \ell) = \frac{(a x_0 + b y_0 + c)^2}{a^2 + b^2}, \qquad "
            r"Q_{13} + Q_{24} = 2(Q_{12} + Q_{23})",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.10`, :ref:`I.47`, :ref:`II.4` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.1`, :ref:`G.3`"),
            ("GEOMETOR Fundamentals", ":ref:`F.9 Circle Equations <f-09>`"),
            ("Sister Codices", "``geometor/model`` (exact polynomial distance/quadrance algebra)"),
        ),
        depends_on=("W.01",),
    ),
    PrincipleSpec(
        num=4,
        code="W.04",
        slug="w-04",
        part=PART_I,
        category="Foundational Quadratic Invariants",
        tags=("spread", "cross", "twist", "turn", "complementary spreads"),
        title="Spread, Cross, Twist & Line Separation Ratios",
        subtitle="Algebraic Separation of Unoriented Lines Replacing Transcendental Angle",
        enunciation=(
            "For two non-null lines l_1 = <a_1 : b_1 : c_1> and l_2 = <a_2 : b_2 : c_2>, the spread "
            "s(l_1, l_2) = (a_1*b_2 - a_2*b_1)^2 / ((a_1^2 + b_1^2)*(a_2^2 + b_2^2)) depends only on "
            "the unoriented lines, vanishes iff l_1 || l_2, equals 1 iff l_1 perp l_2, and equals "
            "Q(B, C) / Q(A, B) for any altitude BC dropped from B on l_1 to C on l_2."
        ),
        signature_given=(
            "A : Point",
            "B : Point",
            "P_2 : Point",
        ),
        signature_steps=(
            "l_1 = line(A, B)",
            "l_2 = line(A, P_2)",
            "C = foot(B, l_2)",
            "n_bc = segment(B, C)",
        ),
        synthesis=(
            "Classical angle requires circular arc-length integration, ray orientation, and :math:`\\pi` "
            "ambiguities across eight possible arcs at an intersection. :person:`Norman J. Wildberger <wildberger>` "
            "replaces angle with :term:`spread` :math:`s(\\ell_1, \\ell_2) \\in F` (:cite:`Wildberger2005`): "
            "if :g:`l_1` and :g:`l_2` intersect at :g:`A`, choosing any point :g:`B` :math:`\\neq A` on :g:`l_1` "
            "and dropping altitude :g:`n_bc` to its foot :g:`C` on :g:`l_2` yields the invariant ratio "
            ":math:`s(\\ell_1, \\ell_2) = Q(B, C) / Q(A, B)`.",
            "Paired with spread are the :term:`cross` :math:`c(\\ell_1, \\ell_2) = 1 - s(\\ell_1, \\ell_2) = Q(A, C)/Q(A, B)` "
            "and the :term:`twist` :math:`t(\\ell_1, \\ell_2) = s / c = Q(B, C)/Q(A, C)`, which squares the "
            "signed :term:`turn` :math:`u(\\ell_1, \\ell_2)`. Supplementary angles share the **exact same line**, "
            "so supplementary spreads are identical, while orthogonal lines swap spread and cross "
            "(:math:`s \\leftrightarrow 1 - s`).",
        ),
        math_blocks=(
            r"s(\ell_1, \ell_2) = \frac{(a_1 b_2 - a_2 b_1)^2}{(a_1^2 + b_1^2)(a_2^2 + b_2^2)} = \frac{Q(B, C)}{Q(A, B)}, "
            r"\qquad c(\ell_1, \ell_2) = 1 - s(\ell_1, \ell_2) = \frac{(a_1 a_2 + b_1 b_2)^2}{(a_1^2 + b_1^2)(a_2^2 + b_2^2)}",
            r"t(\ell_1, \ell_2) = \frac{s(\ell_1, \ell_2)}{c(\ell_1, \ell_2)} = u(\ell_1, \ell_2)^2, \qquad "
            r"\ell_3 \perp \ell_2 \implies s(\ell_1, \ell_3) = 1 - s(\ell_1, \ell_2)",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.11`, :ref:`I.13`, :ref:`VI.4` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.5`"),
            ("GEOMETOR Fundamentals", ":ref:`F.14 Conway Notation <f-14>`"),
            ("Sister Codices", "``geometor/divine`` (exact algebraic ratios without floating-point trig)"),
        ),
        depends_on=("W.01", "W.03"),
    ),
    PrincipleSpec(
        num=5,
        code="W.05",
        slug="w-05",
        part=PART_I,
        category="Polynomial Families & Golden Proportion",
        tags=("spread polynomials", "Chebyshev", "logistic map", "golden ratio", "pentagon"),
        title="Spread Polynomials S_n(s) & Pentagonal Golden Spreads",
        subtitle="Universal Chebyshev Analogues, Semigroup Composition, and Exact Golden Roots",
        enunciation=(
            "The integer-coefficient spread polynomials S_0(s) = 0, S_1(s) = s, "
            "S_n(s) = 2(1 - 2s)S_{n-1}(s) - S_{n-2}(s) + 2s satisfy the semigroup composition law "
            "S_n(S_m(s)) = S_{nm}(s) over every commutative ring, and the fivefold polynomial "
            "S_5(s) = s(16s^2 - 20s + 5)^2 vanishes precisely at the Pentagonal Golden Spreads "
            "s = (5 -/+ sqrt(5))/8 = (3 - phi)/4 and (2 + phi)/4."
        ),
        signature_given=(
            "O : Point",
            "V_0 : Point",
            "V_1 : Point",
        ),
        signature_steps=(
            "l_0 = line(O, V_0)",
            "l_1 = line(O, V_1)",
            "l_2 = reflect_line(l_0, l_1)",
            "l_3 = reflect_line(l_1, l_2)",
            "l_4 = reflect_line(l_2, l_3)",
        ),
        synthesis=(
            "Reflecting a line :g:`l_0` successively across :g:`l_1` to form a fan of equally spread lines "
            ":math:`\\ell_0, \\ell_1, \\ell_2, \\dots` with :math:`s(\\ell_k, \\ell_{k+1}) = s` produces "
            ":math:`s(\\ell_0, \\ell_n) = S_n(s)`, where :math:`S_n(s) \\in \\mathbb{Z}[s]` is the :math:`n`-th "
            ":term:`spread polynomial` (:cite:`Wildberger2005`). Over :math:`\\mathbb{R}`, :math:`S_n(\\sin^2\\theta) = \\sin^2(n\\theta)` "
            "rescales :person:`Pafnuty Chebyshev <chebyshev>`'s polynomials, while :math:`S_2(s) = 4s(1-s)` is the "
            "maximal logistic map and :math:`S_n(S_m(s)) = S_{nm}(s)` forms a commutative polynomial semigroup!",
            "Where Rational Trigonometry meets **GEOMETOR's Divine Proportion** (:math:`\\phi = \\frac{1+\\sqrt{5}}{2}`) "
            "is in :math:`S_5(s) = s(16s^2 - 20s + 5)^2 = 0`: its non-zero roots are the two :term:`Pentagonal spread` "
            "constants :math:`\\alpha = \\frac{5 - \\sqrt{5}}{8} = \\frac{3 - \\phi}{4}` and "
            ":math:`\\beta = \\frac{5 + \\sqrt{5}}{8} = \\frac{2 + \\phi}{4}`, whose ratio is "
            ":math:`\\beta / \\alpha = \\phi^2 = \\phi + 1`! Over :math:`\\mathbb{F}_{19}` (where :math:`9^2 \\equiv 5`), "
            "these roots reduce to exact residues :math:`s \\equiv 9, 16 \\pmod{19}`.",
        ),
        math_blocks=(
            r"S_0(s) = 0, \quad S_1(s) = s, \quad S_2(s) = 4s(1-s), \quad S_3(s) = s(3 - 4s)^2, \quad "
            r"S_n(S_m(s)) = S_{nm}(s)",
            r"S_5(s) = s(16s^2 - 20s + 5)^2 = 0 \iff s \in \left\{0,\; "
            r"\alpha = \frac{5 - \sqrt{5}}{8} = \frac{3 - \phi}{4},\; "
            r"\beta = \frac{5 + \sqrt{5}}{8} = \frac{2 + \phi}{4}\right\}",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`IV.11`, :ref:`XIII.8` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.12`, :ref:`G.15` (Golden section & pentagonal symmetry)"),
            ("GEOMETOR Pacioli", "*De Divina Proportione* Cap. VII–XXIII (:cite:`Pacioli1509`)"),
            ("Sister Codices", "``geometor/divine`` (golden ratio :math:`\\phi` algebraic field ``Q(phi)``)"),
        ),
        depends_on=("W.02", "W.04"),
    ),
    PrincipleSpec(
        num=6,
        code="W.06",
        slug="w-06",
        part=PART_II,
        category="The Five Fundamental Laws",
        tags=("Pythagoras", "right triangle", "right midpoint", "quadrea", "Egyptian triangle"),
        title="Law I: Pythagoras' Theorem & Right Triangle Invariants",
        subtitle="Equivalence of Perpendicularity (s_3 = 1) and Additive Quadrances (Q_1 + Q_2 = Q_3)",
        enunciation=(
            "For any three non-collinear points A_1, A_2, A_3 over a field F (char F != 2) with non-null "
            "lines A_1 A_3 and A_2 A_3, the lines A_1 A_3 and A_2 A_3 are perpendicular (s_3 = 1) if and "
            "only if Q(A_2, A_3) + Q(A_1, A_3) = Q(A_1, A_2), in which case the hypotenuse midpoint M_3 "
            "is equidistant in quadrance (Q_3 / 4) from all three vertices."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "M_3 = midpoint(A_1, A_2)",
            "c = circle(M_3, A_3)",
            "F_3 = foot(A_3, line(A_1, A_2))",
        ),
        synthesis=(
            "In :person:`Euclid <euclid>`'s *Elements* (:ref:`I.47` and :ref:`I.48`), :person:`Pythagoras <pythagoras>`' "
            "theorem equates geometric areas of squares erected on the sides of a right triangle. In Rational "
            "Trigonometry (:cite:`Wildberger2005`), **squares on the sides are the native metric**: "
            ":math:`Q_1 + Q_2 = Q_3` is an exact linear equation in the three side quadrances whenever the "
            "lines at :g:`A_3` have :term:`spread` :math:`s_3 = 1`.",
            "Two immediate corollaries hold over any field :math:`F`: the **Right Quadrea Theorem** "
            ":math:`\\mathcal{A} = 4 Q_1 Q_2`, and the **Right Midpoint Theorem** showing that the midpoint "
            ":g:`M_3` of hypotenuse :math:`A_1 A_2` is the :term:`circumcenter` of :g:`t` with "
            ":math:`Q(M_3, A_1) = Q(M_3, A_2) = Q(M_3, A_3) = Q_3 / 4`, placing :g:`A_3` on circle :g:`c` "
            "and splitting the hypotenuse at altitude foot :g:`F_3` in ratio :math:`Q_2 : Q_1`.",
        ),
        math_blocks=(
            r"\ell_1 \perp \ell_2 \iff s_3 = 1 \iff Q_1 + Q_2 = Q_3",
            r"Q(M_3, A_1) = Q(M_3, A_2) = Q(M_3, A_3) = \frac{Q_3}{4}, \qquad "
            r"\mathcal{A}(Q_1, Q_2, Q_1 + Q_2) = 4 Q_1 Q_2",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.47`, :ref:`I.48`, :ref:`III.31`, :ref:`VI.8` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`"),
            ("GEOMETOR Fundamentals", ":ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.42 Right Triangles <f-42>`"),
            ("ETC Reference", "Egyptian right triangle ``(3, 4, 5)`` -> ``Q = (9, 16, 25)`` in ``geometor/etc``"),
        ),
        depends_on=("W.03", "W.04"),
    ),
    PrincipleSpec(
        num=7,
        code="W.07",
        slug="w-07",
        part=PART_II,
        category="The Five Fundamental Laws",
        tags=("Triple Quad Formula", "quadrea", "Archimedes", "Heron", "collinearity"),
        title="Law II: Triple Quad Formula, Archimedes' Function & Quadrea",
        subtitle="Polynomial Collinearity Criterion and Radical-Free Triangle Area Algebra",
        enunciation=(
            "Three planar points A_1, A_2, A_3 with pairwise quadrances Q_1, Q_2, Q_3 are collinear "
            "if and only if Archimedes' symmetric quadratic form A(Q_1, Q_2, Q_3) = (Q_1 + Q_2 + Q_3)^2 - "
            "2(Q_1^2 + Q_2^2 + Q_3^2) vanishes; for any triangle, A(Q_1, Q_2, Q_3) equals 4 times the "
            "squared coordinate determinant (16 * Delta^2), defining the triangle's quadrea."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
            "P_col : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "l_base = line(A_1, A_2)",
            "h_3 = segment(A_3, foot(A_3, l_base))",
        ),
        synthesis=(
            "In classical geometry, collinearity is expressed linearly via distances :math:`d_1 + d_2 = d_3` "
            "(which depends on ordering), while triangle area uses :person:`Heron <heron>`'s radical "
            ":math:`\\Delta = \\sqrt{s(s-a)(s-b)(s-c)}`. Squaring out all three sign combinations "
            ":math:`(\\pm\\sqrt{Q_1} \\pm \\sqrt{Q_2} \\pm \\sqrt{Q_3}) = 0` yields :person:`Archimedes <archimedes>`' "
            "symmetric polynomial :math:`\\mathcal{A}(Q_1, Q_2, Q_3)` (:cite:`Wildberger2005`).",
            "Over any field :math:`F` (:math:`\\operatorname{char} F \\neq 2`), the :term:`Triple Quad Formula` "
            ":math:`\\mathcal{A}(Q_1, Q_2, Q_3) = 0` characterizes collinearity (illustrated by :g:`P_col` on "
            ":g:`l_base`) without ordering or square roots! When :g:`A_1`, :g:`A_2`, :g:`A_3` form a triangle "
            ":g:`t` with altitude :g:`h_3`, the :term:`quadrea` :math:`\\mathcal{A} = 4 Q_3 Q(A_3, \\ell_{\\text{base}}) = 16 \\Delta^2` "
            "is always an element of :math:`F`—for the Heronian :math:`(13, 14, 15)` triangle with "
            ":math:`Q = (169, 196, 225)`, :math:`\\mathcal{A} = 112896 = 16 \\times 84^2`.",
        ),
        math_blocks=(
            r"\mathcal{A}(Q_1, Q_2, Q_3) = (Q_1 + Q_2 + Q_3)^2 - 2(Q_1^2 + Q_2^2 + Q_3^2) "
            r"= 4 Q_1 Q_2 - (Q_1 + Q_2 - Q_3)^2",
            r"A_1, A_2, A_3 \text{ collinear} \iff \mathcal{A}(Q_1, Q_2, Q_3) = 0, \qquad "
            r"\mathcal{A}(Q_1, Q_2, Q_3) = 4 \det\begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{pmatrix}^2 = 16\Delta^2",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`II.12`, :ref:`II.13` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.1`, :ref:`G.3`"),
            ("GEOMETOR Fundamentals", ":ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>` (:cite:`SeeligNotebooks`)"),
            ("ETC Reference", "Acute Heronian reference triangle ``(13, 14, 15)``"),
        ),
        depends_on=("W.01", "W.03", "W.06"),
    ),
    PrincipleSpec(
        num=8,
        code="W.08",
        slug="w-08",
        part=PART_II,
        category="The Five Fundamental Laws",
        tags=("Spread Law", "circumquadrance", "sine law", "extended spread law"),
        title="Law III: The Spread Law & Extended Circumquadrance Law",
        subtitle="Exact Rational Proportionality of Vertex Spreads and Opposite Quadrances",
        enunciation=(
            "In any non-null triangle A_1 A_2 A_3 with side quadrances Q_1, Q_2, Q_3, vertex spreads "
            "s_1, s_2, s_3, quadrea A, and circumquadrance K, the ratios of spread to opposite quadrance "
            "are equal: s_1 / Q_1 = s_2 / Q_2 = s_3 / Q_3 = A / (4 * Q_1 * Q_2 * Q_3) = 1 / (4 * K)."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "F_1 = foot(A_1, line(A_2, A_3))",
            "F_2 = foot(A_2, line(A_1, A_3))",
            "C = circumcenter(A_1, A_2, A_3)",
            "c = circle(C, A_1)",
        ),
        synthesis=(
            "Dropping altitudes to feet :g:`F_1` and :g:`F_2` in triangle :g:`t` gives two right-triangle "
            "expressions for the altitude quadrances: :math:`Q(A_1, F_1) = Q_3 s_2` and :math:`Q(A_2, F_2) = Q_3 s_1`, "
            "while matching :math:`Q_2 s_3 = Q_3 s_2` immediately yields the :term:`Spread Law` "
            ":math:`s_1 / Q_1 = s_2 / Q_2 = s_3 / Q_3` (:cite:`Wildberger2005`)—replacing the transcendental "
            "Law of Sines with pure field division!",
            "Connecting the Spread Law to the :term:`circumcenter` :g:`C` and circumcircle :g:`c` produces "
            "the **Extended Spread Law**: every ratio :math:`s_i / Q_i` equals :math:`1 / (4 K)`, where "
            ":math:`K = Q(C, A_i) = Q_1 Q_2 Q_3 / \\mathcal{A}` is the :term:`circumquadrance`—the exact "
            "quadratic counterpart of the classical :math:`a / \\sin A = 2 R` identity.",
        ),
        math_blocks=(
            r"\frac{s_1}{Q_1} = \frac{s_2}{Q_2} = \frac{s_3}{Q_3} = \frac{\mathcal{A}}{4 Q_1 Q_2 Q_3} = \frac{1}{4 K}",
            r"K = \frac{Q_1 Q_2 Q_3}{\mathcal{A}}, \qquad \mathcal{A} = 64 K^2 s_1 s_2 s_3",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`III.20`, :ref:`IV.5`, :ref:`VI.4` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.5`"),
            ("GEOMETOR Fundamentals", ":ref:`F.11 Circumcenter <f-11>`, :ref:`F.13 Compare Triangles in Circles <f-13>`"),
            ("ETC Reference", "Circumcenter ``X(3)`` (:cite:`Kimberling1998`)"),
        ),
        depends_on=("W.04", "W.06", "W.07"),
    ),
    PrincipleSpec(
        num=9,
        code="W.09",
        slug="w-09",
        part=PART_II,
        category="The Five Fundamental Laws",
        tags=("Cross Law", "cosine law", "cross", "quadrea spread"),
        title="Law IV: The Cross Law & Quadrea-Spread Identity",
        subtitle="Quadratic Replacement for the Law of Cosines Without Ambiguous Angle Signs",
        enunciation=(
            "In any triangle A_1 A_2 A_3 with non-null sides Q_1, Q_2 meeting with spread s_3 and "
            "cross c_3 = 1 - s_3 at vertex A_3, the quadrances satisfy (Q_1 + Q_2 - Q_3)^2 = "
            "4 * Q_1 * Q_2 * (1 - s_3) = 4 * Q_1 * Q_2 * c_3, equivalently A(Q_1, Q_2, Q_3) = 4 * Q_1 * Q_2 * s_3."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "l_1 = line(A_2, A_3)",
            "F_1 = foot(A_1, l_1)",
            "alt_1 = segment(A_1, F_1)",
        ),
        synthesis=(
            "Squaring the Conway-style dot-product term :math:`Q_1 + Q_2 - Q_3` eliminates the sign ambiguity "
            "between acute and obtuse angles in the classical Law of Cosines, producing the :term:`Cross Law` "
            ":math:`(Q_1 + Q_2 - Q_3)^2 = 4 Q_1 Q_2 (1 - s_3)` (:cite:`Wildberger2005`). Geometrically, "
            "dropping altitude :g:`alt_1` from :g:`A_1` to foot :g:`F_1` on line :g:`l_1` decomposes triangle "
            ":g:`t` into two right triangles whose Pythagorean relations eliminate :math:`Q(A_3, F_1)` quadratically.",
            "Subtracting :math:`4 Q_1 Q_2` from both sides reveals the **Quadrea Spread Theorem** "
            ":math:`\\mathcal{A} = 4 Q_1 Q_2 s_3` (the rational analogue of :math:`\\Delta = \\frac{1}{2} a b \\sin C`). "
            "Given rational quadrances—such as :math:`Q = (16, 49, 25)` for sides :math:`(4, 7, 5)`—the Cross "
            "Law immediately yields exact rational spreads :math:`s_1 = 384/1225`, :math:`s_2 = 24/25`, "
            "and :math:`s_3 = 24/49` by elementary arithmetic alone!",
        ),
        math_blocks=(
            r"(Q_1 + Q_2 - Q_3)^2 = 4 Q_1 Q_2 (1 - s_3) = 4 Q_1 Q_2 c_3",
            r"s_3 = 1 - \frac{(Q_1 + Q_2 - Q_3)^2}{4 Q_1 Q_2} = \frac{\mathcal{A}(Q_1, Q_2, Q_3)}{4 Q_1 Q_2}",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`II.12`, :ref:`II.13` (Obtuse and acute generalizations of Pythagoras)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`"),
            ("GEOMETOR Fundamentals", ":ref:`F.14 Conway Notation <f-14>` (:math:`4 S_C^2 = (a^2 + b^2 - c^2)^2`)"),
            ("Classical Bridge", "Replaces ``c^2 = a^2 + b^2 - 2ab cos C`` over arbitrary fields"),
        ),
        depends_on=("W.04", "W.06", "W.07"),
    ),
    PrincipleSpec(
        num=10,
        code="W.10",
        slug="w-10",
        part=PART_II,
        category="The Five Fundamental Laws",
        tags=("Triple Spread Formula", "triple cross", "quadruple spread", "angle sum"),
        title="Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas",
        subtitle="Cubic Polynomial Harmony Replacing theta_1 + theta_2 + theta_3 = pi",
        enunciation=(
            "For any three coplanar non-null lines l_1, l_2, l_3 with pairwise spreads s_1, s_2, s_3 "
            "and crosses c_i = 1 - s_i, the spreads satisfy the cubic Triple Spread Formula "
            "(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 and the crosses satisfy "
            "(c_1 + c_2 + c_3 - 1)^2 = 4*c_1*c_2*c_3; for four lines, the Quadruple Spread polynomial "
            "R(s_12, s_23, s_34, s_14) = 0 is identically invariant under s_ij <-> 1 - s_ij."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "l_1 = line(A_2, A_3)",
            "l_2 = line(A_1, A_3)",
            "l_3 = line(A_1, A_2)",
            "t = polygon(A_1, A_2, A_3)",
        ),
        synthesis=(
            "Just as the :term:`Triple Quad Formula` replaces :math:`d_1 + d_2 = d_3` by a quadratic relation "
            "with no square roots, the :term:`Triple Spread Formula` replaces Euclid's angle-sum theorem "
            ":math:`\\theta_1 + \\theta_2 + \\theta_3 = \\pi` with a symmetric cubic equation in the three "
            "spreads :math:`(s_1, s_2, s_3)` of lines :g:`l_1`, :g:`l_2`, :g:`l_3` (:cite:`Wildberger2005`). "
            "Notice the structural miracle: it differs from :math:`\\mathcal{A}(s_1, s_2, s_3) = 0` by the "
            "single cubic term :math:`4 s_1 s_2 s_3`!",
            "Substituting :math:`s_i = 1 - c_i` produces the **Triple Cross Formula** "
            ":math:`(c_1 + c_2 + c_3 - 1)^2 = 4 c_1 c_2 c_3`. Extending from three to four lines yields the "
            ":term:`Quadruple Spread Formula` :math:`R(s_{12}, s_{23}, s_{34}, s_{14}) = 0`, which possesses "
            "an unexpected self-duality: replacing every spread :math:`s_{ij}` with its cross :math:`c_{ij} = 1 - s_{ij}` "
            "leaves the polynomial :math:`R` **identically unchanged**!",
        ),
        math_blocks=(
            r"(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3 "
            r"\iff (s_3 - (s_1 + s_2 - 2 s_1 s_2))^2 = 4 s_1 s_2 (1 - s_1)(1 - s_2)",
            r"(c_1 + c_2 + c_3 - 1)^2 = 4 c_1 c_2 c_3, \qquad "
            r"R(a, b, c, d) \equiv R(1 - a, 1 - b, 1 - c, 1 - d)",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.32` (Angle sum of a triangle, :cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.5`"),
            ("GEOMETOR Fundamentals", ":ref:`F.35 Obtuse and Acute Triangles <f-35>`, :ref:`F.53 Geometric Half-Angle Trigonometry <f-53>`"),
            ("3D Algebraic Surface", "Defines the :term:`ellipson` surface in ``[0, 1]^3`` (:ref:`W.28 <w-28>`)"),
        ),
        depends_on=("W.04", "W.08", "W.09"),
    ),
    PrincipleSpec(
        num=11,
        code="W.11",
        slug="w-11",
        part=PART_II,
        category="Special & Golden Triangles",
        tags=("isosceles", "equilateral", "Kepler triangle", "golden ratio", "Pons Asinorum"),
        title="Isosceles, Equilateral & Kepler's Golden Right Triangle",
        subtitle="Pons Asinorum, the 3/4 Equilateral Spread, and Pure Golden Powers Q = (1, phi, phi^2)",
        enunciation=(
            "In a non-null triangle, Q_1 = Q_2 iff s_1 = s_2 (with apex spread s_3 = (Q_3/Q_1)(1 - Q_3/(4*Q_1))), "
            "and Q_1 = Q_2 = Q_3 iff s_1 = s_2 = s_3 = 3/4; in Kepler's Golden Right Triangle with side lengths "
            "(1, sqrt(phi), phi), the nested radical vanishes in quadrance to give Q = (1, phi, phi^2) and "
            "exact golden spreads (s_1, s_2, s_3) = (2 - phi, phi - 1, 1) = (1/phi^2, 1/phi, 1)."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t_kepler = polygon(A_1, A_2, A_3)",
            "F_1 = foot(A_1, line(A_2, A_3))",
            "alt = segment(A_1, F_1)",
        ),
        synthesis=(
            "In Universal Geometry, *Pons Asinorum* (:ref:`I.5`) holds for every non-null triangle over any "
            "field (:cite:`Wildberger2005`): :math:`Q_1 = Q_2 \\iff s_1 = s_2`. Equilateral triangles satisfy "
            ":math:`Q_1 = Q_2 = Q_3 \\iff s_1 = s_2 = s_3 = 3/4`, which immediately proves that no equilateral "
            "triangle can have rational coordinates in :math:`\\mathbb{Q}^2` because :math:`\\mathcal{A} = 3 Q^2` "
            "requires :math:`3` to be a square in :math:`F` (as it is in :math:`\\mathbb{F}_{11}`, where :math:`5^2 \\equiv 3`)!",
            "Even more striking is :person:`Johannes Kepler <kepler>`'s **Golden Right Triangle** (:g:`t_kepler`), "
            "canonical in ``geometor/etc`` and ``geometor/divine``. Classically burdened with the nested radical "
            ":math:`\\sqrt{\\phi}`, its quadrances are pure geometric powers of the :term:`golden ratio` "
            ":math:`(Q_3, Q_2, Q_1) = (1, \\phi, \\phi^2)` satisfying :math:`1 + \\phi = \\phi^2`, while its "
            "spreads are :math:`(1/\\phi^2, 1/\\phi, 1) = (2 - \\phi, \\phi - 1, 1)` with altitude foot :g:`F_1` "
            "dividing the hypotenuse in the **exact golden section** :math:`\\phi : 1`!",
        ),
        math_blocks=(
            r"Q_1 = Q_2 \implies s_3 = \frac{Q_3}{Q_1}\left(1 - \frac{Q_3}{4 Q_1}\right), \qquad "
            r"Q_1 = Q_2 = Q_3 \iff s_1 = s_2 = s_3 = \frac{3}{4}",
            r"\text{Kepler Triangle:}\quad (Q_3, Q_2, Q_1) = (1, \phi, \phi^2), \qquad "
            r"(s_3, s_2, s_1) = \left(\frac{1}{\phi^2}, \frac{1}{\phi}, 1\right) = (2 - \phi,\; \phi - 1,\; 1)",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.1`, :ref:`I.5`, :ref:`II.11`, :ref:`VI.30` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.2`, :ref:`G.12`"),
            ("GEOMETOR Fundamentals", ":ref:`F.18 Equilateral Triangle <f-18>`, :ref:`F.23 Golden Triangles <f-23>`, :ref:`F.30 Isosceles Triangles <f-30>`"),
            ("GEOMETOR ETC & Divine", "Canonical Kepler triangle ``(1, sqrt(phi), phi)`` in ``geometor/etc`` & ``geometor/divine``"),
        ),
        depends_on=("W.05", "W.06", "W.08", "W.09", "W.10"),
    ),
    PrincipleSpec(
        num=12,
        code="W.12",
        slug="w-12",
        part=PART_III,
        category="Triangle Centers & Number Theory",
        tags=("vertex bisector", "square vertex", "incenter", "inquadrance", "excenters"),
        title="Vertex Bisectors, Square Vertices & The Four Incenters",
        subtitle="Number-Theoretic Criterion for Rational Bisectors and Symmetric Inquadrances",
        enunciation=(
            "The locus of points X having equal quadrance Q(X, l_1) = Q(X, l_2) to two intersecting "
            "non-null lines l_1, l_2 splits into two orthogonal vertex bisectors over F if and only if "
            "(a_1^2 + b_1^2)(a_2^2 + b_2^2) is a square in F; when two vertices of a triangle have "
            "bisectors in F, so does the third, producing four symmetric incenters I_0, I_1, I_2, I_3."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "I_0 = incenter(A_1, A_2, A_3)",
            "b_1 = line(A_1, I_0)",
            "b_2 = line(A_2, I_0)",
            "b_3 = line(A_3, I_0)",
            "c_in = circle(I_0, foot(I_0, line(A_1, A_2)))",
        ),
        synthesis=(
            "Unlike medians and altitudes—which always exist rationally over :math:`F`—:term:`vertex bisector` "
            "lines reveal a deep arithmetic obstruction in Universal Geometry (:cite:`Wildberger2005`). "
            "Equating :math:`Q(X, \\ell_1) = Q(X, \\ell_2)` gives "
            ":math:`(a_2^2 + b_2^2)(a_1 x + b_1 y + c_1)^2 = (a_1^2 + b_1^2)(a_2 x + b_2 y + c_2)^2`, "
            "which factors into two perpendicular linear equations over :math:`F` if and only if the vertex "
            "is a :term:`square vertex` (:math:`(a_1^2 + b_1^2)(a_2^2 + b_2^2) = r^2` in :math:`F`, equivalently "
            ":math:`1 - s` is a square when one line has norm square).",
            "When two vertices of :g:`t` admit bisectors in :math:`F`, **Theorem 88** guarantees that the "
            "third vertex also admits bisectors, intersecting in four completely symmetric :term:`incenter` "
            "points :math:`I_0, I_1, I_2, I_3` (classical :math:`X(1)` :g:`I_0` and the three excenters). "
            "For the Heronian triangle :math:`A_1=[0,0], A_2=[14,0], A_3=[5,12]`, all three vertices are "
            "square over :math:`\\mathbb{Q}`, placing :g:`I_0` at exact integer coordinates :math:`[6, 4]` "
            "with :term:`inquadrance` :math:`R_0 = 16` (:g:`c_in`)!",
        ),
        math_blocks=(
            r"Q(X, \ell_1) = Q(X, \ell_2) \iff (a_2^2 + b_2^2)(a_1 x + b_1 y + c_1)^2 "
            r"= (a_1^2 + b_1^2)(a_2 x + b_2 y + c_2)^2",
            r"s(I A_1, I A_2) = 1 - s(A_3 I, A_3 A_1), \qquad "
            r"\mathcal{A}(Q_1, Q_2, Q_3) \text{ & } R_i:\; Q(I_0, \ell_1) = Q(I_0, \ell_2) = Q(I_0, \ell_3) = R_0",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.9`, :ref:`IV.4` (Angle bisection and inscribed circle, :cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.8`"),
            ("GEOMETOR Fundamentals", ":ref:`F.28 Incenter <f-28>`, :ref:`F.29 Inradius <f-29>` (:cite:`SeeligNotebooks`)"),
            ("ETC Reference", "Incenter ``X(1)`` & Excenters in ``geometor/etc`` (:cite:`Kimberling1998`)"),
        ),
        depends_on=("W.02", "W.03", "W.04", "W.10"),
    ),
    PrincipleSpec(
        num=13,
        code="W.13",
        slug="w-13",
        part=PART_III,
        category="Proportions, Cevians & Medians",
        tags=("Stewart's theorem", "medians", "Apollonius", "centroid", "medial triangle"),
        title="Stewart's Theorem, Median Quadrances & The Centroid",
        subtitle="Exact Quadratic Cevian Laws, Apollonius' Identity, and X(2) Concurrency",
        enunciation=(
            "For any affine point D = (1 - lambda)*A_1 + lambda*A_2 on side A_1 A_2 of triangle "
            "A_1 A_2 A_3, the cevian quadrance satisfies Q(A_3, D) = (1 - lambda)*Q_2 + lambda*Q_1 - "
            "lambda*(1 - lambda)*Q_3; at lambda = 1/2, the median quadrance satisfies "
            "4*Q(A_3, M_3) = 2*Q_1 + 2*Q_2 - Q_3, and the three medians concur at G = (A_1 + A_2 + A_3)/3."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "M_1 = midpoint(A_2, A_3)",
            "M_2 = midpoint(A_1, A_3)",
            "M_3 = midpoint(A_1, A_2)",
            "G = meet(line(A_1, M_1), line(A_2, M_2))",
            "t_med = polygon(M_1, M_2, M_3)",
        ),
        synthesis=(
            ":person:`Matthew Stewart <stewart>`'s 1746 cevian relation becomes completely algebraic in "
            "quadrances (:cite:`Wildberger2005`). Expressing any point :math:`D` on :math:`A_1 A_2` as the "
            "affine combination :math:`(1 - \\lambda)A_1 + \\lambda A_2` (with :math:`R_1 = \\lambda^2 Q_3` and "
            ":math:`R_2 = (1 - \\lambda)^2 Q_3`) gives :math:`Q(A_3, D)` as a linear combination of "
            ":math:`Q_1, Q_2, Q_3`, or in pure quadrances without :math:`\\lambda` via :term:`Stewart's theorem`.",
            "Setting :math:`\\lambda = 1/2` gives :person:`Apollonius <apollonius>`' **Median Quadrance Theorem** "
            ":math:`4 M_3 = 2 Q_1 + 2 Q_2 - Q_3` for the midpoints :g:`M_1`, :g:`M_2`, :g:`M_3`. Provided "
            ":math:`\\operatorname{char} F \\neq 3`, the three medians concur at the :term:`centroid` "
            ":g:`G` :math:`= \\frac{1}{3}(A_1 + A_2 + A_3)` (:math:`X(2)`), dividing each median in quadrance "
            "proportion :math:`4 : 1`, while the medial triangle :g:`t_med` has side quadrances :math:`Q_i / 4` "
            "and quadrea :math:`\\mathcal{A} / 16`.",
        ),
        math_blocks=(
            r"Q(A_3, D) = (1 - \lambda) Q_2 + \lambda Q_1 - \lambda(1 - \lambda) Q_3, \qquad "
            r"4 Q(A_3, M_3) = 2 Q_1 + 2 Q_2 - Q_3",
            r"G = \frac{A_1 + A_2 + A_3}{3}, \qquad Q(A_i, G) = \frac{4}{9} Q(A_i, M_i) = 4 Q(G, M_i)",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`I.10`, :ref:`VI.2` (Thales' midpoint parallel theorem, :cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.5`"),
            ("GEOMETOR Fundamentals", ":ref:`F.6 Centroid <f-06>`, :ref:`F.46 Stewart's Theorem <f-46>` (:cite:`SeeligNotebooks`)"),
            ("ETC Reference", "Centroid ``X(2)`` in ``geometor/etc`` (:cite:`Kimberling1998`)"),
        ),
        depends_on=("W.01", "W.03", "W.07", "W.09"),
    ),
    PrincipleSpec(
        num=14,
        code="W.14",
        slug="w-14",
        part=PART_III,
        category="Projective & Cevian Proportions",
        tags=("Menelaus' theorem", "Ceva's theorem", "alternate spreads", "cevians", "transversal"),
        title="Menelaus, Ceva & The Alternate Spreads Theorem",
        subtitle="Multiplicative Quadrance and Spread Balance for Collinearity and Concurrency",
        enunciation=(
            "If either a transversal line l cuts the sidelines A_2 A_3, A_3 A_1, A_1 A_2 of a non-null "
            "triangle at B_1, B_2, B_3 (Menelaus) or three cevians through a point A_0 meet the opposite "
            "sidelines at B_1, B_2, B_3 (Ceva), then the six segment quadrances satisfy "
            "Q(A_2, B_1) * Q(A_3, B_2) * Q(A_1, B_3) = Q(B_1, A_3) * Q(B_2, A_1) * Q(B_3, A_2)."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
            "A_0 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "B_1 = meet(line(A_2, A_3), line(A_1, A_0))",
            "B_2 = meet(line(A_1, A_3), line(A_2, A_0))",
            "B_3 = meet(line(A_1, A_2), line(A_3, A_0))",
        ),
        synthesis=(
            "Classically, :person:`Menelaus <menelaus>`' theorem (:math:`\\prod = -1`) and :person:`Giovanni Ceva <ceva>`'s "
            "theorem (:math:`\\prod = +1`) differ only in sign! Because :term:`quadrance` squares signed "
            "ratios, **both** collinear transversals and concurrent cevians through :g:`A_0` satisfy the "
            "identical necessary multiplicative law :math:`R_1 R_2 R_3 = P_1 P_2 P_3` at division points "
            ":g:`B_1`, :g:`B_2`, :g:`B_3` (:cite:`Wildberger2005`). (Consequently, the converse of neither "
            "quadrance product holds alone—their combined six-solution locus splits neatly into the "
            "collinear Menelaus configurations and concurrent Ceva configurations!)",
            "Underpinning Ceva's theorem is the **Alternate Spreads Theorem** (Theorem 79): for any point "
            ":g:`A_0` in the plane of :g:`t`, the alternating vertex spreads :math:`r_i = s(A_i A_{i+1}, A_i A_0)` "
            "and :math:`p_i = s(A_i A_{i-1}, A_i A_0)` satisfy :math:`r_1 r_2 r_3 = p_1 p_2 p_3`—an "
            "invariant that generalizes to any :math:`n`-gon and drives the algebraic solution of "
            ":term:`Hansen's problem` (:ref:`W.25 <w-25>`).",
        ),
        math_blocks=(
            r"Q(A_2, B_1)\, Q(A_3, B_2)\, Q(A_1, B_3) = Q(B_1, A_3)\, Q(B_2, A_1)\, Q(B_3, A_2)",
            r"\text{Alternate Spreads:}\quad "
            r"s(A_1 A_2, A_1 A_0)\, s(A_2 A_3, A_2 A_0)\, s(A_3 A_1, A_3 A_0) = "
            r"s(A_1 A_3, A_1 A_0)\, s(A_2 A_1, A_2 A_0)\, s(A_3 A_2, A_3 A_0)",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`VI.2` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.5`"),
            ("GEOMETOR Fundamentals", ":ref:`F.7 Ceva and Menelaus <f-07>` (26 manuscript folios, :cite:`SeeligNotebooks`)"),
            ("Sister Codices", "``geometor/pappus`` (projective incidence & transversal invariants)"),
        ),
        depends_on=("W.01", "W.08"),
    ),
)
