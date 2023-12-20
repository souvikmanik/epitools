.. _installation:

Installation
------------
To use Epitools, first install it using pip:

.. code-block:: console

   $ pip install epitools
   
Then import it in python console

>>> import epitools
>>> import epitools.epigrowthmodel as egm
>>> from epitools import tcoeff.get_tcoeff as tc

let's do a quickstart 

.. literalinclude:: exp.py
    :language: python

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2 \\
      n(t) & = & \frac{L}{1 + e^{-k(t - t_o)}}
   \end{eqnarray}
