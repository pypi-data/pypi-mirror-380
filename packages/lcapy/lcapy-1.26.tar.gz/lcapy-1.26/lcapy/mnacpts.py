"""
This module defines the components for modified nodal analysis.  The components
are defined at the bottom of this file.

Copyright 2015--2023 Michael Hayes, UCECE

"""

from __future__ import print_function
from .expr import expr
from .cexpr import ConstantDomainExpression
from .omegaexpr import AngularFourierDomainExpression
from .symbols import j, omega, jomega, s, t
from .functions import sqrt
from .sym import capitalize_name, omegasym, eps
from .grammar import delimiters
from .immittancemixin import ImmittanceMixin
from .superpositioncurrent import SuperpositionCurrent
from .voltage import voltage
from .current import current
from .opts import Opts
from .node import DummyNode
from .valueparser import value_parser
import lcapy
import inspect
import sys
import sympy as sym
from warnings import warn

__all__ = ()
module = sys.modules[__name__]

cptaliases = {'E': 'VCVS', 'F': 'CCCS',
              'G': 'VCCS',  'H': 'CCVS',
              'r': 'Damper', 'm': 'Mass',
              'k': 'Spring'}


class Cpt(ImmittanceMixin):

    need_branch_current = False
    need_extra_branch_current = False
    need_control_current = False
    is_directive = False
    flip_branch_current = False
    ignore = False
    add_series = False
    add_parallel = False
    equipotential_nodes = ()
    is_dependent_source = False
    is_independent_source = False
    is_reactive = False
    is_mutual_coupling = False
    is_open_circuit = False
    is_port = False
    is_switch = False
    is_transformer = False
    is_wire = False
    is_current_controlled = False
    is_voltage_controlled = False
    is_opamp = False
    extra_argnames = ()

    def __init__(self, cct, namespace, name, cpt_type, cpt_id, string,
                 opts_string, node_names, keyword, *args):

        self.cct = cct
        self.type = cpt_type
        self.id = cpt_id
        self.name = name
        self.relname = name
        self.namespace = ''
        self.node_names = node_names

        self.nodes = []
        if cct is not None:
            for node_name in node_names:
                self.nodes.append(cct.nodes.add(node_name, self, cct))
        else:
            for node_name in node_names:
                self.nodes.append(DummyNode(node_name))

        self.relnodes = self.nodes

        # Handle names such as a.R1 or a.b.R1.  The namespace is
        # a for the first example and a.b for the second.
        # The relative name (relname) in both cases is R1.
        parts = name.split('.')
        if len(parts) > 1:
            self.namespace = '.'.join(parts[0:-1]) + '.'
            self.relname = parts[-1]
            # self.relnodes = []
            # for node in nodes:
            #     if node.startswith(self.namespace):
            #         node = node[len(self.namespace):]
            #     self.relnodes.append(node)

        self._string = string
        self.args = args
        args = self._process_args(args)
        self.classname = self.__class__.__name__
        self.keyword = keyword
        self.opts = Opts(opts_string)

        self.nosim = 'nosim' in self.opts

        # No defined cpt
        if self.type in ('XX', 'Cable') or self.nosim:
            self._cpt = lcapy.oneport.Dummy()
            return

        classname = self.classname
        # Handle aliases.
        try:
            classname = cptaliases[classname]
        except:
            pass

        try:
            newclass = getattr(lcapy.oneport, classname)
        except:
            try:
                newclass = getattr(lcapy.twoport, classname)
            except:
                self._cpt = lcapy.oneport.Dummy()
                self.check()
                return

        self._cpt = newclass(*args)
        self.check()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        # This works if the nodes are renamed or the args are changed
        return self._netmake()

    def _process_args(self, args):
        """Convert args such as 42p to 42e-12.

        The suffixes are ignored in expressions such as 10 * 42p."""

        pargs = []
        for arg in args:
            pargs.append(value_parser(arg))

        return pargs

    @property
    def cpt(self):
        return self._cpt

    @property
    def _kind(self):
        return self.keyword[1]

    def pdb(self):
        import pdb
        pdb.set_trace()
        return self

    def check(self):
        pass

    def _stamp(self, mna):
        raise NotImplementedError('stamp method not implemented for %s' % self)

    def _copy(self):
        """Make copy of net."""

        return str(self)

    def _expand(self):
        """Make copy of net."""

        return str(self)

    def _arg_format(self, value):
        """Place value string inside curly braces if it contains a delimiter."""

        # Don't use Expr.__str__ since this will add units
        # if show_units enabled.
        try:
            value = value.sympy
        except AttributeError:
            pass

        string = str(value)

        if string.startswith('{'):
            return string

        for delimiter in delimiters:
            if delimiter in string:
                return '{' + string + '}'
        return string

    def annotate(self, *args, **kwargs):
        """Annotate cpt by adding `kwargs` to opts.
        For example, `color='blue'` or `'color=blue'`."""

        s = ''
        for arg in args:
            s += ',' + arg

        for key, val in kwargs.items():
            s += ',' + key + '=' + val

        opts = self.opts.copy()
        opts.add(s)

        return self._netmake_opts(opts)

    def _kill(self):
        """Kill sources."""

        return self._copy()

    def _replace_switch(self, t, before=False):
        """Replace switch with short-circuit or open-circuit at time t."""

        return self._copy()

    def _subs(self, subs_dict):
        """Substitute values using dictionary of substitutions.
        If a scalar is passed, this is substituted for the component value.

        For example, given a component, cpt, defined as 'R1 1 2' then
        cpt.subs(5) and cpt.subs({'R1': 5}) are equivalent.  In both
        cases, the result is 'R1 1 2 5'."""

        if not isinstance(subs_dict, dict):
            subs_dict = {self.args[0]: subs_dict}

        return self._netsubs(subs_dict=subs_dict)

    def _initialize(self, ic):
        """Change initial condition to ic."""

        return self._copy()

    def _change_kind(self, kind):

        if self.keyword[1] == kind:
            return self

        cpt = self
        node_positions = [node.pos for node in cpt.nodes]
        self.cct.remove(cpt.name)
        cpt.keyword = (cpt.keyword[0], kind)
        self.cct.add(str(cpt))
        newcpt = self.cct[cpt.name]
        for node, pos in zip(newcpt.nodes, node_positions):
            node.pos = pos
        return newcpt

    def _change_name(self, name):

        if self.name == name:
            return self

        cpt = self
        node_positions = [node.pos for node in cpt.nodes]
        # TODO, fix if namespace not ''
        cpt.relname = name
        self.cct.add(str(cpt))
        self.cct.remove(cpt.name)

        newcpt = self.cct[name]
        for node, pos in zip(newcpt.nodes, node_positions):
            node.pos = pos
        return newcpt

    def _change_control(self, control_cpt_name):

        from .parser import split

        if not self.is_dependent_source:
            return self

        control_cpt = self.cct[control_cpt_name]

        cpt = self
        node_positions = [node.pos for node in cpt.nodes]
        self.cct.remove(cpt.name)

        fields = split(str(cpt), ' ')
        if cpt.type in ('E', 'G'):
            fields[3] = control_cpt.nodes[0].name
            fields[4] = control_cpt.nodes[1].name

        else:
            fields[3] = control_cpt_name

        netitem = ' '.join(fields)
        self.cct.add(netitem)
        newcpt = self.cct[cpt.name]
        for node, pos in zip(newcpt.nodes[0:2], node_positions[0:2]):
            node.pos = pos
        return newcpt

    def _netsubs(self, node_map=None, zero=False, subs_dict=None):
        """Create a new net description using substitutions in `subs_dict`.
        If `node_map` is not `None`, rename the nodes.  If `zero` is `True`,
        set args to zero."""

        string = self.name
        field = 0

        for node in self.relnodes:
            node_name = node.name
            if node_map is not None:
                node_name = node_map[node_name]
            string += ' ' + node_name
            field += 1
            if field == self.keyword[0]:
                string += ' ' + self.keyword[1]
                field += 1

        for arg in self.args:
            if zero:
                # FIXME: zeroing all args doesn't make much sense.
                # Perhaps only zero first arg?
                arg = 0
            elif subs_dict is not None:
                if arg is None:
                    continue
                # Perform substitutions
                arg = str(expr(arg).subs(subs_dict))

            string += ' ' + self._arg_format(arg)
            field += 1
            if field == self.keyword[0]:
                string += ' ' + self.keyword[1]

        if len(self.args) == 0 and self.keyword[0] == 0:
            string += ' ' + self.keyword[1]

        opts_str = str(self.opts).strip()
        if opts_str != '':
            string += '; ' + opts_str
        return string

    def _rename_nodes(self, node_map):
        """Rename the nodes using dictionary node_map."""

        return self._netsubs(node_map)

    def _netmake1(self, name, nodes=None, args=None, opts=None,
                  ignore_keyword=False):

        if nodes is None:
            nodes = self.relnodes

        if args is None:
            args = self.args
        elif isinstance(args, tuple):
            args = list(args)
        elif not isinstance(args, list):
            args = [args]

        if opts is None:
            opts = self.opts

        parts = name.split('.')
        relname = parts[-1]
        namespace = '.'.join(parts[0:-1])

        fmtargs = []
        for m, arg in enumerate(args):
            # Ignore initial value if not defined.
            if arg is None:
                if m == len(args) - 1:
                    continue
                arg = 0

            fmtargs.append(self._arg_format(arg))

        if len(fmtargs) == 1 and fmtargs[0] == relname:
            fmtargs = []

        # Never name wires, etc, since this confuses the autonamer
        if relname[0] in ('A', 'O', 'W', 'P') and relname[1:].startswith('anon'):
            relname = relname[0]

        name = relname
        if namespace != '':
            name = namespace + '.' + relname

        parts = [name]

        # Handle things like U1 opamp
        if self.keyword[0] == 0 and self.keyword[1] != '':
            parts.append(self.keyword[1])

        for m, node in enumerate(nodes):
            name = node if isinstance(node, str) else node.name
            parts.append(name)
            if not ignore_keyword and self.keyword[0] == m + 1 \
               and self.keyword[1] != '':
                parts.append(self.keyword[1])

        parts.extend(fmtargs)

        net = ' '.join(parts)
        opts_str = str(opts).strip()
        if opts_str != '':
            net += '; ' + opts_str
        return net

    def _netmake(self, nodes=None, args=None, opts=None, ignore_keyword=False):
        """This keeps the same cpt name"""
        return self._netmake1(self.namespace + self.relname, nodes, args, opts,
                              ignore_keyword=ignore_keyword)

    def _netmake_W(self, nodes=None, opts=None):
        """This is used for changing cpt name from L1 to W"""
        return self._netmake1(self.namespace + 'W', nodes, args=(),
                              opts=opts, ignore_keyword=True)

    def _netmake_O(self, nodes=None, opts=None):
        """This is used for changing cpt name from C1 to O"""
        return self._netmake1(self.namespace + 'O', nodes, args=(),
                              opts=opts, ignore_keyword=True)

    def _netmake_opts(self, opts=None):
        """This is used for changing the opts"""
        return self._netmake1(self.namespace + self.relname, opts=opts)

    def _netmake_variant(self, newtype, nodes=None, args=None, opts=None,
                         suffix=''):
        """This is used for changing cpt name from C1 to ZC1"""

        name = self.namespace + newtype + self.relname + suffix
        return self._netmake1(name, nodes, args, opts)

    def _netmake_expand(self, name, nodes=None, args=None, opts=None):
        """This is used for expanding a component into multiple components"""

        name = self.namespace + name + '__' + self.relname
        return self._netmake1(name, nodes, args, opts, ignore_keyword=True)

    def _select(self, kind=None):
        return self._copy()

    def _new_value(self, value, ic=None):

        args = (value, )
        if ic is not None:
            args = (value, ic)

        return self._netmake(args=args)

    def _zero(self):
        """Zero value of the voltage source.  This kills it but keeps it as a
        voltage source in the netlist.  This is required for dummy
        voltage sources that are required to specify the controlling
        current for CCVS and CCCS components."""

        raise ValueError('Component not a source: %s' % self)

    def _r_model(self):
        """Return resistive model of component."""
        return self._copy()

    def _s_model(self, var):
        """Return s-domain model of component."""
        return self._copy()

    def _ss_model(self):
        """Return state-space model of component."""
        return self._copy()

    def _pre_initial_model(self):
        """Return pre-initial model of component."""
        return self._copy()

    @property
    def is_dangling(self):
        """Return True if component is dangling (i.e., has a node with a
        single connection)."""

        return len(self.nodes) == 2 and \
            (self.nodes[0].is_dangling or self.nodes[1].is_dangling)

    @property
    def is_disconnected(self):
        """Return True if component is disconnected (i.e., all nodes have a
        single connection)."""

        if self.type == 'XX':
            return False

        for node in self.nodes:
            if not node.is_dangling:
                return False
        return True

    @property
    def is_source(self):
        """Return True if component is a source (dependent or independent)"""
        return self.is_dependent_source or self.is_independent_source

    @property
    def _source_IV(self):

        if self.cpt.is_voltage_source:
            return self.cpt.Voc
        elif self.cpt.is_current_source:
            return self.cpt.Isc
        else:
            raise ValueError('%s is not a source' % self)

    def in_parallel(self):
        """Return set of components in parallel with cpt."""

        return self.cct.in_parallel(self.name)

    def in_series(self):
        """Return set of components in series with cpt.  Note, this
        does not find components that do not share a node, for example,
        R1 and R3 are not considered as being in series for
        R1 + (R2 | R3) + R3"""

        return self.cct.in_series(self.name)

    @property
    def is_causal(self):
        """Return True if causal component or if source produces
        a causal signal."""

        if self.is_source:
            return self._source_IV.is_causal
        return self.cpt.is_causal

    @property
    def is_dc(self):
        """Return True if source is dc."""

        return self._source_IV.is_dc

    @property
    def is_ac(self):
        """Return True if source is ac."""

        return self._source_IV.is_ac

    @property
    def has_ac(self):
        """Return True if source has ac component."""

        return self._source_IV.has_ac

    @property
    def has_dc(self):
        """Return True if source has dc component."""

        return self._source_IV.has_dc

    @property
    def has_noisy(self):
        """Return True if source has noisy component."""

        return self._source_IV.has_noisy

    @property
    def has_s_transient(self):
        """Return True if source has transient component defined in s-domain."""

        return self._source_IV.has_s_transient

    @property
    def has_t_transient(self):
        """Return True if source has transient component defined in time domain."""

        return self._source_IV.has_t_transient

    @property
    def has_transient(self):
        """Return True if source has a transient component."""

        return self._source_IV.has_transient

    @property
    def is_noisy(self):
        """Return True if source is noisy."""

        if self.cpt.is_voltage_source:
            return self.cpt.is_noisy
        elif self.cpt.is_current_source:
            return self.cpt.is_noisy
        else:
            raise ValueError('%s is not a source' % self)

    @property
    def is_noiseless(self):
        """Return True if component is noiseless."""

        return self.cpt.is_noiseless

    @property
    def is_inductor(self):
        """Return True if component is an inductor."""
        return self.cpt.is_inductor

    @property
    def is_capacitor(self):
        """Return True if component is a capacitor."""
        return self.cpt.is_capacitor

    @property
    def is_oneport(self):
        """Return True if component is any oneport (R, C, L, V, I, etc.)."""

        from .oneport import OnePort
        return isinstance(self.cpt, OnePort)

    @property
    def is_twoport(self):
        """Return True if component is any twoport (TP, TF, GY, etc.)."""

        from .twoport import TwoPort
        return isinstance(self.cpt, TwoPort)

    @property
    def is_reactance(self):
        """Return True if component is a capacitor or inductor."""
        return self.is_capacitor or self.is_inductor

    @property
    def is_resistor(self):
        """Return True if component is a resistor."""
        return self.cpt.is_resistor

    @property
    def is_conductor(self):
        """Return True if component is a conductor."""
        return self.cpt.is_conductor

    @property
    def is_voltage_source(self):
        """Return True if component is a voltage source (dependent or
        independent)"""
        return self.cpt.is_voltage_source

    @property
    def is_dependent_voltage_source(self):
        """Return True if component is a dependent voltage source."""
        return self.cpt.is_voltage_source and self.is_dependent_source

    @property
    def is_independent_voltage_source(self):
        """Return True if component is a independent voltage source."""
        return self.cpt.is_voltage_source and self.is_independent_source

    @property
    def is_current_source(self):
        """Return True if component is a current source (dependent or
        independent)"""
        return self.cpt.is_current_source

    @property
    def is_dependent_current_source(self):
        """Return True if component is a dependent current source."""
        return self.cpt.is_current_source and self.is_dependent_source

    @property
    def is_independent_current_source(self):
        """Return True if component is a independent current source."""
        return self.cpt.is_current_source and self.is_independent_source

    @property
    def zeroic(self):
        """Return True if initial conditions are zero (or unspecified)."""

        return self.cpt.zeroic

    @property
    def has_ic(self):
        """Return True if initial conditions are specified."""

        return self.cpt.has_ic

    @property
    def I(self):
        """Current through component.  The current is defined to be into the
        positive node."""

        if self.ignore:
            raise ValueError('Cannot determine I for %s' % self)

        return self.cct.get_I(self.name)

    @property
    def i(self):
        """Time-domain current through component.  The current is
        defined to be into the positive node."""

        return self.cct.get_i(self.name)

    @property
    def V(self):
        """Voltage drop across component."""

        if self.ignore:
            raise ValueError('Cannot determine V for %s' % self)

        return self.cct.get_Vd(self.nodes[0].name, self.nodes[1].name)

    @property
    def v(self):
        """Time-domain voltage drop across component."""

        return self.cct.get_vd(self.nodes[0].name, self.nodes[1].name)

    @property
    def Isc(self):
        """Short-circuit current for component in isolation, i.e, current in
        wire connected across component."""

        return self.cpt.Isc.select(self.cct.kind, True)

    @property
    def isc(self):
        """Short-circuit time-domain current for component in isolation, i.e,
        current in wire connected across component."""

        return self.Isc.time()

    @property
    def Voc(self):
        """Open-circuit voltage for component in isolation."""

        return self.cpt.Voc.select(self.cct.kind, True)

    @property
    def voc(self):
        """Open-circuit time-domain voltage for component in isolation."""

        return self.Voc.time()

    @property
    def V0(self):
        """Initial voltage (for capacitors only)."""

        return voltage(0)

    @property
    def I0(self):
        """Initial current (for inductors only)."""

        return current(0)

    @property
    def admittance(self):
        """Self admittance of component.

        The admittance is expressed in jomega form for AC circuits
        and in s-domain for for transient circuits.

        For the driving-point admittance measured across the component
        use .dpY or .oneport().Y"""

        return self.cpt.admittance._select(self.cct.kind)

    @property
    def impedance(self):
        """Self impedance of component.

        The impedance is expressed in jomega form for AC circuits
        and in s-domain for for transient circuits.

        For the driving-point impedance measured across the component
        use .dpZ or .oneport().Z"""

        return self.cpt.impedance._select(self.cct.kind)

    @property
    def dpIsc(self):
        """Driving-point short-circuit current, i.e, current in wire
        connected across component connected in-circuit.

        """
        return self.oneport().Isc

    @property
    def dpisc(self):
        """Driving-point short-circuit time-domain current i.e, current in
        wire connected across component in-circuit."""

        return self.dpIsc.time()

    @property
    def dpVoc(self):
        """Driving-point open-circuit voltage across component in-circuit."""

        return self.oneport().V

    @property
    def dpvoc(self):
        """Driving-point open-circuit time-domain voltage across component in
        circuit."""

        return self.dpVoc.time()

    @property
    def dpY(self):
        """Driving-point admittance measured across component in-circuit.  For
        the admittance of the component in isolation use .Y"""

        return self.cct.admittance(self.nodes[1].name, self.nodes[0].name)

    @property
    def dpZ(self):
        """Driving-point impedance measured across component in-circuit.  For
        the impedance of the component in isolation use .Z"""

        return self.cct.impedance(self.nodes[1].name, self.nodes[0].name)

    def _dummy_node(self):

        return DummyNode(self.cct._dummy_node_name())

    def oneport(self):
        """Create oneport object."""

        return self.cct.oneport(self.nodes[1].name, self.nodes[0].name)

    def thevenin(self):
        """Create Thevenin oneport object."""

        return self.cct.thevenin(self.nodes[1].name, self.nodes[0].name)

    def norton(self):
        """Create Norton oneport object."""

        return self.cct.norton(self.nodes[1].name, self.nodes[0].name)

    def transfer(self, cpt):
        """Create transfer function for the s-domain voltage across the
        specified cpt divided by the s-domain voltage across self."""

        if isinstance(cpt, str):
            cpt = self.cct._elements[cpt]

        return self.cct.transfer(self.nodes[1].name, self.nodes[0].name,
                                 cpt.nodes[1].name, cpt.nodes[0].name)

    def connected(self):
        """Return list of components connected to this component."""

        cpts = set()
        for node in self.nodes:
            cpts = cpts.union(set(node.connected))

        return list(cpts)

    def is_connected(self, cpt):
        """Return True if cpt is connected to this component."""

        if isinstance(cpt, str):
            for cpt1 in self.connected:
                if cpt1.name == cpt:
                    return True
            return False

        return cpt in self.connected

    def open_circuit(self):
        """Apply open-circuit in series with component.  Returns name of
        open-circuit component."""

        dummy_node = self._dummy_node()
        net = self._netmake((dummy_node, ) + tuple(self.relnodes[1:]))
        self.cct.remove(self.name)
        self.cct.add(net)
        self.cct.add('O? %s %s' % (self.relnodes[0].name, dummy_node.name))
        return self.cct.last_added()

    def short_circuit(self):
        """Apply short-circuit across component.  Returns name of voltage
        source component used as the short."""

        parallel_set = self.in_parallel()
        for cptname in parallel_set:
            cpt = self.cct.elements[cptname]
            if cpt.is_voltage_source:
                if cpt.value == 0:
                    warn('Component %s already shorted by %s' %
                         (self.name, cptname))
                else:
                    warn('Shorting voltage source %s in parallel with %s' %
                         (cptname, self.name))
            elif cpt.is_current_source:
                warn('Shorting current source %s in parallel with %s' %
                     (cptname, self.name))

        # Could add wire or zero ohm resistor but then could not
        # determine current through the short.  So instead add a
        # voltage source.
        self.cct.add('V? %s %s 0' % (self.nodes[0], self.nodes[1]))

        return self.cct.last_added()

    @property
    def argnames(self):

        """Return list of arg names."""

        args = [self.name]
        args.extend([self.name + '_' + name for name in self.extra_argnames])

        return args

    def defs(self):
        """Return directory of argname-value pair."""

        defs = {}
        for argname, value in zip(self.argnames, self.args):
            if value is None:
                # Initial condition for C and L.
                continue
            if argname != value and expr(value).is_constant:
                defs[argname] = value

        return defs

    def sympify(self):
        """Return component with numerical values removed."""

        if len(self.args) == 1:

            if expr(self.args[0]).is_constant:
                return self._netmake(args=[])
            return self._netmake()

        # FIXME
        # What about E1 1 0 opamp 2 3 Ac 7 Ro  ?  Should the 7 be replaced
        # with Ad, or perhaps E1.Ad?

        return self._netmake(args=self.argnames)


class Invalid(Cpt):
    pass


class NonLinear(Invalid):

    def _stamp(self, mna):
        raise NotImplementedError(
            'Cannot analyse non-linear component: %s' % self)


class TimeVarying(Invalid):

    def _stamp(self, mna):
        raise NotImplementedError(
            'Cannot analyse time-varying component (use convert_IVP): %s' % self)


class Logic(Invalid):

    def _stamp(self, mna):
        raise NotImplementedError('Cannot analyse logic component: %s' % self)


class Misc(Invalid):

    def _stamp(self, mna):
        raise NotImplementedError('Cannot analyse misc component: %s' % self)


class Dummy(Cpt):

    causal = True
    dc = False
    ac = False
    zeroic = True
    has_ic = None
    noisy = False

    def _stamp(self, mna):
        pass


class Ignore(Dummy):

    ignore = True

    @property
    def Voc(self):
        raise ValueError('Cannot determine Voc for %s' % self)

    @property
    def Isc(self):
        raise ValueError('Cannot determine Isc for %s' % self)


class XX(Ignore):

    is_directive = True

    def _subs(self, subs_dict):
        return self._copy()

    def _rename_nodes(self, node_map):
        """Rename the nodes using dictionary node_map."""

        return self._copy()

    def __str__(self):
        return self._string

    def sympify(self):
        return self._copy()


class AM(Cpt):

    # Model ammeter as a 0 V voltage source so can determine
    # the current.

    need_branch_current = True
    flip_branch_current = True
    add_series = True

    def _stamp(self, mna):

        n1, n2 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n1 >= 0:
            mna._B[n1, m] += 1
            mna._C[m, n1] += 1
        if n2 >= 0:
            mna._B[n2, m] -= 1
            mna._C[m, n2] -= 1


class IndependentSource(Cpt):

    is_independent_source = True

    def _zero(self):
        """Zero value of the source.  For a voltage source this makes it a
        short-circuit; for a current source this makes it
        open-circuit.  This effectively kills the source but keeps it
        as a source in the netlist.  This is required for dummy
        voltage sources that are required to specify the controlling
        current for CCVS and CCCS components.

        """
        return self._netsubs(zero=True)


class DependentSource(Dummy):

    is_dependent_source = True

    def _zero(self):
        return self._copy()


class RLC(Cpt):

    def _s_model(self, kind):

        var = s if kind == 's' else kind

        if self.Voc == 0:
            return self._netmake_variant('Z', args=self.Z(var))

        dummy_node = self._dummy_node()

        opts = self.opts.copy()

        # Strip voltage labels and save for open-circuit cpt
        # in parallel with Z and V.
        voltage_opts = opts.strip_voltage_labels()

        znet = self._netmake_variant('Z', nodes=(self.relnodes[0], dummy_node),
                                     args=self.Z(var), opts=opts)

        # Strip voltage and current labels from voltage source.
        opts.strip_all_labels()

        vnet = self._netmake_variant('V', nodes=(dummy_node, self.relnodes[1]),
                                     args=self.Voc.laplace()(var), opts=opts)
        if voltage_opts == {}:
            return znet + '\n' + vnet

        # Create open circuit in parallel to the Z and V
        # that has the voltage labels.
        opts = self.opts.copy()
        opts.strip_current_labels()
        # Need to convert voltage labels to s-domain.
        # v(t) -> V(s)
        # v_C -> V_C
        # v_L(t) -> V_L(s)
        for opt, val in voltage_opts.items():
            opts[opt] = capitalize_name(val)

        onet = self._netmake_O(opts=opts)
        return znet + '\n' + vnet + '\n' + onet


class RC(RLC):

    def _noisy(self, T='T'):

        dummy_node = self._dummy_node()

        opts = self.opts.copy()

        # Should check for namespace conflict if user has defined
        # a noiseless resistor.
        rnet = self._netmake_variant('N', nodes=(self.relnodes[0], dummy_node),
                                     args=str(self.R), opts=opts)

        # Use k_B for Boltzmann's constant to avoid clash with k symbol
        # for discrete frequency
        Vn = 'sqrt(4 * k_B * %s * %s)' % (T, self.args[0])
        vnet = self._netmake_variant('Vn', nodes=(dummy_node, self.relnodes[1]),
                                     args=('noise', Vn), opts=opts)
        return rnet + '\n' + vnet

    def _stamp(self, mna):

        # L's can also be added with this stamp but if have coupling
        # it is easier to generate a stamp that requires the branch current
        # through the L.
        n1, n2 = mna._cpt_node_indexes(self)

        if self.type == 'm':
            if n1 != -1 and n2 != -1:
                warn('Mass %s should have one node grounded' % self)

        if self.type == 'C' and mna.kind == 'dc':
            # Assume a conductance of eps in parallel with the
            # capacitor.  After the matrix inversion, the limit
            # will be calculated for eps=0.
            Y = eps
        else:
            Y = self.Y.sympy

        if n1 >= 0 and n2 >= 0:
            mna._G[n1, n2] -= Y
            mna._G[n2, n1] -= Y
        if n1 >= 0:
            mna._G[n1, n1] += Y
        if n2 >= 0:
            mna._G[n2, n2] += Y

        if mna.kind == 'ivp' and self.cpt.has_ic:
            I = self.Isc.sympy
            if n1 >= 0:
                mna._Is[n1] += I
            if n2 >= 0:
                mna._Is[n2] -= I


class C(RC):

    is_reactive = True
    add_parallel = True
    extra_argnames = ('v0', )

    @property
    def C(self):
        return self.cpt.C

    # Replace C with open-circuit for DC but this loses branch current through C
    # def _select(self, kind=None):
    #     if kind != 'dc':
    #         return self._copy()
    #
    #     copts = self.opts.copy()
    #     copts.add('nosim')
    #     return self._netmake_opts(copts) + '\n' + self._netmake_O()

    def _kill(self):
        """Kill implicit sources due to initial conditions."""
        return self.netmake(args=self.args[0])

    def _initialize(self, ic):
        """Change initial condition to ic."""
        return self._netmake(args=(self.args[0], ic))

    def _pre_initial_model(self):

        return self._netmake_variant('V', args=self.cpt.v0)

    def _r_model(self):

        dummy_node = self._dummy_node()
        opts = self.opts.copy()

        # Use Thevenin model.  This will require the current through
        # the voltage source to be explicitly computed.

        Req = 'R%seq' % self.name
        Veq = 'V%seq' % self.name

        opts.strip_voltage_labels()
        rnet = self._netmake_variant('R', suffix='eq',
                                     nodes=(
                                         self.relnodes[0], dummy_node),
                                     args=Req, opts=opts)

        opts.strip_current_labels()
        vnet = self._netmake_variant('V', suffix='eq',
                                     nodes=(dummy_node,
                                            self.relnodes[1]),
                                     args=('dc', Veq), opts=opts)

        # TODO: the voltage labels should be added across an
        # open-circuit object.

        return rnet + '\n' + vnet

    def _ss_model(self):
        # Perhaps mangle name to ensure it does not conflict
        # with another voltage source?
        return self._netmake_variant('V_', args='v_%s(t)' % self.relname)

    def sympify(self):
        """Return component with numerical values removed."""

        if self.has_ic:
            return self._netmake(args=self.argnames)

        return self._netmake(args=[])

    @property
    def V0(self):
        """Initial voltage (for capacitors only)."""

        if self.cct.kind == 'ivp' and self.cpt.has_ic:
            return voltage(self.cpt.v0 / s)
        return voltage(0)


class CPE(RC):

    extra_argnames = ('alpha',)

    @property
    def K(self):
        return self.cpt.K

    @property
    def alpha(self):
        return self.cpt.alpha

    @property
    def is_reactive(self):
        return self.alpha != 0


class VCVS(DependentSource):
    """VCVS"""

    need_branch_current = True
    is_voltage_controlled = True

    def check(self):

        n1, n2, n3, n4 = [node.name for node in self.nodes]
        if n1 == n3 and n2 == n4:
            warn('VCVS output nodes and control nodes are the same for %s' % self)

    def _stamp(self, mna):
        n1, n2, n3, n4 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n1 >= 0:
            mna._B[n1, m] += 1
            mna._C[m, n1] += 1
        if n2 >= 0:
            mna._B[n2, m] -= 1
            mna._C[m, n2] -= 1

        Ad = ConstantDomainExpression(self.args[0]).sympy
        if len(self.args) > 1:
            Ac = ConstantDomainExpression(self.args[1]).sympy
        else:
            Ac = 0

        Ap = (Ac / 2 + Ad)
        Am = (Ac / 2 - Ad)

        if n3 >= 0:
            mna._C[m, n3] -= Ap
        if n4 >= 0:
            mna._C[m, n4] -= Am

    def _kill(self):
        newopts = self.opts.copy()
        newopts.strip_current_labels()
        newopts.strip_labels()

        return self._netmake_W(opts=newopts)


class E(VCVS):
    pass


class Eopamp(DependentSource):
    """Operational amplifier"""

    extra_argnames = ('Ac', 'Ro')
    is_opamp = True

    def _expand(self):

        Ad, Ac, Ro = self.args

        Roval = expr(Ro)

        if Roval == 0:
            onode = self.relnodes[0]
        else:
            onode = self._dummy_node()

        opts = self.opts.copy()
        # If opamp drawn to right, VCVS needs to be drawn down and so on
        # FIXME: this needs more work
        if 'right' in opts:
            opts.remove('right')
            opts.add('down')

        vcvs = self._netmake_expand('E',
                                    nodes=(onode, self.relnodes[1],
                                           self.relnodes[2], self.relnodes[3]),
                                    args=(Ad, Ac), opts=opts)
        if Roval == 0:
            return vcvs

        rout = self._netmake_expand('R', nodes=(onode, self.relnodes[0]),
                                    args=(Ro, ))

        return vcvs + '\n' + rout + '\n'

    def _stamp(self, mna):
        raise RuntimeError('Internal error, component not expanded')


class Efdopamp(DependentSource):
    """Fully differential opamp"""

    extra_argnames = ('Ac')
    is_opamp = True

    def _expand(self):

        Ad, Ac = self.args
        Ad = '{%s / 2}' % Ad

        opampp = self._netmake_expand('Ep',
                                      nodes=(self.relnodes[0],
                                             self.relnodes[4],
                                             'opamp',
                                             self.relnodes[2],
                                             self.relnodes[3]),
                                      args=(Ad, Ac))
        opampm = self._netmake_expand('Em',
                                      nodes=(self.relnodes[4],
                                             self.relnodes[1],
                                             'opamp',
                                             self.relnodes[2],
                                             self.relnodes[3]),
                                      args=(Ad, '-' + Ac))

        return opampp + '\n' + opampm + '\n'

    def _stamp(self, mna):
        raise RuntimeError('Internal error, component not expanded')


class Einamp(DependentSource):
    """Instrumentation amplifier"""

    extra_argnames = ('Ac', 'Rf')
    is_opamp = True

    def _expand(self):

        Ad, Ac, Rf = self.args

        cpts = []
        node7 = self._dummy_node()
        node8 = self._dummy_node()

        cpts.append(self._netmake_expand('Ep',
                                         nodes=(node7, '0', 'opamp',
                                                self.relnodes[2],
                                                self.relnodes[4]),
                                         args=(Ad, )))
        cpts.append(self._netmake_expand('Em',
                                         nodes=(node8, '0', 'opamp',
                                                self.relnodes[3], self.relnodes[5]),
                                         args=(Ad, )))
        # This is an ideal differential amplifier with differential gain Ad=1.
        # The common-mode gain Ac is small, ideally 0.
        cpts.append(self._netmake_expand('Ed',
                                         nodes=(self.relnodes[0], self.relnodes[1], 'opamp',
                                                node7, node8), args=('1', Ac)))
        cpts.append(self._netmake_expand('Rfp',
                                         nodes=(self.relnodes[4], node7), args=(Rf, )))
        cpts.append(self._netmake_expand('Rfm',
                                         nodes=(self.relnodes[5], node8), args=(Rf, )))
        return '\n'.join(cpts)

    def _stamp(self, mna):
        raise RuntimeError('Internal error, component not expanded')


class CCCS(DependentSource):
    """CCCS"""

    need_control_current = True
    is_current_controlled = True

    def check(self):

        if self.args[0] == self.name:
            warn('CCCS controlled by its own current for %s' % self)

    def _stamp(self, mna):

        # The positive control current flows into the positive input
        # of the controlling component.

        # This fails if have a control component in parallel
        # with a voltage source.

        cname = self.args[0]
        ccpt = self.cct.elements[cname]

        if not ccpt.is_voltage_source:
            raise ValueError('The controlling component for %s must be a voltage souce' % self)

        n1, n2 = mna._cpt_node_indexes(self)
        m = mna._branch_index(cname)
        F = ConstantDomainExpression(self.args[1]).sympy

        if n1 >= 0:
            mna._B[n1, m] += F
        if n2 >= 0:
            mna._B[n2, m] -= F

    def _kill(self):
        newopts = self.opts.copy()
        newopts.strip_voltage_labels()
        newopts.strip_labels()

        return self._netmake_O(opts=newopts)


class FB(Misc):
    """Ferrite bead"""
    pass


class VCCS(DependentSource):
    """VCCS"""

    is_voltage_controlled = True

    def _stamp(self, mna):
        n1, n2, n3, n4 = mna._cpt_node_indexes(self)
        G = ConstantDomainExpression(self.args[0]).sympy

        if n1 >= 0 and n3 >= 0:
            mna._G[n1, n3] -= G
        if n1 >= 0 and n4 >= 0:
            mna._G[n1, n4] += G
        if n2 >= 0 and n3 >= 0:
            mna._G[n2, n3] += G
        if n2 >= 0 and n4 >= 0:
            mna._G[n2, n4] -= G

    def _kill(self):
        newopts = self.opts.copy()
        newopts.strip_voltage_labels()
        newopts.strip_labels()

        return self._netmake_O(opts=newopts)


class GY(Dummy):
    """Gyrator"""

    need_branch_current = True
    need_extra_branch_current = True

    def _stamp(self, mna):

        n1, n2, n3, n4 = mna._cpt_node_indexes(self)
        m1 = mna._branch_index(self.name + 'X')
        m2 = mna._cpt_branch_index(self)

        # m1 is the input branch
        # m2 is the output branch
        # GY.I gives the current through the output branch

        # Could generalise to have different input and output
        # impedances, Z1 and Z2, but if Z1 != Z2 then the device is
        # not passive.

        # V2 = -I1 Z2     V1 = I2 Z1
        # where V2 = V[n1] - V[n2] and V1 = V[n3] - V[n4]

        Z1 = ConstantDomainExpression(self.args[0]).sympy
        Z2 = Z1

        if n1 >= 0:
            mna._B[n1, m2] += 1
            mna._C[m1, n1] += 1
        if n2 >= 0:
            mna._B[n2, m2] -= 1
            mna._C[m1, n2] -= 1
        if n3 >= 0:
            mna._B[n3, m1] += 1
            mna._C[m2, n3] += 1
        if n4 >= 0:
            mna._B[n4, m1] -= 1
            mna._C[m2, n4] -= 1

        mna._D[m1, m1] += Z2
        mna._D[m2, m2] -= Z1


class CCVS(DependentSource):
    """CCVS"""

    need_branch_current = True
    need_control_current = True
    is_current_controlled = True

    def _stamp(self, mna):
        n1, n2 = mna._cpt_node_indexes(self)
        m1 = mna._cpt_branch_index(self)

        if n1 >= 0:
            mna._B[n1, m1] += 1
            mna._C[m1, n1] += 1
        if n2 >= 0:
            mna._B[n2, m1] -= 1
            mna._C[m1, n2] -= 1

        cname = self.args[0]
        m2 = mna._branch_index(cname)
        H = ConstantDomainExpression(self.args[1]).sympy
        mna._D[m1, m2] -= H

        ccpt = self.cct.elements[cname]
        if ccpt.is_voltage_source:
            return
        # Controlling node indices
        n3, n4 = [mna._node_index(name) for name in ccpt.node_names[0:2]]

        if n3 >= 0:
            mna._B[n3, m2] += 1
            mna._C[m2, n3] += 1
        if n4 >= 0:
            mna._B[n4, m2] -= 1
            mna._C[m2, n4] -= 1

    def _kill(self):
        newopts = self.opts.copy()
        newopts.strip_current_labels()
        newopts.strip_labels()

        return self._netmake_O(opts=newopts)


class I(IndependentSource):

    add_parallel = True

    def _select(self, kind=None):
        """Select domain kind for component."""
        return self._netmake(args=self.cpt.Isc.netval(kind),
                             ignore_keyword=True)

    def _kill(self):
        newopts = self.opts.copy()
        newopts.strip_voltage_labels()
        newopts.strip_labels()

        return self._netmake_O(opts=newopts)

    def _stamp(self, mna):

        n1, n2 = mna._cpt_node_indexes(self)

        I = self.Isc.sympy

        if n1 >= 0:
            mna._Is[n1] += I
        if n2 >= 0:
            mna._Is[n2] -= I

    def _ss_model(self):
        return self._netmake(args=self.cpt.isc, ignore_keyword=True)

    def _s_model(self, kind):
        return self._netmake(args=self.Isc.laplace(), ignore_keyword=True)

    def _pre_initial_model(self):

        return self._netmake(args=self.cpt.Isc.pre_initial_value())


class K(Dummy):

    is_mutual_coupling = True

    def __init__(self, cct, namespace, name, cpt_type, cpt_id, string,
                 opts_string, nodes, keyword, *args):

        self.Lname1 = args[0]
        self.Lname2 = args[1]
        super(K, self).__init__(cct, namespace, name,
                                cpt_type, cpt_id, string,
                                opts_string, nodes, keyword, *args)

    def _stamp(self, mna):
        from .sym import ssym

        if mna.kind == 'dc':
            return

        if mna.kind in ('t', 'time'):
            raise RuntimeError('Should not be evaluating mutual inductance in'
                               ' time domain')

        L1 = self.Lname1
        L2 = self.Lname2
        K = self.cpt.K

        ZL1 = mna.cct.elements[L1].Z.sympy
        ZL2 = mna.cct.elements[L2].Z.sympy

        if mna.kind in ('s', 'ivp', 'laplace'):
            # FIXME, generalise for other domains...
            ZM = K.sympy * sym.sqrt(ZL1 * ZL2 / ssym**2) * ssym
        else:
            ZM = K.sympy * sym.sqrt(ZL1 * ZL2)

        m1 = mna._branch_index(L1)
        m2 = mna._branch_index(L2)

        mna._D[m1, m2] += -ZM
        mna._D[m2, m1] += -ZM


class L(RLC):

    need_branch_current = True
    is_reactive = True
    add_series = True
    extra_argnames = ('i0', )

    def _r_model(self):

        dummy_node = self._dummy_node()
        opts = self.opts.copy()

        # Use Thevenin model.  This will require the current through
        # the voltage source to be explicitly computed.

        Req = 'R%seq' % self.name
        Veq = 'V%seq' % self.name

        opts.strip_voltage_labels()
        rnet = self._netmake_variant('R', suffix='eq',
                                     nodes=(
                                         self.relnodes[0], dummy_node),
                                     args=Req, opts=opts)

        opts.strip_current_labels()
        vnet = self._netmake_variant('V', suffix='eq',
                                     nodes=(dummy_node,
                                            self.relnodes[1]),
                                     args=('dc', Veq), opts=opts)

        # TODO: the voltage labels should be added across an
        # open-circuit object.

        return rnet + '\n' + vnet

    @property
    def I0(self):
        """Initial current (for capacitors only)."""

        if self.cct.kind == 'ivp' and self.cpt.has_ic:
            return current(self.cpt.i0 / s)
        return current(0)

    @property
    def L(self):
        return self.cpt.L

    def _kill(self):
        """Kill implicit sources due to initial conditions."""
        return self.netmake(args=self.args[0])

    def _initialize(self, ic):
        """Change initial condition to ic."""
        return self._netmake(args=(self.args[0], ic))

    def _stamp(self, mna):

        # This formulation adds the inductor current to the unknowns

        n1, n2 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n1 >= 0:
            mna._B[n1, m] = 1
            mna._C[m, n1] = 1
        if n2 >= 0:
            mna._B[n2, m] = -1
            mna._C[m, n2] = -1

        if mna.kind == 'dc':
            Z = 0
        else:
            Z = self.Z.sympy

        mna._D[m, m] += -Z

        if mna.kind == 'ivp' and self.cpt.has_ic:
            V = self.Voc.sympy
            mna._Es[m] += V

    def _pre_initial_model(self):

        return self._netmake_variant('I', args=self.cpt.i0)

    def _ss_model(self):
        # Perhaps mangle name to ensure it does not conflict
        # with another current source?
        return self._netmake_variant('I_', args='-i_%s(t)' % self.relname)

    def sympify(self):
        """Return component with numerical values removed."""

        if self.has_ic:
            return self._netmake(args=self.argnames)

        return self._netmake(args=[])

class O(Dummy):
    """Open circuit"""

    is_open_circuit = True

    @property
    def I(self):
        return SuperpositionCurrent(0)

    @property
    def i(self):
        return SuperpositionCurrent(0)(t)


class P(Dummy):
    """Port"""

    is_port = True

    @property
    def I(self):
        return SuperpositionCurrent(0)

    @property
    def i(self):
        return SuperpositionCurrent(0)(t)


class R(RC):

    add_series = True

    def _r_model(self):
        return self._copy()


class NR(R):

    add_series = True

    def _r_model(self):
        return self._copy()


class RV(RC):

    def _stamp(self, mna):

        n1, n2, n3 = mna._cpt_node_indexes(self)

        R = expr(self.args[0]).sympy
        a = expr(self.args[1]).sympy

        Y1 = 1 / (R * (1 - a))
        Y2 = 1 / (R * a)

        if n1 >= 0 and n3 >= 0:
            mna._G[n1, n3] -= Y1
            mna._G[n3, n1] -= Y1
        if n1 >= 0:
            mna._G[n1, n1] += Y1
        if n3 >= 0:
            mna._G[n3, n3] += Y1

        if n3 >= 0 and n2 >= 0:
            mna._G[n3, n2] -= Y2
            mna._G[n2, n3] -= Y2
        if n3 >= 0:
            mna._G[n3, n3] += Y2
        if n2 >= 0:
            mna._G[n2, n2] += Y2

class SPpp(Dummy):

    need_branch_current = True

    def _stamp(self, mna):
        n1, n2, n3 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n3 >= 0:
            mna._B[n3, m] += 1
            mna._C[m, n3] += 1

        if n1 >= 0:
            mna._C[m, n1] -= 1
        if n2 >= 0:
            mna._C[m, n2] -= 1


class SPpm(Dummy):

    need_branch_current = True

    def _stamp(self, mna):
        n1, n2, n3 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n3 >= 0:
            mna._B[n3, m] += 1
            mna._C[m, n3] += 1

        if n1 >= 0:
            mna._C[m, n1] -= 1
        if n2 >= 0:
            mna._C[m, n2] += 1


class SPppp(Dummy):

    need_branch_current = True

    def _stamp(self, mna):
        n1, n2, n3, n4 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n3 >= 0:
            mna._B[n3, m] += 1
            mna._C[m, n3] += 1

        if n1 >= 0:
            mna._C[m, n1] -= 1
        if n2 >= 0:
            mna._C[m, n2] -= 1
        if n4 >= 0:
            mna._C[m, n4] -= 1


class SPpmm(Dummy):

    need_branch_current = True

    def _stamp(self, mna):
        n1, n2, n3, n4 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n3 >= 0:
            mna._B[n3, m] += 1
            mna._C[m, n3] += 1

        if n1 >= 0:
            mna._C[m, n1] -= 1
        if n2 >= 0:
            mna._C[m, n2] += 1
        if n4 >= 0:
            mna._C[m, n4] += 1


class SPppm(Dummy):

    need_branch_current = True

    def _stamp(self, mna):
        n1, n2, n3, n4 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n3 >= 0:
            mna._B[n3, m] += 1
            mna._C[m, n3] += 1

        if n1 >= 0:
            mna._C[m, n1] -= 1
        if n2 >= 0:
            mna._C[m, n2] -= 1
        if n4 >= 0:
            mna._C[m, n4] += 1


class SW(TimeVarying):
    """Switch"""

    is_switch = True

    def _replace_switch(self, t, before=False):
        """Replace switch with open-circuit or short-circuit
        using specified time `t`."""

        kind = self.__class__.__name__

        active_time = expr(self.args[0])

        if before:
            active = expr(t) < active_time
        else:
            active = expr(t) >= active_time

        if kind in ('SW', 'SWno', 'SWpush'):
            if active:
                return self._netmake_W()
            return self._netmake_O()
        elif kind in ('SWnc', ):
            if active:
                return self._netmake_O()
            return self._netmake_W()
        elif kind in ('SWspdt', ):

            opts = self.opts.copy()
            opts.add('nosim')
            if 'l' not in opts:
                # Remove label
                opts.add('l=')

            wopts = self.opts.copy()
            wopts.add('ignore')

            if active:
                if 'mirror' in opts:
                    opts.remove('mirror')
                else:
                    opts.add('mirror')
            net = self._netmake_opts(opts)

            if active ^ ('mirror' in self.opts):
                return net + '\n' + self._netmake_W(nodes=(self.relnodes[0],
                                                           self.relnodes[2]),
                                                    opts=wopts)
            return net + '\n' + self._netmake_W(nodes=(self.relnodes[0],
                                                       self.relnodes[1]),
                                                opts=wopts)

        else:
            raise RuntimeError('Internal error, unhandled switch %s' % self)


class TF(Cpt):
    """Transformer"""

    need_branch_current = True
    is_transformer = True

    def _stamp(self, mna):

        n1, n2, n3, n4 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n1 >= 0:
            mna._B[n1, m] += 1
            mna._C[m, n1] += 1
        if n2 >= 0:
            mna._B[n2, m] -= 1
            mna._C[m, n2] -= 1

        # Voltage gain = 1 / a where a = N_1 / N_2
        # is the turns-ratio.
        T = self.cpt.alpha.sympy

        if n3 >= 0:
            mna._B[n3, m] -= T
            mna._C[m, n3] -= T
        if n4 >= 0:
            mna._B[n4, m] += T
            mna._C[m, n4] += T


class TFtap(Cpt):
    """Tapped transformer"""

    def _stamp(self, mna):
        raise NotImplementedError(
            'Cannot analyse tapped transformer %s' % self)


class TL(Cpt):
    """Transmission line"""

    is_reactive = True
    need_branch_current = True

    def _stamp(self, mna):

        if mna.kind not in ('s', 'dc'):
            raise ValueError(
                'Only Laplace or DC domains currently supported for TL')

        cpt = self.cpt

        m = mna._cpt_branch_index(self)
        n4, n3, n2, n1 = mna._cpt_node_indexes(self)

        # TODO, tweak values if doing phasor analysis

        if mna.kind == 'dc':
            A11 = 1
            A12 = 0
            A21 = 0
            A22 = 1
        else:
            A11 = cpt.A11.sympy
            A12 = cpt.A12.sympy
            A21 = cpt.A21.sympy
            A22 = cpt.A22.sympy

        # This stamp is the same as an A twoport.
        if n1 >= 0:
            if n3 >= 0:
                mna._G[n1, n3] += A21
            if n4 >= 0:
                mna._G[n1, n4] -= A21
            mna._B[n1, m] += A22

        if n2 >= 0:
            if n3 >= 0:
                mna._G[n2, n3] -= A21
            if n4 >= 0:
                mna._G[n2, n4] += A21
            mna._B[n2, m] -= A22

        if n3 >= 0:
            mna._B[n3, m] -= 1

        if n4 >= 0:
            mna._B[n4, m] += 1

        if n1 >= 0:
            mna._C[m, n1] -= 1

        if n2 >= 0:
            mna._C[m, n2] += 1

        if n3 >= 0:
            mna._C[m, n3] += A11

        if n4 >= 0:
            mna._C[m, n4] -= A11

        mna._D[m, m] += A12


class Cable(Cpt):
    """Cable"""

    equipotential_nodes = (('in+', 'out+'), ('in-', 'out-'), ('in', 'out'),
                           ('ignd', 'ognd', 'b', 't'), ('mid', 'out'))

    def _stamp(self, mna):
        pass


class TP(Misc):
    """Two port"""

    # TODO
    pass


class TPCpt(Cpt):
    pass


class TPA(TPCpt):
    """A-parameter two port"""

    need_branch_current = True

    def _stamp(self, mna):

        cpt = self.cpt
        if cpt.V1a != 0 or cpt.I1a != 0:
            raise ValueError('Sources not supported yet for %s' % self)

        m = mna._cpt_branch_index(self)
        n4, n3, n2, n1 = mna._cpt_node_indexes(self)
        A11, A12, A21, A22 = cpt.A11.sympy, cpt.A12.sympy, cpt.A21.sympy, cpt.A22.sympy

        if n1 >= 0:
            if n3 >= 0:
                mna._G[n1, n3] += A21
            if n4 >= 0:
                mna._G[n1, n4] -= A21
            mna._B[n1, m] += A22

        if n2 >= 0:
            if n3 >= 0:
                mna._G[n2, n3] -= A21
            if n4 >= 0:
                mna._G[n2, n4] += A21
            mna._B[n2, m] -= A22

        if n3 >= 0:
            mna._B[n3, m] -= 1

        if n4 >= 0:
            mna._B[n4, m] += 1

        if n1 >= 0:
            mna._C[m, n1] -= 1

        if n2 >= 0:
            mna._C[m, n2] += 1

        if n3 >= 0:
            mna._C[m, n3] += A11

        if n4 >= 0:
            mna._C[m, n4] -= A11

        mna._D[m, m] += A12


class TPB(TPA):
    """B-parameter two port"""

    def _stamp(self, mna):

        if self.cpt.V2b != 0 or self.cpt.I2b != 0:
            raise ValueError('Sources not supported yet for %s' % self)

        super(TPB, self)._stamp(mna)


class TPG(TPA):
    """G-parameter two port"""

    # TODO, create G stamp directly

    def _stamp(self, mna):

        if self.cpt.I1g != 0 or self.cpt.V2g != 0:
            raise ValueError('Sources not supported yet for %s' % self)

        super(TPG, self)._stamp(mna)


class TPH(TPA):
    """H-parameter two port"""

    # TODO, create H stamp directly

    def _stamp(self, mna):

        if self.cpt.V1h != 0 or self.cpt.I2h != 0:
            raise ValueError('Sources not supported yet for %s' % self)

        super(TPH, self)._stamp(mna)


class TPY(TPCpt):
    """Y-parameter two port"""

    def _stamp(self, mna):

        cpt = self.cpt
        if cpt.I1y != 0 or cpt.I2y != 0:
            raise ValueError('Sources not supported yet for %s' % self)

        n3, n4, n1, n2 = mna._cpt_node_indexes(self)
        Y11, Y12, Y21, Y22 = cpt.Y11.sympy, cpt.Y12.sympy, cpt.Y21.sympy, cpt.Y22.sympy

        if n1 >= 0:
            mna._G[n1, n1] += Y11
            if n2 >= 0:
                mna._G[n1, n2] -= Y11
            if n3 >= 0:
                mna._G[n1, n3] += Y12
            if n4 >= 0:
                mna._G[n1, n4] -= Y12

        if n2 >= 0:
            if n1 >= 0:
                mna._G[n2, n1] -= Y11
            mna._G[n2, n2] += Y11
            if n3 >= 0:
                mna._G[n2, n3] -= Y12
            if n4 >= 0:
                mna._G[n2, n4] += Y12

        if n3 >= 0:
            if n1 >= 0:
                mna._G[n3, n1] += Y21
            if n2 >= 0:
                mna._G[n3, n2] -= Y21
            mna._G[n3, n3] += Y22
            if n4 >= 0:
                mna._G[n3, n4] -= Y22

        if n4 >= 0:
            if n1 >= 0:
                mna._G[n4, n1] -= Y21
            if n2 >= 0:
                mna._G[n4, n2] += Y21
            if n3 >= 0:
                mna._G[n4, n3] -= Y22
            mna._G[n4, n4] += Y22


class TPZ(TPY):
    """Z-parameter two port"""

    # TODO, create Z stamp directly

    def _stamp(self, mna):

        if self.cpt.V1z != 0 or self.cpt.V2z != 0:
            raise ValueError('Sources not supported yet for %s' % self)

        super(TPZ, self)._stamp(mna)


class TR(Dummy):
    """Transfer function.  This is equivalent to a VCVS with the input and
    output referenced to node 0."""

    need_branch_current = True

    def _stamp(self, mna):
        n1, n2 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n2 >= 0:
            mna._B[n2, m] += 1
            mna._C[m, n2] += 1

        A = ConstantDomainExpression(self.args[0]).sympy

        if n1 >= 0:
            mna._C[m, n1] -= A


class V(IndependentSource):

    need_branch_current = True
    flip_branch_current = True
    add_series = True

    def _select(self, kind=None):
        """Select domain kind for component."""
        return self._netmake(args=self.cpt.Voc.netval(kind),
                             ignore_keyword=True)

    def _kill(self):
        newopts = self.opts.copy()
        newopts.strip_current_labels()
        newopts.strip_labels()

        return self._netmake_W(opts=newopts)

    def _stamp(self, mna):

        n1, n2 = mna._cpt_node_indexes(self)
        m = mna._cpt_branch_index(self)

        if n1 >= 0:
            mna._B[n1, m] += 1
            mna._C[m, n1] += 1
        if n2 >= 0:
            mna._B[n2, m] -= 1
            mna._C[m, n2] -= 1

        V = self.Voc.sympy
        mna._Es[m] += V

    def _ss_model(self):
        return self._netmake(args=self.cpt.voc, ignore_keyword=True)

    def _s_model(self, kind):
        return self._netmake(args=self.cpt.Voc.laplace(), ignore_keyword=True)

    def _pre_initial_model(self):

        return self._netmake(args=self.cpt.Voc.pre_initial_value())


class W(Dummy):
    """Wire"""

    is_wire = True

    @property
    def I(self):
        raise ValueError(
            'Cannot determine current through wire, use a 0 V voltage source')

    @property
    def i(self):
        raise ValueError(
            'Cannot determine current through wire, use a 0 V voltage source')


class XT(Misc):
    """Crystal"""

    is_reactive = True


class Y(RC):
    """Admittance"""

    is_reactive = True
    add_parallel = True


class Z(RC):
    """Impedance"""

    is_reactive = True
    add_series = True


classes = {}


def defcpt(name, base, docstring):

    if isinstance(base, str):
        base = classes[base]

    newclass = type(name, (base, ), {'__doc__': docstring})

    classes[name] = newclass


def make(classname, parent, namespace, name, cpt_type, cpt_id,
         string, opts_string, nodes, keyword, *args):

    # Create instance of component object
    newclass = classes[classname]

    cpt = newclass(parent, namespace, name, cpt_type, cpt_id, string,
                   opts_string, nodes, keyword, *args)

    return cpt


# Dynamically create classes.
defcpt('A', Ignore, 'Annotation')
defcpt('ADC', Misc, 'ADC')
defcpt('ANT', Misc, 'Antenna')

defcpt('BAT', V, 'Battery')
defcpt('BL', Misc, 'Block')

defcpt('D', NonLinear, 'Diode')
defcpt('DAC', Misc, 'DAC')
defcpt('Dled', 'D', 'LED')
defcpt('Dphoto', 'D', 'Photo diode')
defcpt('Dschottky', 'D', 'Schottky diode')
defcpt('Dtunnel', 'D', 'Tunnel diode')
defcpt('Dzener', 'D', 'Zener diode')

defcpt('Eamp', VCVS, 'Amplifier')

defcpt('F', CCCS, 'CCCS')
defcpt('FS', Misc, 'Fuse')

defcpt('G', VCCS, 'VCCS')

defcpt('H', CCVS, 'CCVS')

defcpt('sI', I, 's-domain current source')
defcpt('Isin', I, 'Sinusoidal current source')
defcpt('Istep', I, 'Step current source')
defcpt('Iac', I, 'AC current source')
defcpt('Idc', I, 'DC current source')
defcpt('Inoise', I, 'Noise current source')

defcpt('J', NonLinear, 'N JFET transistor')
defcpt('Jnjf', 'J', 'N JFET transistor')
defcpt('Jpjf', 'J', 'P JFET transistor')

defcpt('M', NonLinear, 'N MOSJFET transistor')
defcpt('Mnmos', 'M', 'N channel MOSJFET transistor')
defcpt('Mpmos', 'M', 'P channel MOSJFET transistor')
defcpt('MISC', Misc, 'Generic circuitikz bipole')
defcpt('MT', Misc, 'Motor')
defcpt('MX', Misc, 'Mixer')

defcpt('Q', NonLinear, 'NPN transistor')
defcpt('Qpnp', 'Q', 'PNP transistor')
defcpt('Qnpn', 'Q', 'NPN transistor')

# Could model if introduce MagneticCircuit class.
defcpt('REL', Misc, 'Reluctance')

defcpt('Sbox', Misc, 'Box shape')
defcpt('Scircle', Misc, 'Circle shape')
defcpt('Sellipse', Misc, 'Ellipse shape')
defcpt('Striangle', Misc, 'Triangle shape')
defcpt('SWno', SW, 'Normally open switch')
defcpt('SWnc', SW, 'Normally closed switch')
defcpt('SWpush', SW, 'Pushbutton switch')
defcpt('SWspdt', SW, 'SPDT switch')

defcpt('TFcore', TF, 'Transformer with core')
defcpt('TFtapcore', TFtap, 'Transformer with core')
defcpt('TLlossless', TL, 'Lossless transmission line')
defcpt('TVtriode', NonLinear, 'Triode')

defcpt('Uand', Logic, 'And gate')
defcpt('Ubuffer', Logic, 'Buffer')
defcpt('Upbuffer', Logic, 'Buffer with power supplies')
defcpt('Uinverter', Logic, 'Inverter')
defcpt('Upinverter', Logic, 'Inverter with power supplies')
defcpt('Uinamp', Misc, 'Instrumentation amplifier')
defcpt('Uisoamp', Misc, 'Isolated amplifier')
defcpt('Udiffamp', Misc, 'Differential amplifier')
defcpt('Udiffdriver', Misc, 'Differential driver')
defcpt('Ufdopamp', Misc, 'Fully differential opamp ')
defcpt('Uopamp', Misc, 'Opamp ')
defcpt('Uregulator', Misc, 'Regulator ')
defcpt('Uadc', Misc, 'ADC')
defcpt('Udac', Misc, 'DAC')
defcpt('Ubox', Misc, 'Box')
defcpt('Ucircle', Misc, 'Circle')
defcpt('Ubox4', Misc, 'Box')
defcpt('Ubox12', Misc, 'Box')
defcpt('Ucircle4', Misc, 'Circle')
defcpt('Uchip1313', Logic, 'General purpose chip')
defcpt('Uchip2121', Logic, 'General purpose chip')
defcpt('Uchip2222', Logic, 'General purpose chip')
defcpt('Uchip3131', Logic, 'General purpose chip')
defcpt('Uchip3333', Logic, 'General purpose chip')
defcpt('Uchip4141', Logic, 'General purpose chip')
defcpt('Uchip4444', Logic, 'General purpose chip')
defcpt('Uchip5555', Logic, 'General purpose chip')
defcpt('Uchip6666', Logic, 'General purpose chip')
defcpt('Uchip7777', Logic, 'General purpose chip')
defcpt('Uchip8181', Logic, 'General purpose chip')
defcpt('Uchip8888', Logic, 'General purpose chip')
defcpt('Udff', Misc, 'D flip-flop')
defcpt('Umux21', Logic, '2-1 multiplexer')
defcpt('Umux41', Logic, '4-1 multiplexer')
defcpt('Umux42', Logic, '4-2 multiplexer')
defcpt('Unand', Logic, 'Nand gate')
defcpt('Unor', Logic, 'Nor gate')
defcpt('Uor', Logic, 'Or gate')
defcpt('Ujkff', Misc, 'JK flip-flop')
defcpt('Urslatch', Misc, 'RS latch')
defcpt('Uxor', Logic, 'Xor gate')
defcpt('Uxnor', Logic, 'Xnor gate')
defcpt('sV', V, 's-domain voltage source')
defcpt('Vsin', V, 'Sinusoidal voltage source')
defcpt('Vstep', V, 'Step voltage source')
defcpt('Vac', V, 'AC voltage source')
defcpt('Vdc', V, 'DC voltage source')
defcpt('Vnoise', V, 'Noise voltage source')
defcpt('VM', O, 'Voltmeter')



# Mechanical analogue I (the mobility analogue) where
# force is equivalent to current and velocity is equivalent to
# voltage.  With this analogy Kirchhoff's current law is equivalent
# to D'alembert's law.
defcpt('m', C, 'Mass')
defcpt('k', L, 'Spring')
defcpt('r', R, 'Damper')

# Append classes defined in this module but not imported.
clsmembers = inspect.getmembers(module, lambda member: inspect.isclass(
    member) and member.__module__ == __name__)
for name, cls in clsmembers:
    classes[name] = cls
