:order: 18
:type: topic
:category: Cyclic Polygons & Four-Point Invariants
:tags: cyclic quadrilateral, Quadruple Quad Formula, Brahmagupta, Ptolemy, Euler four-point

.. _w-18:

=================================================================
W.18 Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation
=================================================================

*Opposite-Spread Equality, Radical-Free Brahmagupta/Robbins, and Determinant Cocircularity*

.. enunciation::

   Four non-collinear points A_1, A_2, A_3, A_4 on a circle c satisfy equal opposite spreads s(A_1 A_2, A_1 A_4) = s(A_3 A_2, A_3 A_4), Ptolemy's Triple-Quad Law A(Q_12*Q_34, Q_23*Q_14, Q_13*Q_24) = 0 among product quadrances, and the cyclic quadrea / circumquadrance formulas, while four collinear points satisfy Q(Q_12, Q_23, Q_34, Q_14) = 0.

.. figure:: w-18.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.18 (Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O_c : Point
   A_1 : Point
   A_2 : Point
   A_3 : Point
   A_4 : Point
   =====
   c = circle(O_c, A_1)
   q_cyc = polygon(A_1, A_2, A_3, A_4)
   d_13 = segment(A_1, A_3)
   d_24 = segment(A_2, A_4)
   P_x = meet(line(A_1, A_3), line(A_2, A_4))

Mathematical Synthesis
----------------------

In :person:`Euclid <euclid>`'s :ref:`III.22`, opposite angles of a cyclic quadrilateral sum to two right angles (:math:`\theta_1 + \theta_3 = \pi`). Taking :math:`\sin^2` turns supplementarity into **exact equality**: on circle :g:`c` (center :g:`O_c`), cyclic quadrilateral :g:`q_cyc` with diagonals :g:`d_13` and :g:`d_24` meeting at :g:`P_x` has **equal opposite vertex spreads** :math:`s_1 = s_3` and :math:`s_2 = s_4` (:cite:`Wildberger2005`)!

Equally remarkable is :person:`Claudius Ptolemy <ptolemy>`'s theorem (:math:`ac + bd = ef` in lengths): squaring out the radicals shows that the three product pairs :math:`(Q_{12} Q_{34},\; Q_{23} Q_{14},\; Q_{13} Q_{24})` obey the **exact Triple Quad Formula** :math:`\mathcal{A} = 0`! Meanwhile, :person:`Leonhard Euler <euler>`'s four-point relation proves that for **any** four coplanar points, the Cayley-Menger determinant vanishes identically, and for four collinear points their sequential quadrances satisfy the :term:`Quadruple Quad Formula` :math:`Q(Q_{12}, Q_{23}, Q_{34}, Q_{14}) = 0`.

Key Algebraic Identities
------------------------

.. math::

   \text{Cyclic } A_1 A_2 A_3 A_4:\quad s_1 = s_3, \quad s_2 = s_4, \qquad \mathcal{A}(Q_{12} Q_{34},\; Q_{23} Q_{14},\; Q_{13} Q_{24}) = 0

.. math::

   Q(a, b, c, d) = \big((a + b + c + d)^2 - 2(a^2 + b^2 + c^2 + d^2)\big)^2 - 64 a b c d = 0

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Opposite spreads s_1 == s_3 & s_2 == s_4``
     - ``1 == 1, 9/10 == 9/10``
     - Theorem 108 verified
   * - ``Ptolemy's Theorem A(Q_12*Q_34, Q_23*Q_14, Q_13*Q_24)``
     - ``0``
     - Verified == 0
   * - ``Euler's 4-Point Cayley-Menger E(Q_ij)``
     - ``0``
     - Verified == 0
   * - ``Collinear Quadruple Quad Q(4, 9, 25, 100)``
     - ``0``
     - Verified == 0

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-18.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`III.21`, :ref:`III.22` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.7`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.15 Cyclic Quadrilateral <f-15>` (16 manuscript folios, :cite:`SeeligNotebooks`)
   * - **Classical Canon**
     - :person:`Brahmagupta <brahmagupta>` & :person:`Claudius Ptolemy <ptolemy>` (*Almagest*)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#d8dee9", color="#4c566a", URL="../w-07/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#d8dee9", color="#4c566a", URL="../w-09/index.html"];
       "W.17" [label="W.17\nCircle Geometry: Subtended Spre...", fillcolor="#d8dee9", color="#4c566a", URL="../w-17/index.html"];
       "W.18" [label="W.18\nCyclic Quadrilaterals, Ptolemy...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-18/index.html"];
       "W.07" -> "W.18";
       "W.09" -> "W.18";
       "W.17" -> "W.18";
   }

**Depends on**: :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`, :ref:`W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points <w-17>`

.. toctree::
   :hidden:

   code
