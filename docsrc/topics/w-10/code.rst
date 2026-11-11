==========================================================================
W.10 Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas — Code
==========================================================================

.. enunciation::

   For any three coplanar non-null lines l_1, l_2, l_3 with pairwise spreads s_1, s_2, s_3 and crosses c_i = 1 - s_i, the spreads satisfy the cubic Triple Spread Formula (s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4*s_1*s_2*s_3 and the crosses satisfy (c_1 + c_2 + c_3 - 1)^2 = 4*c_1*c_2*c_3; for four lines, the Quadruple Spread polynomial R(s_12, s_23, s_34, s_14) = 0 is identically invariant under s_ij <-> 1 - s_ij.

.. figure:: w-10.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.10 (Law V: Triple Spread, Triple Cross & Quadruple Spread Formulas)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
