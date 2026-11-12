:order: 7
:type: topic
:category: The Five Fundamental Laws
:tags: Triple Quad Formula, quadrea, Archimedes, Heron, collinearity

.. _w-07:

================================================================
W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea
================================================================

*Polynomial Collinearity Criterion and Radical-Free Triangle Area Algebra*

.. enunciation::

   Three planar points A_1, A_2, A_3 with pairwise quadrances Q_1, Q_2, Q_3 are collinear if and only if Archimedes' symmetric quadratic form A(Q_1, Q_2, Q_3) = (Q_1 + Q_2 + Q_3)^2 - 2(Q_1^2 + Q_2^2 + Q_3^2) vanishes; for any triangle, A(Q_1, Q_2, Q_3) equals 4 times the squared coordinate determinant (16 * Delta^2), defining the triangle's quadrea.

.. figure:: w-07.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.07 (Law II: Triple Quad Formula, Archimedes' Function & Quadrea)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   P_col : Point
   =====
   t = polygon(A_1, A_2, A_3)
   l_base = line(A_1, A_2)
   h_3 = segment(A_3, foot(A_3, l_base))

Mathematical Synthesis
----------------------

In classical geometry, collinearity is expressed linearly via distances :math:`d_1 + d_2 = d_3` (which depends on ordering), while triangle area uses :person:`Heron <heron>`'s radical :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}`. Squaring out all three sign combinations :math:`(\pm\sqrt{Q_1} \pm \sqrt{Q_2} \pm \sqrt{Q_3}) = 0` yields :person:`Archimedes <archimedes>`' symmetric polynomial :math:`\mathcal{A}(Q_1, Q_2, Q_3)` (:cite:`Wildberger2005`).

Over any field :math:`F` (:math:`\operatorname{char} F \neq 2`), the :term:`Triple Quad Formula` :math:`\mathcal{A}(Q_1, Q_2, Q_3) = 0` characterizes collinearity (illustrated by :g:`P_col` on :g:`l_base`) without ordering or square roots! When :g:`A_1`, :g:`A_2`, :g:`A_3` form a triangle :g:`t` with altitude :g:`h_3`, the :term:`quadrea` :math:`\mathcal{A} = 4 Q_3 Q(A_3, \ell_{\text{base}}) = 16 \Delta^2` is always an element of :math:`F`—for the Heronian :math:`(13, 14, 15)` triangle with :math:`Q = (169, 196, 225)`, :math:`\mathcal{A} = 112896 = 16 \times 84^2`.

Key Algebraic Identities
------------------------

.. math::

   \mathcal{A}(Q_1, Q_2, Q_3) = (Q_1 + Q_2 + Q_3)^2 - 2(Q_1^2 + Q_2^2 + Q_3^2) = 4 Q_1 Q_2 - (Q_1 + Q_2 - Q_3)^2

.. math::

   A_1, A_2, A_3 \text{ collinear} \iff \mathcal{A}(Q_1, Q_2, Q_3) = 0, \qquad \mathcal{A}(Q_1, Q_2, Q_3) = 4 \det\begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{pmatrix}^2 = 16\Delta^2

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Collinear quadrances (A_1, P_col, A_2)``
     - ``(81, 25, 196)``
     - A(81, 25, 196) = 0
   * - ``Heronian triangle quadrances (Q_1, Q_2, Q_3)``
     - ``(225, 169, 196)``
     - Sides (15, 13, 14) with zero radicals
   * - ``Triangle quadrea A(Q_1, Q_2, Q_3)``
     - ``112896``
     - Matches 4*det^2 = 112896
   * - ``Altitude relation 4 * Q_3 * Q(A_3, l_base)``
     - ``112896``
     - 112896 == A

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-07.svg``)
   * - **Thematic Part**
     - Part II: The Five Fundamental Laws
   * - **Euclid's Elements**
     - :ref:`II.12`, :ref:`II.13` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.1`, :ref:`G.3`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>` (:cite:`SeeligNotebooks`)
   * - **ETC Reference**
     - Acute Heronian reference triangle ``(13, 14, 15)``

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
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#d8dee9", color="#4c566a", URL="../w-06/index.html"];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-07/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#e5e9f0", color="#777777", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#e5e9f0", color="#777777", URL="../w-09/index.html"];
       "W.13" [label="W.13\nStewart's Theorem, Median Quadr...", fillcolor="#e5e9f0", color="#777777", URL="../w-13/index.html"];
       "W.18" [label="W.18\nCyclic Quadrilaterals, Ptolemy...", fillcolor="#e5e9f0", color="#777777", URL="../w-18/index.html"];
       "W.20" [label="W.20\nMetrical Conics: Circles, Ribbo...", fillcolor="#e5e9f0", color="#777777", URL="../w-20/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#e5e9f0", color="#777777", URL="../w-23/index.html"];
       "W.27" [label="W.27\n3D Planes, De Gua's Quadrea Law...", fillcolor="#e5e9f0", color="#777777", URL="../w-27/index.html"];
       "W.01" -> "W.07";
       "W.03" -> "W.07";
       "W.06" -> "W.07";
       "W.07" -> "W.08";
       "W.07" -> "W.09";
       "W.07" -> "W.13";
       "W.07" -> "W.18";
       "W.07" -> "W.20";
       "W.07" -> "W.23";
       "W.07" -> "W.27";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`

**Required for**: :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`, :ref:`W.13 Stewart's Theorem, Median Quadrances & The Centroid <w-13>`, :ref:`W.18 Cyclic Quadrilaterals, Ptolemy & Euler's Four-Point Relation <w-18>`, :ref:`W.20 Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas <w-20>`, :ref:`W.23 Chromogeometry & Universal Symmetric Bilinear Forms <w-23>`, :ref:`W.27 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads <w-27>`

.. toctree::
   :hidden:

   code
