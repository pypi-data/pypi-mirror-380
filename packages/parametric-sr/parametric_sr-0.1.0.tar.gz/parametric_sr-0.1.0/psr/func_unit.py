""" """

from itertools import zip_longest
from typing import Any, Literal, Sequence, overload

import numpy as np
from numpy.typing import NDArray

from .base import Operation, Variable, Constant, DelayedConstant
from .typing import (
    DelayedConstantOptions,
    Number,
    OperationOptions,
    SequenceOfDelayedConstantOptions,
)

dummy_func_unit: Constant = Constant(0, name="DUMMY", singleton=False)


def add_(
    a: NDArray[Any] | float, b: NDArray[Any] | float, *args: NDArray[Any] | float
) -> NDArray[Any] | float:
    """
    Adds two arrays or numbers element-wise.

    Parameters
    ----------
    a, b, *args : NDArray | float
        The arguments to add. Should contain exactly two elements. Extra arguments are ignored.

    Returns
    -------
    NDArray | float
        The element-wise sum of the two arguments.
    """
    return a + b


def sub_(
    a: NDArray[Any] | float, b: NDArray[Any] | float, *args: NDArray[Any] | float
) -> NDArray[Any] | float:
    """
    Subtracts the second argument from the first element-wise.

    Parameters
    ----------
    a, b, *args : NDArray | float
        The arguments to subtract. Should contain exactly two elements. Extra arguments are ignored.

    Returns
    -------
    NDArray | float
        The element-wise difference of the two arguments.
    """
    return a - b


def mul_(
    a: NDArray[Any] | float, b: NDArray[Any] | float, *args: NDArray[Any] | float
) -> NDArray[Any] | float:
    """
    Multiplies two arrays or numbers element-wise.

    Parameters
    ----------
    a, b, *args : NDArray | float
        The arguments to multiply. Should contain exactly two elements. Extra arguments are ignored.

    Returns
    -------
    NDArray | float
        The element-wise product of the two arguments.
    """
    return a * b


def div_(
    a: NDArray[Any] | float, b: NDArray[Any] | float, *args: NDArray[Any] | float
) -> NDArray[Any] | float:
    """
    Divides the first argument by the second element-wise.

    Parameters
    ----------
    a, b, *args : NDArray | float
        The arguments to divide. Should contain exactly two elements. Extra arguments are ignored.

    Returns
    -------
    NDArray | float
        The element-wise quotient of the two arguments.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return float("nan")


def square_(
    a: NDArray[Any] | float, *args: NDArray[Any] | float
) -> NDArray[Any] | float:
    """
    Computes the square of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to square. Should contain exactly one element. Extra arguments are ignored.

    Returns
    -------
    NDArray | float
        The element-wise square of the input.
    """
    return a**2


def pow_(
    a: NDArray[Any] | float, b: NDArray[Any] | float, *args: NDArray[Any] | float
) -> NDArray[Any] | float:
    """
    Raises the first argument to the power of the second element-wise.

    Parameters
    ----------
    a, b, *args : NDArray | float
        The arguments to exponentiate. Should contain exactly two elements. Extra arguments are
        ignored.

    Returns
    -------
    NDArray | float
        The element-wise result of raising the first argument to the power of the second.
    """
    res = np.pow(np.asarray(a), np.asarray(b))
    return np.where(np.isfinite(res), res, np.nan)


def neg_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any] | float:
    """
    Negates the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to negate. Should contain exactly one element. Extra arguments are ignored.

    Returns
    -------
    NDArray | float
        The element-wise negation of the input.
    """
    return -a


def abs_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any]:
    """
    Computes the absolute value of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to compute the absolute value. Should contain exactly one element. Extra
        arguments are ignored.

    Returns
    -------
    NDArray
        The element-wise absolute value of the input.
    """
    return np.abs(a)


def inv_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any] | float:
    """
    Computes the inverse of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to compute the inverse. Should contain exactly one element. Extra arguments
        are ignored.

    Returns
    -------
    NDArray | float
        The element-wise inverse of the input.
    """
    try:
        return 1 / a
    except ZeroDivisionError:
        return float("nan")


def log_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any]:
    """
    Computes the natural logarithm of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to compute the logarithm. Should contain exactly one element. Extra arguments
        are ignored.

    Returns
    -------
    NDArray
        The element-wise natural logarithm of the input.
    """
    return np.log(a)


def exp_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any]:
    """
    Computes the exponential of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to compute the exponential. Should contain exactly one element. Extra
        arguments are ignored.

    Returns
    -------
    NDArray
        The element-wise exponential of the input.
    """
    return np.exp(a)


def sqrt_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any] | float:
    """
    Computes the square root of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to compute the square root. Should contain exactly one element. Extra
        arguments are ignored.

    Returns
    -------
    NDArray | float
        The element-wise square root of the input.
    """
    return a**0.5


def sin_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any]:
    """
    Computes the sine of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to compute the sine. Should contain exactly one element. Extra arguments are
        ignored.

    Returns
    -------
    NDArray
        The element-wise sine of the input.
    """
    return np.sin(a)


def cos_(a: NDArray[Any] | float, *args: NDArray[Any] | float) -> NDArray[Any]:
    """
    Computes the cosine of the input element-wise.

    Parameters
    ----------
    a, *args : NDArray | float
        The arguments to compute the cosine. Should contain exactly one element. Extra arguments are
        ignored.

    Returns
    -------
    NDArray
        The element-wise cosine of the input.
    """
    return np.cos(a)


add = Operation(
    "add",
    arity=2,
    operation=add_,
    formatter=(r"{0} + {1}", (True, True), True),
    weight=2.0,
    cost=1.0,
)
sub = Operation(
    "sub",
    arity=2,
    operation=sub_,
    formatter=(r"{0} - {1}", (True, True), True),
    weight=2.0,
    cost=1.0,
)
mul = Operation(
    "mul",
    arity=2,
    operation=mul_,
    formatter=(r"{0} * {1}", (True, True), True),
    weight=2.0,
    cost=1.0,
)
div = Operation(
    "div",
    arity=2,
    operation=div_,
    formatter=(r"{0} / {1}", (True, True), True),
    weight=2.0,
    cost=1.0,
)
square = Operation(
    "square",
    arity=1,
    operation=square_,
    formatter=(r"{0} ^ 2", (True,), True),
    weight=1.0,
    cost=1.0,
)
pow = Operation(
    "pow",
    arity=2,
    operation=pow_,
    formatter=(r"{0} ^ {1}", (True, True), True),
    weight=1.0,
    cost=2.0,
)
neg = Operation(
    "neg",
    arity=1,
    operation=neg_,
    formatter=(r"-{0}", (True,), False),
    weight=1.0,
    cost=1.0,
)
abs_op = Operation(
    "abs",
    arity=1,
    operation=abs_,
    formatter=(r"|{0}|", (False,), False),  # no brackets needed in'n'out
    weight=0.25,
    cost=1.0,
)
inv = Operation(
    "inv",
    arity=1,
    operation=inv_,
    formatter=(r"1 / {0}", (True,), True),
    weight=0.5,
    cost=1.0,
)
log = Operation(
    "log",
    arity=1,
    operation=log_,
    formatter=(r"log({0})", (False,), False),  # no brackets needed in'n'out
    weight=0.5,
    cost=2.0,
)
exp = Operation(
    "exp",
    arity=1,
    operation=exp_,
    formatter=(r"exp({0})", (False,), False),  # no brackets needed in'n'out
    weight=0.5,
    cost=2.0,
)
sqrt = Operation(
    "sqrt",
    arity=1,
    operation=sqrt_,
    formatter=(r"sqrt({0})", (False,), False),  # no brackets needed in'n'out
    weight=0.5,
    cost=2.0,
)
sin = Operation(
    "sin",
    arity=1,
    operation=sin_,
    formatter=(r"sin({0})", (False,), False),  # no brackets needed in'n'out
    weight=0.25,
    cost=3.0,
)
cos = Operation(
    "cos",
    arity=1,
    operation=cos_,
    formatter=(r"cos({0})", (False,), False),  # no brackets needed in'n'out
    weight=0.25,
    cost=3.0,
)

builtin_operations: dict[OperationOptions, Operation[NDArray[Any]]] = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "square": square,
    "pow": pow,
    "neg": neg,
    "abs": abs_op,
    "inv": inv,
    "log": log,
    "exp": exp,
    "sqrt": sqrt,
    "sin": sin,
    "cos": cos,
}


@overload
def get_operations(
    names: OperationOptions,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> Operation[NDArray[Any]]: ...
@overload
def get_operations(
    names: Sequence[OperationOptions] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> list[Operation[NDArray[Any]]]: ...


def get_operations(
    names: OperationOptions | Sequence[OperationOptions] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> Operation[NDArray[Any]] | list[Operation[NDArray[Any]]]:
    """
    Get a list of built-in operations by their names and modify their weights.

    If custom weights are specified, they will be used to alter **existing operations** in place,
    if they were created previously and are in the class instance registry (`dict`).

    Parameters
    ----------
    names : OperationOptions | Sequence[OperationOptions] | None
        The names of the operations to retrieve. If None, all operations will be retrieved.
    weights : Sequence[int | float | None] | None
        The weights to set/update the operations.
    costs : Sequence[int | float | None] | None
        The costs to set/update the operations.

    Returns
    -------
    Operation[NDArray] | list[Operation[NDArray]]
        The requested operation(s).

    Raises
    -------
    ValueError
        If no operation names are provided.
    """
    if names is None:
        return list(builtin_operations.values())

    return_single = False
    if isinstance(names, str):
        names = [names]
        return_single = True
    elif len(names) == 0:
        raise ValueError("At least one operation name must be specified.")

    ops = [builtin_operations[name] for name in names]

    weights = weights or []
    for op, weight in zip(ops, weights):
        if weight is None:
            continue
        op.weight = weight

    costs = costs or []
    for op, cost in zip(ops, costs):
        if cost is None:
            continue
        op.cost = cost

    return ops[0] if return_single else ops


@overload
def get_variables(
    indices: int,
    no_span: Literal[True],
    names: str | Sequence[str | None] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> Variable[Any]: ...
@overload
def get_variables(
    indices: int,
    no_span: Literal[False] = False,
    names: str | Sequence[str | None] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> list[Variable[NDArray[Any]]]: ...
@overload
def get_variables(
    indices: Sequence[int],
    no_span: bool = False,
    names: str | Sequence[str | None] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> list[Variable[NDArray[Any]]]: ...


def get_variables(
    indices: int | Sequence[int],
    no_span: bool = False,
    names: str | Sequence[str | None] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> Variable[NDArray[Any]] | list[Variable[NDArray[Any]]]:
    """
    Get a list of variables by their indices and modify their names/weights.

    If custom names or weights are specified, they will be used to alter **existing variables** in
    place, if they were created previously and are in the class instance registry (`dict`).

    Parameters
    ----------
    indices : int | Sequence[int]
        The max index or indices of the variables to retrieve.

        - `int`: The number of variables to retrieve/initialize. The indices will be [0, 1, ...,
          n-1]. This should be the number of features to expect in the input data `X`.

            If `no_span` is true, the integer will be intepreted as a single 0-based index.
        - `Sequence[int]`: A specific list of indices to retrieve. Should be a subset of [0, 1, ...,
          n-1], where `n` is the number of features to expect in the input data `X`.

    no_span : bool
        If true and the `indices` is an integer, it will be interpreted as a single 0-based index,
        instead of spanning the range.
    names : str | Sequence[str]
        The prefix or names of the variables to retrieve.

        - `str`: The prefix name to use for variables. See `psr.base.func_unit.Variable.prefix` and
          `psr.base.func_unit.IndexedFunction.prefix` for more details.
        - `Sequence[str | None]`: A specific list of names to use for variables. See
          `psr.base.func_unit.Variable.name` for more details. The sequence will be padded with None
          to match the length of the index sequence. *This should not be a single string*.
        - `None`: If no name is provided, the default prefix `X` will be used.

    weights : Sequence[int | float | None] | None
        The weights to set/update the variables.
    costs : Sequence[int | float | None] | None
        The costs to set/update the variables.

    Returns
    -------
    Variable[NDArray] | list[Variable[NDArray]]
        The requested variable(s).

    Raises
    -------
    ValueError
        If no variable indices are provided.
    """
    return_single = False
    if isinstance(indices, int):
        if no_span:
            indices = [indices]
            return_single = True
        else:
            indices = range(indices)

    n = len(indices)
    if n == 0:
        raise ValueError("At least one variable index must be specified.")

    vars: list[Variable[NDArray[Any]]] = [
        Variable(idx, no_warning=True) for idx in indices
    ]

    if names is None:
        names = []
    elif isinstance(names, str):
        Variable.set(prefix=names)
        names = []
    else:
        names = names[:n]

    weights = (weights or [])[:n]
    costs = (costs or [])[:n]

    for op, name, weight, cost in zip_longest(vars, names, weights, costs):
        if name is not None:
            op.name = name
        if weight is not None:
            op.weight = weight
        if cost is not None:
            op.cost = cost

    return vars[0] if return_single else vars


@overload
def get_constants(
    values: Number,
    names: Sequence[str | None] | None = None,
    protections: Sequence[bool | None] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> Constant[NDArray[Any]]: ...
@overload
def get_constants(
    values: Sequence[Number],
    names: Sequence[str | None] | None = None,
    protections: Sequence[bool | None] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> list[Constant[NDArray[Any]]]: ...


def get_constants(
    values: Number | Sequence[Number],
    names: Sequence[str | None] | None = None,
    protections: Sequence[bool | None] | None = None,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> Constant[NDArray[Any]] | list[Constant[NDArray[Any]]]:
    """
    Get a list of constants by their values.

    If custom names or weights are specified, they will be used to alter **existing constants** in
    place, if they were created previously and are in the class instance registry (`dict`).

    Parameters
    ----------
    values : Number | Sequence[Number]
        The value(s) of the constants(s) to retrieve/initalize.
    names : Sequence[str | None] | None
        The names to assign to the constants. Typically, the names should be automatically generated
        as the string representations of the values. Make sure you understand the implications if
        providing custom names.
    protections : Sequence[bool | None] | None
        For the provided names, whether they need to be protected when formatting the expression.
        In most cases, you should not use names such as `1 + e` to represent a constant value, which
        needs to be protected with brackets in mathematical expressions. Round `1 + e` to a float
        and use the default name instead (recommended).
    weights : Sequence[int | float | None] | None
        The weights to assign to the constants.
    costs : Sequence[int | float | None] | None
        The costs to assign to the constants.

    Returns
    -------
    Constant[NDArray] | list[Constant[NDArray]]
        The requested constants.

    Raises
    ------
    ValueError
        If no values are specified.
    """
    return_single = False
    if not isinstance(values, Sequence):
        values = [values]
        return_single = True

    cs: list[Constant[NDArray[Any]]] = [
        Constant(val, no_warning=True) for val in values
    ]
    n = len(cs)
    if n == 0:
        raise ValueError("At least one value must be specified.")

    names = [] if names is None else names[:n]
    protections = [] if protections is None else protections[:n]
    weights = [] if weights is None else weights[:n]
    costs = [] if costs is None else costs[:n]
    for c, name, protection, weight, cost in zip_longest(
        cs, names, protections, weights, costs
    ):
        if name is not None:
            c.name = name
            if protection is not None:
                c.needs_protection = protection
        if weight is not None:
            c.weight = weight
        if cost is not None:
            c.cost = cost

    return cs[0] if return_single else cs


# method 1: explicit subclass creation with subclassing parameters
class DelayedConstantPos(
    DelayedConstant[NDArray[Any]],
    prefix="C_p",
    initial_guess=1.0,
    bounds=(0, None),
    weight=1.0,
    cost=2.0,
):
    """
    :class:`DelayedConstant` with positive initial guess and bounds.
    """

    pass


# method 2: built-in subclass creation with the class method
DelayedConstantNeg = DelayedConstant[NDArray[Any]].create_subclass(
    "DelayedConstantNeg",
    prefix="C_n",
    initial_guess=-1.0,
    bounds=(None, 0),
    weight=1.0,
    cost=2.0,
)
"""
:class:`DelayedConstant` with negative initial guess and bounds.
"""

DelayedConstantReal = DelayedConstant[NDArray[Any]]  # alias for real-valued constants
"""
alias for :class:`psr.base.func_unit.DelayedConstant` (initial_guess=0., bounds=(None, None))
"""


# method 1: explicit subclass creation with subclassing parameters
class DelayedConstantSmall(
    DelayedConstant[NDArray[Any]],
    prefix="C_s",
    initial_guess=1.0,
    bounds=(-5.0, 5.0),
    weight=1.0,
    cost=2.0,
):
    """
    :class:`DelayedConstant` with small initial guess and bounds (-5.0, 5.0).
    """

    pass


# method 1: explicit subclass creation with subclassing parameters
class DelayedConstantMini(
    DelayedConstant[NDArray[Any]],
    prefix="C_m",
    initial_guess=0.2,
    bounds=(-1.0, 1.0),
    weight=1.0,
    cost=2.0,
):
    """
    :class:`DelayedConstant` with small initial guess (0.2) and bounds (-1.0, 1.0).
    """

    pass


@overload
def get_delayed_constants(
    prefixes: DelayedConstantOptions,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> DelayedConstant[NDArray[Any]]: ...
@overload
def get_delayed_constants(
    prefixes: SequenceOfDelayedConstantOptions,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> list[DelayedConstant[NDArray[Any]]]: ...


def get_delayed_constants(
    prefixes: DelayedConstantOptions | SequenceOfDelayedConstantOptions,
    weights: Sequence[int | float | None] | None = None,
    costs: Sequence[int | float | None] | None = None,
) -> DelayedConstant[NDArray[Any]] | list[DelayedConstant[NDArray[Any]]]:
    """
    Get a list of delayed constants by their prefixes and modify their weights. You must create
    subclasses of `DelayedConstant` first if you have custom implementations other than the built-in
    ones.

    The builtin prefixes include:

    - `C`: :class:`psr.func_unit.DelayedConstant` (initial_guess=0., bounds=(None, None))
    - `C_p`: :class:`psr.func_unit.DelayedConstantPos` (initial_guess=1., bounds=(0., None))
    - `C_n`: :class:`psr.func_unit.DelayedConstantNeg` (initial_guess=-1., bounds=(None, 0.))
    - `C_s`: :class:`psr.func_unit.DelayedConstantSmall` (initial_guess=1., bounds=(-5., 5.))
    - `C_m`: :class:`psr.func_unit.DelayedConstantMini` (initial_guess=0.2, bounds=(-1.0, 1.0))

    If custom weights are specified, they will be used to alter **existing delayed constants** in
    place.

    Parameters
    ----------
    prefixes : DelayedConstantOptions | Sequence[DelayedConstantOptions]
        The prefixes of the delayed constants to retrieve.

        - `str`: The prefix name to use for the delayed constants.
        - `Sequence[str]`: A specific list of prefixes to use for the delayed constants.

        **Note**: Each prefix must correspond to an existing subclass of `DelayedConstant`.
    weights : Sequence[int | float | None] | None
        The weights to set/update the delayed constants.
    costs : Sequence[int | float | None] | None
        The costs to set/update the delayed constants.

    Returns
    -------
    DelayedConstant[NDArray] | list[DelayedConstant[NDArray]]
        The requested delayed constants.

    Raises
    ------
    ValueError
        If no prefixes are specified.
    """
    return_single = False
    if isinstance(prefixes, str):
        prefixes = [prefixes]
        return_single = True
    elif len(prefixes) == 0:
        raise ValueError("At least one prefix must be specified.")

    dcs: list[DelayedConstant[NDArray[Any]]] = []
    for prefix in prefixes:
        cls = DelayedConstant.get(prefix=prefix)
        if cls is None:
            raise KeyError(f"DelayedConstant of prefix '{prefix}' not found.")
        if not issubclass(cls, DelayedConstant):
            raise TypeError(
                f"Class '{cls.__name__}' is not a subclass of DelayedConstant."
            )
        dc_: DelayedConstant[NDArray[Any]] = cls()  # type: ignore
        dcs.append(dc_)

    weights = weights or []
    for dc, weight in zip(dcs, weights):
        if weight is not None:
            dc.weight = weight

    costs = costs or []
    for dc, cost in zip(dcs, costs):
        if cost is not None:
            dc.cost = cost

    return dcs[0] if return_single else dcs
