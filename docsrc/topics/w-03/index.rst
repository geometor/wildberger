:order: 3
:type: topic
:category: Foundational Quadratic Invariants
:tags: quadrance, midpoint, parallelogram, perpendicular bisector, null line

.. _w-03:

====================================================
W.03 Quadrance, Midpoints & Point-to-Line Separation
====================================================

*Replacing Irrational Euclidean Distance with Exact Quadratic Point Separation*

.. enunciation::

   The quadrance between A_1 = [x_1, y_1] and A_2 = [x_2, y_2] is the quadratic form Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2; midpoint M divides the quadrance by 4, the locus Q(X, A_1) = Q(X, A_2) is the linear perpendicular bisector, and the quadrance from A_0 to a non-null line l = <a : b : c> is (a*x_0 + b*y_0 + c)^2 / (a^2 + b^2).

.. figure:: w-03.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.03 (Quadrance, Midpoints & Point-to-Line Separation)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_0 : Point
   =====
   l = line(A_1, A_2)
   M = midpoint(A_1, A_2)
   b_12 = perp_bisector(A_1, A_2)
   F_0 = foot(A_0, l)

Mathematical Synthesis
----------------------

:term:`Quadrance` is the primary point-separation invariant of Rational Trigonometry (:cite:`Wildberger2005`). Because :math:`Q(A_1, A_2)` avoids square roots, points in :math:`F^2` always have separation in :math:`F`. Scaling a displacement by :math:`\lambda` multiplies its quadrance by :math:`\lambda^2`, so the midpoint :g:`M` of :g:`A_1` and :g:`A_2` satisfies :math:`Q(A_1, M) = Q(M, A_2) = Q(A_1, A_2)/4`.

Equating quadrances :math:`Q(X, A_1) = Q(X, A_2)` cancels the quadratic terms :math:`x^2 + y^2`, yielding the linear perpendicular bisector :g:`b_12` even when :math:`Q(A_1, A_2)` is not a square in :math:`F`! Similarly, the quadrance from an external point :g:`A_0` to line :g:`l` equals :math:`Q(A_0, F_0)`, and in any parallelogram the diagonal quadrances sum to twice the sum of adjacent side quadrances. Over fields where :math:`-1 = i^2` (such as :math:`\mathbb{F}_{13}` with :math:`5^2 \equiv -1`), non-coincident points along a :term:`null line` satisfy :math:`Q(A_1, A_2) = 0`.

Key Algebraic Identities
------------------------

.. math::

   Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2, \qquad Q(A_1, M) = Q(M, A_2) = \frac{Q(A_1, A_2)}{4}

.. math::

   Q(A_0, \ell) = \frac{(a x_0 + b y_0 + c)^2}{a^2 + b^2}, \qquad Q_{13} + Q_{24} = 2(Q_{12} + Q_{23})

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Segment quadrance Q(A_1, A_2)``
     - ``40``
     - No square root of 40 needed
   * - ``Midpoint quadrance Q(A_1, M) = Q/4``
     - ``10``
     - Verified 4 * 10 == 40
   * - ``Perpendicular bisector b_12``
     - ``<-6 : -2 : 28>``
     - Linear locus Q(X,A_1)=Q(X,A_2)
   * - ``Point-to-line quadrance Q(A_0, l)``
     - ``98/5``
     - Matches Q(A_0, F_0) = 98/5
   * - ``Null segment [0,0]->[1,5] over GF(13)``
     - ``1^2 + 5^2 = 26 == 0 (mod 13)``
     - Non-trivial isotropic line

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-03.svg``)
   * - **Thematic Part**
     - Part I: Preliminaries & Foundational Invariants
   * - **Euclid's Elements**
     - :ref:`I.10`, :ref:`I.47`, :ref:`II.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.1`, :ref:`G.3`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.9 Circle Equations <f-09>`
   * - **Sister Codices**
     - ``geometor/model`` (exact polynomial distance/quadrance algebra)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.01" [label="W.01\nPlanar Points, Line Proportions...", fillcolor="#d8dee9", color="#4c566a", URL="../w-01/index.html"];
       "W.03" [label="W.03\nQuadrance, Midpoints & Point-to...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-03/index.html"];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#e5e9f0", color="#777777", URL="../w-04/index.html"];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#e5e9f0", color="#777777", URL="../w-06/index.html"];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#e5e9f0", color="#777777", URL="../w-07/index.html"];
       "W.12" [label="W.12\nVertex Bisectors, Square Vertic...", fillcolor="#e5e9f0", color="#777777", URL="../w-12/index.html"];
       "W.13" [label="W.13\nStewart's Theorem, Median Quadr...", fillcolor="#e5e9f0", color="#777777", URL="../w-13/index.html"];
       "W.15" [label="W.15\nCircumcenter, Orthocenter & Uni...", fillcolor="#e5e9f0", color="#777777", URL="../w-15/index.html"];
       "W.20" [label="W.20\nMetrical Conics: Circles, Ribbo...", fillcolor="#e5e9f0", color="#777777", URL="../w-20/index.html"];
       "W.21" [label="W.21\nTaylor Conics, Algebraic Tangen...", fillcolor="#e5e9f0", color="#777777", URL="../w-21/index.html"];
       "W.22" [label="W.22\nProjective Cross-Ratio, Harmoni...", fillcolor="#e5e9f0", color="#777777", URL="../w-22/index.html"];
       "W.28" [label="W.28\nRational Polar Coordinates, Cla...", fillcolor="#e5e9f0", color="#777777", URL="../w-28/index.html"];
       "W.01" -> "W.03";
       "W.03" -> "W.04";
       "W.03" -> "W.06";
       "W.03" -> "W.07";
       "W.03" -> "W.12";
       "W.03" -> "W.13";
       "W.03" -> "W.15";
       "W.03" -> "W.20";
       "W.03" -> "W.21";
       "W.03" -> "W.22";
       "W.03" -> "W.28";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`

**Required for**: :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`, :ref:`W.12 Vertex Bisectors, Square Vertices & The Four Incenters <w-12>`, :ref:`W.13 Stewart's Theorem, Median Quadrances & The Centroid <w-13>`, :ref:`W.15 Circumcenter, Orthocenter & Universal Affine Barycentrics <w-15>`, :ref:`W.20 Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas <w-20>`, :ref:`W.21 Taylor Conics, Algebraic Tangents & Optical Reflection Laws <w-21>`, :ref:`W.22 Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge <w-22>`, :ref:`W.28 Rational Polar Coordinates, Classical Curves & The Ellipson <w-28>`

.. toctree::
   :hidden:

   code
