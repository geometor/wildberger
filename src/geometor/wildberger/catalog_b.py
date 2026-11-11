"""Catalog definitions for Principles `W.15` through `W.28` (Parts III & IV).

Covers circumcenters and orthocenters, the Euler line and nine-point circle,
rational circle geometry and cyclic quadrilaterals, regular polygons and golden
stars, metrical conics and Taylor tangents, projective cross-ratios,
Chromogeometry (Blue/Red/Green metrics), triangle/surveying solvers (including
Snellius-Pothenot and Hansen's problem), algebraic physics, 3D Platonic dihedral
spreads, and rational polar curves / the ellipson.
"""

from __future__ import annotations

from geometor.wildberger.catalog import PrincipleSpec

PART_III = "Part III: Universal Triangle, Conic & Chromogeometry"
PART_IV = "Part IV: Practical Solvers, 3D Platonic Geometry & Polar Curves"

PRINCIPLES_B: tuple[PrincipleSpec, ...] = (
    PrincipleSpec(
        num=15,
        code="W.15",
        slug="w-15",
        part=PART_III,
        category="Triangle Centers & Classical Lines",
        tags=("circumcenter", "orthocenter", "orthic triangle", "barycentric", "Conway notation"),
        title="Circumcenter, Orthocenter & Universal Affine Barycentrics",
        subtitle="Radical-Free Coordinates for X(3), X(4), and Orthic Bisector Symmetry",
        enunciation=(
            "Every non-null triangle A_1 A_2 A_3 over a field F (char F != 2) has a unique circumcenter C "
            "at the intersection of its side perpendicular bisectors and a unique orthocenter O at the "
            "intersection of its altitudes, with affine barycentric weights beta_i = Q_i*(Q_j + Q_k - Q_i)/(2*A) "
            "for C and gamma_i = (Q_i + Q_j - Q_k)*(Q_k + Q_i - Q_j)/(2*A) for O."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "C = circumcenter(A_1, A_2, A_3)",
            "c_circ = circle(C, A_1)",
            "F_1 = foot(A_1, line(A_2, A_3))",
            "F_2 = foot(A_2, line(A_1, A_3))",
            "F_3 = foot(A_3, line(A_1, A_2))",
            "O = meet(line(A_1, F_1), line(A_2, F_2))",
            "t_orth = polygon(F_1, F_2, F_3)",
        ),
        synthesis=(
            "Unlike the :term:`incenter`—which requires square vertices—both the :term:`circumcenter` :g:`C` "
            "(:math:`X(3)`) and the :term:`orthocenter` :g:`O` (:math:`X(4)`) are **universally rational** "
            "in the vertex coordinates of any non-null triangle :g:`t` (:cite:`Wildberger2005`). Their "
            "homogeneous barycentric weights depend exclusively on the Conway-style dot-product factors "
            ":math:`2 S_i = Q_j + Q_k - Q_i` normalized by :math:`2\\mathcal{A}`, linking directly to "
            ":ref:`F.14 Conway Notation <f-14>` and :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`.",
            "Dropping altitudes to feet :g:`F_1`, :g:`F_2`, :g:`F_3` forms the **orthic triangle** :g:`t_orth`, "
            "whose altitudes bisect its vertex spreads (**Orthic Triangle Theorem**): the altitudes of :g:`t` "
            "are :term:`vertex bisector` lines of :g:`t_orth`, making :g:`O` an incenter/excenter of :g:`t_orth` "
            "even over fields where :g:`t` itself has no rational incenter! Moreover, reflecting :g:`O` across "
            "each sideline lands directly on the circumcircle :g:`c_circ`.",
        ),
        math_blocks=(
            r"C = \sum_{i=1}^{3} \frac{Q_i(Q_j + Q_k - Q_i)}{2\mathcal{A}}\, A_i, \qquad "
            r"O = \sum_{i=1}^{3} \frac{(Q_i + Q_j - Q_k)(Q_k + Q_i - Q_j)}{2\mathcal{A}}\, A_i",
            r"Q(O, A_3) = 4 K (1 - s_3), \qquad s(F_3 F_1, F_3 A_3) = s(F_3 F_2, F_3 A_3) = 1 - s_3",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`IV.5` (Circumscribing a circle about a triangle, :cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`, :ref:`G.7`"),
            ("GEOMETOR Fundamentals", ":ref:`F.11 Circumcenter <f-11>`, :ref:`F.36 Orthic Triangle <f-36>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`"),
            ("ETC Reference", "Circumcenter ``X(3)`` & Orthocenter ``X(4)`` (:cite:`Kimberling1998`)"),
        ),
        depends_on=("W.01", "W.03", "W.08", "W.09"),
    ),
    PrincipleSpec(
        num=16,
        code="W.16",
        slug="w-16",
        part=PART_III,
        category="Triangle Centers & Classical Circles",
        tags=("Euler line", "nine-point circle", "nine-point center", "Feuerbach", "finite fields"),
        title="The Euler Line & Nine-Point Circle Over Arbitrary Fields",
        subtitle="Exact Collinearity of C, G, N, O and the K/4 Nine-Point Circle in Q and F_p",
        enunciation=(
            "In any non-null triangle A_1 A_2 A_3 over a field F (char F != 2), the nine-point center "
            "N = (C + O)/2 satisfies 2*N - C = O (and 3*G = 2*C + O when char F != 3), placing C, G, N, O "
            "on the Euler line with quadrance proportions Q(C, G) : Q(C, N) : Q(C, O) = 4 : 9 : 36; the "
            "three side midpoints M_i, three altitude feet F_i, and three Euler midpoints E_i = (A_i + O)/2 "
            "all have exact quadrance K / 4 from N."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "C = circumcenter(A_1, A_2, A_3)",
            "O = orthocenter(A_1, A_2, A_3)",
            "N = midpoint(C, O)",
            "G = centroid(A_1, A_2, A_3)",
            "l_euler = line(C, O)",
            "c_circ = circle(C, A_1)",
            "c_nine = circle(N, midpoint(A_2, A_3))",
        ),
        synthesis=(
            ":person:`Leonhard Euler <euler>`'s collinearity of :g:`C` (:math:`X(3)`), :g:`G` (:math:`X(2)`), "
            ":g:`N` (:math:`X(5)`), and :g:`O` (:math:`X(4)`) along :g:`l_euler` is a pure vector identity "
            ":math:`O - C = (A_1 - C) + (A_2 - C) + (A_3 - C)` that holds over **every field** of characteristic "
            "not :math:`2` (:cite:`Wildberger2005`, :cite:`CoxeterGreitzer1967`). Notice that even in "
            "characteristic :math:`3`—where the centroid :g:`G` moves to infinity—the midpoint relation "
            ":math:`N = (C + O)/2` and the :term:`nine-point circle` remain completely intact!",
            "The circumcircle :g:`c_circ` has :term:`circumquadrance` :math:`K`, while :g:`c_nine` centered at "
            ":g:`N` passes through all nine canonical points—side midpoints :g:`M_1`, :g:`M_2`, :g:`M_3`, "
            "altitude feet :g:`F_1`, :g:`F_2`, :g:`F_3`, and Euler midpoints :g:`E_1`, :g:`E_2`, :g:`E_3`—with "
            "exact quadrance :math:`K_9 = K / 4`, verified identically over both :math:`\\mathbb{Q}[x_i, y_i]` "
            "and finite prime fields such as :math:`\\mathbb{F}_{17}`!",
        ),
        math_blocks=(
            r"O - C = \sum_{i=1}^{3} (A_i - C), \qquad 3 G = 2 C + O, \qquad N = \frac{C + O}{2}",
            r"Q(C, G) = \frac{1}{9} Q(C, O), \quad Q(C, N) = \frac{1}{4} Q(C, O), \quad "
            r"Q(N, M_i) = Q(N, F_i) = Q(N, E_i) = \frac{K}{4}",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`III.31`, :ref:`IV.5` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`, :ref:`G.7`"),
            ("GEOMETOR Fundamentals", ":ref:`F.34 Nine-Point Circle <f-34>` (:cite:`SeeligNotebooks`)"),
            ("ETC Reference", "Centers ``X(2)``, ``X(3)``, ``X(4)``, ``X(5)`` in ``geometor/etc`` (:cite:`Kimberling1998`)"),
        ),
        depends_on=("W.06", "W.13", "W.15"),
    ),
    PrincipleSpec(
        num=17,
        code="W.17",
        slug="w-17",
        part=PART_III,
        category="Circle Geometry & Rational Parametrization",
        tags=("Thales", "inscribed spread", "power of a point", "rational circle", "stereographic"),
        title="Circle Geometry: Subtended Spreads, Secant Products & Rational Points",
        subtitle="Thales' Right-Diameter Law, Inscribed Spread s_2(s), and Stereographic Parametrization",
        enunciation=(
            "On a circle Q(X, O_c) = K over F, a diameter subtends spread 1 at every other circle point "
            "(Thales), any chord P_1 P_2 subtends constant spread s_3 at the circumference with Q(P_1, P_2) = "
            "4*K*s_3 and central spread s(O_c P_1, O_c P_2) = S_2(s_3) = 4*s_3*(1 - s_3), and any external "
            "or internal point A_0 has invariant secant quadrance product Q(A_0, P_1)*Q(A_0, P_2) = (Q(A_0, O_c) - K)^2."
        ),
        signature_given=(
            "O_c : Point",
            "P_1 : Point",
            "P_2 : Point",
            "B : Point",
            "A_0 : Point",
        ),
        signature_steps=(
            "c = circle(O_c, P_1)",
            "l_sec1 = line(A_0, P_1)",
            "l_sec2 = line(A_0, B)",
            "Q_1 = meet_other(c, l_sec1, P_1)",
            "Q_2 = meet_other(c, l_sec2, B)",
        ),
        synthesis=(
            "Classical circle theorems suffer from case distinctions between acute and obtuse inscribed "
            "angles (:math:`\\theta` vs. :math:`\\pi - \\theta`). Because supplementary rays define the **same line**, "
            "every point :g:`B` on circle :g:`c` (centered at :g:`O_c`) subtends the **exact same spread** "
            ":math:`s(B P_1, B P_2) = Q(P_1, P_2) / (4 K)` on chord :math:`P_1 P_2`, regardless of which arc "
            ":g:`B` inhabits (:cite:`Wildberger2005`)! And the central spread at :g:`O_c` is governed by the "
            "second :term:`spread polynomial` :math:`S_2(s_3) = 4 s_3 (1 - s_3)`.",
            "Similarly, Euclid's intersecting chords/secants theorem (:ref:`III.35`, :ref:`III.36`) becomes "
            "the **Equal Products Theorem**: lines :g:`l_sec1` and :g:`l_sec2` through :g:`A_0` cut :g:`c` at "
            "(:g:`P_1`, :g:`Q_1`) and (:g:`B`, :g:`Q_2`) with invariant quadrance product :math:`(Q(A_0, O_c) - K)^2`. "
            "Projecting from :math:`[-1, 0]` parametrizes the unit circle by "
            ":math:`\\left[\\frac{1 - t^2}{1 + t^2}, \\frac{2 t}{1 + t^2}\\right]`, generating all Pythagorean "
            "triples over :math:`\\mathbb{Q}` and counting :math:`p \\mp 1` points on circles over :math:`\\mathbb{F}_p`.",
        ),
        math_blocks=(
            r"s(B P_1, B P_2) = \frac{Q(P_1, P_2)}{4 K} = s_3, \qquad "
            r"s(O_c P_1, O_c P_2) = S_2(s_3) = 4 s_3 (1 - s_3)",
            r"Q(A_0, P_1)\, Q(A_0, Q_1) = Q(A_0, B)\, Q(A_0, Q_2) = \big(Q(A_0, O_c) - K\big)^2, \qquad "
            r"U(t) = \left[\frac{1 - t^2}{1 + t^2},\; \frac{2 t}{1 + t^2}\right]",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`III.20`, :ref:`III.21`, :ref:`III.31`, :ref:`III.35`, :ref:`III.36`, :ref:`X.29` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.7`, :ref:`G.11`"),
            ("GEOMETOR Fundamentals", ":ref:`F.8 Chord Intersection <f-08>`, :ref:`F.9 Circle Equations <f-09>`, :ref:`F.33 Euclidean (m, n) Generators <f-33>`"),
            ("Number Theory Bridge", "Counts ``p + 1`` (when ``-1`` non-square) or ``p - 1`` rational points over ``F_p``"),
        ),
        depends_on=("W.05", "W.06", "W.08"),
    ),
    PrincipleSpec(
        num=18,
        code="W.18",
        slug="w-18",
        part=PART_III,
        category="Cyclic Polygons & Four-Point Invariants",
        tags=("cyclic quadrilateral", "Quadruple Quad Formula", "Brahmagupta", "Ptolemy", "Euler four-point"),
        title="Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation",
        subtitle="Opposite-Spread Equality, Radical-Free Brahmagupta/Robbins, and Determinant Cocircularity",
        enunciation=(
            "Four non-collinear points A_1, A_2, A_3, A_4 on a circle c satisfy equal opposite spreads "
            "s(A_1 A_2, A_1 A_4) = s(A_3 A_2, A_3 A_4), Ptolemy's Triple-Quad Law "
            "A(Q_12*Q_34, Q_23*Q_14, Q_13*Q_24) = 0 among product quadrances, and the cyclic quadrea "
            "/ circumquadrance formulas, while four collinear points satisfy Q(Q_12, Q_23, Q_34, Q_14) = 0."
        ),
        signature_given=(
            "O_c : Point",
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
            "A_4 : Point",
        ),
        signature_steps=(
            "c = circle(O_c, A_1)",
            "q_cyc = polygon(A_1, A_2, A_3, A_4)",
            "d_13 = segment(A_1, A_3)",
            "d_24 = segment(A_2, A_4)",
            "P_x = meet(line(A_1, A_3), line(A_2, A_4))",
        ),
        synthesis=(
            "In :person:`Euclid <euclid>`'s :ref:`III.22`, opposite angles of a cyclic quadrilateral sum to "
            "two right angles (:math:`\\theta_1 + \\theta_3 = \\pi`). Taking :math:`\\sin^2` turns supplementarity "
            "into **exact equality**: on circle :g:`c` (center :g:`O_c`), cyclic quadrilateral :g:`q_cyc` with "
            "diagonals :g:`d_13` and :g:`d_24` meeting at :g:`P_x` has **equal opposite vertex spreads** "
            ":math:`s_1 = s_3` and :math:`s_2 = s_4` (:cite:`Wildberger2005`)!",
            "Equally remarkable is :person:`Claudius Ptolemy <ptolemy>`'s theorem (:math:`ac + bd = ef` in "
            "lengths): squaring out the radicals shows that the three product pairs "
            ":math:`(Q_{12} Q_{34},\\; Q_{23} Q_{14},\\; Q_{13} Q_{24})` obey the **exact Triple Quad Formula** "
            ":math:`\\mathcal{A} = 0`! Meanwhile, :person:`Leonhard Euler <euler>`'s four-point relation proves "
            "that for **any** four coplanar points, the Cayley-Menger determinant vanishes identically, "
            "and for four collinear points their sequential quadrances satisfy the :term:`Quadruple Quad Formula` "
            ":math:`Q(Q_{12}, Q_{23}, Q_{34}, Q_{14}) = 0`.",
        ),
        math_blocks=(
            r"\text{Cyclic } A_1 A_2 A_3 A_4:\quad s_1 = s_3, \quad s_2 = s_4, \qquad "
            r"\mathcal{A}(Q_{12} Q_{34},\; Q_{23} Q_{14},\; Q_{13} Q_{24}) = 0",
            r"Q(a, b, c, d) = \big((a + b + c + d)^2 - 2(a^2 + b^2 + c^2 + d^2)\big)^2 - 64 a b c d = 0",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`III.21`, :ref:`III.22` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.7`"),
            ("GEOMETOR Fundamentals", ":ref:`F.15 Cyclic Quadrilateral <f-15>` (16 manuscript folios, :cite:`SeeligNotebooks`)"),
            ("Classical Canon", ":person:`Brahmagupta <brahmagupta>` & :person:`Claudius Ptolemy <ptolemy>` (*Almagest*)"),
        ),
        depends_on=("W.07", "W.09", "W.17"),
    ),
    PrincipleSpec(
        num=19,
        code="W.19",
        slug="w-19",
        part=PART_III,
        category="Regular Polygons, Golden Stars & Finite Fields",
        tags=("regular pentagon", "pentagram", "golden ratio", "finite field", "GF(19)", "spread sequence"),
        title="Regular Stars, Golden Pentagons & Finite-Field Polygons",
        subtitle="Exact Golden Quadrance Ratios Q_diag / Q_side = phi^2 and Rational Pentagons Over F_19",
        enunciation=(
            "A regular n-star of lines has consecutive spread s satisfying S_n(s) = 0; for n = 5, "
            "a regular pentagon P_0..P_4 has side-to-diagonal spread alpha = (5 - sqrt(5))/8 = (3 - phi)/4, "
            "exterior/star spread beta = (5 + sqrt(5))/8 = (2 + phi)/4, and exact golden quadrance ratio "
            "Q_diag / Q_side = beta / alpha = phi^2 = phi + 1, existing rationally in F_p^2 whenever "
            "5 and -1/5-dependent discriminants split (e.g. regular 5-stars in F_19)."
        ),
        signature_given=(
            "O : Point",
            "P_0 : Point",
        ),
        signature_steps=(
            "c = circle(O, P_0)",
            "P_1 = golden_pentagon_vertex(O, P_0, 1)",
            "P_2 = golden_pentagon_vertex(O, P_0, 2)",
            "P_3 = golden_pentagon_vertex(O, P_0, 3)",
            "P_4 = golden_pentagon_vertex(O, P_0, 4)",
            "pent = polygon(P_0, P_1, P_2, P_3, P_4)",
            "star = polygon(P_0, P_2, P_4, P_1, P_3)",
        ),
        synthesis=(
            "In classical Euclidean geometry over :math:`\\mathbb{Q}`, no regular pentagon can have purely "
            "rational vertex coordinates because :math:`S_5(s) = s(16s^2 - 20s + 5)^2 = 0` requires :math:`\\sqrt{5}`, "
            "and vertex placement on circle :g:`c` further involves :math:`\\sqrt{10 \\pm 2\\sqrt{5}}`. Yet in "
            "**Rational Trigonometry** (:cite:`Wildberger2005`), every intrinsic invariant of pentagon :g:`pent` "
            "and pentagram :g:`star` lives cleanly inside :math:`\\mathbb{Q}(\\phi)` without nested radicals: "
            "the spread at :g:`P_0` between two adjacent diagonals is :math:`\\alpha = (3 - \\phi)/4`, the spread "
            "between two adjacent sides is :math:`\\beta = (2 + \\phi)/4`, and the diagonal-to-side quadrance "
            "ratio is :math:`Q(P_0, P_2) / Q(P_0, P_1) = \\phi^2 = \\phi + 1`!",
            "Even more remarkably, over finite prime fields :math:`\\mathbb{F}_p` where :math:`5` is a quadratic "
            "residue (:math:`p \\equiv \\pm 1 \\pmod{5}`), :math:`\\sqrt{5}` is an **ordinary integer modulo** :math:`p`! "
            "In :math:`\\mathbb{F}_{19}`, :math:`9^2 = 81 \\equiv 5`, so the :term:`Pentagonal spread` roots "
            "become :math:`\\alpha \\equiv 16` and :math:`\\beta \\equiv 9`, producing exact 5-fold periodic "
            "spread orbits :math:`(0, 16, 9, 9, 16, 0)` with purely integer arithmetic!",
        ),
        math_blocks=(
            r"\frac{Q(P_0, P_2)}{Q(P_0, P_1)} = \frac{\beta}{\alpha} = \frac{5 + \sqrt{5}}{5 - \sqrt{5}} = \phi^2 = \phi + 1, "
            r"\qquad \alpha + \beta = \frac{5}{4}, \quad \alpha \beta = \frac{5}{64}",
            r"\text{In } \mathbb{F}_{19}\; (9^2 \equiv 5):\quad 16 s^2 - 20 s + 5 \equiv 16(s - 16)(s - 9) \pmod{19}",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`IV.11`, :ref:`XIII.8`, :ref:`XIII.11` (:cite:`EuclidElements`)"),
            ("GEOMETOR Elements", ":ref:`G.10`, :ref:`G.12`, :ref:`G.25`"),
            ("GEOMETOR Fundamentals", ":ref:`F.23 Golden Triangles <f-23>`, :ref:`F.40 Regular Polygons and Nested Radicals <f-40>`"),
            ("GEOMETOR Pacioli", "*De Divina Proportione* (:cite:`Pacioli1509`) & ``geometor/divine``"),
        ),
        depends_on=("W.05", "W.11", "W.17"),
    ),
    PrincipleSpec(
        num=20,
        code="W.20",
        slug="w-20",
        part=PART_III,
        category="Metrical Conics & Quadratic Loci",
        tags=("conic", "parabola", "quadrola", "grammola", "ribbon", "focus-directrix"),
        title="Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas",
        subtitle="Quadratic Focus-Directrix and Bifocal Loci Over Arbitrary Fields",
        enunciation=(
            "A conic is the zero locus of a quadratic polynomial proportion C = <a:b:c:d:e:f>; metrically, "
            "Q(X, l) = R defines a ribbon, Q(X, F_0) = Q(X, l_dir) defines a parabola, the squared-sum/difference "
            "bifocal locus A(Q(X, F_1), Q(X, F_2), S) = 0 defines a quadrola (unifying ellipses and hyperbolas "
            "into one irreducible algebraic curve), and Q(X, l_1) +/- Q(X, l_2) = R defines a grammola."
        ),
        signature_given=(
            "F_0 : Point",
            "D_1 : Point",
            "D_2 : Point",
            "F_1 : Point",
            "F_2 : Point",
        ),
        signature_steps=(
            "l_dir = line(D_1, D_2)",
            "V_p = midpoint(F_0, foot(F_0, l_dir))",
            "parabola = parabola_locus(F_0, l_dir)",
            "C_q = midpoint(F_1, F_2)",
            "quadrola = quadrola_locus(F_1, F_2, S)",
        ),
        synthesis=(
            "Classically, an ellipse (:math:`d_1 + d_2 = k`) and a hyperbola (:math:`|d_1 - d_2| = k`) are "
            "separated by absolute values and square roots. In Universal Geometry (:cite:`Wildberger2005`), "
            "squaring :math:`(\\pm\\sqrt{Q_1} \\pm \\sqrt{Q_2} \\pm \\sqrt{S}) = 0` via :person:`Archimedes <archimedes>`' "
            "function produces a **single algebraic curve**—the :term:`quadrola` :g:`quadrola` centered at "
            ":g:`C_q` with foci :g:`F_1`, :g:`F_2`—given by :math:`\\mathcal{A}(Q(X, F_1), Q(X, F_2), S) = 0`! "
            "Over :math:`\\mathbb{R}`, the same equation defines an ellipse when :math:`S > Q(F_1, F_2)` and a "
            "two-branched hyperbola when :math:`0 < S < Q(F_1, F_2)`, while over :math:`\\mathbb{F}_p` both regimes "
            "coexist seamlessly without ordering!",
            "Similarly, equating point-to-focus quadrance :math:`Q(X, F_0)` and point-to-directrix quadrance "
            ":math:`Q(X, \\ell_{\\text{dir}})` yields the :term:`parabola` :g:`parabola` with vertex :g:`V_p` "
            "and focus :g:`F_0` on non-null directrix :g:`l_dir`, while constant quadrance to a single line "
            "yields a :term:`ribbon` (two parallel lines) and constant sum/difference of quadrances to two "
            "lines yields a :term:`grammola`.",
        ),
        math_blocks=(
            r"\text{Parabola:}\quad Q(X, F_0) = Q(X, \ell_{\text{dir}}) \iff "
            r"(a^2 + b^2)\big((x - x_0)^2 + (y - y_0)^2\big) = (a x + b y + c)^2",
            r"\text{Quadrola:}\quad \mathcal{A}\big(Q(X, F_1),\; Q(X, F_2),\; S\big) = 0, \qquad "
            r"\text{Grammola:}\quad Q(X, \ell_1) \pm Q(X, \ell_2) = R",
        ),
        canon_links=(
            ("Classical Canon", ":person:`Apollonius <apollonius>` (*Conics*, Books I–III)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`"),
            ("GEOMETOR Fundamentals", ":ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.17 Ellipse <f-17>`, :ref:`F.37 Euler's Inradius Parabola <f-37>`"),
            ("Universal Unification", "Ellipses and hyperbolas share the single polynomial ``A(Q_1, Q_2, S) = 0``"),
        ),
        depends_on=("W.03", "W.07"),
    ),
    PrincipleSpec(
        num=21,
        code="W.21",
        slug="w-21",
        part=PART_III,
        category="Algebraic Tangents & Optical Reflection",
        tags=("Taylor conic", "tangent", "parabola reflection", "quadrola reflection", "optics"),
        title="Taylor Conics, Algebraic Tangents & Optical Reflection Laws",
        subtitle="Derivative-Free Tangent Proportions and Exact Equal-Spread Focal Reflections",
        enunciation=(
            "Translating any conic f(x, y) = 0 to a point A = [x_0, y_0] on the conic isolates a unique "
            "linear term l_1(x - x_0, y - y_0) = 0 defining its algebraic tangent t_tan without limits; "
            "for a parabola, t_tan is the perpendicular bisector of focus F_0 and directrix foot D_0 "
            "(giving equal spreads with F_0 A and the axis), and for a quadrola, t_tan makes equal spreads "
            "with both focal lines F_1 P_q and F_2 P_q."
        ),
        signature_given=(
            "F_0 : Point",
            "D_1 : Point",
            "D_2 : Point",
            "A : Point",
        ),
        signature_steps=(
            "l_dir = line(D_1, D_2)",
            "parabola = parabola_locus(F_0, l_dir)",
            "D_0 = foot(A, l_dir)",
            "t_tan = perp_bisector(F_0, D_0)",
            "l_in = line(F_0, A)",
            "l_out = line(D_0, A)",
        ),
        synthesis=(
            "Over finite or discrete fields there are no limits :math:`\\lim_{h \\to 0}`, yet conics possess "
            "exact tangents! Expanding :math:`f(x_0 + u, y_0 + v) = f(x_0, y_0) + \\ell_1(u, v) + q_2(u, v)` "
            "(the **Taylor Conic Translation** of :person:`Brook Taylor <taylor>`, :cite:`Wildberger2005`) "
            "produces the algebraic tangent line :math:`\\ell_A = \\langle 2 a x_0 + b y_0 + d : b x_0 + 2 c y_0 + e : "
            "d x_0 + e y_0 + 2 f \\rangle` whenever :math:`A = [x_0, y_0]` is non-singular.",
            "Applied to :g:`parabola` (focus :g:`F_0`, directrix :g:`l_dir`), the tangent :g:`t_tan` at :g:`A` "
            "is literally the **perpendicular bisector** of :g:`F_0` and the directrix foot :g:`D_0`! Since "
            ":math:`D_0 A` (:g:`l_out`) is perpendicular to :g:`l_dir` (hence parallel to the parabola's axis), "
            "reflection symmetry across :g:`t_tan` immediately proves the **Parabola Reflection Theorem** "
            ":math:`s(t_{\\text{tan}}, F_0 A) = s(t_{\\text{tan}}, D_0 A)` over every field! Analogously, at any "
            "point :g:`P_q` on a :term:`quadrola` :g:`quadrola` with foci :g:`F_1`, :g:`F_2`, the algebraic "
            "tangent :g:`t_q` satisfies :math:`s(t_q, F_1 P_q) = s(t_q, F_2 P_q)`.",
        ),
        math_blocks=(
            r"\ell_A = \langle 2 a x_0 + b y_0 + d :\; b x_0 + 2 c y_0 + e :\; d x_0 + e y_0 + 2 f \rangle",
            r"s(t_{\text{tan}}, F_0 A) = s(t_{\text{tan}}, D_0 A), \qquad "
            r"s(t_q, F_1 P_q) = s(t_q, F_2 P_q)",
        ),
        canon_links=(
            ("Classical Canon", ":person:`Apollonius <apollonius>` (*Conics* III.48) & :person:`Diocles <diocles>` (*On Burning Mirrors*)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`"),
            ("GEOMETOR Fundamentals", ":ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.39 Pole and Polar with Respect to a Triangle <f-39>`"),
            ("Algebraic Geometry", "Purely polynomial tangent space over ``Q`` and ``F_p`` without calculus"),
        ),
        depends_on=("W.02", "W.03", "W.20"),
    ),
    PrincipleSpec(
        num=22,
        code="W.22",
        slug="w-22",
        part=PART_III,
        category="Projective Geometry & Harmonic Ranges",
        tags=("cross-ratio", "harmonic range", "projective invariance", "Pappus", "perspectivity"),
        title="Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge",
        subtitle="Exact Equivalence of Line-Pencil Spread Cross-Ratio and Point-Range Quadrance Cross-Ratio",
        enunciation=(
            "If four concurrent lines r_1, r_2, r_3, r_4 through O_p meet a transversal l_a at collinear "
            "points A_1, A_2, A_3, A_4 and another transversal l_b at B_1, B_2, B_3, B_4, then the squared "
            "cross-ratio in quadrances (Q(A_1, A_3)*Q(A_2, A_4)) / (Q(A_1, A_4)*Q(A_2, A_3)) equals the "
            "pencil spread cross-ratio (s_13 * s_24) / (s_14 * s_23) and is invariant across all transversals."
        ),
        signature_given=(
            "O_p : Point",
            "A_1 : Point",
            "A_2 : Point",
            "B_1 : Point",
            "B_2 : Point",
        ),
        signature_steps=(
            "l_a = line(A_1, A_2)",
            "l_b = line(B_1, B_2)",
            "r_1 = line(O_p, A_1)",
            "r_2 = line(O_p, A_2)",
            "r_3 = line(O_p, A_3)",
            "r_4 = line(O_p, A_4)",
            "B_3 = meet(r_3, l_b)",
            "B_4 = meet(r_4, l_b)",
        ),
        synthesis=(
            ":person:`Pappus of Alexandria <pappus>` discovered that the cross-ratio of four collinear points "
            "is preserved under central projection (:cite:`CoxeterGreitzer1967`). In Rational Trigonometry "
            "(:cite:`Wildberger2005`), squaring the classical signed cross-ratio replaces signed lengths with "
            ":term:`quadrance` along transversals :g:`l_a` (:g:`A_1`, :g:`A_2`, :g:`A_3`, :g:`A_4`) and :g:`l_b` "
            "(:g:`B_1`, :g:`B_2`, :g:`B_3`, :g:`B_4`), and replaces directed sine ratios in the pencil of rays "
            ":g:`r_1`, :g:`r_2`, :g:`r_3`, :g:`r_4` through :g:`O_p` with pairwise :term:`spread`!",
            "Applying the :term:`Spread Law` to the four sub-triangles at apex :g:`O_p` cancels all radial "
            "quadrances :math:`Q(O_p, A_i)` and transversal spreads :math:`s(r_i, \\ell_a)` in a single stroke, "
            "proving :math:`R_Q(A_1, A_2; A_3, A_4) = R_s(r_1, r_2; r_3, r_4) = R_Q(B_1, B_2; B_3, B_4)`. "
            "When the signed cross-ratio is :math:`-1` (**harmonic conjugates**), its quadrance cross-ratio is "
            "identically :math:`(-1)^2 = 1`, directly uniting ``geometor/wildberger``, ``geometor/pappus``, and "
            ":ref:`F.25 Harmonic Conjugates <f-25>`!",
        ),
        math_blocks=(
            r"(A_1, A_2; A_3, A_4)_Q = \frac{Q(A_1, A_3)\, Q(A_2, A_4)}{Q(A_1, A_4)\, Q(A_2, A_3)} "
            r"= \frac{s(r_1, r_3)\, s(r_2, r_4)}{s(r_1, r_4)\, s(r_2, r_3)} = (B_1, B_2; B_3, B_4)_Q",
            r"\text{Harmonic Range } (A_1, A_2; A_3, A_4) = -1 \implies "
            r"Q(A_1, A_3)\, Q(A_2, A_4) = Q(A_1, A_4)\, Q(A_2, A_3)",
        ),
        canon_links=(
            ("Classical Canon", ":person:`Pappus of Alexandria <pappus>` (*Collection* Book VII) & :person:`Girard Desargues <desargues>`"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.5`"),
            ("GEOMETOR Fundamentals", ":ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.25 Harmonic Conjugates <f-25>` (:cite:`SeeligNotebooks`)"),
            ("Sister Codices", "``geometor/pappus`` (projective cross-ratio & harmonic ranges)"),
        ),
        depends_on=("W.01", "W.03", "W.04", "W.08"),
    ),
    PrincipleSpec(
        num=23,
        code="W.23",
        slug="w-23",
        part=PART_III,
        category="Universal Bilinear Forms & Chromogeometry",
        tags=("Chromogeometry", "blue metric", "red metric", "green metric", "Minkowski", "Euler line"),
        title="Chromogeometry & Universal Symmetric Bilinear Forms",
        subtitle="Harmonizing Blue Euclidean, Red Lorentzian, and Green Hyperbolic Triangle Centers",
        enunciation=(
            "Replacing the Euclidean quadratic form with any non-degenerate symmetric bilinear form M on F^2 "
            "preserves all Five Laws of Rational Trigonometry; in Chromogeometry—pairing Blue (dx^2 + dy^2), "
            "Red (dx^2 - dy^2), and Green (2*dx*dy) metrics on the same triangle—the three Euler lines "
            "concur at the centroid G, C_B C_R O_B C_G is a parallelogram, and N_B = (C_R + C_G)/2."
        ),
        signature_given=(
            "A_1 : Point",
            "A_2 : Point",
            "A_3 : Point",
        ),
        signature_steps=(
            "t = polygon(A_1, A_2, A_3)",
            "G = centroid(A_1, A_2, A_3)",
            "C_B, O_B, N_B = centers_blue(A_1, A_2, A_3)",
            "C_R, O_R = centers_red(A_1, A_2, A_3)",
            "C_G, O_G = centers_green(A_1, A_2, A_3)",
            "e_B = line(C_B, O_B)",
            "e_R = line(C_R, O_R)",
            "e_G = line(C_G, O_G)",
            "p_chromo = polygon(C_B, C_R, O_B, C_G)",
        ),
        synthesis=(
            "Because Rational Trigonometry uses only polynomial identities, **every theorem in Parts I–III "
            "generalizes to any symmetric bilinear form** :math:`u \\cdot_M v = u^T M v` (:math:`\\det M \\neq 0`) "
            "with :math:`s_M(\\ell_1, \\ell_2)` scaled by :math:`\\det M` (:cite:`Wildberger2005`, :cite:`Wildberger2008`)! "
            "In :person:`Norman J. Wildberger <wildberger>`'s :term:`Chromogeometry`, three canonical quadratic "
            "forms act simultaneously on the **same** planar triangle :g:`t`: **Blue** Euclidean "
            ":math:`Q_B = \\Delta x^2 + \\Delta y^2`, **Red** Lorentz/Minkowski :math:`Q_R = \\Delta x^2 - \\Delta y^2`, "
            "and **Green** rotated Lorentz :math:`Q_G = 2 \\Delta x \\Delta y`, satisfying **Pythagoras' Identity in "
            "Metrical Space** :math:`Q_B^2 = Q_R^2 + Q_G^2`!",
            "Computing the circumcenters (:g:`C_B`, :g:`C_R`, :g:`C_G`), orthocenters (:g:`O_B`, :g:`O_R`, :g:`O_G`), "
            "and Euler lines (:g:`e_B`, :g:`e_R`, :g:`e_G`) uncovers miraculous cross-metric harmonies: "
            "all three colored Euler lines concur at the metric-free :term:`centroid` :g:`G`; the quadrilateral "
            ":g:`p_chromo` (:math:`C_B C_R O_B C_G`) is **always a parallelogram** (:math:`C_B + O_B = C_R + C_G`); "
            "and the Blue nine-point center :g:`N_B` is the exact midpoint of the Red and Green circumcenters!",
        ),
        math_blocks=(
            r"Q_B = \Delta x^2 + \Delta y^2, \quad Q_R = \Delta x^2 - \Delta y^2, \quad "
            r"Q_G = 2 \Delta x \Delta y \implies Q_B^2 = Q_R^2 + Q_G^2",
            r"C_B + O_B = C_R + C_G, \qquad N_B = \frac{C_R + C_G}{2}, \qquad "
            r"N_R = \frac{C_B + C_G}{2}, \qquad N_G = \frac{C_B + C_R}{2}",
        ),
        canon_links=(
            ("Relativistic Canon", ":person:`Hermann Minkowski <minkowski>` (1908 spacetime metric ``dx^2 - dt^2``)"),
            ("Chromogeometry", ":cite:`Wildberger2008` (*Chromogeometry*, 12+ colored triangle center theorems)"),
            ("GEOMETOR Fundamentals", ":ref:`F.6 Centroid <f-06>`, :ref:`F.34 Nine-Point Circle <f-34>`"),
            ("Universal Invariance", "All Five Laws hold verbatim for Blue, Red, Green, and arbitrary ``M = M^T``"),
        ),
        depends_on=("W.06", "W.07", "W.08", "W.09", "W.10", "W.16"),
    ),
    PrincipleSpec(
        num=24,
        code="W.24",
        slug="w-24",
        part=PART_IV,
        category="Practical Triangle Solvers & Surveying",
        tags=("QQQ", "QQS", "QSS", "SQQ", "surveying", "Regiomontanus", "triangulation"),
        title="Exact Triangle Solvers & Surveying Triangulation",
        subtitle="Polynomial QQQ/QQS/QSS/SQQ Solvers, Inaccessible Heights, and Regiomontanus' Extremum",
        enunciation=(
            "Every classical triangle specification (QQQ, QQS, QSS, SQQ, and SSS up to scaling) reduces "
            "to linear or quadratic equations in quadrances and spreads with exact discriminant branching; "
            "applied to surveying, inaccessible heights and Regiomontanus' maximum-spread viewing problem "
            "resolve by pure rational algebra without trigonometric tables."
        ),
        signature_given=(
            "A : Point",
            "B : Point",
            "D_foot : Point",
            "C_top : Point",
        ),
        signature_steps=(
            "l_ground = line(A, D_foot)",
            "seg_tower = segment(D_foot, C_top)",
            "t_surv = polygon(A, B, C_top)",
            "P_obs = regiomontanus_optimal_point(D_foot, a, b)",
        ),
        synthesis=(
            "Classical triangle resolution (*SSS, SAS, ASA, SSA*) alternates awkwardly between inverse cosines, "
            "inverse sines, and tangent half-angle formulas, accumulating floating-point rounding at every step. "
            "In Rational Trigonometry (:cite:`Wildberger2005`), **QQQ** and **QSS** are purely rational in one "
            "step, while **SQQ** (Cross Law quadratic in :math:`Q_3`), **QQS** (Spread Law + Cross Law), and "
            "**SSS** (proportional quadrances :math:`Q_1 : Q_2 : Q_3 = s_1 : s_2 : s_3` once :math:`s_3` solves "
            "the :term:`Triple Spread Formula`) require at most a single quadratic root!",
            "In field surveying, measuring horizontal baseline :math:`Q(A, B)` along :g:`l_ground` and the "
            "elevation spreads from :g:`A` and :g:`B` to tower top :g:`C_top` above base :g:`D_foot` (:g:`seg_tower`, "
            "triangle :g:`t_surv`) determines the vertical quadrance :math:`Q(D_{\\text{foot}}, C_{\\text{top}})` "
            "by one rational formula. Likewise, :person:`Regiomontanus <regiomontanus>`' 1471 problem—maximizing "
            "the viewing spread of a vertical statue from :math:`y = a` to :math:`y = b`—completes the square "
            "without derivatives to yield optimal quadrance :math:`Q(D_{\\text{foot}}, P_{\\text{obs}}) = a b` "
            "at :g:`P_obs` with maximum spread :math:`(b - a)^2 / (a + b)^2`!",
        ),
        math_blocks=(
            r"\text{SQQ:}\quad (Q_3 - (Q_1 + Q_2))^2 - 4 Q_1 Q_2 (1 - s_3) = \mathcal{A}(Q_1, Q_2, Q_3) - 4 Q_1 Q_2 s_3 = 0",
            r"\text{Regiomontanus }(0 < a < b):\quad x_{\text{opt}}^2 = a b, \qquad "
            r"s_{\max} = \frac{(b - a)^2}{(a + b)^2}",
        ),
        canon_links=(
            ("Classical Surveying", ":person:`Regiomontanus <regiomontanus>` (1471 extremal viewing problem)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.4`, :ref:`G.7`"),
            ("GEOMETOR Fundamentals", ":ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.41 Geometric Problems and Extremal Loci <f-41>`, :ref:`F.54 HP-35s Triangle Program and Coordinate Scripts <f-54>`"),
            ("Computational Engine", "Implemented in ``geometor.wildberger.solvers``"),
        ),
        depends_on=("W.08", "W.09", "W.10"),
    ),
    PrincipleSpec(
        num=25,
        code="W.25",
        slug="w-25",
        part=PART_IV,
        category="Geodetic Resection & Two-Station Surveying",
        tags=("Snellius-Pothenot", "resection", "Hansen's problem", "surveying", "Alternate Spreads"),
        title="Snellius–Pothenot Resection & Hansen's Surveying Problem",
        subtitle="Exact Algebraic Coordinate Recovery from Unmeasured Stations via Spread Triples",
        enunciation=(
            "In Snellius-Pothenot resection, an observer P measuring spreads to three known beacons A, B, C "
            "lies on the algebraic intersection of two subtended-spread conics; in Hansen's problem, knowing "
            "one baseline quadrance Q(A, B) and four sighting spreads at unobserved stations C, D determines "
            "every side and diagonal quadrance exactly via Triple Spread Systems and Alternate Spreads."
        ),
        signature_given=(
            "A : Point",
            "B : Point",
            "C : Point",
            "D : Point",
        ),
        signature_steps=(
            "q_hansen = polygon(A, B, C, D)",
            "d_ac = segment(A, C)",
            "d_bd = segment(B, D)",
        ),
        synthesis=(
            "Two famous benchmarks of 17th–19th century geodesy showcase the computational power of Rational "
            "Trigonometry (:cite:`Wildberger2005`). In :person:`Willebrord Snellius <snellius>`' resection problem "
            "(1615, later revisited by Pothenot), an observer measures spreads :math:`r_1 = s(P A, P B)` and "
            ":math:`r_2 = s(P B, P C)` toward three known landmarks; each spread defines an explicit circumcircle "
            "chord locus (:ref:`W.17 <w-17>`), reducing resection to circle-circle intersection.",
            "In :person:`Peter Andreas Hansen <hansen>`'s two-station problem (1841), landmarks :g:`A` and :g:`B` "
            "have known quadrance :math:`Q(A, B) = 26`, while an observer at unknown stations :g:`C` and :g:`D` "
            "(:g:`q_hansen`, diagonals :g:`d_ac`, :g:`d_bd`) measures only the rational spreads among lines "
            ":math:`C A, C B, C D` and :math:`D A, D B, D C`. Combining two :term:`Triple Spread Formula` "
            "relations with the **Alternate Spreads** ratio (:ref:`W.14 <w-14>`) recovers all four unknown "
            "quadrances (:math:`Q(A,D)=17, Q(B,C)=17, Q(A,C)=41, Q(B,D)=25`) with zero rounding error!",
        ),
        math_blocks=(
            r"\frac{s(C A, C B)\, s(C B, C D)\, s(D A, A C)}{s(D A, D B)\, s(C D, C A)\, s(D B, B C)} = \frac{x}{y} "
            r"\quad (\text{Spread Law Ratio Elimination})",
            r"Q(A, D) = Q(A, B)\,\frac{y}{s(D A, D B)}, \qquad "
            r"Q(B, C) = Q(A, B)\,\frac{x}{s(C A, C B)}",
        ),
        canon_links=(
            ("Geodetic Canon", ":person:`Willebrord Snellius <snellius>` (1615) & :person:`Peter Andreas Hansen <hansen>` (1841)"),
            ("GEOMETOR Elements", ":ref:`G.3`, :ref:`G.7`"),
            ("GEOMETOR Fundamentals", ":ref:`F.7 Ceva and Menelaus <f-07>`, :ref:`F.12 Coaxial Circles <f-12>`"),
            ("Exact Solver", "Verified symbolically in ``geometor.wildberger.solvers.solve_hansen_benchmark``"),
        ),
        depends_on=("W.10", "W.14", "W.17", "W.24"),
    ),
    PrincipleSpec(
        num=26,
        code="W.26",
        slug="w-26",
        part=PART_IV,
        category="Algebraic Mechanics, Optics & Relativity",
        tags=("projectile motion", "parabola", "Snell's law", "refraction", "special relativity"),
        title="Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity",
        subtitle="Eliminating Transcendental Angles from Ballistics, Wave Refraction, and Lorentz Boosts",
        enunciation=(
            "A Galilean projectile launched from O with initial speed-squared v^2 and elevation spread s "
            "traces a parabola whose apex height h = v^2*s/(2*g), horizontal range quadrance Q_range = "
            "16*(v^4/(4*g^2))*s*(1 - s) = (v^4/g^2)*S_2(s), and focus-directrix geometry depend rationally "
            "on s; Snell's refraction law becomes n_1^2 * s_1 = n_2^2 * s_2 in spreads."
        ),
        signature_given=(
            "O : Point",
            "V_apex : Point",
            "R_range : Point",
        ),
        signature_steps=(
            "traj = projectile_parabola(O, V_apex, R_range)",
            "F_traj = focus(traj)",
            "l_dir = directrix(traj)",
            "l_iface = line(I_inc, P_ref)",
            "l_norm = altitude(l_iface, P_ref)",
        ),
        synthesis=(
            "Physics formulas are filled with :math:`\\sin^2\\theta`, :math:`\\cos^2\\theta`, and :math:`\\sin(2\\theta)` "
            "that become **purely algebraic** when expressed in :term:`quadrance` and :term:`spread` "
            "(:cite:`Wildberger2005`). For a projectile launched from :g:`O` landing at :g:`R_range` via apex "
            ":g:`V_apex` along trajectory :g:`traj` (focus :g:`F_traj`, directrix :g:`l_dir`), the horizontal "
            "range quadrance is governed directly by the logistic spread polynomial :math:`S_2(s) = 4 s (1 - s)`, "
            "immediately proving maximum range at :math:`s = 1/2` and equal ranges for complementary spreads "
            ":math:`s` and :math:`1 - s`!",
            "Across an optical interface :g:`l_iface` with normal :g:`l_norm` at :g:`P_ref` (incident from :g:`I_inc`, "
            "refracted toward :g:`T_trans`), :person:`Willebrord Snellius <snellius>`' law :math:`n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2` "
            "squares cleanly to the **linear spread proportion** :math:`n_1^2 s_1 = n_2^2 s_2`, with total "
            "internal reflection occurring precisely when :math:`(n_1^2 / n_2^2) s_1 > 1`! And in special "
            "relativity, Einstein's velocity addition and spacetime intervals are native instances of the "
            "Red Minkowski metric (:ref:`W.23 <w-23>`).",
        ),
        math_blocks=(
            r"y = x \sqrt{\frac{s}{1-s}} - \frac{g x^2}{2 v^2 (1 - s)}, \qquad "
            r"Q_{\text{range}} = \frac{v^4}{g^2} S_2(s) = \frac{4 v^4}{g^2} s(1 - s)",
            r"\text{Snell's Spread Law:}\quad n_1^2\, s_1 = n_2^2\, s_2, \qquad "
            r"s_{\text{crit}} = \frac{n_2^2}{n_1^2}\; (n_1 > n_2)",
        ),
        canon_links=(
            ("Physical Canon", ":person:`Galileo Galilei <galileo>` (1638) & :person:`Willebrord Snellius <snellius>` (1621)"),
            ("GEOMETOR Fundamentals", ":ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.22 Functions <f-22>`"),
            ("Chromogeometry Bridge", "Relativistic spacetime intervals instantiate the Red metric ``Q_R`` (:ref:`W.23 <w-23>`)"),
            ("Optics Bridge", "Complements parabolic mirror reflection in :ref:`W.21 <w-21>`"),
        ),
        depends_on=("W.05", "W.20", "W.21", "W.23"),
    ),
    PrincipleSpec(
        num=27,
        code="W.27",
        slug="w-27",
        part=PART_IV,
        category="3D Solid Geometry & The Five Platonic Solids",
        tags=("Platonic solids", "dihedral spread", "De Gua", "tetrahedron", "icosahedron", "dodecahedron"),
        title="3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads",
        subtitle="Miraculous Cancellation of sqrt(5): Purely Rational Face Spreads 8/9, 1, 8/9, 4/9, 4/5",
        enunciation=(
            "In 3D space over F, quadrance is Q(A_1, A_2) = dx^2 + dy^2 + dz^2, a right-corner tetrahedron "
            "satisfies De Gua's Quadrea Theorem A_base = A_xy + A_yz + A_zx, and the dihedral (face) spreads "
            "of ALL FIVE regular Platonic solids—Tetrahedron (8/9), Cube (1), Octahedron (8/9), Icosahedron "
            "(4/9), and Dodecahedron (4/5)—are exact rational numbers in Q!"
        ),
        signature_given=(
            "V_0 : Point",
            "V_1 : Point",
            "V_2 : Point",
            "V_3 : Point",
        ),
        signature_steps=(
            "t_base = polygon(V_1, V_2, V_3)",
            "M_edge = midpoint(V_1, V_2)",
            "s_ap1 = segment(V_0, M_edge)",
            "s_ap2 = segment(V_3, M_edge)",
        ),
        synthesis=(
            "Extending :term:`quadrance` to three dimensions (:math:`\\Delta x^2 + \\Delta y^2 + \\Delta z^2`) "
            "defines the :term:`dihedral spread` :math:`S(\\Pi_1, \\Pi_2)` between two planes via the spread of "
            "their normal vectors—equivalently, the spread between face apothems :g:`s_ap1` and :g:`s_ap2` "
            "meeting at edge midpoint :g:`M_edge` on base :g:`t_base` (:g:`V_0`, :g:`V_1`, :g:`V_2`, :g:`V_3`). "
            "For a right-corner tetrahedron, :person:`Pythagoras <pythagoras>`' theorem lifts directly to "
            "**De Gua's Quadrea Law**: the slant face quadrea equals the sum of the three orthogonal face quadreas!",
            "The crowning 3D revelation of :cite:`Wildberger2005` (Chapter 26) concerns the **five Platonic "
            "solids** celebrated in Book XIII of :person:`Euclid <euclid>`'s *Elements* and :person:`Luca Pacioli <pacioli>`'s "
            "*De Divina Proportione* (:cite:`Pacioli1509`). Although the icosahedron and dodecahedron require "
            "the pentagon spreads :math:`\\alpha, \\beta = (5 \\mp \\sqrt{5})/8` solving :math:`16 s^2 - 20 s + 5 = 0` "
            "(:ref:`W.19 <w-19>`), in the face-spread formulas :math:`S_{\\text{ico}} = \\frac{4\\beta}{3\\alpha}(1 - \\frac{\\beta}{3\\alpha}) = \\frac{4}{9}` "
            "and :math:`S_{\\text{dod}} = \\frac{4\\alpha - 1}{4\\alpha^2} = \\frac{4}{5}`, **every factor of** :math:`\\sqrt{5}` "
            "**cancels identically**, leaving five pure fractions in :math:`\\mathbb{Q}`: "
            ":math:`8/9, 1, 8/9, 4/9, 4/5`!",
        ),
        math_blocks=(
            r"16\alpha^2 - 20\alpha + 5 = 0 \implies S_{\text{ico}} = \frac{4\beta}{3\alpha}\!\left(1 - \frac{\beta}{3\alpha}\right) = \frac{4}{9}, \qquad "
            r"S_{\text{dod}} = \frac{4\alpha - 1}{4\alpha^2} = \frac{4}{5}",
            r"\big(S_{\text{tet}},\; S_{\text{cube}},\; S_{\text{oct}},\; S_{\text{ico}},\; S_{\text{dod}}\big) "
            r"= \left(\frac{8}{9},\; 1,\; \frac{8}{9},\; \frac{4}{9},\; \frac{4}{5}\right) \in \mathbb{Q}^5",
        ),
        canon_links=(
            ("Euclid's Elements", ":ref:`XI.4`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.15`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18` (:cite:`EuclidElements`)"),
            ("GEOMETOR Pacioli", "*De Divina Proportione* Platonic polyhedra plates (:cite:`Pacioli1509`)"),
            ("GEOMETOR Fundamentals", ":ref:`F.18 Equilateral Triangle <f-18>`, :ref:`F.23 Golden Triangles <f-23>`"),
            ("SymPy Proof", "Verified from exact 3D vertex coordinates in ``prove_platonic_dihedral_spreads()``"),
        ),
        depends_on=("W.05", "W.06", "W.07", "W.11", "W.19"),
    ),
    PrincipleSpec(
        num=28,
        code="W.28",
        slug="w-28",
        part=PART_IV,
        category="Rational Polar Coordinates & Algebraic Surfaces",
        tags=("rational polar", "lemniscate", "cardioid", "folium of Descartes", "ellipson"),
        title="Rational Polar Coordinates, Classical Curves & The Ellipson",
        subtitle="Parametrizing Curves by [s, Q] and Slicing the Cubic Triple-Spread Surface",
        enunciation=(
            "Replacing polar coordinates (r, theta) with rational polar coordinates [s, Q] where "
            "s = x^2 / (x^2 + y^2) (spread to the y-axis) and Q = x^2 + y^2 converts classical polar curves "
            "into exact polynomial relations—Bernoulli's lemniscate s = (Q + 2)/4 (or Q = a*(2*s - 1)), "
            "Descartes' folium (2*s - 1)^2*(s^2 - s + 1)^2*Q^2 - 18*s*(1 - s)*(1 - 3*s + 3*s^2)*Q + "
            "81*s^2*(1 - s)^2 = 0, and the deltoid/ellipson S_3(s) law—while "
            "(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 cuts out the tetrahedral Ellipson."
        ),
        signature_given=(
            "O : Point",
            "A_ref : Point",
        ),
        signature_steps=(
            "l_ref = line(O, A_ref)",
            "lemniscate = curve_lemniscate(O, l_ref)",
            "cardioid = curve_cardioid(O, l_ref)",
            "folium = curve_folium(O, l_ref)",
            "ellipson_slice = curve_ellipson_section()",
        ),
        synthesis=(
            "Traditional polar coordinates :math:`(r, \\theta)` mix a radical :math:`r = \\sqrt{x^2 + y^2}` "
            "with a transcendental angle :math:`\\theta`, defined only modulo :math:`2\\pi`. "
            ":person:`Norman J. Wildberger <wildberger>`'s **rational polar coordinates** :math:`[s, Q]` "
            "(:cite:`Wildberger2005`, Chapter 27 & Appendices A–B) pair the polar :term:`spread` "
            ":math:`s \\equiv x^2 / (x^2 + y^2)` measured from the vertical :math:`y`-axis :g:`l_ref` "
            "(through :g:`O` and :g:`A_ref`) with the radial :term:`quadrance` :math:`Q \\equiv x^2 + y^2`, "
            "aligning directly with navigation azimuths and 3D rational spherical coordinates.",
            "Classical curves simplify dramatically in :math:`[s, Q]`: :person:`Jakob Bernoulli <bernoulli>`'s "
            "figure-eight **lemniscate** (:g:`lemniscate`, :math:`(x^2 + y^2)^2 = a(x^2 - y^2)`) becomes the "
            "**linear** equation :math:`Q = a(2 s - 1)` (:math:`s = (Q + 2)/4` for :math:`a = 2`), while "
            ":person:`René Descartes <descartes>`' **folium** (:g:`folium`, :math:`x^3 + y^3 + 3 x y = 0`) "
            "eliminates quadrant signs via :math:`(1 - 3s + 3s^2)^2 - 4 s^3(1 - s)^3 = (2s - 1)^2(s^2 - s + 1)^2`, "
            "and the **cardioid** (:g:`cardioid`) admits a pure rational parametrization. "
            "Crowning the codex is the **Ellipson** (:g:`ellipson_slice`): the inflated-tetrahedron cubic surface "
            "inside :math:`[0, 1]^3` defined by the :term:`Triple Spread Formula`, whose horizontal slices "
            ":math:`s_3 = c` are ellipses inscribed in :math:`[0, 1]^2` (an exact circle at :math:`c = 1/2`!) "
            "and whose oblique slice :math:`s_1 + s_2 + s_3 = 2` satisfies :math:`S_3(s) = (36 Q - 5)^2 / (6 Q)^3`!",
        ),
        math_blocks=(
            r"s \equiv \frac{x^2}{x^2 + y^2}, \quad Q \equiv x^2 + y^2 \implies "
            r"\text{Lemniscate: } Q = a(2 s - 1), \quad "
            r"\text{Folium: } (2s - 1)^2(s^2 - s + 1)^2 Q^2 - 18 s(1 - s)(1 - 3s + 3s^2) Q + 81 s^2(1 - s)^2 = 0",
            r"\text{Ellipson }\mathcal{E} \subset [0, 1]^3:\quad "
            r"(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3 "
            r"\quad \Big(s_3 = \tfrac{1}{2} \implies \big(s_1 - \tfrac{1}{2}\big)^2 + \big(s_2 - \tfrac{1}{2}\big)^2 = \tfrac{1}{4}\Big)",
        ),
        canon_links=(
            ("Classical Curves", ":person:`Jakob Bernoulli <bernoulli>` (1694) & :person:`René Descartes <descartes>` (1638)"),
            ("GEOMETOR Fundamentals", ":ref:`F.22 Functions <f-22>`, :ref:`F.51 Apollonian Circles and the Problem of Apollonius <f-51>`"),
            ("Triple Spread Geometry", "Geometric locus of Law V (:ref:`W.10 <w-10>`) in spread space ``(s_1, s_2, s_3)``"),
            ("Universal Synthesis", "Completes the 28-Principle GEOMETOR Wildberger Codex"),
        ),
        depends_on=("W.03", "W.04", "W.10", "W.17", "W.20"),
    ),
)
