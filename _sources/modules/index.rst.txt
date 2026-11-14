:navigation: header
:order: 40
:nav_title: Modules

=======
Modules
=======

``geometor.wildberger`` is organized into focused symbolic, geometric, and
publishing modules:

- :mod:`geometor.wildberger` — Public package interface exporting metrics,
  invariants, polynomial families, solvers, symbolic provers, and codex builders.
- :mod:`geometor.wildberger.invariants` — Exact symbolic quadratic invariants
  (:class:`~geometor.wildberger.invariants.MetricForm`, ``BLUE_METRIC``,
  ``RED_METRIC``, ``GREEN_METRIC``, :class:`~geometor.wildberger.invariants.LineProportion`,
  :class:`~geometor.wildberger.invariants.ConicProportion`, ``quadrance``,
  ``spread``, ``cross``, ``twist``, ``archimedes``, ``quadrea``, ``spread_polynomial``,
  ``cross_polynomial``, 3D dihedral spreads, projective cross-ratios, and
  ``GF(p)`` modular geometry).
- :mod:`geometor.wildberger.proofs` — 17 multivariate ``SymPy`` theorem provers
  establishing the Five Laws, Quadruple Quad/Spread formulas, Euler's Four-Point
  relation, Ptolemy's cyclic spread/quadrance theorem, Euler line & Nine-Point
  Circle over :math:`\mathbb{F}`, Chromogeometry's Nine-Point Midpoint Theorem,
  Taylor conic tangents & parabolic reflection, and the five rational Platonic
  solid dihedral spreads.
- :mod:`geometor.wildberger.solvers` — Exact algebraic triangle solvers
  (``QQQ``, ``QQS``, ``QSS``, ``SQQ``, ``SSS``) and classical surveying engines
  (inaccessible tower quadrance, Regiomontanus' extremal statue spread,
  Snellius–Pothenot resection, and Hansen's two-station problem).
- :mod:`geometor.wildberger.catalog` — Unified 28-Principle registry
  (:data:`~geometor.wildberger.catalog.PRINCIPLES`, ``W.01``–``W.28``) and
  dependency graph helpers, backed by ``catalog_a`` and ``catalog_b``.
- :mod:`geometor.wildberger.models` — Exact ``geometor.model.Model`` builders
  and live ``SymPy`` verifiers for all 28 principles, backed by ``models_a``
  and ``models_b``.
- :mod:`geometor.wildberger.render` — Interactive Explorer-styled dark-canvas
  SVG renderer with two-way ``:g:`` <-> ``data-ref`` hover highlighting.
- :mod:`geometor.wildberger.apparatus` — Scholarly glossary, historical persons
  index, and bibliography RST generators.
- :mod:`geometor.wildberger.topics` — 2-Track Dossier generator compiling
  ``docsrc/topics/w-NN/{model.py,w-NN.svg,index.rst,code.rst}``.
