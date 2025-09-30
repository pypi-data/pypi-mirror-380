"""
typing
"""

from typing import (
    Any,
    Callable,
    Generator,
    Hashable,
    Literal,
    Optional,
    Protocol,
    Self,
    Sequence,
    TypeAlias,
    TypeVar,
    TypedDict,
)

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import LinearConstraint, NonlinearConstraint

# for now, Number only represent real values; complex values are not supported
Number: TypeAlias = int | float
NDArrayOrNumber: TypeAlias = NDArray[Any] | Number
HashableT = TypeVar("HashableT", bound=Hashable)
T = TypeVar("T")
R = TypeVar("R")


class _ArrayLike(Protocol):
    def __getitem__(self, *args: Any, **kwargs: Any) -> Self | Number | Any: ...

    def __len__(self) -> int: ...

    def __iter__(self) -> Generator[Any, Any, Any]: ...

    # @property
    # def shape(self) -> Sequence[int]: ...


NestedSequence: TypeAlias = Sequence["Number | NestedSequence"]
ArrayLike: TypeAlias = _ArrayLike | NDArray[Any]
ArrayLikeT = TypeVar("ArrayLikeT", ArrayLike, NDArray[Any])
RngGeneratorSeed: TypeAlias = Optional[
    int
    | Sequence[int]
    | np.random.SeedSequence
    | np.random.BitGenerator
    | np.random.Generator
    | np.random.RandomState
]

OperationOptions: TypeAlias = Literal[
    "add",
    "sub",
    "mul",
    "div",
    "square",
    "pow",
    "neg",
    "abs",
    "inv",
    "log",
    "exp",
    "sqrt",
    "sin",
    "cos",
]


DelayedConstantOptions: TypeAlias = Literal["C", "C_p", "C_n", "C_s", "C_m"] | str
SequenceOfDelayedConstantOptions: TypeAlias = (
    list[DelayedConstantOptions]
    | tuple[DelayedConstantOptions, ...]
    | set[DelayedConstantOptions]
    | frozenset[DelayedConstantOptions]
)


class _ScipyConstraintA(TypedDict, total=True):
    type: str
    fun: Callable[..., Any]


class _ScipyConstraintB(TypedDict, total=False):
    jac: Callable[..., Any]
    args: Sequence[Any]


class _ScipyConstraintCombined(_ScipyConstraintA, _ScipyConstraintB):
    pass


_ScipyConstraint: TypeAlias = (
    LinearConstraint | NonlinearConstraint | _ScipyConstraintCombined
)


class _ScipyMinimizeOptions(TypedDict, total=False):
    maxiter: int
    disp: bool


class ScipyMinimizeOptions(TypedDict, total=False):
    method: Optional[str]
    jac: Optional[Literal["2-point", "3-point", "cs"] | bool | Callable[..., Any]]
    hess: Optional[Literal["2-point", "3-point", "cs"] | bool | Callable[..., Any]]
    hessp: Optional[Callable[..., Any]]
    constraints: Optional[_ScipyConstraint | list[_ScipyConstraint]]
    tol: Optional[float]
    options: Optional[_ScipyMinimizeOptions]
    callback: Optional[Callable[..., Any]]


ScipyMinimizeFunction: TypeAlias = Callable[
    [ArrayLikeT | Sequence[Number], ArrayLikeT, ArrayLikeT, Optional[ArrayLikeT]], float
]


class ScipyCurveFitOptions(TypedDict, total=False):
    method: Optional[Literal["lm", "trf", "dogbox"]]
    sigma: Optional[ArrayLike | Sequence[Number] | Sequence[Sequence[Number]]]
    absolute_sigma: Optional[bool]
    check_finite: Optional[bool]
    jac: Optional[Literal["2-point", "3-point", "cs"] | Callable[..., Any]]
    full_output: Optional[bool]
    nan_policy: Optional[Literal["raise", "omit"]]
    options: dict[str, Any]


ScipyCurveFitFunction: TypeAlias = Callable[
    [ArrayLikeT, *tuple[Number, ...]], ArrayLikeT
]
CurveFitResult: TypeAlias = tuple[
    NDArray[np.float64], NDArray[np.float64], *tuple[Any, ...]
]

PSRCollectionOptions: TypeAlias = Literal[
    "operations", "variables", "constants", "delayed_constants"
]

# expression generation techniques that require zero/one/two parent(s)
ExpressionInitOptions: TypeAlias = Literal["random", "balanced", "full"]
ExpressionEvolOptions: TypeAlias = Literal["crossover", "mutation", "reproduction"]
ExpressionMutaOptions: TypeAlias = Literal["subtree", "hoist", "point"]
ExpressionHow_0: TypeAlias = Literal[
    "seed", "init-random", "init-balanced", "init-full"
]
ExpressionHow_1: TypeAlias = Literal[
    "reproduction", "mutation-subtree", "mutation-hoist", "mutation-point"
]
ExpressionHow_2: TypeAlias = Literal["crossover"]
ExpressionHow: TypeAlias = (
    ExpressionHow_0
    | ExpressionHow_1
    | ExpressionHow_2
    | tuple[ExpressionHow_2, ExpressionHow_1]
    | str
    | tuple[str, str]
    | None
)

# scoring options
OptimizeOptions: TypeAlias = Literal["curve_fit", "minimize"]
ScalingOptions: TypeAlias = Literal["log", "plog", "square"]
scaling_options: tuple[ScalingOptions, ...] = ("log", "plog", "square")
ScalingCallable: TypeAlias = Callable[
    [ArrayLike | Sequence[Number] | Number], NDArray[Any]
]
ScoringOptions: TypeAlias = Literal[
    "mae",
    "mape",
    "mse",
    "rmse",
    "r2",
    "log_mae",
    "log_mape",
    "log_mse",
    "log_rmse",
    "log_r2",
]
BatchScoringOptions: TypeAlias = Literal["mean", "median", "max", "min"] | float
RankingOptions: TypeAlias = Literal["softmax", "power", "rank", "linear"]

# for configuration

NumpyErrKeys: TypeAlias = Literal["all", "divide", "over", "under", "invalid"]
NumpyErrVals: TypeAlias = Optional[
    Literal["ignore", "raise", "warn", "call", "print", "log"]
]
NumpyErrState: TypeAlias = dict[NumpyErrKeys, NumpyErrVals]
