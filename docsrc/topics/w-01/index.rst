:order: 1
:type: topic
:category: Affine & Projective Incidence
:tags: proportions, lines, determinants, collinearity, concurrency, altitude

.. _w-01:

=============================================================
W.01 Planar Points, Line Proportions & Incidence Determinants
=============================================================

*Field-Independent Coordinate Incidence, Parallels, and Altitudes*

.. enunciation::

   Over any field F of characteristic not equal to 2, a planar point is an ordered pair A = [x, y] and a planar line is a homogeneous 3-proportion l = <a : b : c> with (a, b) != (0, 0) representing a*x + b*y + c = 0; three points are collinear and three lines are concurrent if and only if their respective 3x3 coordinate determinants vanish.

.. figure:: w-01.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.01 (Planar Points, Line Proportions & Incidence Determinants)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   l_3 = line(A_1, A_2)
   p_3 = parallel(l_3, A_3)
   n_3 = altitude(l_3, A_3)
   F_3 = meet(l_3, n_3)

Mathematical Synthesis
----------------------

In :person:`Norman J. Wildberger <wildberger>`'s algebraic foundation (:cite:`Wildberger2005`), classical continuum postulates are replaced by arithmetic over an arbitrary field :math:`F` (:math:`\operatorname{char} F \neq 2`). Two distinct points :g:`A_1` :math:`= [x_1, y_1]` and :g:`A_2` :math:`= [x_2, y_2]` determine a unique line proportion :g:`l_3` :math:`= \langle y_1 - y_2 : x_2 - x_1 : x_1 y_2 - x_2 y_1 \rangle`, while two non-parallel lines meet at a unique rational point given by Cramer's determinant ratios.

Parallelism (:math:`a_1 b_2 - a_2 b_1 = 0`) and Euclidean perpendicularity (:math:`a_1 a_2 + b_1 b_2 = 0`) are purely polynomial conditions. Given an external point :g:`A_3` and a non-:term:`null line` :g:`l_3`, both the parallel line :g:`p_3` and the altitude :g:`n_3` meeting :g:`l_3` at its foot :g:`F_3` are obtained by exact rational expressions without square roots or compass arcs—bridging :person:`René Descartes <descartes>`' coordinate algebra directly to projective incidence in ``geometor/pappus``.

Key Algebraic Identities
------------------------

.. math::

   \ell(A_1, A_2) = \langle y_1 - y_2 : x_2 - x_1 : x_1 y_2 - x_2 y_1 \rangle, \qquad \ell_1 \cap \ell_2 = \left[\frac{b_1 c_2 - b_2 c_1}{a_1 b_2 - a_2 b_1},\; \frac{a_2 c_1 - a_1 c_2}{a_1 b_2 - a_2 b_1}\right]

.. math::

   F_3 = \left[\frac{b^2 x_3 - a b y_3 - a c}{a^2 + b^2},\; \frac{-a b x_3 + a^2 y_3 - b c}{a^2 + b^2}\right], \qquad \det\begin{pmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{pmatrix} = 0

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Line proportion l_3 = line(A_1, A_2)``
     - ``<-3 : 6 : -6>``
     - Exact integer 3-proportion
   * - ``Parallel proportion p_3 through A_3``
     - ``<-3 : 6 : -30>``
     - a_1*b_2 - a_2*b_1 = 0
   * - ``Altitude foot F_3 = meet(l_3, n_3)``
     - ``[18/5, 14/5]``
     - Zero radicals
   * - ``Collinearity det(A_1, A_2, F_3)``
     - ``0``
     - Verified == 0
   * - ``Concurrency det at F_3``
     - ``0``
     - Verified == 0

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-01.svg``)
   * - **Thematic Part**
     - Part I: Preliminaries & Foundational Invariants
   * - **Euclid's Elements**
     - :ref:`I.11`, :ref:`I.12`, :ref:`I.31` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.1`, :ref:`G.3`, :ref:`G.4`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.14 Conway Notation <f-14>` (:cite:`SeeligNotebooks`)
   * - **Sister Codices**
     - ``geometor/pappus`` (projective collinearity & concurrency determinants)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.01" [label="W.01\nPlanar Points, Line Proportions...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-01/index.html"];
       "W.02" [label="W.02\nLineations, Central Rotations &...", fillcolor="#e5e9f0", color="#777777", URL="../w-02/index.html"];
       "W.03" [label="W.03\nQuadrance, Midpoints & Point-to...", fillcolor="#e5e9f0", color="#777777", URL="../w-03/index.html"];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#e5e9f0", color="#777777", URL="../w-04/index.html"];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#e5e9f0", color="#777777", URL="../w-07/index.html"];
       "W.13" [label="W.13\nStewart's Theorem, Median Quadr...", fillcolor="#e5e9f0", color="#777777", URL="../w-13/index.html"];
       "W.14" [label="W.14\nMenelaus, Ceva & The Alternate...", fillcolor="#e5e9f0", color="#777777", URL="../w-14/index.html"];
       "W.15" [label="W.15\nCircumcenter, Orthocenter & Uni...", fillcolor="#e5e9f0", color="#777777", URL="../w-15/index.html"];
       "W.22" [label="W.22\nProjective Cross-Ratio, Harmoni...", fillcolor="#e5e9f0", color="#777777", URL="../w-22/index.html"];
       "W.01" -> "W.02";
       "W.01" -> "W.03";
       "W.01" -> "W.04";
       "W.01" -> "W.07";
       "W.01" -> "W.13";
       "W.01" -> "W.14";
       "W.01" -> "W.15";
       "W.01" -> "W.22";
   }

**Required for**: :ref:`W.02 Lineations, Central Rotations & Reflections in Lines <w-02>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`, :ref:`W.13 Stewart's Theorem, Median Quadrances & The Centroid <w-13>`, :ref:`W.14 Menelaus, Ceva & The Alternate Spreads Theorem <w-14>`, :ref:`W.15 Circumcenter, Orthocenter & Universal Affine Barycentrics <w-15>`, :ref:`W.22 Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge <w-22>`

.. toctree::
   :hidden:

   code
