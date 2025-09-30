"""
utilities
"""

from multiprocessing import cpu_count
from typing import Any, Callable, Literal, NoReturn, Sequence, TypeVar, overload

import numpy as np
from numpy.typing import NDArray
from scipy.special import softmax

from .config import config
from .typing import ExpressionHow, RankingOptions, T


class noquote_str(str):
    """
    A string with a `__repr__` method that returns the string without quotes.
    """

    def __repr__(self) -> str:
        return self.__str__()


def inplace_cls_update(existing_cls: type[T], new_cls: type[T]) -> None:
    """
    Update the attributes of an existing class in place with those from a new class.

    Parameters
    ----------
    existing_cls : type
        The existing class to update.
    new_cls : type
        The new class to copy attributes from.
    """
    for key, value in new_cls.__dict__.items():
        if key not in ("__dict__", "__weakref__"):
            setattr(existing_cls, key, value)


@overload
def validate_expression_how(how: ExpressionHow, /) -> Literal[True]: ...
@overload
def validate_expression_how(how: Any, /) -> bool: ...


def validate_expression_how(how: Any, /) -> bool:
    """
    Validate the `how` parameter for :class:`~psr.expression.ExpressionTracker`.

    Parameters
    ----------
    how : ExpressionHow | Any
        The `how` parameter to validate.

    Returns
    -------
    bool
        True if the `how` parameter is valid, False otherwise.
    """
    if isinstance(how, str) or how is None:
        return True

    if how is None:
        return True

    if (
        isinstance(how, tuple)
        and len(how) == 2
        and all(isinstance(x, str) for x in how)
    ):
        return True
    return False


@overload
def get_normalized_weights(weights: None, /, match: None = None) -> NoReturn: ...
@overload
def get_normalized_weights(
    weights: Sequence[float] | None, /, match: Sequence[Any] | None = None
) -> NDArray[np.float64]: ...


def get_normalized_weights(
    weights: Sequence[float] | None, /, match: Sequence[Any] | None = None
) -> NDArray[np.float64]:
    """
    Normalize weights to sum to 1.

    Parameters
    ----------
    weights : Sequence[float] | None
        The weights to normalize. If None, `match` sequence must be provided and the normalized
        weights will be uniform.
    match : Sequence[Any] | None
        Optional sequence to match the length of the returned weights.

    Returns
    -------
    Sequence[float]
        Normalized weights.

    Raises
    ------
    ValueError
        If the weights are negative or do not sum to 1, or if there is a length mismatch.
    """
    if weights is None:
        if match is None:
            raise ValueError("Match sequence must be provided if weights are None.")
        norm_w = np.ones_like(match, dtype=np.float64)
    else:
        norm_w = np.array(weights, dtype=np.float64)
        if np.any(norm_w < 0) or np.allclose(norm_w, 0):
            raise ValueError(
                "Weights cannot be negative and "
                "must contain at least one non-zero value."
            )
        if match is not None and len(norm_w) != len(match):
            raise ValueError("Match sequence must be the same length as weights.")

    norm_w /= np.sum(norm_w)
    return norm_w


def always(value: T) -> Callable[..., T]:
    """
    Return a function that always returns the given value.
    """

    def f(*args: Any, **kwargs: Any) -> T:
        """
        A function that always returns the given value.
        """
        return value

    return f


def compute_n_cpus(n_jobs: int | None = None) -> int:
    """
    Compute the number of CPUs to use for multiprocessing.

    Parameters
    ----------
    n_jobs : int | None, default=None
        The number of jobs to run in parallel.

        - `None` or `0`: use just one CPU core.
        - *negative*: `-1` (use all available CPUs), `-2` (use all available CPUs minus 1), etc.
        - The *minimum* is 1 CPU core, and the *maximum* is the number of available CPUs.

    Returns
    -------
    int
        The integer number of CPUs to use, between 1 and the number of available CPUs.
    """
    n_max = cpu_count()

    if n_jobs is None or n_jobs == 0:
        return 1

    if n_jobs < 0:
        n_jobs = max(1, n_max + 1 + n_jobs)

    return min(n_jobs, n_max)


def scores_to_weights(
    scores: NDArray[np.float64] | Sequence[float],
    method: RankingOptions = "softmax",
    temperature: float = 1.0,
    power: float = 2.0,
    eps: float = 1e-12,
) -> NDArray[np.float64] | NDArray[np.int64]:
    """
    Map scores (higher = better) -> selection weights summing to 1.

    Parameters
    ----------
    scores : NDArray[np.float64] | Sequence[float]
        The input scores to convert to weights.
    method : Literal["softmax", "power", "rank", "linear"], default="softmax"
        The method to use for converting scores to weights.
    temperature : float, default=1.0
        The temperature parameter for the softmax function.
    power : float, default=2.0
        The power parameter for the power method.
    eps : float, default=1e-12
        A small value to avoid division by zero.

    Returns
    -------
    NDArray[np.float64] | NDArray[np.int64]
        The resulting weights.
    """

    scores = np.array(scores, dtype=np.float64)
    if scores.ndim != 1:
        scores = scores.flatten()

    if scores.size == 0:
        return np.empty((0,), dtype=np.float64)

    # for non-finite numbers, use a small value
    finite_mask = np.isfinite(scores)
    if not np.any(finite_mask):
        # uniform weights
        return np.repeat(1 / scores.size, scores.size)

    with np.errstate(**config.np_errstate):
        _min, _max = np.min(scores[finite_mask]), np.max(scores[finite_mask])
        _extra_min = 1.5 * _min - 0.5 * _max
        if not np.isfinite(_extra_min):
            _extra_min = _min
        scores[~finite_mask] = _extra_min

    if method == "softmax":
        scores = scores / max(temperature, eps)
        return softmax(scores)

    if method == "power":
        scores = scores - np.min(scores)
        weights = np.power(scores + eps, power)
        return weights / (np.sum(weights) + eps)

    if method == "rank":
        # higher score -> lower rank number -> higher weight
        ranks = np.argsort(np.argsort(scores))
        weights = np.power(len(scores) + 1 - ranks, power)
        return weights / (np.sum(weights) + eps)

    if method == "linear":
        weights = scores - np.min(scores)
        return weights / (np.sum(weights) + eps)

    raise ValueError(f"Unknown method: {method!r}")


def zipsort(
    val: NDArray[Any], /, *seqs: Sequence[Any], descending: bool = False
) -> tuple[NDArray[Any], *tuple[Sequence[Any], ...]]:
    """
    Sort multiple iterables based on the sorting order of a reference array.

    Parameters
    ----------
    val : NDArray[Any]
        The reference array to sort by. Must be 1D.
    *seqs : Sequence[Any]
        The sequences to sort in the same order as `val`.
    descending : bool, default=False
        Whether to sort in descending order.

    Returns
    -------
    tuple[NDArray[Any], *tuple[Sequence[Any], ...]]
        A tuple containing the sorted reference array and the sorted sequences.
    """
    val = np.asarray(val)
    if not val.ndim == 1:
        raise ValueError("Input array must be 1D.")

    if len(val) == 0:
        return (val,) + seqs

    if not all(len(seq) == len(val) for seq in seqs):
        raise ValueError(
            "All sequences must have the same length as the reference array."
        )

    indices = np.argsort(val)
    if descending:
        indices = indices[::-1]

    sorted_val = val[indices]
    idx = indices.tolist()
    sorted_sequences = tuple(
        seq[idx] if isinstance(seq, np.ndarray) else [seq[i] for i in idx]
        for seq in seqs
    )
    return (sorted_val,) + sorted_sequences
