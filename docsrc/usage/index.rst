:navigation: header
:order: 20

=====
Usage
=====

``geometor.wildberger`` provides a Rich command-line interface, a programmatic
``SymPy`` invariants and proofs API, exact surveying and triangle solvers, and
28 standalone ``geometor.model`` construction scripts.

Command-Line Interface
----------------------

.. code-block:: bash

   # Display summary table of all 28 principles (W.01..W.28)
   uv run --offline wildberger summary

   # Run all 18 multivariate SymPy symbolic theorem provers
   uv run --offline wildberger verify

   # Regenerate all 28 codex dossiers, SVGs, model.py scripts, and apparatus
   uv run --offline wildberger build

   # Build the Sphinx HTML documentation
   publish build

Python API Quickstart
---------------------

.. code-block:: python

   import sympy as sp
   from geometor.wildberger import (
       BLUE_METRIC,
       RED_METRIC,
       GREEN_METRIC,
       compute_triangle_invariants,
       quadrance,
       spread_polynomial,
       solve_hansen_benchmark,
       verify_all_proofs,
   )

   # 1. Verify all 18 Universal Geometry & Chromogeometry SymPy proofs
   certificates = verify_all_proofs()
   assert all(c.verified for c in certificates)

   # 2. Chromogeometry Nine-Point Midpoint Theorem: N_B == (C_R + C_G) / 2
   a1, a2, a3 = (0, 0), (8, 2), (2, 6)
   inv_b = compute_triangle_invariants(a1, a2, a3, metric=BLUE_METRIC)
   inv_r = compute_triangle_invariants(a1, a2, a3, metric=RED_METRIC)
   inv_g = compute_triangle_invariants(a1, a2, a3, metric=GREEN_METRIC)
   assert inv_b.q3**2 == inv_r.q3**2 + inv_g.q3**2  # 68^2 == 60^2 + 32^2

   # 3. Exact pentagonal spread polynomial S_5(s) = s*(16*s^2 - 20*s + 5)^2
   s = sp.Symbol("s")
   assert sp.factor(spread_polynomial(5, s)) == s * (16 * s**2 - 20 * s + 5) ** 2

   # 4. Solve Hansen's two-station surveying problem with zero rounding error
   hansen = solve_hansen_benchmark()
   assert (hansen["Q_AD"], hansen["Q_BC"], hansen["Q_AC"], hansen["Q_BD"]) == (17, 17, 41, 25)

Running Standalone Topic Scripts
--------------------------------

Every topic directory (``docsrc/topics/w-NN/``) contains an executable
``model.py`` script that builds its ``geometor.model.Model``, verifies its
symbolic identities with zero ``sp.Float`` approximations, and renders
``w-NN.svg``:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python docsrc/topics/w-23/model.py
