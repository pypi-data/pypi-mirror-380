"""
Parametric Symbolic Regression
"""

from collections import defaultdict
from itertools import zip_longest
from multiprocessing import Pool
from typing import (
    Any,
    Callable,
    Final,
    Generic,
    Iterable,
    Literal,
    NoReturn,
    Optional,
    Self,
    Sequence,
    final,
    overload,
)
import warnings

import numpy as np
from numpy.typing import NDArray
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.exceptions import NotFittedError

from .base.func_unit import Constant, DelayedConstant, FuncUnit, Operation, Variable
from .config import config
from .expression import Expression
from .expression_builder import ExpressionBuilder, ExpressionTracker
from .logging import logger
from .metrics import Scorer, get_scorer, is_batch_scorer, is_scaler, is_scorer
from .typing import (
    ArrayLikeT,
    BatchScoringOptions,
    NestedSequence,
    Number,
    OptimizeOptions,
    RankingOptions,
    RngGeneratorSeed,
    ScalingOptions,
    ScipyCurveFitFunction,
    ScipyCurveFitOptions,
    ScipyMinimizeFunction,
    ScipyMinimizeOptions,
    ScoringOptions,
)
from .utils import compute_n_cpus, scores_to_weights


class _Missing:
    """
    Marker class for missing values.
    """

    @final
    def __bool__(self) -> bool:
        return False


_missing: Final[_Missing] = _Missing()


@overload
def _batch_evaluate_per_expression(
    expression: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
    X: Sequence[ArrayLikeT],
    y: Sequence[ArrayLikeT],
    sample_weight: Sequence[ArrayLikeT | None] | None = None,
    optimize_with: OptimizeOptions = "curve_fit",
    func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
    curve_fit_y_scaling: Optional[ScalingOptions] = None,
    curve_fit_options: Optional[ScipyCurveFitOptions] = None,
    func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
    minimize_scoring: ScoringOptions | str | Scorer = "rmse",
    minimize_options: ScipyMinimizeOptions | None = None,
    scoring: ScoringOptions | str | Scorer = "rmse",
    batch_scoring: BatchScoringOptions | str = "median",
    batch_weight: ArrayLikeT | None = None,
    random_state: RngGeneratorSeed = None,
    n_jobs: int | None = None,
) -> float: ...
@overload
def _batch_evaluate_per_expression(
    expression: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
    X: Sequence[ArrayLikeT],
    y: Sequence[ArrayLikeT],
    sample_weight: Sequence[ArrayLikeT | None] | None,
    optimize_with: OptimizeOptions,
    func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]],
    curve_fit_y_scaling: Optional[ScalingOptions],
    curve_fit_options: Optional[ScipyCurveFitOptions],
    func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None,
    minimize_scoring: ScoringOptions | str | Scorer,
    minimize_options: ScipyMinimizeOptions | None,
    scoring: ScoringOptions | str | Scorer,
    batch_scoring: None,
    batch_weight: ArrayLikeT | None = None,
    random_state: RngGeneratorSeed = None,
    n_jobs: int | None = None,
) -> NDArray[np.float64]: ...
@overload
def _batch_evaluate_per_expression(
    expression: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
    X: Sequence[ArrayLikeT],
    y: Sequence[ArrayLikeT],
    sample_weight: Sequence[ArrayLikeT | None] | None = None,
    optimize_with: OptimizeOptions = "curve_fit",
    func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
    curve_fit_y_scaling: Optional[ScalingOptions] = None,
    curve_fit_options: Optional[ScipyCurveFitOptions] = None,
    func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
    minimize_scoring: ScoringOptions | str | Scorer = "rmse",
    minimize_options: ScipyMinimizeOptions | None = None,
    scoring: ScoringOptions | str | Scorer = "rmse",
    *,
    batch_scoring: None,
    batch_weight: ArrayLikeT | None = None,
    random_state: RngGeneratorSeed = None,
    n_jobs: int | None = None,
) -> NDArray[np.float64]: ...
@overload
def _batch_evaluate_per_expression(
    expression: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
    X: Sequence[ArrayLikeT],
    y: Sequence[ArrayLikeT],
    sample_weight: Sequence[ArrayLikeT | None] | None = None,
    optimize_with: OptimizeOptions = "curve_fit",
    func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
    curve_fit_y_scaling: Optional[ScalingOptions] = None,
    curve_fit_options: Optional[ScipyCurveFitOptions] = None,
    func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
    minimize_scoring: ScoringOptions | str | Scorer = "rmse",
    minimize_options: ScipyMinimizeOptions | None = None,
    scoring: ScoringOptions | str | Scorer = "rmse",
    batch_scoring: BatchScoringOptions | str | None = "median",
    batch_weight: ArrayLikeT | None = None,
    random_state: RngGeneratorSeed = None,
    n_jobs: int | None = None,
) -> float | NDArray[np.float64]: ...


def _batch_evaluate_per_expression(
    expression: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
    X: Sequence[ArrayLikeT],
    y: Sequence[ArrayLikeT],
    sample_weight: Sequence[ArrayLikeT | None] | None = None,
    optimize_with: OptimizeOptions = "curve_fit",
    func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
    curve_fit_y_scaling: Optional[ScalingOptions] = None,
    curve_fit_options: Optional[ScipyCurveFitOptions] = None,
    func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
    minimize_scoring: ScoringOptions | str | Scorer = "rmse",
    minimize_options: ScipyMinimizeOptions | None = None,
    scoring: ScoringOptions | str | Scorer = "rmse",
    batch_scoring: BatchScoringOptions | str | None = "median",
    batch_weight: ArrayLikeT | None = None,
    random_state: RngGeneratorSeed = None,
    n_jobs: int | None = None,
) -> float | NDArray[np.float64]:
    """
    Fits one :class:`Expression` model to a series of data (X-y pairs), and for each batch, compute
    the score between the predicted values and the true values.

    This function calls :func:`psr.expression.Expression.batch_fit_score` directly.

    Parameters
    ----------
    expression : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
        The expression to use for fitting and scoring.
    X : Sequence[ArrayLikeT]
        The input data, a 3D array or a list of 2D arrays.
    y : Sequence[ArrayLikeT]
        The target values, a 2D array or a list of 1D arrays.
    sample_weight : ArrayLikeT | None, default=None
        The sample weights. Should match the shape of y; a 2D array or a list of 1D arrays/None.
    optimize_with : OptimizeOptions, default="curve_fit" (keyword-only)
        The optimization method to use for fitting the model.

        - `curve_fit` uses :func:`scipy.optimize.curve_fit` for a more robust fitting process.
        - `minimize` uses :func:`scipy.optimize.minimize` for a more flexible fitting process,
            with a custom loss function.

    func_curve_fit, curve_fit_y_scaling, curve_fit_options : Any
        See :func:`psr.expression.Expression.fit`.
    func_minimize, minimize_scoring, minimize_options : Any
        See :func:`psr.expression.Expression.fit`.
    scoring : ScoringOptions | str | Scorer, default="rmse"
        The scoring method to use between the predicted values (after fitting) and the true
        values. A score is returned as a single float value, with higher values indicating a
        better fit. For a loss-based metric, its negative will be returned as the score.

        **Difference between `minimize_scoring` and `scoring`**

        - `minimize_scoring` is used during the optimization process to find the optimal values
          for the delayed constants that would give the best fit.
        - `scoring` is used after the model has been fitted to evaluate its performance on the
          training data. It can be the same as `minimize_scoring` or different. The final reported
          score between the predicted values (after fitting) and the true values will be computed
          using the specified `scoring` method.

    batch_scoring : BatchScoringOptions | str | None, default="median"
        The batch scoring method to use.

        - `None`: the returned value will be an array of scores, each score for each batch data.
        - `mean`: the returned value will be the mean score across all batches.
        - `median`: the returned value will be the median score across all batches.
        - `max`: the returned value will be the maximum score across all batches.
        - `min`: the returned value will be the minimum score across all batches.
        - *float*: a quantile value between 0 and 1 (inclusive). The returned value will be the
          score at the specified quantile across all batches.

    batch_weight : ArrayLikeT | None = None
        The weight to apply to each batch for a digested score of all batches with `batch_scoring`.
        If `None`, all batches are equally weighted.
    random_state : RngGeneratorSeed, default=None
        The random seed to use for the optimization process to perturb the initial guess.
    n_jobs : int | None, default=None
        The number of jobs to run in parallel. `None`, `0`, or `1` will use the parent process
        and **NOT** use multiple processes. `-1` will use all available cores.

    Returns
    -------
    float | NDArray[np.float64]
        The scores for each batch, or a digested score of all batches.

    See Also
    --------
    psr.expression.Expression.batch_fit_score : The base method for fitting and scoring the
        expression.
    """
    if isinstance(expression, ExpressionTracker):
        expression = expression.to_expression()
    return expression.batch_fit_score(
        X,
        y,
        sample_weight=sample_weight,
        optimize_with=optimize_with,
        func_curve_fit=func_curve_fit,
        curve_fit_y_scaling=curve_fit_y_scaling,
        curve_fit_options=curve_fit_options,
        func_minimize=func_minimize,
        minimize_scoring=minimize_scoring,
        minimize_options=minimize_options,
        scoring=scoring,
        batch_scoring=batch_scoring,
        batch_weight=batch_weight,
        random_state=random_state,
        n_jobs=n_jobs,
    )


def _batch_evaluate(
    expressions: Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]],
    X: Sequence[ArrayLikeT],
    y: Sequence[ArrayLikeT],
    sample_weight: Sequence[ArrayLikeT | None] | None = None,
    optimize_with: OptimizeOptions = "curve_fit",
    func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
    curve_fit_y_scaling: Optional[ScalingOptions] = None,
    curve_fit_options: Optional[ScipyCurveFitOptions] = None,
    func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
    minimize_scoring: ScoringOptions | str | Scorer = "rmse",
    minimize_options: ScipyMinimizeOptions | None = None,
    scoring: ScoringOptions | str | Scorer = "rmse",
    batch_scoring: BatchScoringOptions | str | None = "median",
    batch_weight: ArrayLikeT | None = None,
    random_state: RngGeneratorSeed = None,
    n_jobs: int | None = None,
) -> NDArray[np.float64]:
    """
    Similar to :func:`_batch_evaluate_per_expression`, but fits multiple expressions to all batches.

    Parameters
    ----------
    expressions : Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]]
        The sequence of expressions or expression trackers to fit.

    Returns
    -------
    NDArray[np.float64]
        The scores for each batch, or a digested score of all batches. When `batch_scoring` is:

        - `None`: the returned value will be a 2D array of shape (n_expressions, n_batches), with
          each row representing the score of one expression on all batches.
        - *str*: the returned value will be a 1D array of shape (n_expressions,), with each element
          representing the digested score (mean/median/...) of the scores from one expression on
          all batches.
    """
    expression_list: list[Expression[ArrayLikeT]] = [
        expr.to_expression() if isinstance(expr, ExpressionTracker) else expr
        for expr in expressions
    ]
    n_exp = len(expression_list)
    n_batch = len(X)
    n_cpus = min(max(n_exp, n_batch), compute_n_cpus(n_jobs))
    if n_cpus < 1:
        raise ValueError("The number of expressions and batches must be positive.")

    rng = np.random.default_rng(random_state)
    if n_cpus < 2 or n_batch > n_exp:
        # no parallelization or parallelize within one expression
        random_states = rng.choice(2**32 - 1, size=n_exp, replace=False)
        results = [
            _batch_evaluate_per_expression(
                expr,
                X,
                y,
                sample_weight=sample_weight,
                optimize_with=optimize_with,
                func_curve_fit=func_curve_fit,
                curve_fit_y_scaling=curve_fit_y_scaling,
                curve_fit_options=curve_fit_options,
                func_minimize=func_minimize,
                minimize_scoring=minimize_scoring,
                minimize_options=minimize_options,
                scoring=scoring,
                batch_scoring=batch_scoring,
                batch_weight=batch_weight,
                random_state=rs,
                n_jobs=n_jobs,
            )
            for expr, rs in zip(expression_list, random_states)
        ]
    else:
        # parallelize across expressions
        with config.multiprocessing(), Pool(n_cpus) as pool:
            random_states = rng.choice(2**32 - 1, size=n_exp, replace=False)
            results = pool.starmap(
                _batch_evaluate_per_expression,
                [
                    (
                        expr,
                        X,
                        y,
                        sample_weight,
                        optimize_with,
                        func_curve_fit,
                        curve_fit_y_scaling,
                        curve_fit_options,
                        func_minimize,
                        minimize_scoring,
                        minimize_options,
                        scoring,
                        batch_scoring,
                        batch_weight,
                        rs,
                        1,
                    )
                    for expr, rs in zip(expression_list, random_states)
                ],
            )

    # results is a list of numpy arrays; consolidate into one numpy array
    if batch_scoring is None:
        return np.vstack(results)
    return np.asarray(results)


def _array_factory() -> NDArray[np.float64]:
    return np.empty((0,), dtype=np.float64)


class ParametricSR(RegressorMixin, BaseEstimator, Generic[ArrayLikeT]):
    """
    Parametric Symbolic Regression

    This model uses genetic algorithm to perform parametric symbolic regression. In addition to the
    traditional symbolic regression techniques, it incorporates the concept of a delayed
    constant/variable that can be decided during fitting.

    For example, the model can propose an expression with the form :math:`f(x) = a * x + 1`, where
    :math:`a` is a delayed constant that can be optimized during the fitting process to better fit
    the data. Why? Because the model does not need to rely on random selection of real values with
    this feature, which can produce more accurate and reliable results.

    Parameters
    ----------
    expression_builder : ExpressionBuilder | None, default=None
        The expression builder to use for generating candidate expressions.

        See :class:`ExpressionBuilder` for more details.
    n_gen : int, default=10
        The number of generations to run the evolutionary algorithm.
    n_per_gen: int, default=200
        The number of individuals (population size) to generate and evaluate per generation.
    n_elite : int, default=10
        The number of elite individuals to keep for the next generation. The top elites with the
        best performances are directly kept without going through weighted selection.
    n_survivor : int, default=20
        The number of individuals to keep for the next generation. After keeping the top elites, the
        rest of the population is ranked and randomly selected, weighted on their performances.
    propagate_seeds : bool, default=True
        Whether to propagate the initial seed individuals across generations. The `seeds` are user
        generated expressions from their domain expertise to help guide the search process.

        If propagate, the seed expressions will be preserved and used in subsequent generations.
        Otherwise, they are only evaluated and selected on the initial generation, and may get
        washed out if their performance is not competitive.
    minimize_scoring : ScoringOptions | str | Scorer, default="rmse"
        The scoring method to use for minimizing the objective function.

        See :func:`psr.expression.Expression.fit`.
    minimize_options : ScipyMinimizeOptions | None, default=None
        Options to pass to the scipy minimize function.

        See :func:`psr.expression.Expression.fit`.
    scoring : ScoringOptions | str | Scorer, default="rmse"
        The scoring method to use for evaluating the predicted values and the true values per batch
        data.

        See :func:`psr.expression.Expression.fit_score`.
    batch_scoring : BatchScoringOptions | str, default="median"
        The batch scoring method to use for digesting (e.g., averaging) the scores across multiple
        batches of data.

        Combined with `scoring`, `batch_scoring` determines how well an :class:`Expression` fits the
        data and produces the raw scores.

        See :func:`psr.expression.Expression.batch_fit_score`.
    filter_duplicates : bool, default=True
        Whether to filter out offspring expressions that are duplicates of their parents. This can
        accelerate the search process by reducing the number of similar expressions and allow the
        search to explore more diverse solutions.

        Note: Duplicates within the same generation/population are filtered out by default to speed
        up evaluation.
    filter_func : Callable[[Expression], bool] | int | None, default=None
        A function to filter out undesirable expressions. Either:

        - A callable function that takes an expression as input and returns a boolean value.
        - A integer representing the maximum number of :class:`psr.base.func_unit.DelayedConstant`
            instances allowed in the expression (inclusive).
        - No filtering (i.e., keep all expressions).

    penalty_func : Callable[[Expression], float] | float, default=1e-3
        A function to compute a penalty for complex expressions. The penalty is applied to the raw
        scores to compute the fitness scores. Penalties must be positive.

        `penalty_func` can be one of:

        - A callable function that takes an expression as input and returns a float value as the
        penalty (should be positive).
        - A float representing the coefficient to apply to the `cost` of an :class:`Expression`.
        The coefficient will be multiplied by the `cost` to compute the final penalty. It should be
        positive.

        You should consider `scoring` and `batch_scoring` when designing your `penalty_func`.
    ranking_method : RankingOptions, default="softmax"
        The method to use for ranking individuals and converting their scores to weights for the
        random selection (survival of the fittest).

        See more details in :func:`~psr.utils.scores_to_weights`.
    sort_with : Literal["raw", "fitness"] = "fitness"
        The method to use for sorting individuals. Can be either "raw" for raw scores or "fitness"
        for fitness scores (penalized raw scores).

        This will affect how each generation is ordered in the fitted results and how the best
        estimator is selected. This does not affect the survival-of-the-fittest selection process,
        which always uses fitness scores.
    n_gen_no_change : int | None, default=None
        The number of generations to wait for improvement before stopping the search.
    warm_start : bool, default=False
        Whether to warm start the optimization process. When enabled, the search process will resume
        from the last fully-evaluated generation. Otherwise, the fitting starts from scratch.
    n_jobs : int | None, default=1
        The number of jobs to run in parallel.
    random_state : RngGeneratorSeed | None, default=None
        The random seed to use for reproducibility.
    verbose: int, default=0
        The verbosity level of the output. This controls the number of individual performances
        logged during the fitting process. The top `n` performances will be logged per generation,
        where `n` is determined by the `verbose` parameter (must be an integer).

    Attributes
    ----------
    fitted_data_ : Literal["batch", "single"]
        Whether the model was fitted on batches/series of data (multiple curves/surfaces), or a
        single batch of data (one curve/surface).
    trackers_ : dict[int, list[Expression[ArrayLikeT]]]
        A dictionary mapping generation indices to lists of tracked expressions
        (:class:`ExpressionTracker`). These are the expressions that were generated, evaluated, and
        selected during the search process.
    gens_ : list[int]
        A list of generation indices that were recorded in `trackers_`.
    estimators_ : list[Expression[ArrayLikeT]]
        A list of the best estimators found during the search process.
    raw_scores_ : NDArray[np.float64]
        The raw scores associated with the `estimators_`.
    fitness_scores_ : NDArray[np.float64]
        The fitness scores (penalized raw scores) associated with the `estimators_`.
    best_estimator_idx_ : tuple[int, int]
        The (gen, idx) of the best estimator found during the search.
    best_estimator_ : Expression[ArrayLikeT]
        The best estimator found during the search. Should correspond to the `best_estimator_idx_`.

        Equivalent to `self.estimators_[self.best_estimator_idx_[1]]` or
        `self.trackers_[self.best_estimator_idx_[0]][self.best_estimator_idx_[1]]`.
    """

    def __init__(
        self,
        expression_builder: ExpressionBuilder[ArrayLikeT] | None = None,
        n_gen: int = 10,
        n_per_gen: int = 200,
        n_elite: int = 10,
        n_survivor: int = 20,
        propagate_seeds: bool = True,
        optimize_with: OptimizeOptions = "curve_fit",
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        scoring: ScoringOptions | str | Scorer = "rmse",
        batch_scoring: BatchScoringOptions | str = "median",
        filter_duplicates: bool = True,
        filter_func: Callable[[Expression[ArrayLikeT]], bool] | int | None = 4,
        penalty_func: Callable[[Expression[ArrayLikeT]], float] | float = 1e-3,
        ranking_method: RankingOptions = "softmax",
        sort_with: Literal["raw", "fitness"] = "fitness",
        n_gen_no_change: int | None = None,
        warm_start: bool = False,
        n_jobs: int | None = 1,
        random_state: RngGeneratorSeed = None,
        verbose: int = 0,
    ) -> None:
        """
        Initializes the Parametric Symbolic Regression model.

        Parameters
        ----------
        expression_builder : ExpressionBuilder | None, default=None
            The expression builder to use for generating candidate expressions.

            See :class:`ExpressionBuilder` for more details.
        n_gen : int, default=10
            The number of generations to run the evolutionary algorithm.
        n_per_gen : int, default=200
            The number of individuals (population size) to generate and evaluate per generation.
        n_elite : int, default=10
            The number of elite individuals to keep for the next generation. The top elites with the
            best performances are directly kept without going through weighted selection.
        n_survivor : int, default=20
            The number of individuals to keep for the next generation. After keeping the top elites,
            the rest of the population is ranked and randomly selected, weighted on their
            performances.
        propagate_seeds : bool, default=True
            Whether to propagate the initial seed individuals across generations. The `seeds` are
            user generated expressions from their domain expertise to help guide the search process.

            If propagate, the seed expressions will be preserved and used in subsequent generations.
            Otherwise, they are only evaluated and selected on the initial generation, and may get
            washed out if their performance is not competitive.
        minimize_scoring : ScoringOptions | str | Scorer, default="rmse"
            The scoring method to use for minimizing the objective function.

            See :func:`psr.expression.Expression.fit`.
        minimize_options : ScipyMinimizeOptions | None, default=None
            Options to pass to the scipy minimize function.

            See :func:`psr.expression.Expression.fit`.
        scoring : ScoringOptions | str | Scorer, default="rmse"
            The scoring method to use for evaluating the predicted values and the true values per
            batch data.

            See :func:`psr.expression.Expression.fit_score`.
        batch_scoring : BatchScoringOptions | str, default="median"
            The batch scoring method to use for digesting (e.g., averaging) the scores across
            multiple batches of data.

            Combined with `scoring`, `batch_scoring` determines how well an :class:`Expression` fits
            the data and produces the raw scores.

            See :func:`psr.expression.Expression.batch_fit_score`.
        filter_duplicates : bool, default=True
            Whether to filter out offspring expressions that are duplicates of their parents. This
            can accelerate the search process by reducing the number of similar expressions and
            allow the search to explore more diverse solutions.

            Note: Duplicates within the same generation/population are filtered out by default to
            speed up evaluation.
        filter_func : Callable[[Expression], bool] | int | None, default=None
            A function to filter out undesirable expressions. Either:

            - A callable function that takes an expression as input and returns a boolean value.
            - A integer representing the maximum number of :class:`psr.base.func_unit.DelayedConstant`
              instances allowed in the expression (inclusive).
            - No filtering (i.e., keep all expressions).

        penalty_func : Callable[[Expression], float] | float, default=1e-3
            A function to compute a penalty for complex expressions. The penalty is applied to the
            raw scores to compute the fitness scores. Penalties must be positive.

            `penalty_func` can be one of:

            - A callable function that takes an expression as input and returns a float value as the
            penalty (should be positive).
            - A float representing the coefficient to apply to the `cost` of an :class:`Expression`.
            The coefficient will be multiplied by the `cost` to compute the final penalty. It should
            be positive.

            You should consider `scoring` and `batch_scoring` when designing your `penalty_func`.
        ranking_method: RankingOptions, default="softmax"
            The method to use for ranking individuals and converting their scores to weights for
            the random selection (survival of the fittest).

            See more details in :func:`~psr.utils.scores_to_weights`.
        sort_with: Literal["raw", "fitness"] = "fitness"
            The method to use for sorting individuals. Can be either "raw" for raw scores or
            "fitness" for fitness scores (penalized raw scores).

            This will affect how each generation is ordered in the fitted results and how the best
            estimator is selected. This does not affect the survival-of-the-fittest selection
            process, which always uses fitness scores.
        n_gen_no_change : int | None, default=None
            The number of generations to wait for improvement before stopping the search.
        warm_start: bool, default=False
            Whether to warm start the optimization process. When enabled, the search process will
            resume from the last fully-evaluated generation. Otherwise, the fitting starts from
            scratch.
        n_jobs: int | None, default=1
            The number of jobs to run in parallel.
        random_state: RngGeneratorSeed | None, default=None
            The random seed to use for reproducibility.
        verbose: int, default=0
            The verbosity level of the output.
        """

        params: dict[str, Any] = {}
        self.expression_builder = expression_builder
        params["expression_builder"] = expression_builder
        self._expression_builder: ExpressionBuilder[ArrayLikeT]

        if n_gen < 0 or n_per_gen < 0 or n_elite < 0:
            raise ValueError("All parameters must be non-negative.")
        if n_elite > n_per_gen:
            raise ValueError(
                "Number of elite individuals cannot be greater than "
                "number of individuals per generation."
            )
        self.n_gen = n_gen
        self.n_per_gen = n_per_gen
        self.n_elite = n_elite
        self.n_survivor = n_survivor

        if optimize_with not in ("curve_fit", "minimize"):
            raise ValueError(f"Invalid optimize_with: {optimize_with!r}")
        self.optimize_with: OptimizeOptions = optimize_with

        if not is_scaler(curve_fit_y_scaling):
            raise ValueError(f"Invalid curve_fit_y_scaling: {curve_fit_y_scaling!r}")
        self.curve_fit_y_scaling: ScalingOptions | None = curve_fit_y_scaling
        self.curve_fit_options = curve_fit_options

        if not is_scorer(minimize_scoring):
            raise ValueError(f"Invalid minimize_scoring: {minimize_scoring!r}")
        self.minimize_scoring = minimize_scoring
        self.minimize_options = minimize_options

        if not is_scorer(scoring):
            raise ValueError(f"Invalid scoring: {scoring!r}")
        self.scoring = scoring
        if not is_batch_scorer(batch_scoring) or batch_scoring is None:
            raise ValueError(f"Invalid batch_scoring: {batch_scoring!r}")
        self.batch_scoring = batch_scoring

        self.propagate_seeds = propagate_seeds

        self.filter_duplicates = filter_duplicates
        self.filter_func = filter_func
        self.penalty_func = penalty_func
        if ranking_method not in RankingOptions.__args__:
            raise ValueError(f"Invalid ranking: {ranking_method!r}")
        self.ranking_method: RankingOptions = ranking_method
        self.sort_with = sort_with

        self.n_gen_no_change = n_gen_no_change
        self.warm_start = warm_start
        self.n_jobs = n_jobs
        self.random_state = random_state
        self.verbose = verbose

        self.set_params(**params)

        # fitting-related properties
        self._current_gen: int = 0
        self._trackers: defaultdict[int, list[ExpressionTracker[ArrayLikeT]]] = (
            defaultdict(list)
        )
        self._raw_scores: defaultdict[int, NDArray[np.float64]] = defaultdict(
            _array_factory
        )
        self._fitness_scores: defaultdict[int, NDArray[np.float64]] = defaultdict(
            _array_factory
        )

        # after successful fitting
        self.fitted_data_: Literal["batch", "single"]
        self.trackers_: dict[int, list[ExpressionTracker[ArrayLikeT]]]
        self.gens_: list[int]
        self.estimators_: list[Expression[ArrayLikeT]]
        self.raw_scores_: NDArray[np.float64]
        self.fitness_scores_: NDArray[np.float64]
        self.best_estimator_idx_: tuple[int, int]
        self.best_estimator_: Expression[ArrayLikeT]

    def set_params(self, **params: Any) -> Self:
        """
        sklearn-style parameter setter. Changes made directly to the input parameters in `__init__`
        may not affect the internal state of the estimator; use the :func:`set_params` method
        to ensure proper updates.
        """
        super().set_params(**params)

        missing: _Missing = _missing

        # parameter setter hook for expression_builder
        builder: ExpressionBuilder[ArrayLikeT] | None | _Missing = params.pop(
            "expression_builder", missing
        )
        if not isinstance(builder, _Missing):
            if isinstance(builder, ExpressionBuilder):
                _builder = builder
            elif builder is None:
                from .collection import PSRCollection

                _builder: ExpressionBuilder[ArrayLikeT] = ExpressionBuilder(
                    psr_collection=PSRCollection()
                )
            else:
                raise TypeError("Expected ExpressionBuilder instance or None.")
            self._expression_builder = _builder

        if params.pop("n_gen", 6) < 1:
            raise ValueError("n_gen must be at least 1.")
        if params.pop("n_per_gen", 6) < 2:
            raise ValueError("n_per_gen must be at least 2.")
        if params.pop("n_elite", 6) < 0:
            raise ValueError("n_elite must be non-negative.")
        if params.pop("n_survivor", 6) < 2:
            raise ValueError("n_survivor must be at least 2.")
        if self.n_elite + self.n_survivor > self.n_per_gen:
            raise ValueError(
                "The total number of elite individuals and survivors cannot be "
                "greater than the number of individuals per generation."
            )

        return self

    @property
    def builder(self) -> ExpressionBuilder[ArrayLikeT]:
        """
        The expression builder used to construct and manipulate expressions. The expression builder
        is automatically generated if the initialization parameter `expression_builder` is not
        provided.

        Returns
        -------
        ExpressionBuilder[ArrayLikeT]
            The expression builder used for fitting with parametric symbolic regression.
        """
        return self._expression_builder

    @property
    def current_gen(self) -> int:
        """
        The current generation number.
        """
        return self._current_gen

    @current_gen.setter
    def current_gen(self, value: int) -> NoReturn:
        raise AttributeError(
            "'current_gen' is a critical attribute and cannot be modified directly."
        )

    @property
    def is_fitted(self) -> bool:
        """
        Check if the model is fitted.

        Returns
        -------
        bool
            True if the model is fitted, False otherwise.
        """
        return hasattr(self, "best_estimator_")

    @property
    def n_cpus(self) -> int:
        """
        Parse `n_jobs` and return the integer number of CPUs to use.
        """
        return compute_n_cpus(self.n_jobs)

    @property
    def _filter_func(self) -> Callable[[Expression[ArrayLikeT]], bool] | None:
        """
        Get the filter function for filtering "good" expressions.

        Returns
        -------
        Callable[[Expression[ArrayLikeT]], bool] | None
            The filter function if it exists, None otherwise.
        """
        filter_func = self.filter_func
        if isinstance(filter_func, int):

            def filter_func_(x: Expression[ArrayLikeT]) -> bool:
                return len(x.delayed_constants) <= filter_func

            return filter_func_
        return filter_func

    def add_seeds(
        self,
        seeds: Sequence[
            Sequence[str | Number | FuncUnit[ArrayLikeT]] | Expression[ArrayLikeT]
        ],
        *,
        types: Iterable[type["FuncUnit[ArrayLikeT]"]] = (
            Operation,
            Variable,
            Constant,
            DelayedConstant,
        ),
        custom_registry: dict[str | Number, FuncUnit[ArrayLikeT]] | None = None,
        init: bool = True,
        enforce_height: bool | None = None,
        apply_filter: bool = True,
    ) -> None:
        """
        Add seed expressions as guidance for the genetic algorithm search.

        Parameters
        ----------
        seeds : Sequence[Sequence[str | Number | FuncUnit[ArrayLikeT]] | Expression[ArrayLikeT]]
            The seed expressions to add. For each seed, it should be either the DFS-ordered nodes to
            construct an :class:`Expression` tree, or an existing :class:`Expression` instance.

            See :func:`FuncUnit.import_list` for more details on the expected format of the `nodes`,
            `types`, `custom_registry`, and `init` parameters.
        types : Iterable[type["FuncUnit[ArrayLikeT]"]]
            The types of the nodes in the expression tree to consider when importing a node list.
        custom_registry : dict[str | Number, FuncUnit[ArrayLikeT]] | None
            A custom registry of function units to use during expression construction.
        init : bool, default=True
            Whether to initialize an unknown function unit.
        enforce_height : bool | None, default=None
            Whether to enforce the height of the expression tree.

            The height constraints are defined in the `expression_builder` property at
            initialization. See :class:`~psr.expression.ExpressionBuilder` for more details. If
            `None`, the default definition of `enforce_height` in `expression_builder` is used.
        apply_filter : bool, default=True
            Whether to apply the filter function to the seed expressions.
        """
        filter_func = self._filter_func if apply_filter else None

        seed_trackers = self._trackers[0]
        for i, seed in enumerate(seeds, start=len(seed_trackers)):
            tracker = self._expression_builder.seed(
                seed,
                types=types,
                custom_registry=custom_registry,
                init=init,
                enforce_height=enforce_height,
                return_tracker=True,
                tracker_props=dict(gen=0, idx=i),
            )
            if filter_func and not filter_func(tracker.to_expression()):
                continue
            seed_trackers.append(tracker)

    def clear_seeds(self) -> None:
        """
        Clear the seed expressions.
        """
        self._trackers.pop(0, None)
        self._raw_scores.pop(0, None)
        self._fitness_scores.pop(0, None)

    def _evolve(self) -> None:
        """
        Evolve the population for one generation. The **current** generation must be evaluated
        properly first before evolving. `_evolve` will move the generation to the next one if the
        **current** generation has been evaluated.

        Internal use only. See the :func:`builder` property for more details.
        """
        builder = self._expression_builder
        cgen = self._current_gen
        num_exp = len(self._trackers.get(cgen, []))

        # check if the current generation has been evaluated
        if (
            len(self._raw_scores.get(cgen, [])) != num_exp
            or len(self._fitness_scores.get(cgen, [])) != num_exp
        ):
            raise ValueError(
                f"Generation {cgen} has not been evaluated or the model has been corrupted."
            )
        if cgen > 0 and num_exp > self.n_elite + self.n_survivor:
            if self.warm_start:
                warnings.warn(
                    f"Generation {cgen} was evaluated with {num_exp} individuals, "
                    "which is greater than your current total `n_elite + n_survivor`."
                )
            else:
                raise ValueError(
                    f"Generation {cgen} has not been evaluated against "
                    "the survival-of-the-fittest rule."
                )

        if cgen == 0:
            src = None
        else:
            src = self._trackers.get(cgen, []).copy()
            if len(src) == 0:
                warnings.warn(f"Generation {cgen} has a population of 0.")
            if self.propagate_seeds or cgen == 1:
                src = self._trackers.get(0, []) + list(
                    filter(lambda x: x.gen != 0, src)
                )

        cgen += 1
        trackers = builder.build(
            self.n_per_gen,
            src=src,
            random_state=self._random_integer(cgen),
            n_jobs=self.n_jobs,
            gen=cgen,
            idx_start=0,
        )
        if filter_func := self._filter_func:
            trackers = [t for t in trackers if filter_func(t.to_expression())]

        unique_trackers: list[ExpressionTracker[ArrayLikeT]] = []
        _set: set[str] = set()
        _gens: set[int]
        if self.filter_duplicates:
            _gens = set(range(cgen))
        elif self.propagate_seeds:
            _gens = {0}
        else:
            _gens = set()
        for _gen in _gens:
            _ts: list[ExpressionTracker[ArrayLikeT]] = self._trackers.get(_gen, [])
            for _t in _ts:
                _set.add(_t.to_expression().format())
        for tracker in trackers:
            _tracker_str = tracker.to_expression().format()
            if _tracker_str in _set:
                continue
            unique_trackers.append(tracker)
            _set.add(_tracker_str)

        if len(unique_trackers) == 0:
            warnings.warn(f"Evolution for generation {cgen} resulted in 0 individuals.")

        self._trackers[cgen] = unique_trackers
        self._current_gen = cgen

    def _evaluate(
        self,
        X: list[NDArray[np.float64]],
        y: list[NDArray[np.float64]],
        sample_weight: list[NDArray[np.float64] | None] | None = None,
        batch_weight: NDArray[np.float64] | None = None,
        gen: int | None = None,
        no_random_selection: bool = False,
        sort_with: Literal["raw", "fitness"] | None = None,
        **fit_params: Any,
    ) -> None:
        """
        Evaluate the **current** generation/population.

        `_evaluate` only evaluated the **current** generation. It does not increment `_current_gen`
        count even after a successful evaluation.

        Internal use only. See :func:`fit` for more details on the input parameters.

        Parameters
        ----------
        X, y, sample_weight, batch_weight : array-like
            The input features, target values, sample weights, and batch weights.

            See :func:`fit` for more details on the input parameters.
        gen : int | None
            The generation to evaluate. If `None`, will use the current generation pointer.
        no_random_selection : bool
            Whether to disable random selection of individuals for evaluation. If disabled,
            individuals with highest scores are selected directly.

            This is typically used in the last generation of the fitting process to ensure the best
            individuals are selected for the final model.
        sort_with : Literal["raw", "fitness"] | None
            Whether to sort the individuals by raw scores or fitness scores (penalized raw scores).

            If None, will use the `sort_with` parameter from the initialization parameters.
        **fit_params : Any
            Additional fit parameters.
        """
        if gen is None:
            gen = self._current_gen

        trackers = self._trackers.get(gen, [])
        population_size = len(trackers)
        if population_size == 0:
            if gen == 0:
                # no seed expressions to evaluate
                return
            raise ValueError(
                f"Generation {gen} has a population of 0 - no expressions to evaluate."
            )

        if gen == 1 or (gen > 1 and self.propagate_seeds):
            # seed expressions need to be evaluated first
            n_seeds = len(self._trackers.get(0, []))
            if (
                len(self._raw_scores.get(0, [])) != n_seeds
                or len(self._fitness_scores.get(0, [])) != n_seeds
            ):
                raise ValueError(
                    "Seed expressions have not been evaluated or the model has been corrupted."
                )

        # only generation 0 can be re-evaluated
        if (
            gen != 0
            and len(self._raw_scores.get(gen, [])) == population_size
            and len(self._fitness_scores.get(gen, [])) == population_size
        ):
            raise ValueError(f"Generation {gen} has already been evaluated.")
        self._raw_scores.pop(gen, None)
        self._fitness_scores.pop(gen, None)

        random_state = self._random_integer(gen)
        raw_scores = _batch_evaluate(
            trackers,
            X=X,  # type: ignore
            y=y,  # type: ignore
            sample_weight=sample_weight,  # type: ignore
            optimize_with=self.optimize_with,
            func_curve_fit=None,
            curve_fit_y_scaling=self.curve_fit_y_scaling,
            curve_fit_options=self.curve_fit_options,
            func_minimize=None,
            minimize_scoring=self.minimize_scoring,
            minimize_options=self.minimize_options,
            scoring=self.scoring,
            batch_scoring=self.batch_scoring,
            batch_weight=batch_weight,  # type: ignore
            random_state=random_state,
            n_jobs=self.n_jobs,
        )
        if len(raw_scores) != population_size:
            raise ValueError(
                "The number of scores returned does not match the number of expressions."
            )

        penalty_func = self.penalty_func
        expressions = [tracker.to_expression() for tracker in trackers]
        if isinstance(penalty_func, Callable):
            penalties = np.array(
                [penalty_func(exp) for exp in expressions], dtype=np.float64
            )
        else:
            if penalty_func < 0:
                raise ValueError("The penalty coefficient must be non-negative.")
            penalties = np.array(
                [penalty_func * exp.cost for exp in expressions], dtype=np.float64
            )

        if np.any(penalties < 0):
            raise ValueError("Penalties must be non-negative.")
        fitness_scores = raw_scores - penalties

        raw_scores = np.nan_to_num(raw_scores, nan=-np.inf)
        fitness_scores = np.nan_to_num(fitness_scores, nan=-np.inf)

        if gen == 0:
            if (sort_with or self.sort_with) == "raw":
                indices = np.argsort(raw_scores)[::-1]
            else:
                indices = np.argsort(fitness_scores)[::-1]
            trackers = [trackers[i] for i in indices]
            raw_scores = raw_scores[indices]
            fitness_scores = fitness_scores[indices]
            self._trackers[0] = trackers
            self._raw_scores[0] = raw_scores
            self._fitness_scores[0] = fitness_scores
            return

        if gen == 1 or (gen > 1 and self.propagate_seeds):
            trackers = self._trackers.get(0, []) + trackers
            raw_scores = np.concatenate([self._raw_scores.get(0, []), raw_scores])
            fitness_scores = np.concatenate(
                [self._fitness_scores.get(0, []), fitness_scores]
            )

        # add previous elites
        if gen > 1 and (last_gen := gen - 1) in self._trackers:
            last_trackers = self._trackers.get(last_gen, [])
            last_n = len(last_trackers)
            last_raw_scores = self._raw_scores.get(last_gen, [])
            last_fitness_scores = self._fitness_scores.get(last_gen, [])
            if last_n != len(last_raw_scores) or last_n != len(last_fitness_scores):
                # verify same length
                warnings.warn("Inconsistent lengths in previous generation.")
            else:
                # add previous elites
                trackers = last_trackers + trackers
                raw_scores = np.concatenate((last_raw_scores, raw_scores))
                fitness_scores = np.concatenate((last_fitness_scores, fitness_scores))

        # sort trackers, raw_scores, fitness_scores by fitness_scores in descending order
        sorted_indices = np.argsort(fitness_scores)[::-1]
        trackers = [trackers[i] for i in sorted_indices]
        raw_scores = raw_scores[sorted_indices]
        fitness_scores = fitness_scores[sorted_indices]

        # select the best expressions based on fitness scores
        n_candidate = len(trackers)
        n_elite, n_survivor = self.n_elite, self.n_survivor
        n_total = n_elite + n_survivor

        if no_random_selection or n_candidate <= n_total:
            trackers = trackers[:n_total]
            raw_scores = raw_scores[:n_total]
            fitness_scores = fitness_scores[:n_total]
        else:
            # pick first n_elite; then random pick n_survivors
            weights = scores_to_weights(
                fitness_scores[n_elite:], method=self.ranking_method
            )
            indices = n_elite + np.random.choice(
                len(weights), size=n_survivor, p=weights
            )
            # sort indices based on the fitness scores
            indices = indices[np.argsort(fitness_scores[indices])[::-1]]
            trackers = trackers[:n_elite] + [trackers[i] for i in indices]
            raw_scores = np.concatenate((raw_scores[:n_elite], raw_scores[indices]))
            fitness_scores = np.concatenate(
                (fitness_scores[:n_elite], fitness_scores[indices])
            )

        if (sort_with or self.sort_with) == "raw":
            # sort trackers, raw_scores, fitness_scores by raw_scores in descending order
            sorted_indices = np.argsort(raw_scores)[::-1]
            trackers = [trackers[i] for i in sorted_indices]
            raw_scores = raw_scores[sorted_indices]
            fitness_scores = fitness_scores[sorted_indices]

        self._trackers[gen] = trackers
        self._raw_scores[gen] = raw_scores
        self._fitness_scores[gen] = fitness_scores

    def _random_integer(self, gen: int) -> int:
        _max = np.iinfo(np.int32).max
        return int(
            np.random.default_rng(self.random_state).integers(1 + (97 * gen) % _max)
        )

    def fit(
        self,
        X: ArrayLikeT | NestedSequence,
        y: ArrayLikeT | NestedSequence,
        sample_weight: ArrayLikeT | NestedSequence | None = None,
        batch_weight: ArrayLikeT | None = None,
        **fit_params: Any,
    ) -> Self:
        """
        Fit the model to the training data.

        Parameters
        ----------
        X : ArrayLikeT | NestedSequence
            The input features.
        y : ArrayLikeT | NestedSequence
            The target values.
        sample_weight : ArrayLikeT | NestedSequence | None, optional
            Per data point sample weights for the training data.
        batch_weight : ArrayLikeT | None, optional
            Per batch weights for the training data.
        **fit_params : Any
            Additional fit parameters.

        Returns
        -------
        Self
            The fitted model.
        """
        if self.verbose > 0:
            logger.info("========== Parametric Symbolic Regression ==========")
            try:
                params = self.get_params(deep=False)
            except:
                params = {}
            for key, value in params.items():
                logger.info(f"{str(key):>20s}: {value!r}")

        if not self.warm_start:
            self.reset()
        else:
            while (cgen := self._current_gen) > 0:
                num_exp = len(self._trackers[cgen])
                if (
                    len(self._raw_scores[cgen]) == num_exp
                    and len(self._fitness_scores[cgen]) == num_exp
                ):
                    break
                warnings.warn(
                    f"Warm starting, but the previous generation {cgen} was not "
                    "fully evaluated. Rolling back to an earlier generation..."
                )
                self._raw_scores.pop(cgen, None)
                self._fitness_scores.pop(cgen, None)
                self._trackers.pop(cgen, None)
                self._current_gen -= 1

            if cgen >= self.n_gen:
                raise ValueError(
                    "Warm starting but the previous generations have exceeded budget. "
                    "Consider increasing `n_gen`."
                )
            if self.verbose > 0:
                logger.info(f">>> Warm starting from generation {cgen}")

        cgen = self._current_gen
        _list: list[dict[int, Any]] = [
            self._trackers,
            self._raw_scores,
            self._fitness_scores,
        ]
        for _dict in _list:
            for k in _dict.keys():
                if k > cgen:
                    _dict.pop(k)
        self._expression_builder.psr_collection.sync()

        X_data, y_data, w_data, b_data = self._to_batch_data(
            X, y, sample_weight=sample_weight, batch_weight=batch_weight
        )
        n_batch, n_feat = len(X_data), X_data[0].shape[1]
        self.builder.variables.cap(n_feat)

        self._evaluate(
            X=X_data, y=y_data, sample_weight=w_data, batch_weight=b_data, gen=0
        )
        if self.verbose > 0:
            self._verbose_summary(0)

        for cgen in range(cgen, self.n_gen):
            if self.verbose > 0:
                logger.info(f"... working on gen {cgen + 1} ...")
            self._evolve()
            self._evaluate(
                X=X_data,
                y=y_data,
                sample_weight=w_data,
                batch_weight=b_data,
                no_random_selection=(cgen == self.n_gen - 1),
            )
            if self.verbose > 0:
                self._verbose_summary()

            # check if early stopping
            if not (n_gen_no_change := self.n_gen_no_change):
                continue
            if n_gen_no_change < 1:
                warnings.warn("Wrong value for n_gen_no_change")
                continue

            _cgen = self._current_gen
            gens = sorted(self._trackers.keys())
            if 0 in gens:
                gens.remove(0)
            gens = gens[: gens.index(_cgen) + 1]
            if len(gens) <= n_gen_no_change:
                continue
            gens = gens[:-n_gen_no_change]
            _min_fitness_prev = np.min([np.min(self._fitness_scores[g]) for g in gens])
            _min_fitness_cur = self._fitness_scores[_cgen].min()
            if _min_fitness_cur < _min_fitness_prev and not np.isclose(
                _min_fitness_cur, _min_fitness_prev
            ):
                continue
            _min_raw_prev = np.min([np.min(self._raw_scores[g]) for g in gens])
            _min_raw_cur = self._raw_scores[_cgen].min()
            if _min_raw_cur < _min_raw_prev and not np.isclose(
                _min_raw_cur, _min_raw_prev
            ):
                continue

            # early stopping
            if self.verbose > 0:
                logger.info(
                    "********* Early Stopping Triggered "
                    f"(n_gen_no_change: {n_gen_no_change}) *********"
                )
            break

        # save the fitting results
        cgen = self._current_gen
        self.fitted_data_ = "batch" if n_batch > 1 else "single"
        self.trackers_ = self._trackers
        self.gens_ = sorted(self.trackers_.keys())
        self.raw_scores_ = self._raw_scores[cgen]
        self.fitness_scores_ = self._fitness_scores[cgen]
        self.best_estimator_ = self._trackers[cgen][0].to_expression()
        self.best_estimator_idx_ = (cgen, 0)
        return self

    @overload
    def predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT | None = None,
        sample_weight: ArrayLikeT | None = None,
        *args: Any,
        estimator: tuple[int, int] | None = None,
        refit: bool = False,
        return_estimator: Literal[True],
        **fit_params: Any,
    ) -> tuple[NDArray[np.float64], Expression[ArrayLikeT]]: ...
    @overload
    def predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT | None = None,
        sample_weight: ArrayLikeT | None = None,
        *args: Any,
        estimator: tuple[int, int] | None = None,
        refit: bool = False,
        return_estimator: Literal[False] = False,
        **fit_params: Any,
    ) -> NDArray[np.float64]: ...
    @overload
    def predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT | None = None,
        sample_weight: ArrayLikeT | None = None,
        *args: Any,
        estimator: tuple[int, int] | None = None,
        refit: bool = False,
        return_estimator: bool = False,
        **fit_params: Any,
    ) -> NDArray[np.float64] | tuple[NDArray[np.float64], Expression[ArrayLikeT]]: ...

    def predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT | None = None,
        sample_weight: ArrayLikeT | None = None,
        *args: Any,
        estimator: tuple[int, int] | None = None,
        refit: bool = False,
        return_estimator: bool = False,
        **fit_params: Any,
    ) -> NDArray[np.float64] | tuple[NDArray[np.float64], Expression[ArrayLikeT]]:
        """
        Predict target values for the given input features.

        **NOTE**: It is not recommended to use this method directly. Instead, you should get the
        best estimator (`best_estimator_`, an :class:`Expression` instance) and perform fit-predict
        from there. You can also pick other estimators for testing.

        Parameters
        ----------
        X : ArrayLikeT | NestedSequence
            The input features for which to make predictions. Should be a 2D array.
        y : ArrayLikeT | None, default=None
            The target values corresponding to the input features, which are required if `refit`
            is True. Should be a 1D array if provided.
        sample_weight : ArrayLikeT | None, default=None
            The sample weights for the input features, which can be used when refitting the model.
            Should be a 1D array if provided.
        estimator : tuple[int, int] | None, default=None
            The specific estimator to use for prediction. If None, the best estimator
            (`best_estimator_`); otherwise, this should be a tuple of (generation, index).
        refit : bool, default=False
            Whether to refit the estimator on the provided data before making predictions.
        return_estimator : bool, default=False
            Whether to return the fitted estimator along with the predictions.
        **fit_params : Any
            Additional fitting parameters to pass to the estimator's fit method.

            See :func:`psr.expression.Expression.fit` for more details.

        Returns
        -------
        NDArray[np.float64]  | tuple[NDArray[np.float64], Expression[ArrayLikeT]]
            The predicted target values (and the fitted estimator, if requested).
        """
        if not self.is_fitted:
            raise NotFittedError("This model is not fitted yet.")

        if estimator is None:
            model = self.best_estimator_
        else:
            model = self._trackers.get(estimator[0], [])[estimator[1]].to_expression()

        if not refit and not model.is_fitted:
            raise NotFittedError("The selected estimator/expression is not fitted yet.")

        X_data = np.asarray(X)
        if X_data.ndim != 2 or X_data.size == 0:
            raise ValueError("Invalid input shape for X.")
        if refit:
            if y is None:
                raise ValueError("y must be provided when refit is True.")
            model.fit(X, y, sample_weight=sample_weight, **fit_params)

        result = model.predict(X)
        arr = np.asarray(result, dtype=np.float64).flatten()
        if arr.size == 1:
            arr = np.repeat(arr, len(X_data))

        if return_estimator:
            return arr, model
        return arr

    def _to_batch_data(
        self,
        X: ArrayLikeT | NestedSequence,
        y: ArrayLikeT | NestedSequence,
        sample_weight: ArrayLikeT | NestedSequence | None = None,
        batch_weight: ArrayLikeT | None = None,
        _not_a_batch: bool = False,
    ) -> tuple[
        list[NDArray[np.float64]],
        list[NDArray[np.float64]],
        list[NDArray[np.float64] | None],
        NDArray[np.float64] | None,
    ]:
        """
        Preprocess the input data into a batch format. For each batch (series of data points), the
        function will ensure that the data is properly shaped and formatted for fitting.

        The returned tuple contains the following elements:

        - A sequence of input feature arrays for each batch.
        - A sequence of target arrays for each batch.
        - A sequence of sample weight arrays for each batch (or None if not provided).
        - An array of batch weights for each batch (or None if not provided).

        Parameters
        ----------
        X : ArrayLikeT
            The input features. Should be either:

            - A 2D array-like structure representing one batch of data points.
            - A 3D array-like structure or a sequence of 2D array-like structures representing
              multiple batches of data points.

        y : ArrayLikeT
            The target values. Corresponds to the input features in X. Should be either:

            - A 1D array-like structure representing one batch of target values.
            - A 2D array-like structure or a sequence of 1D array-like structures representing
              multiple batches of target values.

            The length of y must match the length of X for each batch.
        sample_weight : ArrayLikeT | None, optional
            Per data point sample weights for the training data. The shape must match `y` unless
            `None` is passed for the batch.
        batch_weight : ArrayLikeT | None, optional
            Per batch weights for the training data. The shape must match the number of batches
            unless `None` is passed.
        _not_a_batch : bool, optional
            If True, the function will only treat the input as a single batch (X is 2D and y is 1D).
            This is used **internally** to prevent endless recursion.

        Returns
        -------
        tuple[Sequence[NDArray], Sequence[NDArray], Sequence[NDArray | None], NDArray | None]
            A tuple containing the processed input features, target values, the sample weights, and
            the batch weights. The four returned sequences will have the same length corresponding
            to the number of batches (if not None).

            For each batch, `X` is a 2D array, `y` is a 1D array, and `sample_weight` is either a 1D
            array or None. They should have a matching length representing the number of data points
            within one batch.

        Raises
        -------
        ValueError
            If the input data is not properly shaped or if there are mismatched lengths.
        """
        n = len(X)
        if (
            n == 0
            or len(y) != n
            or (sample_weight is not None and len(sample_weight) != n)
        ):
            raise ValueError("Mismatched lengths between X, y, and sample_weight.")

        # check if this is a single data batch
        if not isinstance(y[0], Iterable):
            X_i = np.array(X, dtype=np.float64)
            y_i = np.array(y, dtype=np.float64).flatten()
            if not X_i.ndim == 2 or len(X_i) != len(y_i):
                raise ValueError("Incompatible shapes between X and y.")

            if sample_weight is None:
                return [X_i], [y_i], [None], None

            sample_weight_i = np.array(sample_weight, dtype=np.float64).flatten()
            if len(X_i) != len(sample_weight_i):
                raise ValueError("Incompatible shapes between X and sample_weight.")
            return [X_i], [y_i], [sample_weight_i], None

        if _not_a_batch:
            raise ValueError("Expected single data (X is 2D and y is 1D).")

        # is batch data
        if batch_weight is None:
            batch_weight_data = None
        elif len(batch_weight) == n:
            batch_weight_data = np.asarray(batch_weight, dtype=np.float64).flatten()
        else:
            raise ValueError("Incompatible shapes between X and batch_weight.")

        X_data: list[NDArray[np.float64]] = []
        y_data: list[NDArray[np.float64]] = []
        sample_weight_data: list[NDArray[np.float64] | None] = []
        for Xi, yi, wi in zip_longest(X, y, sample_weight or []):
            X_i, y_i, sample_weight_i, _ = self._to_batch_data(
                Xi, yi, wi, _not_a_batch=True
            )
            X_data.extend(X_i)
            y_data.extend(y_i)
            sample_weight_data.extend(sample_weight_i)

        # the number of features in each X_i also must match
        if not all(X_data[0].shape[1] == X_i.shape[1] for X_i in X_data[1:]):
            raise ValueError("Mismatched number of features between batches.")

        return X_data, y_data, sample_weight_data, batch_weight_data

    def _verbose_summary(self, gen: int | None = None) -> None:
        """
        Verbose summary of the current generation.
        """
        if self.verbose <= 0:
            return

        if gen is None:
            gen = self._current_gen

        logger.info(f"========== Generation {gen} ==========")
        trackers: list[ExpressionTracker[ArrayLikeT]] = self._trackers.get(gen, [])
        if len(trackers) == 0:
            logger.info("No expressions found.")
            return

        raw_scores: NDArray[np.float64] = self._raw_scores.get(gen, np.array([]))
        fitness_scores: NDArray[np.float64] = self._fitness_scores.get(
            gen, np.array([])
        )

        logger.info(
            f"{'gen':^3s} | {'idx':^5s} | {'Raw score':^13s} | "
            f"{'Fitness score':^13s} | {'Estimator'}"
        )
        for rscore, fscore, tracker in zip(
            raw_scores[: self.verbose], fitness_scores, trackers
        ):
            logger.info(
                f"{tracker.gen:^3d} | {tracker.idx:^5d} | {rscore:^13.5g} | "
                f"{fscore:^13.5g} | {tracker.to_expression().format()}"
            )

        logger.info("----------------------------------------")
        scoring = self.scoring
        scorer = get_scorer(scoring)
        logger.info(
            f"Score ({scoring if isinstance(scoring, str) else 'custom'}): {scorer!r}"
        )
        if isinstance(scorer, Scorer) and not scorer.greater_is_better:
            logger.info(
                f"The reported score is a negated loss to ensure greater is better."
            )
        logger.info("----------------------------------------")
        logger.info(f"Best estimator: {trackers[0].to_expression().format()}")
        logger.info(f"     Raw score: {raw_scores[0]:.5g}")
        logger.info(f" Fitness score: {fitness_scores[0]:.5g}")
        logger.info("----------------------------------------")
        logger.info(f"    Population: {len(trackers)}")
        logger.info(
            f"   Pop. scores: {np.mean(raw_scores):.5g} ± {np.std(raw_scores):.5g}"
        )
        logger.info(
            f"  Pop. fitness: {np.mean(fitness_scores):.5g} ± {np.std(fitness_scores):.5g}"
        )

    def reset(self) -> None:
        """
        Reset the model to its initial state.
        """
        self._current_gen = 0
        _seeds = self._trackers[0]
        self._trackers.clear()
        if _seeds:
            self._trackers[0] = _seeds
        self._raw_scores.clear()
        self._fitness_scores.clear()

        for prop in (
            "fitted_data_",
            "trackers_",
            "gens_",
            "estimators_",
            "raw_scores_",
            "fitness_scores_",
            "best_estimator_idx_",
            "best_estimator_",
        ):
            if hasattr(self, prop):
                delattr(self, prop)

    def __sklearn_is_fitted__(self) -> bool:
        """
        Check if the model is fitted with sklearn's API.
        """
        return self.is_fitted
