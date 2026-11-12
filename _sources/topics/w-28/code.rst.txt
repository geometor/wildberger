=======================================================================
W.28 Rational Polar Coordinates, Classical Curves & The Ellipson — Code
=======================================================================

.. enunciation::

   Replacing polar coordinates (r, theta) with rational polar coordinates [s, Q] where s = x^2 / (x^2 + y^2) (spread to the y-axis) and Q = x^2 + y^2 converts classical polar curves into exact polynomial relations—Bernoulli's lemniscate s = (Q + 2)/4 (or Q = a*(2*s - 1)), Descartes' folium (2*s - 1)^2*(s^2 - s + 1)^2*Q^2 - 18*s*(1 - s)*(1 - 3*s + 3*s^2)*Q + 81*s^2*(1 - s)^2 = 0, and the deltoid/ellipson S_3(s) law—while (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 cuts out the tetrahedral Ellipson.

.. figure:: w-28.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.28 (Rational Polar Coordinates, Classical Curves & The Ellipson)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
