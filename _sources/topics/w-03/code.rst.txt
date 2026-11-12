===========================================================
W.03 Quadrance, Midpoints & Point-to-Line Separation — Code
===========================================================

.. enunciation::

   The quadrance between A_1 = [x_1, y_1] and A_2 = [x_2, y_2] is the quadratic form Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2; midpoint M divides the quadrance by 4, the locus Q(X, A_1) = Q(X, A_2) is the linear perpendicular bisector, and the quadrance from A_0 to a non-null line l = <a : b : c> is (a*x_0 + b*y_0 + c)^2 / (a^2 + b^2).

.. figure:: w-03.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.03 (Quadrance, Midpoints & Point-to-Line Separation)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
