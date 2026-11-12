:order: 23
:type: topic
:category: Universal Bilinear Forms & Chromogeometry
:tags: Chromogeometry, blue metric, red metric, green metric, Minkowski, Euler line

.. _w-23:

========================================================
W.23 Chromogeometry & Universal Symmetric Bilinear Forms
========================================================

*Harmonizing Blue Euclidean, Red Lorentzian, and Green Hyperbolic Triangle Centers*

.. enunciation::

   Replacing the Euclidean quadratic form with any non-degenerate symmetric bilinear form M on F^2 preserves all Five Laws of Rational Trigonometry; in Chromogeometry—pairing Blue (dx^2 + dy^2), Red (dx^2 - dy^2), and Green (2*dx*dy) metrics on the same triangle—the three Euler lines concur at the centroid G, C_B C_R O_B C_G is a parallelogram, and N_B = (C_R + C_G)/2.

.. figure:: w-23.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.23 (Chromogeometry & Universal Symmetric Bilinear Forms)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A_1 : Point
   A_2 : Point
   A_3 : Point
   =====
   t = polygon(A_1, A_2, A_3)
   G = centroid(A_1, A_2, A_3)
   C_B, O_B, N_B = centers_blue(A_1, A_2, A_3)
   C_R, O_R = centers_red(A_1, A_2, A_3)
   C_G, O_G = centers_green(A_1, A_2, A_3)
   e_B = line(C_B, O_B)
   e_R = line(C_R, O_R)
   e_G = line(C_G, O_G)
   p_chromo = polygon(C_B, C_R, O_B, C_G)

Mathematical Synthesis
----------------------

Because Rational Trigonometry uses only polynomial identities, **every theorem in Parts I–III generalizes to any symmetric bilinear form** :math:`u \cdot_M v = u^T M v` (:math:`\det M \neq 0`) with :math:`s_M(\ell_1, \ell_2)` scaled by :math:`\det M` (:cite:`Wildberger2005`, :cite:`Wildberger2008`)! In :person:`Norman J. Wildberger <wildberger>`'s :term:`Chromogeometry`, three canonical quadratic forms act simultaneously on the **same** planar triangle :g:`t`: **Blue** Euclidean :math:`Q_B = \Delta x^2 + \Delta y^2`, **Red** Lorentz/Minkowski :math:`Q_R = \Delta x^2 - \Delta y^2`, and **Green** rotated Lorentz :math:`Q_G = 2 \Delta x \Delta y`, satisfying **Pythagoras' Identity in Metrical Space** :math:`Q_B^2 = Q_R^2 + Q_G^2`!

Computing the circumcenters (:g:`C_B`, :g:`C_R`, :g:`C_G`), orthocenters (:g:`O_B`, :g:`O_R`, :g:`O_G`), and Euler lines (:g:`e_B`, :g:`e_R`, :g:`e_G`) uncovers miraculous cross-metric harmonies: all three colored Euler lines concur at the metric-free :term:`centroid` :g:`G`; the quadrilateral :g:`p_chromo` (:math:`C_B C_R O_B C_G`) is **always a parallelogram** (:math:`C_B + O_B = C_R + C_G`); and the Blue nine-point center :g:`N_B` is the exact midpoint of the Red and Green circumcenters!

Key Algebraic Identities
------------------------

.. math::

   Q_B = \Delta x^2 + \Delta y^2, \quad Q_R = \Delta x^2 - \Delta y^2, \quad Q_G = 2 \Delta x \Delta y \implies Q_B^2 = Q_R^2 + Q_G^2

.. math::

   C_B + O_B = C_R + C_G, \qquad N_B = \frac{C_R + C_G}{2}, \qquad N_R = \frac{C_B + C_G}{2}, \qquad N_G = \frac{C_B + C_R}{2}

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Pythagoras in Metrical Space Q_B^2 == Q_R^2 + Q_G^2``
     - ``68^2 == 60^2 + 32^2``
     - 68^2 = 60^2 + 32^2 = 4624
   * - ``Nine-Point Midpoint N_B == (C_R + C_G)/2``
     - ``[69/22, 65/22] == [69/22, 65/22]``
     - Chromo-Nine-Point Theorem verified
   * - ``Parallelogram C_B + O_B == C_R + C_G``
     - ``2 * N_B = [69/11, 65/11]``
     - C_B C_R O_B C_G is a parallelogram
   * - ``Concurrency of Blue, Red, Green Euler lines``
     - ``G = [10/3, 8/3]``
     - All 3 Euler lines pass through X(2)

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-23.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Relativistic Canon**
     - :person:`Hermann Minkowski <minkowski>` (1908 spacetime metric ``dx^2 - dt^2``)
   * - **Chromogeometry**
     - :cite:`Wildberger2008` (*Chromogeometry*, 12+ colored triangle center theorems)
   * - **GEOMETOR Fundamentals**
     - :ref:`F.6 Centroid <f-06>`, :ref:`F.34 Nine-Point Circle <f-34>`
   * - **Universal Invariance**
     - All Five Laws hold verbatim for Blue, Red, Green, and arbitrary ``M = M^T``

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.06" [label="W.06\nLaw I: Pythagoras' Theorem & Ri...", fillcolor="#d8dee9", color="#4c566a", URL="../w-06/index.html"];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#d8dee9", color="#4c566a", URL="../w-07/index.html"];
       "W.08" [label="W.08\nLaw III: The Spread Law & Exten...", fillcolor="#d8dee9", color="#4c566a", URL="../w-08/index.html"];
       "W.09" [label="W.09\nLaw IV: The Cross Law & Quadrea...", fillcolor="#d8dee9", color="#4c566a", URL="../w-09/index.html"];
       "W.10" [label="W.10\nLaw V: Triple Spread, Triple Cr...", fillcolor="#d8dee9", color="#4c566a", URL="../w-10/index.html"];
       "W.16" [label="W.16\nThe Euler Line & Nine-Point Cir...", fillcolor="#d8dee9", color="#4c566a", URL="../w-16/index.html"];
       "W.23" [label="W.23\nChromogeometry & Universal Symm...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-23/index.html"];
       "W.26" [label="W.26\nAlgebraic Physics: Projectile P...", fillcolor="#e5e9f0", color="#777777", URL="../w-26/index.html"];
       "W.06" -> "W.23";
       "W.07" -> "W.23";
       "W.08" -> "W.23";
       "W.09" -> "W.23";
       "W.10" -> "W.23";
       "W.16" -> "W.23";
       "W.23" -> "W.26";
   }

**Depends on**: :ref:`W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants <w-06>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`, :ref:`W.08 Law III: The Spread Law & Extended Circumquadrance Law <w-08>`, :ref:`W.09 Law IV: The Cross Law & Quadrea-Spread Identity <w-09>`, :ref:`W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas <w-10>`, :ref:`W.16 The Euler Line & Nine-Point Circle Over Arbitrary Fields <w-16>`

**Required for**: :ref:`W.26 Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity <w-26>`

.. toctree::
   :hidden:

   code
