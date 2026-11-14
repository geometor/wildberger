=========
changelog
=========

0.1.1 (2026-11-14)
------------------

* Standardized Book Title Page with publication metadata, reading instructions, and structured navigation.
* Added top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``) and dedicated Reader's Guide (``docsrc/usage/``).
* Enhanced ``People`` directory with featured Author and Translator biographical profiles.
* Standardized structural section headings and terminology in English across codex indices.

0.1.0 (2026-11-11)
------------------

- Initial release of ``geometor.wildberger``: **Rational Trigonometry, Universal
  Geometry & Chromogeometry Principles + SymPy Demonstration Codex**
  (``W.01``–``W.28``).
- Implemented exact symbolic invariants in ``geometor.wildberger.invariants``
  (``MetricForm``, ``BLUE_METRIC``, ``RED_METRIC``, ``GREEN_METRIC``,
  ``LineProportion``, ``ConicProportion``, ``quadrance``, ``spread``, ``cross``,
  ``twist``, ``signed_turn``, ``archimedes``, ``quadrea``, Triple/Quadruple
  Quad & Spread functions, Euler's four-point function, ``spread_polynomial``,
  ``cross_polynomial``, 3D dihedral spreads, rational polar coordinates
  ``[s, Q]``, projective cross-ratios, and ``GF(p)`` arithmetic).
- Implemented 18 multivariate ``SymPy`` theorem provers in
  ``geometor.wildberger.proofs`` and exact triangle/surveying solvers in
  ``geometor.wildberger.solvers`` (``QQQ``, ``QQS``, ``QSS``, ``SQQ``, ``SSS``,
  inaccessible height, Regiomontanus, Snellius–Pothenot, and Hansen's problem).
- Generated 28 2-Track Symbolic Dossiers (``docsrc/topics/w-01``..``w-28``) with
  standalone ``geometor.model`` construction scripts, interactive Explorer-styled
  SVGs, and cross-repository GEOMETOR Sphinx links.
