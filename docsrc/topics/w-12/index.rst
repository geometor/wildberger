:order: 12
:type: topic
:category: Triangle Centers & Number Theory
:tags: vertex bisector, square vertex, incenter, inquadrance, excenters

.. _w-12:

===========================================================
W.12 Vertex Bisectors, Square Vertices & The Four Incenters
===========================================================

*Number-Theoretic Criterion for Rational Bisectors and Symmetric Inquadrances*

.. enunciation::

   The locus of points X having equal quadrance Q(X, l_1) = Q(X, l_2) to two intersecting non-null lines l_1, l_2 splits into two orthogonal vertex bisectors over F if and only if (a_1^2 + b_1^2)(a_2^2 + b_2^2) is a square in F; when two vertices of a triangle have bisectors in F, so does the third, producing four symmetric incenters I_0, I_1, I_2, I_3.

.. figure:: w-12.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.12 (Vertex Bisectors, Square Vertices & The Four Incenters)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   I_0 = incenter(A_1, A_2, A_3)
   b_1 = line(A_1, I_0)
   b_2 = line(A_2, I_0)
   b_3 = line(A_3, I_0)
   c_in = circle(I_0, foot(I_0, line(A_1, A_2)))

Mathematical Synthesis
----------------------

Unlike medians and altitudes—which always exist rationally over :math:`F`—:term:`vertex bisector` lines reveal a deep arithmetic obstruction in Universal Geometry (:cite:`Wildberger2005`). Equating :math:`Q(X, \ell_1) = Q(X, \ell_2)` gives :math:`(a_2^2 + b_2^2)(a_1 x + b_1 y + c_1)^2 = (a_1^2 + b_1^2)(a_2 x + b_2 y + c_2)^2`, which factors into two perpendicular linear equations over :math:`F` if and only if the vertex is a :term:`square vertex` (:math:`(a_1^2 + b_1^2)(a_2^2 + b_2^2) = r^2` in :math:`F`, equivalently :math:`1 - s` is a square when one line has norm square).

When two vertices of :g:`t` admit bisectors in :math:`F`, **Theorem 88** guarantees that the third vertex also admits bisectors, intersecting in four completely symmetric :term:`incenter` points :math:`I_0, I_1, I_2, I_3` (classical :math:`X(1)` :g:`I_0` and the three excenters). For the Heronian triangle :math:`A_1=[0,0], A_2=[14,0], A_3=[5,12]`, all three vertices are square over :math:`\mathbb{Q}`, placing :g:`I_0` at exact integer coordinates :math:`[6, 4]` with :term:`inquadrance` :math:`R_0 = 16` (:g:`c_in`)!

Key Algebraic Identities
------------------------

.. math::

   Q(X, \ell_1) = Q(X, \ell_2) \iff (a_2^2 + b_2^2)(a_1 x + b_1 y + c_1)^2 = (a_1^2 + b_1^2)(a_2 x + b_2 y + c_2)^2

.. math::

   s(I A_1, I A_2) = 1 - s(A_3 I, A_3 A_1), \qquad \mathcal{A}(Q_1, Q_2, Q_3) \text{ & } R_i:\; Q(I_0, \ell_1) = Q(I_0, \ell_2) = Q(I_0, \ell_3) = R_0

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Square vertex norms (|l_2|^2*|l_3|^2, ...)``
     - ``(169*196, 225*196, 169*225)``
     - All three products are exact squares in Q!
   * - ``Rational Incenter I_0 = X(1)``
     - ``[6, 4]``
     - Exact integer coordinates
   * - ``Equal side quadrances Q(I_0, l_i) = R_0``
     - ``16 == 16 == 16``
     - Inquadrance R_0 = 16
   * - ``Incenter Spread Theorem (Thm 89)``
     - ``s(I_0 A_1, I_0 A_2) = 49/65``
     - Matches 1 - s(A_3 I_0, A_3 A_1) = 49/65

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-12.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Euclid's Elements**
     - :ref:`I.9`, :ref:`IV.4` (Angle bisection and inscribed circle, :cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.8`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.28 Incenter <f-28>`, :ref:`F.29 Inradius <f-29>` (:cite:`SeeligNotebooks`)
   * - **ETC Reference**
     - Incenter ``X(1)`` & Excenters in ``geometor/etc`` (:cite:`Kimberling1998`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.02" [label="W.02\nLineations, Central Rotations &...", fillcolor="#d8dee9", color="#4c566a", URL="../w-02/index.html"];
       "W.03" [label="W.03\nQuadrance, Midpoints & Point-to...", fillcolor="#d8dee9", color="#4c566a", URL="../w-03/index.html"];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#d8dee9", color="#4c566a", URL="../w-04/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#d8dee9", color="#4c566a", URL="../w-10/index.html"];
       "W.12" [label="W.12\nVertex Bisectors, Square Vertic...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-12/index.html"];
       "W.02" -> "W.12";
       "W.03" -> "W.12";
       "W.04" -> "W.12";
       "W.10" -> "W.12";
   }

**Depends on**: :ref:`W.02 Lineations, Central Rotations & Reflections in Lines <w-02>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`

.. toctree::
   :hidden:

   code
