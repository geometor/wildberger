====================================================================
W.16 The Euler Line & Nine-Point Circle Over Arbitrary Fields — Code
====================================================================

.. enunciation::

   In any non-null triangle A_1 A_2 A_3 over a field F (char F != 2), the nine-point center N = (C + O)/2 satisfies 2*N - C = O (and 3*G = 2*C + O when char F != 3), placing C, G, N, O on the Euler line with quadrance proportions Q(C, G) : Q(C, N) : Q(C, O) = 4 : 9 : 36; the three side midpoints M_i, three altitude feet F_i, and three Euler midpoints E_i = (A_i + O)/2 all have exact quadrance K / 4 from N.

.. figure:: w-16.svg
   :align: center
   :width: 88%

   Exact ``geometor.model`` SVG output of ``model.py`` for **W.16 (The Euler Line & Nine-Point Circle Over Arbitrary Fields)**.

Symbolic Construction & Verification Script (``model.py``)
----------------------------------------------------------

.. literalinclude:: model.py
   :language: python
