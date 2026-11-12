:order: 26
:type: topic
:category: Algebraic Mechanics, Optics & Relativity
:tags: projectile motion, parabola, Snell's law, refraction, special relativity

.. _w-26:

======================================================================
W.26 Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity
======================================================================

*Eliminating Transcendental Angles from Ballistics, Wave Refraction, and Lorentz Boosts*

.. enunciation::

   A Galilean projectile launched from O with initial speed-squared v^2 and elevation spread s traces a parabola whose apex height h = v^2*s/(2*g), horizontal range quadrance Q_range = 16*(v^4/(4*g^2))*s*(1 - s) = (v^4/g^2)*S_2(s), and focus-directrix geometry depend rationally on s; Snell's refraction law becomes n_1^2 * s_1 = n_2^2 * s_2 in spreads.

.. figure:: w-26.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.26 (Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   V_apex : Point
   R_range : Point
   =====
   traj = projectile_parabola(O, V_apex, R_range)
   F_traj = focus(traj)
   l_dir = directrix(traj)
   l_iface = line(I_inc, P_ref)
   l_norm = altitude(l_iface, P_ref)

Mathematical Synthesis
----------------------

Physics formulas are filled with :math:`\sin^2\theta`, :math:`\cos^2\theta`, and :math:`\sin(2\theta)` that become **purely algebraic** when expressed in :term:`quadrance` and :term:`spread` (:cite:`Wildberger2005`). For a projectile launched from :g:`O` landing at :g:`R_range` via apex :g:`V_apex` along trajectory :g:`traj` (focus :g:`F_traj`, directrix :g:`l_dir`), the horizontal range quadrance is governed directly by the logistic spread polynomial :math:`S_2(s) = 4 s (1 - s)`, immediately proving maximum range at :math:`s = 1/2` and equal ranges for complementary spreads :math:`s` and :math:`1 - s`!

Across an optical interface :g:`l_iface` with normal :g:`l_norm` at :g:`P_ref` (incident from :g:`I_inc`, refracted toward :g:`T_trans`), :person:`Willebrord Snellius <snellius>`' law :math:`n_1 \sin\theta_1 = n_2 \sin\theta_2` squares cleanly to the **linear spread proportion** :math:`n_1^2 s_1 = n_2^2 s_2`, with total internal reflection occurring precisely when :math:`(n_1^2 / n_2^2) s_1 > 1`! And in special relativity, Einstein's velocity addition and spacetime intervals are native instances of the Red Minkowski metric (:ref:`W.23 <w-23>`).

Key Algebraic Identities
------------------------

.. math::

   y = x \sqrt{\frac{s}{1-s}} - \frac{g x^2}{2 v^2 (1 - s)}, \qquad Q_{\text{range}} = \frac{v^4}{g^2} S_2(s) = \frac{4 v^4}{g^2} s(1 - s)

.. math::

   \text{Snell's Spread Law:}\quad n_1^2\, s_1 = n_2^2\, s_2, \qquad s_{\text{crit}} = \frac{n_2^2}{n_1^2}\; (n_1 > n_2)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Projectile range law Q_range(s) ~ S_2(s)``
     - ``S_2(1/2) = 1, S_2(s) == S_2(1 - s)``
     - Complementary spreads land identically
   * - ``Trajectory focus & directrix``
     - ``F_traj = [4, 0], l_dir: y = 4``
     - Exact focus-directrix parabola
   * - ``Snell's Spread Law n_1^2 * s_1 == n_2^2 * s_2``
     - ``9 * (16/25) == 16 * (9/25) == 144/25``
     - Integer ray vectors [-4,3] -> [3,-4]

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-26.svg``)
   * - **Thematic Part**
     - Part IV: Practical Solvers, 3D Platonic Geometry & Polar Curves
   * - **Physical Canon**
     - :person:`Galileo Galilei <galileo>` (1638) & :person:`Willebrord Snellius <snellius>` (1621)
   * - **GEOMETOR Fundamentals**
     - :ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.22 Functions <f-22>`
   * - **Chromogeometry Bridge**
     - Relativistic spacetime intervals instantiate the Red metric ``Q_R`` (:ref:`W.23 <w-23>`)
   * - **Optics Bridge**
     - Complements parabolic mirror reflection in :ref:`W.21 <w-21>`

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.05" [label="W.05\nSpread Polynomials S_n(s) & Pen...", fillcolor="#d8dee9", color="#4c566a", URL="../w-05/index.html"];
       "W.20" [label="W.20\nMetrical Conics: Circles, Ribbo...", fillcolor="#d8dee9", color="#4c566a", URL="../w-20/index.html"];
       "W.21" [label="W.21\nTaylor Conics, Algebraic Tangen...", fillcolor="#d8dee9", color="#4c566a", URL="../w-21/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#d8dee9", color="#4c566a", URL="../w-23/index.html"];
       "W.26" [label="W.26\nAlgebraic Physics: Projectile P...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-26/index.html"];
       "W.05" -> "W.26";
       "W.20" -> "W.26";
       "W.21" -> "W.26";
       "W.23" -> "W.26";
   }

**Depends on**: :ref:`W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads <w-05>`, :ref:`W.20 Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas <w-20>`, :ref:`W.21 Taylor Conics, Algebraic Tangents & Optical Reflection Laws <w-21>`, :ref:`W.23 Chromogeometry & Universal Symmetric Bilinear Forms <w-23>`

.. toctree::
   :hidden:

   code
