:order: 20
:type: topic
:category: Metrical Conics & Quadratic Loci
:tags: conic, parabola, quadrola, grammola, ribbon, focus-directrix

.. _w-20:

========================================================================
W.20 Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas
========================================================================

*Quadratic Focus-Directrix and Bifocal Loci Over Arbitrary Fields*

.. enunciation::

   A conic is the zero locus of a quadratic polynomial proportion C = <a:b:c:d:e:f>; metrically, Q(X, l) = R defines a ribbon, Q(X, F_0) = Q(X, l_dir) defines a parabola, the squared-sum/difference bifocal locus A(Q(X, F_1), Q(X, F_2), S) = 0 defines a quadrola (unifying ellipses and hyperbolas into one irreducible algebraic curve), and Q(X, l_1) +/- Q(X, l_2) = R defines a grammola.

.. figure:: w-20.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **W.20 (Metrical Conics: Circles, Ribbons, Parabolas, Quadrolas & Grammolas)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   F_0 : Point
   D_1 : Point
   D_2 : Point
   F_1 : Point
   F_2 : Point
   =====
   l_dir = line(D_1, D_2)
   V_p = midpoint(F_0, foot(F_0, l_dir))
   parabola = parabola_locus(F_0, l_dir)
   C_q = midpoint(F_1, F_2)
   quadrola = quadrola_locus(F_1, F_2, S)

Mathematical Synthesis
----------------------

Classically, an ellipse (:math:`d_1 + d_2 = k`) and a hyperbola (:math:`|d_1 - d_2| = k`) are separated by absolute values and square roots. In Universal Geometry (:cite:`Wildberger2005`), squaring :math:`(\pm\sqrt{Q_1} \pm \sqrt{Q_2} \pm \sqrt{S}) = 0` via :person:`Archimedes <archimedes>`' function produces a **single algebraic curve**—the :term:`quadrola` :g:`quadrola` centered at :g:`C_q` with foci :g:`F_1`, :g:`F_2`—given by :math:`\mathcal{A}(Q(X, F_1), Q(X, F_2), S) = 0`! Over :math:`\mathbb{R}`, the same equation defines an ellipse when :math:`S > Q(F_1, F_2)` and a two-branched hyperbola when :math:`0 < S < Q(F_1, F_2)`, while over :math:`\mathbb{F}_p` both regimes coexist seamlessly without ordering!

Similarly, equating point-to-focus quadrance :math:`Q(X, F_0)` and point-to-directrix quadrance :math:`Q(X, \ell_{\text{dir}})` yields the :term:`parabola` :g:`parabola` with vertex :g:`V_p` and focus :g:`F_0` on non-null directrix :g:`l_dir`, while constant quadrance to a single line yields a :term:`ribbon` (two parallel lines) and constant sum/difference of quadrances to two lines yields a :term:`grammola`.

Key Algebraic Identities
------------------------

.. math::

   \text{Parabola:}\quad Q(X, F_0) = Q(X, \ell_{\text{dir}}) \iff (a^2 + b^2)\big((x - x_0)^2 + (y - y_0)^2\big) = (a x + b y + c)^2

.. math::

   \text{Quadrola:}\quad \mathcal{A}\big(Q(X, F_1),\; Q(X, F_2),\; S\big) = 0, \qquad \text{Grammola:}\quad Q(X, \ell_1) \pm Q(X, \ell_2) = R

Symbolic ``SymPy`` Verification
-------------------------------

.. list-table::
   :widths: 36 36 28
   :header-rows: 1

   * - Invariant / Theorem Check
     - Exact ``SymPy`` Value
     - Verification Status
   * - ``Parabola 6-proportion``
     - ``<100:0:0:0:-400:400>``
     - Exact focus-directrix polynomial
   * - ``Quadrola 6-proportion (S = 100)``
     - ``Center = [10, 2]``
     - Unifies ellipse & hyperbola into 1 polynomial
   * - ``Rational sample check on quadrola``
     - ``q([390/53, -74/53]) = 0``
     - Verified == 0

Cross-Repository Canon
----------------------

.. list-table::
   :widths: 28 72

   * - **Executable Demonstration**
     - :doc:`code` (Standalone ``model.py`` & ``w-20.svg``)
   * - **Thematic Part**
     - Part III: Universal Triangle, Conic & Chromogeometry
   * - **Classical Canon**
     - :person:`Apollonius <apollonius>` (*Conics*, Books I–III)
   * - **GEOMETOR Elements**
     - :ref:`G.3`, :ref:`G.4`
   * - **GEOMETOR Fundamentals**
     - :ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.17 Ellipse <f-17>`, :ref:`F.37 Euler's Inradius Parabola <f-37>`
   * - **Universal Unification**
     - Ellipses and hyperbolas share the single polynomial ``A(Q_1, Q_2, S) = 0``

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "W.03" [label="W.03\nQuadrance, Midpoints & Point-to...", fillcolor="#d8dee9", color="#4c566a", URL="../w-03/index.html"];
       "W.07" [label="W.07\nLaw II: Triple Quad Formula, Ar...", fillcolor="#d8dee9", color="#4c566a", URL="../w-07/index.html"];
       "W.20" [label="W.20\nMetrical Conics: Circles, Ribbo...", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../w-20/index.html"];
       "W.21" [label="W.21\nTaylor Conics, Algebraic Tangen...", fillcolor="#e5e9f0", color="#777777", URL="../w-21/index.html"];
       "W.26" [label="W.26\nAlgebraic Physics: Projectile P...", fillcolor="#e5e9f0", color="#777777", URL="../w-26/index.html"];
       "W.28" [label="W.28\nRational Polar Coordinates, Cla...", fillcolor="#e5e9f0", color="#777777", URL="../w-28/index.html"];
       "W.03" -> "W.20";
       "W.07" -> "W.20";
       "W.20" -> "W.21";
       "W.20" -> "W.26";
       "W.20" -> "W.28";
   }

**Depends on**: :ref:`W.03 Quadrance, Midpoints & Point-to-Line Separation <w-03>`, :ref:`W.07 Law II: Triple Quad Formula, Archimedes' Function & Quadrea <w-07>`

**Required for**: :ref:`W.21 Taylor Conics, Algebraic Tangents & Optical Reflection Laws <w-21>`, :ref:`W.26 Algebraic Physics: Projectile Parabolas, Snell's Law & Relativity <w-26>`, :ref:`W.28 Rational Polar Coordinates, Classical Curves & The Ellipson <w-28>`

.. toctree::
   :hidden:

   code
