:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-wildberger:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

The GEOMETOR edition of :person:`Norman J. Wildberger <wildberger>` establishes a comprehensive digital critical codex synthesizing the revolutionary algebraic framework of *Divine Proportions: Rational Trigonometry to Universal Geometry* (:cite:`Wildberger2005`) and *Chromogeometry* (:cite:`Wildberger2008`). Classical geometry and trigonometry have long rested upon transcendental functions ($\sin$, $\cos$), square roots, and real-number completeness—introducing analytical approximations at the very first step of metrical measurement. Wildberger's Rational Trigonometry radically reconstructs metrical geometry upon two purely algebraic quadratic invariants: :term:`quadrance` $Q(A_1, A_2)$ and :term:`spread` $s(l_1, l_2)$. By replacing transcendental angle and radical distance with polynomial relations, geometry becomes fully exact and universally valid over any field of characteristic $\ne 2$, including rational numbers $\mathbb{Q}$, quadratic number fields ($\mathbb{Q}(\sqrt{5})$, $\mathbb{Q}(\phi)$), and finite Galois fields $\mathbb{F}_p$.

This edition compiles Wildberger's discoveries into an addressable **28-Principle Executable Codex** (:ref:`W.01 <w-01>` through :ref:`W.28 <w-28>`), structured into four thematic parts: Foundations & Universal Affine Geometry, The Five Laws & Polynomial Trigonometry, Triangle Centers & Conics, and Chromogeometry & 3D Space. Every principle is presented as a synchronized two-track dossier: a formal mathematical synthesis (with ``.. enunciation::``, constructive ``.. signature::``, live ``SymPy`` algebraic verification tables, dependency DAGs, and interactive Explorer-styled SVGs) paired with standalone runnable Python models (``model.py``) creating verified vector geometry with zero floating-point error.

Within the GEOMETOR ecosystem, ``geometor.wildberger`` supplies the essential algebraic bridge linking classical synthetic geometry to modern symbolic computing: connecting the classical proofs of :doc:`geometor/elements <elements:index>` and :doc:`geometor/euclid <euclid:index>`, the projective pole-polar harmonies and cross-ratios of :doc:`geometor/pappus <pappus:index>`, the dynamic symmetry and root-rectangle quadrances of :doc:`geometor/thompson <thompson:index>`, and the golden section structures of :doc:`geometor/divine <divine:index>` to the foundational polynomial engine of ``geometor.model``.

The GEOMETOR Mission
--------------------

GEOMETOR is an ongoing research initiative founded by **phi ARCHITECT** dedicated to recovering, formalizing, and revitalizing the world's mathematical and geometric heritage through three foundational pillars:

1. **Extracting Historical Semantic Knowledge**:
   Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises—elevating prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

2. **Exact Symbolic Grounding (``geometor.model``)**:
   Anchoring geometric constructions in 100% exact symbolic algebra (`SymPy <https://www.sympy.org/>`_) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic fields rather than floating-point approximations. In ``geometor.wildberger``, every law is verified through multivariate polynomial certificates holding identically across arbitrary fields.

3. **Repurposing Knowledge Across Mediums**:
   Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (`photon-platform/publish <https://github.com/phiarchitect/publish>`_), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This edition represents a 100% original synthesis and executable re-derivation of Norman J. Wildberger's published monographs and papers, containing zero scanned book reproductions:

* **Wildberger, Norman J. (2005):** *Divine Proportions: Rational Trigonometry to Universal Geometry*. Sydney: Wild Egg Books.
* **Wildberger, Norman J. (2007):** "A Rational Approach to Trigonometry." *Math Horizons* 15, no. 2: 16–20.
* **Wildberger, Norman J. (2008–2009):** "Chromogeometry." *The Mathematical Intelligencer* / UNSW Preprint.
* **Wildberger, Norman J. (2009):** "Affine and Projective Universal Geometry." *Journal of Geometry*.

Every principle and theorem is formally verified using multivariate polynomial algebra in ``SymPy``, confirming that all five core laws (Pythagoras' Law, the Triple Quad Formula, the Spread Law, the Cross Law, and the Triple Spread Formula), Taylor conics, and Chromogeometric relations are algebraically exact.

For further exploration of this codex and its apparatus:

* :doc:`The 28-Principle Codex Directory <../topics/index>`
* :doc:`Reader's Guide & Usage Instructions <../usage/index>`
* :ref:`Systematic Bibliography <bibliography>`
* :ref:`People & Historical Figures <persons>`
* :ref:`Glossary of Rational Trigonometry <glossary>`
