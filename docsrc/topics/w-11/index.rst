:order: 11
:type: topic
:category: Special & Golden Triangles
:tags: isosceles, equilateral, Kepler triangle, golden ratio, Pons Asinorum

.. _w-11:

============================================================
W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle
============================================================

*Pons Asinorum, the 3/4 Equilateral Spread, and Pure Golden Powers Q = (1, phi, phi^2)*

.. enunciation::

   In a non-null triangle, Q_1 = Q_2 iff s_1 = s_2 (with apex spread s_3 = (Q_3/Q_1)(1 - Q_3/(4*Q_1))), and Q_1 = Q_2 = Q_3 iff s_1 = s_2 = s_3 = 3/4; in Kepler's Golden Right Triangle with side lengths (1, sqrt(phi), phi), the nested radical vanishes in quadrance to give Q = (1, phi, phi^2) and exact golden spreads (s_1, s_2, s_3) = (2 - phi, phi - 1, 1) = (1/phi^2, 1/phi, 1).

.. figure:: w-11.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.11 (Isosceles, Equilateral & Kepler's Golden Right Triangle)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t_kepler = polygon(A_1, A_2, A_3)
   F_1 = foot(A_1, line(A_2, A_3))
   alt = segment(A_1, F_1)

Mathematical Synthesis
----------------------

In Universal Geometry, *Pons Asinorum* (:ref:`I.5`) holds for every non-null triangle over any field (:cite:`Wildberger2005`): :math:`Q_1 = Q_2 \iff s_1 = s_2`. Equilateral triangles satisfy :math:`Q_1 = Q_2 = Q_3 \iff s_1 = s_2 = s_3 = 3/4`, which immediately proves that no equilateral triangle can have rational coordinates in :math:`\mathbb{Q}^2` because :math:`\mathcal{A} = 3 Q^2` requires :math:`3` to be a square in :math:`F` (as it is in :math:`\mathbb{F}_{11}`, where :math:`5^2 \equiv 3`)!

Even more striking is :person:`Johannes Kepler <kepler>`'s **Golden Right Triangle** (:g:`t_kepler`), canonical in ``geometor/etc`` and ``geometor/divine``. Classically burdened with the nested radical :math:`\sqrt{\phi}`, its quadrances are pure geometric powers of the :term:`golden ratio` :math:`(Q_3, Q_2, Q_1) = (1, \phi, \phi^2)` satisfying :math:`1 + \phi = \phi^2`, while its spreads are :math:`(1/\phi^2, 1/\phi, 1) = (2 - \phi, \phi - 1, 1)` with altitude foot :g:`F_1` dividing the hypotenuse in the **exact golden section** :math:`\phi : 1`!

Key Algebraic Identities
------------------------

.. math::

   Q_1 = Q_2 \implies s_3 = \frac{Q_3}{Q_1}\left(1 - \frac{Q_3}{4 Q_1}\right), \qquad Q_1 = Q_2 = Q_3 \iff s_1 = s_2 = s_3 = \frac{3}{4}

.. math::

   \text{Kepler Triangle:}\quad (Q_3, Q_2, Q_1) = (1, \phi, \phi^2), \qquad (s_3, s_2, s_1) = \left(\frac{1}{\phi^2}, \frac{1}{\phi}, 1\right) = (2 - \phi,\; \phi - 1,\; 1)

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Kepler quadrances (Q_3, Q_2, Q_1)``
     - ``(1, phi, phi^2)``
     - 1 + phi = phi^2 (nested sqrt(phi) vanishes!)
   * - ``Kepler spreads (s_3, s_2, s_1)``
     - ``(3/2 - sqrt(5)/2, -1/2 + sqrt(5)/2, 1)``
     - Exact golden powers (1/phi^2, 1/phi, 1)
   * - ``Golden section at foot F_1``
     - ``Q(F_1,A_3) / Q(A_2,F_1) = phi^2``
     - Lengths 1 and 1/phi on hypotenuse
   * - ``Equilateral spread law s_1=s_2=s_3=3/4``
     - ``S(3/4, 3/4, 3/4) = 0``
     - Verified over Z[1/2] & GF(11)

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-11.svg``)
   * - **Thematic Part**
     - Part II: The Five Fundamental Laws
   * - **Euclid's Elements**
     - :ref:`I.1`, :ref:`I.5`, :ref:`II.11`, :ref:`VI.30` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements**
     - :ref:`G.2`, :ref:`G.12`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.18 Equilateral Triangle <f-18>`, :ref:`F.23 Golden Triangles <f-23>`, :ref:`F.30 Isosceles Triangles <f-30>`
   * - **GEOMETOR ETC & Divine**
     - Canonical Kepler triangle ``(1, sqrt(phi), phi)`` in ``geometor/etc`` & ``geometor/divine``

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.05" [label="W.05\nSpread Polynomials S_n(s) & Pen...", fillcolor="#d8dee9", color="#4c566a", URL="../w-05/index.html"];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#d8dee9", color="#4c566a", URL="../w-06/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#d8dee9", color="#4c566a", URL="../w-09/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#d8dee9", color="#4c566a", URL="../w-10/index.html"];
       "W.11" [label="W.11\nIsosceles, Equilateral & Kepler...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-11/index.html"];
       "W.19" [label="W.19\nRegular Stars, Golden Pentagons...", fillcolor="#e5e9f0", color="#777777", URL="../w-19/index.html"];
       "W.27" [label="W.27\n3D Planes, De Gua's Quadrea Law...", fillcolor="#e5e9f0", color="#777777", URL="../w-27/index.html"];
       "W.05" -> "W.11";
       "W.06" -> "W.11";
       "W.08" -> "W.11";
       "W.09" -> "W.11";
       "W.10" -> "W.11";
       "W.11" -> "W.19";
       "W.11" -> "W.27";
   }

**Depends on**: :ref:`W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads <w-05>`, :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`, :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`

**Required for**: :ref:`W.19 Regular Stars, Golden Pentagons & Finite-Field Polygons <w-19>`, :ref:`W.27 3D Planes, De Gua's Quadrea Law & Platonic Dihedral Spreads <w-27>`

.. toctree::
   :hidden:

   code
