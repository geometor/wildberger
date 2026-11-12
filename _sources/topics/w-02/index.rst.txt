:order: 2
:type: topic
:category: Isometries & Lineations
:tags: reflections, rotations, lineations, symmetry, isometries

.. _w-02:

=========================================================
W.02 Lineations, Central Rotations & Reflections in Lines
=========================================================

*Square-Root-Free Point and Line Reflections Across Arbitrary Non-Null Axes*

.. enunciation::

   For any non-null line l = <a : b : c> over a field F (char F != 2), the reflection sigma_l maps every point A = [x, y] and every line m = <a_2 : b_2 : c_2> to exact rational images whose denominators depend only on the quadratic norm a^2 + b^2, without radicals or angles.

.. figure:: w-02.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.02 (Lineations, Central Rotations & Reflections in Lines)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   P_1 : Point
   P_2 : Point
   A : Point
   B : Point
   =====
   l = line(P_1, P_2)
   F = foot(A, l)
   A_r = reflect_point(A, l)
   m = line(A, B)
   m_r = reflect_line(m, l)

Mathematical Synthesis
----------------------

Classical orthogonal reflection across an oblique axis typically invokes unit normal vectors containing :math:`\sqrt{a^2 + b^2}` or trigonometric double-angle matrices. In Universal Geometry (:cite:`Wildberger2005`, :cite:`SnapperTroyer1971`), because the foot :g:`F` of the altitude from :g:`A` to :g:`l` is rational in :math:`(a, b, c)`, the reflected point :g:`A_r` :math:`= 2 F - A` is **always rational** over the ground field :math:`F`!

Even more remarkably, reflecting an entire line :g:`m` across :g:`l` produces the reflected line :g:`m_r` :math:`= \Sigma_l(m)` via homogeneous quadratic polynomials in :math:`(a, b)`. Iterating line reflections generates cyclic reflection sequences that directly govern :term:`spread polynomials` and regular star symmetries over both :math:`\mathbb{Q}` and finite fields.

Key Algebraic Identities
------------------------

.. math::

   \sigma_\ell([x, y]) = \left[\frac{(b^2 - a^2)x - 2 a b y - 2 a c}{a^2 + b^2},\; \frac{-2 a b x + (a^2 - b^2)y - 2 b c}{a^2 + b^2}\right]

.. math::

   \Sigma_\ell(\langle a_2 : b_2 : c_2 \rangle) = \langle (a^2 - b^2)a_2 + 2 a b b_2 :\; 2 a b a_2 - (a^2 - b^2)b_2 :\; 2 c(a a_2 + b b_2) - (a^2 + b^2)c_2 \rangle

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Mirror axis l = line(P_1, P_2)``
     - ``<-1 : 2 : 0>``
     - Norm a^2 + b^2 = 5
   * - ``Reflected point sigma_l([1, 4])``
     - ``[19/5, -8/5]``
     - Exact in Q^2
   * - ``Reflected line Sigma_l(m)``
     - ``<-16 : 12 : 80>``
     - Matches line(A_r, B_r)
   * - ``Quadrance preservation Q(A,B) == Q(A_r,B_r)``
     - ``16 == 16``
     - Verified
   * - ``Equal spreads s(l, m) == s(l, m_r)``
     - ``1/5 == 1/5``
     - Verified

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-02.svg``)
   * - **Thematic Part**
     - Part I: Preliminaries & Foundational Invariants
   * - **Euclid's Elements**
     - :ref:`I.9`, :ref:`I.10`, :ref:`I.12` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.5 Centers of Similitude <f-05>`
   * - **Metric Affine Canon**
     - :cite:`SnapperTroyer1971` (Orthogonal reflections over general fields)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.01" [label="W.01\nPlanar Points, Line Proportions...", fillcolor="#d8dee9", color="#4c566a", URL="../w-01/index.html"];
       "W.02" [label="W.02\nLineations, Central Rotations &...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-02/index.html"];
       "W.05" [label="W.05\nSpread Polynomials S_n(s) & Pen...", fillcolor="#e5e9f0", color="#777777", URL="../w-05/index.html"];
       "W.12" [label="W.12\nVertex Bisectors, Square Vertic...", fillcolor="#e5e9f0", color="#777777", URL="../w-12/index.html"];
       "W.21" [label="W.21\nTaylor Conics, Algebraic Tangen...", fillcolor="#e5e9f0", color="#777777", URL="../w-21/index.html"];
       "W.01" -> "W.02";
       "W.02" -> "W.05";
       "W.02" -> "W.12";
       "W.02" -> "W.21";
   }

**Depends on**: :ref:`W.01 Planar Points, Line Proportions & Incidence Determinants <w-01>`

**Required for**: :ref:`W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads <w-05>`, :ref:`W.12 Vertex Bisectors, Square Vertices & The Four Incenters <w-12>`, :ref:`W.21 Taylor Conics, Algebraic Tangents & Optical Reflection Laws <w-21>`

.. toctree::
   :hidden:

   code
