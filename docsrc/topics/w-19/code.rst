===================================================================
W.19 Regular Stars, Golden Pentagons & Finite-Field Polygons — Code
===================================================================

.. enunciation::

   A regular n-star of lines has consecutive spread s satisfying S_n(s) = 0; for n = 5, a regular pentagon P_0..P_4 has side-to-diagonal spread alpha = (5 - sqrt(5))/8 = (3 - phi)/4, exterior/star spread beta = (5 + sqrt(5))/8 = (2 + phi)/4, and exact golden quadrance ratio Q_diag / Q_side = beta / alpha = phi^2 = phi + 1, existing rationally in F_p^2 whenever 5 and -1/5-dependent discriminants split (e.g. regular 5-stars in F_19).

.. figure:: w-19.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.19 (Regular Stars, Golden Pentagons & Finite-Field Polygons)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
