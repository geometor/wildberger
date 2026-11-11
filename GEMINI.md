# GEOMETOR • wildberger

**Rational Trigonometry, Universal Geometry & Chromogeometry Codex (`W.01`–`W.28`)**

`geometor.wildberger` synthesizes the mathematical principles of Norman J. Wildberger's *Divine Proportions: Rational Trigonometry to Universal Geometry* (2005) and *Chromogeometry* (2008) into exact `SymPy` symbolic algebra, multivariate polynomial proofs, exact surveying solvers, and interactive `geometor.model` SVG constructions.

## Architecture & Key Modules

- `src/geometor/wildberger/invariants.py`: Quadratic invariants (`MetricForm`, `BLUE_METRIC`, `RED_METRIC`, `GREEN_METRIC`, `LineProportion`, `ConicProportion`, `quadrance`, `spread`, `cross`, `twist`, `archimedes`, `quadrea`, `spread_polynomial`, `cross_polynomial`, 3D dihedral spreads, rational polar coordinates `[s, Q]`, projective cross-ratios, and `GF(p)` arithmetic).
- `src/geometor/wildberger/proofs.py`: 18 multivariate `SymPy` theorem provers (`verify_all_proofs()`).
- `src/geometor/wildberger/solvers.py`: Exact algebraic triangle solvers (`QQQ`, `QQS`, `QSS`, `SQQ`, `SSS`) and surveying benchmarks (inaccessible height, Regiomontanus, Snellius–Pothenot, Hansen's problem).
- `src/geometor/wildberger/catalog.py` (`catalog_a.py`, `catalog_b.py`): Complete 28-Principle catalog (`W.01`–`W.28`) across Parts I–IV.
- `src/geometor/wildberger/models.py` (`models_a.py`, `models_b.py`): Exact `geometor.model.Model` builders (zero `sp.Float` approximations).
- `src/geometor/wildberger/render.py`: Explorer-styled interactive SVG renderer (`data-ref` <-> `:g:` hover highlighting).
- `src/geometor/wildberger/topics.py` & `apparatus.py`: Sphinx 2-Track Dossier and scholarly apparatus generators (`docsrc/topics/w-NN/`).

## Strictly Original Symbolic Synthesis

- All formulas and conventions (including rational polar coordinates `[s, Q]` with spread to the $y$-axis, Taylor conic proportions `<d : e : f : a : b : c>`, and Platonic face spreads) are verified in exact `SymPy` algebra.
- No scanned book pages or verbatim copyrighted prose are stored or committed in the repository (`*.pdf` is git-ignored).

## Development Commands

```bash
# Run test suite
/home/phi/PROJECTS/geometor/.venv/bin/pytest

# Lint source, tests, demos, and generated model scripts
ruff check src tests demos docsrc

# Rebuild all 28 codex topics and verify proofs
/home/phi/PROJECTS/geometor/.venv/bin/python demos/build_codex.py

# Build Sphinx documentation
publish build
```
