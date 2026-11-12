=====================================================================
W.15 Circumcenter, Orthocenter & Universal Affine Barycentrics — Code
=====================================================================

.. enunciation::

   Every non-null triangle A_1 A_2 A_3 over a field F (char F != 2) has a unique circumcenter C at the intersection of its side perpendicular bisectors and a unique orthocenter O at the intersection of its altitudes, with affine barycentric weights beta_i = Q_i*(Q_j + Q_k - Q_i)/(2*A) for C and gamma_i = (Q_i + Q_j - Q_k)*(Q_k + Q_i - Q_j)/(2*A) for O.

.. figure:: w-15.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.15 (Circumcenter, Orthocenter & Universal Affine Barycentrics)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
