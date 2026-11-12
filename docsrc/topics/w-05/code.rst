=================================================================
W.05 Spread Polynomials S_n(s) & Pentagonal Golden Spreads — Code
=================================================================

.. enunciation::

   The integer-coefficient spread polynomials S_0(s) = 0, S_1(s) = s, S_n(s) = 2(1 - 2s)S_{n-1}(s) - S_{n-2}(s) + 2s satisfy the semigroup composition law S_n(S_m(s)) = S_{nm}(s) over every commutative ring, and the fivefold polynomial S_5(s) = s(16s^2 - 20s + 5)^2 vanishes precisely at the Pentagonal Golden Spreads s = (5 -/+ sqrt(5))/8 = (3 - phi)/4 and (2 + phi)/4.

.. figure:: w-05.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.05 (Spread Polynomials S_n(s) & Pentagonal Golden Spreads)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
