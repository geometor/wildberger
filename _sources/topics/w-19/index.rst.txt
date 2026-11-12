:order: 19
:type: topic
:category: Regular Polygons, Golden Stars & Finite Fields
:tags: regular pentagon, pentagram, golden ratio, finite field, GF(19), spread sequence

.. _w-19:

============================================================
W.19 Regular Stars, Golden Pentagons & Finite-Field Polygons
============================================================

*Exact Golden Quadrance Ratios Q_diag / Q_side = phi^2 and Rational Pentagons Over F_19*

.. enunciation::

   A regular n-star of lines has consecutive spread s satisfying S_n(s) = 0; for n = 5, a regular pentagon P_0..P_4 has side-to-diagonal spread alpha = (5 - sqrt(5))/8 = (3 - phi)/4, exterior/star spread beta = (5 + sqrt(5))/8 = (2 + phi)/4, and exact golden quadrance ratio Q_diag / Q_side = beta / alpha = phi^2 = phi + 1, existing rationally in F_p^2 whenever 5 and -1/5-dependent discriminants split (e.g. regular 5-stars in F_19).

.. figure:: w-19.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.19 (Regular Stars, Golden Pentagons & Finite-Field Polygons)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   P_0 : Point
   =====
   c = circle(O, P_0)
   P_1 = golden_pentagon_vertex(O, P_0, 1)
   P_2 = golden_pentagon_vertex(O, P_0, 2)
   P_3 = golden_pentagon_vertex(O, P_0, 3)
   P_4 = golden_pentagon_vertex(O, P_0, 4)
   pent = polygon(P_0, P_1, P_2, P_3, P_4)
   star = polygon(P_0, P_2, P_4, P_1, P_3)

Mathematical Synthesis
----------------------

In classical Euclidean geometry over :math:`\mathbb{Q}`, no regular pentagon can have purely rational vertex coordinates because :math:`S_5(s) = s(16s^2 - 20s + 5)^2 = 0` requires :math:`\sqrt{5}`, and vertex placement on circle :g:`c` further involves :math:`\sqrt{10 \pm 2\sqrt{5}}`. Yet in **Rational Trigonometry** (:cite:`Wildberger2005`), every intrinsic invariant of pentagon :g:`pent` and pentagram :g:`star` lives cleanly inside :math:`\mathbb{Q}(\phi)` without nested radicals: the spread at :g:`P_0` between two adjacent diagonals is :math:`\alpha = (3 - \phi)/4`, the spread between two adjacent sides is :math:`\beta = (2 + \phi)/4`, and the diagonal-to-side quadrance ratio is :math:`Q(P_0, P_2) / Q(P_0, P_1) = \phi^2 = \phi + 1`!

Even more remarkably, over finite prime fields :math:`\mathbb{F}_p` where :math:`5` is a quadratic residue (:math:`p \equiv \pm 1 \pmod{5}`), :math:`\sqrt{5}` is an **ordinary integer modulo** :math:`p`! In :math:`\mathbb{F}_{19}`, :math:`9^2 = 81 \equiv 5`, so the :term:`Pentagonal spread` roots become :math:`\alpha \equiv 16` and :math:`\beta \equiv 9`, producing exact 5-fold periodic spread orbits :math:`(0, 16, 9, 9, 16, 0)` with purely integer arithmetic!

Key Algebraic Identities
------------------------

.. math::

   \frac{Q(P_0, P_2)}{Q(P_0, P_1)} = \frac{\beta}{\alpha} = \frac{5 + \sqrt{5}}{5 - \sqrt{5}} = \phi^2 = \phi + 1, \qquad \alpha + \beta = \frac{5}{4}, \quad \alpha \beta = \frac{5}{64}

.. math::

   \text{In } \mathbb{F}_{19}\; (9^2 \equiv 5):\quad 16 s^2 - 20 s + 5 \equiv 16(s - 16)(s - 9) \pmod{19}

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Unit-circle side quadrance Q(P_0, P_1)``
     - ``3 - phi = (5 - sqrt(5))/2``
     - Equals 4 * alpha
   * - ``Unit-circle diagonal quadrance Q(P_0, P_2)``
     - ``2 + phi = (5 + sqrt(5))/2``
     - Equals 4 * beta
   * - ``Golden quadrance ratio Q_diag / Q_side``
     - ``phi^2 = phi + 1``
     - Exact divine proportion squared
   * - ``5-star spread orbits over GF(19)``
     - ``[0, 16, 9, 9, 16] & [0, 9, 16, 16, 9]``
     - 9^2 == 5 (mod 19) splits S_5(s)

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-19.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`IV.11`, :ref:`XIII.8`, :ref:`XIII.11` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.10`, :ref:`G.12`, :ref:`G.25`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.23 Golden Triangles <f-23>`, :ref:`F.40 Regular Polygons and Nested Radicals <f-40>`
   * - **GEOMETOR Pacioli**
     - *De Divina Proportione* (:cite:`Pacioli1509`) & ``geometor/divine``

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.05" [label="W.05\nSpread Polynomials S_n(s) & Pen...", fillcolor="#d8dee9", color="#4c566a", URL="../w-05/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#d8dee9", color="#4c566a", URL="../w-11/index.html"];
       "W.17" [label="W.17\nCircle Geometry: Subtended Spre...", fillcolor="#d8dee9", color="#4c566a", URL="../w-17/index.html"];
       "W.19" [label="W.19\nRegular Stars, Golden Pentagons...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-19/index.html"];
       "W.27" [label="W.27\n3D Planes, De Gua's Quadrea Law...", fillcolor="#e5e9f0", color="#777777", URL="../w-27/index.html"];
       "W.05" -> "W.19";
       "W.11" -> "W.19";
       "W.17" -> "W.19";
       "W.19" -> "W.27";
   }

**Depends on**: :ref:`W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads <w-05>`, :ref:`W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle <w-11>`, :ref:`W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points <w-17>`

**Required for**: :ref:`W.27 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads <w-27>`

.. toctree::
   :hidden:

   code
