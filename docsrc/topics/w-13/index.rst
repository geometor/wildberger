:order: 13
:type: topic
:category: Proportions, Cevians & Medians
:tags: Stewart's theorem, medians, Apollonius, centroid, medial triangle

.. _w-13:

========================================================
W.13 Stewart's Theorem, Median Quadrances & The Centroid
========================================================

*Exact Quadratic Cevian Laws, Apollonius' Identity, and X(2) Concurrency*

.. enunciation::

   For any affine point D = (1 - lambda)*A_1 + lambda*A_2 on side A_1 A_2 of triangle A_1 A_2 A_3, the cevian quadrance satisfies Q(A_3, D) = (1 - lambda)*Q_2 + lambda*Q_1 - lambda*(1 - lambda)*Q_3; at lambda = 1/2, the median quadrance satisfies 4*Q(A_3, M_3) = 2*Q_1 + 2*Q_2 - Q_3, and the three medians concur at G = (A_1 + A_2 + A_3)/3.

.. figure:: w-13.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.13 (Stewart's Theorem, Median Quadrances & The Centroid)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   M_1 = midpoint(A_2, A_3)
   M_2 = midpoint(A_1, A_3)
   M_3 = midpoint(A_1, A_2)
   G = meet(line(A_1, M_1), line(A_2, M_2))
   t_med = polygon(M_1, M_2, M_3)

Mathematical Synthesis
----------------------

:person:`Matthew Stewart <stewart>`'s 1746 cevian relation becomes completely algebraic in quadrances (:cite:`Wildberger2005`). Expressing any point :math:`D` on :math:`A_1 A_2` as the affine combination :math:`(1 - \lambda)A_1 + \lambda A_2` (with :math:`R_1 = \lambda^2 Q_3` and :math:`R_2 = (1 - \lambda)^2 Q_3`) gives :math:`Q(A_3, D)` as a linear combination of :math:`Q_1, Q_2, Q_3`, or in pure quadrances without :math:`\lambda` via :term:`Stewart's theorem`.

Setting :math:`\lambda = 1/2` gives :person:`Apollonius <apollonius>`' **Median Quadrance Theorem** :math:`4 M_3 = 2 Q_1 + 2 Q_2 - Q_3` for the midpoints :g:`M_1`, :g:`M_2`, :g:`M_3`. Provided :math:`\operatorname{char} F \neq 3`, the three medians concur at the :term:`centroid` :g:`G` :math:`= \frac{1}{3}(A_1 + A_2 + A_3)` (:math:`X(2)`), dividing each median in quadrance proportion :math:`4 : 1`, while the medial triangle :g:`t_med` has side quadrances :math:`Q_i / 4` and quadrea :math:`\mathcal{A} / 16`.

Key Algebraic Identities
------------------------

.. math::

   Q(A_3, D) = (1 - \lambda) Q_2 + \lambda Q_1 - \lambda(1 - \lambda) Q_3, \qquad 4 Q(A_3, M_3) = 2 Q_1 + 2 Q_2 - Q_3

.. math::

   G = \frac{A_1 + A_2 + A_3}{3}, \qquad Q(A_i, G) = \frac{4}{9} Q(A_i, M_i) = 4 Q(G, M_i)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Median quadrance 4 * Q(A_3, M_3)``
     - ``360``
     - Matches 2*Q_1 + 2*Q_2 - Q_3 = 360
   * - ``Centroid G = (A_1 + A_2 + A_3)/3``
     - ``[5, 3]``
     - Concurrent medians
   * - ``Centroid 4:1 quadrance division``
     - ``Q(A_3,G) = 40, Q(G,M_3) = 10``
     - Verified Q(A_3,G) == 4 * Q(G,M_3)
   * - ``Medial triangle quadrea A_med``
     - ``2916``
     - Equals A / 16 = 2916

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-13.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`I.10`, :ref:`VI.2` (Thales' midpoint parallel theorem, :cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.5`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.6 Centroid <f-06>`, :ref:`F.46 Stewart's Theorem <f-46>` (:cite:`SeeligNotebooks`)
   * - **ETC Reference**
     - Centroid ``X(2)`` in ``geometor/etc`` (:cite:`Kimberling1998`)

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
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#d8dee9", color="#4c566a", URL="../w-07/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#d8dee9", color="#4c566a", URL="../w-09/index.html"];
       "W.13" [label="W.13\nStewart's Theorem, Median Quadr...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-13/index.html"];
       "W.16" [label="W.16\nThe Euler Line & Nine-Point Cir...", fillcolor="#e5e9f0", color="#777777", URL="../w-16/index.html"];
       "W.01" -> "W.13";
       "W.03" -> "W.13";
       "W.07" -> "W.13";
       "W.09" -> "W.13";
       "W.13" -> "W.16";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`

**Required for**: :ref:`W.16 The Euler Line & Nine-Point Circle Over Arbitrary Fields <w-16>`

.. toctree::
   :hidden:

   code
