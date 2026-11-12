:order: 17
:type: topic
:category: Circle Geometry & Rational Parametrization
:tags: Thales, inscribed spread, power of a point, rational circle, stereographic

.. _w-17:

==========================================================================
W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points
==========================================================================

*Thales' Right-Diameter Law, Inscribed Spread s_2(s), and Stereographic Parametrization*

.. enunciation::

   On a circle Q(X, O_c) = K over F, a diameter subtends spread 1 at every other circle point (Thales), any chord P_1 P_2 subtends constant spread s_3 at the circumference with Q(P_1, P_2) = 4*K*s_3 and central spread s(O_c P_1, O_c P_2) = S_2(s_3) = 4*s_3*(1 - s_3), and any external or internal point A_0 has invariant secant quadrance product Q(A_0, P_1)*Q(A_0, P_2) = (Q(A_0, O_c) - K)^2.

.. figure:: w-17.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.17 (Circle Geometry: Subtended Spreads, Secant Products & Rational Points)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O_c : Point
   P_1 : Point
   P_2 : Point
   B : Point
   A_0 : Point
   =====
   c = circle(O_c, P_1)
   l_sec1 = line(A_0, P_1)
   l_sec2 = line(A_0, B)
   Q_1 = meet_other(c, l_sec1, P_1)
   Q_2 = meet_other(c, l_sec2, B)

Mathematical Synthesis
----------------------

Classical circle theorems suffer from case distinctions between acute and obtuse inscribed angles (:math:`\theta` vs. :math:`\pi - \theta`). Because supplementary rays define the **same line**, every point :g:`B` on circle :g:`c` (centered at :g:`O_c`) subtends the **exact same spread** :math:`s(B P_1, B P_2) = Q(P_1, P_2) / (4 K)` on chord :math:`P_1 P_2`, regardless of which arc :g:`B` inhabits (:cite:`Wildberger2005`)! And the central spread at :g:`O_c` is governed by the second :term:`spread polynomial` :math:`S_2(s_3) = 4 s_3 (1 - s_3)`.

Similarly, Euclid's intersecting chords/secants theorem (:ref:`III.35`, :ref:`III.36`) becomes the **Equal Products Theorem**: lines :g:`l_sec1` and :g:`l_sec2` through :g:`A_0` cut :g:`c` at (:g:`P_1`, :g:`Q_1`) and (:g:`B`, :g:`Q_2`) with invariant quadrance product :math:`(Q(A_0, O_c) - K)^2`. Projecting from :math:`[-1, 0]` parametrizes the unit circle by :math:`\left[\frac{1 - t^2}{1 + t^2}, \frac{2 t}{1 + t^2}\right]`, generating all Pythagorean triples over :math:`\mathbb{Q}` and counting :math:`p \mp 1` points on circles over :math:`\mathbb{F}_p`.

Key Algebraic Identities
------------------------

.. math::

   s(B P_1, B P_2) = \frac{Q(P_1, P_2)}{4 K} = s_3, \qquad s(O_c P_1, O_c P_2) = S_2(s_3) = 4 s_3 (1 - s_3)

.. math::

   Q(A_0, P_1)\, Q(A_0, Q_1) = Q(A_0, B)\, Q(A_0, Q_2) = \big(Q(A_0, O_c) - K\big)^2, \qquad U(t) = \left[\frac{1 - t^2}{1 + t^2},\; \frac{2 t}{1 + t^2}\right]

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Inscribed spread invariance s(B) == s(Q_1)``
     - ``1/2 == 1/2``
     - Equals Q(P_1, P_2)/(4K) = 50/100 = 1/2
   * - ``Central spread s(O_c P_1, O_c P_2)``
     - ``1``
     - Matches S_2(1/2) = 1
   * - ``Equal secant products from A_0``
     - ``275625/256 == 275625/256``
     - Matches (Q(A_0,O_c) - K)^2 = 275625/256
   * - ``Rational unit circle point count in GF(17), GF(19)``
     - ``16 (= 17-1), 20 (= 19+1)``
     - p - 1 when -1 square, p + 1 otherwise

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-17.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`III.20`, :ref:`III.21`, :ref:`III.31`, :ref:`III.35`, :ref:`III.36`, :ref:`X.29` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.7`, :ref:`G.11`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.8 Chord Intersection <f-08>`, :ref:`F.9 Circle Equations <f-09>`, :ref:`F.33 Euclidean (m, n) Generators <f-33>`
   * - **Number Theory Bridge**
     - Counts ``p + 1`` (when ``-1`` non-square) or ``p - 1`` rational points over ``F_p``

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.05" [label="W.05\nSpread Polynomials S_n(s) & Pen...", fillcolor="#d8dee9", color="#4c566a", URL="../w-05/index.html"];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#d8dee9", color="#4c566a", URL="../w-06/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.17" [label="W.17\nCircle Geometry: Subtended Spre...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-17/index.html"];
       "W.18" [label="W.18\nCyclic Quadrilaterals, Ptolemy...", fillcolor="#e5e9f0", color="#777777", URL="../w-18/index.html"];
       "W.19" [label="W.19\nRegular Stars, Golden Pentagons...", fillcolor="#e5e9f0", color="#777777", URL="../w-19/index.html"];
       "W.25" [label="W.25\nSnellius–Pothenot Resection & H...", fillcolor="#e5e9f0", color="#777777", URL="../w-25/index.html"];
       "W.28" [label="W.28\nRational Polar Coordinates, Cla...", fillcolor="#e5e9f0", color="#777777", URL="../w-28/index.html"];
       "W.05" -> "W.17";
       "W.06" -> "W.17";
       "W.08" -> "W.17";
       "W.17" -> "W.18";
       "W.17" -> "W.19";
       "W.17" -> "W.25";
       "W.17" -> "W.28";
   }

**Depends on**: :ref:`W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads <w-05>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`

**Required for**: :ref:`W.18 Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation <w-18>`, :ref:`W.19 Regular Stars, Golden Pentagons & Finite-Field Polygons <w-19>`, :ref:`W.25 Snellius–Pothenot Resection & Hansen's Surveying Problem <w-25>`, :ref:`W.28 Rational Polar Coordinates, Classical Curves & The Ellipson <w-28>`

.. toctree::
   :hidden:

   code
