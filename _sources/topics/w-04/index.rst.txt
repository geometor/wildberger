:order: 4
:type: topic
:category: Foundational Quadratic Invariants
:tags: spread, cross, twist, turn, complementary spreads

.. _w-04:

==================================================
W.04 Spread, Cross, Twist & Line Separation Ratios
==================================================

*Algebraic Separation of Unoriented Lines Replacing Transcendental Angle*

.. enunciation::

   For two non-null lines l_1 = <a_1 : b_1 : c_1> and l_2 = <a_2 : b_2 : c_2>, the spread s(l_1, l_2) = (a_1*b_2 - a_2*b_1)^2 / ((a_1^2 + b_1^2)*(a_2^2 + b_2^2)) depends only on the unoriented lines, vanishes iff l_1 || l_2, equals 1 iff l_1 perp l_2, and equals Q(B, C) / Q(A, B) for any altitude BC dropped from B on l_1 to C on l_2.

.. figure:: w-04.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.04 (Spread, Cross, Twist & Line Separation Ratios)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   P_2 : Point
   =====
   l_1 = line(A, B)
   l_2 = line(A, P_2)
   C = foot(B, l_2)
   n_bc = segment(B, C)

Mathematical Synthesis
----------------------

Classical angle requires circular arc-length integration, ray orientation, and :math:`\pi` ambiguities across eight possible arcs at an intersection. :person:`Norman J. Wildberger <wildberger>` replaces angle with :term:`spread` :math:`s(\ell_1, \ell_2) \in F` (:cite:`Wildberger2005`): if :g:`l_1` and :g:`l_2` intersect at :g:`A`, choosing any point :g:`B` :math:`\neq A` on :g:`l_1` and dropping altitude :g:`n_bc` to its foot :g:`C` on :g:`l_2` yields the invariant ratio :math:`s(\ell_1, \ell_2) = Q(B, C) / Q(A, B)`.

Paired with spread are the :term:`cross` :math:`c(\ell_1, \ell_2) = 1 - s(\ell_1, \ell_2) = Q(A, C)/Q(A, B)` and the :term:`twist` :math:`t(\ell_1, \ell_2) = s / c = Q(B, C)/Q(A, C)`, which squares the signed :term:`turn` :math:`u(\ell_1, \ell_2)`. Supplementary angles share the **exact same line**, so supplementary spreads are identical, while orthogonal lines swap spread and cross (:math:`s \leftrightarrow 1 - s`).

Key Algebraic Identities
------------------------

.. math::

   s(\ell_1, \ell_2) = \frac{(a_1 b_2 - a_2 b_1)^2}{(a_1^2 + b_1^2)(a_2^2 + b_2^2)} = \frac{Q(B, C)}{Q(A, B)}, \qquad c(\ell_1, \ell_2) = 1 - s(\ell_1, \ell_2) = \frac{(a_1 a_2 + b_1 b_2)^2}{(a_1^2 + b_1^2)(a_2^2 + b_2^2)}

.. math::

   t(\ell_1, \ell_2) = \frac{s(\ell_1, \ell_2)}{c(\ell_1, \ell_2)} = u(\ell_1, \ell_2)^2, \qquad \ell_3 \perp \ell_2 \implies s(\ell_1, \ell_3) = 1 - s(\ell_1, \ell_2)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Spread s(l_1, l_2)``
     - ``1/5``
     - Matches Q(B,C)/Q(A,B) = 1/5
   * - ``Cross c(l_1, l_2) = 1 - s``
     - ``4/5``
     - Matches Q(A,C)/Q(A,B) = 4/5
   * - ``Twist t(l_1, l_2) = s / c``
     - ``1/4``
     - Matches u(l_1,l_2)^2 = (-1/2)^2
   * - ``Complementary orthogonal spread``
     - ``4/5``
     - s(l_1, l_2^perp) = c(l_1, l_2)

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-04.svg``)
   * - **Thematic Part**
     - Part I: Preliminaries & Foundational Invariants
   * - **Euclid's Elements**
     - :ref:`I.11`, :ref:`I.13`, :ref:`VI.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.5`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.14 Conway Notation <f-14>`
   * - **Sister Codices**
     - ``geometor/divine`` (exact algebraic ratios without floating-point trig)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.01" [label="W.01\nPlanar Points, Line Proportions...", fillcolor="#d8dee9", color="#4c566a", URL="../w-01/index.html"];
       "W.03" [label="W.03\nQuadrance, Midpoints & Point-to...", fillcolor="#d8dee9", color="#4c566a", URL="../w-03/index.html"];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-04/index.html"];
       "W.05" [label="W.05\nSpread Polynomials S_n(s) & Pen...", fillcolor="#e5e9f0", color="#777777", URL="../w-05/index.html"];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#e5e9f0", color="#777777", URL="../w-06/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#e5e9f0", color="#777777", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#e5e9f0", color="#777777", URL="../w-09/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#e5e9f0", color="#777777", URL="../w-10/index.html"];
       "W.12" [label="W.12\nVertex Bisectors, Square Vertic...", fillcolor="#e5e9f0", color="#777777", URL="../w-12/index.html"];
       "W.22" [label="W.22\nProjective Cross-Ratio, Harmoni...", fillcolor="#e5e9f0", color="#777777", URL="../w-22/index.html"];
       "W.28" [label="W.28\nRational Polar Coordinates, Cla...", fillcolor="#e5e9f0", color="#777777", URL="../w-28/index.html"];
       "W.01" -> "W.04";
       "W.03" -> "W.04";
       "W.04" -> "W.05";
       "W.04" -> "W.06";
       "W.04" -> "W.08";
       "W.04" -> "W.09";
       "W.04" -> "W.10";
       "W.04" -> "W.12";
       "W.04" -> "W.22";
       "W.04" -> "W.28";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`

**Required for**: :ref:`W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads <w-05>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`, :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`, :ref:`W.12 Vertex Bisectors, Square Vertices & The Four Incenters <w-12>`, :ref:`W.22 Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge <w-22>`, :ref:`W.28 Rational Polar Coordinates, Classical Curves & The Ellipson <w-28>`

.. toctree::
   :hidden:

   code
