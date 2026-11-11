:order: 24
:type: topic
:category: Practical Triangle Solvers & Surveying
:tags: QQQ, QQS, QSS, SQQ, surveying, Regiomontanus, triangulation

.. _w-24:

=====================================================
W.24 Exact Triangle Solvers & Surveying Triangulation
=====================================================

*Polynomial QQQ/QQS/QSS/SQQ Solvers, Inaccessible Heights, and Regiomontanus' Extremum*

.. enunciation::

   Every classical triangle specification (QQQ, QQS, QSS, SQQ, and SSS up to scaling) reduces to linear or quadratic equations in quadrances and spreads with exact discriminant branching; applied to surveying, inaccessible heights and Regiomontanus' maximum-spread viewing problem resolve by pure rational algebra without trigonometric tables.

.. figure:: w-24.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.24 (Exact Triangle Solvers & Surveying Triangulation)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   D_foot : Point
   C_top : Point
   =====
   l_ground = line(A, D_foot)
   seg_tower = segment(D_foot, C_top)
   t_surv = polygon(A, B, C_top)
   P_obs = regiomontanus_optimal_point(D_foot, a, b)

Mathematical Synthesis
----------------------

Classical triangle resolution (*SSS, SAS, ASA, SSA*) alternates awkwardly between inverse cosines, inverse sines, and tangent half-angle formulas, accumulating floating-point rounding at every step. In Rational Trigonometry (:cite:`Wildberger2005`), **QQQ** and **QSS** are purely rational in one step, while **SQQ** (Cross Law quadratic in :math:`Q_3`), **QQS** (Spread Law + Cross Law), and **SSS** (proportional quadrances :math:`Q_1 : Q_2 : Q_3 = s_1 : s_2 : s_3` once :math:`s_3` solves the :term:`Triple Spread Formula`) require at most a single quadratic root!

In field surveying, measuring horizontal baseline :math:`Q(A, B)` along :g:`l_ground` and the elevation spreads from :g:`A` and :g:`B` to tower top :g:`C_top` above base :g:`D_foot` (:g:`seg_tower`, triangle :g:`t_surv`) determines the vertical quadrance :math:`Q(D_{\text{foot}}, C_{\text{top}})` by one rational formula. Likewise, :person:`Regiomontanus <regiomontanus>`' 1471 problem—maximizing the viewing spread of a vertical statue from :math:`y = a` to :math:`y = b`—completes the square without derivatives to yield optimal quadrance :math:`Q(D_{\text{foot}}, P_{\text{obs}}) = a b` at :g:`P_obs` with maximum spread :math:`(b - a)^2 / (a + b)^2`!

Key Algebraic Identities
------------------------

.. math::

   \text{SQQ:}\quad (Q_3 - (Q_1 + Q_2))^2 - 4 Q_1 Q_2 (1 - s_3) = \mathcal{A}(Q_1, Q_2, Q_3) - 4 Q_1 Q_2 s_3 = 0

.. math::

   \text{Regiomontanus }(0 < a < b):\quad x_{\text{opt}}^2 = a b, \qquad s_{\max} = \frac{(b - a)^2}{(a + b)^2}

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``QQQ solver on A B C_top (52, 117, 25)``
     - ``s = (4/13, 9/13, 25/169)``
     - Pure rational Cross Law
   * - ``SQQ quadratic branches``
     - ``Q_3 roots = [52, 2116/13]``
     - Recovers exact Q_2 = 117
   * - ``Inaccessible height H from D=25, s_A=4/13, s_B=9/13``
     - ``Roots = [900/169, 36]``
     - Recovers exact tower quadrance H = 36
   * - ``Regiomontanus extremum (a=4, b=9)``
     - ``X_opt = 36, s_max = 25/169``
     - Zero derivatives

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-24.svg``)
   * - **Thematic Part**
     - Part IV: Practical Solvers, 3D Platonic Geometry & Polar Curves
   * - **Classical Surveying**
     - :person:`Regiomontanus <regiomontanus>` (1471 extremal viewing problem)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`, :ref:`G.7`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.41 Geometric Problems and Extremal Loci <f-41>`, :ref:`F.54 HP-35s Triangle Program and Coordinate Scripts <f-54>`
   * - **Computational Engine**
     - Implemented in ``geometor.wildberger.solvers``

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#d8dee9", color="#4c566a", URL="../w-09/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#d8dee9", color="#4c566a", URL="../w-10/index.html"];
       "W.24" [label="W.24\nExact Triangle Solvers & Survey...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-24/index.html"];
       "W.25" [label="W.25\nSnellius–Pothenot Resection & H...", fillcolor="#e5e9f0", color="#777777", URL="../w-25/index.html"];
       "W.08" -> "W.24";
       "W.09" -> "W.24";
       "W.10" -> "W.24";
       "W.24" -> "W.25";
   }

**Depends on**: :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`, :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`

**Required for**: :ref:`W.25 Snellius–Pothenot Resection & Hansen's Surveying Problem <w-25>`

.. toctree::
   :hidden:

   code
