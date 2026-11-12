:order: 6
:type: topic
:category: The Five Fundamental Laws
:tags: Pythagoras, right triangle, right midpoint, quadrea, Egyptian triangle

.. _w-06:

===========================================================
W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants
===========================================================

*Equivalence of Perpendicularity (s_3 = 1) and Additive Quadrances (Q_1 + Q_2 = Q_3)*

.. enunciation::

   For any three non-collinear points A_1, A_2, A_3 over a field F (char F != 2) with non-null lines A_1 A_3 and A_2 A_3, the lines A_1 A_3 and A_2 A_3 are perpendicular (s_3 = 1) if and only if Q(A_2, A_3) + Q(A_1, A_3) = Q(A_1, A_2), in which case the hypotenuse midpoint M_3 is equidistant in quadrance (Q_3 / 4) from all three vertices.

.. figure:: w-06.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.06 (Law I: Pythagoras' Theorem & Right Triangle Invariants)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   M_3 = midpoint(A_1, A_2)
   c = circle(M_3, A_3)
   F_3 = foot(A_3, line(A_1, A_2))

Mathematical Synthesis
----------------------

In :person:`Euclid <euclid>`'s *Elements* (:ref:`I.47` and :ref:`I.48`), :person:`Pythagoras <pythagoras>`' theorem equates geometric areas of squares erected on the sides of a right triangle. In Rational Trigonometry (:cite:`Wildberger2005`), **squares on the sides are the native metric**: :math:`Q_1 + Q_2 = Q_3` is an exact linear equation in the three side quadrances whenever the lines at :g:`A_3` have :term:`spread` :math:`s_3 = 1`.

Two immediate corollaries hold over any field :math:`F`: the **Right Quadrea Theorem** :math:`\mathcal{A} = 4 Q_1 Q_2`, and the **Right Midpoint Theorem** showing that the midpoint :g:`M_3` of hypotenuse :math:`A_1 A_2` is the :term:`circumcenter` of :g:`t` with :math:`Q(M_3, A_1) = Q(M_3, A_2) = Q(M_3, A_3) = Q_3 / 4`, placing :g:`A_3` on circle :g:`c` and splitting the hypotenuse at altitude foot :g:`F_3` in ratio :math:`Q_2 : Q_1`.

Key Algebraic Identities
------------------------

.. math::

   \ell_1 \perp \ell_2 \iff s_3 = 1 \iff Q_1 + Q_2 = Q_3

.. math::

   Q(M_3, A_1) = Q(M_3, A_2) = Q(M_3, A_3) = \frac{Q_3}{4}, \qquad \mathcal{A}(Q_1, Q_2, Q_1 + Q_2) = 4 Q_1 Q_2

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Side quadrances (Q_1, Q_2, Q_3)``
     - ``(16, 9, 25)``
     - 16 + 9 = 25
   * - ``Right spread s_3 at A_3``
     - ``1``
     - l_1 perp l_2 <=> s_3 = 1
   * - ``Right midpoint quadrance Q(M_3, A_i)``
     - ``25/4``
     - Equals Q_3 / 4 = 25/4
   * - ``Right quadrea A = 4*Q_1*Q_2``
     - ``576``
     - Matches 4 * 16 * 9 = 576
   * - ``Altitude foot F_3 split Q(A_1,F_3):Q(F_3,A_2)``
     - ``81/25 : 256/25``
     - Proportional to Q_2^2 : Q_1^2 = 81 : 256

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-06.svg``)
   * - **Thematic Part**
     - Part II: The Five Fundamental Laws
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`I.48`, :ref:`III.31`, :ref:`VI.8` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.42 Right Triangles <f-42>`
   * - **ETC Reference**
     - Egyptian right triangle ``(3, 4, 5)`` -> ``Q = (9, 16, 25)`` in ``geometor/etc``

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.03" [label="W.03\nQuadrance, Midpoints & Point-to...", fillcolor="#d8dee9", color="#4c566a", URL="../w-03/index.html"];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#d8dee9", color="#4c566a", URL="../w-04/index.html"];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-06/index.html"];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#e5e9f0", color="#777777", URL="../w-07/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#e5e9f0", color="#777777", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#e5e9f0", color="#777777", URL="../w-09/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#e5e9f0", color="#777777", URL="../w-11/index.html"];
       "W.16" [label="W.16\nThe Euler Line & Nine-Point Cir...", fillcolor="#e5e9f0", color="#777777", URL="../w-16/index.html"];
       "W.17" [label="W.17\nCircle Geometry: Subtended Spre...", fillcolor="#e5e9f0", color="#777777", URL="../w-17/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#e5e9f0", color="#777777", URL="../w-23/index.html"];
       "W.27" [label="W.27\n3D Planes, De Gua's Quadrea Law...", fillcolor="#e5e9f0", color="#777777", URL="../w-27/index.html"];
       "W.03" -> "W.06";
       "W.04" -> "W.06";
       "W.06" -> "W.07";
       "W.06" -> "W.08";
       "W.06" -> "W.09";
       "W.06" -> "W.11";
       "W.06" -> "W.16";
       "W.06" -> "W.17";
       "W.06" -> "W.23";
       "W.06" -> "W.27";
   }

**Depends on**: :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`

**Required for**: :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`, :ref:`W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle <w-11>`, :ref:`W.16 The Euler Line & Nine-Point Circle Over Arbitrary Fields <w-16>`, :ref:`W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points <w-17>`, :ref:`W.23 Chromogeometry & Universal Symmetric Bilinear Forms <w-23>`, :ref:`W.27 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads <w-27>`

.. toctree::
   :hidden:

   code
