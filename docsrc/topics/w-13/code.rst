===============================================================
W.13 Stewart's Theorem, Median Quadrances & The Centroid — Code
===============================================================

.. enunciation::

   For any affine point D = (1 - lambda)*A_1 + lambda*A_2 on side A_1 A_2 of triangle A_1 A_2 A_3, the cevian quadrance satisfies Q(A_3, D) = (1 - lambda)*Q_2 + lambda*Q_1 - lambda*(1 - lambda)*Q_3; at lambda = 1/2, the median quadrance satisfies 4*Q(A_3, M_3) = 2*Q_1 + 2*Q_2 - Q_3, and the three medians concur at G = (A_1 + A_2 + A_3)/3.

.. figure:: w-13.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.13 (Stewart's Theorem, Median Quadrances & The Centroid)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
