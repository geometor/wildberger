==================================================================
W.06 Law I: Pythagoras' Theorem & Right Triangle Invariants — Code
==================================================================

.. enunciation::

   For any three non-collinear points A_1, A_2, A_3 over a field F (char F != 2) with non-null lines A_1 A_3 and A_2 A_3, the lines A_1 A_3 and A_2 A_3 are perpendicular (s_3 = 1) if and only if Q(A_2, A_3) + Q(A_1, A_3) = Q(A_1, A_2), in which case the hypotenuse midpoint M_3 is equidistant in quadrance (Q_3 / 4) from all three vertices.

.. figure:: w-06.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.06 (Law I: Pythagoras' Theorem & Right Triangle Invariants)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
