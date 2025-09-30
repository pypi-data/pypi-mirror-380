"""
`parametric-sr` is a Python package for parametric symbolic regression, designed to facilitate the
discovery of mathematical expressions to model one or multiple groups of data.

The basic idea behind symbolic regression is to find a mathematical expression `f` that fits a given
dataset, e.g., y = f(x) + ε, where y is the output variable, x is the input variable, and ε is the
error term. Most probably, the expression `f` includes a set of values/numbers that complete the
expression. Instead of using a fixed set of values, `parametric-sr` allows undertermined values in
the expression, which can be optimized during the fitting process using techniques like gradient
descent or other optimization algorithms. For example, the expression could be formed as
`f(x) = a * x^2 + b * x + c`, where a, b, and c are the parameters to be optimized during the
fitting/evaluation process. This allows for a more flexible and powerful modeling approach that can
adapt to various types of data and relationships.

This also allows for the discovery of patterns across a family of datasets. For example, for the
expression `f(x) = a * x^2 + b * x + c`, the parameters `(a, b, c)` can be used to describe a
specific shape of the curve. In other words, this parametric expression can be used to model a
family of datasets that share the same underlying relationship but may differ in the specific
parameter values. This is particularly useful in scenarios where multiple datasets exhibit similar
trends or behaviors, allowing for a unified model that captures the essence of the data across
different contexts. This can be useful in fields like physics, biology, and economics, where similar
patterns may emerge across different experiments or observations.
"""

__version__ = "0.1.0"

from .base import Tree, FuncUnit, Operation, Variable, Constant, DelayedConstant
from .collection import PSRCollection
from .config import Config, config
from .expression import Expression
from .expression_builder import ExpressionBuilder, ExpressionTracker
from .func_unit import DelayedConstantReal, DelayedConstantPos, DelayedConstantNeg
from .func_unit import DelayedConstantMini, DelayedConstantSmall
from .func_unit import (
    get_operations,
    get_variables,
    get_constants,
    get_delayed_constants,
)
from .logging import add_file_handler, logger
from .metrics import Scorer, digest_batch_scores, get_scorer, set_scorer
from .psr import ParametricSR

__all__ = [
    "Tree",
    "FuncUnit",
    "Operation",
    "Variable",
    "Constant",
    "DelayedConstant",
    "PSRCollection",
    "Config",
    "config",
    "Expression",
    "ExpressionBuilder",
    "ExpressionTracker",
    "DelayedConstantReal",
    "DelayedConstantPos",
    "DelayedConstantNeg",
    "DelayedConstantMini",
    "DelayedConstantSmall",
    "get_operations",
    "get_variables",
    "get_constants",
    "get_delayed_constants",
    "add_file_handler",
    "logger",
    "Scorer",
    "digest_batch_scores",
    "get_scorer",
    "set_scorer",
    "ParametricSR",
]
