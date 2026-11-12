:order: 16
:type: topic
:category: Triangle Centers & Classical Circles
:tags: Euler line, nine-point circle, nine-point center, Feuerbach, finite fields

.. _w-16:

=============================================================
W.16 The Euler Line & Nine-Point Circle Over Arbitrary Fields
=============================================================

*Exact Collinearity of C, G, N, O and the K/4 Nine-Point Circle in Q and F_p*

.. enunciation::

   In any non-null triangle A_1 A_2 A_3 over a field F (char F != 2), the nine-point center N = (C + O)/2 satisfies 2*N - C = O (and 3*G = 2*C + O when char F != 3), placing C, G, N, O on the Euler line with quadrance proportions Q(C, G) : Q(C, N) : Q(C, O) = 4 : 9 : 36; the three side midpoints M_i, three altitude feet F_i, and three Euler midpoints E_i = (A_i + O)/2 all have exact quadrance K / 4 from N.

.. figure:: w-16.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.16 (The Euler Line & Nine-Point Circle Over Arbitrary Fields)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   C = circumcenter(A_1, A_2, A_3)
   O = orthocenter(A_1, A_2, A_3)
   N = midpoint(C, O)
   G = centroid(A_1, A_2, A_3)
   l_euler = line(C, O)
   c_circ = circle(C, A_1)
   c_nine = circle(N, midpoint(A_2, A_3))

Mathematical Synthesis
----------------------

:person:`Leonhard Euler <euler>`'s collinearity of :g:`C` (:math:`X(3)`), :g:`G` (:math:`X(2)`), :g:`N` (:math:`X(5)`), and :g:`O` (:math:`X(4)`) along :g:`l_euler` is a pure vector identity :math:`O - C = (A_1 - C) + (A_2 - C) + (A_3 - C)` that holds over **every field** of characteristic not :math:`2` (:cite:`Wildberger2005`, :cite:`CoxeterGreitzer1967`). Notice that even in characteristic :math:`3`—where the centroid :g:`G` moves to infinity—the midpoint relation :math:`N = (C + O)/2` and the :term:`nine-point circle` remain completely intact!

The circumcircle :g:`c_circ` has :term:`circumquadrance` :math:`K`, while :g:`c_nine` centered at :g:`N` passes through all nine canonical points—side midpoints :g:`M_1`, :g:`M_2`, :g:`M_3`, altitude feet :g:`F_1`, :g:`F_2`, :g:`F_3`, and Euler midpoints :g:`E_1`, :g:`E_2`, :g:`E_3`—with exact quadrance :math:`K_9 = K / 4`, verified identically over both :math:`\mathbb{Q}[x_i, y_i]` and finite prime fields such as :math:`\mathbb{F}_{17}`!

Key Algebraic Identities
------------------------

.. math::

   O - C = \sum_{i=1}^{3} (A_i - C), \qquad 3 G = 2 C + O, \qquad N = \frac{C + O}{2}

.. math::

   Q(C, G) = \frac{1}{9} Q(C, O), \quad Q(C, N) = \frac{1}{4} Q(C, O), \quad Q(N, M_i) = Q(N, F_i) = Q(N, E_i) = \frac{K}{4}

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Euler collinearity det(C, G, O) & det(C, N, O)``
     - ``0, 0``
     - Verified == 0
   * - ``Euler quadrance ratio Q(C,G):Q(C,N):Q(C,O)``
     - ``4 : 9 : 36``
     - Exact harmonic center spacing
   * - ``All 9 points {M_i, F_i, E_i} to N``
     - ``305/18``
     - Equals K / 4 = 610/9 / 4
   * - ``Nine-Point Circle over GF(17)``
     - ``N = [14, 1], K_9 = 16 (mod 17)``
     - Exact modular verification

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-16.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`III.31`, :ref:`IV.5` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`, :ref:`G.7`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.34 Nine-Point Circle <f-34>` (:cite:`SeeligNotebooks`)
   * - **ETC Reference**
     - Centers ``X(2)``, ``X(3)``, ``X(4)``, ``X(5)`` in ``geometor/etc`` (:cite:`Kimberling1998`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#d8dee9", color="#4c566a", URL="../w-06/index.html"];
       "W.13" [label="W.13\nStewart's Theorem, Median Quadr...", fillcolor="#d8dee9", color="#4c566a", URL="../w-13/index.html"];
       "W.15" [label="W.15\nCircumcenter, Orthocenter & Uni...", fillcolor="#d8dee9", color="#4c566a", URL="../w-15/index.html"];
       "W.16" [label="W.16\nThe Euler Line & Nine-Point Cir...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-16/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#e5e9f0", color="#777777", URL="../w-23/index.html"];
       "W.06" -> "W.16";
       "W.13" -> "W.16";
       "W.15" -> "W.16";
       "W.16" -> "W.23";
   }

**Depends on**: :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.13 Stewart's Theorem, Median Quadrances & The Centroid <w-13>`, :ref:`W.15 Circumcenter, Orthocenter & Universal Affine Barycentrics <w-15>`

**Required for**: :ref:`W.23 Chromogeometry & Universal Symmetric Bilinear Forms <w-23>`

.. toctree::
   :hidden:

   code
