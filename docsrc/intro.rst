==========
Wildberger
==========

**Rational Trigonometry, Universal Geometry & Chromogeometry in Exact SymPy Algebra**

``geometor.wildberger`` synthesizes the algebraic principles of
:person:`Norman J. Wildberger <wildberger>`'s *Divine Proportions: Rational
Trigonometry to Universal Geometry* (:cite:`Wildberger2005`) and
*Chromogeometry* (:cite:`Wildberger2008`) into a **28-Principle Executable
Codex** (:ref:`W.01 <w-01>` through :ref:`W.28 <w-28>`).

Where classical trigonometry introduces square-root distances and transcendental
angles (:math:`\sin, \cos, \arccos`) at the very first step, Rational
Trigonometry grounds geometry in two purely quadratic invariants—:term:`quadrance`
:math:`Q(A_1, A_2)` and :term:`spread` :math:`s(l_1, l_2)`—unlocking exact
polynomial laws over :math:`\mathbb{Q}`, quadratic extensions such as
:math:`\mathbb{Q}(\sqrt{5})`, arbitrary bilinear metrics, and finite fields
:math:`\mathbb{F}_p` (:math:`p \ne 2`).

Architecture of the Codex
-------------------------

Every principle (:ref:`W.01 <w-01>` through :ref:`W.28 <w-28>`) is compiled as a
**2-Track Symbolic Dossier** (zero scanned book reproductions, 100% original
synthesis and executable proofs):

1. **Track 1 — Synthesis** (``index.rst``): Formal ``.. enunciation::``,
   interactive Explorer-styled SVG construction (``w-NN.svg``) with two-way
   hover highlighting on every ``:g:`` label, constructive ``.. signature::``
   block, mathematical synthesis, key algebraic identities, live ``SymPy``
   verification table, Graphviz dependency DAG, and cross-repository canon links
   to ``geometor/euclid``, ``geometor/elements``, ``geometor/fundamentals``,
   ``geometor/etc``, ``geometor/pacioli``, and ``geometor/pappus``.
2. **Track 2 — Code** (``code.rst``): Standalone runnable Python script
   (``model.py``) building the exact ``geometor.model.Model`` with zero
   floating-point approximations and rendering ``w-NN.svg``.

The Four Thematic Parts
-----------------------

.. list-table::
   :widths: 28 18 54
   :header-rows: 1

   * - Part
     - Principles
     - Core Algebraic Laws & Discoveries
   * - **I. Foundations & Universal Affine Geometry**
     - :ref:`W.01 <w-01>` – :ref:`W.05 <w-05>`
     - Arbitrary fields :math:`\mathbb{F}` (:math:`\operatorname{char}\mathbb{F}\ne 2`), :term:`line proportion` :math:`\langle a : b : c \rangle`, :term:`quadrance`, :term:`null line` isotropy, :term:`spread`, :term:`cross`, :term:`twist`, altitudes, rational reflections :math:`\Sigma_l(m)`, and projective :term:`cross-ratio` bridges.
   * - **II. The Five Laws & Polynomial Trigonometry**
     - :ref:`W.06 <w-06>` – :ref:`W.12 <w-12>`
     - **Pythagoras' Law** (:math:`Q_1 + Q_2 = Q_3`), **Triple Quad Formula** & :term:`Archimedes' function` / :term:`quadrea` :math:`\mathcal{A}`, **Spread Law**, **Cross Law**, **Triple Spread Formula**, :term:`spread polynomial` Chebyshev/logistic hierarchy :math:`S_n(s)`, and **Quadruple Quad / Spread** formulas.
   * - **III. Triangle Centers, Polygons, Circles & Conics**
     - :ref:`W.13 <w-13>` – :ref:`W.21 <w-21>`
     - Isosceles/Equilateral/Barycentric laws, Stewart/Menelaus/Ceva, circumcenter/orthocenter/incenter, Euler line & **Nine-Point Circle over** :math:`\mathbb{F}_p`, cyclic quadrilaterals & quadratic **Ptolemy's Theorem**, **Kepler's Golden Triangle** & :math:`\mathbb{F}_{19}` pentagrams, **Quadrolas & Grammolas**, and calculus-free **Taylor Conic** tangents.
   * - **IV. Chromogeometry, Surveying, Physics & 3D Space**
     - :ref:`W.22 <w-22>` – :ref:`W.28 <w-28>`
     - Finite-field spreads in :math:`\mathbb{F}_p`, **Blue/Red/Green Chromogeometry** (:math:`N_B = \tfrac{1}{2}(C_R + C_G)`), exact triangle/Regiomontanus/Snellius–Pothenot/**Hansen** solvers, projectile parabolas & Snell's Spread Law, **rational Platonic dihedral spreads** (:math:`8/9, 1, 8/9, 4/9, 4/5`), rational polar curves :math:`[s, Q]`, and the cubic **Ellipson**.
