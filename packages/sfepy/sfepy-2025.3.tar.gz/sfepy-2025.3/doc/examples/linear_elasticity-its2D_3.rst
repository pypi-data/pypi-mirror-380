.. _linear_elasticity-its2D_3:

linear_elasticity/its2D_3.py
============================

**Description**


Diametrically point loaded 2-D disk with nodal stress calculation. See
:ref:`sec-primer`.

Find :math:`\ul{u}` such that:

.. math::
    \int_{\Omega} D_{ijkl}\ e_{ij}(\ul{v}) e_{kl}(\ul{u})
    = 0
    \;, \quad \forall \ul{v} \;,

where

.. math::
    D_{ijkl} = \mu (\delta_{ik} \delta_{jl}+\delta_{il} \delta_{jk}) +
    \lambda \ \delta_{ij} \delta_{kl}
    \;.


.. image:: /../doc/images/gallery/linear_elasticity-its2D_3.png


:download:`source code </../sfepy/examples/linear_elasticity/its2D_3.py>`

.. literalinclude:: /../sfepy/examples/linear_elasticity/its2D_3.py

