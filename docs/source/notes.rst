
#####
Notes
#####

My notes on chapter 1 of :

Hairer E, Lubich C, Wanner G, Geometric Numerical Integration: Structure-Preserving Algorithms for ODEs.

A system of differential equations can be written in the form:


.. math::

   \dot{y} = f(y)


------------------
Flow of the System
------------------

A mapping is defined by:

.. math::

    \phi_t(y_0) = y(t)  \text{ with } y(0) = y_0


---------------------
Explicit Euler Method
---------------------

This is the simplest of all numerical methods.

.. math::

   y_{n+1} = y_n + h f(y_n)

This mapping can be represented by:


.. math::

   \Phi_h : y_n \mapsto y_{n+1} 




.. code-block:: python

   #plug python code in 

---------------------
Other Methods
---------------------

The implicit Euler Method:

.. math::

   y_{n+1} = y_n + h f(y_{n+1})

