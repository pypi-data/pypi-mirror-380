"""
This module implements the Lcapy Matrix class.

Copyright 2019--2025 Michael Hayes, UCECE
"""

import sympy as sym
from copy import copy
from .expr import expr, delcapify
from .sym import simplify
from .printing import pprint, latex, pretty
from .rcparams import rcParams
from warnings import warn


def msympify(expr):
    # If do nothing, will get a problem with matrices that
    # have mixed data types, e.g., A matrix.

    if isinstance(expr, Expr):
        # Bye bye Lcapy type information...
        return expr.sympy
    return sym.sympify(expr)


class Matrix(sym.Matrix):

    # Unlike numpy.ndarray, the sympy.Matrix runs all the elements
    # through _sympify, creating sympy objects and thus losing the
    # original type information and associated methods.  As a hack, we
    # try to wrap elements when they are read using __getitem__.  This
    # assumes that all the elements have the same type.  This is not
    # the case for A, B, G, and H two-port matrices.  This could be
    # handled by having another matrix to specify the type for each
    # element.  What's worse, is that calling _sympify on each element
    # creates different variables than what we are expecting.  For
    # example, the LaplaceDomainExpression s looks the same but gets
    # different attributes.  We prevent this by defining _sympify.

    # Unfortunately, as of SymPy-1.9, having non-SymPy quantities
    # for SymPy matrix elements is deprecated.   Having Lcapy quantities
    # as SymPy matrix elements almost works for many operations.

    # An alternative approach is for Lcapy to define its own Matrix
    # class, similar to the SymPy Matrix class but independent.  This
    # would store Lcapy quantities for each matrix element.  The
    # advantage is that different matrix classes are not required for
    # each domain.  The down-sides are that there is a divergence with
    # SymPy matrix behaviour and that many of the SymPy Matrix
    # operations need to be reimplemented or wrapped.  Wrapping is
    # easier but the units may be wrong, say with a matrix inverse
    # operation.

    # _sympify is called for each matrix element when a matrix is created.
    _sympify = staticmethod(msympify)

    def __new__(cls, *args, **kwargs):

        newargs = delcapify(args)
        return super(Matrix, cls).__new__(cls, *newargs, **kwargs)

    def __getitem__(self, key):

        # This wraps elements as an Expr.  It is called
        # for each element when a Matrix is printed.

        item = super(Matrix, self).__getitem__(key)

        # The following line is to handle slicing used
        # by the latex method.
        if isinstance(item, sym.Matrix):
            return item

        if hasattr(self, '_typewrap'):
            return self._typewrap(item)

        return expr(item, rational=False)

    def __repr__(self):
        """This is called by repr(expr).  It is used, e.g., when printing
        in the debugger."""

        s = self.__class__.__name__ + '(('

        rowreprs = []

        for r in range(self.rows):
            rowreprs.append(
                '(' + ', '.join([repr(elt) for elt in self[r, :]]) + ')')

        reprs = ',\n'.join(rowreprs)

        return s + reprs + '))'

    def _repr_pretty_(self, p, cycle):
        """This is used by jupyter notebooks to display an expression using
        unicode."""

        p.text(pretty(self))

    def _repr_latex_(self):
        """This is used by jupyter notebooks to display an expression using
        LaTeX markup.  However, this requires mathjax.  If this method
        is not defined, jupyter falls back on _repr__pretty_ which
        outputs unicode."""

        s = self.latex(mode='plain')
        return "$$%s$$" % s

    def _repr_png_(self):

        return None

    def _repr_svg_(self):

        return None

    def pprint(self):

        return pprint(self)

    def latex(self, **kwargs):

        return latex(self, **kwargs)

    def pdb(self):
        """Enter the python debugger."""

        import pdb
        pdb.set_trace()
        return self

    def canonical(self):

        return self

    # TODO. There is probably a cunning way to automatically handle
    # the following.

    def inv(self, method='default'):

        mat = self.sympy
        Minv = matrix_inverse(mat, method=method)

        return self.__class__(Minv)

    def det(self):

        return expr(super(Matrix, self).det())

    def discretize(self, method=None, alpha=0.5, drop_dt=False):

        def f(x):
            result = expr(x).discretize(method, alpha)
            if drop_dt:
                result = result.drop_dt()
            return result.sympy

        return self.applyfunc(f)

    def limit(self, var, value, dir='+'):

        def f(x): return expr(x).limit(var, value, dir)

        return self.applyfunc(f)

    def next_timestep(self):

        def f(x): return expr(x).next_timestep()

        return self.applyfunc(f)

    def norm(self):

        return expr(super(Matrix, self).norm())

    # TODO, either need to explicitly wrap methods or use some cunning
    # implicit method.

    def replace(self, query, value, map=False, simultaneous=True, exact=None):

        try:
            query = query.sympy
        except:
            pass

        try:
            value = value.sympy
        except:
            pass

        ret = super(Matrix, self).replace(
            query, value, map, simultaneous, exact)
        return self.__class__(ret)

    def rewrite(self, *args, **hints):

        def f(x): return expr(x).rewrite(*args, **hints).sympy
        return self.applyfunc(f)

    def simplify(self):
        """Simplify the elements of the matrix."""

        ret = self.copy()
        # The SymPy method does the simplification in-place.  It does
        # not return anything.
        super(Matrix, ret).simplify()
        return ret

    def subs(self, *args, **kwargs):
        """Substitute variables in expression, see sympy.subs for usage."""

        def f(x): return expr(x).subs(*args, **kwargs).sympy
        return self.applyfunc(f)

    @property
    def conj(self):
        """Complex conjugate; for compatilibility with Expr, conj is an attribute."""
        return self._new(self.rows, self.cols, [x.conj for x in self])

    @property
    def symbols(self):

        symbols = {}
        for elt in self:
            symbols.update(expr(elt).symbols)
        return symbols

    @property
    def sympy(self):

        return sym.Matrix(self.rows, self.cols, [x.sympy for x in self])

    @property
    def expr(self):
        return self.sympy

    @property
    def is_complex(self):

        for x in self:
            if x.is_complex:
                return True
        return False

    def evaluate(self, arg=None):
        """Evaluate matrix at arg.  `arg` may be a scalar.
        The result is a NumPy float or complex array.

        There can be only one or fewer undefined variables in the expression.
        This is replaced by `arg` and then evaluated to obtain a result.
        """

        from numpy import empty

        dtype = float
        if self.is_complex:
            dtype = complex
        result = empty((self.rows, self.cols), dtype=dtype)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j].evaluate(arg)
        return result

    @property
    def numpy(self):
        """Return NumPy array; not a NumPy matrix."""
        return self.evaluate()


def matrix(mat):
    """Create Lcapy Matrix from a SymPy Matrix.

    If a t symbol is found in an element a tMatrix object is created.
    If a s symbol is found in an element an sMatrix object is created.

    """

    from .sym import tsym, ssym
    from .smatrix import LaplaceDomainMatrix
    from .tmatrix import TimeDomainMatrix

    elt = mat[0]
    try:
        elt = elt[0]
    except:
        pass

    if elt.has(tsym):
        return TimeDomainMatrix(mat)
    elif elt.has(ssym):
        return LaplaceDomainMatrix(mat)
    else:
        return mat


def matrix_inverse(M, method='default'):

    N = M.shape[0]
    if N >= 10:
        warn("""
This may take a while...  A symbolic matrix inversion is O(%d^3) for a matrix
of size %dx%d""" % (N, N, N))

    if method == 'default':
        method = rcParams['sympy.matrix.inverse']

    if method == 'GE':
        try:
            from sympy.matrices import dotprodsimp

            # GE loses it without this assumption.  Well with
            # sympy-1.6.2 and the master version, GE still loses it
            # with a poor pivot.
            with dotprodsimp(False):
                return M.inv(method='GE')
        except:
            return M.inv(method='GE')

    elif method == 'DM':
        # This is experimental and requires a new version of sympy.
        # It only works for rational function fields but
        # fails for polynomial rings.  The latter can be handled
        # by converting it to a field.
        try:
            return M.to_DM().to_field().inv().to_Matrix()
        except:
            try:
                from sympy.polys.domainmatrix import DomainMatrix
                dM = DomainMatrix.from_list_sympy(
                    *M.shape, rows=M.tolist()).to_field()
                return dM.inv().to_Matrix()
            except:
                method = 'ADJ'

    return M.inv(method=method)


def matrix_solve(M, b, method='default'):

    if method == 'default':
        method = rcParams['sympy.solver']

    if method == 'DM':
        try:
            sol_num, sol_den = M.to_DM().solve_den(b.to_DM())
            x = (sol_num.to_field() / sol_den).to_Matrix()
        except:
            # Fallback
            Minv = matrix_inverse(M, method)
            x = Minv * b
        return x
    else:
        N = M.shape[0]
        if N >= 10:
            warn("""
            This may take a while...  Solving a system of equations is O(%d^3) for a matrix of size %dx%d""" % (N, N, N))
        x = M.solve(b, method=method)
    return x

    def canonical(self):

        return self.applyfunc(self._typewrap.canonical)

    def general(self):

        return self.applyfunc(self._typewrap.general)

    def mixedfrac(self):

        return self.applyfunc(self._typewrap.mixedfrac)

    def partfrac(self):

        return self.applyfunc(self._typewrap.partfrac)

    def timeconst(self):

        return self.applyfunc(self._typewrap.timeconst)

    def ZPK(self):

        return self.applyfunc(self._typewrap.ZPK)


from .expr import Expr, expr  # nopep8
