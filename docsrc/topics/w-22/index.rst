:order: 22
:type: topic
:category: Projective Geometry & Harmonic Ranges
:tags: cross-ratio, harmonic range, projective invariance, Pappus, perspectivity

.. _w-22:

=================================================================
W.22 Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge
=================================================================

*Exact Equivalence of Line-Pencil Spread Cross-Ratio and Point-Range Quadrance Cross-Ratio*

.. enunciation::

   If four concurrent lines r_1, r_2, r_3, r_4 through O_p meet a transversal l_a at collinear points A_1, A_2, A_3, A_4 and another transversal l_b at B_1, B_2, B_3, B_4, then the squared cross-ratio in quadrances (Q(A_1, A_3)*Q(A_2, A_4)) / (Q(A_1, A_4)*Q(A_2, A_3)) equals the pencil spread cross-ratio (s_13 * s_24) / (s_14 * s_23) and is invariant across all transversals.

.. figure:: w-22.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.22 (Projective Cross-Ratio, Harmonic Pencils & The Pappus Bridge)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O_p : Point
   A_1 : Point
   A_2 : Point
   B_1 : Point
   B_2 : Point
   =====
   l_a = line(A_1, A_2)
   l_b = line(B_1, B_2)
   r_1 = line(O_p, A_1)
   r_2 = line(O_p, A_2)
   r_3 = line(O_p, A_3)
   r_4 = line(O_p, A_4)
   B_3 = meet(r_3, l_b)
   B_4 = meet(r_4, l_b)

Mathematical Synthesis
----------------------

:person:`Pappus of Alexandria <pappus>` discovered that the cross-ratio of four collinear points is preserved under central projection (:cite:`CoxeterGreitzer1967`). In Rational Trigonometry (:cite:`Wildberger2005`), squaring the classical signed cross-ratio replaces signed lengths with :term:`quadrance` along transversals :g:`l_a` (:g:`A_1`, :g:`A_2`, :g:`A_3`, :g:`A_4`) and :g:`l_b` (:g:`B_1`, :g:`B_2`, :g:`B_3`, :g:`B_4`), and replaces directed sine ratios in the pencil of rays :g:`r_1`, :g:`r_2`, :g:`r_3`, :g:`r_4` through :g:`O_p` with pairwise :term:`spread`!

Applying the :term:`Spread Law` to the four sub-triangles at apex :g:`O_p` cancels all radial quadrances :math:`Q(O_p, A_i)` and transversal spreads :math:`s(r_i, \ell_a)` in a single stroke, proving :math:`R_Q(A_1, A_2; A_3, A_4) = R_s(r_1, r_2; r_3, r_4) = R_Q(B_1, B_2; B_3, B_4)`. When the signed cross-ratio is :math:`-1` (**harmonic conjugates**), its quadrance cross-ratio is identically :math:`(-1)^2 = 1`, directly uniting ``geometor/wildberger``, ``geometor/pappus``, and :ref:`F.25 Harmonic Conjugates <f-25>`!

Key Algebraic Identities
------------------------

.. math::

   (A_1, A_2; A_3, A_4)_Q = \frac{Q(A_1, A_3)\, Q(A_2, A_4)}{Q(A_1, A_4)\, Q(A_2, A_3)} = \frac{s(r_1, r_3)\, s(r_2, r_4)}{s(r_1, r_4)\, s(r_2, r_3)} = (B_1, B_2; B_3, B_4)_Q

.. math::

   \text{Harmonic Range } (A_1, A_2; A_3, A_4) = -1 \implies Q(A_1, A_3)\, Q(A_2, A_4) = Q(A_1, A_4)\, Q(A_2, A_3)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Harmonic quadruple (A_1, A_2; A_3, A_4)``
     - ``[0,0], [4,0]; [3,0], [6,0]``
     - Signed CR = -1 => Quadrance CR_Q = 1
   * - ``Pencil spread cross-ratio CR_s at O_p``
     - ``1``
     - Equals (s_13*s_24)/(s_14*s_23) = 1
   * - ``Projected range (B_1, B_2; B_3, B_4) on l_b``
     - ``CR_Q(B) = 1``
     - Exact projective invariance CR_a == CR_s == CR_b

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-22.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Classical Canon**
     - :person:`Pappus of Alexandria <pappus>` (*Collection* Book VII) & :person:`Girard Desargues <desargues>`
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.5`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.25 Harmonic Conjugates <f-25>` (:cite:`SeeligNotebooks`)
   * - **Sister Codices**
     - ``geometor/pappus`` (projective cross-ratio & harmonic ranges)

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
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#d8dee9", color="#4c566a", URL="../w-04/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.22" [label="W.22\nProjective Cross-Ratio, Harmoni...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-22/index.html"];
       "W.01" -> "W.22";
       "W.03" -> "W.22";
       "W.04" -> "W.22";
       "W.08" -> "W.22";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`

.. toctree::
   :hidden:

   code
