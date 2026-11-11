==========================================================
W.14 Menelaus, Ceva & The Alternate Spreads Theorem — Code
==========================================================

.. enunciation::

   If either a transversal line l cuts the sidelines A_2 A_3, A_3 A_1, A_1 A_2 of a non-null triangle at B_1, B_2, B_3 (Menelaus) or three cevians through a point A_0 meet the opposite sidelines at B_1, B_2, B_3 (Ceva), then the six segment quadrances satisfy Q(A_2, B_1) * Q(A_3, B_2) * Q(A_1, B_3) = Q(B_1, A_3) * Q(B_2, A_1) * Q(B_3, A_2).

.. figure:: w-14.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.14 (Menelaus, Ceva & The Alternate Spreads Theorem)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
