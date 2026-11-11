:order: 8
:type: topic
:category: The Five Fundamental Laws
:tags: Spread Law, circumquadrance, sine law, extended spread law

.. _w-08:

===========================================================
W.08 Law III: The Spread Law & Extended Circumquadrance Law
===========================================================

*Exact Rational Proportionality of Vertex Spreads and Opposite Quadrances*

.. enunciation::

   In any non-null triangle A_1 A_2 A_3 with side quadrances Q_1, Q_2, Q_3, vertex spreads s_1, s_2, s_3, quadrea A, and circumquadrance K, the ratios of spread to opposite quadrance are equal: s_1 / Q_1 = s_2 / Q_2 = s_3 / Q_3 = A / (4 * Q_1 * Q_2 * Q_3) = 1 / (4 * K).

.. figure:: w-08.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.08 (Law III: The Spread Law & Extended Circumquadrance Law)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   F_1 = foot(A_1, line(A_2, A_3))
   F_2 = foot(A_2, line(A_1, A_3))
   C = circumcenter(A_1, A_2, A_3)
   c = circle(C, A_1)

Mathematical Synthesis
----------------------

Dropping altitudes to feet :g:`F_1` and :g:`F_2` in triangle :g:`t` gives two right-triangle expressions for the altitude quadrances: :math:`Q(A_1, F_1) = Q_3 s_2` and :math:`Q(A_2, F_2) = Q_3 s_1`, while matching :math:`Q_2 s_3 = Q_3 s_2` immediately yields the :term:`Spread Law` :math:`s_1 / Q_1 = s_2 / Q_2 = s_3 / Q_3` (:cite:`Wildberger2005`)—replacing the transcendental Law of Sines with pure field division!

Connecting the Spread Law to the :term:`circumcenter` :g:`C` and circumcircle :g:`c` produces the **Extended Spread Law**: every ratio :math:`s_i / Q_i` equals :math:`1 / (4 K)`, where :math:`K = Q(C, A_i) = Q_1 Q_2 Q_3 / \mathcal{A}` is the :term:`circumquadrance`—the exact quadratic counterpart of the classical :math:`a / \sin A = 2 R` identity.

Key Algebraic Identities
------------------------

.. math::

   \frac{s_1}{Q_1} = \frac{s_2}{Q_2} = \frac{s_3}{Q_3} = \frac{\mathcal{A}}{4 Q_1 Q_2 Q_3} = \frac{1}{4 K}

.. math::

   K = \frac{Q_1 Q_2 Q_3}{\mathcal{A}}, \qquad \mathcal{A} = 64 K^2 s_1 s_2 s_3

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Quadrances (Q_1, Q_2, Q_3)``
     - ``(225, 169, 196)``
     - Exact integer quadrances
   * - ``Vertex spreads (s_1, s_2, s_3)``
     - ``(144/169, 16/25, 3136/4225)``
     - Exact rational spreads
   * - ``Common ratio s_1/Q_1 == s_2/Q_2 == s_3/Q_3``
     - ``16/4225``
     - Verified identical
   * - ``Circumcenter C & Circumquadrance K``
     - ``C = [7, 33/8], K = 4225/64``
     - 1/(4K) = 16/4225

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-08.svg``)
   * - **Thematic Part**
     - Part II: The Five Fundamental Laws
   * - **Euclid's Elements**
     - :ref:`III.20`, :ref:`IV.5`, :ref:`VI.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.5`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.11 Circumcenter <f-11>`, :ref:`F.13 Compare Triangles in Circles <f-13>`
   * - **ETC Reference**
     - Circumcenter ``X(3)`` (:cite:`Kimberling1998`)

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
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-08/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#e5e9f0", color="#777777", URL="../w-10/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#e5e9f0", color="#777777", URL="../w-11/index.html"];
       "W.14" [label="W.14\nMenelaus, Ceva & The Alternate...", fillcolor="#e5e9f0", color="#777777", URL="../w-14/index.html"];
       "W.15" [label="W.15\nCircumcenter, Orthocenter & Uni...", fillcolor="#e5e9f0", color="#777777", URL="../w-15/index.html"];
       "W.17" [label="W.17\nCircle Geometry: Subtended Spre...", fillcolor="#e5e9f0", color="#777777", URL="../w-17/index.html"];
       "W.22" [label="W.22\nProjective Cross-Ratio, Harmoni...", fillcolor="#e5e9f0", color="#777777", URL="../w-22/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#e5e9f0", color="#777777", URL="../w-23/index.html"];
       "W.24" [label="W.24\nExact Triangle Solvers & Survey...", fillcolor="#e5e9f0", color="#777777", URL="../w-24/index.html"];
       "W.04" -> "W.08";
       "W.06" -> "W.08";
       "W.07" -> "W.08";
       "W.08" -> "W.10";
       "W.08" -> "W.11";
       "W.08" -> "W.14";
       "W.08" -> "W.15";
       "W.08" -> "W.17";
       "W.08" -> "W.22";
       "W.08" -> "W.23";
       "W.08" -> "W.24";
   }

**Depends on**: :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`

**Required for**: :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`, :ref:`W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle <w-11>`, :ref:`W.14 Menelaus, Ceva & The Alternate Spreads Theorem <w-14>`, :ref:`W.15 Circumcenter, Orthocenter & Universal Affine Barycentrics <w-15>`, :ref:`W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points <w-17>`, :ref:`W.22 Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge <w-22>`, :ref:`W.23 Chromogeometry & Universal Symmetric Bilinear Forms <w-23>`, :ref:`W.24 Exact Triangle Solvers & Surveying Triangulation <w-24>`

.. toctree::
   :hidden:

   code
