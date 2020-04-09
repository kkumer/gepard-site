#############
Documentation
#############

To be written or converted from before:

   * Tutorials as Jupyter notebooks
   * PDFs documenting some specific concepts (MB, ADACF, ..)
   * Proper full documentation

To compile Gepard's Fortran and C extensions after installation
you need Debian packages `gfortran`, `python3-dev` and `python3-numpy` (for f2py)

To run Gepard you also need Debian packages
`python3-logzero`, `python3-gdbm`, `python3-pandas` (which will get `python3-scipy`
and `python3-matplotlib`  as dependencies), and for working
with neural networks you need `pybrain3` which
is not available as Debian package so should be installed by `pip`
or similar Python package manager. (ISSUE/BUG: both pybrain and pybrain3
modules are explicitely needed/imported)


To perform tests of the code you need Debian package
`python3-nose`. Basic tests are done by issuing::

   nosetests --rednose -vA "not newfeature and not long and not extendedtesting"

