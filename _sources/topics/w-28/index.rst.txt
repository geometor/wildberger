:order: 28
:type: topic
:category: Rational Polar Coordinates & Algebraic Surfaces
:tags: rational polar, lemniscate, cardioid, folium of Descartes, ellipson

.. _w-28:

================================================================
W.28 Rational Polar Coordinates, Classical Curves & The Ellipson
================================================================

*Parametrizing Curves by [s, Q] and Slicing the Cubic Triple-Spread Surface*

.. enunciation::

   Replacing polar coordinates (r, theta) with rational polar coordinates [s, Q] where s = x^2 / (x^2 + y^2) (spread to the y-axis) and Q = x^2 + y^2 converts classical polar curves into exact polynomial relations—Bernoulli's lemniscate s = (Q + 2)/4 (or Q = a*(2*s - 1)), Descartes' folium (2*s - 1)^2*(s^2 - s + 1)^2*Q^2 - 18*s*(1 - s)*(1 - 3*s + 3*s^2)*Q + 81*s^2*(1 - s)^2 = 0, and the deltoid/ellipson S_3(s) law—while (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 cuts out the tetrahedral Ellipson.

.. figure:: w-28.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.28 (Rational Polar Coordinates, Classical Curves & The Ellipson)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A_ref : Point
   =====
   l_ref = line(O, A_ref)
   lemniscate = curve_lemniscate(O, l_ref)
   cardioid = curve_cardioid(O, l_ref)
   folium = curve_folium(O, l_ref)
   ellipson_slice = curve_ellipson_section()

Mathematical Synthesis
----------------------

Traditional polar coordinates :math:`(r, \theta)` mix a radical :math:`r = \sqrt{x^2 + y^2}` with a transcendental angle :math:`\theta`, defined only modulo :math:`2\pi`. :person:`Norman J. Wildberger <wildberger>`'s **rational polar coordinates** :math:`[s, Q]` (:cite:`Wildberger2005`, Chapter 27 & Appendices A–B) pair the polar :term:`spread` :math:`s \equiv x^2 / (x^2 + y^2)` measured from the vertical :math:`y`-axis :g:`l_ref` (through :g:`O` and :g:`A_ref`) with the radial :term:`quadrance` :math:`Q \equiv x^2 + y^2`, aligning directly with navigation azimuths and 3D rational spherical coordinates.

Classical curves simplify dramatically in :math:`[s, Q]`: :person:`Jakob Bernoulli <bernoulli>`'s figure-eight **lemniscate** (:g:`lemniscate`, :math:`(x^2 + y^2)^2 = a(x^2 - y^2)`) becomes the **linear** equation :math:`Q = a(2 s - 1)` (:math:`s = (Q + 2)/4` for :math:`a = 2`), while :person:`René Descartes <descartes>`' **folium** (:g:`folium`, :math:`x^3 + y^3 + 3 x y = 0`) eliminates quadrant signs via :math:`(1 - 3s + 3s^2)^2 - 4 s^3(1 - s)^3 = (2s - 1)^2(s^2 - s + 1)^2`, and the **cardioid** (:g:`cardioid`) admits a pure rational parametrization. Crowning the codex is the **Ellipson** (:g:`ellipson_slice`): the inflated-tetrahedron cubic surface inside :math:`[0, 1]^3` defined by the :term:`Triple Spread Formula`, whose horizontal slices :math:`s_3 = c` are ellipses inscribed in :math:`[0, 1]^2` (an exact circle at :math:`c = 1/2`!) and whose oblique slice :math:`s_1 + s_2 + s_3 = 2` satisfies :math:`S_3(s) = (36 Q - 5)^2 / (6 Q)^3`!

Key Algebraic Identities
------------------------

.. math::

   s \equiv \frac{x^2}{x^2 + y^2}, \quad Q \equiv x^2 + y^2 \implies \text{Lemniscate: } Q = a(2 s - 1), \quad \text{Folium: } (2s - 1)^2(s^2 - s + 1)^2 Q^2 - 18 s(1 - s)(1 - 3s + 3s^2) Q + 81 s^2(1 - s)^2 = 0

.. math::

   \text{Ellipson }\mathcal{E} \subset [0, 1]^3:\quad (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3 \quad \Big(s_3 = \tfrac{1}{2} \implies \big(s_1 - \tfrac{1}{2}\big)^2 + \big(s_2 - \tfrac{1}{2}\big)^2 = \tfrac{1}{4}\Big)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Lemniscate [s, Q] law Q == 16*(2*s - 1)``
     - ``Q = 4608/337, 16*(2*s - 1) = 4608/337``
     - Linear in [s, Q] (s to y-axis)
   * - ``Folium of Descartes [s, Q] quadratic (t=2)``
     - ``s=1/5, Q=20/9 => residual = 0``
     - Matches Wildberger App. A p. 286
   * - ``Ellipson horizontal slice s_3 = 1/2``
     - ``S(4/5, 9/10, 1/2) == 0``
     - Exact inscribed circle in [0, 1]^2!

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-28.svg``)
   * - **Thematic Part**
     - Part IV: Practical Solvers, 3D Platonic Geometry & Polar Curves
   * - **Classical Curves**
     - :person:`Jakob Bernoulli <bernoulli>` (1694) & :person:`René Descartes <descartes>` (1638)
   * - **GEOMETOR Fundamentals**
     - :ref:`F.22 Functions <f-22>`, :ref:`F.51 Apollonian Circles and the Problem of Apollonius <f-51>`
   * - **Triple Spread Geometry**
     - Geometric locus of Law V (:ref:`W.10 <w-10>`) in spread space ``(s_1, s_2, s_3)``
   * - **Universal Synthesis**
     - Completes the 28-Principle GEOMETOR Wildberger Codex

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.03" [label="W.03\nQuadrance, Midpoints & Point-to...", fillcolor="#d8dee9", color="#4c566a", URL="../w-03/index.html"];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#d8dee9", color="#4c566a", URL="../w-04/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#d8dee9", color="#4c566a", URL="../w-10/index.html"];
       "W.17" [label="W.17\nCircle Geometry: Subtended Spre...", fillcolor="#d8dee9", color="#4c566a", URL="../w-17/index.html"];
       "W.20" [label="W.20\nMetrical Conics: Circles, Ribbo...", fillcolor="#d8dee9", color="#4c566a", URL="../w-20/index.html"];
       "W.28" [label="W.28\nRational Polar Coordinates, Cla...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-28/index.html"];
       "W.03" -> "W.28";
       "W.04" -> "W.28";
       "W.10" -> "W.28";
       "W.17" -> "W.28";
       "W.20" -> "W.28";
   }

**Depends on**: :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`, :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`, :ref:`W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points <w-17>`, :ref:`W.20 Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas <w-20>`

.. toctree::
   :hidden:

   code
