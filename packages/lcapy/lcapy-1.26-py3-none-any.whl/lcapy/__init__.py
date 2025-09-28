"""
Lcapy is a Python library for symbolic linear circuit and signal analysis.

Lcapy can analyse circuits described with netlists using modified nodal
analysis.  See lcapy.netlist

Alternatively, Lcapy can analyse networks and circuits formed by
combining one, two, and three port networks.  See lcapy.oneport

For detailed documentation see http://lcapy.readthedocs.io/en/latest

Copyright 2014--2022 Michael Hayes, UCECE
"""
from __future__ import absolute_import, print_function
from sympy import Symbol
from sympy.core.sympify import converter
# This must be imported early to avoid circular import with expr
from .functions import *
from .units import volts, amperes, ohms, siemens, watts
from .state import state
from .inverse_dft import *
from .dft import *
from .differenceequation import *
from .dltifilter import *
from .differentialequation import *
from .ltifilter import *
from .discretetime import *
from .phasor import phasor, phasor_ratio
from .normfexpr import Fexpr
from .normomegaexpr import Omegaexpr
from .omegaexpr import omegaexpr
from .cexpr import *
from .texpr import *
from .uexpr import *
from .sexpr import *
from .fexpr import *
from .expr import *
from .simulator import *
from .randomnetwork import *
from .nettransform import *
from .laplace import *
from .inverse_laplace import *
from .fourier import *
from .inverse_fourier import *
from .hilbert import *
from .inverse_hilbert import *
from .dtstatespace import *
from .statespace import *
from .vector import *
from .tmatrix import *
from .smatrix import *
from .matrix import *
from .sym import *
from .susceptance import susceptance
from .reactance import reactance
from .inductance import inductance
from .capacitance import capacitance
from .conductance import conductance
from .resistance import resistance
from .transfer import transfer
from .impedance import impedance
from .admittance import admittance
from .current import current, noisecurrent, phasorcurrent
from .voltage import voltage, noisevoltage, phasorvoltage
from .twoport import *
from .oneport import *
from .circuit import *
from .symbols import *
from .nodalanalysis import *
from .loopanalysis import *
from .exprclasses import *
from .seqclasses import *
from .printing import *
from .rcparams import rcParams

import sys
del absolute_import, print_function


name = "lcapy"

from packaging.version import Version
from sys import version as python_version

python_version = python_version.split(' ')[0]
if Version(python_version) >= Version('3.8'):
    from importlib.metadata import version
    __version__ = version('lcapy')
    del version
else:
    import pkg_resources
    __version__ = pkg_resources.require('lcapy')[0].version

del python_version
del Version

lcapy_version = __version__

if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    raise ImportError("Python Version 2.6 or above is required for Lcapy.")
else:  # Python 3
    pass
    # Here we can also check for specific Python 3 versions, if needed

del sys

# Do not import units.u since this will conflict with unit step


def show_version():
    """Show versions of Lcapy, SymPy, NumPy, MatplotLib, SciPy, and Python."""

    from sys import version as python_version
    from sympy import __version__ as sympy_version
    from numpy import __version__ as numpy_version
    from scipy import __version__ as scipy_version
    from matplotlib import __version__ as matplotlib_version
    from networkx import __version__ as networkx_version

    print('Python: %s\nSymPy: %s\nNumPy: %s\nMatplotlib: %s\nSciPy: %s\nNetworkx: %s\nLcapy: %s' %
          (python_version, sympy_version, numpy_version,
           matplotlib_version, scipy_version, networkx_version, lcapy_version))


rcParams.load_user()
rcParams.load_local()

# The following is to help sympify deal with j.
# A better fix might be to define an Lcapy class for j and to
# use the __sympy_ method.
converter['j'] = j
converter[Symbol('j')] = j
del converter, Symbol

from .printing import printing_init
printing_init(rcParams['sympy.print_order'])
