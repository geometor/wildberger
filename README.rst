==========
wildberger
==========

**Rational Trigonometry, Universal Geometry & Chromogeometry in Exact SymPy Algebra**

``geometor.wildberger`` is an executable codex of **28 Geometric & Algebraic
Principles** (``W.01``–``W.28``) synthesized from Norman J. Wildberger's
*Divine Proportions: Rational Trigonometry to Universal Geometry* (2005) and
*Chromogeometry* (2008), demonstrated in 100% exact ``SymPy`` symbolic algebra
and ``geometor.model`` constructions.

Overview
--------

Classical trigonometry relies on square-root distances and transcendental
circular functions (``sin``, ``cos``, ``arccos``), introducing irrational and
floating-point approximations immediately. **Rational Trigonometry** replaces
distance and angle with two purely quadratic invariants valid over any field
:math:`\mathbb{F}` with :math:`\operatorname{char}(\mathbb{F}) \ne 2`:

- **Quadrance** :math:`Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2`
- **Spread** :math:`s(l_1, l_2) = \dfrac{(a_1 b_2 - a_2 b_1)^2}{(a_1^2 + b_1^2)(a_2^2 + b_2^2)}`

Key Capabilities
----------------

- **28-Principle Executable Codex** (``W.01``–``W.28``): Covers universal affine
  geometry, the Five Main Laws, Spread & Cross polynomials, triangle centers,
  cyclic quadrilaterals & quadratic Ptolemy, Kepler's Golden Triangle & regular
  pentagrams in :math:`\mathbb{F}_{19}`, Quadrolas & Grammolas, calculus-free
  Taylor conic tangents, Blue/Red/Green Chromogeometry, Snellius–Pothenot &
  Hansen surveying solvers, algebraic ballistics & Snell's Spread Law, the five
  rational Platonic dihedral spreads (:math:`8/9, 1, 8/9, 4/9, 4/5`), rational
  polar coordinates :math:`[s, Q]`, and the cubic **Ellipson** surface.
- **18 Multivariate SymPy Proofs**: Every core law is proved symbolically over
  polynomial rings with zero floating-point approximations.
- **Interactive Explorer SVGs**: Every topic generates an interactive dark-canvas
  SVG construction (``w-NN.svg``) with two-way hover highlighting wired to
  ``:g:`` geometry roles in the Sphinx documentation.

Quickstart
----------

.. code-block:: bash

   # Summarize all 28 principles
   /home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.wildberger summary

   # Verify all 18 symbolic SymPy theorem certificates
   /home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.wildberger verify

   # Rebuild all 28 codex dossiers, standalone model.py scripts, and SVGs
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/build_codex.py

   # Run the showcase demonstration script
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/showcase_rational_trigonometry.py

   # Build Sphinx HTML documentation into docs/
   publish build

License
-------

MIT License — Copyright (c) GEOMETOR.
