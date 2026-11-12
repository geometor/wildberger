"""Scholarly apparatus generator (`glossary.rst`, `persons.rst`, `bibliography.rst`).

Maintains canonical definitions for Rational Trigonometry & Universal Geometry
terms, historical geometers, and bibliographic sources cited across the 28
principles of the GEOMETOR Wildberger Codex.
"""

from __future__ import annotations

from pathlib import Path

GLOSSARY_ENTRIES: tuple[tuple[tuple[str, ...], str], ...] = (
    (
        ("quadrance",),
        "The exact quadratic separation :math:`Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2` "
        "(or :math:`(A_2 - A_1)^T M (A_2 - A_1)` under a general symmetric bilinear form :math:`M`), "
        "replacing irrational Euclidean distance over any field :math:`F` (:math:`\\operatorname{char} F \\neq 2`).",
    ),
    (
        ("spread",),
        "The algebraic separation :math:`s(\\ell_1, \\ell_2) = (a_1 b_2 - a_2 b_1)^2 / ((a_1^2 + b_1^2)(a_2^2 + b_2^2))` "
        "between two unoriented non-null lines (equal to :math:`\\sin^2\\theta` over :math:`\\mathbb{R}`), "
        "vanishing when parallel and equaling :math:`1` when perpendicular.",
    ),
    (
        ("cross",),
        "The complementary line invariant :math:`c(\\ell_1, \\ell_2) = 1 - s(\\ell_1, \\ell_2) = "
        "(a_1 a_2 + b_1 b_2)^2 / ((a_1^2 + b_1^2)(a_2^2 + b_2^2))` (equal to :math:`\\cos^2\\theta` over :math:`\\mathbb{R}`).",
    ),
    (
        ("twist",),
        "The ratio :math:`t(\\ell_1, \\ell_2) = s(\\ell_1, \\ell_2) / c(\\ell_1, \\ell_2)` for two non-perpendicular "
        "non-null lines (equal to :math:`\\tan^2\\theta` over :math:`\\mathbb{R}`).",
    ),
    (
        ("turn",),
        "The signed rational tangent :math:`u(\\ell_1, \\ell_2) = (a_1 b_2 - a_2 b_1)/(a_1 a_2 + b_1 b_2)` "
        "between two ordered lines, whose square is the twist :math:`t = u^2` and which satisfies "
        ":math:`u_1 + u_2 + u_3 = u_1 u_2 u_3`.",
    ),
    (
        ("null line", "isotropic line"),
        "A line :math:`\\langle a : b : c \\rangle` whose quadratic norm :math:`a^2 + b^2` (or :math:`Q_M(u)`) "
        "vanishes, occurring in Euclidean geometry over fields containing :math:`\\sqrt{-1}` (such as :math:`\\mathbb{F}_{13}`) "
        "and along light cones in Red/Green relativistic metrics.",
    ),
    (
        ("quadrea", "Archimedes' function"),
        "The symmetric quadratic polynomial :math:`\\mathcal{A}(Q_1, Q_2, Q_3) = (Q_1 + Q_2 + Q_3)^2 - "
        "2(Q_1^2 + Q_2^2 + Q_3^2)` of a triangle's side quadrances, equal to :math:`16 \\Delta^2` over :math:`\\mathbb{R}`.",
    ),
    (
        ("Triple Quad Formula",),
        "Law II of Rational Trigonometry: three points with pairwise quadrances :math:`Q_1, Q_2, Q_3` "
        "are collinear if and only if :math:`\\mathcal{A}(Q_1, Q_2, Q_3) = 0`.",
    ),
    (
        ("Spread Law",),
        "Law III of Rational Trigonometry: in any non-null triangle, :math:`s_1 / Q_1 = s_2 / Q_2 = s_3 / Q_3 = 1 / (4 K)`.",
    ),
    (
        ("Cross Law",),
        "Law IV of Rational Trigonometry: :math:`(Q_1 + Q_2 - Q_3)^2 = 4 Q_1 Q_2 (1 - s_3) = 4 Q_1 Q_2 c_3`, "
        "replacing the Law of Cosines without angle-sign ambiguity.",
    ),
    (
        ("Triple Spread Formula",),
        "Law V of Rational Trigonometry: three coplanar non-null lines have pairwise spreads satisfying "
        ":math:`(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3`.",
    ),
    (
        ("Quadruple Quad Formula",),
        "The symmetric degree-4 relation :math:`Q(a, b, c, d) = ((a+b+c+d)^2 - 2(a^2+b^2+c^2+d^2))^2 - 64 a b c d = 0` "
        "satisfied by sequential quadrances of four collinear points.",
    ),
    (
        ("Quadruple Spread Formula",),
        "The degree-8 self-dual polynomial relation :math:`R(s_{12}, s_{23}, s_{34}, s_{14}) = 0` governing "
        "four coplanar lines, identically invariant under :math:`s_{ij} \\leftrightarrow 1 - s_{ij}`.",
    ),
    (
        ("spread polynomial", "spread polynomials"),
        "Wildberger's universal integer-coefficient polynomial family :math:`S_n(s) \\in \\mathbb{Z}[s]` "
        "satisfying :math:`S_0(s) = 0`, :math:`S_1(s) = s`, :math:`S_n(s) = 2(1 - 2s)S_{n-1}(s) - S_{n-2}(s) + 2s`, "
        "and semigroup composition :math:`S_n(S_m(s)) = S_{nm}(s)`.",
    ),
    (
        ("Pentagonal spread", "Pentagonal spreads"),
        "The two golden roots :math:`\\alpha = (5 - \\sqrt{5})/8 = (3 - \\phi)/4` and "
        ":math:`\\beta = (5 + \\sqrt{5})/8 = (2 + \\phi)/4` of :math:`S_5(s)/s = (16 s^2 - 20 s + 5)^2 = 0`, "
        "with exact ratio :math:`\\beta / \\alpha = \\phi^2`.",
    ),
    (
        ("golden ratio", "divine proportion"),
        "The positive root :math:`\\phi = (1 + \\sqrt{5})/2` of :math:`\\phi^2 = \\phi + 1`, governing "
        "Kepler's Golden Right Triangle (:ref:`W.11 <w-11>`), pentagonal spreads (:ref:`W.19 <w-19>`), "
        "and icosahedral/dodecahedral coordinates (:ref:`W.27 <w-27>`).",
    ),
    (
        ("vertex bisector", "square vertex"),
        "A line of equal quadrance :math:`Q(X, \\ell_1) = Q(X, \\ell_2)` to two intersecting lines; "
        "exists over :math:`F` iff the vertex is a *square vertex* where :math:`(a_1^2 + b_1^2)(a_2^2 + b_2^2)` is a square in :math:`F`.",
    ),
    (
        ("incenter", "inquadrance"),
        "One of the four symmetric points :math:`I_0, I_1, I_2, I_3` equidistant in quadrance (:math:`R_i`) "
        "from all three sidelines of a triangle whose vertices are square over :math:`F`.",
    ),
    (
        ("centroid",),
        "The affine, metric-independent center :math:`G = (A_1 + A_2 + A_3)/3` (:math:`X(2)` when :math:`\\operatorname{char} F \\neq 3`) "
        "where the three medians and all three Chromogeometry Euler lines concur.",
    ),
    (
        ("circumcenter", "circumquadrance"),
        "The unique intersection :math:`C` (:math:`X(3)`) of the side perpendicular bisectors of a non-null triangle, "
        "having equal quadrance :math:`K = Q_1 Q_2 Q_3 / \\mathcal{A}` (*circumquadrance*) to all three vertices.",
    ),
    (
        ("orthocenter",),
        "The unique intersection :math:`O` (:math:`X(4)`) of the three altitudes of a non-null triangle.",
    ),
    (
        ("nine-point circle",),
        "The universal circle centered at :math:`N = (C + O)/2` (:math:`X(5)`) of quadrance :math:`K_9 = K / 4` "
        "passing through the three side midpoints, three altitude feet, and three Euler midpoints.",
    ),
    (
        ("Stewart's theorem",),
        "The exact quadratic cevian identity relating :math:`Q(A_3, D)` for any point :math:`D` on :math:`A_1 A_2` "
        "to the side quadrances :math:`Q_1, Q_2, Q_3` and segment quadrances on :math:`A_1 A_2`.",
    ),
    (
        ("ribbon",),
        "The degree-2 conic locus :math:`Q(X, \\ell) = R` of points having constant quadrance :math:`R` to a fixed non-null line.",
    ),
    (
        ("parabola",),
        "The metrical conic locus :math:`Q(X, F_0) = Q(X, \\ell_{\\text{dir}})` of points equidistant in quadrance "
        "from a focus :math:`F_0` and a non-null directrix :math:`\\ell_{\\text{dir}}`.",
    ),
    (
        ("quadrola",),
        "Wildberger's irreducible bifocal conic :math:`\\mathcal{A}(Q(X, F_1), Q(X, F_2), S) = 0`, unifying "
        "classical ellipses (:math:`S > Q(F_1, F_2)`) and hyperbolas (:math:`0 < S < Q(F_1, F_2)`) into one algebraic curve.",
    ),
    (
        ("grammola",),
        "The metrical conic locus :math:`Q(X, \\ell_1) \\pm Q(X, \\ell_2) = R` relative to two non-null lines.",
    ),
    (
        ("Chromogeometry",),
        "Wildberger's triality of planar geometries acting on the same coordinates: Blue Euclidean (:math:`\\Delta x^2 + \\Delta y^2`), "
        "Red Minkowski (:math:`\\Delta x^2 - \\Delta y^2`), and Green hyperbolic (:math:`2 \\Delta x \\Delta y`).",
    ),
    (
        ("Hansen's problem",),
        "Peter Andreas Hansen's 1841 geodetic problem of determining all quadrances among two known landmarks "
        ":math:`A, B` and two unmeasured observer stations :math:`C, D` from baseline :math:`Q(A, B)` and four spreads at :math:`C, D`.",
    ),
    (
        ("dihedral spread",),
        "The spread :math:`S(\\Pi_1, \\Pi_2) = 1 - (n_1 \\cdot n_2)^2 / ((n_1 \\cdot n_1)(n_2 \\cdot n_2))` "
        "between two planes in 3D space, equal to pure rationals :math:`(8/9, 1, 8/9, 4/9, 4/5)` across all five Platonic solids.",
    ),
    (
        ("ellipson",),
        "The compact cubic algebraic surface inside :math:`[0, 1]^3` defined by the Triple Spread Formula "
        ":math:`(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3`.",
    ),
)

PERSONS_ENTRIES: tuple[tuple[str, str, str], ...] = (
    (
        "wildberger",
        "Norman J. Wildberger (b. 1955)",
        "Canadian-Australian mathematician at UNSW Sydney who formulated Rational Trigonometry, "
        "Universal Geometry (*Divine Proportions*, 2005), and Chromogeometry (2008).",
    ),
    (
        "euclid",
        "Euclid of Alexandria (fl. 300 BCE)",
        "Author of the thirteen books of the *Elements*, whose synthetic propositions from Books I–IV, "
        "VI, and XIII gain field-independent algebraic proofs in Universal Geometry.",
    ),
    (
        "pythagoras",
        "Pythagoras of Samos (c. 570–c. 495 BCE)",
        "Ancient Greek philosopher-geometer associated with Law I of Rational Trigonometry (:math:`Q_1 + Q_2 = Q_3 \\iff s_3 = 1`).",
    ),
    (
        "archimedes",
        "Archimedes of Syracuse (c. 287–c. 212 BCE)",
        "Hellenistic mathematician after whom Wildberger named Archimedes' function :math:`\\mathcal{A}(Q_1, Q_2, Q_3)` "
        "for collinearity and triangle quadrea.",
    ),
    (
        "apollonius",
        "Apollonius of Perga (c. 240–c. 190 BCE)",
        "Author of *Conics*, whose median theorem and focal conic reflections become derivative-free polynomial laws in :ref:`W.13 <w-13>`, :ref:`W.20 <w-20>`, and :ref:`W.21 <w-21>`.",
    ),
    (
        "diocles",
        "Diocles (c. 240–c. 180 BCE)",
        "Greek geometer whose *On Burning Mirrors* established the focal reflection property of the parabola.",
    ),
    (
        "heron",
        "Heron of Alexandria (c. 10–c. 70 CE)",
        "Geometer and engineer whose radical area formula squares cleanly into :math:`\\mathcal{A} = 16 \\Delta^2`.",
    ),
    (
        "menelaus",
        "Menelaus of Alexandria (c. 70–140 CE)",
        "Astronomer and geometer whose transversal theorem shares the exact multiplicative quadrance balance of Ceva's theorem (:ref:`W.14 <w-14>`).",
    ),
    (
        "ptolemy",
        "Claudius Ptolemy (c. 100–c. 170 CE)",
        "Author of the *Almagest*, whose cyclic quadrilateral diagonal theorem becomes :math:`\\mathcal{A}(Q_{12}Q_{34}, Q_{23}Q_{14}, Q_{13}Q_{24}) = 0` (:ref:`W.18 <w-18>`).",
    ),
    (
        "pappus",
        "Pappus of Alexandria (c. 290–c. 350 CE)",
        "Author of the *Synagoge* (*Collection*), establishing projective cross-ratio invariance (:ref:`W.22 <w-22>`).",
    ),
    (
        "brahmagupta",
        "Brahmagupta (598–c. 668 CE)",
        "Indian mathematician whose cyclic quadrilateral area formula (*Brahmasphutasiddhanta*, 628 CE) underpins cyclic quadrea.",
    ),
    (
        "regiomontanus",
        "Regiomontanus (Johannes Müller von Königsberg, 1436–1476)",
        "Renaissance astronomer and mathematician who posed the 1471 extremal viewing-angle problem solved algebraically in :ref:`W.24 <w-24>`.",
    ),
    (
        "pacioli",
        "Luca Pacioli (c. 1447–1517)",
        "Franciscan mathematician and author of *De Divina Proportione* (1509, illustrated by Leonardo da Vinci), celebrating :math:`\\phi` and the five Platonic solids.",
    ),
    (
        "galileo",
        "Galileo Galilei (1564–1642)",
        "Establisher of parabolic projectile kinematics (*Two New Sciences*, 1638), reformulated via :math:`S_2(s)` in :ref:`W.26 <w-26>`.",
    ),
    (
        "kepler",
        "Johannes Kepler (1571–1630)",
        "Astronomer and geometer whose Golden Right Triangle has pure golden-power quadrances :math:`(1, \\phi, \\phi^2)` and spreads :math:`(1/\\phi^2, 1/\\phi, 1)` (:ref:`W.11 <w-11>`).",
    ),
    (
        "snellius",
        "Willebrord Snellius (1580–1626)",
        "Dutch astronomer and geodesist who pioneered triangulation resection (1615, :ref:`W.25 <w-25>`) and the law of refraction (:math:`n_1^2 s_1 = n_2^2 s_2`, :ref:`W.26 <w-26>`).",
    ),
    (
        "desargues",
        "Girard Desargues (1591–1661)",
        "Founder of synthetic projective geometry and harmonic involution theory.",
    ),
    (
        "descartes",
        "René Descartes (1596–1650)",
        "Founder of analytic coordinate geometry (*La Géométrie*, 1637) and discoverer of the folium of Descartes (:ref:`W.28 <w-28>`).",
    ),
    (
        "ceva",
        "Giovanni Ceva (1647–1734)",
        "Italian geometer who proved Ceva's concurrency theorem (*De lineis rectis*, 1678, :ref:`W.14 <w-14>`).",
    ),
    (
        "bernoulli",
        "Jakob Bernoulli (1655–1705)",
        "Swiss mathematician who introduced the lemniscate (:math:`Q = a(1 - 2s)` in rational polar coordinates, :ref:`W.28 <w-28>`).",
    ),
    (
        "taylor",
        "Brook Taylor (1685–1731)",
        "English mathematician whose polynomial shift expansion defines derivative-free algebraic tangents to conics (:ref:`W.21 <w-21>`).",
    ),
    (
        "euler",
        "Leonhard Euler (1707–1783)",
        "Proved the collinearity of triangle centers along the Euler line (:ref:`W.16 <w-16>`) and the four-point planar distance relation (:ref:`W.18 <w-18>`).",
    ),
    (
        "stewart",
        "Matthew Stewart (1717–1785)",
        "Scottish geometer who published Stewart's cevian theorem (*Some General Theorems*, 1746, :ref:`W.13 <w-13>`).",
    ),
    (
        "hansen",
        "Peter Andreas Hansen (1795–1874)",
        "Danish-German astronomer and geodesist who formulated Hansen's two-station surveying problem (1841, :ref:`W.25 <w-25>`).",
    ),
    (
        "chebyshev",
        "Pafnuty Chebyshev (1821–1894)",
        "Russian mathematician whose orthogonal polynomials :math:`T_n` rescale onto Wildberger's spread polynomials :math:`S_n(s)` (:ref:`W.05 <w-05>`).",
    ),
    (
        "minkowski",
        "Hermann Minkowski (1864–1909)",
        "Formulated relativistic spacetime geometry (1908), corresponding to the Red metric :math:`Q_R = \\Delta x^2 - \\Delta y^2` of Chromogeometry (:ref:`W.23 <w-23>`).",
    ),
    (
        "conway",
        "John Horton Conway (1937–2020)",
        "Introduced Conway triangle notation (:math:`S_A, S_B, S_C`), matching the quadratic Cross Law numerators :math:`(Q_j + Q_k - Q_i)/2`.",
    ),
    (
        "seelig",
        "Fred Seelig",
        "Compiler of the archival notebooks and spreadsheets preserved in ``geometor/fundamentals``.",
    ),
)

BIBLIOGRAPHY_ENTRIES: tuple[tuple[str, str], ...] = (
    (
        "Wildberger2005",
        "Wildberger, Norman J. *Divine Proportions: Rational Trigonometry to Universal Geometry*. "
        "Sydney: Wild Egg Books, 2005.",
    ),
    (
        "Wildberger2007",
        "Wildberger, Norman J. 'A Rational Approach to Trigonometry.' *Math Horizons* 15, no. 2 "
        "(November 2007): 16–20.",
    ),
    (
        "Wildberger2008",
        "Wildberger, Norman J. 'Chromogeometry.' *The Mathematical Intelligencer* / UNSW Preprint "
        "(2008–2009).",
    ),
    (
        "Wildberger2009",
        "Wildberger, Norman J. 'Affine and Projective Universal Geometry.' *Journal of Geometry* "
        "(UNSW Universal Geometry series, 2009).",
    ),
    (
        "Artin1957",
        "Artin, Emil. *Geometric Algebra*. Interscience Tracts in Pure and Applied Mathematics #3. "
        "New York: Interscience Publishers, 1957.",
    ),
    (
        "CoxeterGreitzer1967",
        "Coxeter, H. S. M., and S. L. Greitzer. *Geometry Revisited*. New Mathematical Library #19. "
        "Washington, DC: Mathematical Association of America, 1967.",
    ),
    (
        "EuclidElements",
        "Euclid. *The Thirteen Books of Euclid's Elements*, translated with commentary by Sir Thomas L. Heath, "
        "2nd ed. Cambridge University Press, 1926 (Dover reprint, 1956).",
    ),
    (
        "Kimberling1998",
        "Kimberling, Clark. 'Triangle Centers and Central Triangles.' *Congressus Numerantium* 129 "
        "(1998): 1–295; and *Encyclopedia of Triangle Centers (ETC)*.",
    ),
    (
        "Pacioli1509",
        "Pacioli, Luca. *De Divina Proportione*. Venice: Paganino Paganini, 1509 (digital synthesis in ``geometor/pacioli``).",
    ),
    (
        "SeeligNotebooks",
        "Seelig, Fred. *Geometric Notebooks and OpenDocument Spreadsheets* (archival synthesis in ``geometor/fundamentals``).",
    ),
    (
        "SnapperTroyer1971",
        "Snapper, Ernst, and Robert J. Troyer. *Metric Affine Geometry*. New York: Academic Press, 1971 (Dover reprint, 1989).",
    ),
)


def write_apparatus_files(docsrc_dir: Path) -> list[Path]:
    """Write `glossary.rst`, `persons.rst`, and `bibliography.rst` into `docsrc_dir`.

    Args:
        docsrc_dir: Target `docsrc/` directory path.

    Returns:
        List of written file paths.
    """
    docsrc_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    # 1. glossary.rst
    g_lines = [
        ":navigation: header",
        ":order: 30",
        "",
        ".. _glossary:",
        "",
        "========",
        "Glossary",
        "========",
        "",
        "Algebraic definitions and quadratic invariants referenced across the 28",
        "principles of the **GEOMETOR Wildberger** codex.",
        "",
        ".. glossary::",
        "   :sorted:",
        "",
    ]
    for terms, desc in GLOSSARY_ENTRIES:
        for t in terms:
            g_lines.append(f"   {t}")
        g_lines.append(f"      {desc}")
        g_lines.append("")
    g_path = docsrc_dir / "glossary.rst"
    g_path.write_text("\n".join(g_lines), encoding="utf-8")
    written.append(g_path)

    # 2. persons.rst
    p_lines = [
        ":navigation: header",
        ":order: 40",
        "",
        ".. _persons:",
        "",
        "=======",
        "Persons",
        "=======",
        "",
        "Mathematicians, geometers, astronomers, and physicists connected to",
        "Rational Trigonometry and Universal Geometry.",
        "",
    ]
    for slug, heading, bio in PERSONS_ENTRIES:
        p_lines.extend(
            [
                f".. _person-{slug}:",
                f".. _{slug}:",
                "",
                heading,
                "-" * len(heading),
                "",
                bio,
                "",
            ]
        )
    p_path = docsrc_dir / "persons.rst"
    p_path.write_text("\n".join(p_lines), encoding="utf-8")
    written.append(p_path)

    # 3. bibliography.rst
    b_lines = [
        ":navigation: header",
        ":order: 50",
        "",
        ".. _bibliography:",
        "",
        "============",
        "Bibliography",
        "============",
        "",
        "Foundational monographs, historical treatises, and GEOMETOR sister",
        "archives referenced throughout this codex.",
        "",
    ]
    for key, ref_text in BIBLIOGRAPHY_ENTRIES:
        b_lines.extend(
            [
                f".. _cite-{key}:",
                f".. _{key}:",
                "",
                key,
                "-" * len(key),
                "",
                ref_text,
                "",
            ]
        )
    b_path = docsrc_dir / "bibliography.rst"
    b_path.write_text("\n".join(b_lines), encoding="utf-8")
    written.append(b_path)

    return written
