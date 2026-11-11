:order: 15
:type: topic
:category: Triangle Centers & Classical Lines
:tags: circumcenter, orthocenter, orthic triangle, barycentric, Conway notation

.. _w-15:

==============================================================
W.15 Circumcenter, Orthocenter & Universal Affine Barycentrics
==============================================================

*Radical-Free Coordinates for X(3), X(4), and Orthic Bisector Symmetry*

.. enunciation::

   Every non-null triangle A_1 A_2 A_3 over a field F (char F != 2) has a unique circumcenter C at the intersection of its side perpendicular bisectors and a unique orthocenter O at the intersection of its altitudes, with affine barycentric weights beta_i = Q_i*(Q_j + Q_k - Q_i)/(2*A) for C and gamma_i = (Q_i + Q_j - Q_k)*(Q_k + Q_i - Q_j)/(2*A) for O.

.. figure:: w-15.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.15 (Circumcenter, Orthocenter & Universal Affine Barycentrics)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   C = circumcenter(A_1, A_2, A_3)
   c_circ = circle(C, A_1)
   F_1 = foot(A_1, line(A_2, A_3))
   F_2 = foot(A_2, line(A_1, A_3))
   F_3 = foot(A_3, line(A_1, A_2))
   O = meet(line(A_1, F_1), line(A_2, F_2))
   t_orth = polygon(F_1, F_2, F_3)

Mathematical Synthesis
----------------------

Unlike the :term:`incenter`—which requires square vertices—both the :term:`circumcenter` :g:`C` (:math:`X(3)`) and the :term:`orthocenter` :g:`O` (:math:`X(4)`) are **universally rational** in the vertex coordinates of any non-null triangle :g:`t` (:cite:`Wildberger2005`). Their homogeneous barycentric weights depend exclusively on the Conway-style dot-product factors :math:`2 S_i = Q_j + Q_k - Q_i` normalized by :math:`2\mathcal{A}`, linking directly to :ref:`F.14 Conway Notation <f-14>` and :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`.

Dropping altitudes to feet :g:`F_1`, :g:`F_2`, :g:`F_3` forms the **orthic triangle** :g:`t_orth`, whose altitudes bisect its vertex spreads (**Orthic Triangle Theorem**): the altitudes of :g:`t` are :term:`vertex bisector` lines of :g:`t_orth`, making :g:`O` an incenter/excenter of :g:`t_orth` even over fields where :g:`t` itself has no rational incenter! Moreover, reflecting :g:`O` across each sideline lands directly on the circumcircle :g:`c_circ`.

Key Algebraic Identities
------------------------

.. math::

   C = \sum_{i=1}^{3} \frac{Q_i(Q_j + Q_k - Q_i)}{2\mathcal{A}}\, A_i, \qquad O = \sum_{i=1}^{3} \frac{(Q_i + Q_j - Q_k)(Q_k + Q_i - Q_j)}{2\mathcal{A}}\, A_i

.. math::

   Q(O, A_3) = 4 K (1 - s_3), \qquad s(F_3 F_1, F_3 A_3) = s(F_3 F_2, F_3 A_3) = 1 - s_3

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Circumcenter C = X(3)``
     - ``[7, 33/8]``
     - K = 4225/64
   * - ``Orthocenter O = X(4)``
     - ``[5, 15/4]``
     - Concurrent altitudes
   * - ``Orthocenter quadrance Q(O, A_3) = 4*K*(1 - s_3)``
     - ``1089/16 == 1089/16``
     - Exact rational identity
   * - ``Orthic bisector law s(F_3 F_1, F_3 A_3) == s(F_3 F_2, F_3 A_3)``
     - ``1089/4225 == 1089/4225 = 1 - s_3``
     - Theorem 86 verified

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-15.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`IV.5` (Circumscribing a circle about a triangle, :cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`, :ref:`G.7`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.11 Circumcenter <f-11>`, :ref:`F.36 Orthic Triangle <f-36>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`
   * - **ETC Reference**
     - Circumcenter ``X(3)`` & Orthocenter ``X(4)`` (:cite:`Kimberling1998`)

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
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#d8dee9", color="#4c566a", URL="../w-09/index.html"];
       "W.15" [label="W.15\nCircumcenter, Orthocenter & Uni...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-15/index.html"];
       "W.16" [label="W.16\nThe Euler Line & Nine-Point Cir...", fillcolor="#e5e9f0", color="#777777", URL="../w-16/index.html"];
       "W.01" -> "W.15";
       "W.03" -> "W.15";
       "W.08" -> "W.15";
       "W.09" -> "W.15";
       "W.15" -> "W.16";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`

**Required for**: :ref:`W.16 The Euler Line & Nine-Point Circle Over Arbitrary Fields <w-16>`

.. toctree::
   :hidden:

   code
