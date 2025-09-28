"""
This module implements modified nodal analysis (MNA).

Copyright 2014--2025 Michael Hayes, UCECE
"""

from __future__ import division
from .assumptions import Assumptions
from .vector import Vector
from .matrix import Matrix, matrix_solve
from .sym import eps
from .expr import ExprDict, expr
from .voltage import Vtype
from .current import Itype, current_sign
from .systemequations import SystemEquations
import sympy as sym
from warnings import warn

# Note, all the maths is performed using sympy expressions and the
# values and converted to Expr when required.  This is more
# efficient and, more importantly, overcomes some of the wrapping
# problems which casues the is_real attribute to be dropped.


class Nodedict(ExprDict):

    def __getitem__(self, name):
        """Return node by name or number."""

        # If name is an integer, convert to a string.
        if isinstance(name, int):
            name = '%d' % name
        return super(Nodedict, self).__getitem__(name)


class Branchdict(ExprDict):
    pass


class MNA(object):
    """This class performs modified nodal analysis (MNA) on a netlist of
    components.  There are several variants:

    1. DC analysis if all the independent sources are DC.  The .V and .I
    methods return DC expressions with the dc assumption set.

    2. AC analysis if all the independent sources are AC.  The .V and .I
    methods return phasors.

    3. Initial value Laplace analysis if an L or C has an explicit
    initial value.  The .V and .I methods return s-domain expressions
    with no assumption sets; thus the time-domain results are only
    valid for t >= 0.

    4. General Laplace analysis.  If all the sources are causal and
    all the initial conditions are zero (explicitly or implicitly)
    then the time-domain results are causal.

    5. Noise analysis.

    Note, it is assumed that the user of this class uses superposition
    to solve problems with mixed independent sources, such as DC and
    AC.

    """

    def __init__(self, cct, solver_method):

        self.cct = cct
        self.kind = cct.kind
        self.solver_method = solver_method

        if cct.elements == {}:
            raise ValueError('No elements to analyse')

        # TODO: think this out.  When a circuit is converted
        # to a s-domain model we get Z (and perhaps Y) components.
        # We also lose the ability to determine the voltage
        # across a capacitor or inductor since they get split
        # into a Thevenin model and renamed.
        if hasattr(self, '_s_model'):
            raise RuntimeError('Cannot analyse s-domain model')

        # Determine which branch currents are needed.
        self.unknown_branch_currents = []
        self.extra_branch_currents = []

        for elt in self.cct.elements.values():
            if elt.need_branch_current:
                self.unknown_branch_currents.append(elt.name)
            if elt.need_extra_branch_current:
                self.unknown_branch_currents.append(elt.name + 'X')
                self.extra_branch_currents.append(elt.name + 'X')
            if elt.is_current_controlled:
                cname = elt.args[0]
                if cname not in self.cct.elements:
                    raise ValueError(
                        'Undefined controlling source %s for %s' % (cname, elt.name))
                if cname not in self.unknown_branch_currents:
                    self.unknown_branch_currents.append(cname)

        # Generate stamps.
        num_nodes = len(self.cct.node_list) - 1
        num_branches = len(self.unknown_branch_currents)

        self._G = sym.zeros(num_nodes, num_nodes)
        self._B = sym.zeros(num_nodes, num_branches)
        self._C = sym.zeros(num_branches, num_nodes)
        self._D = sym.zeros(num_branches, num_branches)

        self._Is = sym.zeros(num_nodes, 1)
        self._Es = sym.zeros(num_branches, 1)

        # Iterate over circuit elements and fill in matrices.
        for elt in self.cct.elements.values():
            if not elt.nosim:
                elt._stamp(self)

        # Augment the admittance matrix to form A matrix.
        self._A = self._G.row_join(self._B).col_join(self._C.row_join(self._D))
        # Augment the known current vector with known voltage vector
        # to form Z vector.
        self._Z = self._Is.col_join(self._Es)

    def _invalidate(self):
        for attr in ('_A', '_Vdict', '_Idict'):
            if hasattr(self, attr):
                delattr(self, attr)

    def _cpt_node_indexes(self, cpt):

        return [self._node_index(n) for n in cpt.node_names]

    def _cpt_branch_index(self, cpt):

        return self._branch_index(cpt.name)

    def _node_index(self, node):
        """Return node index; ground is -1"""
        return self.cct.node_list.index(self.cct.node_map[node]) - 1

    def _branch_index(self, cpt_name):

        try:
            index = self.unknown_branch_currents.index(cpt_name)
            return index
        except ValueError:
            raise ValueError(
                'Unknown component name %s for branch current' % cpt_name)

    def _failure_reasons(self):

        message = 'The MNA A matrix is not invertible for %s analysis:' % self.kind
        cct = self.cct
        if cct.nodes['0'].count == 0:
            return message + ' Nothing electrically connected to ground.'

        reasons = []
        components = cct.components

        if not cct.is_connected:
            reasons.append('The circuit graph is disjoint.')

            unreachable = cct.unreachable_nodes('0')
            if unreachable != []:
                reasons.append('There is no path to node 0 for nodes: ' + ', '.join(unreachable))
            return message + '\n    ' + '\n    '.join(reasons)

        if cct.kind == 'dc':
            reasons.append('Check there is a DC path between all nodes.')
        if components.transformers != []:
            reasons.append(
                'Check secondary of transformer is referenced to ground.')
        if len(components.capacitors) > 1:
            reasons.append('Check capacitors are not in series.')
        if components.voltage_sources != []:
            reasons.append('Check voltage source is not short-circuited.')
        if len(components.voltage_sources) > 1:
            reasons.append('Check for loop of voltage sources.')
        if components.current_sources != []:
            # Note, when determining impedance, a test current source
            # is added.  This test source should be ignored here.
            reasons.append('Check current source is not open-circuited.')
        if len(components.current_sources) > 1:
            reasons.append('Check for current sources in series.')

        return message + '\n    ' + '\n    '.join(reasons)

    def _solve(self):
        """Solve network.  This does not simplify the results."""

        if hasattr(self, '_Vdict'):
            return

        cct = self.cct

        if '0' not in cct.node_map:
            raise ValueError('No ground node specified.')

        solver_method = self.solver_method
        # Hack to overcome simplification of sqrt with noise circuits
        # if using LU solver. For example,
        # opamp-noninverting-amplifier-noise1.py
        if (solver_method in ('LU', 'GE') and isinstance(self.kind, str)
                and self.kind[0] == 'n'):
            # GE is faster but produces sqrt(x**2 + 2*x*y + y**2)
            # that SymPy does not realise is x + y.  This causes
            # a failure with test_noisy2.
            # LU suffers from similar problems and can make a dog's breakfast
            # ADJ seems robust but is slower than GE.
            solver_method = 'ADJ'

        # Solve for the nodal voltages
        try:
            results = matrix_solve(self._A, self._Z, method=solver_method)
        except ValueError:
            message = self._failure_reasons()
            raise ValueError(message)

        results = results.subs(cct.context.symbols)

        # Handle capacitors at DC by assuming an infinite resistance
        # in parallel.
        if results.has(eps):
            # Perhaps this should be lazily done if needed
            results = results.limit(eps, 0)

        branchdict = {}
        for elt in cct.elements.values():
            if elt.type in ('K', 'Cable') or elt.ignore:
                continue
            n1 = cct.node_map[elt.node_names[0]]
            n2 = cct.node_map[elt.node_names[1]]
            branchdict[elt.name] = (n1, n2)

        vtype = Vtype(self.kind)
        itype = Itype(self.kind)
        assumptions = Assumptions()
        if vtype.is_phasor_domain:
            assumptions.set('omega', self.kind)
        elif self.kind in ('s', 'ivp', 'transient'):
            assumptions.set('ac', cct.is_ac)
            assumptions.set('dc', cct.is_dc)
            assumptions.set('causal', cct.is_causal)
        elif isinstance(self.kind, str) and self.kind[0] == 'n':
            assumptions.set('nid', self.kind)

        # Create dictionary of node voltages
        self._Vdict = Nodedict()
        self._Vdict['0'] = vtype(0, **assumptions)
        for n in cct.nodes:
            index = self._node_index(n)
            if index >= 0:
                self._Vdict[n] = vtype(
                    results[index], **assumptions)
            else:
                self._Vdict[n] = vtype(0, **assumptions)

        num_nodes = len(cct.node_list) - 1

        # Create dictionary of branch currents through elements
        self._Idict = Branchdict()
        for m, key in enumerate(self.unknown_branch_currents):

            if key in self.extra_branch_currents:
                is_source = False
            else:
                is_source = cct.elements[key].is_source

            I = current_sign(results[m + num_nodes], is_source)
            self._Idict[key] = itype(I, **assumptions)

        # Calculate the branch currents.  These should be lazily
        # evaluated as required.
        for elt in cct.elements.values():
            if elt.type in ('R', 'NR', 'C', 'Y', 'Z'):
                n1 = cct.node_map[elt.node_names[0]]
                n2 = cct.node_map[elt.node_names[1]]
                V1, V2 = self._Vdict[n1], self._Vdict[n2]
                I = (V1.expr - V2.expr - elt.V0.expr) / elt.Z.expr
                self._Idict[elt.name] = itype(I, **assumptions)
            elif elt.type in ('I', ):
                I = current_sign(-elt.Isc, True)
                self._Idict[elt.name] = I

    @property
    def A(self):
        """Return A matrix for MNA"""

        ret = Matrix(self._A)

        # Could cache
        if ret.has(eps):
            # Should only do this after inverse...  It is more rigorous
            # if don't evaluate limit.
            ret = ret.limit(eps, 0)
        return ret

    @property
    def B(self):
        """Return B matrix for MNA"""

        return Matrix(self._B)

    @property
    def C(self):
        """Return C matrix for MNA"""

        return Matrix(self._C)

    @property
    def D(self):
        """Return D matrix for MNA"""

        return Matrix(self._D)

    @property
    def G(self):
        """Return G matrix for MNA"""

        return Matrix(self._G)

    @property
    def Z(self):
        """Return Z vector for MNA"""

        return Vector(self._Z)

    @property
    def E(self):
        """Return E vector for MNA"""

        return Vector(self._Es)

    @property
    def I(self):
        """Return I vector for MNA"""

        return Vector(self._Is)

    @property
    def X(self):
        """Return X vector (of unknowns) for MNA"""

        V = [self.cct.Vname('Vn%s' % node) for node in self.cct.node_list[1:]]
        I = [self.cct.Iname('I%s' % branch)
             for branch in self.unknown_branch_currents]
        return Vector(V + I)

    @property
    def Vdict(self):
        """Return dictionary of transform domain node voltages indexed by node
        name"""

        self._solve()
        return self._Vdict

    @property
    def Idict(self):
        """Return dictionary of transform domain branch currents indexed by
        component name"""

        self._solve()
        return self._Idict

    def matrix_equations(self, form='default', invert=False):
        """System of equations used to find the unknowns.

        Forms can be:
         A y = b
         b = A y
         Ainv b = y
         y = Ainv b

        If `invert` is True, evaluate the matrix inverse."""

        from .expr import delcapify

        sys = SystemEquations(self._A, self._Z, delcapify(self.X))
        return sys.format(form, invert)

    def equations(self, inverse=False):
        """System of equations used to find the unknowns.

        If inverse is True, evaluate the matrix inverse.

        This is for compatibility and is deprecated.  Use
        matrix_equations instead."""

        return self.matrix_equations(invert=inverse)
