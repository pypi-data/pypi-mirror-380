"""
This module provides current support.

Copyright 2020--2024 Michael Hayes, UCECE

"""
from .deprecation import LcapyDeprecationWarning
from .expr import expr
from .state import state
from .classmap import domain_kind_to_symbol, domain_kind_quantity_to_class
from warnings import warn


def Iname(name, kind, cache=False):

    # Not caching is a hack to avoid conflicts of Vn1 with Vn1(s) etc.
    # when using subnetlists.  The alternative is a proper context
    # switch.  This would require every method to set the context.

    if kind in ('t', 'time'):
        name = name.lower()

    undef = domain_kind_to_symbol(kind, name)
    cls = domain_kind_quantity_to_class(kind, 'current')

    if not isinstance(kind, str):
        return cls(undef, cache=cache, omega=kind)

    return cls(undef, cache=cache)


def Itype(kind):

    return domain_kind_quantity_to_class(kind, 'current')


def current(arg, **assumptions):
    """Create a current object from the specified arg."""

    expr1 = expr(arg, **assumptions)

    if 'nid' in assumptions:
        from .noisefexpr import FourierNoiseDomainCurrent
        from .noiseomegaexpr import AngularFourierNoiseDomainCurrent

        if expr1.is_fourier_domain or expr1.is_constant_domain:
            expr1 = FourierNoiseDomainCurrent(expr1)
        elif expr1.is_angular_fourier_domain:
            expr1 = AngularFourierNoiseDomainCurrent(expr1)
        else:
            raise ValueError(
                'Cannot represent noise current in %s domain' % expr1.domain)

    try:
        expr1 = expr1.as_current()
    except:
        raise ValueError('Cannot represent %s(%s) as current' %
                         (expr1.__class__.__name__, expr1))

    return expr1


def noisecurrent(arg, **assumptions):
    """Create a new noise current with specified amplitude spectral density."""

    nid = assumptions.get('nid', None)
    positive = assumptions.get('positive', True)

    return current(arg, nid=nid, positive=positive, **assumptions)


def phasorcurrent(arg, omega=None, **assumptions):
    from .phasor import phasor

    return phasor(arg, omega, **assumptions).as_current()


def current_sign(I, is_source):
    """Manipulate the sign of the current according to the current sign
    convention specified by `state.current_sign_convention`."""

    sign_convention = state.current_sign_convention

    if sign_convention is None:
        sign_convention = 'hybrid'

        if is_source:
            state.sign_convention = sign_convention
            warn(
                """The default hybrid sign convention for currents is deprecated and will default to the passive sign convention in the next version of Lcapy.  This only affects the sign of the current through sources.  For example, given the netlist

I1 1 0
R1 1 0

the hybrid sign convention gives `I1.i` as `I1` and the passive sign
convention gives `I1.i` as -I1.

To select the passive sign convention use:
`from lcapy import state; state.current_sign_convention = 'passive'`

To select the hybrid sign convention use:
`from lcapy import state; state.current_sign_convention = 'hybrid'`

""")

    if ((sign_convention == 'hybrid' and is_source)
            or sign_convention == 'active'):
        return -I
    return I
