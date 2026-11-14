:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Principles & Exact Symbolic Engine

The GEOMETOR edition of :cite:`Norman J. Wildberger's Rational Trigonometry <Wildberger2005>` and Universal Geometry unites 28 executable mathematical principles with interactive parallel tracks, theme-adaptive vector figures, and exact symbolic proofs.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Each of the 28 principles (:math:`\text{W.01}` through :math:`\text{W.28}`) provides synchronized parallel tracks accessible from the principle header bar:
   
   * **Synthesis Track:** Formal mathematical definitions, theorem statements, and synthetic geometric exposition.
   * **Code Track:** Exact, runnable Python implementations utilizing ``geometor.model``, ``geometor.render``, and ``sympy``.

2. Primary-Source Foundations & Executable Formalization
   Every principle directly implements definitions and laws from Norman J. Wildberger's *Divine Proportions* (:cite:`Wildberger2005`) and *Universal Hyperbolic Geometry* (:cite:`Wildberger2008`), formalizing classical theorems into field-independent polynomial identities with zero floating-point error.

3. Interactive Diagrams & Deductive Links
   Throughout the text, geometric entities, assertions, and algebraic expressions link to formal definitions:
   
   * Calibrated SVG figures dynamically adapt between light and dark reading themes.
   * Chromogeometric figures distinguish Blue (Euclidean), Red (relativistic), and Green (hyperbolic) null lines and circles.
   * Links cross-reference companion historical treatises like :cite:`Euclid's Elements <EuclidElements>`.

4. Full-Text Search with In-Page Highlighting
   The sidebar search queries the entire corpus of 28 principles, mathematical proofs, and glossaries. Search query parameters automatically append ``?highlight=`` to highlight matched terms directly inside propositions and remarks.

5. Faceted Navigation & Collection Views
   Browse principles, quadratic invariants, and historical figures via the sidebar index. Collection pages support switching between **Cards**, **Banners**, and **List** layout modes.

6. People, Bibliography & Glossary Tooltips
   Hovering over any mathematician (:person:`Norman J. Wildberger <wildberger>`, :person:`Euclid of Alexandria <euclid>`, :person:`Pythagoras of Samos <pythagoras>`, :person:`Archimedes of Syracuse <archimedes>`), citation (:cite:`Wildberger2005`), or technical term (:term:`quadrance`, :term:`spread`, :term:`cross`, :term:`twist`, :term:`Chromogeometry`) displays an instant context card.

----

Command-Line & Python Verification API
--------------------------------------

In addition to web reading, ``geometor.wildberger`` provides a command-line interface, a programmatic ``SymPy`` invariants and proofs API, exact surveying and triangle solvers, and 28 standalone ``geometor.model`` construction scripts.

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every topic directory (``docsrc/topics/w-NN/``) contains an executable
``model.py`` script that builds its ``geometor.model.Model``, verifies its
symbolic identities with zero ``sp.Float`` approximations, and renders
``w-NN.svg``:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python docsrc/topics/w-23/model.py
