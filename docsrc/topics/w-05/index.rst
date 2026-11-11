:order: 5
:type: topic
:category: Polynomial Families & Golden Proportion
:tags: spread polynomials, Chebyshev, logistic map, golden ratio, pentagon

.. _w-05:

==========================================================
W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads
==========================================================

*Universal Chebyshev Analogues, Semigroup Composition, and Exact Golden Roots*

.. enunciation::

   The integer-coefficient spread polynomials S_0(s) = 0, S_1(s) = s, S_n(s) = 2(1 - 2s)S_{n-1}(s) - S_{n-2}(s) + 2s satisfy the semigroup composition law S_n(S_m(s)) = S_{nm}(s) over every commutative ring, and the fivefold polynomial S_5(s) = s(16s^2 - 20s + 5)^2 vanishes precisely at the Pentagonal Golden Spreads s = (5 -/+ sqrt(5))/8 = (3 - phi)/4 and (2 + phi)/4.

.. figure:: w-05.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.05 (Spread Polynomials S_n(s) & Pentagonal Golden Spreads)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   V_0 : Point
   V_1 : Point
   =====
   l_0 = line(O, V_0)
   l_1 = line(O, V_1)
   l_2 = reflect_line(l_0, l_1)
   l_3 = reflect_line(l_1, l_2)
   l_4 = reflect_line(l_2, l_3)

Mathematical Synthesis
----------------------

Reflecting a line :g:`l_0` successively across :g:`l_1` to form a fan of equally spread lines :math:`\ell_0, \ell_1, \ell_2, \dots` with :math:`s(\ell_k, \ell_{k+1}) = s` produces :math:`s(\ell_0, \ell_n) = S_n(s)`, where :math:`S_n(s) \in \mathbb{Z}[s]` is the :math:`n`-th :term:`spread polynomial` (:cite:`Wildberger2005`). Over :math:`\mathbb{R}`, :math:`S_n(\sin^2\theta) = \sin^2(n\theta)` rescales :person:`Pafnuty Chebyshev <chebyshev>`'s polynomials, while :math:`S_2(s) = 4s(1-s)` is the maximal logistic map and :math:`S_n(S_m(s)) = S_{nm}(s)` forms a commutative polynomial semigroup!

Where Rational Trigonometry meets **GEOMETOR's Divine Proportion** (:math:`\phi = \frac{1+\sqrt{5}}{2}`) is in :math:`S_5(s) = s(16s^2 - 20s + 5)^2 = 0`: its non-zero roots are the two :term:`Pentagonal spread` constants :math:`\alpha = \frac{5 - \sqrt{5}}{8} = \frac{3 - \phi}{4}` and :math:`\beta = \frac{5 + \sqrt{5}}{8} = \frac{2 + \phi}{4}`, whose ratio is :math:`\beta / \alpha = \phi^2 = \phi + 1`! Over :math:`\mathbb{F}_{19}` (where :math:`9^2 \equiv 5`), these roots reduce to exact residues :math:`s \equiv 9, 16 \pmod{19}`.

Key Algebraic Identities
------------------------

.. math::

   S_0(s) = 0, \quad S_1(s) = s, \quad S_2(s) = 4s(1-s), \quad S_3(s) = s(3 - 4s)^2, \quad S_n(S_m(s)) = S_{nm}(s)

.. math::

   S_5(s) = s(16s^2 - 20s + 5)^2 = 0 \iff s \in \left\{0,\; \alpha = \frac{5 - \sqrt{5}}{8} = \frac{3 - \phi}{4},\; \beta = \frac{5 + \sqrt{5}}{8} = \frac{2 + \phi}{4}\right\}

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Reflection fan spreads (s = 1/5)``
     - ``S_2=16/25, S_3=121/125, S_4=576/625``
     - Exact match s(l_0, l_n) == S_n(1/5)
   * - ``Fivefold polynomial S_5(s)``
     - ``s*(16*s**2 - 20*s + 5)**2``
     - s*(16*s^2 - 20*s + 5)^2
   * - ``Golden root alpha = (3 - phi)/4``
     - ``(5 - sqrt(5))/8``
     - S_5(alpha) = 0
   * - ``Golden root beta = (2 + phi)/4``
     - ``(5 + sqrt(5))/8``
     - beta/alpha = phi^2, S_5(beta) = 0
   * - ``Pentagonal orbit in GF(19) at s = 16``
     - ``[0, 16, 9, 9, 16]``
     - Exact period-5 integer cycle

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-05.svg``)
   * - **Thematic Part**
     - Part I: Preliminaries & Foundational Invariants
   * - **Euclid's Elements**
     - :ref:`IV.11`, :ref:`XIII.8` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.12`, :ref:`G.15` (Golden section & pentagonal symmetry)
   * - **GEOMETOR Pacioli**
     - *De Divina Proportione* Cap. VII–XXIII (:cite:`Pacioli1509`)
   * - **Sister Codices**
     - ``geometor/divine`` (golden ratio :math:`\phi` algebraic field ``Q(phi)``)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.02" [label="W.02\nLineations, Central Rotations &...", fillcolor="#d8dee9", color="#4c566a", URL="../w-02/index.html"];
       "W.04" [label="W.04\nSpread, Cross, Twist & Line Sep...", fillcolor="#d8dee9", color="#4c566a", URL="../w-04/index.html"];
       "W.05" [label="W.05\nSpread Polynomials S_n(s) & Pen...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-05/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#e5e9f0", color="#777777", URL="../w-11/index.html"];
       "W.17" [label="W.17\nCircle Geometry: Subtended Spre...", fillcolor="#e5e9f0", color="#777777", URL="../w-17/index.html"];
       "W.19" [label="W.19\nRegular Stars, Golden Pentagons...", fillcolor="#e5e9f0", color="#777777", URL="../w-19/index.html"];
       "W.26" [label="W.26\nAlgebraic Physics: Projectile P...", fillcolor="#e5e9f0", color="#777777", URL="../w-26/index.html"];
       "W.27" [label="W.27\n3D Planes, De Gua's Quadrea Law...", fillcolor="#e5e9f0", color="#777777", URL="../w-27/index.html"];
       "W.02" -> "W.05";
       "W.04" -> "W.05";
       "W.05" -> "W.11";
       "W.05" -> "W.17";
       "W.05" -> "W.19";
       "W.05" -> "W.26";
       "W.05" -> "W.27";
   }

**Depends on**: :ref:`W.02 Lineations, Central Rotations & Reflections in Lines <w-02>`, :ref:`W.04 Spread, Cross, Twist & Line Separation Ratios <w-04>`

**Required for**: :ref:`W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle <w-11>`, :ref:`W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points <w-17>`, :ref:`W.19 Regular Stars, Golden Pentagons & Finite-Field Polygons <w-19>`, :ref:`W.26 Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity <w-26>`, :ref:`W.27 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads <w-27>`

.. toctree::
   :hidden:

   code
