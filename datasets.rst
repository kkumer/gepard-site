.. _sec-data_sets:

#########
Data sets
#########

There are two types of data sets that ship together with Gepard.
One contain original numbers published by experimental collaborations
which made the measurements. Another are derived sets where original
sets are transformed in some way (e. g. by discrete Fourier transform).
Every data set (and point) has the attributes `reference` and
`reference2` which should explain where the data comes from
and whether it is original or derived. 

Even "original" sets are still transformed
by Gepard author(s) into Gepard datafile format either by using datafiles provided by
collaborations or tables from published papers. If some errors are
introduced in this process, experimental collaborations obviously cannot
be blamed for this. If you need "official" datafiles, contact the
corresponding collaborations.

Here we list most of the available data sets, with some comments
on how we chose to use them in our fits.

.. todo::

   Only DVCS data sets are listed here at the moment.

CLAS
----


CLAS:2001wjj `hep-ex/0107043 <http://arXiv.org/abs/hep-ex/0107043>`_
....................................................................

S. Stepanyan et al., Phys.Rev.Lett. 87 (2001) 182002

4.25 GeV electron beam. Just one BSA point: $A_{LU}^{\sin\phi}$($Q^2$ = 1.25 GeV$^2$, $x_B$ = 0.19, $-t$ = 0.19 GeV$^2$) = 0.202 $\pm$ 0.028 $\pm$ 0.013.



CLAS:2006krx `hep-ex/0605012 <http://arXiv.org/abs/hep-ex/0605012>`_
....................................................................

S. Chen et al., Phys.Rev.Lett. 97 (2006) 072002

.. code-block:: python

   >>> g.list_data([54])
   [ 54]     CLAS   6       TSA    0605012


CLAS:2006krx `arXiv:0711.4805 <http://arXiv.org/abs/0711.4805>`_
................................................................

F.X. Girod et al., Phys.Rev.Lett. 100 (2008) 162002

.. code-block:: python

   >>> g.list_data([6, 7, 8, 25])
   [  6]     CLAS 744       ALU  0711.4805 private table
   [  7]     CLAS  62       ALU  0711.4805 private table
   [  8]     CLAS  12       ALU  0711.4805 F.T. by DM
   [ 25]     CLAS  16       ALU  0711.4805 F.T. by KK


CLAS:2008ahu `arXiv:0812.2950 <http://arXiv.org/abs/0812.2950>`_
................................................................

G. Gavalian et al., Phys.Rev.C 80 (2009) 035206 

.. code-block:: python

   >>> g.list_data([81])
   [ 81]     CLAS  12       ALU  0812.2950 Tables 3 and 4


CLAS:2015bqi `arXiv:1501.07052 <http://arXiv.org/abs/1501.07052>`_
..................................................................

S. Pisano et al., Phys.Rev.D 91 (2015) 5, 052014

.. code-block:: python

   >>> g.list_data(list(range(88,97)))
   [ 88]     CLAS 166       ALU 1501.07052 
   [ 89]     CLAS 166       TSA 1501.07052 
   [ 90]     CLAS 166      BTSA 1501.07052 
   [ 91]     CLAS 166       ALU 1501.07052 bin averages from Silvia Niccolai
   [ 92]     CLAS 166       TSA 1501.07052 bin averages from Silvia Niccolai
   [ 93]     CLAS 166      BTSA 1501.07052 bin averages from Silvia Niccolai
   [ 94]     CLAS  10       ALU 1501.07052 F.T. by K.K.
   [ 95]     CLAS  10       TSA 1501.07052 F.T. by K.K.
   [ 96]     CLAS  20      BTSA 1501.07052 F.T. by K.K.

There is a precursor PRL paper Seder et al. arXiv:1410.6615 [hep-ex] which
brings just TSA. Comparing harmonics, results from this PRL are different from
what is published in Pisano et al. but phi-space TSA is the same, so one can use
just Pisano et al.

``[88-90]`` are data from the paper, while ``[91-93]`` have averaged xB, Q2 and t
so they are used to make Fourier transform to get ``[94-96]``.



CLAS:2015uuo `arXiv:1504.02009 <http://arXiv.org/abs/1504.02009>`_
..................................................................

H.S. Jo et al., Phys.Rev.Lett. 115 (2015) 21, 212003

.. code-block:: python

   >>> g.list_data([97, 98, 99, 100, 101, 102, 104, 106])
   [ 97]     CLAS 2640       XLU 1504.02009 CLAS data base E145M2
   [ 98]     CLAS 2640       XUU 1504.02009 CLAS data base E145M1
   [ 99]     CLAS 1152       XLU 1504.02009 CLAS data base E145M2, restricted kinematics
   [100]     CLAS 1152       XUU 1504.02009 CLAS data base E145M1, restricted kinematics
   [101]     CLAS  48      XLUw 1504.02009 FT analysis with MC error propagation by KK
   [102]     CLAS  96      XUUw 1504.02009 FT analysis with MC error propagation by KK
   [104]     CLAS 1152       ALU 1504.02009 CLAS data base E145M1, E145M2
   [106]     CLAS  48       ALU 1504.02009 FT analysis with MC error propagation by KK

This data is not independent from (compatible) dataset CLAS:2006krx (F.X. Girod et al.). 
Out of ALU from that paper
and XUU and XLU from this paper, only two observables are independent.
Some CLASS experts (M. Garcon) advocate ALU, XUU combination because of larger kinematic coverage of ALU
and smaller total systematics, while some other advocate XLU, XUU for consistent cuts
and corrections applied.


CLAS:2018bgk `arXiv:1810.02110 <http://arXiv.org/abs/1810.02110>`_
..................................................................

N. Hirlinger Saylor et al., Phys.Rev.C 98 (2018) 4, 045203

It seems that no actual data is publicly available. This is certainly
new data, since beam energy is 5.88 GeV. (Data published in 2015 are with 5.75
GeV.)


CLAS:2022syx `arXiv:2211.11274 <http://arXiv.org/abs/2211.11274>`_
..................................................................

G. Christiaens et al., Phys.Rev.Lett. 130 (2023) 21, 211902

.. code-block:: python

   >>> g.list_data([149])
   [149]     CLAS 1535       ALU 2211.11274 

First CLAS12 DVCS measurement.


Hall A
------

JeffersonLabHallA:2006prd `nucl-ex/0107005 <http://arXiv.org/abs/nucl-ex/0607029>`_
...................................................................................

C. Muñoz Camacho et al.,  Phys.Rev.Lett. 97 (2006) 262002

.. code-block:: python

   >>> g.list_data([26, 30, 33, 34, 35, 50, 51, 55, 56]) 
   [ 26]    HALLA  12    XLUw2C    0607029 DFT analysis with MC error propagation by KK
   [ 30]    HALLA   4       XwA    0607029 DM's fit
   [ 33]    HALLA 288       XLU    0607029 private tables
   [ 34]    HALLA  96       XUU    0607029 private tables
   [ 35]    HALLA   8    XUUw2C    0607029 DFT analysis with MC error propagation by KK
   [ 50]    HALLA 288      XLUw    0607029 DFT analysis with MC error propagation by KK
   [ 51]    HALLA  96      XUUw    0607029 DFT analysis with MC error propagation by KK
   [ 55]    HALLA  36      XLUw    0607029 private tables
   [ 56]    HALLA  20      XUUw    0607029 private tables

For ``KM09b`` ``[30]`` was used. ``[26, 35]`` are $C_{I}$ coefficient extractions. ``[33,34]``
are $\phi$-dependent original data. ``[50,51]`` are KKs DFT transforms of data.
``[55,56]`` are DMs fit to first few harmonics. 
Both of these are weighted with BH propagators.
For global fits we used ``[50]`` (1st sin harmonic) as ``BSSwpoints`` and ``[51]`` 
(0th and 1st cos harmonic) as ``BSDwpoints``.

There is also derived asymmetry data ALU = XLU/XUU by DM:

.. code-block:: python

   >>> g.list_data([103, 105]) 
   [103]    HALLA  96       ALU    0607029 private table
   [105]    HALLA  96       ALU    0607029 FT analysis with MC error propagation by KK



JeffersonLabHallA:2015dwe `arXiv:1504.05453 <http://arXiv.org/abs/1504.05453>`_
...............................................................................

M. Defurne et al.,  Phys.Rev.C 92 (2015) 5, 055202

.. code-block:: python

   >>> g.list_data(list(range(107, 124)))
   [107]    HALLA 120       XUU 1504.05453 Kin2, Table VII
   [108]    HALLA 120       XUU 1504.05453 Kin3, Table VIII
   [109]    HALLA 120       XLU 1504.05453 Kin1, Table IX
   [110]    HALLA 120       XLU 1504.05453 Kin2, Table X
   [111]    HALLA 120       XLU 1504.05453 Kin3, Table XI
   [112]    HALLA 120       XUU 1504.05453 KinX2, Table XII
   [113]    HALLA 120       XUU 1504.05453 KinX3, Table XIII
   [114]    HALLA 120       XLU 1504.05453 KinX2, Table XIV
   [115]    HALLA 120       XLU 1504.05453 KinX3, Table XV
   [116]    HALLA  20      XUUw 1504.05453 FT analysis with MC error propagation by KK
   [117]    HALLA  15      XLUw 1504.05453 FT analysis with MC error propagation by KK
   [118]    HALLA  25      XLUw 1504.05453 FT fitting with numerical error propagation by DM
   [119]    HALLA  40      XUUw 1504.05453 FT fitting with numerical error propagation by DM
   [120]    HALLA  20       XUU 1504.05453 FT analysis with MC error propagation by KK
   [121]    HALLA  15       XLU 1504.05453 FT analysis with MC error propagation by KK
   [122]   HERMES  24       ALU  1206.5683 Table 2
   [123]    HALLA  20      XUUw 1504.05453 FT analysis with MC error propagation by KK

DM's BSSw and BSDw include also KINX kinematic ranges, which are not independent measurements.
There may be disagreements DM vs. KK regarding total systematic uncertainty.
``[122]`` doesn't belong here obviously.


Defurne:2017paw `arXiv:1703.09442 <http://arXiv.org/abs/1703.09442>`_
.....................................................................

M. Defurne et al., Nature Commun. 8 (2017) 1, 1408

.. code-block:: python

   >>> g.list_data(list(range(124, 139)))
   [124]    HALLA  36       BSD 1703.09442 
   [125]    HALLA  36       BSD 1703.09442 
   [126]    HALLA  96       BSD 1703.09442 
   [127]    HALLA  96       BSD 1703.09442 
   [128]    HALLA  96       BSD 1703.09442 
   [129]    HALLA  36       BSS 1703.09442 
   [130]    HALLA  36       BSS 1703.09442 
   [131]    HALLA  96       BSS 1703.09442 
   [132]    HALLA  96       BSS 1703.09442 
   [133]    HALLA  96       BSS 1703.09442 
   [134]    HALLA  90       BSS 1703.09442 
   [135]    HALLA  18      BSDw 1703.09442 FT analysis with MC error propagation by KK
   [136]    HALLA  44      BSSw 1703.09442 FT analysis with MC error propagation by KK
   [137]    HALLA  44      BSSw 1703.09442 FT analysis with MC error propagation by KK

360 XLU and 450 XUU measurements at three beam energies: 3.355, 4.455 and 5.55 GeV.
``[137]`` is extraction where possible c0/c1 enhancement is neglected.




JeffersonLabHallA:2022pnx `arXiv:2201.03714 <http://arXiv.org/abs/2201.03714>`_
.......................................................................................

F. Georges et al., Phys.Rev.Lett. 128 (2022) 25, 252002

Full data available from
`PhD thesis <https://inspirehep.net/literature/1764888>`_
by Frédéric Georges (Orsay, IPN)

.. code-block:: python

   >>> g.list_data([141, 142, 143, 144])
   [141]    HALLA 1080       XUU Georges:2018kyi Appendix D
   [142]    HALLA 1080       XLU Georges:2018kyi Appendix D
   [143]    HALLA  90      XUUw Georges:2018kyi FT analysis with MC error propagation by MC
   [144]    HALLA  45      XLUw Georges:2018kyi FT analysis with MC error propagation by MC

First 12 GeV Hall A data.


Benali:2020vma `arXiv:2109.02076 <http://arXiv.org/abs/2109.02076>`_
.....................................................................

M. Benali et al., Nature Phys. 16 (2020) 2, 191-198

.. code-block:: python

   >>> g.list_data([138, 139, 140])
   [138]    HALLA   8  XSintphi doi:10.1038/s41567-019-0774-3 Table 4
   [139]    HALLA  96       XUU doi:10.1038/s41567-019-0774-3 Table 3
   [140]    HALLA  16      XUUw doi:10.1038/s41567-019-0774-3 FT analysis with MC error propagation by MC


Neutron DVCS at two beam energies: 4.45 and 5.55 GeV.


HERMES
------

HERMES:2001bob `hep-ex/0106058 <http://arXiv.org/abs/hep-ex/0106068>`_
......................................................................

A. Airapetian et al.,   Phys.Rev.Lett. 87 (2001) 182001

ALU. First DVCS measurement. Just a plot, no published numbers.



Frank Ellinghaus (QCD 2002, unpublished)
........................................


.. code-block:: python

   >>> g.list_data([29])
   [ 29]   HERMES  12       ALU   Frank E. from DM's notebook



HERMES:2006pre `hep-ex/0605108 <http://arXiv.org/abs/hep-ex/0605108>`_
......................................................................

A. Airapetian et al., Phys.Rev.D 75 (2007) 011103

$A_C^{\cos\phi}$ in four $x_B$-$Q^2$-$t$ bins. This data is not used in fits.
It is not clear when and how much data is taken. It is probably contained in 
the next dataset HERMES:2008abz.


HERMES:2008abz `arXiv:0802.2499 <http://arXiv.org/abs/0802.2499>`_
..................................................................

A. Airapetian et al., JHEP 06 (2008) 066

.. code-block:: python

   >>> g.list_data([31, 65, 66])
   [ 31]   HERMES  24        AC  0802.2499 Table 1
   [ 65]   HERMES  12   AUTDVCS  0802.2499 Table 1a
   [ 66]   HERMES  36      AUTI  0802.2499 Table 1b

$A_C^{\cos0\phi}$ and $A_C^{\cos\phi}$. The latter 12 points are used in
**GLOpoints** for *KM09a* and *KM09b* fits.

$A_{UT,I}^{\sin(\phi-\phi_S) \cos(\phi)}$, sensitive to
$\Im{}m(F_1\mathcal{E}-F_2\mathcal{H})$ and thus to $\mathcal{E}$, is 12
**AUTIpoints**. As an independent subset (with emphasis on $t$ dependence),
first 4 points (alias: **AUTIpts**) are used in global fits such as *KMM12*.
$A_{UT,I}^{\cos(\phi-\phi_S) \sin(\phi)}$ is proportional to  $\Im{}m(2
F_2\tilde{\mathcal{H}}-F_1\tilde{\mathcal{E}})$ and is consistent with zero so
could be used to put constraint on $\tilde{\mathcal{H}}$ (alias: **AUTICSpts**)
where advantage w.r.t. $A_{UL}$ is that here we have no DVCS$^2$ pollution.


HERMES:2009cqe `arXiv:0909.3587 <http://arXiv.org/abs/0909.3587>`_
..................................................................

A. Airapetian et al., JHEP 11 (2009) 083

.. code-block:: python

   >>> g.list_data([5, 32])
   [  5]   HERMES  18      ALUI  0909.3587 Table 2
   [ 32]   HERMES  36        AC  0909.3587 Table 4


$A_{LU}^{\sin\phi}$ and $A_C^{\cos\phi}$ are used in KM10 models (all 18
points, not just statistically independent 6).



HERMES:2010dsx `arXiv:1004.0177 <http://arXiv.org/abs/1004.0177>`_
..................................................................

A. Airapetian et al., JHEP 06 (2010) 019

.. code-block:: python

   >>> g.list_data([52, 53])
   [ 52]   HERMES  36       TSA  1004.0177 Table 4
   [ 53]   HERMES  36      BTSA  1004.0177 Table 4


HERMES:2011bou `arXiv:1106.2990 <http://arXiv.org/abs/1106.2990>`_
..................................................................

A. Airapetian et al., Phys.Lett.B 704 (2011) 15-23

.. code-block:: python

   >>> g.list_data([73, 74])
   [ 73]   HERMES  39 ALTBHDVCS  1106.2990 Table 2
   [ 74]   HERMES  65      ALTI  1106.2990 Table 2

This data was not yet used for global fits (was used for local fits with
M. Murray). It is consistent with zero.


HERMES:2012idp `arXiv:1206.5683 <http://arXiv.org/abs/1206.5683>`_
..................................................................

A. Airapetian et al., JHEP 10 (2012) 042

.. code-block:: python

   >>> g.list_data([122])
   [122]   HERMES  24       BSA  1206.5683 Table 2

Data with recoil detector.


HERMES:2012gbh `arXiv:1203.6287 <http://arXiv.org/abs/1203.6287>`_
..................................................................

A. Airapetian et al., JHEP 07 (2012) 032

.. code-block:: python

   >>> g.list_data([67, 68, 69, 70, 71, 72])
   [ 67]   HERMES  72        AC  1203.6287 Table 6
   [ 68]   HERMES  36      ALUI  1203.6287 Table 5
   [ 69]   HERMES  18   ALUDVCS  1203.6287 
   [ 70]   HERMES  48        AC  Morgan M. combined 1996-2007 data
   [ 71]   HERMES  24      ALUI  Morgan M. combined 1996-2007 data
   [ 72]   HERMES  12   ALUDVCS  Morgan M. combined 1996-2007 data

Final HERMES data on BCA and BSA. First 6 independent $t$-dep points are used
for global fits as **BCApts** (6 0th and 6 1st cos harmonics) and **ALUIpts**
(6 1st sin harmonics). There is also 4-bin version of this data communicated
privately by M. Murray.


H1
--

H1:2001nez `hep-ex/0107005 <http://arXiv.org/abs/hep-ex/0107005>`_
.....................................................................

C. Adloff et al., Phys.Lett.B 517 (2001) 47-58

This data is not used because it is contained withing the next
item Aktas:2005ty.


H1:2005gdw `hep-ex/0505061 <http://arXiv.org/abs/hep-ex/0505061>`_
....................................................................

A. Aktas et al., Eur.Phys.J.C 44 (2005) 1-11


.. code-block:: python

   >>> g.list_data([39, 43, 44])
   [ 39]       H1   8    XGAMMA    0505061 Table 1
   [ 43]       H1   9    XGAMMA    0505061 Table 3
   [ 44]       H1   6    XGAMMA    0505061 Table 2   

We take Table 1 (cross section differential in t), with separate 4 points for
1996-1997 and 4 points for 1999-2000 data. Tables 2 and 3 are total cross
section from same events in dependence on Q2 and W, respectively.


H1:2007vrx `arXiv:0709.4114 <http://arXiv.org/abs/0709.4114>`_
................................................................

F.D. Aaron et al., Phys.Lett.B 659 (2008) 796-806


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


H1:2009wnw `arXiv:0907.5289 <http://arXiv.org/abs/0907.5289>`_
................................................................

F.D. Aaron et al., Phys.Lett.B 681 (2009) 391-399

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


ZEUS
----

ZEUS:2003pwh `hep-ex/0305028 <http://arXiv.org/abs/hep-ex/0305028>`_
.......................................................................

S. Chekanov et al., Phys.Lett.B 573 (2003) 46-62

.. code-block:: python

   >>> import gepard as g
   >>> g.list_data(45)
   [ 45]     ZEUS   6         X    0305028 Table 1


We take data from Table 1 with DVCS cross section in dependence on Q2. 
Tables 2 and 3 are same data but binned for W dependence. 
Using Q2 dependence gives us handle on evolution.


ZEUS:2008hcd `arXiv:0812.2517 <http://arXiv.org/abs/0812.2517>`_
...................................................................

S. Chekanov et al., JHEP 05 (2009) 108


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



Combined datasets used for fits
-------------------------------

Starting from ``KMM12`` global model, we use just 35 independent
collider points ``H1ZEUS``:

.. code-block:: python

   >>> from gepard.fits import H1ZEUS
   >>> g.describe_data(H1ZEUS)
   npt x obs     collab  FTn    id  ref.        
   ----------------------------------------------
    8 x XGAMMA  H1      N/A    39  hep-ex/0505061
   12 x XGAMMA  H1      N/A    63  arXiv:0907.5289 [hep-ex]
    6 x XGAMMA  ZEUS    N/A    45  hep-ex/0305028
    4 x XGAMMA  ZEUS    N/A    46  arXiv:0812.2517
    5 x XGAMMA  ZEUS    N/A    47  arXiv:0812.2517
   ----------------------------------------------
   TOTAL = 35

