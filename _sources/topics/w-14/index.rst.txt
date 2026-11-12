:order: 14
:type: topic
:category: Projective & Cevian Proportions
:tags: Menelaus' theorem, Ceva's theorem, alternate spreads, cevians, transversal

.. _w-14:

===================================================
W.14 Menelaus, Ceva & The Alternate Spreads Theorem
===================================================

*Multiplicative Quadrance and Spread Balance for Collinearity and Concurrency*

.. enunciation::

   If either a transversal line l cuts the sidelines A_2 A_3, A_3 A_1, A_1 A_2 of a non-null triangle at B_1, B_2, B_3 (Menelaus) or three cevians through a point A_0 meet the opposite sidelines at B_1, B_2, B_3 (Ceva), then the six segment quadrances satisfy Q(A_2, B_1) * Q(A_3, B_2) * Q(A_1, B_3) = Q(B_1, A_3) * Q(B_2, A_1) * Q(B_3, A_2).

.. figure:: w-14.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.14 (Menelaus, Ceva & The Alternate Spreads Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   A_0 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   B_1 = meet(line(A_2, A_3), line(A_1, A_0))
   B_2 = meet(line(A_1, A_3), line(A_2, A_0))
   B_3 = meet(line(A_1, A_2), line(A_3, A_0))

Mathematical Synthesis
----------------------

Classically, :person:`Menelaus <menelaus>`' theorem (:math:`\prod = -1`) and :person:`Giovanni Ceva <ceva>`'s theorem (:math:`\prod = +1`) differ only in sign! Because :term:`quadrance` squares signed ratios, **both** collinear transversals and concurrent cevians through :g:`A_0` satisfy the identical necessary multiplicative law :math:`R_1 R_2 R_3 = P_1 P_2 P_3` at division points :g:`B_1`, :g:`B_2`, :g:`B_3` (:cite:`Wildberger2005`). (Consequently, the converse of neither quadrance product holds alone—their combined six-solution locus splits neatly into the collinear Menelaus configurations and concurrent Ceva configurations!)

Underpinning Ceva's theorem is the **Alternate Spreads Theorem** (Theorem 79): for any point :g:`A_0` in the plane of :g:`t`, the alternating vertex spreads :math:`r_i = s(A_i A_{i+1}, A_i A_0)` and :math:`p_i = s(A_i A_{i-1}, A_i A_0)` satisfy :math:`r_1 r_2 r_3 = p_1 p_2 p_3`—an invariant that generalizes to any :math:`n`-gon and drives the algebraic solution of :term:`Hansen's problem` (:ref:`W.25 <w-25>`).

Key Algebraic Identities
------------------------

.. math::

   Q(A_2, B_1)\, Q(A_3, B_2)\, Q(A_1, B_3) = Q(B_1, A_3)\, Q(B_2, A_1)\, Q(B_3, A_2)

.. math::

   \text{Alternate Spreads:}\quad s(A_1 A_2, A_1 A_0)\, s(A_2 A_3, A_2 A_0)\, s(A_3 A_1, A_3 A_0) = s(A_1 A_3, A_1 A_0)\, s(A_2 A_1, A_2 A_0)\, s(A_3 A_2, A_3 A_0)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Cevian feet B_1, B_2, B_3``
     - ``B_1=[180/23, 108/23], B_2=[48/25, 108/25], B_3=[11/2, 0]``
     - Exact rational intersections
   * - ``Ceva Quadrance Balance LHS == RHS``
     - ``2070829332/66125 == 2070829332/66125``
     - Verified exact equality
   * - ``Alternate Spreads Product r_1*r_2*r_3 == p_1*p_2*p_3``
     - ``14907321/1026238660 == 14907321/1026238660``
     - Theorem 79 verified

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-14.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`VI.2` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.5`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.7 Ceva and Menelaus <f-07>` (26 manuscript folios, :cite:`SeeligNotebooks`)
   * - **Sister Codices**
     - ``geometor/pappus`` (projective incidence & transversal invariants)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.01" [label="W.01\nPlanar Points, Line Proportions...", fillcolor="#d8dee9", color="#4c566a", URL="../w-01/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.14" [label="W.14\nMenelaus, Ceva & The Alternate...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-14/index.html"];
       "W.25" [label="W.25\nSnellius–Pothenot Resection & H...", fillcolor="#e5e9f0", color="#777777", URL="../w-25/index.html"];
       "W.01" -> "W.14";
       "W.08" -> "W.14";
       "W.14" -> "W.25";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`

**Required for**: :ref:`W.25 Snellius–Pothenot Resection & Hansen's Surveying Problem <w-25>`

.. toctree::
   :hidden:

   code
