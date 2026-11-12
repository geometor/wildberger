:order: 27
:type: topic
:category: 3D Solid Geometry & The Five Platonic Solids
:tags: Platonic solids, dihedral spread, De Gua, tetrahedron, icosahedron, dodecahedron

.. _w-27:

================================================================
W.27 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads
================================================================

*Miraculous Cancellation of sqrt(5): Purely Rational Face Spreads 8/9, 1, 8/9, 4/9, 4/5*

.. enunciation::

   In 3D space over F, quadrance is Q(A_1, A_2) = dx^2 + dy^2 + dz^2, a right-corner tetrahedron satisfies De Gua's Quadrea Theorem A_base = A_xy + A_yz + A_zx, and the dihedral (face) spreads of ALL FIVE regular Platonic solids—Tetrahedron (8/9), Cube (1), Octahedron (8/9), Icosahedron (4/9), and Dodecahedron (4/5)—are exact rational numbers in Q!

.. figure:: w-27.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.27 (3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   V_0 : Point
   V_1 : Point
   V_2 : Point
   V_3 : Point
   =====
   t_base = polygon(V_1, V_2, V_3)
   M_edge = midpoint(V_1, V_2)
   s_ap1 = segment(V_0, M_edge)
   s_ap2 = segment(V_3, M_edge)

Mathematical Synthesis
----------------------

Extending :term:`quadrance` to three dimensions (:math:`\Delta x^2 + \Delta y^2 + \Delta z^2`) defines the :term:`dihedral spread` :math:`S(\Pi_1, \Pi_2)` between two planes via the spread of their normal vectors—equivalently, the spread between face apothems :g:`s_ap1` and :g:`s_ap2` meeting at edge midpoint :g:`M_edge` on base :g:`t_base` (:g:`V_0`, :g:`V_1`, :g:`V_2`, :g:`V_3`). For a right-corner tetrahedron, :person:`Pythagoras <pythagoras>`' theorem lifts directly to **De Gua's Quadrea Law**: the slant face quadrea equals the sum of the three orthogonal face quadreas!

The crowning 3D revelation of :cite:`Wildberger2005` (Chapter 26) concerns the **five Platonic solids** celebrated in Book XIII of :person:`Euclid <euclid>`'s *Elements* and :person:`Luca Pacioli <pacioli>`'s *De Divina Proportione* (:cite:`Pacioli1509`). Although the icosahedron and dodecahedron require the pentagon spreads :math:`\alpha, \beta = (5 \mp \sqrt{5})/8` solving :math:`16 s^2 - 20 s + 5 = 0` (:ref:`W.19 <w-19>`), in the face-spread formulas :math:`S_{\text{ico}} = \frac{4\beta}{3\alpha}(1 - \frac{\beta}{3\alpha}) = \frac{4}{9}` and :math:`S_{\text{dod}} = \frac{4\alpha - 1}{4\alpha^2} = \frac{4}{5}`, **every factor of** :math:`\sqrt{5}` **cancels identically**, leaving five pure fractions in :math:`\mathbb{Q}`: :math:`8/9, 1, 8/9, 4/9, 4/5`!

Key Algebraic Identities
------------------------

.. math::

   16\alpha^2 - 20\alpha + 5 = 0 \implies S_{\text{ico}} = \frac{4\beta}{3\alpha}\!\left(1 - \frac{\beta}{3\alpha}\right) = \frac{4}{9}, \qquad S_{\text{dod}} = \frac{4\alpha - 1}{4\alpha^2} = \frac{4}{5}

.. math::

   \big(S_{\text{tet}},\; S_{\text{cube}},\; S_{\text{oct}},\; S_{\text{ico}},\; S_{\text{dod}}\big) = \left(\frac{8}{9},\; 1,\; \frac{8}{9},\; \frac{4}{9},\; \frac{4}{5}\right) \in \mathbb{Q}^5

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Regular Tetrahedron & Octahedron face spreads``
     - ``S_tet = 8/9, S_oct = 8/9``
     - Exact rational spreads
   * - ``Cube orthogonal face spread``
     - ``S_cube = 1``
     - Mutually perpendicular planes
   * - ``Regular Icosahedron face spread (vertices [0,+/-1,+/-phi])``
     - ``S_ico = 4/9``
     - sqrt(5) cancels completely!
   * - ``Regular Dodecahedron face spread``
     - ``S_dod = 4/5``
     - sqrt(5) cancels completely!
   * - ``De Gua's 3D Right-Corner Quadrea Theorem``
     - ``A_slant = 2016 == 2016``
     - 3D generalization of Pythagoras

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-27.svg``)
   * - **Thematic Part**
     - Part IV: Practical Solvers, 3D Platonic Geometry & Polar Curves
   * - **Euclid's Elements**
     - :ref:`XI.4`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.15`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18` (:cite:`EuclidElements`)
   * - **GEOMETOR Pacioli**
     - *De Divina Proportione* Platonic polyhedra plates (:cite:`Pacioli1509`)
   * - **GEOMETOR Fundamentals**
     - :ref:`F.18 Equilateral Triangle <f-18>`, :ref:`F.23 Golden Triangles <f-23>`
   * - **SymPy Proof**
     - Verified from exact 3D vertex coordinates in ``prove_platonic_dihedral_spreads()``

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
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#d8dee9", color="#4c566a", URL="../w-07/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#d8dee9", color="#4c566a", URL="../w-11/index.html"];
       "W.19" [label="W.19\nRegular Stars, Golden Pentagons...", fillcolor="#d8dee9", color="#4c566a", URL="../w-19/index.html"];
       "W.27" [label="W.27\n3D Planes, De Gua's Quadrea Law...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-27/index.html"];
       "W.05" -> "W.27";
       "W.06" -> "W.27";
       "W.07" -> "W.27";
       "W.11" -> "W.27";
       "W.19" -> "W.27";
   }

**Depends on**: :ref:`W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads <w-05>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`, :ref:`W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle <w-11>`, :ref:`W.19 Regular Stars, Golden Pentagons & Finite-Field Polygons <w-19>`

.. toctree::
   :hidden:

   code
