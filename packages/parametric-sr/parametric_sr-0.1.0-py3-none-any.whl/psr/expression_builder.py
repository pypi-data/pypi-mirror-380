"""
implementation for a mathematical expression builder to support :class:`~psr.expression.Expression`.
"""

from dataclasses import dataclass, field, fields
from functools import update_wrapper
from multiprocessing import Pool
from typing import (
    Any,
    Callable,
    Final,
    Generic,
    Iterable,
    Literal,
    NoReturn,
    Self,
    Sequence,
    TypeAlias,
    TypedDict,
    cast,
    final,
    overload,
)

import numpy as np
from numpy.typing import NDArray

from .base import FuncUnit, Operation, Variable, Constant, DelayedConstant
from .base.base import WeakInstanceRegistry
from .collection import (
    PSRCollection,
    OperationCollection,
    VariableCollection,
    ConstantCollection,
    DelayedConstantCollection,
)
from .config import config
from .expression import Expression
from .func_unit import dummy_func_unit
from .typing import (
    ArrayLikeT,
    ExpressionHow,
    ExpressionEvolOptions,
    ExpressionInitOptions,
    ExpressionMutaOptions,
    Number,
    RngGeneratorSeed,
)
from .utils import compute_n_cpus, get_normalized_weights, validate_expression_how


class _Missing:
    """
    Marker class for missing values.
    """

    @final
    def __bool__(self) -> bool:
        return False


_missing: Final[_Missing] = _Missing()
dummy_expression = Expression(dummy_func_unit)


class _ExpressionTrackerBase(TypedDict, total=True):

    gen: int | None
    idx: int | None
    random_state: int | None
    how: ExpressionHow

    parent_1_info: tuple[int | None, int | None] | None
    parent_2_info: tuple[int | None, int | None] | None

    use_registry: bool


class _ExpressionTrackerLite(_ExpressionTrackerBase, total=True):
    """
    Typed dict class to represent a lightweight version of the expression tracker where the
    expressions are represented with a DFS-ordered list of function unit identifiers.
    """

    expression: list[str | Number]
    parent_1: list[str | Number] | None
    parent_2: list[str | Number] | None


class _ExpressionTrackerMixed(_ExpressionTrackerBase, Generic[ArrayLikeT], total=True):
    """
    Typed dict class to represent a mixed version of the expression tracker with both lightweight
    and heavyweight expression information.
    """

    expression: list[str | Number] | Expression[ArrayLikeT]
    parent_1: list[str | Number] | Expression[ArrayLikeT] | None
    parent_2: list[str | Number] | Expression[ArrayLikeT] | None

    use_registry: bool


class _ExpressionTrackerHeavy(_ExpressionTrackerBase, Generic[ArrayLikeT], total=True):
    """
    Typed dict class to represent a heavy version of the expression tracker with full expression
    information from the original :class:`Expression`.
    """

    expression: Expression[ArrayLikeT]
    parent_1: Expression[ArrayLikeT] | None
    parent_2: Expression[ArrayLikeT] | None


ExpressionLikeT: TypeAlias = list[str | Number] | Expression[ArrayLikeT]


@dataclass(frozen=True)
class ExpressionTracker(
    WeakInstanceRegistry[tuple[int, int] | None], Generic[ArrayLikeT]
):
    """
    A class to track how an :class:`Expression` instance was built to its current state in the
    parametric symbolic regression process.

    The tracker is frozen and cannot be modified after creation. To make changes, either create a
    new instance or *cheat* by using the methods: :func:`update_gen_idx`, :func:`update_parent`,
    :func:`update_random_state`, and :func:`update_how`. The `expression` property cannot be
    modified.

    Parameters
    ----------
    expression : ExpressionLikeT
        The :class:`Expression` instance to import, or a DFS-ordered list of expression nodes
        that can be converted into an :class:`Expression` instance.
    gen : int | None, default=None
        The generation number to locate/id the expression.
    idx : int | None, default=None
        The index number within the generation to locate/id the expression.
    random_state : int | None, default=None
        The random state that was used to generate the expression. Only integers or None are
        recorded. Intermediate states are not preserved to reduce memory usage.
    how : ExpressionHow, default=None
        The strategy used to create the expression. An expression can be initiated in several
        ways that require:

        1. no parent: custom `seed` from user (:class:`~psr.psr.ParametricSR`); *init* method
          from :class:`ExpressionBuilder`.
        2. one parent: mutation methods from :class:`ExpressionBuilder`.
        3. two parents: crossover methods from :class:`ExpressionBuilder`.
        4. two parents+: crossover first and then mutation.

    parent_1 : Self | ExpressionLikeT | None
        The first parent expression, if applicable. Also referred to as an acceptor. Check the
        details for the `how` argument.
    parent_1_info : tuple[int | None, int | None] | None
        The generation and index of the first parent expression, if applicable.
    parent_2 : Self | ExpressionLikeT | None
        The second parent expression, if applicable. Also referred to as a donor. This should
        only be set for expressions created with crossover. Check the details for the `how`
        argument.
    parent_2_info : tuple[int | None, int | None] | None
        The generation and index of the second parent expression, if applicable.

    See Also
    --------
    update_gen_idx : method to update the generation and index of the expression.
    update_parent : method to update the parent expressions.
    update_random_state : method to update the random state.
    update_how : method to update the strategy used to create the expression.
    to_expression : method to convert the tracker instance back to an :class:`Expression` instance.
    to_list : method to convert the tracker instance back to a list of expression nodes.
    to_dict : method to convert the tracker instance to a reloadable dictionary for serialization.
    from_dict : method to load the tracker instance from a dictionary (from :func:`to_dict`).
    from_expression : class method to create an :class:`ExpressionTracker` instance from an
        :class:`Expression` instance.
    to_expression : method to convert the tracker instance back to an :class:`Expression` instance.
    """

    expression: ExpressionLikeT[ArrayLikeT]
    gen: int | None = field(default=None)
    idx: int | None = field(default=None)
    random_state: int | None = field(default=None)
    how: ExpressionHow = field(default=None)

    parent_1: Self | ExpressionLikeT[ArrayLikeT] | None = field(
        default=None, repr=False
    )
    parent_1_info: tuple[int | None, int | None] | None = field(
        default=None, repr=False
    )
    parent_2: Self | ExpressionLikeT[ArrayLikeT] | None = field(
        default=None, repr=False
    )
    parent_2_info: tuple[int | None, int | None] | None = field(
        default=None, repr=False
    )

    use_registry: bool = field(default=True, repr=False)

    def __post_init__(self) -> None:
        """
        Post-initialization method to add the created tracker instance to the class registry if
        applicable.
        """
        if isinstance(self.parent_1, ExpressionTracker) and self.parent_1_info is None:
            object.__setattr__(self, "parent_1_info", self.parent_1.unsafe_key)
        if isinstance(self.parent_2, ExpressionTracker) and self.parent_2_info is None:
            object.__setattr__(self, "parent_2_info", self.parent_2.unsafe_key)

        gen, idx = self.gen, self.idx
        if isinstance(gen, int) and isinstance(idx, int) and self.use_registry:
            self.__class__.add_instance((gen, idx), self, overwrite=False)

    def update_gen_idx(self, gen: int | None, idx: int | None, /) -> None:
        """
        Update the generation and index of the ExpressionTracker instance, and update the class
        registry accordingly. The instance is only added to the registry if the new `(gen, idx)`
        key is valid (both are integers) and not taken by another instance. If the instance was
        previously in the registry with the old `(gen, idx)` key before the update, the old key will
        be removed from the registry to ensure no conflicts.

        Parameters
        ----------
        gen : int | None
            The generation to set.
        idx : int | None
            The index to set.

        Raises
        ------
        TypeError
            If the `gen` or `idx` parameters are not integers or None.
        ValueError
            If the new `(gen, idx)` key is valid but the key has been taken by another instance.
        """
        old_gen, old_idx = self.gen, self.idx
        if old_gen == gen and old_idx == idx:
            return

        if isinstance(gen, int) and isinstance(idx, int) and self.use_registry:
            self.__class__.add_instance(
                (gen, idx), self, check_key_mismatch=False, overwrite=False
            )

        # remove old instance from the registry if it exists
        if isinstance(old_gen, int) and isinstance(old_idx, int):
            self.__class__.remove_instance((old_gen, old_idx), self, error="ignore")

        # update instance attributes after successful registration
        object.__setattr__(self, "gen", gen)
        object.__setattr__(self, "idx", idx)

    def update_self(self, expression: ExpressionLikeT[ArrayLikeT]) -> None:
        """
        Update the expression stored in the ExpressionTracker instance.

        Parameters
        ----------
        expression : ExpressionLikeT[ArrayLikeT]
            The new expression to set.
        """
        if isinstance(expression, Expression):
            pass
        elif isinstance(expression, list) and all(
            isinstance(i, (str, int, float)) for i in expression
        ):
            pass
        else:
            raise TypeError("Invalid value for expression")
        object.__setattr__(self, "expression", expression)

    def update_parent(
        self,
        parent: Self | ExpressionLikeT[ArrayLikeT] | None,
        /,
        parent_info: tuple[int | None, int | None] | None | _Missing = _missing,
        which: Literal[1, 2] = 1,
    ) -> None:
        """
        Update the parent of the ExpressionTracker instance.

        Parameters
        ----------
        which : Literal[1, 2]
            The parent to update (1 or 2).
        parent : ExpressionLikeT[ArrayLikeT] | None
            The new parent expression or None to remove the parent.

        Raises
        ------
        TypeError
            If the `parent` parameter is not a valid expression type.
        """
        if which not in (1, 2):
            raise ValueError("can only update parent 1 or 2")

        if parent is None:
            pass
        elif type(parent) is self.__class__:
            pass
        elif isinstance(parent, Expression):
            pass
        elif isinstance(parent, list) and all(
            isinstance(i, (str, int, float)) for i in parent
        ):
            pass
        else:
            raise TypeError("Invalid value for parent")

        parent_prop = f"parent_{which:d}"
        object.__setattr__(self, parent_prop, parent)

        parent_info_prop = f"parent_{which:d}_info"
        if parent_info is not _missing:
            if parent_info is None:
                parent_info_ = None
            elif (
                isinstance(parent_info, tuple)
                and len(parent_info) == 2
                and all(x is None or isinstance(x, int) for x in parent_info)
            ):
                if all(x is None for x in parent_info):
                    parent_info_ = None
                else:
                    parent_info_ = parent_info
            else:
                raise TypeError("Invalid value for parent_info")
            object.__setattr__(self, parent_info_prop, parent_info_)
        elif isinstance(parent, (list, Expression)):
            pass
        elif parent:
            parent_info_: tuple[int | None, int | None] | None = parent.unsafe_key
            if all(x is None for x in parent_info_):
                parent_info_ = None
            object.__setattr__(self, parent_info_prop, parent_info_)

    def update_random_state(self, random_state: int | None, /) -> None:
        """
        Update the random state of the :class:`ExpressionTracker` instance. Only an integer can be
        accepted; all other values will be regarded as None.

        Parameters
        ----------
        random_state : int | None
            The new random state to set. Non-integer values will be regarded as None.

        Raises
        ------
        TypeError
            If the `random_state` parameter is not an integer or None.
        """
        if random_state is not None and not isinstance(random_state, int):
            raise TypeError("Invalid value for random_state")
        object.__setattr__(self, "random_state", random_state)

    def update_how(self, how: ExpressionHow, /) -> None:
        """
        Update the `how` attribute of the :class:`ExpressionTracker` instance.

        Parameters
        ----------
        how : ExpressionHow
            The new `how` value to set.

        Raises
        ------
        TypeError
            If the `how` parameter is not a valid expression builder type.
        """
        if not validate_expression_how(how):
            raise ValueError(f"Invalid value for how (no permitted: {how!r})")
        object.__setattr__(self, "how", how)

    @property
    def has_valid_key(self) -> bool:
        """
        Check if the ExpressionTracker instance has a valid key/identifier. This requires both the
        generation and index to be set as valid integers.

        Returns
        -------
        bool
            True if the instance has a valid key/identifier, False otherwise.
        """
        return isinstance(self.gen, int) and isinstance(self.idx, int)

    @property
    def unsafe_key(self) -> tuple[int | None, int | None]:
        """
        The unsafe key to identify the ExpressionTracker instance in the class registry.
        This key may contain None values if the generation or index is not set.

        Returns
        -------
        tuple[int | None, int | None]
            The generation and index of the instance, or None if not set.
        """
        return (self.gen, self.idx)

    @property
    def key(self) -> tuple[int, int] | None:
        """
        The key to identify the ExpressionTracker instance in the class registry.

        Returns
        -------
        tuple[int, int] | None
            The generation and index of the instance. The tuple can be used to uniquely identify
            the instance in the class registry. If any part of the key is not set, None will be
            returned.
        """
        if not isinstance(self.gen, int) or not isinstance(self.idx, int):
            return None
        return (self.gen, self.idx)

    def to_expression(
        self,
        types: Iterable[type[FuncUnit]] = (
            Operation,
            Variable,
            Constant,
            DelayedConstant,
        ),
        custom_registry: dict[str | Number, FuncUnit[ArrayLikeT]] | None = None,
        init: bool = False,
        **kwargs: Any,
    ) -> Expression[ArrayLikeT]:
        """
        Convert the :class:`ExpressionTracker` instance back into an :class:`Expression` instance.
        If the tracker was initialized with an expression, instead of a list of function unit nodes,
        the original expression will be returned. Otherwise, the node list will be used to construct
        a new expression.

        See details in :func:`Expression.import_list`.

        See Also
        --------
        Expression.import_list : the base method for importing expressions from a node list (DFS).
        to_list : method to export the tracked expression to a list of function unit identities.
        """
        if isinstance((expression := self.expression), Expression):
            return expression
        return Expression.import_list(
            expression,
            types=types,
            custom_registry=custom_registry,
            init=init,
            **kwargs,
        )

    def to_list(self) -> list[str | Number]:
        """
        Export the tracked expression to a DFS-ordered list of function unit identities.

        Returns
        -------
        list[str | Number]
            The exported list of function unit identities.

        See Also
        --------
        to_expression : method to convert the tracked expression back into an :class:`Expression`
            instance.
        psr.base.FuncUnit.integrated_identify : method to identify a function identity back to a
            :class:`psr.base.FuncUnit` instance.
        """
        expression = self.expression
        if isinstance(expression, Expression):
            return expression.export_list(simple=True)
        return expression

    @overload
    def to_dict(self, style: Literal["lite"] = "lite", /) -> _ExpressionTrackerLite: ...
    @overload
    def to_dict(self, style: Literal["mixed"], /) -> _ExpressionTrackerMixed: ...
    @overload
    def to_dict(self, style: Literal["heavy"], /) -> _ExpressionTrackerHeavy: ...

    def to_dict(
        self, style: Literal["lite", "mixed", "heavy"] = "lite", /
    ) -> _ExpressionTrackerLite | _ExpressionTrackerMixed | _ExpressionTrackerHeavy:
        """
        Export the tracker instance to a reloadable dictionary for serialization.

        Returns
        -------
        _ExpressionTrackerLite | _ExpressionTrackerMixed | _ExpressionTrackerHeavy
            A lightweight representation of the tracker instance with list of function unit
            identities, or a heavyweight representation with full expression information for
            serialization, or a mixed representation with both lightweight and heavyweight
            information.

        See Also
        --------
        from_dict : method to load the tracker instance from a dictionary (from :func:`to_dict`).
        to_expression : method to convert the tracker instance back to an :class:`Expression`
            instance.
        to_list : method to convert the tracker instance back to a list of expression nodes.
        """

        if style == "lite":
            p_list1: list[list[str | Number] | None] = []
            for parent in (self.parent_1, self.parent_2):
                if isinstance(parent, ExpressionTracker):
                    p_list1.append(parent.to_list())
                elif isinstance(parent, Expression):
                    p_list1.append(parent.export_list(simple=True))
                else:
                    p_list1.append(parent)
            return {
                "expression": self.to_list(),
                "gen": self.gen,
                "idx": self.idx,
                "random_state": self.random_state,
                "how": self.how,
                "parent_1": p_list1[0],
                "parent_1_info": self.parent_1_info,
                "parent_2": p_list1[1],
                "parent_2_info": self.parent_2_info,
                "use_registry": self.use_registry,
            }

        if style == "mixed":
            p_list2: list[Expression[ArrayLikeT] | list[str | Number] | None] = []
            for parent in (self.parent_1, self.parent_2):
                if isinstance(parent, ExpressionTracker):
                    p_list2.append(parent.to_expression())
                else:
                    p_list2.append(parent)
            return {
                "expression": self.to_expression(),
                "gen": self.gen,
                "idx": self.idx,
                "random_state": self.random_state,
                "how": self.how,
                "parent_1": p_list2[0],
                "parent_1_info": self.parent_1_info,
                "parent_2": p_list2[1],
                "parent_2_info": self.parent_2_info,
                "use_registry": self.use_registry,
            }

        if style == "heavy":
            p_list3: list[Expression[ArrayLikeT] | None] = []
            for parent in (self.parent_1, self.parent_2):
                if isinstance(parent, ExpressionTracker):
                    p_list3.append(parent.to_expression())
                elif isinstance(parent, Expression) or parent is None:
                    p_list3.append(parent)
                else:
                    p_list3.append(Expression.import_list(parent))
            return {
                "expression": self.to_expression(),
                "gen": self.gen,
                "idx": self.idx,
                "random_state": self.random_state,
                "how": self.how,
                "parent_1": p_list3[0],
                "parent_1_info": self.parent_1_info,
                "parent_2": p_list3[1],
                "parent_2_info": self.parent_2_info,
                "use_registry": self.use_registry,
            }

        raise ValueError("Unknown style")

    @classmethod
    def from_dict(
        cls,
        data: (
            _ExpressionTrackerLite | _ExpressionTrackerMixed | _ExpressionTrackerHeavy
        ),
        /,
        create_expression: bool = False,
        types: Iterable[type[FuncUnit[ArrayLikeT]]] = (
            Operation[ArrayLikeT],
            Variable[ArrayLikeT],
            Constant[ArrayLikeT],
            DelayedConstant[ArrayLikeT],
        ),
        custom_registry: dict[str | Number, FuncUnit[ArrayLikeT]] | None = None,
        init: bool = False,
        **kwargs: Any,
    ) -> Self:
        """
        Load an :class:`ExpressionTracker` instance from a dictionary, typically obtained from the
        :func:`to_dict` method.

        **Warning**: the values in the provided list may be used directly in the returned tracker
        instance and this may bring *cross-referencing* issues. Provide a (deep)copy of the input
        dictionary if you need to avoid this.

        Parameters
        ----------
        data : _ExpressionTrackerLite | _ExpressionTrackerMixed | _ExpressionTrackerHeavy
            The dictionary representation of the tracker instance.
        create_expression : bool, default=False
            When importing the expressions (the expression itself and its parents), whether to
            create :class:`Expression` instances, or leave them as the original lists.
        types : Iterable[type["FuncUnit"]]
            The subclasses of `FuncUnit` to consider **in order** during identification of the
            function unit identities in the lists. The first match is returned.
        custom_registry : dict[str | Number, FuncUnit[ArrayLikeT]] | None, default=None
            A custom registry for mapping identities to function units.
        init : bool, default=False
            Whether to initialize new function units if they are not found. The order of `types`
            also applies here - the first successful initialization will be used.

            > See :func:`psr.base.func_unit.FuncUnit.integrated_identify` for more details.
        **kwargs: Any
            Additional keyword arguments to pass to the constructor.

        See Also
        --------
        Expression.import_list : method to load an expression from a list representation.
        to_dict : method to convert the tracker instance to a dictionary representation.
        to_expression : method to convert the tracker instance back to an :class:`Expression`
            instance.
        to_list : method to convert the tracker instance back to a list of expression nodes.
        """
        if not create_expression:
            return cls(**data, **kwargs)

        new_data = cast(_ExpressionTrackerHeavy[ArrayLikeT], data.copy())
        for key in ("expression", "parent_1", "parent_2"):
            if (value := data[key]) is None:
                if key == "expression":
                    raise ValueError("Expression is required.")
                continue
            if isinstance(value, Expression):
                continue
            new_data[key] = Expression.import_list(
                value, types=types, custom_registry=custom_registry, init=init
            )
        return cls(**new_data, **kwargs)

    def __reduce__(
        self,
    ) -> (
        tuple[Callable, tuple[_ExpressionTrackerMixed, Literal[False]]]
        | tuple[Callable, tuple[_ExpressionTrackerLite]]
    ):
        """
        Custom reduce method for pickling the :class:`ExpressionTracker` instance. The referenced
        :class:`Expression` instances will be cast to a list of DFS-ordered function units to avoid
        cross-referencing issues.

        Returns
        -------
        tuple[Callable, tuple[_ExpressionTrackerMixed, Literal[False]]] | tuple[Callable, tuple[_ExpressionTrackerLite]]
            A tuple containing the callable to recreate the instance and its arguments.
        """
        if config.multiprocessing:
            data = self.to_dict("mixed")
            data["use_registry"] = False
            return (self.__class__.from_dict, (data, False))

        return (
            self.__class__.from_dict,
            (self.to_dict(),),
        )


class ExpressionTrackerBuilder:
    """
    A **decorator** for automatically generating :class:`ExpressionTracker` instances in the genetic
    programming pipeline.

    When using the decorator, the function being decorated only needs to return the expression
    generated in the process (e.g., crossover, mutation). The function should take two positional
    arguments: the first parent and the second parent (optional), and accept the keyword arguments:
    `random_state`, `return_tracker`, and `tracker_props`.

    See :func:`process_func_return` for more details on the requirements for the signature of the
    decorated function and how the return value from the function is processed.

    Examples
    --------
    .. code-block:: python

        # use the decorator directly; the func name will be used as the method name
        @ExpressionTrackerBuilder
        def my_expression_builder(parent_1, parent_2=None, /, *args, **kwargs):
            # Build and return the expression
            return expression

        expression, tracker = my_expression_builder(parent_1, parent_2, return_tracker=True)
        print(tracker.how)  # "my_expression_builder"

        # customize the name for the builder method
        @ExpressionTrackerBuilder(how="custom_builder")
        def my_expression_builder(parent_1, parent_2=None, /, *args, **kwargs):
            # Build and return the expression
            return expression

        expression, tracker = my_expression_builder(parent_1, parent_2, return_tracker=True)
        print(tracker.how)  # "custom_builder"

        # the decorator also works for class methods
        class MyClass:
            @ExpressionTrackerBuilder
            def my_method(self, parent_1, parent_2=None, /, *args, **kwargs):
                # Build and return the expression
                return expression

        instance = MyClass()
        expression, tracker = instance.my_method(parent_1, parent_2, return_tracker=True)
        print(tracker.how)  # "my_method"
    """

    def __init__(self, func=None, /, *, how: ExpressionHow = None) -> None:
        self.func = func
        if not validate_expression_how(how):
            raise TypeError(f"Invalid how parameter: {how}")
        self.how = how
        if func:
            update_wrapper(self, func)

    def __call__(
        self,
        *args,
        **kwargs: Any,
    ) -> Any:
        func = self.func
        if func is None:
            func = args[0]
            self.func = func
            update_wrapper(self, func)
            return self

        func_return = func(*args, **kwargs)
        return self.process_func_return(func, func_return, *args, **kwargs)

    def __get__(self, instance, owner) -> Callable[[*tuple[Any, ...]], Any]:
        """
        Ensure `self.func` binds correctly as a method.
        """
        if instance is None:
            # Accessed via class: return the decorator itself
            return self

        # Ensure `self.func` is not None before binding
        func = self.func
        if func is None:
            raise TypeError(
                f"{self.__class__.__name__} object has no function to bind."
            )

        # Bind function to instance: like functools.partial(self.func, instance)
        def bound(*args, **kwargs):
            func_return = func(instance, *args, **kwargs)
            return self.process_func_return(func, func_return, *args, **kwargs)

        update_wrapper(bound, func)
        return bound

    def process_func_return(
        self,
        func: Callable,
        func_return: Expression,
        parent_1,
        parent_2=None,
        /,
        *args,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        tracker_props: dict[str, Any] | None = None,
        how: ExpressionHow = None,
        **kwargs: Any,
    ):
        """
        Process the return value of the decorated function and create an :class:`ExpressionTracker`
        instance if requested.

        The decorated function should have a signature that includes the following parameters:

        - `parent_1`: The first parent expression.
        - `parent_2`: The second parent expression (optional).
        - `*args`: Any additional positional arguments.
        - `random_state`: The random state for reproducibility (optional).
        - `return_tracker`: Whether to return an :class:`ExpressionTracker` instance (optional).
        - `tracker_props`: Additional properties to customize the :class:`ExpressionTracker`
          (optional).
        - `how`: The method used to create the expression (optional). This will supersede the init
          value from the decorator and the name of the decorated function, if provided.
        - `**kwargs`: Any additional keyword arguments.

        The decorated function should only return an :class:`Expression` instance.
        """
        expression = func_return
        expression.refresh()
        if not return_tracker:
            return expression

        if not validate_expression_how(how):
            raise TypeError(f"Invalid how parameter: {how}")

        tracker_props = tracker_props or {}
        return ExpressionTracker(
            expression=expression,
            random_state=random_state if isinstance(random_state, int) else None,
            how=how or self.how or func.__name__,
            parent_1=parent_1,
            parent_2=parent_2,
            **tracker_props,
        )


@dataclass(frozen=True)
class ExpressionBuilder(Generic[ArrayLikeT]):
    """
    A builder class for constructing an :class:`Expression` instance in the parametric symbolic
    regression pipeline.

    Parameters
    ----------
    psr_collection : PSRCollection[ArrayLikeT], default=PSRCollection()
        The collection of function units available for building expressions. See details in
        :class:`PSRCollection`.
    min_height : int, default=0
        The minimum height of an expression allowed. A expression tree with a single root node has
        height of 0.
    max_height : int, default=5
        The maximum height of an expression allowed. Assuming a function unit can take a max of 2
        children, the expression can have a maximum number of nodes of :math:`2^{5+1} - 1 = 63`.
    enforce_height: bool, default=True
        Whether to enforce the height constraints during expression construction.
    init_methods : tuple[ExpressionInitOptions, ...], default=('random', 'balanced', 'full')
        The initialization methods to use for constructing expressions.
    init_probs: tuple[float, float, float] | None, default=None
        The probabilities associated with each initialization method (`random`, `balanced`, `full`).
    evol_methods: tuple[ExpressionEvolOptions, ...], default=('crossover', 'mutation', 'reproduction')
        The evolutionary methods to use for constructing expressions.
    evol_probs: tuple[float, ...] | None, default=(0.85, 0.14, 0.01)
        The probabilities associated with each evolutionary method.
    muta_methods: tuple[ExpressionMutaOptions, ...], default=('subtree', 'hoist', 'point')
        The mutation methods to use for constructing expressions.
    muta_probs: tuple[float, ...] | None, default=(0.5, 0.25, 0.25)
        The probabilities associated with each mutation method.
    cross_muta_prob: float, default=0.2
        The probability of triggering an extra mutation after crossover.
    max_height_allowed: int, default=10
        The maximum height allowed for expression trees. This is mostly used to restrict users from
        using a `max_height` that is too large.

    See Also
    --------
    init : method to initialize an :class:`Expression` instance with the specified parameters.
    seed : method to construct an :class:`Expression` instance from a preset scaffold.
    crossover : method to perform crossover between two :class:`Expression` instances.
    reproduction : method to perform reproduction (copying) of an :class:`Expression` instance.
    mutation_subtree : method to perform subtree mutation on an :class:`Expression` instance.
    mutation_hoist : method to perform hoisting mutation on an :class:`Expression` instance.
    mutation_point : method to perform point mutation on an :class:`Expression` instance.
    """

    psr_collection: PSRCollection[ArrayLikeT] = field(
        default_factory=PSRCollection[ArrayLikeT]
    )
    min_height: int = field(default=0)
    max_height: int = field(default=5)
    enforce_height: bool = field(default=True, init=True, repr=False)

    # random initialization of expression trees
    init_methods: tuple[ExpressionInitOptions, ...] = field(
        default=("random", "balanced", "full")
    )
    init_probs: tuple[float, ...] | None = field(default=(0.8, 0.15, 0.05), repr=False)

    # evolutionary methods
    evol_methods: tuple[ExpressionEvolOptions, ...] = field(
        default=("crossover", "mutation", "reproduction")
    )
    evol_probs: tuple[float, ...] | None = field(default=(0.85, 0.14, 0.01), repr=False)

    # mutation methods
    muta_methods: tuple[ExpressionMutaOptions, ...] = field(
        default=("subtree", "hoist", "point")
    )
    muta_probs: tuple[float, ...] | None = field(default=(0.5, 0.25, 0.25), repr=False)

    # crossover-mutation
    cross_muta_prob: float = field(default=0.2, repr=False)

    # do not change max_height_allowed unless you absolutely need to
    # this is a safeguard against overly complex expressions
    max_height_allowed: int = field(default=10, init=True, repr=False)

    _cache: dict[
        Literal["init_probs", "evol_probs", "muta_probs"], NDArray[np.float64]
    ] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        """
        Post initialization processing to set the initial probabilities of the initialization
        methods. The probabilities are normalized to sum to 1.
        """
        if self.min_height < 0 or self.max_height < 0:
            raise ValueError("Min height and max height must be non-negative.")
        if self.min_height > self.max_height:
            raise ValueError("Min height cannot exceed max height.")
        if self.max_height > self.max_height_allowed:
            raise ValueError(f"Max height cannot exceed {self.max_height_allowed}.")

        if not self.init_methods or len(self.init_methods) != len(
            set(self.init_methods)
        ):
            raise ValueError("Invalid initialization methods.")
        self._cache["init_probs"] = get_normalized_weights(
            self.init_probs, self.init_methods
        )

        if not self.evol_methods or len(self.evol_methods) != len(
            set(self.evol_methods)
        ):
            raise ValueError("Invalid evolutionary methods.")
        self._cache["evol_probs"] = get_normalized_weights(
            self.evol_probs, self.evol_methods
        )

        if not self.muta_methods and "mutation" in self.evol_methods:
            raise ValueError("Invalid mutation methods.")
        if len(self.muta_methods) != len(set(self.muta_methods)):
            raise ValueError("Invalid mutation methods.")
        self._cache["muta_probs"] = get_normalized_weights(
            self.muta_probs, self.muta_methods
        )

        if self.cross_muta_prob < 0 or self.cross_muta_prob > 1:
            raise ValueError("Crossover-mutation probability must be between 0 and 1.")

    @property
    def init_weights(self) -> NDArray[np.float64]:
        """
        The normalized weights for the initialization methods.
        """
        return self._cache["init_probs"]

    @property
    def evol_weights(self) -> NDArray[np.float64]:
        """
        The normalized weights for the evolutionary methods.
        """
        return self._cache["evol_probs"]

    @property
    def muta_weights(self) -> NDArray[np.float64]:
        """
        The normalized weights for the mutation methods.
        """
        return self._cache["muta_probs"]

    @property
    def operations(self) -> OperationCollection[ArrayLikeT]:
        """
        The collection of operations available for building expressions.

        See Also
        --------
        psr.collection.PSRCollection.operations : The collection of operations available for
            building expressions.
        psr.collection.OperationCollection : The class implementing the collection of operations.
        """
        return self.psr_collection.operations

    @property
    def variables(self) -> VariableCollection[ArrayLikeT]:
        """
        The collection of variables available for building expressions.

        See Also
        --------
        psr.collection.PSRCollection.variables : The collection of variables available for
            building expressions.
        psr.collection.VariableCollection : The class implementing the collection of variables.
        """
        return self.psr_collection.variables

    @property
    def constants(self) -> ConstantCollection[ArrayLikeT]:
        """
        The collection of constants available for building expressions.

        See Also
        --------
        psr.collection.PSRCollection.constants : The collection of constants available for
            building expressions.
        psr.collection.ConstantCollection : The class implementing the collection of constants.
        """
        return self.psr_collection.constants

    @property
    def delayed_constants(self) -> DelayedConstantCollection[ArrayLikeT]:
        """
        The collection of delayed constants available for building expressions.

        See Also
        --------
        psr.collection.PSRCollection.delayed_constants : The collection of delayed constants
            available for building expressions.
        psr.collection.DelayedConstantCollection : The class implementing the collection of delayed
            constants.
        """
        return self.psr_collection.delayed_constants

    @overload
    def build_once(
        self,
        src: Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]] | None,
        min_height: int | None,
        max_height: int | None,
        enforce_height: bool | None,
        random_state: RngGeneratorSeed,
        gen: int | None,
        idx: int | None,
        tracker_props: dict[str, Any] | None,
        no_raise: Literal[True],
    ) -> ExpressionTracker[ArrayLikeT] | None: ...
    @overload
    def build_once(
        self,
        src: (
            Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]] | None
        ) = None,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        gen: int | None = None,
        idx: int | None = None,
        tracker_props: dict[str, Any] | None = None,
        *,
        no_raise: Literal[True],
    ) -> ExpressionTracker[ArrayLikeT] | None: ...
    @overload
    def build_once(
        self,
        src: (
            Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]] | None
        ) = None,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        gen: int | None = None,
        idx: int | None = None,
        tracker_props: dict[str, Any] | None = None,
        no_raise: Literal[False] = False,
    ) -> ExpressionTracker[ArrayLikeT]: ...

    def build_once(
        self,
        src: (
            Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]] | None
        ) = None,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        gen: int | None = None,
        idx: int | None = None,
        tracker_props: dict[str, Any] | None = None,
        no_raise: bool = False,
    ) -> ExpressionTracker[ArrayLikeT] | None:
        """
        Build one expression and return an :class:`ExpressionTracker` to track how the expression
        was built.

        The build action is for one expression using one CPU.

        Parameters
        ----------
        src: Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]] | None
            The source expressions to build from. When no `src` is provides, the build task will be
            "init": randomly initialize an expression. Otherwise, there should be at least one
            source expressions, and the build task will be one of "crossover", "mutation",
            or "reproduction", including "crossover_mutation" and sub-mutation methods.
        min_height: int | None
            The minimum height of the expression.
        max_height: int | None
            The maximum height of the expression.
        enforce_height: bool | None
            Whether to enforce the height constraints. If None, will use the default behavior
            defined during initialization.
        random_state: RngGeneratorSeed | None
            The random state for reproducibility.
        gen: int | None = None
            The generation number for the tracker.
        idx: int | None = None
            The index of the expression in the generation.
        tracker_props: dict[str, Any] | None
            Additional properties for the tracker.
        no_raise: bool = False
            Whether to raise an error or return a None value when an exception occurs.

        Returns
        -------
        ExpressionTracker[ArrayLikeT] | None
            The tracker for the built expression, or None if building failed.
        """
        tracker_props = tracker_props or {}

        if src is None or len(src) == 0:
            try:
                tracker = self.init(
                    min_height=min_height,
                    max_height=max_height,
                    enforce_height=enforce_height,
                    random_state=random_state,
                    return_tracker=True,
                    tracker_props=tracker_props,
                )
            except Exception as e:
                if no_raise:
                    return None
                raise e
            tracker.update_gen_idx(gen, idx)
            return tracker

        # pick between crossover, mutation, and reproduction
        rng = np.random.default_rng(random_state)
        evo_method = rng.choice(self.evol_methods, p=self.evol_weights)

        parent1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
        parent2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
        n = len(src)
        match evo_method:
            case "crossover":
                n1, n2 = rng.choice(n, size=2, replace=True)
                parent1 = src[n1]
                parent2 = src[n2]
                if rng.random() < self.cross_muta_prob:
                    method = self.crossover_mutation
                else:
                    method = self.crossover
            case "mutation":
                parent1 = src[rng.choice(n)]
                parent2 = None
                method = self.mutation
            case "reproduction":
                parent1 = src[rng.choice(n)]
                parent2 = None
                method = self.reproduction
            case _:
                raise ValueError("Invalid evolutionary methods.")

        try:
            tracker = method(
                parent1,
                parent2,
                min_height=min_height,
                max_height=max_height,
                enforce_height=enforce_height,
                random_state=random_state,
                return_tracker=True,
                tracker_props=tracker_props,
            )
        except Exception as e:
            if no_raise:
                return None
            raise e
        tracker.update_gen_idx(gen, idx)
        return tracker

    def build(
        self,
        size: int,
        src: (
            Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]] | None
        ) = None,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        n_jobs: int | None = None,
        gen: int | None = None,
        idx_start: int | None = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> list[ExpressionTracker[ArrayLikeT]]:
        """
        Build **n** expressions for one generation and return their trackers (how they were built).

        **Warning**: Although this function supports multiprocessing with the `n_jobs` parameter,
        the overhead from serialization may actually negate the performance benefits. Thus, the
        implementation allocates at least 300 generation tasks per CPU core.

        Parameters
        ----------
        size: int
            The number of expressions to build.
        src: Sequence[Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]] | None
            The source expressions to use for building new ones.
        min_height: int | None
            The minimum height of the expressions.
        max_height: int | None
            The maximum height of the expressions.
        enforce_height: bool | None
            Whether to enforce the height constraints.
        random_state: RngGeneratorSeed | None
            The random seed to use for reproducibility.
        n_jobs: int | None
            The number of parallel jobs to run.
        gen: int | None
            The generation number for the generated expressions.
        idx_start: int | None
            The starting index for the new expressions.
        tracker_props: dict[str, Any] | None
            Additional properties to pass to the expression trackers.

        Returns
        -------
        list[ExpressionTracker[ArrayLikeT]]
            The list of expression trackers for the generated expressions.

        See Also
        --------
        build_once : method to build one expression.
        init : method to randomly initialize/generate an expression from scratch.
        seed : method to import a seed expression.
        crossover : method to crossover two expressions.
        reproduction : method to reproduce an expression (make a copy).
        mutation : integrated method to mutate an expression.
        mutation_subtree : method to perform subtree mutation on an expression.
        mutation_hoist : method to perform hoisting mutation on an expression.
        mutation_point : method to perform point mutation on an expression.
        crossover_mutation : method to perform crossover two expressions first and then mutate the
            generated expression.
        """
        if size < 1:
            raise ValueError("Size must be at least 1.")

        min_h = self.min_height if min_height is None else min_height
        max_h = self.max_height if max_height is None else max_height
        enforce_h = self.enforce_height if enforce_height is None else enforce_height

        rng = np.random.default_rng(random_state)
        n_cpus = min(int(np.ceil(size / 300)), compute_n_cpus(n_jobs))
        idx_start = 0 if idx_start is None else idx_start
        if idx_start < 0 or (gen is not None and gen < 0):
            raise ValueError("Invalid generation/index start.")
        random_states = rng.choice(2**32 - 1, size=size, replace=False)

        if n_cpus == 1:
            results = [
                self.build_once(
                    src=src,
                    min_height=min_h,
                    max_height=max_h,
                    enforce_height=enforce_h,
                    random_state=rs,
                    gen=gen,
                    idx=i,
                    tracker_props=tracker_props,
                    no_raise=True,
                )
                for i, rs in enumerate(random_states, start=idx_start)
            ]
            return [x for x in results if x is not None]

        # multiprocessing
        with config.multiprocessing(), Pool(n_cpus) as pool:
            results = pool.starmap(
                self.build_once,
                [
                    (src, min_h, max_h, enforce_h, rs, gen, i, tracker_props, True)
                    for i, rs in enumerate(random_states, start=idx_start)
                ],
            )
            return [x for x in results if x is not None]

    @overload
    def seed(
        self,
        nodes: Sequence[str | Number | FuncUnit[ArrayLikeT]] | Expression[ArrayLikeT],
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
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        return_tracker: Literal[True],
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def seed(
        self,
        nodes: Sequence[str | Number | FuncUnit[ArrayLikeT]] | Expression[ArrayLikeT],
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
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        return_tracker: Literal[False] = False,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    def seed(
        self,
        nodes: Sequence[str | Number | FuncUnit[ArrayLikeT]] | Expression[ArrayLikeT],
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
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        return_tracker: bool = False,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Initialize an :class:`Expression` from a seed scaffold. This can be useful in the PSR
        discovery process to provide some domain knowledge to guide the search process in the
        genetic programming context.

        The import is directly handled by the method :func:`FuncUnit.import_list`.

        Parameters
        ----------
        nodes : Sequence[str | Number | FuncUnit[ArrayLikeT]] | Expression[ArrayLikeT]
            The DFS-ordered nodes to construct an :class:`Expression` tree, or an existing
            :class:`Expression` instance.

            See :func:`FuncUnit.import_list` for more details on the expected format of the `nodes`,
            `types`, `custom_registry`, and `init` parameters.
        types : Iterable[type["FuncUnit[ArrayLikeT]"]]
            The types of the nodes in the expression tree.
        custom_registry : dict[str | Number, FuncUnit[ArrayLikeT]] | None
            A custom registry of function units to use during expression construction.
        init : bool
            Whether to initialize an unknown function unit.
        min_height : int | None
            The minimum height of the expression tree.
        max_height : int | None
            The maximum height of the expression tree.
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints. If None, will use the default behavior
            defined during initialization.
        return_tracker : bool
            Whether to return the expression tracker.
        tracker_props : dict[str, Any] | None
            Additional properties to pass to the expression tracker. For a seed expression, the keys
            should be limited to `idx` only and the `gen` should be 0.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The constructed expression, or the expression tracker containing the expression.

        Raises
        ------
        ValueError
            If the expression cannot be constructed or if the height constraints are violated.

        See Also
        --------
        Expression.import_list : Method to import a list of DFS-order function units to an
            :class:`Expression` tree.
        init : Class method to randomly initialize an :class:`Expression` tree.
        """
        if isinstance(nodes, Expression):
            expression = nodes
        else:
            expression = Expression.import_list(
                nodes, types=types, custom_registry=custom_registry, init=init
            )
        if enforce_height is None:
            enforce_height = self.enforce_height
        if enforce_height:
            min_ = min_height if min_height is not None else self.min_height
            max_ = max_height if max_height is not None else self.max_height

            min_h = max(0, min_)
            max_h = max(0, max_)
            exp_h = expression.height
            if min_h > max_h:
                raise ValueError("Invalid height range.")
            if exp_h < min_h or exp_h > max_h:
                raise ValueError(
                    f"Expression height {exp_h} out of bounds [{min_h}, {max_h}]."
                )

        if not return_tracker:
            return expression

        tracker_props = tracker_props or {}
        tracker_props.setdefault("gen", 0)
        return ExpressionTracker(
            expression=expression,
            random_state=None,
            how="seed",
            parent_1=None,
            parent_1_info=None,
            parent_2=None,
            parent_2_info=None,
            **tracker_props,
        )

    @overload
    def init(
        self,
        method: ExpressionInitOptions | str | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        tracker_props: dict[str, Any] | None = None,
        _is_root: bool = True,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def init(
        self,
        method: ExpressionInitOptions | str | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        tracker_props: dict[str, Any] | None = None,
        _is_root: bool = True,
    ) -> Expression[ArrayLikeT]: ...

    def init(
        self,
        method: ExpressionInitOptions | str | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        tracker_props: dict[str, Any] | None = None,
        _is_root: bool = True,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Randomly initialize an :class:`Expression` with the specified parameters.

        Parameters
        ----------
        method : ExpressionInitOptions | str  | None, default=None
            The initialization method to use, one of:

            1. `random`: randomly grow the expression between the min and max heights.
            2. `balanced`: grow the expression in a balanced manner. The expression tree should grow
              to the maximum height but not required to grow fully.
            3. `full`: fully grow the expression to the maximum height. All leaf nodes must be
              at the maximum height.
            4. *None*: randomly select an initialization method from the above options.

        min_height : int | None, default=None
            The minimum height of the expression. If None, use the default minimum height.
        max_height : int | None, default=None
            The maximum height of the expression. If None, use the default maximum height.
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints during initialization. Height constraints
            are always enforced during initialization. **NOT USED**
        random_state : RngGeneratorSeed | None, default=None
            The random seed to use for initialization. A *None* value does not set a seed.
        return_tracker : bool, default=False
            Whether to return an expression tracker showing how the expression was initialized,
            along with the expression.
        tracker_props : dict[str, Any] | None = None
            Additional properties to pass to the expression tracker for initialization. See
            :class:`ExpressionTracker` for more details. Cannot include the following keys:
            *expression*, *random_state*, and *how*.
        _is_root : bool, default=True
            Whether this initialization is called to generate a root expression. This is an internal
            flag used to control the behavior of the initialization process and avoid repeated
            refreshing of the subtree expressions. You should not modify this flag in most cases.
        **tracker_props : Any
            Additional properties to pass to the :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The initialized expression, or the expression tracker containing the expression.

        Raises
        ------
        ValueError
            One of the following:

            - Invalid initialization method.
            - Invalid height range

        See Also
        --------
        ExpressionTracker : The tracker class used to monitor the initialization process.
        seed : Method to import an :class:`Expression` tree from a preset scaffold.
        """
        rng = np.random.default_rng(random_state)
        if method is None:
            choices = self.init_methods
            init_method = choices[rng.choice(len(choices), p=self.init_weights)]
        else:
            if method not in self.init_methods:
                raise ValueError(
                    f"Invalid initialization method: {method}. "
                    f"Supported methods: {self.init_methods}."
                )
            init_method = method

        min_height = self.min_height if min_height is None else min_height
        max_height = self.max_height if max_height is None else max_height

        min_h, max_h = max(0, min_height), max(0, max_height)
        if min_h > max_h:
            raise ValueError("Invalid height range.")

        # do we terminate here or grow further?
        if max_h == 0:
            terminate = True
        elif min_h > 0:
            terminate = False
        elif init_method == "random":
            terminate = bool(rng.choice(2))
        elif init_method == "balanced":
            terminate = False
        elif init_method == "full":
            terminate = False
        else:
            raise ValueError(f"Invalid initialization method: {init_method}.")

        if terminate:
            expression = Expression(self.psr_collection.nselect(rng))
        else:
            func_unit = self.psr_collection.pselect(rng)
            expression = Expression(func_unit)

            arity = func_unit.arity
            if init_method == "balanced":
                child_methods = ["balanced"] + ["random"] * (arity - 1)
            else:  # random or full
                child_methods = [init_method] * arity
            for method in child_methods:
                expression.add_child(
                    self.init(
                        method,
                        min_height=min_h - 1,
                        max_height=max_h - 1,
                        random_state=rng,
                        return_tracker=False,
                        _is_root=False,
                    )
                )

        if _is_root:
            # refresh the expression from root for proper node indexing
            expression.refresh()

        if not return_tracker:
            return expression

        tracker_props = tracker_props or {}
        tracker_props.setdefault("use_registry", True)
        return ExpressionTracker(
            expression=expression,
            random_state=random_state if isinstance(random_state, int) else None,
            how=f"init-{init_method}",
            **tracker_props,
        )

    @overload
    def crossover(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def crossover(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    @ExpressionTrackerBuilder(how="crossover")
    def crossover(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Create a new :class:`Expression` by crossing over two parent expressions and return it. If
        requested, an :class:`ExpressionTracker` instance will be returned, instead.

        In `crossover`, a subtree in `parent_1` is replaced with a subtree from `parent_2`.

        This method only returns the newly created :class:`Expression`. The decorator
        :class:`ExpressionTrackerBuilder` will handle the tracking of the expression building
        process and return an :class:`ExpressionTracker` instance if requested. The decorator also
        handles the refreshing of the expression from the root for proper node indexing.

        Parameters
        ----------
        parent_1 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The primary parent expression. This will be used as the basis for the new expression. If
            the parent is provided as a :class:`ExpressionTracker`, its underlying expression will
            be used, as well as its tracking information when building the return tracker.

            As known as an acceptor in a crossover operation. A subtree in `parent_1` will be
            replaced with a subtree from `parent_2`.
        parent_2 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
            The secondary parent expression with a similar role as `parent_1`.

            Also known as a donor in a crossover operation. A subtree in `parent_2` will be used to
            replace a subtree in `parent_1`.

            If None, the acceptor `parent_1` is also used as the donor `parent_2`.
        min_height : int | None, default=None
            The minimum height of the new expression. If None, use the default minimum height from
            instance initialization.
        max_height : int | None, default=None
            The maximum height of the new expression. If None, use the default maximum height from
            instance initialization.
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints during crossover.

            - If None, will use the default behavior defined during initialization.
            - If True, the final expression will be generated with the specified height constraints,
            unless `parent_1` or `parent_2` violate these constraints themselves.

        random_state : RngGeneratorSeed | None, default=None
            The random state to use. *Only integers will be recorded in the returned tracker.
        return_tracker : bool, default=False
            Whether to return an :class:`ExpressionTracker`, in addition to the :class:`Expression`.
        how : ExpressionHow, default=None
            The method used to create the expression (optional). This will supersede the init value
            from the decorator and the name of the decorated function (`crossover`), if provided.
        tracker_props : dict[str, Any] | None, default=None
            Additional properties to use when creating the tracker. See :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The newly created expression, or the tracker containing it.

        Raises
        ------
        ValueError
            If the expression cannot be constructed or if the height constraints are violated.

        See Also
        --------
        ExpressionTrackerBuilder : Decorator for automatically building expression trackers.
        """
        rng = np.random.default_rng(random_state)
        if isinstance(parent_1, ExpressionTracker):
            expression_1 = parent_1.to_expression().copy()
        else:
            expression_1 = parent_1.copy()

        if parent_2 is None:
            expression_2 = expression_1.copy()
        elif isinstance(parent_2, ExpressionTracker):
            expression_2 = parent_2.to_expression()
        else:
            expression_2 = parent_2
        n1, n2 = len(expression_1), len(expression_2)

        idx_1 = rng.choice(n1)  # acceptor index
        node_1 = expression_1[idx_1]

        if enforce_height is None:
            enforce_height = self.enforce_height
        if not enforce_height:
            idx_2 = rng.choice(n2)
            node_1.update(expression_2[idx_2].copy())
            return expression_1

        # enforce height
        node_1.update(dummy_expression.copy())
        dummy_height = expression_1.height
        if min_height is None:
            min_height = self.min_height
        if max_height is None:
            max_height = self.max_height

        # calculate height requirement for the donor subtree
        min_h = max(0, min_height - dummy_height)
        max_h = max(0, max_height - node_1.depth)
        if min_h > max_h:
            raise ValueError("Invalid height range.")

        _ = expression_2.height  # cache height in all nodes
        heights = np.array([node._height for node in expression_2], dtype=int)
        idxs = np.where(np.bitwise_and(heights >= min_h, heights <= max_h))[0]
        if len(idxs) == 0:
            raise ValueError("Incompatible parents - height cannot be enforced.")
        idx_2 = rng.choice(idxs)
        node_1.update(expression_2[idx_2].copy())

        return expression_1

    @overload
    def reproduction(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def reproduction(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    @ExpressionTrackerBuilder
    def reproduction(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Create a new :class:`Expression` by reproduction from a parent expression and return it. If
        requested, an :class:`ExpressionTracker` instance will be returned, instead.

        **Development note:**
        This method (undecorated) only returns the newly created :class:`Expression`. The decorator
        :class:`ExpressionTrackerBuilder` will handle the tracking of the expression building
        process and return an :class:`ExpressionTracker` instance if requested. The decorator also
        handles the refreshing of the expression from the root for proper node indexing.

        Parameters
        ----------
        parent_1 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The primary parent expression. This will be used as the basis for the new expression. If
            the parent is provided as a :class:`ExpressionTracker`, its underlying expression will
            be used, as well as its tracking information when building the return tracker.
        parent_2 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
            The secondary parent expression with a similar role as `parent_1`. For a reproduction,
            the second parent is not needed and will not be used.
        min_height : int | None, default=None
            The minimum height of the new expression. **NOT APPLICABLE HERE**
        max_height : int | None, default=None
            The maximum height of the new expression. **NOT APPLICABLE HERE**
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints during reproduction. **NOT APPLICABLE HERE**
        random_state : RngGeneratorSeed | None, default=None
            The random state to use. **NOT APPLICABLE HERE**
        return_tracker : bool, default=False
            Whether to return an :class:`ExpressionTracker`, in addition to the :class:`Expression`.
        how : ExpressionHow, default=None
            The method used to create the expression (optional). This will supersede the init
            value from the decorator and the name of the decorated function (`reproduction`), if
            provided.
        tracker_props : dict[str, Any] | None, default=None
            Additional properties to use when creating the tracker. See :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The newly created expression, or the tracker containing it.
        Raises
        ------
        ValueError
            If the expression cannot be constructed or if the height constraints are violated.

        See Also
        --------
        ExpressionTrackerBuilder : Decorator for automatically building expression trackers.
        """
        if not isinstance(parent_1, Expression):
            parent_1 = parent_1.to_expression()
        return parent_1.copy()

    @overload
    def mutation_subtree(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        method: ExpressionInitOptions | str | None = None,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def mutation_subtree(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        method: ExpressionInitOptions | str | None = None,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    @ExpressionTrackerBuilder(how="mutation-subtree")
    def mutation_subtree(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        method: ExpressionInitOptions | str | None = None,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Create a new :class:`Expression` by performing subtree mutation on one parent expressions
        and return it. If requested, an :class:`ExpressionTracker` instance will be returned,
        instead.

        In `subtree mutation`, a subtree from `parent_1` is replaced with a new random subtree.

        This method only returns the newly created :class:`Expression`. The decorator
        :class:`ExpressionTrackerBuilder` will handle the tracking of the expression building
        process and return an :class:`ExpressionTracker` instance if requested. The decorator also
        handles the refreshing of the expression from the root for proper node indexing.

        Parameters
        ----------
        parent_1 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The primary parent expression. This will be used as the basis for the new expression. If
            the parent is provided as a :class:`ExpressionTracker`, its underlying expression will
            be used, as well as its tracking information when building the return tracker.

            A subtree in `parent_1` will be first be selected, and a new randomly generated subtree
            will be used to replace it.
        parent_2 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
            The secondary parent expression with a similar role as `parent_1`. Ignored in subtree
            mutation. Not applicable here.
        method : ExpressionInitOptions | str  | None, default=None
            The initialization method to use. See :func:`ExpressionBuilder.init` for more details.
        min_height : int | None, default=None
            The minimum height of the new expression. If None, use the default minimum height from
            instance initialization.
        max_height : int | None, default=None
            The maximum height of the new expression. If None, use the default maximum height from
            instance initialization.
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints during subtree mutation. If True, the final
            expression will be generated with the specified height constraints, unless `parent_1`
            or `parent_2` violate these constraints themselves.

            In `subtree mutation`, the height constraints are **always** enforced, either with the
            heights set at instantiation or the heights provided when calling the method.
        random_state : RngGeneratorSeed | None, default=None
            The random state to use. *Only integers will be recorded in the returned tracker.
        return_tracker : bool, default=False
            Whether to return an :class:`ExpressionTracker`, in addition to the :class:`Expression`.
        how : ExpressionHow, default=None
            The method used to create the expression (optional). This will supersede the init
            value from the decorator and the name of the decorated function (`mutation_subtree`), if
            provided.
        tracker_props : dict[str, Any] | None, default=None
            Additional properties to use when creating the tracker. See :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The newly created expression, or the tracker containing it.

        Raises
        ------
        ValueError
            If the expression cannot be constructed or if the height constraints are violated.

        See Also
        --------
        ExpressionTrackerBuilder : Decorator for automatically building expression trackers.
        """
        rng = np.random.default_rng(random_state)
        if isinstance(parent_1, ExpressionTracker):
            parent_1 = parent_1.to_expression()
        expression = parent_1.copy()

        n1 = len(expression)
        idx_1 = rng.choice(n1)  # acceptor index
        node_1 = expression[idx_1]
        # enforce height - always for subtree mutation
        node_1.update(dummy_expression.copy())
        dummy_height = expression.height
        if min_height is None:
            min_height = self.min_height
        if max_height is None:
            max_height = self.max_height

        if max_height < dummy_height:
            raise ValueError("Incompatible parents - height cannot be enforced.")

        # calculate height requirement for the donor subtree
        min_h = max(0, min_height - dummy_height)
        max_h = max(0, max_height - node_1.depth)
        if min_h > max_h:
            raise ValueError("Invalid height range.")

        parent_2 = self.init(
            method,
            min_height=min_h,
            max_height=max_h,
            random_state=rng,
            return_tracker=False,
        )
        node_1.update(parent_2)
        return expression

    @overload
    def mutation_hoist(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def mutation_hoist(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    @ExpressionTrackerBuilder(how="mutation-hoist")
    def mutation_hoist(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Create a new :class:`Expression` by performing hoist mutation on one parent expressions and
        return it. If requested, an :class:`ExpressionTracker` instance will be returned, instead.

        In `hoist mutation`, a subtree from `parent_1` is replaced with a subtree from the subtree
        itself. In other words, the selected subtree becomes the donor parent in a :func:`crossover`
        operation.

        This method only returns the newly created :class:`Expression`. The decorator
        :class:`ExpressionTrackerBuilder` will handle the tracking of the expression building
        process and return an :class:`ExpressionTracker` instance if requested. The decorator also
        handles the refreshing of the expression from the root for proper node indexing.

        Parameters
        ----------
        parent_1 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The primary parent expression. This will be used as the basis for the new expression. If
            the parent is provided as a :class:`ExpressionTracker`, its underlying expression will
            be used, as well as its tracking information when building the return tracker.

            A subtree in `parent_1` will be first be selected, and a subtree from the subtree will
            be used to replace it. In other words, the selected subtree becomes the donor parent in
            a :func:`crossover` operation.
        parent_2 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
            The secondary parent expression with a similar role as `parent_1`. Ignored in hoist
            mutation. Not applicable here.
        min_height : int | None, default=None
            The minimum height of the new expression. If None, use the default minimum height from
            instance initialization.
        max_height : int | None, default=None
            The maximum height of the new expression. If None, use the default maximum height from
            instance initialization.
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints during hoist mutation.

            - If None, the default behavior defined during initialization will be used.
            - If True, the final expression will be generated with the specified height constraints,
              unless `parent_1` violate these constraints themselves.

        random_state : RngGeneratorSeed | None, default=None
            The random state to use. *Only integers will be recorded in the returned tracker.
        return_tracker : bool, default=False
            Whether to return an :class:`ExpressionTracker`, in addition to the :class:`Expression`.
        how : ExpressionHow, default=None
            The method used to create the expression (optional). This will supersede the init
            value from the decorator and the name of the decorated function (`mutation_hoist`), if
            provided.
        tracker_props : dict[str, Any] | None, default=None
            Additional properties to use when creating the tracker. See :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The newly created expression, or the tracker containing it.

        Raises
        ------
        ValueError
            If the expression cannot be constructed or if the height constraints are violated.

        See Also
        --------
        ExpressionTrackerBuilder : Decorator for automatically building expression trackers.
        """
        rng = np.random.default_rng(random_state)
        if isinstance(parent_1, ExpressionTracker):
            parent_1 = parent_1.to_expression()
        expression = parent_1.copy()

        n1 = len(expression)
        idx_1 = rng.choice(n1)  # acceptor index
        node_1 = expression[idx_1]

        if enforce_height is None:
            enforce_height = self.enforce_height
        if not enforce_height:
            idx_2 = rng.choice(len(node_1))
            node_1.update(node_1[idx_2])
            return expression

        # enforce height
        parent_2 = node_1.copy(as_root=True)  # subtree becomes the donor
        node_1.update(dummy_expression.copy())
        dummy_height = expression.height
        if min_height is None:
            min_height = self.min_height
        if max_height is None:
            max_height = self.max_height

        # calculate height requirement for the donor subtree
        min_height = max(0, min_height - dummy_height)
        max_height = max(0, max_height - node_1.depth)

        _ = parent_2.height  # cache height in all nodes
        heights = np.array([node._height for node in parent_2])
        idxs = np.where(np.bitwise_and(heights >= min_height, heights <= max_height))[0]
        if len(idxs) == 0:
            raise ValueError("Incompatible parents - height cannot be enforced.")
        idx_2 = rng.choice(idxs)
        node_1.update(parent_2[idx_2])

        return expression

    @overload
    def mutation_point(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def mutation_point(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    @ExpressionTrackerBuilder(how="mutation-point")
    def mutation_point(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Create a new :class:`Expression` by performing point mutation on one parent expressions and
        return it. If requested, an :class:`ExpressionTracker` instance will be returned, instead.

        In `point mutation`, a function unit node from `parent_1` is replaced with a function unit
        node of the same arity. The mutated expression will be the same as `parent_1` except for
        one node. For example, `+`, `-`, `*`, `/` could be replaced with each other because they all
        have an arity of 2.

        This method only returns the newly created :class:`Expression`. The decorator
        :class:`ExpressionTrackerBuilder` will handle the tracking of the expression building
        process and return an :class:`ExpressionTracker` instance if requested. The decorator also
        handles the refreshing of the expression from the root for proper node indexing.

        Parameters
        ----------
        parent_1 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The primary parent expression. This will be used as the basis for the new expression. If
            the parent is provided as a :class:`ExpressionTracker`, its underlying expression will
            be used, as well as its tracking information when building the return tracker.

            A function unit node in `parent_1` will be first be selected and then replaced with a
            new function unit node of the same arity. The mutated expression will be the same as
            `parent_1` except for one node.
        parent_2 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
            The secondary parent expression with a similar role as `parent_1`. Ignored in point
            mutation. Not applicable here.
        min_height : int | None, default=None
            The minimum height of the new expression. If None, use the default minimum height from
            instance initialization. Not applicable here.
        max_height : int | None, default=None
            The maximum height of the new expression. If None, use the default maximum height from
            instance initialization. Not applicable here.
        enforce_height : bool | None, default=True
            Whether to enforce the height constraints during point mutation. **Not applicable**. The
            returned expression will have the same heights as `parent_1`.
        random_state : RngGeneratorSeed | None, default=None
            The random state to use. *Only integers will be recorded in the returned tracker.
        return_tracker : bool, default=False
            Whether to return an :class:`ExpressionTracker`, in addition to the :class:`Expression`.
        how : ExpressionHow, default=None
            The method used to create the expression (optional). This will supersede the init
            value from the decorator and the name of the decorated function (`mutation_point`), if
            provided.
        tracker_props : dict[str, Any] | None, default=None
            Additional properties to use when creating the tracker. See :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The newly created expression, or the tracker containing it.

        Raises
        ------
        ValueError
            If the expression cannot be constructed or the function unit collection is incomplete.

        See Also
        --------
        ExpressionTrackerBuilder : Decorator for automatically building expression trackers.
        """
        rng = np.random.default_rng(random_state)
        if isinstance(parent_1, ExpressionTracker):
            parent_1 = parent_1.to_expression()
        expression = parent_1.copy()

        n1 = len(expression)
        node_1 = expression[rng.choice(n1)]
        arity = node_1.func_unit.arity
        if arity == 0:
            new_func_unit = self.psr_collection.nselect(rng)
        else:
            collection = self.psr_collection.operations
            idxs = [
                i for i, value in enumerate(collection.values) if value.arity == arity
            ]
            weights = collection.weights[idxs]
            total_weight = np.sum(weights)
            if np.isclose(total_weight, 0):
                raise ValueError(
                    f"No function units with arity={arity} found in the collection."
                )
            weights /= total_weight
            new_func_unit = collection.values[rng.choice(idxs, p=weights)]
        node_1.func_unit = new_func_unit
        return expression

    @overload
    def mutation(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        mutation: ExpressionMutaOptions | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def mutation(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        mutation: ExpressionMutaOptions | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    def mutation(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        mutation: ExpressionMutaOptions | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Create a new :class:`Expression` by performing one mutation on one parent expressions and
        return it. If requested, an :class:`ExpressionTracker` instance will be returned, instead.

        In `subtree mutation`, a subtree from `parent_1` is replaced with a new random subtree.

        This method only returns the newly created :class:`Expression`. The decorator
        :class:`ExpressionTrackerBuilder` will handle the tracking of the expression building
        process and return an :class:`ExpressionTracker` instance if requested. The decorator also
        handles the refreshing of the expression from the root for proper node indexing.

        Parameters
        ----------
        parent_1 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The primary parent expression. This will be used as the basis for the new expression. If
            the parent is provided as a :class:`ExpressionTracker`, its underlying expression will
            be used, as well as its tracking information when building the return tracker.

            A subtree in `parent_1` will be first be selected, and a new randomly generated subtree
            will be used to replace it.
        parent_2 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
            The secondary parent expression with a similar role as `parent_1`. Ignored in subtree
            mutation. Not applicable here.
        mutation : Literal["subtree", "hoist", "point"] | None
            The type of mutation to apply to the offspring after crossover.

            The `mutation` method also determines how the tracker will be named. The `how` property
            of the returned :class:`ExpressionTracker` will be set to `("crossover", <mutation>)`.

            If None, a random mutation method will be selected.
        min_height : int | None, default=None
            The minimum height of the new expression. If None, use the default minimum height from
            instance initialization.
        max_height : int | None, default=None
            The maximum height of the new expression. If None, use the default maximum height from
            instance initialization.
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints during subtree mutation. If True, the final
            expression will be generated with the specified height constraints, unless `parent_1`
            or `parent_2` violate these constraints themselves.
        random_state : RngGeneratorSeed | None, default=None
            The random state to use. *Only integers will be recorded in the returned tracker.
        return_tracker : bool, default=False
            Whether to return an :class:`ExpressionTracker`, in addition to the :class:`Expression`.
        how : ExpressionHow, default=None
            The method used to create the expression (optional). This will supersede the init
            value from the decorator and the name of the decorated function (`mutation_subtree`), if
            provided.
        tracker_props : dict[str, Any] | None, default=None
            Additional properties to use when creating the tracker. See :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The newly created expression, or the tracker containing it.

        Raises
        ------
        ValueError
            If the expression cannot be constructed or if the height constraints are violated.

        See Also
        --------
        mutation_subtree : Method for subtree mutation.
        mutation_hoist : Method for hoist mutation.
        mutation_point : Method for point mutation.
        """
        rng = np.random.default_rng(random_state)

        if mutation is None:
            _mutation = self.muta_methods[rng.choice(len(self.muta_methods))]
        else:
            _mutation = mutation
        match _mutation:
            case "subtree":
                func = self.mutation_subtree
                mutation_method = "mutation-subtree"
            case "hoist":
                func = self.mutation_hoist
                mutation_method = "mutation-hoist"
            case "point":
                func = self.mutation_point
                mutation_method = "mutation-point"
            case _:
                raise ValueError("Unsupported mutation type.")

        expression = func(
            parent_1,
            parent_2,
            min_height=min_height,
            max_height=max_height,
            enforce_height=enforce_height,
            random_state=random_state,
            return_tracker=False,
        )
        if not return_tracker:
            return expression

        tracker_props = tracker_props or {}
        if not isinstance(random_state, int):
            random_state = None
        return ExpressionTracker(
            expression,
            random_state=random_state,
            how=how or mutation_method,
            parent_1=parent_1,
            parent_2=parent_2,
            **tracker_props,
        )

    @overload
    def crossover_mutation(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: None,
        mutation: ExpressionMutaOptions | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> NoReturn: ...
    @overload
    def crossover_mutation(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        mutation: ExpressionMutaOptions | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[True],
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> ExpressionTracker[ArrayLikeT]: ...
    @overload
    def crossover_mutation(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        mutation: ExpressionMutaOptions | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: Literal[False] = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT]: ...

    def crossover_mutation(
        self,
        parent_1: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT],
        parent_2: Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None = None,
        mutation: ExpressionMutaOptions | None = None,
        /,
        *,
        min_height: int | None = None,
        max_height: int | None = None,
        enforce_height: bool | None = None,
        random_state: RngGeneratorSeed = None,
        return_tracker: bool = False,
        how: ExpressionHow = None,
        tracker_props: dict[str, Any] | None = None,
    ) -> Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]:
        """
        Create a new :class:`Expression` by crossing over two parent expressions first, and then
        applying mutation to the offspring, and return it. If requested, an
        :class:`ExpressionTracker` instance will be returned, instead.

        See details in :func:`crossover`, :func:`mutation_subtree`, :func:`mutation_hoist`, and
        :func:`mutation_point`.

        Parameters
        ----------
        parent_1 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The primary parent expression. This will be used as the basis for the new expression. If
            the parent is provided as a :class:`ExpressionTracker`, its underlying expression will
            be used, as well as its tracking information when building the return tracker.

            As known as an acceptor in a crossover operation. A subtree in `parent_1` will be
            replaced with a subtree from `parent_2`.
        parent_2 : Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT] | None
            The secondary parent expression with a similar role as `parent_1`.

            Also known as a donor in a crossover operation. A subtree in `parent_2` will be used to
            replace a subtree in `parent_1`.

            If None, the acceptor `parent_1` will also be used as the donor `parent_2`.
        mutation : Literal["subtree", "hoist", "point"] | None
            The type of mutation to apply to the offspring after crossover.

            The `mutation` method also determines how the tracker will be named. The `how` property
            of the returned :class:`ExpressionTracker` will be set to `("crossover", <mutation>)`.

            If None, a random mutation method will be selected.
        min_height : int | None, default=None
            The minimum height of the new expression. If None, use the default minimum height from
            instance initialization.
        max_height : int | None, default=None
            The maximum height of the new expression. If None, use the default maximum height from
            instance initialization.
        enforce_height : bool | None, default=None
            Whether to enforce the height constraints during crossover and the subsequent mutation.
            If True, the final expression will be generated with the specified height constraints,
            unless `parent_1` or `parent_2` violate these constraints themselves.
        random_state : RngGeneratorSeed | None, default=None
            The random state to use. *Only integers will be recorded in the returned tracker.
        return_tracker : bool, default=False
            Whether to return an :class:`ExpressionTracker`, in addition to the :class:`Expression`.
        how : ExpressionHow, default=None
            The method used to create the expression (optional). This will supersede the init value
            from the decorator, the name of the decorated function (`crossover`), and the `mutation`
            argument, if provided.
        tracker_props : dict[str, Any] | None, default=None
            Additional properties to use when creating the tracker. See :class:`ExpressionTracker`.

        Returns
        -------
        Expression[ArrayLikeT] | ExpressionTracker[ArrayLikeT]
            The newly created expression, or the tracker containing it

        Raises
        ------
        ValueError
            If the expression cannot be constructed or if the height constraints are violated.

        See Also
        --------
        ExpressionTrackerBuilder : Decorator for automatically building expression trackers.
        crossover : Method for performing crossover between two expressions.
        mutation_subtree : Method for performing subtree mutation on an expression.
        mutation_hoist : Method for performing hoisting mutation on an expression.
        mutation_point : Method for performing point mutation on an expression.
        """
        rng = np.random.default_rng(random_state)
        if enforce_height is None:
            enforce_height = self.enforce_height
        expression_1 = self.crossover(
            parent_1,
            parent_2,
            min_height=min_height,
            max_height=max_height,
            enforce_height=enforce_height,
            random_state=rng,
            return_tracker=False,
        )

        tracker = self.mutation(
            expression_1,
            None,
            mutation,
            min_height=min_height,
            max_height=max_height,
            enforce_height=enforce_height,
            random_state=rng,
            return_tracker=True,
            tracker_props=tracker_props,
        )
        expression_2 = tracker.to_expression()
        if not return_tracker:
            return expression_2

        if isinstance(random_state, int):
            tracker.update_random_state(random_state)
        tracker.update_how(how or ("crossover", cast(str, tracker.how)))
        tracker.update_parent(parent_1, which=1)
        tracker.update_parent(parent_2, which=2)
        return tracker

    def __reduce__(self) -> tuple[type[Self], tuple[Any, ...]]:
        """
        Serialize the object for pickling.
        """
        return (
            self.__class__,
            tuple(getattr(self, f.name) for f in fields(self.__class__) if f.init),
        )
