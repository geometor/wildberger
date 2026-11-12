:order: 10
:type: topic
:category: The Five Fundamental Laws
:tags: Triple Spread Formula, triple cross, quadruple spread, angle sum

.. _w-10:

===================================================================
W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas
===================================================================

*Cubic Polynomial Harmony Replacing theta_1 + theta_2 + theta_3 = pi*

.. enunciation::

   For any three coplanar non-null lines l_1, l_2, l_3 with pairwise spreads s_1, s_2, s_3 and crosses c_i = 1 - s_i, the spreads satisfy the cubic Triple Spread Formula (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 and the crosses satisfy (c_1 + c_2 + c_3 - 1)^2 = 4*c_1*c_2*c_3; for four lines, the Quadruple Spread polynomial R(s_12, s_23, s_34, s_14) = 0 is identically invariant under s_ij <-> 1 - s_ij.

.. figure:: w-10.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.10 (Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   l_1 = line(A_2, A_3)
   l_2 = line(A_1, A_3)
   l_3 = line(A_1, A_2)
   t = polygon(A_1, A_2, A_3)

Mathematical Synthesis
----------------------

Just as the :term:`Triple Quad Formula` replaces :math:`d_1 + d_2 = d_3` by a quadratic relation with no square roots, the :term:`Triple Spread Formula` replaces Euclid's angle-sum theorem :math:`\theta_1 + \theta_2 + \theta_3 = \pi` with a symmetric cubic equation in the three spreads :math:`(s_1, s_2, s_3)` of lines :g:`l_1`, :g:`l_2`, :g:`l_3` (:cite:`Wildberger2005`). Notice the structural miracle: it differs from :math:`\mathcal{A}(s_1, s_2, s_3) = 0` by the single cubic term :math:`4 s_1 s_2 s_3`!

Substituting :math:`s_i = 1 - c_i` produces the **Triple Cross Formula** :math:`(c_1 + c_2 + c_3 - 1)^2 = 4 c_1 c_2 c_3`. Extending from three to four lines yields the :term:`Quadruple Spread Formula` :math:`R(s_{12}, s_{23}, s_{34}, s_{14}) = 0`, which possesses an unexpected self-duality: replacing every spread :math:`s_{ij}` with its cross :math:`c_{ij} = 1 - s_{ij}` leaves the polynomial :math:`R` **identically unchanged**!

Key Algebraic Identities
------------------------

.. math::

   (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3 \iff (s_3 - (s_1 + s_2 - 2 s_1 s_2))^2 = 4 s_1 s_2 (1 - s_1)(1 - s_2)

.. math::

   (c_1 + c_2 + c_3 - 1)^2 = 4 c_1 c_2 c_3, \qquad R(a, b, c, d) \equiv R(1 - a, 1 - b, 1 - c, 1 - d)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Spreads (s_1, s_2, s_3)``
     - ``(9/13, 81/130, 9/10)``
     - Exact rationals
   * - ``Triple Spread Formula S(s_1, s_2, s_3)``
     - ``0``
     - Verified == 0
   * - ``Triple Cross Formula C(c_1, c_2, c_3)``
     - ``0``
     - Verified == 0
   * - ``Quadruple Spread Formula R(s_12,s_23,s_34,s_14)``
     - ``0``
     - Verified == 0 & self-dual under s <-> 1-s

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-10.svg``)
   * - **Thematic Part**
     - Part II: The Five Fundamental Laws
   * - **Euclid's Elements**
     - :ref:`I.32` (Angle sum of a triangle, :cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.5`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.35 Obtuse and Acute Triangles <f-35>`, :ref:`F.53 Geometric Half-Angle Trigonometry <f-53>`
   * - **3D Algebraic Surface**
     - Defines the :term:`ellipson` surface in ``[0, 1]^3`` (:ref:`W.28 <w-28>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#d8dee9", color="#4c566a", URL="../w-04/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#d8dee9", color="#4c566a", URL="../w-09/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-10/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#e5e9f0", color="#777777", URL="../w-11/index.html"];
       "W.12" [label="W.12\nVertex Bisectors, Square Vertic...", fillcolor="#e5e9f0", color="#777777", URL="../w-12/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#e5e9f0", color="#777777", URL="../w-23/index.html"];
       "W.24" [label="W.24\nExact Triangle Solvers & Survey...", fillcolor="#e5e9f0", color="#777777", URL="../w-24/index.html"];
       "W.25" [label="W.25\nSnellius–Pothenot Resection & H...", fillcolor="#e5e9f0", color="#777777", URL="../w-25/index.html"];
       "W.28" [label="W.28\nRational Polar Coordinates, Cla...", fillcolor="#e5e9f0", color="#777777", URL="../w-28/index.html"];
       "W.04" -> "W.10";
       "W.08" -> "W.10";
       "W.09" -> "W.10";
       "W.10" -> "W.11";
       "W.10" -> "W.12";
       "W.10" -> "W.23";
       "W.10" -> "W.24";
       "W.10" -> "W.25";
       "W.10" -> "W.28";
   }

**Depends on**: :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`

**Required for**: :ref:`W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle <w-11>`, :ref:`W.12 Vertex Bisectors, Square Vertices & The Four Incenters <w-12>`, :ref:`W.23 Chromogeometry & Universal Symmetric Bilinear Forms <w-23>`, :ref:`W.24 Exact Triangle Solvers & Surveying Triangulation <w-24>`, :ref:`W.25 Snellius–Pothenot Resection & Hansen's Surveying Problem <w-25>`, :ref:`W.28 Rational Polar Coordinates, Classical Curves & The Ellipson <w-28>`

.. toctree::
   :hidden:

   code
