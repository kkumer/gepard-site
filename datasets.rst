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



H1
--

Adloff:2001cn `hep-ex/0107005 <http://arXiv.org/abs/hep-ex/0107005>`_
.....................................................................

This data is not used because it is contained withing the next
item Aktas:2005ty.


Aktas:2005ty `hep-ex/0505061 <http://arXiv.org/abs/hep-ex/0505061>`_
....................................................................


.. code-block:: python

   >>> g.list_data([39, 43, 44])
   [ 39]       H1   8    XGAMMA    0505061 Table 1
   [ 43]       H1   9    XGAMMA    0505061 Table 3
   [ 44]       H1   6    XGAMMA    0505061 Table 2   

We take Table 1 (cross section differential in t), with separate 4 points for
1996-1997 and 4 points for 1999-2000 data. Tables 2 and 3 are total cross
section from same events in dependence on Q2 and W, respectively.


Aaron:2007ab `arXiv:0709.4114 <http://arXiv.org/abs/0709.4114>`_
................................................................


.. code-block:: python

   >>> g.list_data([36, 37, 38, 40, 41, 42])
   [ 36]       H1  12    XGAMMA  0709.4114 Table 3 - upper half
   [ 37]       H1  12    XGAMMA  0709.4114 Table 3 - lower half
   [ 38]       H1  24    XGAMMA  0709.4114 Table 4
   [ 40]       H1   5    XGAMMA  0709.4114 Table 1 - right
   [ 41]       H1  15    XGAMMA  0709.4114 Table 2
   [ 42]       H1   4    XGAMMA  0709.4114 Table 1 - left

This data is not used because it is contained withing the next
item Aaron:2009ac.


Aaron:2009ac `arXiv:0907.5289 <http://arXiv.org/abs/0907.5289>`_
................................................................


.. code-block:: python

   >>> g.list_data([60, 61, 62, 63, 64])
   [ 60]       H1   4    XGAMMA  0907.5289 Table 1a
   [ 61]       H1   5    XGAMMA  0907.5289 Table 1b
   [ 62]       H1  15    XGAMMA  0907.5289 Table 2
   [ 63]       H1  12    XGAMMA  0907.5289 Table 3a
   [ 64]       H1  12    XGAMMA  0907.5289 Table 3b

We use Table 3a which is differential DVCS cross section binned in t and Q2.

.. todo::

   Create dataset from BCA data from Table 4 of this reference.
