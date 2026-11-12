=================================================================================
W.17 Circle Geometry: Subtended Spreads, Secant Products & Rational Points — Code
=================================================================================

.. enunciation::

   On a circle Q(X, O_c) = K over F, a diameter subtends spread 1 at every other circle point (Thales), any chord P_1 P_2 subtends constant spread s_3 at the circumference with Q(P_1, P_2) = 4*K*s_3 and central spread s(O_c P_1, O_c P_2) = S_2(s_3) = 4*s_3*(1 - s_3), and any external or internal point A_0 has invariant secant quadrance product Q(A_0, P_1)*Q(A_0, P_2) = (Q(A_0, O_c) - K)^2.

.. figure:: w-17.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.17 (Circle Geometry: Subtended Spreads, Secant Products & Rational Points)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
