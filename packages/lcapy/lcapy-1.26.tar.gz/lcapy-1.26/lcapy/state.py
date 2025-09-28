"""This module provides the State class that maintains the global state,
such as the symbol context.

Copyright 2014--2025 Michael Hayes, UCECE

"""

from sympy.assumptions.assume import global_assumptions

from .context import Context
from .printing_config import PrintingConfig
from .symbolregistry import SymbolRegistry
from copy import copy
from warnings import warn


class State(object):
    """This maintains Lcapy's state, such as the defined symbols, and
    behaviour.

    `loose_units` (default True) allows constants to be added to quantities
    `show_units` (default False) prints the units after an expression
    `canonical_units` (default True) converts units to canonical form, e.g., V / A is shown as ohms.
    'printing.abbreviate_units` (default True) prints V rather than volts

    """

    def __init__(self):
        self.symbols = SymbolRegistry()
        self.context = Context()
        self.context.symbols = self.symbols
        self.previous_context = []
        self.printing = PrintingConfig()

        # The following are updated by rcparam
        # With loose_units can add constants to quantities, e.g., voltage(1) + 2
        # or impedance(2) == 2.
        self.loose_units = True
        self.check_units = True
        self.show_units = False
        self.canonical_units = False
        self.printing.abbreviate_units = True

        self.warn_subs = False
        self.break_subs = False
        self.notify_symbol_add = False
        self.warn_unknown_symbol = False
        self.break_unknown_symbol = False

        self.zero_initial_conditions = False

        # The following can either be `allow`, `warn`, or `error`.
        # They are used in expr.c:__mul__ to validate multiplications.
        self.s_times_t = 'warn'
        self.t_times_s = 'warn'
        self.f_times_t = 'warn'
        self.t_times_f = 'warn'
        self.w_times_t = 'warn'
        self.t_times_w = 'warn'

        # The following can either be `allow`, `warn`, or `error`.
        # They are used in the expression class constructors.
        self.f_in_t = 'warn'
        self.s_in_t = 'warn'
        self.w_in_t = 'warn'

        self.f_in_s = 'warn'
        self.t_in_s = 'warn'
        self.w_in_s = 'warn'

        self.s_in_f = 'warn'
        self.t_in_f = 'warn'
        self.w_in_f = 'warn'

        self.f_in_w = 'warn'
        self.s_in_w = 'warn'
        self.t_in_w = 'warn'

        self.f_in_jf = 'warn'
        self.s_in_jf = 'warn'
        self.t_in_jf = 'warn'

        self.f_in_jw = 'warn'
        self.s_in_jw = 'warn'
        self.t_in_jw = 'warn'

        self.pdb_on_warn = False
        self.error_on_warn = False

        # 'passive', 'active', 'hybrid', None for default ('hybrid')
        self.current_sign_convention = 'passive'

    def new_context(self):

        context = Context()
        context.symbols = self.symbols
        return context

    def switch_context(self, context):

        self.previous_context.append(self.context)
        self.context = context

        global_assumptions.clear()
        global_assumptions.update(self.context.assumptions)

    def restore_context(self):

        self.context.assumptions.update(global_assumptions)

        self.context = self.previous_context.pop()

        global_assumptions.clear()
        global_assumptions.update(self.context.assumptions)

    @property
    def abbreviate_units(self):

        return self.printing.abbreviate_units

    @abbreviate_units.setter
    def abbreviate_units(self, val):
        """Enable/disable printing of units in abbreviated form."""

        self.printing.abbreviate_units = val


def validate(value, message):

    if value == 'allow':
        pass
    elif value == 'warn':
        if state.pdb_on_warn:
            import pdb
            pdb.set_trace()
        if state.error_on_warn:
            raise ValueError(message)
        else:
            warn(message)
    elif value == 'error':
        raise ValueError(message)
    else:
        raise RuntimeError('Unexpected option ' + value)


state = State()
