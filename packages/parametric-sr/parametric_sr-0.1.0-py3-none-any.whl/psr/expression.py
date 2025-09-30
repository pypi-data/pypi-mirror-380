"""
implementation for a mathematical expression
"""

from multiprocessing import Pool, cpu_count
from typing import (
    Any,
    Callable,
    Generator,
    Generic,
    Iterable,
    Literal,
    Optional,
    Self,
    Sequence,
    cast,
    overload,
)
import sys
import warnings

from matplotlib.axes import Axes
import numpy as np
from numpy.typing import NDArray
from scipy.optimize import OptimizeResult, OptimizeWarning, curve_fit, minimize

from .base import Tree, FuncUnit, Operation, Variable, Constant, DelayedConstant
from .base.exception import InvalidTreeError
from .config import config
from .metrics import Scorer, digest_batch_scores, get_scaler, get_scorer
from .typing import (
    ArrayLikeT,
    BatchScoringOptions,
    Number,
    OptimizeOptions,
    RngGeneratorSeed,
    ScalingOptions,
    ScipyCurveFitFunction,
    ScipyCurveFitOptions,
    CurveFitResult,
    ScipyMinimizeFunction,
    ScipyMinimizeOptions,
    ScoringOptions,
)


class Expression(Tree[FuncUnit[ArrayLikeT]], Generic[ArrayLikeT]):
    """
    A class representing a mathematical expression as a tree structure.

    This class extends the Tree class (:class:`psr.base.tree.Tree`) to represent mathematical
    expressions, where each node is a function unit (FuncUnit) that can be an operation, variable,
    constant, etc. The expression can be evaluated, simplified, and manipulated like a mathematical
    expression.

    See :class:`psr.base.tree.Tree` for the base class implementation.
    """

    def __init__(
        self,
        value: FuncUnit[ArrayLikeT],
        idx: int = 0,
        parent: Self | None = None,
        children: Iterable[Self] | None = None,
        reindex: bool = False,
    ) -> None:
        super().__init__(value, idx, parent, children)

        if reindex:
            try:
                self.refresh()
            except InvalidTreeError as e:
                warnings.warn(f"Failed to refresh expression tree: {e}")

    @property
    def func_unit(self) -> FuncUnit[ArrayLikeT]:
        """
        Alias for the node `value` attribute.

        Returns
        -------
        FuncUnit[ArrayLikeT]
            The function unit that represents this node.
        """
        return self.value

    @func_unit.setter
    def func_unit(self, value: FuncUnit[ArrayLikeT]) -> None:
        """
        ## Property Setter
        Setter for the node `value` attribute.

        Parameters
        ----------
        value : FuncUnit[ArrayLikeT]
            The function unit to set for this node.
        """
        self.value = value

    @property
    def _n_delayed_constants(self) -> int:
        """
        Returns the **cached** number of delayed constants in the subtree rooted at this node.

        **WARNING**: this number is not updated automatically. It is set manually and may not
        reflect the actual number of delayed constants, if the tree structure of the expression is
        modified without updating this value. Check `reindex_delayed_constants` method to update it.

        Returns
        -------
        int
            The **cached** number of delayed constants in the subtree rooted at this node.

        Notes
        -----
        To calculate the number of delayed constant in real time, you can use:
        >>> len([node for node in expression if node.func_unit.is_delayed])
        >>> len(expression.delayed_constants)
        """
        return self._num_dcs

    @_n_delayed_constants.setter
    def _n_delayed_constants(self, value: int) -> None:
        """
        ## Property Setter
        Set the **cached** number of delayed constants in the subtree rooted at this node.

        Parameters
        ----------
        value : int
            The number of delayed constants to set as **cached**.

        Raises
        ------
        ValueError
            If the number of delayed constants is negative.
        """
        if value < 0:
            raise ValueError("Number of delayed constants cannot be negative.")
        self._num_dcs = value

    @property
    def cost(self) -> float:
        """
        Returns the cost of the expression, which is the sum of the costs of all its nodes.

        The cost must be positive.

        Returns
        -------
        float
            The cost of the expression.
        """
        return sum(child.cost for child in self.children) + self.func_unit.cost

    def custom_validate(
        self, node: FuncUnit[ArrayLikeT], children: Iterable[FuncUnit[ArrayLikeT]]
    ) -> bool:
        """
        A custom validation method to check if the structure at **the current node** is valid.

        See Also
        --------
        validate : the main method for checking if the expression is valid.
        """
        if self.func_unit.arity == len(self.children):
            return True
        return False

    def reindex_nodes(self, idx: int | None = 0, from_root: bool = True) -> int:
        """
        Reindexes the tree nodes in depth-first search (DFS) order, by default starting from the
        root node. See the implementation :func:`psr.base.tree.Tree.reindex` for more details.

        Parameters
        ----------
        idx : int | None
            The index to start reindexing from. If None, the initial index of the node is used.
        from_root : bool, default=True
            If True, the reindexing starts from the root node. If False, it starts from this node.
            In most cases, reindexing only makes sense when starting from the root node, as it
            ensures a consistent and correct indexing of all nodes in the tree.

        Returns
        -------
        int
            The total number of nodes in the subtree rooted at this node, or the root tree if
            `from_root` is True.

        See Also
        --------
        validate : the main method for checking if the expression is valid; recommended to use
            before reindexing.
        custom_validate : custom validation method for checking if the expression is valid.
        psr.base.tree.Tree.reindex : the base class implementation.
        reindex_delayed_constants : the method for reindexing delayed constants in the expression
            tree.
        refresh : the main method for refreshing and reindexing the expression tree.
        """
        return super().reindex(idx, from_root=from_root)

    def reindex_delayed_constants(self, idx: int = 0, from_root: bool = True) -> int:
        """
        Reindexes the delayed constants in the expression tree.

        Parameters
        ----------
        idx : int, default=0
            The starting index for reindexing. This should always be 0 when `from_root` is True.
        from_root : bool, default=True
            If True, the reindexing starts from the root of the expression tree.

        Returns
        -------
        int
            The total number of delayed constants in the subtree rooted at this node, or the root
            tree if `from_root` is True.

        Raises
        ------
        TypeError
            If the function unit is delayed but not a DelayedConstant.

        See Also
        --------
        validate : the main method for checking if the expression is valid; recommended to use
            before reindexing.
        custom_validate : custom validation method for checking if the expression is valid.
        refresh : the main method for refreshing and reindexing the expression tree.
        psr.base.func_unit.DelayedConstant : a class representing a delayed constant.
        """
        target = self.root if from_root else self
        func_unit = target.func_unit

        if func_unit.is_delayed:
            if not isinstance(func_unit, DelayedConstant):
                raise TypeError(
                    f"Expected DelayedConstant but got {type(func_unit).__name__}"
                )
            func_unit.index = idx
            idx += 1

        n = 0
        for child in target.children:
            n += child.reindex_delayed_constants(idx + n, from_root=False)

        target._n_delayed_constants = n + int(target.func_unit.is_delayed)
        return target._n_delayed_constants

    def refresh(
        self,
        idx: int | None = 0,
        idx_dc: int = 0,
        validate: bool = True,
        check_structure: bool = True,
        from_root: bool = True,
    ) -> tuple[int, int]:
        """
        Reindexes the nodes and delayed constants in the expression tree.

        Parameters
        ----------
        idx : int | None, default=0
            The starting index for reindexing the nodes. If None, the node indices are not changed.
            This should always be 0 when `from_root` is True.
        idx_dc : int, default=0
            The starting index for reindexing the delayed constants. This should always be 0 when
            `from_root` is True.
        validate : bool, default=True
            If True, the expression is validated **before** reindexing.
        check_structure : bool, default=True
            If True, the structure of the expression is checked before reindexing. Only used when
            `validate` is True.
        from_root : bool, default=True
            If True, the reindexing starts from the root of the expression tree.

        Returns
        -------
        tuple[int, int]
            A tuple containing:
            - The total number of nodes in the subtree rooted at this node, or the root tree if
              `from_root` is True.
            - The total number of delayed constants in the subtree rooted at this node, or the root
              tree if `from_root` is True.

        Raises
        -------
        InvalidTreeError
            If the expression is invalid.

        See Also
        --------
        validate : the main method for checking if the expression is valid; recommended to use
            before reindexing.
        custom_validate : custom validation method for checking if the expression is valid.
        reindex_nodes : reindexes only the nodes in the expression tree.
        reindex_delayed_constants : reindexes only the delayed constants in the expression tree.
        """
        if validate:
            self.validate(check_structure=check_structure, from_root=from_root)
        n_nodes = super().reindex(idx, from_root=from_root)
        n_dcs = self.reindex_delayed_constants(idx_dc, from_root=from_root)
        return n_nodes, n_dcs

    def detach(
        self,
        value_detacher: (
            Callable[[FuncUnit[ArrayLikeT]], FuncUnit[ArrayLikeT]] | None
        ) = None,
        as_root: bool = True,
    ) -> Self:
        """
        Detaches the expression rooted at the current node from its original tree (the whole
        expression tree) as a new copy. The purpose of this method is to create a new expression
        tree with the same structure and values, but without any references to the original tree.
        Cross-references between different trees can cause issues when manipulating the trees, so
        this method is useful to avoid such issues.

        Parameters
        ----------
        value_detacher : Callable[[FuncUnit[ArrayLikeT]], FuncUnit[ArrayLikeT]] | None, default=None
            A function that takes the value of the node (`self.value`) and returns a copy of it.
            In certain cases, `self.value` may be a mutable object that can cause cross-referencing
            issues. This custom detacher function can be used to create a new copy of the value.

            The node value of an expression node is a function unit. `FuncUnit` class and subclasses
            have a copy method that can be used to create a new copy of the value, which is used by
            default, if no custom detacher is provided.
        as_root : bool, default=True
            If True, the detached tree will be treated as a root tree and the parent will be set to
            None. This means that the new tree will not have any parent, and it will be a standalone
            tree. In other words, the returned expression will not be related to the
            expression tree.

            If False, the parent of the detached tree will be set to the original parent. In most
            cases, you should **NOT** use this option, as it can lead to cross-referencing issues.

        Returns
        -------
        Self
            A new instance of the expression tree with the same structure and values, but detached
            from the original expression tree. The detached tree will have no references to the
            original expression tree, unless `as_root` is False (not recommended).
        """
        if value_detacher is None:

            def default_value_detacher(x: FuncUnit[ArrayLikeT]) -> FuncUnit[ArrayLikeT]:
                return x.copy()

            value_detacher = default_value_detacher

        return super().detach(value_detacher=value_detacher, as_root=as_root)

    def copy(self, as_root: bool = True, deep: bool = False) -> Self:
        """
        Creates a copy of the expression tree. The value (`func_unit`) representing each node is
        also copied.

        Parameters
        ----------
        as_root : bool, default=True
            If True, the copied tree will be treated as a root tree and the parent will be set to
            None. This means that the new tree will not have any parent, and it will be a standalone
            tree. In other words, the returned expression copy will not be related to the current
            expression tree.

            If False, the parent of the copied tree will be set to the original parent. In most
            cases, you should **NOT** use this option, as it can lead to cross-referencing issues.
        deep : bool, default=False
            If True, the value (`func_unit`) at each node is deeply copied. See details in
            :func:`psr.base.func_unit.FuncUnit.copy`.

        Returns
        -------
        Self
            A new instance of the expression tree with the same structure and values.

        See Also
        --------
        detach : The base method for detaching the expression tree as a new copy.
        psr.base.func_unit.FuncUnit.copy : the copy method for function units.
        """

        def value_detacher(x: FuncUnit[ArrayLikeT]) -> FuncUnit[ArrayLikeT]:
            return x.copy(deep=deep)

        return self.detach(value_detacher=value_detacher, as_root=as_root)

    def forward(
        self,
        X: ArrayLikeT,
        C: ArrayLikeT | Sequence[Number | None] | None,
        **kwargs: Any,
    ) -> ArrayLikeT | Number:
        """
        Evaluates the expression tree.

        Parameters
        ----------
        X : ArrayLike (keyword-only)
            Input data array, typically a 2D array-like structure where each row represents a data
            point and each column represents a variable.
        C : ArrayLike | Sequence[Number | None] | None (keyword-only)
            Array of delayed constants, used to pass constants determined at fit time. Should be a
            1D array-like structure where each element represents a delayed constant. The length
            should match the number of delayed constants in the expression tree.

            If None or an element is None, the fitted value of the corresponding delayed constant
            will be used. If a None is provided to a not fitted delayed constant, it will result in
            an error during evaluation.

            Values provided in `C` take precedence over the fitted values.
        **kwargs : Any
            Additional keyword arguments to pass to the evaluation method.

        Returns
        -------
        ArrayLike | Number
            The result of evaluating the expression tree.

        See Also
        --------
        psr.base.func_unit.FuncUnit.evaluate : the evaluation method for function units.
        """
        if not np.all(np.isfinite(np.asarray(X))):
            return float("nan")
        with np.errstate(**config.np_errstate):
            result = self.func_unit.forward(
                *(child.forward(X=X, C=C, **kwargs) for child in self.children),
                X=X,
                C=C,
                **kwargs,
            )
            if not np.all(np.isfinite(np.asarray(result))):
                return float("nan")
            return result

    def format(
        self,
        protect: bool = False,
        C: ArrayLikeT | Sequence[Number | None] | None = None,
        C_use_fitted: bool = False,
        C_protection_rules: Sequence[None | bool] | None = None,
        **kwargs: Any,
    ) -> str:
        """
        Formats the expression tree into a string representation.

        Parameters
        ----------
        protect : bool, default=False
            If True, the returned string representation will be protected and can be directly used
            to compose new expressions without being altered.

            For example, `X1 + 1` can not be directly applied to a multiplication `2 * X1 + 1`. If
            using `protect=True`, the expression should be formatted as `(X1 + 1)`, instead. In this
            case, multiplication requires protection and addition also requires protection.

            Protection goes both ways. `X1 + 1` can be directly applied to `exp(X1 + 1)`. In this
            case, addition requires protection but exponentiation does not.
        C : ArrayLikeT | Sequence[Number | None] | None, default=None
            Array of delayed constants to use in the formatting. This can be used when the delayed
            constants are known and you need to get the string representation of the expression tree
            using the values to represent the delayed constants.

            If `C` is provided, the delayed constant will be formatted using the value at its
            index in `C`, unless `C_use_fitted` is set to True and the fitted value is available.

            For example, for an expression `C1 * X1 + 1 + C2`, you can provide `C = [5.0, None]` to
            format the expression as `5.0 * X1 + 1 + C2`.
        C_use_fitted : bool, default=False
            Whether to use the fitted value from the delayed constant, if available, instead of
            the value from the previous input argument `C`.
        C_protection_rules : Sequence[None | bool] | None, default=None
            Array of protection rules for the delayed constants, corresponding to the elements in
            `C`. This is used to determine whether each delayed constant needs to be protected with
            parentheses when formatting the expression. Examples of constants needing protection
            include `1 + e`, etc. By default, no protection is assumed unless explicitly specified
            as True.

        Returns
        -------
        str
            A string representation of the expression tree, formatted according to the function
            units and their operations.

        See Also
        --------
        psr.base.func_unit.FuncUnit.format : the format method for function units.
        """
        child_protections = self.func_unit.protection_rules
        child_formats = (
            child.format(
                protect=p_rule,
                C=C,
                C_use_fitted=C_use_fitted,
                C_protection_rules=C_protection_rules,
                **kwargs,
            )
            for child, p_rule in zip(self.children, child_protections)
        )
        return self.func_unit.format(
            *child_formats,
            protect=protect,
            C=C,
            C_use_fitted=C_use_fitted,
            C_protection_rules=C_protection_rules,
            **kwargs,
        )

    @property
    def delayed_constants(self) -> list[DelayedConstant[ArrayLikeT]]:
        """
        Returns a list of all delayed constants in the expression.

        Returns
        -------
        list[DelayedConstant[ArrayLikeT]]
            A list of all delayed constants in the expression.
        """
        return [
            node.func_unit
            for node in self
            if isinstance(node.func_unit, DelayedConstant)
        ]

    @property
    def born_fitted(self) -> bool:
        """
        If the expression does not contain any delayed constants, it is considered "born fitted". In
        other words, no fitting is needed for the expression to be evaluated.

        Returns
        -------
        bool
            True if the expression does not require fitting, False otherwise.
        """
        return not any(node.func_unit.is_delayed for node in self)

    @property
    def is_fitted(self) -> bool:
        """
        Checks if the model is fitted. A fitted expression should have all its delayed constants
        fitted to the data. If there is no delayed constant, the expression is considered fitted.

        Returns
        -------
        bool
            True if the model is fitted, False otherwise.
        """
        return all(node.func_unit.is_fitted for node in self.iter(DelayedConstant))

    def formulate(
        self,
    ) -> Callable[[ArrayLikeT, *tuple[Number, ...]], ArrayLikeT | Number]:
        """
        Formulates the expression into a callable function that can be used to evaluate the
        expression.

        Returns
        -------
        Callable[[ArrayLikeT, *tuple[Number, ...]], ArrayLikeT | Number]
            A callable function that takes no arguments and returns the evaluated expression.

            The callable can be called as `evaluate(X, *args_dc_values)`, where `X` is the input
            data (a 2D array). This callable works with `scipy.optimize.curve_fit` for finding the
            optimal values for the delayed constants.
        """
        num_dc = len(tuple(self.iter(DelayedConstant)))
        args_dc = ", ".join([f"arg{i}" for i in range(num_dc)])
        args_dc_type = ", ".join([f"arg{i}: Number" for i in range(num_dc)])

        # tricking type hint
        local_scope: dict[
            str, Callable[[ArrayLikeT, *tuple[Number, ...]], ArrayLikeT | Number]
        ] = {}
        exec(
            f"def evaluate(X: ArrayLikeT, {args_dc_type}) -> ArrayLikeT | Number:\n"
            f"    return self.forward(X=X, C=({args_dc},))",
            {"ArrayLikeT": ArrayLikeT, "Number": Number, "self": self},
            local_scope,
        )

        evaluate = local_scope["evaluate"]
        evaluate.__module__ = __name__
        setattr(sys.modules[__name__], "evaluate", evaluate)
        return evaluate

    def formulate_minimize(
        self,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
    ) -> ScipyMinimizeFunction[ArrayLikeT]:
        """
        Formulates the expression into a callable function for minimization.

        The callable will have the signature: `evaluate_minimize(*args_dc, X, y, sample_weight)`,
        where `*args_dc` are the delayed constants, and `X`, `y`, and `sample_weight` are the input
        data, target values, and sample weights, respectively. The returned callable function works
        with `scipy.optimize.minimize` for finding the optimal values for the delayed constants.

        Parameters
        ----------
        minimize_scoring : Literal["mae", "mse", "rmse", "r2", ...] | str | Scorer, default="rmse"
            The scoring method to use for evaluating the fit. Can be a string or a custom Scorer
            object. If a string is provided, it should be one of the supported methods:

                - "mae": Mean Absolute Error
                - "mse": Mean Squared Error
                - "rmse": Root Mean Squared Error
                - "r2": R2 Score

            The scoring method will be modified so that the greater the better is enforced.

        Returns
        -------
        Callable[[*tuple[Number, ...], ArrayLikeT, ArrayLikeT, ArrayLikeT | None], float]
            A callable function that takes the delayed constants/arguments, the input data `X`,
            target data `y`, and the sample weight `sample_weight`, and returns a float.
        """
        if (scorer := get_scorer(minimize_scoring, None)) is None:
            raise ValueError(f"Unknown scoring method: {minimize_scoring}")

        # tricking type hint
        local_scope: dict[str, ScipyMinimizeFunction[ArrayLikeT]] = {}
        exec(
            f"def evaluate_minimize(\n"
            f"    guess: ArrayLikeT | Sequence[Number],\n"
            f"    X: ArrayLikeT | None = None,\n"
            f"    y: ArrayLikeT | None = None,\n"
            f"    sample_weight: ArrayLikeT | None = None,\n"
            f") -> float:\n"
            f"    if not np.all(np.isfinite(guess)) or not np.all(np.isfinite(y)):\n"
            f"        return float('inf')\n"
            f"    y_pred = self.forward(X=X, C=guess)\n"
            f"    if not np.all(np.isfinite(y_pred)):\n"
            f"        return float('inf')\n"
            f"    return -scorer(y, y_pred, sample_weight=sample_weight)",
            {
                "Number": Number,
                "ArrayLikeT": ArrayLikeT,
                "Sequence": Sequence,
                "self": self,
                "scorer": scorer,
                "np": np,
            },
            local_scope,
        )

        evaluate_minimize = local_scope["evaluate_minimize"]
        evaluate_minimize.__module__ = __name__
        setattr(sys.modules[__name__], "evaluate_minimize", evaluate_minimize)
        return evaluate_minimize

    def formulate_curve_fit(self, y_scaling: Optional[ScalingOptions] = "log"):
        """
        Formulates the expression into a callable function for curve fitting, similarly to
        :func:`formulate` but with additional scaling the output.

        The callable will have the signature: `evaluate_curve_fit(X, *args_dc)` where `*args_dc` are
        the delayed constants, and `X` is the input data. The returned callable function works with
        `scipy.optimize.curve_fit` for finding the optimal values for the delayed constants.

        Parameters
        ----------
        y_scaling : Optional[ScalingOptions]
            The scaling options for the output `y` values. For example, if `log`, then the log of
            the original output is returned, instead of the original values evaluated through the
            :class:`Expression`.

            This is mostly designed for when the target values span across multiple magnitudes and
            the least square error used by :func:`scipy.optimize.curve_fit` might ignore the errors
            on smaller-scale values.

            **Performance warning**: Scaling the output may affect the fitting process. Using a
            `log` scaling to transform the values may yield NaN values and thus affect fitting.

        Returns
        -------
        Callable[[ArrayLikeT, *tuple[Number, ...]], NDArray[np.float64]]
            A callable function that takes the input data `X` and the delayed constants as arguments,
            and returns the predicted `y` values.
        """
        y_scaler = get_scaler(y_scaling, None)

        num_dc = len(tuple(self.iter(DelayedConstant)))
        args_dc = ", ".join([f"arg{i}" for i in range(num_dc)])
        args_dc_type = ", ".join([f"arg{i}: Number" for i in range(num_dc)])

        # tricking type hint
        local_scope: dict[str, ScipyCurveFitFunction[ArrayLikeT]] = {}
        exec(
            f"def evaluate_curve_fit(\n"
            f"    X: ArrayLikeT, {args_dc_type}\n"
            f") -> NDArray[np.float64]:\n"
            f"    y = self.forward(X=X, C=({args_dc},))\n"
            f"    if y_scaler:\n"
            f"        y = y_scaler(y)\n"
            f"    y = np.asarray(y).reshape(-1).astype(np.float64)\n"
            f"    if y.size == 1:\n"
            f"        y = np.repeat(y, len(X))\n"
            f"    return y",
            {
                "ArrayLikeT": ArrayLikeT,
                "NDArray": NDArray,
                "Number": Number,
                "Sequence": Sequence,
                "np": np,
                "self": self,
                "y_scaler": y_scaler,
            },
            local_scope,
        )

        evaluate_curve_fit = local_scope["evaluate_curve_fit"]
        evaluate_curve_fit.__module__ = __name__
        setattr(sys.modules[__name__], "evaluate_curve_fit", evaluate_curve_fit)
        return evaluate_curve_fit

    @overload
    def _fit_minimize(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[True],
    ) -> tuple[Self, OptimizeResult | None]: ...
    @overload
    def _fit_minimize(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[False] = False,
    ) -> Self: ...
    @overload
    def _fit_minimize(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
    ) -> Self | tuple[Self, OptimizeResult | None]: ...

    def _fit_minimize(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: Optional[ArrayLikeT] = None,
        *,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
    ) -> Self | tuple[Self, OptimizeResult | None]:
        """
        Fits the model to the data with a loss minimization approach.

        This method optimizes the model parameters by minimizing a loss function, which is
        customizable but may have performance issues since `scipy.optimize` will **not** have access
        to the residuals of the predictions.

        Parameters
        ----------
        X : ArrayLikeT, 2-dimensional
            The input data (2D).
        y : ArrayLikeT, 1-dimensional
            The target values (1D).
        sample_weight : ArrayLikeT, optional
            The weights for each sample in the fitting process. Should be 1-dimensional if provided.
        func_minimize : ScipyMinimizeFunction, optional (keyword-only)
            The function to use for minimization. If None, the output from the `formulate_minimize`
            method will be used; if provided, the function should follow the method's output
            signature. This is implemented so that the `formulate_minimize` method does not need to
            be repeated run when fitting the multiple sets of data.

            `minimize_scoring` will be ignored if `func_minimize` is provided.
        minimize_scoring : Literal["mae", "mse", "rmse", "r2"] | str | Scorer, default="rmse" (keyword-only)
            The scoring method to use for evaluating the fit. Can be a string or a custom Scorer
            object. If a string is provided, it should be one of the supported methods:

                - "mae": Mean Absolute Error
                - "mse": Mean Squared Error
                - "rmse": Root Mean Squared Error
                - "r2": R2 Score

            The scoring method will be modified so that the greater the better is enforced.

            If `func_minimize` is provided, the `minimize_scoring` will be ignored.
        minimize_options : ScipyMinimizeOptions, optional (keyword-only)
            Arguments to pass to the `scipy.optimize.minimize` function. Not all arguments are
            supported. Arguments such as `x0` and `bounds` are compiled automatically and cannot be
            passed here.
        random_state: RngGeneratorSeed, optional (keyword-only)
            The random seed to use for the optimization process to perturb the initial guess.
        return_result : bool, default=False (keyword-only)
            Whether to return the result of the optimization process along with the fitted model.
            If True, a tuple (Self, OptimizeResult | None) will be returned; if False, only the
            fitted model will be returned, which is compatible with sklearn API.

        Returns
        -------
        Self | tuple[Self, OptimizeResult | None]
            The fitted model or a tuple containing the fitted model and the optimization result. If
            the optimization result is returned as None, then it means either the optimization
            failed or no optimization was performed because the model does not require fitting.

        Raises
        ------
        ValueError
            If the input data is not valid.
        RuntimeError
            If the optimization process fails.

        See Also
        --------
        formulate :  methods to formulate the expression as callable functions for optimization with
            `scipy.optimize.curve_fit`.
        formulate_minimize : methods to formulate the expression as callable functions for
            optimization with `scipy.optimize.minimize`.
        predict : method for predicting target values with the fitted values.
        """
        if self.born_fitted:
            if return_result:
                return self, None
            return self

        if func_minimize is not None:
            func = func_minimize
        else:
            func = self.formulate_minimize(minimize_scoring)

        try:
            dcs = self.delayed_constants
            bounds = [dc.bounds for dc in dcs]
            x0 = np.array([dc.initial_guess for dc in dcs])
            if config.initial_guess_noise_scale is not None:
                x0 += np.random.default_rng(random_state).normal(
                    scale=abs(config.initial_guess_noise_scale), size=x0.shape
                )
            x0 = np.array(
                [np.clip(x, min_, max_) for x, (min_, max_) in zip(x0, bounds)]
            )
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                result: OptimizeResult | None = minimize(  # type: ignore
                    func,  # type: ignore
                    x0=x0,
                    args=(X, y, sample_weight),
                    bounds=bounds,
                    **(minimize_options or {}),  # type: ignore
                )  # type: ignore
            if not np.all(np.isfinite(result.x)):  # type: ignore
                raise RuntimeError("Optimization produced non-finite values")
            for dc, x in zip(dcs, result.x):  # type: ignore
                dc.fitted_value = float(x)  # type: ignore
        except Exception:
            result = None

        if return_result:
            return self, result  # type: ignore
        return self

    @overload
    def _fit_curve_fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[True],
    ) -> tuple[Self, CurveFitResult | None]: ...
    @overload
    def _fit_curve_fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[False] = False,
    ) -> Self: ...
    @overload
    def _fit_curve_fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
    ) -> Self | tuple[Self, CurveFitResult | None]: ...

    def _fit_curve_fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: Optional[ArrayLikeT] = None,
        *,
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
    ) -> Self | tuple[Self, CurveFitResult | None]:
        """
        Fits the model to the data with a least-squares approach (or similar).

        Parameters
        ----------
        X : ArrayLikeT, 2-dimensional
            The input data (2D).
        y : ArrayLikeT, 1-dimensional
            The target values (1D).
        sample_weight : ArrayLikeT, optional
            The weights for each sample in the fitting process. Should be 1-dimensional if provided.

            **Note**: while :func:`~scipy.optimize.curve_fit` does not support sample weights
            natively, the provided sample weights are converted as the `sigma` parameter for
            `curve_fit`, if `sigma` is not defined in the `curve_fit_options` parameter.
        func_curve_fit: ScipyCurveFitFunction[ArrayLikeT], optional
            The function to use for curve fitting. If None, the output from the `formulate_curve_fit`
            method will be used; if provided, the function should follow the method's output
            signature. This is implemented so that the `formulate_curve_fit` method does not need to
            be repeated run when fitting the multiple sets of data.

            **Warning**: when providing a custom `func_curve_fit`, make sure its return values match
            `curve_fit_y_scaling`. Otherwise, the true `y` values will be scaled but the predicted
            values from `func_curve_fit` will not be scaled, creating inconsistencies.
        curve_fit_y_scaling: ScalingOptions, optional
            The scaling method to apply to the target values (y) before fitting. If None, no scaling
            will be applied.

            **Performance warning**: currently, the `log` and `plog` options may lead to higher
            fail rate for fitting. If you need to scale `y` values, consider passing scaled `y` to
            `fit` manually, instead.

            This can be useful when `y` spans across multiple magnitudes and the least square error
            will be dominated by large values. For example, you can use a `log` scale of the values
            to calculate the error in a more balanced way.

            You do **not** need to scale `y` values beforehand. The scaling is handled internally.
        curve_fit_options: ScipyCurveFitOptions, optional
            The options to pass to the :func:`scipy.optimize.curve_fit` function. The key `options`
            is reserved for extra keyword arguments that are not defined in the typed dict.
        random_state: RngGeneratorSeed, default=None (keyword-only)
            The random seed to use for the optimization process to perturb the initial guess.
        return_result : bool, default=False (keyword-only)
            Whether to return the result of the optimization process along with the fitted model.
            If True, a tuple (Self, OptimizeResult | None) will be returned; if False, only the
            fitted model will be returned, which is compatible with sklearn API.

        Returns
        -------
        Self | tuple[Self, OptimizeResult | None]
            The fitted model or a tuple containing the fitted model and the optimization result. If
            the optimization result is returned as None, then it means either the optimization
            failed or no optimization was performed because the model does not require fitting.

        Raises
        ------
        ValueError
            If the input data is not valid.
        RuntimeError
            If the optimization process fails.

        See Also
        --------
        formulate_curve_fit : method to formulate the expression as a callable function for
            optimization with `scipy.optimize.curve_fit`.
        formulate :  methods to formulate the expression as callable functions for optimization with
            `scipy.optimize.curve_fit`.
        formulate_minimize : methods to formulate the expression as callable functions for
            optimization with `scipy.optimize.minimize`.
        predict : method for predicting target values with the fitted values.
        """
        if self.born_fitted:
            if return_result:
                return self, None
            return self

        if func_curve_fit is not None:
            func = func_curve_fit
        else:
            func = self.formulate_curve_fit(curve_fit_y_scaling)

        if sample_weight is None:
            sigma = None
        elif len(sample_weight) == len(X):
            sigma = 1.0 / np.sqrt(np.asarray(sample_weight))
        else:
            raise ValueError(
                "sample_weight should be 1-dimensional and have the same length as X"
            )

        curve_fit_kwargs: dict[str, Any] = {}
        if curve_fit_options is not None:
            curve_fit_kwargs.update(curve_fit_options)
            curve_fit_kwargs.update(curve_fit_kwargs.pop("options", {}))
        curve_fit_kwargs.setdefault("sigma", sigma)
        curve_fit_kwargs.setdefault("absolute_sigma", False)
        curve_fit_kwargs.setdefault("maxfev", 20000)

        try:
            dcs = self.delayed_constants
            bounds = [dc.vbounds for dc in dcs]
            x0 = np.array([dc.initial_guess for dc in dcs])
            if config.initial_guess_noise_scale is not None:
                x0 += np.random.default_rng(random_state).normal(
                    scale=abs(config.initial_guess_noise_scale), size=x0.shape
                )
            x0 = np.array(
                [np.clip(x, min_, max_) for x, (min_, max_) in zip(x0, bounds)]
            )
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                warnings.simplefilter("ignore", category=OptimizeWarning)
                scaler = get_scaler(curve_fit_y_scaling, None)
                if scaler:
                    y_ = scaler(np.asarray(y))
                else:
                    y_ = np.asarray(y)
                popt, pcov, *infodict = curve_fit(  # type: ignore
                    func,  # type: ignore
                    xdata=X,  # type: ignore
                    ydata=y_,
                    p0=x0,
                    bounds=np.asarray(bounds, dtype=np.float64).T,  # type: ignore
                    **curve_fit_kwargs,
                )
            if not np.all(np.isfinite(popt)) or len(popt) != len(dcs):
                raise RuntimeError("Optimization produced non-finite values")
            for dc, x in zip(dcs, popt):
                dc.fitted_value = float(x)
            result = (popt, pcov, *infodict)
        except Exception:
            result = None

        if return_result:
            return self, result  # type: ignore
        return self

    @overload
    def fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[True],
    ) -> tuple[Self, CurveFitResult | OptimizeResult | None]: ...
    @overload
    def fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[False] = False,
    ) -> Self: ...
    @overload
    def fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        *,
        sample_weight: Optional[ArrayLikeT] = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
    ) -> Self | tuple[Self, CurveFitResult | OptimizeResult | None]: ...

    def fit(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: Optional[ArrayLikeT] = None,
        *,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: Optional[ScipyMinimizeFunction[ArrayLikeT]] = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: Optional[ScipyMinimizeOptions] = None,
        random_state: Optional[RngGeneratorSeed] = None,
        return_result: bool = False,
    ) -> Self | tuple[Self, CurveFitResult | OptimizeResult | None]:
        """
        Fits the model to the data.

        Parameters
        ----------
        X : ArrayLikeT, 2-dimensional
            The input data (2D).
        y : ArrayLikeT, 1-dimensional
            The target values (1D).
        sample_weight : ArrayLikeT, optional
            The weights for each sample in the fitting process. Should be 1-dimensional if provided.

            - For `optimize_with="curve_fit"`, the sample weights will be converted to the `sigma`
              parameter.
            - For `optimize_with="minimize"`, the sample weights will be applied to calculate a
              weighted loss.

        optimize_with : OptimizeOptions, default="curve_fit" (keyword-only)
            The optimization method to use for fitting the model.

            - `curve_fit` uses :func:`scipy.optimize.curve_fit` for a more robust fitting process.
            - `minimize` uses :func:`scipy.optimize.minimize` for a more flexible fitting process,
              with a custom loss function.

        func_curve_fit: ScipyCurveFitFunction[ArrayLikeT], optional
            The function to use for curve fitting. If None, the output from the `formulate_curve_fit`
            method will be used; if provided, the function should follow the method's output
            signature. This is implemented so that the `formulate_curve_fit` method does not need to
            be repeated run when fitting the multiple sets of data.

            **Warning**: when providing a custom `func_curve_fit`, make sure its return values match
            `curve_fit_y_scaling`. Otherwise, the true `y` values will be scaled but the predicted
            values from `func_curve_fit` will not be scaled, creating inconsistencies.

            Only applicable when `optimize_with="curve_fit"`.
        curve_fit_y_scaling: ScalingOptions, optional
            The scaling method to apply to the target values (y) before fitting. If None, no scaling
            will be applied.

            **Performance warning**: currently, the `log` and `plog` options may lead to higher
            fail rate for fitting. If you need to scale `y` values, consider passing scaled `y` to
            `fit` manually, instead.

            This can be useful when `y` spans across multiple magnitudes and the least square error
            will be dominated by large values. For example, you can use a `log` scale of the values
            to calculate the error in a more balanced way.

            You do **not** need to scale `y` values beforehand. The scaling is handled internally.

            Only applicable when `optimize_with="curve_fit"`.
        curve_fit_options: ScipyCurveFitOptions, optional
            The options to pass to the :func:`scipy.optimize.curve_fit` function. The key `options`
            is reserved for extra keyword arguments that are not defined in the typed dict.

            Only applicable when `optimize_with="curve_fit"`.
        func_minimize : ScipyMinimizeFunction, optional
            The function to use for minimization. If None, the output from the `formulate_minimize`
            method will be used; if provided, the function should follow the method's output
            signature. This is implemented so that the `formulate_minimize` method does not need to
            be repeated run when fitting the multiple sets of data.

            `minimize_scoring` will be ignored if `func_minimize` is provided.

            Only applicable when `optimize_with="minimize"`.
        minimize_scoring : ScoringOptions | str | Scorer, default="rmse" (keyword-only)
            The scoring method to use for evaluating the fit. Can be a string or a custom Scorer
            object. If a string is provided, it should be one of the supported methods:

                - "mae": Mean Absolute Error
                - "mse": Mean Squared Error
                - "rmse": Root Mean Squared Error
                - "r2": R2 Score
                - "log_<scoring_method>": Logarithmic transformation-based error/score.

            The scoring method will be modified so that the greater the better is enforced.

            If `func_minimize` is provided, the `minimize_scoring` will be ignored.

            Only applicable when `optimize_with="minimize"`.
        minimize_options : ScipyMinimizeOptions, optional
            Arguments to pass to the `scipy.optimize.minimize` function. Not all arguments are
            supported. Arguments such as `x0` and `bounds` are compiled automatically and cannot be
            passed here.

            Only applicable when `optimize_with="minimize"`.
        random_state: RngGeneratorSeed, optional
            The random seed to use for the optimization process to perturb the initial guess.
        return_result : bool, default=False (keyword-only)
            Whether to return the result of the optimization process along with the fitted model.
            If True, a tuple (Self, OptimizeResult | None) will be returned; if False, only the
            fitted model will be returned, which is compatible with sklearn API.

        Returns
        -------
        Self | tuple[Self, OptimizeResult | None]
            The fitted model or a tuple containing the fitted model and the optimization result. If
            the optimization result is returned as None, then it means either the optimization
            failed or no optimization was performed because the model does not require fitting.

        Raises
        ------
        ValueError
            If the input data is not valid.
        RuntimeError
            If the optimization process fails.

        See Also
        --------
        formulate :  methods to formulate the expression as callable functions for optimization with
            `scipy.optimize.curve_fit`.
        formulate_minimize : methods to formulate the expression as callable functions for
            optimization with `scipy.optimize.minimize`.
        predict : method for predicting target values with the fitted values.
        """
        if self.born_fitted:
            if return_result:
                return self, None
            return self

        if optimize_with == "curve_fit":
            scaler = get_scaler(curve_fit_y_scaling, None)
            with np.errstate(**config.np_errstate):
                return self._fit_curve_fit(
                    X,
                    y if not scaler else scaler(np.asarray(y)),  # type: ignore
                    sample_weight=sample_weight,
                    func_curve_fit=func_curve_fit,
                    curve_fit_y_scaling=curve_fit_y_scaling,
                    curve_fit_options=curve_fit_options,
                    random_state=random_state,
                    return_result=return_result,
                )

        if optimize_with == "minimize":
            with np.errstate(**config.np_errstate):
                return self._fit_minimize(
                    X,
                    y,
                    sample_weight=sample_weight,
                    func_minimize=func_minimize,
                    minimize_scoring=minimize_scoring,
                    minimize_options=minimize_options,
                    random_state=random_state,
                    return_result=return_result,
                )

        raise ValueError(f"Unknown optimization request: {optimize_with}")

    def predict(self, X: ArrayLikeT, **kwargs: Any) -> ArrayLikeT | Number:
        """
        Predicts the target values for the given input data.

        Parameters
        ----------
        X : ArrayLikeT, 2-dimensional
            The input data (2D).
        **kwargs : Any
            Additional keyword arguments to pass to the prediction process in the `forward` method.

        Returns
        -------
        ArrayLikeT | Number
            The predicted target values. This could be a 1-dimensional array or a single number.

        Raises
        ------
        ValueError
            If the model is not fitted yet.

        See Also
        --------
        forward : the forward method for evaluating the expression with custom values for the
            delayed constants.
        __call__ : alias for the forward method.
        fit : the fit method to fit the expression (the delayed constants) to the data.
        """
        if not self.is_fitted:
            raise ValueError("Model is not fitted yet.")
        return self.forward(X=X, C=None, **kwargs)

    @overload
    def fit_predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: ArrayLikeT | None,
        optimize_with: OptimizeOptions,
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]],
        curve_fit_y_scaling: Optional[ScalingOptions],
        curve_fit_options: Optional[ScipyCurveFitOptions],
        func_minimize: ScipyMinimizeFunction[ArrayLikeT],
        minimize_scoring: ScoringOptions | str | Scorer,
        minimize_options: ScipyMinimizeOptions | None,
        random_state: RngGeneratorSeed,
        return_result: Literal[True],
        no_raise: bool = False,
    ) -> tuple[ArrayLikeT | Number, CurveFitResult | OptimizeResult | None]: ...
    @overload
    def fit_predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: ArrayLikeT | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        random_state: RngGeneratorSeed = None,
        *,
        return_result: Literal[True],
        no_raise: bool = False,
    ) -> tuple[ArrayLikeT | Number, CurveFitResult | OptimizeResult | None]: ...
    @overload
    def fit_predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: ArrayLikeT | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[False] = False,
        no_raise: bool = False,
    ) -> ArrayLikeT | Number: ...
    @overload
    def fit_predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: ArrayLikeT | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
        no_raise: bool = False,
    ) -> (
        ArrayLikeT
        | Number
        | tuple[ArrayLikeT | Number, CurveFitResult | OptimizeResult | None]
    ): ...

    def fit_predict(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: ArrayLikeT | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
        no_raise: bool = False,
    ) -> (
        ArrayLikeT
        | Number
        | tuple[ArrayLikeT | Number, CurveFitResult | OptimizeResult | None]
    ):
        """
        Fit the model to the data and return the prediction results.

        See :func:`fit` for more details on the fitting process and the input parameters.

        Parameters
        ----------
        X : ArrayLikeT, 2-dimensional
            The input data (2D).
        y : ArrayLikeT, 1-dimensional
            The target values (1D).
        sample_weight : ArrayLikeT | None, default=None
            The weights for each sample in the fitting process. Should be 1-dimensional if provided.
        optimize_with : OptimizeOptions, default="curve_fit" (keyword-only)
            The optimization method to use for fitting the model.

            - `curve_fit` uses :func:`scipy.optimize.curve_fit` for a more robust fitting process.
            - `minimize` uses :func:`scipy.optimize.minimize` for a more flexible fitting process,
              with a custom loss function.

        func_curve_fit, curve_fit_y_scaling, curve_fit_options : Any
            See :func:`fit`.
        func_minimize, minimize_scoring, minimize_options : Any
            See :func:`fit`.
        random_state: RngGeneratorSeed, default=None (keyword-only)
            The random seed to use for the optimization process to perturb the initial guess.
        return_result: bool, default=False
            If True, return the optimization result along with the predictions.
        no_raise : bool, default=False
            If True, suppress exceptions and return `nan` instead.

        Returns
        -------
        ArrayLikeT | Number | tuple[ArrayLikeT | Number, OptimizeResult | None]
            The predicted target values from the fitted model. If an exception occurs and `no_raise`
            is set to True, a `nan` value will be returned.

            Or a tuple containing the predicted target values and the optimization result, when
            `return_result` is set to True.

        Raises
        ------
        ValueError
            If the input data is not valid.
        RuntimeError
            If the optimization process fails.

        See Also
        --------
        formulate :  methods to formulate the expression as callable functions for optimization with
            `scipy.optimize.curve_fit`.
        formulate_minimize : methods to formulate the expression as callable functions for
            optimization with `scipy.optimize.minimize`.
        fit : method for fitting the model to the data.
        predict : method for predicting target values with the fitted values.
        """
        if return_result:
            try:
                _, result = self.fit(
                    X=X,
                    y=y,
                    sample_weight=sample_weight,
                    optimize_with=optimize_with,
                    func_curve_fit=func_curve_fit,
                    curve_fit_y_scaling=curve_fit_y_scaling,
                    curve_fit_options=curve_fit_options,
                    func_minimize=func_minimize,
                    minimize_scoring=minimize_scoring,
                    minimize_options=minimize_options,
                    random_state=random_state,
                    return_result=True,
                )
                return self.predict(X), result
            except Exception as e:
                if no_raise:
                    return float("nan"), None
                raise e

        try:
            self.fit(
                X=X,
                y=y,
                sample_weight=sample_weight,
                optimize_with=optimize_with,
                func_curve_fit=func_curve_fit,
                curve_fit_y_scaling=curve_fit_y_scaling,
                curve_fit_options=curve_fit_options,
                func_minimize=func_minimize,
                minimize_scoring=minimize_scoring,
                minimize_options=minimize_options,
                random_state=random_state,
                return_result=False,
            )
            return self.predict(X)
        except Exception as e:
            if no_raise:
                return float("nan")
            raise e

    @overload
    def batch_fit_predict(
        self,
        X: Sequence[ArrayLikeT],
        y: Sequence[ArrayLikeT],
        *,
        sample_weight: Sequence[ArrayLikeT | None] | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[True],
        n_jobs: int | None = None,
    ) -> list[tuple[ArrayLikeT | Number, CurveFitResult | OptimizeResult | None]]: ...
    @overload
    def batch_fit_predict(
        self,
        X: Sequence[ArrayLikeT],
        y: Sequence[ArrayLikeT],
        *,
        sample_weight: Sequence[ArrayLikeT | None] | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        random_state: RngGeneratorSeed = None,
        return_result: Literal[False] = False,
        n_jobs: int | None = None,
    ) -> list[ArrayLikeT | Number]: ...

    def batch_fit_predict(
        self,
        X: Sequence[ArrayLikeT],
        y: Sequence[ArrayLikeT],
        *,
        sample_weight: Sequence[ArrayLikeT | None] | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        random_state: RngGeneratorSeed = None,
        return_result: bool = False,
        n_jobs: int | None = None,
    ) -> (
        list[ArrayLikeT | Number]
        | list[tuple[ArrayLikeT | Number, CurveFitResult | OptimizeResult | None]]
    ):
        """
        Fits the :class:`Expression` model to a series of data (X-y pairs) and returns the
        predictions.

        Parameters
        ----------
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
            See :func:`fit`.
        func_minimize, minimize_scoring, minimize_options : Any
            See :func:`fit`.
        random_state : RngGeneratorSeed, default=None
            The random seed to use for the optimization process to perturb the initial guess.
        n_jobs : int | None, default=None
            The number of jobs to run in parallel. `None`, `0`, or `1` will use the parent process
            and **NOT** use multiple processes. `-1` will use all available cores.

        Returns
        -------
        list[ArrayLikeT | Number] | list[tuple[ArrayLikeT | Number, OptimizeResult | None]]
            The list of predicted target values, or a list of tuples, with each tuple containing
            the predicted target values and the optimization result per batch, when `return_result`
            is set to True.
        """
        n_batches = len(X)
        if n_batches == 0:
            raise ValueError("Must provide at least one batch of data.")
        if len(y) != n_batches:
            raise ValueError("Inconsistent lengths between X and y.")
        if sample_weight is None:
            sample_weight = [None] * n_batches
        elif len(sample_weight) != n_batches:
            raise ValueError("Inconsistent lengths between X and sample_weight.")

        for x_i, y_i, w_i in zip(X, y, sample_weight):
            if len(x_i) != len(y_i):
                raise ValueError(
                    "Inconsistent lengths between X and y in the batch data."
                )
            if w_i is not None and len(x_i) != len(w_i):
                raise ValueError(
                    "Inconsistent lengths between X and sample_weight in the batch data."
                )

        if optimize_with == "curve_fit":
            if func_curve_fit is None and not self.born_fitted:
                func_curve_fit = self.formulate_curve_fit(curve_fit_y_scaling)
            func_minimize = None
        else:
            if func_minimize is None and not self.born_fitted:
                func_minimize = self.formulate_minimize(
                    minimize_scoring=minimize_scoring
                )
            func_curve_fit = None

        n_cpus = cpu_count()
        if n_jobs is None:
            n_jobs = 1
        elif n_jobs < 0:
            n_jobs += n_cpus + 1
        n_jobs = np.clip(n_jobs, 1, min(n_batches, n_cpus))

        random_states = np.random.default_rng(random_state).choice(
            np.iinfo(np.int32).max, size=n_batches, replace=False
        )
        if n_jobs == 1:
            # Single-threaded execution
            results = [
                self.fit_predict(
                    X=x_i,
                    y=y_i,
                    sample_weight=w_i,
                    optimize_with=optimize_with,
                    func_curve_fit=func_curve_fit,
                    curve_fit_y_scaling=curve_fit_y_scaling,
                    curve_fit_options=curve_fit_options,
                    func_minimize=func_minimize,
                    minimize_scoring=minimize_scoring,
                    minimize_options=minimize_options,
                    random_state=r_i,
                    return_result=return_result,
                    no_raise=True,
                )
                for x_i, y_i, w_i, r_i in zip(X, y, sample_weight, random_states)
            ]
            return results  # type: ignore

        # Multi-processing execution
        with config.multiprocessing(), Pool(n_jobs) as p:
            results = p.starmap(
                self.fit_predict,
                [
                    (
                        x_i,
                        y_i,
                        w_i,
                        optimize_with,
                        func_curve_fit,
                        curve_fit_y_scaling,
                        curve_fit_options,
                        func_minimize,
                        minimize_scoring,
                        minimize_options,
                        r_i,
                        return_result,
                        True,
                    )
                    for x_i, y_i, w_i, r_i in zip(X, y, sample_weight, random_states)
                ],
            )
            return results  # type: ignore

    def fit_score(
        self,
        X: ArrayLikeT,
        y: ArrayLikeT,
        sample_weight: ArrayLikeT | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        scoring: ScoringOptions | str | Scorer = "rmse",
        random_state: RngGeneratorSeed = None,
        no_raise: bool = False,
    ) -> float:
        """
        Fit the model to the data, get the prediction values, and calculate the score between the
        predicted and true values.

        See :func:`fit` for more details on the fitting process and the input parameters.

        Parameters
        ----------
        X : ArrayLikeT, 2-dimensional
            The input data (2D).
        y : ArrayLikeT, 1-dimensional
            The target values (1D)
        sample_weight : ArrayLikeT | None, default=None
            The weights for each sample in the fitting process. Should be 1-dimensional if provided.
        optimize_with : OptimizeOptions, default="curve_fit" (keyword-only)
            The optimization method to use for fitting the model.

            - `curve_fit` uses :func:`scipy.optimize.curve_fit` for a more robust fitting process.
            - `minimize` uses :func:`scipy.optimize.minimize` for a more flexible fitting process,
              with a custom loss function.

        func_curve_fit, curve_fit_y_scaling, curve_fit_options : Any
            See :func:`fit`.
        func_minimize, minimize_scoring, minimize_options : Any
            See :func:`fit`.
        scoring : ScoringOptions | str | Scorer, default="rmse"
            The scoring method to use between the predicted values (after fitting) and the true
            values. A score is returned as a single float value, with higher values indicating a
            better fit. For a loss-based metric, its negative will be returned as the score.

            **Difference between `minimize_scoring` and `scoring`**

            - `minimize_scoring` is used during the optimization process to find the optimal values
              for the delayed constants that would give the best fit.
            - `scoring` is used after the model has been fitted to evaluate its performance on the
              training data. It can be the same as `minimize_scoring` or different. The final
              reported score between the predicted values (after fitting) and the true values will
              be computed using the specified `scoring` method.

        random_state: RngGeneratorSeed, default=None (keyword-only)
            The random seed to use for the optimization process to perturb the initial guess.
        no_raise : bool, default=False
            If True, suppress exceptions when fitting failed and use `nan` as the predicted value.

        Returns
        -------
        float
            The final score between the predicted values (after fitting) and the true values.

        Raises
        ------
        ValueError
            If the input data is not valid.
        RuntimeError
            If the optimization process fails.

        See Also
        --------
        formulate :  methods to formulate the expression as callable functions for optimization with
            `scipy.optimize.curve_fit`.
        formulate_minimize : methods to formulate the expression as callable functions for
            optimization with `scipy.optimize.minimize`.
        fit : method for fitting the model to the data.
        predict : method for predicting target values with the fitted values.
        fit_predict : method for fitting the model to the data and predicting target values.
        """
        scorer = get_scorer(scoring)
        if not isinstance(scorer, Scorer):
            raise ValueError(f"Unknown scoring method: {scoring}")

        try:
            self.fit(
                X=X,
                y=y,
                sample_weight=sample_weight,
                optimize_with=optimize_with,
                func_curve_fit=func_curve_fit,
                curve_fit_y_scaling=curve_fit_y_scaling,
                curve_fit_options=curve_fit_options,
                func_minimize=func_minimize,
                minimize_scoring=minimize_scoring,
                minimize_options=minimize_options,
                random_state=random_state,
                return_result=False,
            )
            y_pred = self.predict(X)
        except Exception as e:
            if not no_raise:
                raise e
            y_pred = float("nan")

        return scorer(y, y_pred, sample_weight=sample_weight)

    @overload
    def batch_fit_score(
        self,
        X: Sequence[ArrayLikeT],
        y: Sequence[ArrayLikeT],
        *,
        sample_weight: Sequence[ArrayLikeT | None] | None = None,
        optimize_with: OptimizeOptions = "curve_fit",
        func_curve_fit: Optional[ScipyCurveFitFunction[ArrayLikeT]] = None,
        curve_fit_y_scaling: Optional[ScalingOptions] = None,
        curve_fit_options: Optional[ScipyCurveFitOptions] = None,
        func_minimize: ScipyMinimizeFunction[ArrayLikeT] | None = None,
        minimize_scoring: ScoringOptions | str | Scorer = "rmse",
        minimize_options: ScipyMinimizeOptions | None = None,
        scoring: ScoringOptions | str | Scorer = "rmse",
        batch_scoring: None,
        batch_weight: ArrayLikeT | None = None,
        random_state: RngGeneratorSeed = None,
        n_jobs: int | None = None,
    ) -> NDArray[np.float64]: ...
    @overload
    def batch_fit_score(
        self,
        X: Sequence[ArrayLikeT],
        y: Sequence[ArrayLikeT],
        *,
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
    def batch_fit_score(
        self,
        X: Sequence[ArrayLikeT],
        y: Sequence[ArrayLikeT],
        *,
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

    def batch_fit_score(
        self,
        X: Sequence[ArrayLikeT],
        y: Sequence[ArrayLikeT],
        *,
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
        Fits the :class:`Expression` model to a series of data (X-y pairs), and for each batch,
        compute the score between the predicted values and the true values.

        Parameters
        ----------
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
            See :func:`fit`.
        func_minimize, minimize_scoring, minimize_options : Any
            See :func:`fit`.
        scoring : Literal["mae", "mse", "rmse", "r2"] | str | Scorer, default="rmse"
            The scoring method to use between the predicted values (after fitting) and the true
            values. A score is returned as a single float value, with higher values indicating a
            better fit. For a loss-based metric, its negative will be returned as the score.

            **Difference between `minimize_scoring` and `scoring`**

            - `minimize_scoring` is used during the optimization process to find the optimal values
              for the delayed constants that would give the best fit.
            - `scoring` is used after the model has been fitted to evaluate its performance on the
              training data. It can be the same as `minimize_scoring` or different. The final
              reported score between the predicted values (after fitting) and the true values will
              be computed using the specified `scoring` method.

        batch_scoring : BatchScoringOptions | None, default="median"
            The batch scoring method to use.

            - `None`: the returned value will be an array of scores, each score for each batch data.
            - `mean`: the returned value will be the mean score across all batches.
            - `median`: the returned value will be the median score across all batches.
            - `max`: the returned value will be the maximum score across all batches.
            - `min`: the returned value will be the minimum score across all batches.
            - *float*: a quantile value between 0 and 1 (inclusive). The returned value will be the
              score at the specified quantile across all batches.

        batch_weight : ArrayLikeT | None, default=None
            The weight to apply to each batch for a digested score of all batches with
            `batch_scoring`. If `None`, all batches are equally weighted.
        random_state : RngGeneratorSeed, default=None
            The random seed to use for the optimization process to perturb the initial guess.
        n_jobs : int | None, default=None
            The number of jobs to run in parallel. `None`, `0`, or `1` will use the parent process
            and **NOT** use multiple processes. `-1` will use all available cores.

        Returns
        -------
        float | NDArray[np.float64]
            The scores for each batch, or a digested score of all batches.
        """
        n_batches = len(X)
        if n_batches == 0:
            raise ValueError("Must provide at least one batch of data.")
        if len(y) != n_batches:
            raise ValueError("Inconsistent lengths between X and y.")
        if sample_weight is None:
            sample_weight = [None] * n_batches
        elif len(sample_weight) != n_batches:
            raise ValueError("Inconsistent lengths between X and sample_weight.")
        if batch_weight is not None and len(batch_weight) != n_batches:
            raise ValueError("Inconsistent lengths between X and batch_weight.")

        for x_i, y_i, w_i in zip(X, y, sample_weight):
            if len(x_i) != len(y_i):
                raise ValueError(
                    "Inconsistent lengths between X and y in the batch data."
                )
            if w_i is not None and len(x_i) != len(w_i):
                raise ValueError(
                    "Inconsistent lengths between X and sample_weight in the batch data."
                )

        if optimize_with == "curve_fit":
            if func_curve_fit is None and not self.born_fitted:
                func_curve_fit = self.formulate_curve_fit(curve_fit_y_scaling)
            func_minimize = None
        else:
            if func_minimize is None and not self.born_fitted:
                func_minimize = self.formulate_minimize(
                    minimize_scoring=minimize_scoring
                )
            func_curve_fit = None

        n_cpus = cpu_count()
        if n_jobs is None:
            n_jobs = 1
        elif n_jobs < 0:
            n_jobs += n_cpus + 1
        n_jobs = np.clip(n_jobs, 1, min(n_batches, n_cpus))

        random_states = np.random.default_rng(random_state).choice(
            np.iinfo(np.int32).max, size=n_batches, replace=False
        )
        if n_jobs == 1:
            # Single-threaded execution
            results = [
                self.fit_score(
                    X=x_i,
                    y=y_i,
                    sample_weight=w_i,
                    optimize_with=optimize_with,
                    func_curve_fit=func_curve_fit,
                    curve_fit_y_scaling=curve_fit_y_scaling,
                    curve_fit_options=curve_fit_options,
                    func_minimize=func_minimize,
                    minimize_scoring=minimize_scoring,
                    minimize_options=minimize_options,
                    scoring=scoring,
                    random_state=r_i,
                    no_raise=True,
                )
                for x_i, y_i, w_i, r_i in zip(X, y, sample_weight, random_states)
            ]
        else:
            # Multi-processing execution
            with config.multiprocessing(), Pool(n_jobs) as p:
                results = p.starmap(
                    self.fit_score,
                    [
                        (
                            x_i,
                            y_i,
                            w_i,
                            optimize_with,
                            func_curve_fit,
                            curve_fit_y_scaling,
                            curve_fit_options,
                            func_minimize,
                            minimize_scoring,
                            minimize_options,
                            scoring,
                            r_i,
                            True,
                        )
                        for x_i, y_i, w_i, r_i in zip(
                            X, y, sample_weight, random_states
                        )
                    ],
                )

        if batch_scoring is None:
            return np.array(results, dtype=np.float64)
        return digest_batch_scores(
            results, batch_scoring=batch_scoring, batch_weight=batch_weight
        )

    def unfit(self) -> None:
        """
        Unfits the model by resetting all delayed constants to their initial guesses.

        This method sets the `fitted_value` of each delayed constant to its `initial_guess`, which
        effectively "unfits" the model, allowing it to be refitted with new data.

        See Also
        --------
        fit : the method to fit the expression (the delayed constants) to the data.
        """
        for dc in self.delayed_constants:
            dc.fitted_value = None

    def trim(self) -> Self:
        """
        Method to trim and simplify the expression tree.

        For example, a subtree of `['div', 2, 3]` can be reduced into a :class:`Constant` node with
        value `0.666...`.

        TODO: Implement the trimming logic.
        """
        raise NotImplementedError

    def iter(
        self, *types: type[FuncUnit[ArrayLikeT]], from_root: bool = True
    ) -> Generator[Self, None, None]:
        """
        Iterate over the expression tree, yielding nodes of the specified types.

        Parameters
        ----------
        types : type[FuncUnit[ArrayLikeT]]
            The types of nodes to yield.

        from_root : bool, default=True
            Whether to start the iteration from the root of the expression tree.

        Yields
        ------
        Self
            The nodes of the specified types.

        See Also
        --------
        __iter__ : the default iterator over all nodes in the expression (sub)tree rooted at the
            current node.
        """
        target = self.root if from_root else self
        for exp in target:
            if isinstance(exp.value, types):
                yield exp

    @overload
    def export_list(self, *, simple: Literal[False]) -> list[FuncUnit[ArrayLikeT]]: ...
    @overload
    def export_list(self, *, simple: Literal[True] = True) -> list[str | Number]: ...

    def export_list(
        self, *, simple: bool = True
    ) -> list[FuncUnit[ArrayLikeT]] | list[str | Number]:
        """
        Export the expression tree to a list of function units or their identities. This list will
        be in depth-first order (DFS).

        Parameters
        ----------
        simple : bool, default=True
            Whether to export only the identities of the function units (i.e., their names).

        Returns
        -------
        list[FuncUnit[ArrayLikeT]] | list[str | Number]
            The exported function units or their identities.
        """
        lst = self.to_list(plain=True)
        if simple:
            return [node.identity for node in lst]
        return lst

    @classmethod
    def import_list(
        cls,
        lst: Sequence[FuncUnit[ArrayLikeT] | str | Number],
        /,
        *,
        types: Iterable[type["FuncUnit[ArrayLikeT]"]] = (
            Operation,
            Variable,
            Constant,
            DelayedConstant,
        ),
        custom_registry: dict[str | Number, FuncUnit[ArrayLikeT]] | None = None,
        init: bool = False,
        _is_root: bool = True,
    ) -> Self:
        """
        Import the expression tree from a **list** of function units or their identities. The list
        should be in depth-first order (DFS).

        Parameters
        ----------
        lst : Sequence[FuncUnit[ArrayLikeT] | str | Number] (*mix-and-match supported*)
            The list of function units or their identities. This parameter **must be a non-empty
            list**. In place changes will apply to the original list that is essential for the
            import process.
        types : Iterable[type["FuncUnit[ArrayLikeT]"]]
            The subclasses of `FuncUnit` to consider **in order** during identification. The first
            match is returned.
        custom_registry : dict[str | Number, FuncUnit[ArrayLikeT]] | None, default=None
            A custom registry for mapping identities to function units.
        init : bool, default=False
            Whether to initialize new function units if they are not found. The order of `types`
            also applies here - the first successful initialization will be used.

            > See :func:`psr.base.func_unit.FuncUnit.integrated_identify` for more details.
        _is_root : bool, default=True
            Whether this is a root call to build the expression tree, instead of a recursive call
            from within the method itself. This is used to determine whether to raise an error
            when the `lst` is empty or there are unused elements in the provided list after import.

            > This argument should in general not be used by the user directly.

        Returns
        -------
        Self
            A new :class:`Expression` instance.

        Raises
        ------
        ValueError
            - If the provided list is empty.
            - If some element in the list cannot be identified as a function unit.
            - If there are unused elements in the list after import and `_is_root` is True.

        See Also
        --------
        export_list : method to export the expression tree to a list. An exported list should be
            importable with the `import_list` method.
        psr.base.func_unit.FuncUnit.integrated_identify : method to identify function units from
            their identities.
        """
        if not lst:
            raise ValueError("Empty list cannot be imported.")

        if not isinstance(lst, list):
            lst = list(lst)
        elif _is_root:
            lst = lst.copy()
        func_unit = lst.pop(0)
        if not isinstance(func_unit, FuncUnit):
            temp = FuncUnit.integrated_identify(  # type: ignore
                func_unit, types=types, custom_registry=custom_registry, init=init
            )
            temp = cast(FuncUnit[ArrayLikeT] | None, temp)
            if temp is None:
                raise ValueError(
                    f"Cannot identify/initialize function unit for: {func_unit!r}"
                )
            func_unit = temp

        expression = cls(func_unit.copy())
        if (n_child := func_unit.arity) == 0:
            if _is_root and lst:
                raise ValueError(
                    f"Unused elements in the list. Import stopped at {func_unit!r}."
                )
            return expression

        for _ in range(n_child):
            if not lst:
                raise ValueError(
                    "Not enough elements in the list. "
                    f"{func_unit!r} needs {n_child} children."
                )
            child = cls.import_list(
                lst,
                types=types,
                custom_registry=custom_registry,
                init=init,
                _is_root=False,
            )
            expression.add_child(child)

        if _is_root:
            if lst:
                warnings.warn(
                    f"Unused elements in the list. Import stopped at {func_unit!r}."
                )
            try:
                expression.refresh(from_root=True)
            except Exception as e:
                warnings.warn(f"Failed to refresh expression from root: {e}")

        return expression

    def visualize(
        self,
        reindex: Literal["root", "self", False] = False,
        ax: Axes | None = None,
        with_index: bool = True,
        with_labels: bool = True,
        arrows: bool = True,
        **nxdraw_kwargs: Any,
    ) -> Axes:
        """
        Visualizes the expression rooted at this node using `networkx` and `matplotlib`. The title
        of the returned `matplotlib.axes.Axes` will be set to the string representation of the
        expression.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.
        `is_uniquely_indexed` must also be True to ensure that the graph is valid.

        Parameters
        ----------
        reindex : Literal["root", "self", False], default=False
            Whether to reindex the nodes in the graph. If "root", reindex from the root. If "self",
            reindex from this node. If False, do not reindex.
        ax : matplotlib.axes.Axes | None, default=None
            The matplotlib Axes to draw the graph on. If None, a new figure and axes are created.
        with_index : bool, default=True
            Whether to draw node indices on the graph. If True, the index of each node will be
            displayed in the node label. If False, only the node values will be displayed.
        with_labels : bool, default=True
            Whether to draw node labels (the value of the node) on the graph. See `networkx.draw`
            for more details.
        arrows : bool, default=True
            Whether to draw arrows between nodes. See `networkx.draw` for more details.
        **nxdraw_kwargs : Any
            Additional keyword arguments to pass to the `networkx.draw` drawing function.

        Returns
        -------
        matplotlib.axes.Axes
            The matplotlib Axes with the drawn graph.
        """
        if reindex:
            self.refresh(from_root=(reindex == "root"))

        ax = super().visualize(
            reindex=False,
            ax=ax,
            with_index=with_index,
            with_labels=with_labels,
            arrows=arrows,
            **nxdraw_kwargs,
        )
        ax.set_title(self.__str__())  # type: ignore
        return ax

    def __call__(
        self,
        X: ArrayLikeT,
        C: ArrayLikeT | Sequence[Number | None] | None,
        **kwargs: Any,
    ) -> ArrayLikeT | Number:
        """
        Alias for the `forward` method.

        See Also
        --------
        forward : the forward method to evaluate the expression.
        psr.base.func_unit.FuncUnit.forward : the forward method for function units.
        """
        return self.forward(X=X, C=C, **kwargs)

    def __str__(self) -> str:
        return self.format()
