.. _sec-data_sets:

#########
Data sets
#########

There are two types of data sets that ship together with Gepard.
One are original sets published by experimental collaborations
which made the measurements. Another are derived sets where original
sets are transformed in some way (e. g. by discrete Fourier transform).
Every data set and point has the attribute `reference` which should
explain if it is original or derived.

Here we list most of the available data sets, with some comments
on how we chose to use them in our fits.

.. todo::

   This is a stub. Most of datasets have yet to be added below.

ZEUS
----

Chekanov:2003ya `hep-ex/0305028 <http://arXiv.org/abs/hep-ex/0305028>`_
.......................................................................

.. code-block:: python

   >>> import gepard as g
   >>> g.list_data(45)
   [ 45]     ZEUS   6         X    0305028 Table 1


We take data from Table 1 with DVCS cross section in dependence on Q2. 
Tables 2 and 3 are same data but binned for W dependence. 
Using Q2 dependence gives us handle on evolution.


Chekanov:2008vy `arXiv:0812.2517 <http://arXiv.org/abs/0812.2517>`_
...................................................................


.. code-block:: python

   >>> g.list_data([46, 47, 48, 49])
   [ 46]     ZEUS   4         X  0812.2517 Table 4
   [ 47]     ZEUS   6         X  0812.2517 Table 1
   [ 48]     ZEUS   6         X  0812.2517 Table 2
   [ 49]     ZEUS   8         X  0812.2517 Table 3

We take data from Table 1 (Q2 dependence of cross section, one might cut low-Q2 points) 
while Tables 2 (and 3) are same data binned in W (W and Q2). 
We also take data from Table 4, which is differential cross section in t, 
extracted from the subset of the above data, so strictly it is not statistically independent.




