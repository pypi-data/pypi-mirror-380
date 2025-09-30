"""
score functions and metrics
"""

from functools import partial
from typing import (
    Any,
    Final,
    Generic,
    Literal,
    Protocol,
    Self,
    Sequence,
    TypeGuard,
    final,
    overload,
)

import numpy as np
from numpy.typing import NDArray
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
    root_mean_squared_error,
)

from .config import config
from .typing import (
    ArrayLike,
    ArrayLikeT,
    BatchScoringOptions,
    NestedSequence,
    Number,
    ScalingCallable,
    ScalingOptions,
    ScoringOptions,
    scaling_options,
    T,
)


class _Missing:
    """
    Marker class for missing values.
    """

    @final
    def __bool__(self) -> bool:
        return False


_missing: Final[_Missing] = _Missing()


def _protected_log(
    value: ArrayLike | Sequence[Number] | Number, eps: float = 1e-10
) -> NDArray[np.float64]:
    """
    Compute the protected logarithm of the input array or number.

    Parameters
    ----------
    value : ArrayLike | Number
        The input array or number.
    eps : float, optional
        A small value to avoid log(0) errors. Default is 1e-10.

    Returns
    -------
    NDArray[np.float64]
        The protected logarithm of the input.
    """
    value = np.asarray(value, dtype=np.float64)
    return np.log10(np.maximum(np.abs(value), eps))


def _reverse_protected_log(
    value: ArrayLike | Sequence[Number] | Number, eps: float = 1e-10
) -> NDArray[np.float64]:
    """
    Compute the reverse protected logarithm of the input array or number.

    Parameters
    ----------
    value : ArrayLike | Number
        The input array or number.
    eps : float, optional
        A small value to avoid log(0) errors. Default is 1e-10.

    Returns
    -------
    NDArray[np.float64]
        The reverse protected logarithm of the input.
    """
    value = np.asarray(value, dtype=np.float64)
    return np.maximum(np.power(10, value), eps)


def is_scaler(scaling: Any, /) -> TypeGuard[ScalingOptions | None]:
    """
    Check if a scaling option is a valid scaler (scaling function).

    Parameters
    ----------
    scaling : Any
        The scaling option to check.

    Returns
    -------
    bool
        True if the scaling option is a valid scaler, False otherwise.
    """
    if scaling is None:
        return True
    if isinstance(scaling, str) and scaling in scaling_options:
        return True
    return False


@overload
def get_scaler(
    scaling: ScalingOptions, default: Any = _missing, /
) -> ScalingCallable: ...
@overload
def get_scaler(scaling: None, default: Any = _missing, /) -> None: ...
@overload
def get_scaler(
    scaling: ScalingOptions | None | Any, default: T = _missing, /
) -> ScalingCallable | None | T: ...


def get_scaler(
    scaling: ScalingOptions | None | Any, default: T = _missing, /
) -> ScalingCallable | None | T:
    """
    Get the scaling function based on the provided scaling option.

    Parameters
    ----------
    scaling : Literal["log", "plog", "square"] | None
        The scaling option to use. If None, no scaling will be applied.

    Returns
    -------
    ScalingCallable | None
        The scaling function, or None if no scaling is to be applied.

    Raises
    ------
    ValueError
        If the provided scaling option is not recognized.
    """
    if scaling is None:
        return None
    if isinstance(scaling, str):
        match scaling:
            case "log":
                return np.log10  # type: ignore
            case "plog":
                return _protected_log
            case "square":
                return np.square  # type: ignore
            case _:
                if default is not _missing:
                    return default
                raise ValueError(f"Unknown scaling method: {scaling!r}")
    if default is not _missing:
        return default
    raise ValueError(f"Invalid scaling method: {scaling!r}")


def get_inverse_scaler(
    scaling: ScalingOptions | None | Any, default: T = _missing, /
) -> ScalingCallable | None | T:
    """
    Get the inverse scaling function based on the provided scaling option.

    Parameters
    ----------
    scaling : Literal["log", "plog", "square"] | None
        The scaling option to use. If None, no scaling will be applied.

    Returns
    -------
    ScalingCallable | None
        The inverse scaling function, or None if no scaling is to be applied.

    Raises
    ------
    ValueError
        If the provided scaling option is not recognized.
    """
    if scaling is None:
        return None
    if isinstance(scaling, str):
        match scaling:
            case "log":
                return partial(np.power, 10)
            case "plog":
                return _reverse_protected_log
            case "square":
                return np.sqrt  # type: ignore
            case _:
                if default is not _missing:
                    return default
                raise ValueError(f"Unknown scaling method: {scaling!r}")
    if default is not _missing:
        return default
    raise ValueError(f"Invalid scaling method: {scaling!r}")


class ScoreFunction(Protocol):
    """
    A protocol that defines the interface for a scoring function. This protocol is used to represent
    a callable object that computes a score based on the true and predicted values, with optional
    sample weights and additional keyword arguments.

    Methods
    -------
    __call__(y_true, y_pred, *, sample_weight=None, **kwargs) -> float : Computes the score given
        the true values, predicted values, and optional sample weights and additional parameters.

    Parameters
    ----------
    y_true : ArrayLike | Number
        The ground truth values.
    y_pred : ArrayLike | Number
        The predicted values.
    sample_weight : ArrayLike | None, default=None
        Optional array of weights to apply to individual samples. Defaults to None.
    **kwargs : Any
        Additional keyword arguments for the scoring function.

    Returns
    -------
    float
        The computed score as a floating-point number.
    """

    def __call__(
        self,
        y_true: ArrayLike | NDArray[Any] | Number,
        y_pred: ArrayLike | NDArray[Any] | Number,
        *,
        sample_weight: ArrayLike | NDArray[Any] | None = None,
        **kwargs: Any,
    ) -> float: ...


class Scorer(Generic[ArrayLikeT]):
    """
    A class to encapsulate the scoring function and its parameters. The `__call__` method allows for
    easy invocation of the scoring function with the provided arguments, and the returned float
    value is always the greater the better.
    """

    def __init__(
        self,
        score_func: ScoreFunction,
        *,
        low: Number | None = None,
        high: Number | None = None,
        worst: Number | None = None,
        greater_is_better: bool = True,
        y_scaling: ScalingOptions | None = None,
    ) -> None:
        """
        Initialize the Scorer with the given parameters.

        Parameters
        ----------
        score_func : ScoreFunction
            The scoring function to use. The signature of the function should match the
            `ScoreFunction` protocol, which takes the following arguments:

                - `X`: The predicted values.
                - `y`: The true values.
                - `sample_weight`: Optional keyword argument for sample weights.

            The return value should always be a float. The return value will be further clipped to
            (low, high) definitions.
        low : Number | None, default=None (keyword-only)
            The lower bound for the returned value from the `score_func`.
        high : Number | None, default=None (keyword-only)
            The upper bound for the returned value from the `score_func`.
        worst : Number | None, default=None (keyword-only)
            The value to use when the returned value from the `score_func` is NaN or not finite.
            The worst value must not be `NaN` because it is used as a fallback in case of errors
            and the score is used to calculate mean/median/... statistics.

            The worst-case scenario value to use, regardless of `greater_is_better`. For example,
            for a loss metric, use a large positive number; for a score metric such as R2, use a
            large negative number.

            If None, then `greater_is_better` will be used to determine the worst-case scenario
            (either use `inf` or `-inf`.)
        greater_is_better : bool, default=True (keyword-only)
            Whether a greater score is better. If False, the score will be negated. Note that `low`,
            `high`, and `nan` definitions are **not** dependent on `greater_is_better`.
        y_scaling : Literal["log"] | None, default=None (keyword-only)
            The pre-scaling method to apply to input true values and predicted values before passing
            them to the scoring/loss function.

            - `log`: Apply logarithmic scaling, which can be useful if the values span across
              several orders of magnitude and are not normally distributed. For example, in non-log
              scale, large values can dominate the loss function, making it difficult to optimize
              accuracy for small values.
            - `square`: Apply square scaling, which can be useful for emphasizing larger values. But
              since least square already has a built-in mechanism for handling this, it may not be
              necessary to apply additional scaling.
            - `None`: No pre-scaling will be applied.
        """
        self.score_func = score_func
        self.low = -float("inf") if low is None else low
        self.high = float("inf") if high is None else high
        self.greater_is_better = greater_is_better
        self.worst = worst
        self.y_scaling = y_scaling

    @property
    def low(self) -> float:
        """
        The lower bound of the scorer.
        """
        return self._low

    @low.setter
    def low(self, value: float | None) -> None:
        """
        Set the lower bound of the scorer.
        """
        if value is not None and not np.isnan(value):
            self._low = value
        else:
            self._low = -float("inf")

        if hasattr(self, "_high") and self._low >= self._high:
            raise ValueError("low must be less than high.")

    @property
    def high(self) -> float:
        """
        The upper bound of the scorer.
        """
        return self._high

    @high.setter
    def high(self, value: float | None) -> None:
        """
        Set the upper bound of the scorer.
        """
        if value is not None and not np.isnan(value):
            self._high = value
        else:
            self._high = float("inf")

        if hasattr(self, "_low") and self._low >= self._high:
            raise ValueError("low must be less than high.")

    @property
    def worst(self) -> float:
        """
        The worst-case scenario value of the scorer.
        """
        _worst = self._worst
        if _worst is not None and not np.isnan(_worst):
            return _worst
        if not hasattr(self, "greater_is_better"):
            raise ValueError(
                "Cannot determine worst-case scenario without greater_is_better."
            )
        if self.greater_is_better:
            return float("-inf")
        return float("inf")

    @worst.setter
    def worst(self, value: float | None) -> None:
        """
        Set the worst-case scenario value of the scorer.
        """
        if value is not None and np.isnan(value):
            raise ValueError("Worst-case scenario value cannot be NaN.")
        self._worst = value

    @property
    def y_scaling(self) -> ScalingOptions | None:
        """
        The pre-scaling function of the scorer.
        """
        return self._pre_scaling

    @y_scaling.setter
    def y_scaling(self, value: ScalingOptions | None) -> None:
        """
        Set the pre-scaling function of the scorer.
        """
        if not is_scaler(value):
            raise ValueError("Invalid y_scaling value.")
        self._pre_scaling: ScalingOptions | None = value

    def __call__(
        self,
        y_true: ArrayLikeT | NDArray[Any] | Number,
        y_pred: ArrayLikeT | NDArray[Any] | Number,
        sample_weight: ArrayLikeT | NDArray[Any] | None = None,
    ) -> float:
        """
        Call the scoring function with the provided arguments.

        Parameters
        ----------
        y_true : ArrayLikeT | Number
            The true values.
        y_pred : ArrayLikeT | Number
            The predicted values.
        sample_weight : ArrayLikeT | None, default=None
            Sample weights for the scoring function.

        Returns
        -------
        float
            The computed score.
        """
        with np.errstate(**config.np_errstate):
            try:
                scaler = get_scaler(self.y_scaling, None)
                if scaler:
                    y_true = scaler(np.asarray(y_true))
                    y_pred = scaler(np.asarray(y_pred))
                score = self.score_func(y_true, y_pred, sample_weight=sample_weight)
            except:
                score = float("nan")

        if not np.isfinite(score):
            score = self.worst
        score = float(np.clip(score, self.low, self.high))

        if self.greater_is_better:
            return score
        return -score

    def new(self, **kwargs: Any) -> Self:
        """
        Get a new :class:`Scorer` instance with updated parameters.

        Parameters
        ----------
        **kwargs : Any
            Any __init__ parameters to update. You only nned to provide the ones you want to update.

        Returns
        -------
        Self
            A new :class:`Scorer` instance with the updated parameters.
        """
        kwargs.setdefault("score_func", self.score_func)
        kwargs.setdefault("low", self.low)
        kwargs.setdefault("high", self.high)
        kwargs.setdefault("worst", self.worst)
        kwargs.setdefault("greater_is_better", self.greater_is_better)
        kwargs.setdefault("y_scaling", self.y_scaling)

        return self.__class__(**kwargs)

    def __repr__(self) -> str:
        """
        Return a string representation of the scorer.
        """
        if not self.greater_is_better:
            greater_better = f", greater_is_better={self.greater_is_better}"
        else:
            greater_better = ""
        if isinstance(self.y_scaling, str):
            y_scaling = f", y_scaling={self.y_scaling!r}"
        elif callable(self.y_scaling):
            y_scaling = f", y_scaling={self.y_scaling.__qualname__}"
        else:
            y_scaling = ""

        return (
            f"{self.__class__.__name__}(<{self.score_func.__qualname__}>, "
            f"low={self.low}, high={self.high}, worst={self.worst}, ..."
            f"{greater_better}{y_scaling})"
        )

    def __str__(self) -> str:
        """
        Return a simplified string representation of the scorer.
        """
        return f"{self.__class__.__name__}(<{self.score_func.__qualname__}>)"


mean_absolute_error_scorer = Scorer(
    mean_absolute_error, greater_is_better=False  # type: ignore
)
mean_absolute_percentage_error_scorer = Scorer(
    mean_absolute_percentage_error, greater_is_better=False  # type: ignore
)
mean_squared_error_scorer = Scorer(
    mean_squared_error, greater_is_better=False  # type: ignore
)
root_mean_squared_error_scorer = Scorer(
    root_mean_squared_error, greater_is_better=False  # type: ignore
)
r2_scorer = Scorer(
    r2_score, low=-1.0, high=1.0, worst=-1.0, greater_is_better=True  # type: ignore
)

# use log scaling
log_mean_absolute_error_scorer = mean_absolute_error_scorer.new(y_scaling="log")
log_mean_absolute_percentage_error_scorer = mean_absolute_percentage_error_scorer.new(
    y_scaling="log"
)
log_mean_squared_error_scorer = mean_squared_error_scorer.new(y_scaling="log")
log_root_mean_squared_error_scorer = root_mean_squared_error_scorer.new(y_scaling="log")
log_r2_scorer = r2_scorer.new(y_scaling="log")

# all keys should be in lowercase
scorers: dict[ScoringOptions | str, Scorer] = {
    "mae": mean_absolute_error_scorer,
    "mape": mean_absolute_percentage_error_scorer,
    "mse": mean_squared_error_scorer,
    "rmse": root_mean_squared_error_scorer,
    "r2": r2_scorer,
    "log_mae": log_mean_absolute_error_scorer,
    "log_mape": log_mean_absolute_percentage_error_scorer,
    "log_mse": log_mean_squared_error_scorer,
    "log_rmse": log_root_mean_squared_error_scorer,
    "log_r2": log_r2_scorer,
}


@overload
def get_scorer(
    name: ScoringOptions | Scorer[Any], default: Any = None, /
) -> Scorer[Any]: ...
@overload
def get_scorer(name: str, default: Scorer[Any], /) -> Scorer[Any]: ...
@overload
def get_scorer(name: str, default: T = None, /) -> T: ...


def get_scorer(
    scoring: ScoringOptions | str | Scorer[Any], default: T = None, /
) -> Scorer[Any] | T:
    """
    Parse a scoring parameter and return the scorer by name. If not found, return the default value.

    Parameters
    ----------
    scoring : Literal["mae", "mse", "rmse", "r2"] | str | Scorer[Any]
        The name of the scorer to retrieve (or the scorer itself). The name is case-insensitive.
    default : Scorer[Any] | None, default=None
        The default scorer to return if the requested scorer is not found.

    Returns
    -------
    Any
        The requested scorer, or the default scorer if not found.
    """
    if isinstance(scoring, Scorer):
        return scoring
    return scorers.get(scoring.lower(), default)


@overload
def is_scorer(scoring: Scorer[Any]) -> Literal[True]: ...
@overload
def is_scorer(scoring: ScoringOptions | str | Any) -> bool: ...


def is_scorer(scoring: ScoringOptions | str | Scorer[Any] | Any) -> bool:
    """
    Check if the provided scoring can be parsed as a valid scorer.

    Parameters
    ----------
    scoring : ScoringOptions | str | Scorer | Any
        The scoring to check.

    Returns
    -------
    bool
        True if the scoring is a valid scorer, False otherwise.
    """
    if isinstance(scoring, Scorer):
        return True
    if isinstance(scoring, str) and scoring.lower() in scorers:
        return True
    return False


def set_scorer(
    scoring: ScoringOptions | str, scorer: Scorer[Any], /, overwrite: bool = False
) -> None:
    """
    Set a scorer by name. If the name already exists, it will be overwritten if `overwrite` is True.

    Parameters
    ----------
    scoring : Literal["mae", "mse", "rmse", "r2"] | str
        The name of the scorer to set. The name is case-insensitive and will be converted to
        lowercase.
    scorer : Scorer
        The scorer to set.
    overwrite : bool, default=False
        Whether to overwrite an existing scorer with the same name.

    Raises
    ------
    ValueError
        If the scorer already exists and `overwrite` is False.
    """
    scoring = scoring.lower()
    if not overwrite and scoring in scorers:
        raise ValueError(
            f"Scorer {scoring!r} already exists. " "Use 'overwrite=True' to replace it."
        )

    scorers[scoring] = scorer


def is_batch_scorer(scoring: BatchScoringOptions | str | float | Any, /) -> bool:
    """
    Check if the provided scoring can be parsed as a valid batch scorer.

    Parameters
    ----------
    scoring : BatchScoringOptions | str | float | Any
        The scoring to check.

    Returns
    -------
    bool
        True if the scoring is a valid batch scorer, False otherwise.
    """
    if isinstance(scoring, float) and scoring >= 0 and scoring <= 1:
        return True
    if isinstance(scoring, str):
        if scoring.lower() in {"mean", "median", "max", "min"}:
            return True
    return False


def digest_batch_scores(
    scores: NDArray[np.float64] | ArrayLike | NestedSequence,
    batch_scoring: BatchScoringOptions | str = "median",
    batch_weight: ArrayLikeT | None = None,
) -> float:
    """
    Get the mean/median/max/min/... score digest from a sequence of scores.

    Parameters
    ----------
    scores : NDArray[np.float64] | ArrayLike
        The sequence of scores to digest/summarize.
    batch_scoring : Literal["mean", "median", "max", "min"] | float, default="median"
        The name of the batch scoring function to retrieve. The name is case-insensitive.

        - `mean`: return the mean of the scores.
        - `median`: return the median of the scores.
        - `max`: return the maximum of the scores.
        - `min`: return the minimum of the scores.
        - *float*: If a float is provided, it will be used as a quantile. The value must be between
          0 and 1, inclusive.

    batch_weight : ArrayLikeT | None, default=None
        The weights to apply to each batch. If None, all batches are weighted equally.

    Returns
    -------
    float
        The digest of the scores.

    Raises
    ------
    ValueError
        If the provided `batch_scoring` is not recognized.
    """
    all_scores = np.asarray(scores, dtype=np.float64).flatten()
    if len(all_scores) == 0:
        raise ValueError("Scores array is empty.")

    if batch_weight is None:
        weights = None
        quantile_method = "linear"
    else:
        weights = np.asarray(batch_weight, dtype=np.float64).flatten()
        if len(weights) != len(all_scores):
            raise ValueError("Batch weight must be the same length as scores.")
        if np.any(weights < 0) and np.isclose(np.sum(weights), 0):
            raise ValueError(
                "Batch weights must be non-negative and have at least one positive weight."
            )
        if np.all(np.isclose(weights[1:], weights[0])):
            weights = None
            quantile_method = "linear"
        else:
            weights = weights / np.sum(weights)
            quantile_method = "inverted_cdf"

    # for non-finite numbers, use a small value
    finite_mask = np.isfinite(all_scores)
    if not np.any(finite_mask):
        return float("-inf")

    all_scores[~finite_mask] = -np.inf
    with np.errstate(**config.np_errstate):
        if len(all_scores) == 1:
            return float(all_scores[0])
        elif isinstance(batch_scoring, str):
            match batch_scoring.lower():
                case "mean":
                    val = float(np.average(all_scores, weights=weights))
                case "median":
                    val = float(
                        np.quantile(
                            all_scores, 0.5, method=quantile_method, weights=weights
                        )
                    )
                case "max":
                    val = float(np.max(all_scores))
                case "min":
                    val = float(np.min(all_scores))
                case _:
                    raise ValueError(f"Unknown batch scoring method: {batch_scoring!r}")

        elif isinstance(batch_scoring, (int, float)):
            if not (0 <= batch_scoring <= 1):
                raise ValueError("Quantile must be between 0 and 1.")
            val = float(
                np.quantile(
                    all_scores, batch_scoring, method=quantile_method, weights=weights
                )
            )

        else:
            raise ValueError(f"Invalid batch scoring method: {batch_scoring!r}")

    if not np.isfinite(val):
        return float("-inf")
    return val
