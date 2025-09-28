"""This module provides the CausalChecker, ACChecker, and DCChecker
classes as used by the is_causal, is_ac, and is_dc functions.

Copyright 2020--2023 Michael Hayes, UCECE

"""

from .sym import sympify1
from .extrafunctions import UnitImpulse, UnitStep
from .functions import Eq
import sympy as sym
from sympy import cos, pi, sin, atan2, sqrt, exp


class CausalChecker(object):

    def _has_causal_factor(self, expr):

        factors = expr.as_ordered_factors()
        for factor in factors:
            if factor == 0:
                return True
            if (not factor.is_Function
                or factor.func not in (sym.Heaviside, sym.DiracDelta,
                                       UnitImpulse, UnitStep)):
                continue

            # If have Heaviside(t), etc., then is causal
            if factor.args[0] == self.var:
                return True

            p = sym.Poly(factor.args[0], self.var)
            coeffs = p.all_coeffs()
            if len(coeffs) != 2:
                return False

            # Look for something like func(a * t + b)
            # If a positive and b negative then know func(a * t + b) = 0 for t < 0
            # TODO, generalise.
            a, b = coeffs
            if (a.is_positive and (b.is_negative or b.is_zero)):
                return True

        return False

    def _is_causal(self, expr):

        terms = expr.expand().as_ordered_terms()
        for term in terms:
            if not self._has_causal_factor(term):
                return False

        return True

    def __init__(self, expr, var):

        self.var = getattr(var, 'expr', sympify1(var))
        try:
            expr = expr.expr
        except:
            expr = sympify1(expr)

        self.is_causal = self._is_causal(expr)


class DCChecker(object):

    def _is_dc(self, expr):

        return not self.var in expr.free_symbols

    def __init__(self, expr, var):

        self.var = getattr(var, 'expr', sympify1(var))
        try:
            expr = expr.expr
        except:
            expr = sympify1(expr)

        self.is_dc = self._is_dc(expr)


class ACChecker(object):
    """This looks for real ac signals; it does not work for complex ac signals."""

    def _find_freq_phase(self, expr):

        self.freq = 0
        self.omega = 0

        if expr.func == cos:
            self.phase = 0
        elif expr.func == sin:
            self.phase = -pi / 2
        elif expr.func == exp:
            if not expr.args[0].has(sym.I):
                return False
            self.phase = 0
            self.is_complex = True
        else:
            raise ValueError('%s not sin/cos' % expr)

        arg = expr.args[0]
        if self.is_complex:
            arg /= sym.I

        p = sym.Poly(arg, self.var)
        coeffs = p.all_coeffs()
        if len(coeffs) != 2:
            return False

        self.phase += coeffs[1]
        self.omega = coeffs[0]
        self.freq = self.omega / (2 * pi)
        return True

    def _is_sum_ac(self, terms):

        check = ACChecker(terms[0], self.var)
        if not check.is_ac:
            return False

        for term in terms[1:]:
            check2 = ACChecker(term, self.var)
            if not check2.is_ac or check.omega != check2.omega:
                return False
            if check.is_complex != check2.is_complex:
                return False
            A1, p1 = check.amp, check.phase
            A2, p2 = check2.amp, check2.phase
            x = A1 * cos(p1) + A2 * cos(p2)
            y = A1 * sin(p1) + A2 * sin(p2)
            if y == 0:
                check.phase = 0
                check.amp = x
            elif x == 0:
                check.phase = pi / 2
                check.amp = y
            else:
                check.phase = atan2(y, x)
                check.amp = sqrt(x**2 + y**2)

        self.freq = check.freq
        self.omega = check.omega
        self.amp = check.amp
        self.phase = check.phase
        return True

    def _is_ac(self, expr):

        # Convert exp(-j*x*t) + exp(j*x*t) into 2 * cos(x) etc.
        expr = sym.exptrigsimp(expr.rewrite(cos))

        terms = expr.expand().as_ordered_terms()
        if len(terms) > 1:
            return self._is_sum_ac(terms)

        factors = expr.as_ordered_factors()

        self.amp = 1
        for factor in factors:
            if factor.is_Function:
                if factor.func not in (cos, sin, exp):
                    return False
                if not self._find_freq_phase(factor):
                    return False
            elif is_dc(factor, self.var):
                self.amp *= factor
            else:
                return False
        return True

    def __init__(self, expr, var):

        self.var = getattr(var, 'expr', sympify1(var))
        self.amp = 0
        self.omega = 0
        self.freq = 0
        self.phase = 0
        self.is_complex = False

        try:
            expr = expr.expr
        except:
            expr = sympify1(expr)

        self.is_ac = self._is_ac(expr)


def is_dc(expr, var):

    try:
        if expr.is_Equality:
            return is_dc(expr.expr.args[0], var) or is_dc(expr.expr.args[1], var)
    except:
        pass

    return DCChecker(expr, var).is_dc


def is_ac(expr, var):

    try:
        if expr.is_Equality:
            return is_ac(expr.expr.args[0], var) or is_ac(expr.expr.args[1], var)
    except:
        pass

    return ACChecker(expr, var).is_ac


def is_causal(expr, var):

    try:
        if expr.is_Equality:
            return is_causal(expr.expr.args[0], var) or is_causal(expr.expr.args[1], var)
    except:
        pass

    return CausalChecker(expr, var).is_causal
