===================================================================
W.11 Isosceles, Equilateral & Kepler's Golden Right Triangle — Code
===================================================================

.. enunciation::

   In a non-null triangle, Q_1 = Q_2 iff s_1 = s_2 (with apex spread s_3 = (Q_3/Q_1)(1 - Q_3/(4*Q_1))), and Q_1 = Q_2 = Q_3 iff s_1 = s_2 = s_3 = 3/4; in Kepler's Golden Right Triangle with side lengths (1, sqrt(phi), phi), the nested radical vanishes in quadrance to give Q = (1, phi, phi^2) and exact golden spreads (s_1, s_2, s_3) = (2 - phi, phi - 1, 1) = (1/phi^2, 1/phi, 1).

.. figure:: w-11.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.11 (Isosceles, Equilateral & Kepler's Golden Right Triangle)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
