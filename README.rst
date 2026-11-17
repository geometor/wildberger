GEOMETOR • wildberger
=====================

**Visit the Online Archive:** https://geometor.github.io/wildberger/

.. image:: docsrc/topics/w-01/w-01.svg
   :alt: GEOMETOR • wildberger featured geometric construction
   :target: https://geometor.github.io/wildberger/
   :align: center

**Norman J. Wildberger • Divine Proportions & Rational Trigonometry • semantic digital archive**

Mission
-------

``geometor/wildberger`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It provides a 100% exact symbolic synthesis of Norman J. Wildberger's Rational Trigonometry, Universal Geometry, and Chromogeometry—formulating geometry over arbitrary fields using quadrance and spread without transcendental approximations. By translating foundational treatises and lecture series into executable algebraic certificates, interactive vector diagrams, and verified multivariate theorems, the repository establishes a computable rational foundation across the GEOMETOR corpus.

Catalogs in This Archive
------------------------

- `Principles of Rational Trigonometry & Universal Geometry <https://geometor.github.io/wildberger/topics/>`_ — 28 executable geometric principles (``W.01``–``W.28``) proved in exact SymPy algebra with interactive dark-canvas vector figures.

Python Package & Modules
------------------------

The ``geometor-wildberger`` Python package (``import geometor.wildberger``) provides the executable symbolic geometry, construction, and compilation modules powering this archive:

- ``apparatus.py`` — Scholarly apparatus generator (``glossary.rst``, ``persons.rst``, ``bibliography.rst``).
- ``catalog.py`` — Master catalog of the 28 Rational Trigonometry & Universal Geometry Principles.
- ``catalog_a.py`` — Catalog definitions for Principles ``W.01`` through ``W.14`` (Parts I, II & early III).
- ``catalog_b.py`` — Catalog definitions for Principles ``W.15`` through ``W.28`` (Parts III & IV).
- ``invariants.py`` — Exact algebraic invariants for Rational Trigonometry and Universal Geometry.
- ``models.py`` — Exact ``geometor.model.Model`` builders and SymPy verifiers for ``W.01``..``W.28``.
- ``models_a.py`` — Exact ``geometor.model.Model`` builders and SymPy verifiers for ``W.01``..``W.14``.
- ``models_b.py`` — Exact ``geometor.model.Model`` builders and SymPy verifiers for ``W.15``..``W.28``.
- ``proofs.py`` — Symbolic SymPy theorem provers for Rational Trigonometry and Universal Geometry.
- ``render.py`` — Explorer-styled interactive SVG renderer for GEOMETOR Wildberger.
- *Plus 2 additional modules under* ``src/geometor/wildberger/``.

See the `API Reference <https://geometor.github.io/wildberger/modules/>`_ for full module documentation.

Repository Contents
-------------------

- ``docsrc/`` — RST tracks and catalog pages compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``src/geometor/wildberger/`` — Symbolic core modules, theorem provers, invariant calculators, and CLI tools.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
