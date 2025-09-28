"""This module handles sequences.

Copyright 2020--2023 Michael Hayes, UCECE

"""

from .expr import ExprList, expr
from .seqdomain import SeqDomain
from .utils import isiterable
from .assumptions import Assumptions

# Perhaps subclass numpy ndarray?  But then could not have symbolic
# elements in the sequence.


def parse_seq_str(s):

    if s.startswith('{'):
        if not s.endswith('}'):
            raise ValueError('Mismatched braces for %s' % s)
        s = s[1:-1]

    parts = s.split(',')
    N = len(parts)

    vals = []
    m0 = None
    for m, item in enumerate(parts):
        item = item.strip()
        if item.startswith('_'):
            if m0 is not None:
                raise ValueError('Cannot have multiple zero index indicators')
            m0 = m
            item = item[1:]

        val = expr(item)
        vals.append(val)

    if m0 is None:
        m0 = 0

    ni = range(-m0, N - m0)
    return vals, ni


class Sequence(ExprList, SeqDomain):

    var = None
    is_sequence = True
    quantity = 'undefined'

    def __init__(self, seq, ni=None, origin=None, evaluate=False, var=None,
                 start_trunc=False, end_trunc=False):
        """Sequences can be created from an tuple, list, or ndarray.

        See `seq()` to create a Sequence from a string.

        >>> a = Sequence((1, 2, 3))

        The sequence indices are specified with the optional `ni` argument.
        For example:

        >>> a = Sequence((1, 2, 3, 4), (-1, 0, 1, 2))

        If the `ni` argument is not specified, the sequence indices
        are enumerated from 0.

        The sequence indices can be found using the `n` attribute.
        This returns a list.

        >>> a = Sequence('{1, _2, 3, 4}').n
        [-1, 0, 1, 2]

        Sequences can be converted into discrete-time, discrete-frequency,
        z-domain sequences using call notation, for example::

        >>> a(z)

        `start_trunc` indicates that the start of the sequence was truncated
        `end_trunc` indicates that the end of the sequence was truncated

        `start_trunc` and `end_trunc` are not propagated if a sequence is
        modified.  They indicate that ellipsis should be printed to show
        the sequence has been truncated.

        """

        if isinstance(seq, str):
            seq, ni = parse_seq_str(seq)

        if not isiterable(seq):
            seq = (seq, )

        super(Sequence, self).__init__(seq, evaluate)

        if ni is not None and origin is not None:
            raise ValueError('Cannot specify both ni and origin')

        if origin is not None:
            ni = range(-origin, len(self) - origin)

        if ni is None:
            ni = range(len(seq))

        # Perhaps enforce contiguous sequences and just store the origin?
        # This will simplify sequence comparison.
        self.n = list(ni)

        # Determine if sequence truncated at start, end, or both.
        # Perhaps have separate classes for truncated sequences?
        self.start_trunc = start_trunc
        self.end_trunc = end_trunc
        # For symmetry with Expr
        self.assumptions = Assumptions()

    @property
    def isempty(self):
        """True if empty sequence (zero)."""
        return self.vals == []

    @property
    def vals(self):
        """Return the SymPy values as a list."""
        return list(self)

    @property
    def _pexpr(self):
        """Return expression for printing."""
        return self

    def __eq__(self, x):
        """Test for mathematical equality as far as possible.
        This cannot be guaranteed since it depends on simplification.
        Note, SymPy comparison is for structural equality."""

        self._check_compatible(x)
        # Remove zeros from ends of sequences.
        a = self.prune()
        b = x.prune()
        return a.vals == b.vals and a.n == b.n

    def _check_compatible(self, x):

        if not isinstance(x, Sequence):
            raise TypeError('Can only add a sequence to a sequence')
        if x.quantity != 'undefined' and self.quantity != 'undefined' and x.quantity != self.quantity:
            raise TypeError('Sequences have different quantities: %s and %s' % (
                self.quantity, x.quantity))

        if self.domain != x.domain:
            raise TypeError('Sequences have different domains: %s and %s' % (
                self.domain, x.domain))

    def __abs__(self):
        """Absolute value of each element."""

        vals = [abs(val) for val in self.vals]
        return self.__class__(vals, self.n)

    def __add__(self, x):
        """If x is a sequence, add sequences elementwise, otherwise
        add x to each element of the sequence."""

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(self[m] + x[m])
        else:
            vals = [val + x for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __floordiv__(self, x):
        """If x is a sequence, divide sequences elementwise, otherwise
        divide x from each element of the sequence."""

        # Perhaps this should prune x to avoid division by zero?

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(self[m] // x[m])
        else:
            vals = [val // x for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __lshift__(self, m):

        return self.delay(-m)

    def __mul__(self, x):
        """If x is a sequence, multiply sequences elementwise, otherwise
        multiply x to each element of the sequence."""

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(self[m] * x[m])
        else:
            vals = [val * x for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __ne__(self, x):
        """Test for mathematical inequality as far as possible.
        This cannot be guaranteed since it depends on simplification.
        Note, SymPy comparison is for structural equality."""

        return not self.__eq__(x)

    def __neg__(self):
        """Negate each element of the sequence."""

        vals = [-val for val in self.vals]
        return self.__class__(vals, self.n)

    def __pow__(self, x):
        """If x is a sequence, raise sequence to power of x elementwise,
        otherwise raise each element of the sequence to power of x."""

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(self[m] ** x[m])
        else:
            vals = [val ** x for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __radd__(self, x):
        """Reverse add."""

        return self.__add__(x)

    def __rfloordiv__(self, x):
        """Floor divide."""

        # Perhaps this should prune self to avoid division by zero?

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(x[m] // self[m])
        else:
            vals = [x // val for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __rpow__(self, x):
        """If x is a sequence, raise sequence to power of x elementwise,
        otherwise raise x to power of each element in the sequence."""

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(x[m] ** self[m])
        else:
            vals = [x ** val for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __rshift__(self, m):

        return self.delay(m)

    def __rmul__(self, x):
        """Reverse multiply."""

        return self.__mul__(x)

    def __rsub__(self, x):
        """If x is a sequence, subtract sequences elementwise, otherwise
        subtract each element of the sequence from x."""

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(x[m] - self[m])
        else:
            vals = [x - val for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __rtruediv__(self, x):
        """Reverse true divide."""

        # Perhaps this should prune self to avoid division by zero?

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(x[m] / self[m])
        else:
            vals = [x / val for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __str__(self):

        items = []
        if self.start_trunc:
            items.append('...')

        for v1, n1 in zip(self, self.n):
            s = str(v1)

            if n1 == 0:
                s = '_' + s
            items.append(s)

        if self.end_trunc:
            items.append('...')

        return r'{%s}' % ', '.join(items)

    def __sub__(self, x):
        """If x is a sequence, subtract sequences elementwise, otherwise
        subtract x from each element of the sequence."""

        return self.__add__(-x)

    def __truediv__(self, x):
        """If x is a sequence, divide sequences elementwise, otherwise
        divide x from each element of the sequence."""

        # Perhaps this should prune x to avoid division by zero?

        if isinstance(x, Sequence):
            n = self._common_n(x)
            vals = []
            for m in n:
                vals.append(self[m] / x[m])
        else:
            vals = [val / x for val in self.vals]
            n = self.n
        return self.__class__(vals, n)

    def __getitem__(self, n):
        """Note this returns the element with index matching n.
        This is not necessarily the nth element in the sequence."""

        # TODO, support slices, etc.
        try:
            nindex = list(self.n).index(n)
        except ValueError:
            return expr(0)

        return super(Sequence, self).__getitem__(nindex)

    def append(self, x):
        """Concatenate with sequence x."""

        self._check_compatible(x)
        if self.quantity == 'undefined':
            cls = x.__class__
        else:
            cls = self.__class__

        return cls(super(Sequence, self).__add__(x))

    def _common_n(self, x):

        if not isinstance(x, Sequence):
            raise ValueError('Expecting Sequence')

        if self.isempty:
            return x.n
        if x.isempty:
            return self.n

        n1 = min(self.n[0], x.n[0])
        n2 = max(self.n[-1], x.n[-1])
        n = list(range(n1, n2 + 1))
        return n

    def repeat(self, x):
        """Repeat sequence x times.

        seq((1, 2, 3)).repeat(2) gives {1, 2, 3, 1, 2, 3}
        """

        return self.__class__(super(Sequence, self).__mul__(x))

    @property
    def origin(self):
        """Return the element index for n == 0. This may raise a ValueError
        if the origin is not in the sequence."""

        return -min(self.n)

    @origin.setter
    def origin(self, origin):
        """Set the origin to `origin`."""

        from numpy import arange

        self.n = list(arange(-origin, len(self) - origin))

    def prune(self):
        """Remove zeros from ends of sequence.

        {0, 0, 1, 2, 3, 0} -> {1, 2, 3}"""

        vals = self.vals

        m1 = 0
        while m1 < len(vals) and vals[m1] == 0:
            m1 += 1

        m2 = len(vals) - 1
        if vals[m2] != 0:
            return self.__class__(vals[m1:], self.n[m1:])

        while m2 >= 0 and vals[m2] == 0:
            m2 -= 1
        return self.__class__(vals[m1:m2 + 1], self.n[m1:m2 + 1])

    def zeropad(self, M):
        """Add M zeros to end of sequence:

        For example, with M = 3

        {1, 2, 3} -> {1, 2, 3, 0, 0, 0}"""

        vals = list(self.vals)
        n = self.n

        zero = expr(0)
        for m in range(M):
            vals.append(zero)

        ni = self.n + list(range(self.n[-1] + 1, len(vals)))
        return self.__class__(vals, ni)

    def __str__(self):

        a = self.zeroextend()

        items = []
        if self.start_trunc:
            items.append('...')

        for v1, n1 in zip(a, a.n):
            try:
                s = v1.latex()
            except:
                s = str(v1)

            if n1 == 0:
                s = r'_%s' % v1
            items.append(s)

        if self.end_trunc:
            items.append('...')
        return r'{%s}' % ', '.join(items)

    def pretty(self, **kwargs):

        from .printing import pretty

        a = self.zeroextend()
        return pretty(a)

    def as_array(self):
        """Numerically evaluate and store as NumPy array."""

        from numpy import array, allclose

        # If, for some reason, a sequence can have elements that
        # depend on n...
        #vals = array([v1.evaluate(n1) for v1, n1 in zip(self, self.n)])
        vals = array([v1.cval for v1 in self])

        if allclose(vals.imag, 0.0):
            vals = vals.real

        return vals

    @property
    def expr(self):
        """Convert sequence to an Lcapy expression."""

        if self.var is None:
            raise ValueError('var not specified')

        return self.as_impulses(self.var)

    def as_impulses(self, var=None):
        """Convert to discrete-time signal in the form of
        a weighted sum of delayed impulses.  For example,
        {1, 2, 3} -> ui[n] + 2 * ui[n - 1] + 3 * ui[n - 2]"""

        from .functions import unitimpulse
        from sympy import Add

        if var is None:
            var = self.var
        if var is None:
            raise ValueError('var not specified')

        # This can reorder terms
        result = var * 0
        for v1, n1 in zip(self, self.n):
            result += v1.as_constant() * unitimpulse(var - n1)

        # but so does the unevaluated Add...
        # items = []
        # for v1, n1 in zip(self, self.n):
        #     items.append(v1 * unitimpulse(var.var - n1))
        #
        # expr = Add(*items, evaluate=False)
        # result = var.__class__(expr)

        return result

    def evaluate(self, ni=None):
        """Evaluate expression at sequence indices specified by `arg`.  `arg`
        may be a scalar or a vector.  The result is of type float or
        complex.  Zeroes are returned for indices outside the sequence
        extent.

        If `arg` is iterable, a NumPy array is returned.

        """
        from numpy import array, allclose

        if ni is None:
            return self.as_array()
        if isiterable(ni):
            vals = array([self(n1).cval for n1 in ni])

            if allclose(vals.imag, 0.0):
                vals = vals.real

            return vals
        else:
            val = self(ni).cval

            if allclose(val.imag, 0.0):
                val = val.real

            return val

    @property
    def extent(self):
        """Determine extent of the sequence.

        For example, Sequence([1, 1]).extent = 2
                     Sequence([1, 0, 1]).extent = 3
                     Sequence([0, 1, 0, 1]).extent = 3
        """

        from numpy import argwhere

        # Note, each element is an Expr.
        nz = [elt != 0 for elt in self]
        w = argwhere(nz)
        if len(w) == 0:
            return 0

        return (max(w) - min(w))[0] + 1

    def discrete_time_fourier_transform(self, var=None, **assumptions):
        """Convert to Fourier domain using discrete time Fourier transform."""
        return self.DTFT(var, **assumptions)

    def DTFT(self, var=None, **assumptions):
        """Convert to Fourier domain using discrete time Fourier transform."""

        return self.as_impulses().DTFT(var, **assumptions)

    def plot(self, ni=None, **kwargs):
        """Plot the sequence.  If `ni` is not specified, it defaults to the
        sequence indices.  `ni` can be a vector of specified sequence
        indices, a tuple specifing the range, or a constant specifying
        the maximum value with the minimum value set to 0.

        kwargs include:
        axes - the plot axes to use otherwise a new figure is created
        xlabel - the x-axis label
        ylabel - the y-axis label
        xscale - the x-axis scaling, say for plotting as ms
        yscale - the y-axis scaling, say for plotting mV
        unfilled - the markers are unfilled
        markersize - sets the size of the marker
        markerfacecolor - sets the marker color
        in addition to those supported by the matplotlib plot command.

        The plot axes are returned.

        """

        if ni is None:
            ni = self.n

        # This is not the most efficient way but plot routines expect
        # an Expr object.
        return self.as_impulses().plot(ni, **kwargs)

    def __call__(self, arg, **assumptions):
        """Convert sequence to n-domain or k-domain expression.
        For example, seq((1, 2, 3))(n)"""

        from .symbols import n, k, z
        from .sym import nsym, ksym, zsym

        if id(arg) == id(n) or arg == n:
            if self.var == nsym:
                return self.copy()
            elif self.var == ksym:
                return self.IDFT()
            return self.IZT()
        if id(arg) == id(k) or arg == k:
            if self.var == ksym:
                return self.copy()
            elif self.var == zsym:
                return self.IZT().DFT()
            return self.DFT()
        if id(arg) == id(z) or arg == z:
            if self.var == zsym:
                return self.copy()
            elif self.var == ksym:
                return self.IDFT().ZT()
            return self.ZT()

        # This is experimental and may be deprecated.
        return self[arg]

    def _repr_pretty_(self, p, cycle):
        """This is used by jupyter notebooks to display an expression using
        unicode.  It is also called by IPython when displaying an
        expression."""

        # Note, the method in ExprPrint is bypassed since list
        # has this methodx.

        from .printing import pretty
        p.text(self.pretty())

    def copy(self):
        return self.__class__(super(Sequence, self).copy(),
                              self.n)

    def lfilter(self, b=None, a=None):
        """Implement digital filter specified by a transfer function.  The
        transfer function is described by a vector `b` of coefficients
        for the numerator and an `a` vector of coefficients for the
        denominator.

        If you would like the response with initial conditions see
        `DTfilter.response()`.

        For a FIR filter a = [1]."""

        if b is None:
            b = []
        if a is None:
            a = [1]

        x = self.vals
        y = []

        a0 = a[0]

        for n, x1 in enumerate(x):
            y.append(expr(0))

            for m, b1 in enumerate(b):
                try:
                    y[-1] += b1 * x[n - m] / a0
                except:
                    pass

            yn = y[-1]
            for m, a1 in enumerate(a[1:]):
                try:
                    yn += a1 * y[-m - 2] / a0
                except:
                    pass
            y[-1] = yn

        return self.__class__(y, self.n)

    def convolve(self, h, mode='full'):
        """Convolve with h."""

        from numpy import arange

        x = self
        if not isinstance(h, Sequence):
            h = Sequence(h)

        if self.isempty or h.isempty:
            return self.__class__(())

        Lx = x.extent
        Lh = h.extent
        Ly = Lx + Lh - 1

        if mode == 'full':
            x = x.zeropad(Ly - Lx)
        elif mode == 'same':
            x = x.zeropad(max(Lx, Ly) - Lx)
        else:
            raise ValueError('Unknown mode ' + mode)

        y = x.lfilter(h, a=[1])
        y.n = list(arange(len(y)) + x.n[0] + h.n[0])
        return y

    def delay(self, m=0):
        """Return a new sequence delayed by an integer number of samples `m`.
        If `m` is negative, the sequence is advanced."""

        from numpy import arange

        if m != int(m):
            raise ValueError('Non-integer delay %s' % m)

        origin = self.origin - m
        ni = list(arange(-origin, len(self) - origin))

        return self.__class__(self.vals, ni)

    def truncate(self, size):
        """Truncate sequence length to `size` samples."""

        if len(self.vals) < size:
            raise ValueError('Sequence too short for truncation')

        return self.__class__(self.vals[0: size], self.n[0: size])

    def zeroextend(self):
        """Extend sequence by adding zeros so that the origin
        is included.  This is used for printing."""

        if self.isempty:
            # Empty sequence (all zero)
            return self.__class__(())

        ni = self.n
        vals = self.vals

        if ni[0] > 0:
            vals = [0] * ni[0] + vals
            ni = range(0, ni[-1] + 1)
        elif ni[-1] < 0:
            vals = vals + [0] * -ni[-1]
            ni = range(ni[0], 1)

        return self.__class__(vals, ni,
                              start_trunc=self.start_trunc,
                              end_trunc=self.end_trunc)
