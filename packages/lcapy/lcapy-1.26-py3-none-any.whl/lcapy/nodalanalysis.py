"""This module performs nodal analysis.  It is primarily for showing
the equations rather than for evaluating them.

Copyright 2019--2023 Michael Hayes, UCECE

"""

from .circuitgraph import CircuitGraph
from .expr import equation, ExprTuple
from .systemequations import SystemEquations
import sympy as sym
from warnings import warn

__all__ = ('NodalAnalysis', )


class NodalAnalysis(object):
    """This is for nodal analysis.

    >>> from lcapy import Circuit, NodalAnalysis
    >>> cct = Circuit('''
    ... V1 1 0 {u(t)}; down
    ... R1 1 2; right=2
    ... L1 2 3; down=2
    ... W1 0 3; right
    ... W 1 5; up
    ... W 2 6; up
    ... C1 5 6; right=2
    ...''')

    To perform nodal analysis in the Laplace domain:

    >>> na = NodalAnalysis(cct.laplace())

    To display the equations found by applying KCL at each node:

    >>> na.nodal_equations().pprint()

    To display the system of equations (in matrix form) that needs to
    be solved:

    >>> na.matrix_equations().pprint()

    This only works for dc, ac, or laplace domains.  For example,

    >>> NodalAnalysis(cct.laplace()).matrix_equations().pprint()

    """

    @classmethod
    def from_circuit(cls, cct, node_prefix=''):

        return cls(cct, node_prefix)

    def __init__(self, cct, node_prefix=''):
        """`cct` is a netlist
        `node_prefix` can be used to avoid ambiguity between
        component voltages and node voltages."""

        self.cct = cct
        self.cg = CircuitGraph.from_circuit(cct)

        self.kind = cct.kind
        if cct.kind == 'super':
            source_groups = cct.independent_source_groups()

            if len(source_groups) > 1:
                self.cct = self.cct.time()
                self.kind = 'time'
            elif len(source_groups) == 1:
                self.kind = list(source_groups)[0]

        self.node_prefix = node_prefix

        self._unknowns = self._make_unknowns()

        self._check_unknowns()

        self._y = matrix(
            [val for key, val in self._unknowns.items() if key != '0'])

        self._equations = self._make_equations()

    @property
    def nodes(self):

        return self.cg.nodes

    def _make_unknowns(self):

        # Determine node voltage variables.
        unknowns = ExprDict()

        # cct.node_list is sorted alphabetically
        for node in self.cct.node_list:
            if node.startswith('*'):
                continue
            if node == '0':
                unknowns[node] = 0
            else:
                unknowns[node] = Vname('V%s%s' % (self.node_prefix, node),
                                       self.kind)

        return unknowns

    def _check_unknowns(self):
        """Look for nodal voltage names that are the same as a voltage
        source name."""

        unknowns = []
        for u in self._unknowns.values():
            if u == 0:
                continue
            unknowns.append(u.name)

        conflicts = []
        for src in self.cct.independent_sources:
            if src in unknowns:
                conflicts.append(src)
        if conflicts != []:
            warn('Have nodal voltage name conflict with sources for %s; suggest using node_prefix' %
                 ', '.join(conflicts))

    def _make_equations(self):

        equations = {}
        for node in self.nodes:
            if node == '0':
                continue
            # Ignore dummy nodes
            if node.startswith('*'):
                continue

            voltage_sources = []
            for elt in self.cg.connected_cpts(node):
                if elt.type == 'V':
                    voltage_sources.append(elt)
                elif elt.is_dependent_source:
                    raise ValueError('Dependent sources not handled yet')

            if voltage_sources != []:
                elt = voltage_sources[0]
                n1 = self.cg.node_map[elt.node_names[0]]
                n2 = self.cg.node_map[elt.node_names[1]]

                V = elt.cpt.voltage_equation(0, self.kind)

                lhs, rhs = self._unknowns[n1], self._unknowns[n2] + V

            else:
                result = Itype(self.kind)(0)
                for elt in self.cg.connected_cpts(node):
                    if len(elt.node_names) < 2:
                        raise ValueError('Elt %s has too few nodes' % elt)
                    n1 = self.cg.node_map[elt.node_names[0]]
                    n2 = self.cg.node_map[elt.node_names[1]]
                    if node == n1:
                        pass
                    elif node == n2:
                        n1, n2 = n2, n1
                    else:
                        raise ValueError(
                            'Component %s does not have node %s' % (elt, node))
                    result += elt.cpt.current_equation(
                        self._unknowns[n1] - self._unknowns[n2], self.kind)
                lhs, rhs = result, expr(0)

            equations[node] = (lhs, rhs)

        return equations

    def equations_dict(self):
        """Return dictionary of equations keyed by node name."""

        equations_dict = ExprDict()
        for node, (lhs, rhs) in self._equations.items():
            equations_dict[node] = equation(lhs, rhs)

        return equations_dict

    def nodal_equations(self):
        """Return the equations found by applying KCL at each node.  This is a
        directory of equations keyed by the node name."""

        return self.equations_dict()

    def _analyse(self):

        if self.kind in ('t', 'time'):
            raise ValueError(
                'Cannot put time domain equations into matrix form.  '
                'Convert to dc, ac, or laplace domain first.')

        subsdict = {}
        for node, v in self._unknowns.items():
            if v == 0:
                continue
            subsdict[v.expr] = 'X_X' + node

        exprs = []
        for node, (lhs, rhs) in self._equations.items():
            lhs = lhs.subs(subsdict).expr.expand()
            rhs = rhs.subs(subsdict).expr.expand()
            exprs.append(lhs - rhs)

        y = []
        for y1 in self._y:
            y.append(y1.subs(subsdict).expr)

        A, b = sym.linear_eq_to_matrix(exprs, *y)
        y = [y1.expr for y1 in self._y]
        return SystemEquations(A, b, y)

    @property
    def A(self):
        """Return A matrix where A y = b."""

        if not hasattr(self, '_sys'):
            self._sys = self._analyse()
        return matrix(self._sys.A)

    @property
    def b(self):
        """Return b vector where A y = b."""

        if not hasattr(self, '_sys'):
            self._sys = self._analyse()
        return matrix(self._sys.b)

    @property
    def y(self):
        """Return y vector where A y = b."""
        return self._y

    def matrix_equations(self, form='default', invert=False):
        """Return the equations in matrix form.

        Forms can be:
         'default'
         'A y = b'
         'b = A y'
         'Ainv b = y'
         'y = Ainv b'

        If `invert` is True, evaluate the matrix inverse."""

        if not hasattr(self, '_sys'):
            self._sys = self._analyse()
        return self._sys.format(form, invert)

    @property
    def unknowns(self):
        """Return tuple of the unknown voltages"""

        return ExprTuple(self.y)

    def solve_laplace(self):
        """Determine the unknown voltages using Laplace transforms and
        return as a dict"""

        from .sexpr import s

        unknowns = self.unknowns(s)
        return self.nodal_equations()(s).solve(unknowns)

    def pdb(self):
        """Enter the python debugger."""

        import pdb
        pdb.set_trace()
        return self


from .expr import ExprDict, expr  # nopep8
from .voltage import Vname  # nopep8
from .current import Itype  # nopep8
from .matrix import matrix  # nopep8
