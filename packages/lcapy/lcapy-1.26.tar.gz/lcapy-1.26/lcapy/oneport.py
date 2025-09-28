"""
This module supports simple linear one-port networks based on the
following ideal components:

| V - independent voltage source
| I - independent current source
| R - resistor
| C - capacitor
| L - inductor

These components are converted to s-domain models so capacitor and
inductor components can be specified with initial voltage and
currents, respectively, to model transient responses.

One-ports can either be connected in series (``+``) or parallel (``|``) to
create a new one-port.

Copyright 2014--2024 Michael Hayes, UCECE

"""

from __future__ import division
from .functions import Heaviside, cos, exp, Derivative, Integral
from .sym import omega0sym, tsym, ksym, oo
from .symbols import j, t, s
from .network import Network
from .immittancemixin import ImmittanceMixin
from .impedance import impedance
from .admittance import admittance
from .voltage import voltage
from .current import current
from warnings import warn


__all__ = ('V', 'I', 'v', 'i', 'R', 'NR', 'L', 'C', 'G', 'Y', 'Z',
           'Vdc', 'Vstep', 'Idc', 'Istep', 'Vac', 'sV', 'sI',
           'Iac', 'Vnoise', 'Inoise',
           'Par', 'Ser', 'Xtal', 'FerriteBead', 'CPE', 'series', 'parallel',
           'ladder')


def _check_oneport_args(args):

    for arg1 in args:
        if not isinstance(arg1, OnePort):
            raise ValueError('%s not a OnePort' % arg1)


class OnePort(Network, ImmittanceMixin):
    """
    One-port network

    There are four major types of OnePort:

    - VoltageSource
    - CurrentSource
    - Impedance
    - Admittance
    - ParSer for combinations of OnePort

    """

    # Dimensions and separations of component with horizontal orientation.
    height = 0.3
    """float : Height of the component in a Horizontal orientation

    """
    hsep = 0.5
    """float : Height separation between components in a Horizontal orientation

    """
    width = 1
    """float : Width of the component in a Horizontal orientation

    """
    wsep = 0.25
    """float : Width separation between components in a Horizontal orientation

    """

    _Z = None
    _Y = None
    _Voc = None
    _Isc = None

    def __add__(self, OP):
        """Series combination"""

        return Ser(self, OP)

    def __or__(self, OP):
        """Parallel combination"""

        return Par(self, OP)

    @property
    def admittance(self):
        """
        Admittance of the one-port.

        Returns
        -------
        Admittance of the one-port. :math:`Y = \\frac{1}{Z}`.

        """
        if self._Y is not None:
            return self._Y
        return 1 / self.impedance

    @property
    def has_parallel_V(self):
        """
        Determines if the one-port has a parallel voltage source.

        Returns
        -------
        bool
            True if the one-port has a parallel voltage source.

        """
        return self.is_voltage_source

    @property
    def has_series_I(self):
        """
        Determines if the one-port has a series current source.
        Returns
        -------
        bool
            True if the one-port has a series current source.

        """
        return self.is_current_source

    @property
    def i(self):
        """
        Open-circuit time-domain current.
        Except for a current source this is zero.

        """
        return self.I.time()

    @property
    def I(self):
        """
        Open-circuit current.
        Except for a current source this is zero.

        """
        return SuperpositionCurrent(0)

    @property
    def impedance(self):
        """
        Impedance of the one-port.

        Returns
        -------
        impedance Z

        Raises
        ------
        ValueError
            If the impedance is undefined for the one-port.

            This occurs when ``Isc``, ``Voc``, ``Y``, or ``Z`` is ``None``,
                as there is no way to calculate impedance for the source.

        """

        if self._Z is not None:
            return self._Z
        if self._Y is not None:
            return 1 / self._Y
        if self._Voc is not None:
            return impedance(0)
        if self._Isc is not None:
            return 1 / admittance(0)
        raise ValueError('_Isc, _Voc, _Y, or _Z undefined for %s' % self)

    @property
    def isc(self):
        """
        Short-circuit time-domain current.

        This is the current flowing out of the positive node of the network,
        through a wire, and back to the negative node of the network.

        """
        return self.Isc.time()

    @property
    def Isc(self):
        """
        Short-circuit current in appropriate transform domain.

        This is the current flowing out of the positive node of the network,
        through a wire, and back to the negative node of the network.

        """
        if self._Isc is not None:
            return self._Isc
        return self.Voc._mul(self.admittance)

    @property
    def v(self):
        """Open-circuit time-domain voltage."""
        return self.voc

    @property
    def V(self):
        """Open-circuit voltage."""
        return self.Voc

    @property
    def voc(self):
        """Open-circuit time-domain voltage."""
        return self.Voc.time()

    @property
    def Voc(self):
        """
        Open-circuit voltage in appropriate transform domain.

        Raises
        ------
        ValueError
            If the open-circuit voltage is undefined for the one-port.

            This occurs when ``Isc``, ``Voc``, ``Y``, or ``Z`` is ``None``.
        """
        if self._Voc is not None:
            return self._Voc
        if self._Isc is not None:
            return self._Isc._mul(self.impedance)
        if self._Z is not None or self._Y is not None:
            return SuperpositionVoltage(0)
        raise ValueError('_Isc, _Voc, _Y, or _Z undefined for %s' % self)

    @property
    def z(self):
        """Impedance impulse-response."""
        return self.impedance.time()

    @property
    def y(self):
        """Admittance impulse-response."""
        return self.admittance.time()

    def _Zkind(self, kind):

        # This is for determining impedances
        if not isinstance(kind, str):
            # AC
            domain = kind
        elif kind in ('super', 'time', 't'):
            domain = 't'
        elif kind in ('laplace', 'ivp', 's'):
            domain = 's'
        elif kind == 'dc':
            domain = 0
        elif kind.startswith('n'):
            domain = 'f'
        else:
            raise RuntimeError('Unhandled circuit kind ' + kind)
        return self.Z(domain)

    def chain(self, TP):
        """Chain to a two-port.  This is experimental."""

        if isinstance(TP, OnePort):
            raise ValueError('Cannot chain oneport with a oneport')

        from .twoport import TwoPort
        if not isinstance(TP, TwoPort):
            raise ValueError('%s not a twoport' % TP)

        return TP.source(self)

    def expand(self):

        return self

    def ladder(self, *args):
        """Create (unbalanced) ladder network"""

        return Ladder(self, *args)

    def load(self, OP2):

        if not issubclass(OP2.__class__, OnePort):
            raise TypeError('Load argument not ', OnePort)

        return LoadCircuit(self, OP2)

    def lsection(self, OP2):
        """Create L section (voltage divider)"""

        if not issubclass(OP2.__class__, OnePort):
            raise TypeError('Argument not ', OnePort)

        return LSection(self, OP2)

    def noise_model(self):
        """Convert to noise model."""

        from .symbols import omega

        if not isinstance(self, (R, G, Y, Z)):
            return self

        R1 = self.R
        if R1 != 0:
            Vn = Vnoise('sqrt(4 * k_B * T * %s)' % R1(j * omega))
            return self + Vn
        return self

        def current_equation(self, v, kind='t'):
            """Return expression for current through component given
            applied voltage."""

            raise NotImplementedError('current_equation not defined')

        def voltage_equation(self, i, kind='t'):
            """Return expression for voltage across component given
            applied current."""

            raise NotImplementedError('voltage_equation not defined')

    def norton(self):
        """Simplify to a Norton network"""

        new = self.simplify()
        Isc = new.Isc
        Y = new.admittance

        if Isc.is_superposition and not Y.is_real:
            warn('Detected superposition with reactive impedance, using s-domain.')
            Y1 = Y
            I1 = Isc.laplace()
        elif Isc.is_ac:
            Y1 = Y.subs(j * Isc.ac_keys()[0])
            I1 = Isc.select(Isc.ac_keys()[0])
        elif Isc.is_dc:
            Y1 = Y.subs(0)
            I1 = Isc(0)
        else:
            I1 = Isc
            Y1 = Y

        I1 = I1.cpt()
        Y1 = Y1.cpt()

        if Isc == 0:
            return Y1
        if Y == 0:
            return I1

        return Par(Y1, I1)

    def parallel(self, OP):
        """Parallel combination"""

        return Par(self, OP)

    def s_model(self):
        """Convert to s-domain."""

        if self._Voc is not None:
            if self._Voc == 0:
                return Z(self.impedance)
            Voc = self._Voc.laplace()
            if self.Z == 0:
                return V(Voc)
            return Ser(V(Voc), Z(self.impedance))
        elif self._Isc is not None:
            if self._Isc == 0:
                return Y(self.admittance)
            Isc = self._Isc.laplace()
            if self.admittance == 0:
                return I(Isc)
            return Par(I(Isc), Y(self.admittance))
        elif self._Z is not None:
            return Z(self._Z)
        elif self._Y is not None:
            return Y(self._Y)
        raise RuntimeError('Internal error')

    def series(self, OP):
        """Series combination"""

        return Ser(self, OP)

    def thevenin(self):
        """Simplify to a Thevenin network"""

        new = self.simplify()
        Voc = new.Voc
        Z = new.impedance

        if Voc.is_superposition and not Z.is_real:
            warn('Detected superposition with reactive impedance, using s-domain.')
            Z1 = Z
            V1 = Voc.laplace()
        elif Voc.is_ac:
            Z1 = Z.subs(j * Voc.ac_keys()[0])
            V1 = Voc.select(Voc.ac_keys()[0])
        elif Voc.is_dc:
            Z1 = Z.subs(0)
            V1 = Voc(0)
        else:
            V1 = Voc
            Z1 = Z

        V1 = V1.cpt()
        Z1 = Z1.cpt()

        if Voc == 0:
            return Z1
        if Z == 0:
            return V1

        return Ser(Z1, V1)

    def tsection(self, OP2, OP3):
        """Create T section"""

        if not issubclass(OP2.__class__, OnePort):
            raise TypeError('Argument not ', OnePort)

        if not issubclass(OP3.__class__, OnePort):
            raise TypeError('Argument not ', OnePort)

        return TSection(self, OP2, OP3)


class ParSer(OnePort):
    """
    Parallel/serial class
    """

    def __str__(self):

        str = ''

        for m, arg in enumerate(self.args):
            argstr = arg.__str__()

            if isinstance(arg, ParSer) and arg.__class__ != self.__class__:
                argstr = '(' + argstr + ')'

            str += argstr

            if m != len(self.args) - 1:
                str += ' %s ' % self._operator

        return str

    def _repr_pretty_(self, p, cycle):

        p.text(self.pretty())

    def _repr_latex_(self):

        return '$%s$' % self.latex()

    def pretty(self, **kwargs):
        """
        'Pretty' string representation of the component.

        Returns
        -------
        str
            A string representation of the component.

        Examples
        --------
        >>> print(Par(R(3), R(2)).simplify())
        R(ConstantDomainExpression(6/5))
        >>> print(Par(R(3), R(2)).simplify().pretty())
        R(6/5)

        """
        str = ''

        for m, arg in enumerate(self.args):
            argstr = arg.pretty(**kwargs)

            if isinstance(arg, ParSer) and arg.__class__ != self.__class__:
                argstr = '(' + argstr + ')'

            str += argstr

            if m != len(self.args) - 1:
                str += ' %s ' % self._operator

        return str

    def pprint(self):
        """
        Prints a pretty string representation of the component to the console.

        Examples
        --------
        >>> print(Par(R(3), R(2)).simplify())
        R(ConstantDomainExpression(6/5))
        >>> Par(R(3), R(2)).simplify().pprint()
        R(6/5)

        """
        print(self.pretty())

    def latex(self):
        """
        :math:`\\LaTeX` string representation of the component.
        Returns
        -------
        str
            A latex string representation of the component.
        """
        str = ''

        for m, arg in enumerate(self.args):
            argstr = arg.latex()

            if isinstance(arg, ParSer) and arg.__class__ != self.__class__:
                argstr = '(' + argstr + ')'

            str += argstr

            if m != len(self.args) - 1:
                str += ' %s ' % self._operator

        return str

    def _combine(self, arg1, arg2):

        if arg1.__class__ != arg2.__class__:
            if self.__class__ == Ser:
                if isinstance(arg1, V) and arg1.Voc == 0:
                    return arg2
                if isinstance(arg2, V) and arg2.Voc == 0:
                    return arg1
                if isinstance(arg1, (R, Z)) and arg1.impedance == 0:
                    return arg2
                if isinstance(arg2, (R, Z)) and arg2.impedance == 0:
                    return arg1
            if self.__class__ == Par:
                if isinstance(arg1, I) and arg1.Isc == 0:
                    return arg2
                if isinstance(arg2, I) and arg2.Isc == 0:
                    return arg1
                if isinstance(arg1, (Y, G)) and arg1.admittance == 0:
                    return arg2
                if isinstance(arg2, (Y, G)) and arg2.admittance == 0:
                    return arg1

            return None

        if self.__class__ == Ser:
            if isinstance(arg1, I):
                return None
            if isinstance(arg1, Vdc):
                return Vdc(arg1.v0 + arg2.v0)
            # Could simplify Vac here if same frequency
            if isinstance(arg1, V):
                return V(arg1 + arg2)
            if isinstance(arg1, R):
                return R(arg1._R + arg2._R)
            if isinstance(arg1, L):
                # The currents should be the same!
                if arg1.i0 != arg2.i0 or arg1.has_ic != arg2.has_ic:
                    raise ValueError('Series inductors with different'
                                     ' initial currents!')
                i0 = arg1.i0 if arg1.has_ic else None
                return L(arg1.L + arg2.L, i0)
            if isinstance(arg1, G):
                return G(arg1._G * arg2._G / (arg1._G + arg2._G))
            if isinstance(arg1, C):
                v0 = arg1.v0 + arg2.v0 if arg1.has_ic or arg2.has_ic else None
                return C(arg1.C * arg2.C / (arg1.C + arg2.C), v0)
            return None

        elif self.__class__ == Par:
            if isinstance(arg1, V):
                return None
            if isinstance(arg1, Idc):
                return Idc(arg1.i0 + arg2.i0)
            # Could simplify Iac here if same frequency
            if isinstance(arg1, I):
                return I(arg1 + arg2)
            if isinstance(arg1, G):
                return G(arg1._G + arg2._G)
            if isinstance(arg1, C):
                # The voltages should be the same!
                if arg1.v0 != arg2.v0 or arg1.has_ic != arg2.has_ic:
                    raise ValueError('Parallel capacitors with different'
                                     ' initial voltages!')
                v0 = arg1.v0 if arg1.has_ic else None
                return C(arg1.C + arg2.C, v0)
            if isinstance(arg1, R):
                return R(arg1._R * arg2._R / (arg1._R + arg2._R))
            if isinstance(arg1, L):
                i0 = arg1.i0 + arg2.i0 if arg1.has_ic or arg2.has_ic else None
                return L(arg1.L * arg2.L / (arg1.L + arg2.L), i0)
            return None

        else:
            raise TypeError('Undefined class')

    def simplify(self, deep=True):
        """
        Performs simple simplifications.

        These simplifications may include parallel resistors, series inductors, etc.,
        rather than collapsing to a Thevenin or Norton network.

        Parameters
        ----------
        deep
            TODO: appears unused

        Warnings
        --------
        This does not expand compound components such as crystal or ferrite bead models. Use :meth:`expand` first.

        Examples
        --------
        >>> Par(Par(R(3), R(2)), I(2)).pprint()
        R(3) | R(2) | I(2)
        >>> Par(Par(R(3), R(2)), I(2)).simplify().pprint()
        R(6/5) | I(2)

        """

        # Simplify args (recursively) and combine operators if have
        # Par(Par(A, B), C) etc.
        new = False
        newargs = []
        for m, arg in enumerate(self.args):
            if isinstance(arg, ParSer):
                arg = arg.simplify(deep)
                new = True
                if arg.__class__ == self.__class__:
                    newargs.extend(arg.args)
                else:
                    newargs.append(arg)
            else:
                newargs.append(arg)

        if new:
            self = self.__class__(*newargs)

        # Scan arg list looking for compatible combinations.
        # Could special case the common case of two args.
        new = False
        args = list(self.args)
        for n in range(len(args)):

            arg1 = args[n]
            if arg1 is None:
                continue
            if isinstance(arg1, ParSer):
                continue

            for m in range(n + 1, len(args)):

                arg2 = args[m]
                if arg2 is None:
                    continue
                if isinstance(arg2, ParSer):
                    continue

                # TODO, think how to simplify things such as
                # Par(Ser(V1, R1), Ser(R2, V2)).
                # Could do Thevenin/Norton transformations.

                newarg = self._combine(arg1, arg2)
                if newarg is not None:
                    # print('Combining', arg1, arg2, 'to', newarg)
                    args[m] = None
                    arg1 = newarg
                    new = True

            args[n] = arg1

        if new:
            args = [arg for arg in args if arg is not None]
            if len(args) == 1:
                return args[0]
            self = self.__class__(*args)

        return self

    def expand(self):
        """
        Expand compound components such as crystals or ferrite bead models into
            :class:`R`, :class:`L`, :class:`G`, :class:`C`, :class:`V`, :class:`I`.

        """

        newargs = []
        for m, arg in enumerate(self.args):
            newarg = arg.expand()
            newargs.append(newarg)

        return self.__class__(*newargs)

    def s_model(self):
        """
        Converts the model to s-domain.

        Returns
        -------
        The s-domain model.

        """
        args = [arg.s_model() for arg in self.args]
        return (self.__class__(*args))

    def noise_model(self):
        """
        Convert to noise model representation.

        Returns
        -------
        The noise model representation.

        """
        args = [arg.noise_model() for arg in self.args]
        return (self.__class__(*args))

    @property
    def Isc(self):
        """
        Short circuit current

        Returns
        -------
        The short circuit current.

        """
        if self.has_independent_source:
            return self.cct.Isc(1, 0)
        return SuperpositionCurrent(0)

    @property
    def Voc(self):
        """
        Open circuit voltage

        Returns
        -------
        The open circuit voltage.

        """
        if self.has_independent_source:
            return self.cct.Voc(1, 0)
        return SuperpositionVoltage(0)

    @property
    def has_independent_source(self):

        for arg in self.args:
            if arg.has_independent_source:
                return True
        return False


class Par(ParSer):
    """
    Defines a pair or more of one-port networks in parallel.


    Parameters
    ----------
    args : tuple[OnePort, ...]
        Tuple of components declared in parallel.

    Attributes
    ----------
    args : tuple[OnePort, ...]
        Tuple of components declared in parallel.

    Raises
    ------
    ValueError
        If less than two arguments are provided.
    ValueError
        If two voltage sources are connected in parallel.

    Warns
    -----
    Redundant Component
        A component may be considered redundant if it is in parallel with a voltage source.

    Warnings
    --------
    A minimum of two arguments are required to define a parallel circuit.

    """

    _operator = '|'
    """str : The operator used to represent the parallel operation in a string.

    """
    is_parallel = True
    """bool : Indicates the component is a parallel combination of components.

    """

    def __init__(self, *args):
        if len(args) < 2:
            raise ValueError('Par requires at least two args')

        _check_oneport_args(args)
        super(Par, self).__init__()
        self.args = args

        for n, arg1 in enumerate(self.args):
            for arg2 in self.args[n + 1:]:
                if isinstance(arg1, V) and isinstance(arg2, V):
                    raise ValueError('Voltage sources connected in parallel'
                                     ' %s and %s' % (arg1, arg2))
                elif isinstance(arg1, V):
                    print('Warn: redundant component %s in parallel with voltage source %s' % (
                        arg2, arg1))

                elif isinstance(arg2, V):
                    print('Warn: redundant component %s in parallel with voltage source %s' % (
                        arg1, arg2))

    @property
    def width(self):
        """
        Provides the width of the parallel circuit, which is the largest width of the components in parallel.

        Returns
        -------
        float
            The width of the parallel circuit.

        """
        total = 0
        for arg in self.args:
            val = arg.width
            if val > total:
                total = val
        return total + 2 * self.wsep

    @property
    def height(self):
        """
        Provides the height of the parallel circuit, which is the sum of the heights of the components in parallel.

        Returns
        -------
        float
            The height of the parallel circuit.

        """
        total = 0
        for arg in self.args:
            total += arg.height
        return total + (len(self.args) - 1) * self.hsep

    def _net_make(self, netlist, n1=None, n2=None, dir='right'):

        s = []
        if n1 is None:
            n1 = netlist._node
        n3, n4 = netlist._node, netlist._node

        H = [(arg.height + self.hsep) * 0.5 for arg in self.args]

        N = len(H)
        num_branches = N // 2

        # Draw component in centre if have odd number in parallel.
        if N & 1:
            s.append(self.args[N // 2]._net_make(netlist, n3, n4, dir))

        na, nb = n3, n4

        s.append('W %s %s; %s=%s' % (n1, n3, dir, self.wsep))

        if dir == 'right':
            updir, downdir = 'up', 'down'
        else:
            updir, downdir = 'right', 'left'

        # Draw components above centre
        for n in range(num_branches):

            if not (N & 1) and n == 0:
                sep = H[N // 2 - 1]
            else:
                sep = H[N // 2 - n] + H[N // 2 - 1 - n]

            nc, nd = netlist._node, netlist._node
            s.append('W %s %s; %s=%s' % (na, nc, updir, sep))
            s.append('W %s %s; %s=%s' % (nb, nd, updir, sep))
            s.append(self.args[N // 2 - 1 - n]._net_make(netlist, nc, nd, dir))
            na, nb = nc, nd

        na, nb = n3, n4

        # Draw components below centre
        for n in range(num_branches):

            if not (N & 1) and n == 0:
                sep = H[(N + 1) // 2]
            else:
                sep = H[(N + 1) // 2 + n] + H[(N + 1) // 2 - 1 + n]

            nc, nd = netlist._node, netlist._node
            s.append('W %s %s; %s=%s' % (na, nc, downdir, sep))
            s.append('W %s %s; %s=%s' % (nb, nd, downdir, sep))
            s.append(self.args[(N + 1) // 2 +
                     n]._net_make(netlist, nc, nd, dir))
            na, nb = nc, nd

        if n2 is None:
            n2 = netlist._node

        s.append('W %s %s; %s=%s' % (n4, n2, dir, self.wsep))
        return '\n'.join(s)

    @property
    def has_parallel_V(self):
        """
        Determines if the one-port has a parallel voltage source.

        Returns
        -------
        bool
            True if any parallel components have a parallel voltage source, or are themselves a voltage source.

        """

        for cpt1 in self.args:
            if cpt1.has_parallel_V:
                return True
        return False

    @property
    def admittance(self):
        """
        Admittance :math:`Y` of the parallel circuit.

        This is the sum of the admittances of the components in parallel.

        Returns
        -------
        float
            The admittance :math:`Y` of the parallel circuit.

        """
        Y = 0
        for arg in self.args:
            Y += arg.admittance
        return Y

    @property
    def impedance(self):
        """
        Impedance :math:`Z` of the parallel circuit.

        This is :math:`\\frac{1}{Y}`, or the inverse of the sum of the admittance of the parallel circuit.

        Returns
        -------
        float
            The impedance :math:`Z` of the parallel circuit.

        """
        return 1 / self.admittance

    @property
    def Isc(self):
        """
        Short circuit current :math:`I_{sc}` of the parallel circuit.

        This is the sum of the short circuit currents of the components in parallel.

        Returns
        -------
        float
            The short circuit current :math:`I_{sc}` of the parallel circuit.

        """
        I = 0
        for arg in self.args:
            I += arg.Isc
        return I


class Ser(ParSer):
    """
    Defines a pair or more of one-port networks in series.

    Parameters
    ----------
    args : tuple[OnePort, ...]
        Tuple of components declared in series.

    Attributes
    ----------
    args : tuple[OnePort, ...]
        Tuple of components declared in series.

    Raises
    ------
    ValueError
        If less than two arguments are provided.
    ValueError
        If two current sources are connected in series.

    Warns
    -----
    Redundant Component
        A component may be considered redundant if it is in series with a current source.

    Warnings
    --------
    A minimum of two arguments are required to define a parallel circuit.

    """

    _operator = '+'
    """ str : The operator used to represent the series operation in a string.

    """
    is_series = True
    """bool : Indicates the component is a series combination of components.

    """

    def __init__(self, *args):

        if len(args) < 2:
            raise ValueError('Ser requires at least two args')

        _check_oneport_args(args)
        super(Ser, self).__init__()
        self.args = args

        for n, arg1 in enumerate(self.args):
            for arg2 in self.args[n + 1:]:
                if isinstance(arg1, I) and isinstance(arg2, I):
                    raise ValueError('Current sources connected in series'
                                     ' %s and %s' % (arg1, arg2))
                elif isinstance(arg1, I):
                    print(
                        'Warn: redundant component %s in series with current source %s' % (arg2, arg1))

                elif isinstance(arg2, I):
                    print(
                        'Warn: redundant component %s in series with current source %s' % (arg1, arg2))

    @property
    def height(self):
        """
        Provides the height of the series circuit, which is the largest height of the components in series.

        Returns
        -------
        float
            The height of the series circuit.

        """
        total = 0
        for arg in self.args:
            val = arg.height
            if val > total:
                total = val
        return total

    @property
    def width(self):
        """
        Provides the width of the series circuit, which is the sum of the widths of the components in series.

        Returns
        -------
        float
            The width of the series circuit.

        """
        total = 0
        for arg in self.args:
            total += arg.width
        return total + (len(self.args) - 1) * self.wsep

    def _net_make(self, netlist, n1=None, n2=None, dir='right'):

        s = []
        if n1 is None:
            n1 = netlist._node
        for arg in self.args[:-1]:
            n3 = netlist._node
            s.append(arg._net_make(netlist, n1, n3, dir))
            n1 = netlist._node
            s.append('W %s %s; %s=%s' % (n3, n1, dir, self.wsep))

        if n2 is None:
            n2 = netlist._node
        s.append(self.args[-1]._net_make(netlist, n1, n2, dir))
        return '\n'.join(s)

    @property
    def has_series_I(self):
        """
        Determines if the one-port has a series current source.

        Returns
        -------
        bool
            True if any series components have a series current source, or are themselves a current source.

        """
        for cpt1 in self.args:
            if cpt1.has_series_I:
                return True
        return False

    @property
    def admittance(self):
        """
        Admittance :math:`Y` of the series circuit.

        This is :math:`\\frac{1}{Z}`, or the inverse of the sum of the impedance of the series circuit.

        Returns
        -------
        float
            The admittance :math:`Y` of the series circuit.

        """
        return 1 / self.impedance

    @property
    def impedance(self):
        """
        Impedance :math:`Z` of the series circuit.

        This is the sum of the impedances of the components in series.

        Returns
        -------
        float
            The impedance :math:`Z` of the series circuit.

        """
        Z = 0
        for arg in self.args:
            Z += arg.impedance
        return Z

    @property
    def Voc(self):
        """
        Open circuit voltage :math:`V_{oc}` of the series circuit.

        This is the sum of the open circuit voltages of the components in series.

        Returns
        -------
        float
            The open circuit voltage :math:`V_{oc}` of the series circuit.

        """

        V = 0
        for arg in self.args:
            V += arg.Voc
        return V


class R(OnePort):
    """
    Defines a simple linear one-port resistor

    Parameters
    ----------
    Rval :  int or float or complex or str
        Resistance value

    Attributes
    ----------
    args : tuple[ int or float or complex or str]
        Resistance value, or, placeholder value 'R'

    """

    is_resistor = True
    """bool : Indicates the component is a resistor

    """
    is_noiseless = False
    """
    bool : Indicates the resistor is not noiseless.
        For noiseless resistor see :class:`lcapy.oneport.NR`.

    """

    def __init__(self, Rval='R', **kwargs):
        self.kwargs = kwargs
        self.args = (Rval, )
        self._R = cexpr(Rval)
        self._Z = impedance(self._R, causal=True)

    def current_equation(self, v, kind='t'):
        """
        Return expression for current through component given applied voltage.

        Parameters
        ----------
        v : str or float
            Applied voltage
        kind : str
            The chosen representation of the equation.

            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for current through the resistor

        """

        return SuperpositionCurrent(SuperpositionVoltage(v).select(kind) / self._Z).select(kind)


    def voltage_equation(self, i, kind='t'):
        """
        Return expression for voltage across component given applied current.

        Parameters
        ----------
        i
            Applied current
        kind : str
            The chosen representation of the equation.

            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        """
        return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Z).select(kind)


class NR(R):
    """
    Noiseless resistor

    As :mod:`lcapy.oneport.R` but noiseless.

    """

    is_noiseless = True
    """
        bool : Indicates the resistor is noiseless.
            For regular resistor see :class:`lcapy.oneport.R`.

    """


class G(OnePort):
    """
    Conductor

    Parameters
    ----------
    Gval :  int or float or complex or str
        Conductance value

    Attributes
    ----------
    args : tuple[ int or float or complex or str]
        Conductance value, or, placeholder value 'G'


    """

    is_conductor = True
    """bool : Indicates the component is a conductor

    """
    is_noiseless = False
    """
    bool : Indicates the conductor is not noiseless.
        For noiseless conductor see :class:`lcapy.oneport.NG`.

    """

    def __init__(self, Gval='G', **kwargs):
        self.kwargs = kwargs
        self.args = (Gval, )
        self._G = cexpr(Gval)
        self._Z = impedance(1 / self._G, causal=True)

    def _net_make(self, netlist, n1=None, n2=None, dir='right'):

        if n1 == None:
            n1 = netlist._node
        if n2 == None:
            n2 = netlist._node
        opts_str = self._opts_str(dir)
        return 'R? %s %s {%s}; %s' % (n1, n2, 1 / self._G, opts_str)

    def current_equation(self, v, kind='t'):
        """
        Return expression for current through component given applied voltage.

        Parameters
        ----------
        v
            Applied voltage
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for current through the conductor

        """

        return SuperpositionCurrent(SuperpositionVoltage(v).select(kind) / self._Z).select(kind)

    def voltage_equation(self, i, kind='t'):
        """
        Return expression for voltage across component given applied current.

        Parameters
        ----------
        i
            Applied current
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for voltage across the conductor

        """

        return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Z).select(kind)


class NG(G):
    """
    Noiseless conductor

    """

    is_noiseless = True
    """
    bool : Indicates the conductor is noiseless.
        For noiseless conductor see :class:`lcapy.oneport.G`.

    """

class L(OnePort):
    """
    Inductor

    Parameters
    ----------
    Lval :  int or float or complex or str
        Inductance value :math:`L`
    i0 : int or float, optional
        Initial current :math:`i_0`

    Attributes
    ----------
    args : tuple[ int or float or complex or str, int or float or complex]
        a tuple containing the inductance value :math:`L` and the initial current :math:`i_0`
    L : ConstantDomainExpression
        constant expression representation of the inductance value :math:`L`
    i0 : ConstantDomainExpression
        constant expression representation of the initial current :math:`i_0`
    has_ic : bool
        Indicates if the inductor has an initial current :math:`i_0`
    zeroic : bool
        Indicates if the initial current :math:`i_0` is zero

    """

    is_inductor = True
    """bool: Indicates the component is an inductor

    """

    def __init__(self, Lval='L', i0=None, **kwargs):

        self.kwargs = kwargs
        self.has_ic = i0 is not None
        if i0 is None:
            i0 = 0

        if self.has_ic:
            self.args = (Lval, i0)
        else:
            self.args = (Lval, )

        Lval = cexpr(Lval)
        i0 = cexpr(i0)
        self.L = Lval
        self.i0 = i0
        self._Z = impedance(s * Lval, causal=True)
        self._Voc = SuperpositionVoltage(LaplaceDomainExpression(-i0 * Lval))
        self.zeroic = self.i0 == 0

    def current_equation(self, v, kind='t'):
        """
        Return expression for current through component given applied voltage.

        Parameters
        ----------
        v : int or float
            Applied voltage
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for current through the inductor

        """

        from .sym import tausym

        if kind in ('t', 'time', 'super'):
            u = tausym
            v = expr(v).subs(t, u)
            if self.has_ic:
                return SuperpositionCurrent(Integral(v, (u, 0, tsym)) / self.L).select(kind) + expr(self.i0)

            return SuperpositionCurrent(Integral(v, (u, -oo, tsym)) / self.L).select(kind)
        elif kind in ('s', 'laplace'):
            return SuperpositionCurrent((SuperpositionVoltage(v).select(kind) + self.L * self.i0) / self._Zkind(kind)).select(kind)
        return SuperpositionCurrent(SuperpositionVoltage(v).select(kind) / self._Zkind(kind)).select(kind)

    def voltage_equation(self, i, kind='t'):
        """
        Return expression for voltage across component given applied current.

        Parameters
        ----------
        i : int or float
            Applied current
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for voltage across the inductor

        """

        if kind in ('t', 'time', 'super'):
            return SuperpositionVoltage(self.L * Derivative(i, t)).select(kind)
        elif kind in ('s', 'laplace'):
            return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Zkind(kind) - self.L * self.i0).select(kind)
        return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Zkind(kind)).select(kind)


class C(OnePort):
    """
    Defines a simple linear one-port capacitor.

    Parameters
    ----------
    Cval
        Capacitance
    v0
        Initial Voltage

    Attributes
    ----------
    C
        TODO: What is this?
    v0
        Initial Voltage
    zeroic : bool
        Indicates w if initial voltage v0 is zero volts

    """

    is_capacitor = True
    """
    bool: Indicates the component is a capacitor

    """

    def __init__(self, Cval='C', v0=None, **kwargs):

        self.kwargs = kwargs
        self.has_ic = v0 is not None
        if v0 is None:
            v0 = 0

        if self.has_ic:
            self.args = (Cval, v0)
        else:
            self.args = (Cval, )

        Cval = cexpr(Cval)
        v0 = cexpr(v0)
        self.C = Cval
        self.v0 = v0
        self._Z = impedance(1 / (s * Cval), causal=True)
        self._Voc = SuperpositionVoltage(LaplaceDomainExpression(v0 / s))
        self.zeroic = self.v0 == 0

    def current_equation(self, v, kind='t'):
        """
        Return expression for current through component given applied voltage.

        Parameters
        ----------
        v
            Applied voltage
        kind : str
            The chosen representation of the equation.

            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for current through the capacitor

        Examples
        --------
        >>> from lcapy import C, t, s
        >>> C(2).current_equation(5)
        2*Derivative(5, t)

        """

        if kind in ('t', 'time', 'super'):
            return SuperpositionCurrent(self.C * Derivative(v, t)).select(kind)
        elif kind in ('s', 'laplace'):
            return SuperpositionCurrent((SuperpositionVoltage(v).select(kind) - self.v0 / s) / self._Zkind(kind)).select(kind)

        return SuperpositionCurrent(SuperpositionVoltage(v).select(kind) / self._Zkind(kind)).select(kind)

    def voltage_equation(self, i, kind='t'):
        """
        Return expression for voltage across component given applied current.

        Parameters
        ----------
        i
            Applied current
        kind : str
            The chosen representation of the equation.

            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for voltage across the capacitor

        Examples
        --------
        >>> from lcapy import C, t, s
        >>> C(2).voltage_equation(5)
        Integral(5, (tau, -oo, t))/2

        """

        from .sym import tausym

        if kind in ('t', 'time', 'super'):
            u = tausym
            i = expr(i).subs(t, u)
            if self.has_ic:
                return SuperpositionVoltage(Integral(i, (u, 0, tsym)) / self.C).select(kind) + expr(self.v0)

            return SuperpositionVoltage(Integral(i, (u, -oo, tsym)) / self.C).select(kind)
        elif kind in ('s', 'laplace'):
            return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Zkind(kind) + self.v0 / s).select(kind)

        return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Zkind(kind)).select(kind)
        pass

class CPE(OnePort):
    """
    Constant phase element

    This has an impedance ``1 / s ** alpha * K``.

    - When ``alpha == 0``, the CPE is equivalent to a resistor of resistance 1 / K.
    - When ``alpha == 1``, the CPE is equivalent to a capacitor of capacitance K.
    - When ``alpha == 0.5`` (default), the CPE is a Warburg element.

    The phase of the impedance is ``-pi * alpha / 2``.

    Parameters
    ----------
    K
        Equivalent Capacitance or Conductance
    alpha : float
        Exponent, with value from 0 to 1

    Attributes
    ----------
    K
        Equivalent Capacitance or Conductance
    alpha : float
        Exponent, with value from 0 to 1

    Notes
    -----
    When alpha is non-integral, the impedance cannot be represented as a rational function and so there are no poles or zeros.  So don't be surprised if Lcapy throws an occasional wobbly."""

    def __init__(self, K, alpha=0.5, **kwargs):

        self.kwargs = kwargs
        self.args = (K, alpha)

        K = cexpr(K)
        alpha = cexpr(alpha)
        self.K = K
        self.alpha = alpha
        self._Z = impedance(1 / (s ** alpha * K), causal=True)


class Y(OnePort):
    """
    General admittance :math:`Y`

    Parameters
    ----------
    Yval :  int or float or complex or str
        Admittance value :math:`Y`

    Attributes
    ----------
    args : tuple[ int or float or complex or str]
        Admittance value :math:`Y`

    """

    def __init__(self, Yval='Y', **kwargs):

        self.kwargs = kwargs
        self.args = (Yval, )
        Yval = admittance(Yval)
        self._Y = Yval

    def current_equation(self, v, kind='t'):
        """
        Return expression for current through component given applied voltage.

        Parameters
        ----------
        v
            Applied voltage
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for current through the component

        """

        return SuperpositionCurrent(SuperpositionVoltage(v).select(kind) / self._Z).select(kind)

    def voltage_equation(self, i, kind='t'):
        """
        Return expression for voltage across component given applied current.

        Parameters
        ----------
        i
            Applied current
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        """

        return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Z).select(kind)


class Z(OnePort):
    """
    General impedance :math:`Z`

    Parameters
    ----------
    Zval : int or float or complex or str
        Impedance value :math:`Z`

    Attributes
    ----------
    args : tuple[int or float or complex or str]
        Impedance value :math:`Z`

    """

    def __init__(self, Zval='Z', **kwargs):

        self.kwargs = kwargs
        self.args = (Zval, )
        Zval = impedance(Zval)
        self._Z = Zval

    def current_equation(self, v, kind='t'):
        """
        Return expression for current through component given applied voltage.

        Parameters
        ----------
        v : str or float
            Applied voltage
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for current through the impedance

        """

        return SuperpositionCurrent(SuperpositionVoltage(v).select(kind) / self._Z).select(kind)

    def voltage_equation(self, i, kind='t'):
        """
        Return expression for voltage across component given applied current.

        Parameters
        ----------
        i : str or float
            Applied current
        kind : str
            The chosen representation of the equation.

            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for current voltage across the impedance

        """

        return SuperpositionVoltage(SuperpositionCurrent(i).select(kind) * self._Z).select(kind)


class VoltageSourceBase(OnePort):

    is_voltage_source = True
    """bool : Indicates the component is a voltage source

    """
    has_independent_source = True
    """bool : Indicates the component has an independent source

    """
    cpt_type = 'V'
    """str : The type of component, in this case 'V' for voltage source

    """
    is_noisy = False
    """bool : Indicates the voltage source is not noisy.

    """

    def voltage_equation(self, i, kind='t'):
        """
        Return expression for voltage across component given applied current.

        Parameters
        ----------
        i : int or float or complex
            Applied current :math:`i`
        kind : str
            The chosen representation of the equation.
            See :func:`lcapy.super.Superposition.select` for a description of the different representations supported.

        Returns
        -------
        Expression for voltage across the voltage source

        Warnings
        --------
        Input current ``i`` appears to be ignored when creating the voltage equation.

        """

        return SuperpositionVoltage(self.voc).select(kind)


class sV(VoltageSourceBase):
    """
    Arbitrary s-domain voltage source

    Parameters
    ----------
    Vval : int or float or complex
        Voltage value :math:`v`

    Attributes
    ----------
    args : tuple[int or float or complex]
        Voltage value :math:`v`

    """

    netkeyword = 's'
    """str : The netlist keyword to define the voltage source type

    """

    def __init__(self, Vval, **kwargs):

        self.kwargs = kwargs
        self.args = (Vval, )
        Vval = LaplaceDomainExpression(Vval)
        self._Voc = SuperpositionVoltage(LaplaceDomainExpression(Vval))


class V(VoltageSourceBase):
    """
    Arbitrary voltage source :math:`V`

    Parameters
    ----------
    Vval : int or float or complex
        Voltage value :math:`V`

    Attributes
    ----------
    args : tuple[int or float or complex]
        Voltage value :math:`V`

    """

    def __init__(self, Vval='V', **kwargs):

        self.kwargs = kwargs
        self.args = (Vval, )
        self._Voc = SuperpositionVoltage(Vval)


class Vstep(VoltageSourceBase):
    """
    Step voltage source (s domain voltage of v / s).

    Parameters
    ----------
    v : int or float or complex
        Voltage value :math:`v`

    Attributes
    ----------
    args : tuple[int or float or complex]
        Voltage value :math:`v`
    v0 : int or float or complex
        Initial Voltage :math:`v_0`

    """

    netkeyword = 'step'
    """str : The netlist keyword to define the voltage source type

    """

    def __init__(self, v, **kwargs):

        self.kwargs = kwargs
        self.args = (v, )
        v = cexpr(v)
        self._Voc = SuperpositionVoltage(
            TimeDomainExpression(v) * Heaviside(t))
        self.v0 = v


class Vdc(VoltageSourceBase):
    """
    DC voltage source

    (note a DC voltage source of voltage V has an s domain voltage of V / s).

    Parameters
    ----------
    Vval : int or float or complex
        Voltage value :math:`V`

    Attributes
    ----------
    args : tuple[int or float or complex]
        Voltage value :math:`V`
    v0 : int or float or complex
        Initial Voltage :math:`v_0`

    """

    netkeyword = 'dc'
    """str : The netlist keyword to define the voltage source type

    """

    def __init__(self, Vval, **kwargs):

        self.kwargs = kwargs
        self.args = (Vval, )
        Vval = cexpr(Vval)
        self._Voc = SuperpositionVoltage(cexpr(Vval, dc=True))
        self.v0 = Vval

    @property
    def voc(self):
        """
        Open circuit voltage :math:`V_{oc}` of the DC voltage source.

        Returns
        -------
        Expression for the open circuit voltage :math:`V_{oc}`.

        """
        return voltage(self.v0)


class Vac(VoltageSourceBase):
    """
    AC voltage source.

    Parameters
    ----------
    V : int or float
        Voltage value :math:`V`
    phi : int or float
        Phase angle :math:`\phi`
    omega : int or float
        Angular frequency :math:`\omega`

    Attributes
    ----------
    args
        A tuple containing Voltage value :math:`V`, phase angle :math:`\phi`, and angular frequency :math:`\omega`
    v0
        Initial Voltage :math:`v_0`
    omega
        Angular frequency :math:`\omega`
    phi
        Phase angle :math:`\phi`

    """

    netkeyword = 'ac'
    """str : The netlist keyword to define the voltage source type

    """

    def __init__(self, V, phi=None, omega=None, **kwargs):

        self.kwargs = kwargs
        if phi is None and omega is None:
            self.args = (V, )
        elif phi is not None and omega is None:
            self.args = (V, phi)
        elif phi is None and omega is not None:
            self.args = (V, 0, omega)
        else:
            self.args = (V, phi, omega)

        if phi is None:
            phi = 0

        if omega is None:
            omega = omega0sym
        omega = expr(omega)

        V = cexpr(V)
        phi = cexpr(phi)

        # Note, cos(-pi / 2) is not quite zero.

        self.omega = omega
        self.v0 = V
        self.phi = phi
        self._Voc = SuperpositionVoltage(phasor(self.v0 * exp(j * self.phi),
                                                omega=self.omega))

    @property
    def voc(self):
        """
        Open circuit voltage :math:`V_{oc}` of the AC voltage source.

        Returns
        -------
        Expression for the open circuit voltage :math:`V_{oc}`.

        """
        return voltage(self.v0 * cos(self.omega * t + self.phi))


class Vnoise(VoltageSourceBase):
    """
    Noise voltage source.

    Parameters
    ----------
    V : int or float
        Voltage value :math:`V`
    nid : optional
        Noise Identifier

    Attributes
    ----------
    args
        A tuple containing Voltage value :math:`V` and noise identifier ``nid``

    """

    netkeyword = 'noise'
    """str : The netlist keyword to define the voltage source type

    """
    is_noisy = True
    """bool : Indicates the voltage source is noisy.

    """

    def __init__(self, V, nid=None, **kwargs):

        self.kwargs = kwargs
        V1 = AngularFourierNoiseDomainVoltage(V, nid=nid)
        self.args = (V, V1.nid)
        self._Voc = SuperpositionVoltage(V1)


class v(VoltageSourceBase):
    """
    Arbitrary t-domain voltage source

    Parameters
    ----------
    vval : int or float
        Voltage value :math:`v`

    """

    def __init__(self, vval, **kwargs):

        self.kwargs = kwargs
        self.args = (vval, )
        Vval = TimeDomainExpression(vval)
        self._Voc = SuperpositionVoltage(Vval)


class CurrentSourceBase(OnePort):

    is_current_source = True
    """bool : Indicates the component is a current source

    """
    has_independent_source = True
    """bool : Indicates the component has an independent source

    """
    cpt_type = 'I'
    """str : The type of component, in this case 'I' for current source

    """
    is_noisy = False
    """bool : Indicates the current source is not noisy.

    """

    @property
    def I(self):
        """Open-circuit current of a current source."""
        return self.Isc

    def current_equation(self, v, kind='t'):
        """Return expression for current through component given
        applied voltage."""

        return SuperpositionCurrent(self.isc).select(kind)


class sI(CurrentSourceBase):
    """Arbitrary s-domain current source"""

    netkeyword = 's'

    def __init__(self, Ival, **kwargs):

        if isinstance(Ival, str) and Ival == 'I':
            warn('Current I is being considered as the imaginary number')

        self.kwargs = kwargs
        self.args = (Ival, )
        Ival = LaplaceDomainExpression(Ival)
        self._Isc = SuperpositionCurrent(LaplaceDomainExpression(Ival))


class I(CurrentSourceBase):
    """Arbitrary current source"""

    def __init__(self, Ival='Is', **kwargs):

        if isinstance(Ival, str) and Ival == 'I':
            warn('Current I is being considered as the imaginary number')

        self.kwargs = kwargs
        self.args = (Ival, )
        self._Isc = SuperpositionCurrent(Ival)


class Istep(CurrentSourceBase):
    """Step current source (s domain current of i / s)."""

    netkeyword = 'step'

    def __init__(self, Ival, **kwargs):

        if isinstance(Ival, str) and Ival == 'I':
            warn('Current I is being considered as the imaginary number')

        self.kwargs = kwargs
        self.args = (Ival, )
        Ival = cexpr(Ival)
        self._Isc = SuperpositionCurrent(
            TimeDomainExpression(Ival) * Heaviside(t))
        self.i0 = Ival


class Idc(CurrentSourceBase):
    """DC current source (note a DC current source of current i has
    an s domain current of i / s)."""

    netkeyword = 'dc'

    def __init__(self, Ival, **kwargs):

        if isinstance(Ival, str) and Ival == 'I':
            warn('Current I is being considered as the imaginary number')

        self.kwargs = kwargs
        self.args = (Ival, )
        Ival = cexpr(Ival)
        self._Isc = SuperpositionCurrent(cexpr(Ival, dc=True))
        self.i0 = Ival

    @property
    def isc(self):
        return current(self.i0)


class Iac(CurrentSourceBase):
    """AC current source."""

    netkeyword = 'ac'

    def __init__(self, Ival, phi=0, omega=None, **kwargs):

        if isinstance(Ival, str) and Ival == 'I':
            warn('Current I is being considered as the imaginary number')

        self.kwargs = kwargs
        if phi is None and omega is None:
            self.args = (Ival, )
        elif phi is not None and omega is None:
            self.args = (Ival, phi)
        elif phi is None and omega is not None:
            self.args = (Ival, 0, omega)
        else:
            self.args = (Ival, phi, omega)

        if phi is None:
            phi = 0

        if omega is None:
            omega = omega0sym
        omega = cexpr(omega)

        Ival = cexpr(Ival)
        phi = cexpr(phi)

        self.omega = omega
        self.i0 = Ival
        self.phi = phi
        self._Isc = SuperpositionCurrent(phasor(self.i0 * exp(j * self.phi),
                                                omega=self.omega))

    @property
    def isc(self):
        return current(self.i0 * cos(self.omega * t + self.phi))


class Inoise(CurrentSourceBase):
    """Noise current source."""

    netkeyword = 'noise'
    is_noisy = True

    def __init__(self, Ival, nid=None, **kwargs):

        if isinstance(Ival, str) and Ival == 'I':
            warn('Current I is being considered as the imaginary number')

        self.kwargs = kwargs
        I1 = AngularFourierNoiseDomainCurrent(Ival, nid=nid)
        self._Isc = SuperpositionCurrent(I1)
        self.args = (Ival, I1.nid)


class i(CurrentSourceBase):
    """Arbitrary t-domain current source"""

    def __init__(self, Ival, **kwargs):

        if isinstance(Ival, str) and Ival == 'I':
            warn('Current I is being considered as the imaginary number')

        self.kwargs = kwargs
        self.args = (Ival, )
        Ival = TimeDomainExpression(Ival)
        self._Isc = SuperpositionCurrent(Ival)


class Xtal(OnePort):
    """Crystal

    This is modelled as a series R, L, C circuit in parallel
    with C0 (a Butterworth van Dyke model).  Note,
    harmonic resonances are not modelled.
    """

    def __init__(self, C0, R1, L1, C1, **kwargs):

        self.kwargs = kwargs
        self.C0 = cexpr(C0)
        self.R1 = cexpr(R1)
        self.L1 = cexpr(L1)
        self.C1 = cexpr(C1)

        self._Z = self.expand().impedance
        self.args = (C0, R1, L1, C1)

    def expand(self):

        return (R(self.R1) + L(self.L1) + C(self.C1)) | C(self.C0)

    def _net_make(self, netlist, n1=None, n2=None, dir='right'):

        # TODO: draw this with a symbol
        net = self.expand()
        return net._net_make(netlist, n1, n2, dir)


class FerriteBead(OnePort):
    """Ferrite bead (lossy inductor)

    This is modelled as a series resistor (Rs) connected
    to a parallel R, L, C network (Rp, Lp, Cp).
    """

    def __init__(self, Rs, Rp, Cp, Lp, **kwargs):

        self.kwargs = kwargs
        self.Rs = cexpr(Rs)
        self.Rp = cexpr(Rp)
        self.Cp = cexpr(Cp)
        self.Lp = cexpr(Lp)

        self._Z = self.expand().impedance
        self.args = (Rs, Rp, Cp, Lp)

    def expand(self):

        return R(self.Rs) + (R(self.Rp) + L(self.Lp) + C(self.Cp))

    def _net_make(self, netlist, n1=None, n2=None, dir='right'):

        # TODO: draw this with a symbol
        net = self.expand()
        return net._net_make(netlist, n1, n2, dir)


class LoadCircuit(Network):
    """Circuit comprised of a load oneport connected in parallel with a
    source oneport."""

    def __init__(self, source_OP, load_OP):

        self.source_OP = source_OP
        self.load_OP = load_OP

        self.vnet = source_OP | load_OP
        self.inet = source_OP + load_OP
        self.args = (source_OP, load_OP)

    @property
    def V(self):
        """Voltage across load."""
        return self.vnet.Voc

    @property
    def v(self):
        """Time-domain voltage across load."""
        return self.vnet.voc

    @property
    def I(self):
        """Current into load."""
        return self.inet.Isc

    @property
    def i(self):
        """Time-domain current into load."""
        return self.inet.isc

    def _net_make(self, netlist, n1=None, n2=None, dir='right'):

        # TODO: draw this better rather than as a oneport.
        return self.vnet._net_make(netlist, n1, n2, dir)


class ControlledSource(OnePort):
    """These components are controlled one-ports."""
    pass


class CCVS(ControlledSource):

    is_voltage_source = True

    def __init__(self, control, value, **kwargs):

        self.kwargs = kwargs
        self.args = (control, value)
        self._Voc = SuperpositionVoltage(0)
        self._Z = impedance(0)


class CCCS(ControlledSource):

    is_current_source = True

    def __init__(self, control, value, **kwargs):

        self.kwargs = kwargs
        self.args = (control, value)
        self._Isc = SuperpositionCurrent(0)
        self._Y = admittance(0)


class VCVS(ControlledSource):

    is_voltage_source = True

    def __init__(self, value, Ac=0, **kwargs):

        self.kwargs = kwargs
        self.args = (value, Ac)
        self._Voc = SuperpositionVoltage(0)
        self._Z = impedance(0)


class VCCS(ControlledSource):

    is_current_source = True

    def __init__(self, value, **kwargs):

        self.kwargs = kwargs
        self.args = (value, )
        self._Isc = SuperpositionCurrent(0)
        self._Y = admittance(0)


class Dummy(OnePort):

    def __init__(self, *args, **kwargs):

        self.kwargs = kwargs
        self.args = args


class K(Dummy):
    """Coupling coefficient"""

    def __init__(self, L1, L2, K, **kwargs):

        if K is ksym or (isinstance(K, Expr) and K.var is ksym):
            warn("""
Coupling coefficient %s is the discrete Fourier domain variable.
You can override it using %s = symbol('%s', force=True).""" % (K, K, K))

        self.kwargs = kwargs
        self.args = (L1, L2, K)
        self.K = cexpr(K)


class W(Dummy):
    """Wire (short)"""

    def __init__(self, **kwargs):

        self.kwargs = kwargs
        self.args = ()
        self._Z = impedance(0)


class O(Dummy):
    """Open circuit"""

    def __init__(self, **kwargs):

        self.kwargs = kwargs
        self.args = ()
        self._Y = admittance(0)


class P(O):
    """Port (open circuit)"""
    pass


class Mass(C):
    """Mass

    Mass mval, initial velocity v0"""
    pass


class Spring(L):
    """Spring

    Spring constant kval, initial force f0"""

    def __init__(self, kval='k', f0=None, **kwargs):

        Lval = 1 / cexpr(kval)

        super().__init__(Lval, f0, **kwargs)


class Damper(G):
    """Damper

    Friction coeff val"""
    pass


def series(*args):
    """Create a series combination of a number of components.
    Args that are None are ignored.  If there is only one
    non-None component, return that component."""

    args = [net for net in args if net is not None]
    if args == []:
        return None
    if len(args) == 1:
        return args[0]
    return Ser(*args)


def parallel(*args):
    """Create a parallel combination of a number of components.
    Args that are None are ignored.  If there is only one
    non-None component, return that component."""

    args = [net for net in args if net is not None]
    if args == []:
        return None
    if len(args) == 1:
        return args[0]
    return Par(*args)


def ladder(*args, **kwargs):
    """Create a ladder oneport network with alternating series and shunt components.
    If an arg is None, the component is ignored.

    ladder(R(1), C(2), R(3)) is equivalent to R(1) + (C(1) | R(3))

    ladder(None, R(1), C(2), R(3)) is equivalent to R(1) | (C(1) + R(3))
    """

    start_series = kwargs.pop('start_series', True)

    if len(args) == 0:
        return None
    elif len(args) == 1:
        return args[0]
    elif start_series:
        return series(args[0], ladder(*args[1:], start_series=not start_series))
    else:
        return parallel(args[0], ladder(*args[1:], start_series=not start_series))


# Imports at end to circumvent circular dependencies
from .twoport import Ladder, LSection, TSection  # nopep8
from .superpositioncurrent import SuperpositionCurrent  # nopep8
from .superpositionvoltage import SuperpositionVoltage  # nopep8
from .noiseomegaexpr import AngularFourierNoiseDomainCurrent, AngularFourierNoiseDomainVoltage  # nopep8
from .phasor import phasor  # nopep8
from .texpr import TimeDomainExpression  # nopep8
from .sexpr import LaplaceDomainExpression  # nopep8
from .cexpr import cexpr  # nopep8
from .expr import Expr, expr  # nopep8
