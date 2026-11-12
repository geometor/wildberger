:order: 9
:type: topic
:category: The Five Fundamental Laws
:tags: Cross Law, cosine law, cross, quadrea spread

.. _w-09:

====================================================
W.09 Law IV: The Cross Law & Quadrea-Spread Identity
====================================================

*Quadratic Replacement for the Law of Cosines Without Ambiguous Angle Signs*

.. enunciation::

   In any triangle A_1 A_2 A_3 with non-null sides Q_1, Q_2 meeting with spread s_3 and cross c_3 = 1 - s_3 at vertex A_3, the quadrances satisfy (Q_1 + Q_2 - Q_3)^2 = 4 * Q_1 * Q_2 * (1 - s_3) = 4 * Q_1 * Q_2 * c_3, equivalently A(Q_1, Q_2, Q_3) = 4 * Q_1 * Q_2 * s_3.

.. figure:: w-09.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.09 (Law IV: The Cross Law & Quadrea-Spread Identity)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   l_1 = line(A_2, A_3)
   F_1 = foot(A_1, l_1)
   alt_1 = segment(A_1, F_1)

Mathematical Synthesis
----------------------

Squaring the Conway-style dot-product term :math:`Q_1 + Q_2 - Q_3` eliminates the sign ambiguity between acute and obtuse angles in the classical Law of Cosines, producing the :term:`Cross Law` :math:`(Q_1 + Q_2 - Q_3)^2 = 4 Q_1 Q_2 (1 - s_3)` (:cite:`Wildberger2005`). Geometrically, dropping altitude :g:`alt_1` from :g:`A_1` to foot :g:`F_1` on line :g:`l_1` decomposes triangle :g:`t` into two right triangles whose Pythagorean relations eliminate :math:`Q(A_3, F_1)` quadratically.

Subtracting :math:`4 Q_1 Q_2` from both sides reveals the **Quadrea Spread Theorem** :math:`\mathcal{A} = 4 Q_1 Q_2 s_3` (the rational analogue of :math:`\Delta = \frac{1}{2} a b \sin C`). Given rational quadrances—such as :math:`Q = (16, 49, 25)` for sides :math:`(4, 7, 5)`—the Cross Law immediately yields exact rational spreads :math:`s_1 = 384/1225`, :math:`s_2 = 24/25`, and :math:`s_3 = 24/49` by elementary arithmetic alone!

Key Algebraic Identities
------------------------

.. math::

   (Q_1 + Q_2 - Q_3)^2 = 4 Q_1 Q_2 (1 - s_3) = 4 Q_1 Q_2 c_3

.. math::

   s_3 = 1 - \frac{(Q_1 + Q_2 - Q_3)^2}{4 Q_1 Q_2} = \frac{\mathcal{A}(Q_1, Q_2, Q_3)}{4 Q_1 Q_2}

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Side quadrances (Q_1, Q_2, Q_3)``
     - ``(41, 20, 49)``
     - Irrational lengths, integer quadrances!
   * - ``Cross Law LHS (Q_1 + Q_2 - Q_3)^2``
     - ``144``
     - Matches RHS 4*Q_1*Q_2*(1-s_3) = 144
   * - ``Recovered rational spreads (s_1, s_2, s_3)``
     - ``(4/5, 16/41, 196/205)``
     - Pure rational division
   * - ``Quadrea-Spread identity 4*Q_1*Q_2*s_3``
     - ``3136``
     - Matches quadrea A = 3136

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-09.svg``)
   * - **Thematic Part**
     - Part II: The Five Fundamental Laws
   * - **Euclid's Elements**
     - :ref:`II.12`, :ref:`II.13` (Obtuse and acute generalizations of Pythagoras)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.14 Conway Notation <f-14>` (:math:`4 S_C^2 = (a^2 + b^2 - c^2)^2`)
   * - **Classical Bridge**
     - Replaces ``c^2 = a^2 + b^2 - 2ab cos C`` over arbitrary fields

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#d8dee9", color="#4c566a", URL="../w-04/index.html"];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#d8dee9", color="#4c566a", URL="../w-06/index.html"];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#d8dee9", color="#4c566a", URL="../w-07/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-09/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#e5e9f0", color="#777777", URL="../w-10/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#e5e9f0", color="#777777", URL="../w-11/index.html"];
       "W.13" [label="W.13\nStewart's Theorem, Median Quadr...", fillcolor="#e5e9f0", color="#777777", URL="../w-13/index.html"];
       "W.15" [label="W.15\nCircumcenter, Orthocenter & Uni...", fillcolor="#e5e9f0", color="#777777", URL="../w-15/index.html"];
       "W.18" [label="W.18\nCyclic Quadrilaterals, Ptolemy...", fillcolor="#e5e9f0", color="#777777", URL="../w-18/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#e5e9f0", color="#777777", URL="../w-23/index.html"];
       "W.24" [label="W.24\nExact Triangle Solvers & Survey...", fillcolor="#e5e9f0", color="#777777", URL="../w-24/index.html"];
       "W.04" -> "W.09";
       "W.06" -> "W.09";
       "W.07" -> "W.09";
       "W.09" -> "W.10";
       "W.09" -> "W.11";
       "W.09" -> "W.13";
       "W.09" -> "W.15";
       "W.09" -> "W.18";
       "W.09" -> "W.23";
       "W.09" -> "W.24";
   }

**Depends on**: :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`

**Required for**: :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`, :ref:`W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle <w-11>`, :ref:`W.13 Stewart's Theorem, Median Quadrances & The Centroid <w-13>`, :ref:`W.15 Circumcenter, Orthocenter & Universal Affine Barycentrics <w-15>`, :ref:`W.18 Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation <w-18>`, :ref:`W.23 Chromogeometry & Universal Symmetric Bilinear Forms <w-23>`, :ref:`W.24 Exact Triangle Solvers & Surveying Triangulation <w-24>`

.. toctree::
   :hidden:

   code
