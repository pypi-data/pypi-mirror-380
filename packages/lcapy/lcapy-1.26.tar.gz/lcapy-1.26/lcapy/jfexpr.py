"""This module provides the FrequencyResponseDomainExpression class to
represent jf-domain ( frequency frequency domain) expressions.

Copyright 2022--2024 Michael Hayes, UCECE

"""

from __future__ import division
from .domains import FrequencyResponseDomain
from .inverse_fourier import inverse_fourier_transform
from .expr import Expr, expr, expr_make
from .state import state, validate
from .sym import fsym, ssym, tsym, fsym, j, pi
from .units import u as uu
from sympy import Expr as symExpr

__all__ = ('FrequencyResponseDomainExpression', )


class FrequencyResponseDomainExpression(FrequencyResponseDomain, Expr):
    """Frequency domain expression or symbol."""

    var = fsym

    def __init__(self, val, **assumptions):

        check = assumptions.pop('check', True)

        super(FrequencyResponseDomainExpression,
              self).__init__(val, **assumptions)

        expr = self.expr

        if check and not expr.has(fsym):
            if expr.has(tsym):
                validate(state.t_in_jf,
                         'jf-domain expression %s depends on t' % expr)
            if expr.has(ssym):
                validate(state.s_in_jf,
                         'jf-domain expression % s depends on s' % expr)
            if expr.has(fsym):
                validate(state.f_in_jf,
                         'jf-domain expression %s depends on f' % expr)

    def _div_compatible_domains(self, x):

        if x.is_fourier_domain:
            return True

        return super(FrequencyResponseDomainExpression, self)._div_compatible_domains(x)

    def as_expr(self):
        return FrequencyResponseDomainExpression(self)

    def inverse_fourier(self, **assumptions):
        """Attempt inverse Fourier transform."""

        result = self.inverse_fourier_transform(expr.sympy, fsym, tsym)

        return self.change(result, 'time', units_scale=uu.Hz, **assumptions)

    def time(self, **assumptions):
        """Alias for inverse_fourier."""

        return self.inverse_fourier(**assumptions)

    def _fourier(self, **assumptions):
        """Convert to  Fourier domain."""

        return self.laplace(**assumptions)._fourier()

    def fourier(self, **assumptions):
        """Convert to Fourier domain."""

        return self.laplace(**assumptions).fourier()

    def norm_fourier(self, **assumptions):
        """Convert to normalized Fourier domain."""

        return self.laplace(**assumptions).norm_fourier()

    def norm_angular_fourier(self, **assumptions):
        """Convert to normalized  Fourier domain."""

        return self.laplace(**assumptions).norm_angular_fourier()

    def laplace(self, **assumptions):
        """Convert to Laplace domain."""

        from .symbols import s, j

        return self.subs(s / (j * 2 * pi))

    def phasor(self, **assumptions):
        """Convert to phasor domain."""

        return self.time(**assumptions).phasor(**assumptions)

    def plot(self, vvector=None, **kwargs):
        """Plot  frequency response at values specified by vvector.

        There are many plotting options, see matplotlib.pyplot.plot.

        For example:
            V.plot(fvector, log_frequency=True)
            V.real.plot(fvector, color='black')
            V.phase.plot(fvector, color='black', linestyle='--')

        By default complex data is plotted as separate plots of magnitude (dB)
        and phase.

        `kwargs` include:
        `axes` - the plot axes to use otherwise a new figure is created
        `xlabel` - the x-axis label
        `ylabel` - the y-axis label
        `ylabel2` - the second y-axis label if needed, say for mag and phase
        `xscale` - the x-axis scaling, say for plotting as ms
        `yscale` - the y-axis scaling, say for plotting mV
        `norm` - use normalized frequency
        `dbmin` - the smallest value to plot in dB (default -120)
        in addition to those supported by the matplotlib plot command.

        The plot axes are returned.  This is a tuple for magnitude/phase or
        real/imaginary plots.
        """

        from .plot import plot_frequency
        return plot_frequency(self, vvector, **kwargs)

    def bode_plot(self, vvector=None, unwrap=True, phase='radians', **kwargs):
        """Plot frequency response for a frequency-domain phasor as a Bode
        plot (but without the straight line approximations).  vvector
        specifies the  frequencies.  If it is a tuple (f1, f2), it sets
        the frequency limits.   Since a logarithmic frequency scale is used,
        f1 must be greater than 0.

        `unwrap` controls phase unwrapping (default True).

        For more info, see `plot`.
        """

        from .plot import plot_bode
        return plot_bode(self, vvector, unwrap=unwrap, phase=phase,
                         **kwargs)

    def nyquist_plot(self, vvector=None, log_frequency=True, **kwargs):
        """Plot frequency response as a Nyquist plot (imaginary part versus
        real part).  vvector specifies the  frequencies.  If it
        is a tuple (f1, f2), it sets the frequency limits as (f1, f2).

        `npoints` set the number of plotted points.

        The unit circle is shown by default.  This can be disabled
        with `unitcircle=False`.

        """

        from .plot import plot_nyquist
        return plot_nyquist(self, vvector, log_frequency=log_frequency, **kwargs)

    def nichols_plot(self, vvector=None, log_frequency=True, **kwargs):
        """Plot frequency response as a Nichols plot (dB versus phase).
        vvector specifies the  frequencies.  If it is a tuple
        (f1, f2), it sets the frequency limits as (f1, f2).

        `npoints` set the number of plotted points.

        """

        from .plot import plot_nichols
        return plot_nichols(self, vvector, log_frequency=log_frequency, **kwargs)


jf = FrequencyResponseDomainExpression('j * f')
jf.units = 1 / uu.s

j2pif = FrequencyResponseDomainExpression('j * 2 * pi * f')
j2pif.units = uu.rad / uu.s
