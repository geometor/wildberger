:order: 21
:type: topic
:category: Algebraic Tangents & Optical Reflection
:tags: Taylor conic, tangent, parabola reflection, quadrola reflection, optics

.. _w-21:

================================================================
W.21 Taylor Conics, Algebraic Tangents & Optical Reflection Laws
================================================================

*Derivative-Free Tangent Proportions and Exact Equal-Spread Focal Reflections*

.. enunciation::

   Translating any conic f(x, y) = 0 to a point A = [x_0, y_0] on the conic isolates a unique linear term l_1(x - x_0, y - y_0) = 0 defining its algebraic tangent t_tan without limits; for a parabola, t_tan is the perpendicular bisector of focus F_0 and directrix foot D_0 (giving equal spreads with F_0 A and the axis), and for a quadrola, t_tan makes equal spreads with both focal lines F_1 P_q and F_2 P_q.

.. figure:: w-21.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.21 (Taylor Conics, Algebraic Tangents & Optical Reflection Laws)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   F_0 : Point
   D_1 : Point
   D_2 : Point
   A : Point
   =====
   l_dir = line(D_1, D_2)
   parabola = parabola_locus(F_0, l_dir)
   D_0 = foot(A, l_dir)
   t_tan = perp_bisector(F_0, D_0)
   l_in = line(F_0, A)
   l_out = line(D_0, A)

Mathematical Synthesis
----------------------

Over finite or discrete fields there are no limits :math:`\lim_{h \to 0}`, yet conics possess exact tangents! Expanding :math:`f(x_0 + u, y_0 + v) = f(x_0, y_0) + \ell_1(u, v) + q_2(u, v)` (the **Taylor Conic Translation** of :person:`Brook Taylor <taylor>`, :cite:`Wildberger2005`) produces the algebraic tangent line :math:`\ell_A = \langle 2 a x_0 + b y_0 + d : b x_0 + 2 c y_0 + e : d x_0 + e y_0 + 2 f \rangle` whenever :math:`A = [x_0, y_0]` is non-singular.

Applied to :g:`parabola` (focus :g:`F_0`, directrix :g:`l_dir`), the tangent :g:`t_tan` at :g:`A` is literally the **perpendicular bisector** of :g:`F_0` and the directrix foot :g:`D_0`! Since :math:`D_0 A` (:g:`l_out`) is perpendicular to :g:`l_dir` (hence parallel to the parabola's axis), reflection symmetry across :g:`t_tan` immediately proves the **Parabola Reflection Theorem** :math:`s(t_{\text{tan}}, F_0 A) = s(t_{\text{tan}}, D_0 A)` over every field! Analogously, at any point :g:`P_q` on a :term:`quadrola` :g:`quadrola` with foci :g:`F_1`, :g:`F_2`, the algebraic tangent :g:`t_q` satisfies :math:`s(t_q, F_1 P_q) = s(t_q, F_2 P_q)`.

Key Algebraic Identities
------------------------

.. math::

   \ell_A = \langle 2 a x_0 + b y_0 + d :\; b x_0 + 2 c y_0 + e :\; d x_0 + e y_0 + 2 f \rangle

.. math::

   s(t_{\text{tan}}, F_0 A) = s(t_{\text{tan}}, D_0 A), \qquad s(t_q, F_1 P_q) = s(t_q, F_2 P_q)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Taylor conic constant term at A=[4,5]``
     - ``0``
     - Verified == 0 (A lies on parabola)
   * - ``Tangent t_tan == perp_bisector(F_0, D_0)``
     - ``s(t_tan, pb) = 0``
     - Exact line coincidence
   * - ``Parabola reflection spreads at A``
     - ``1/5 == 1/5``
     - Equal focal and axial spreads
   * - ``Quadrola reflection spreads at P_q``
     - ``25/34 == 25/34``
     - Equal bifocal tangent spreads

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-21.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Classical Canon**
     - :person:`Apollonius <apollonius>` (*Conics* III.48) & :person:`Diocles <diocles>` (*On Burning Mirrors*)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.39 Pole and Polar with Respect to a Triangle <f-39>`
   * - **Algebraic Geometry**
     - Purely polynomial tangent space over ``Q`` and ``F_p`` without calculus

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
       "W.20" [label="W.20\nMetrical Conics: Circles, Ribbo...", fillcolor="#d8dee9", color="#4c566a", URL="../w-20/index.html"];
       "W.21" [label="W.21\nTaylor Conics, Algebraic Tangen...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-21/index.html"];
       "W.26" [label="W.26\nAlgebraic Physics: Projectile P...", fillcolor="#e5e9f0", color="#777777", URL="../w-26/index.html"];
       "W.02" -> "W.21";
       "W.03" -> "W.21";
       "W.20" -> "W.21";
       "W.21" -> "W.26";
   }

**Depends on**: :ref:`W.02 Lineations, Central Rotations & Reflections in Lines <w-02>`, :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.20 Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas <w-20>`

**Required for**: :ref:`W.26 Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity <w-26>`

.. toctree::
   :hidden:

   code
