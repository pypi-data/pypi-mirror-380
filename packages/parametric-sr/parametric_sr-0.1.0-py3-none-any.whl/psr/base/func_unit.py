"""
This module contains the base class for function units in the PSR framework. A function unit
represents a node in a symbolic regression tree, encapsulating either an operation, a variable, a
constant, or a delayed constant.

For example, the function `y = x + 1` has three function units:

- `x` (variable)
- `1` (constant)
- `+` (operation)

The base `FuncUnit` class provides base functionality for all function units used in the PSR
framework.
"""

from abc import ABC, abstractmethod
from contextlib import contextmanager
from copy import deepcopy
import inspect
import pickle
import re
import sys
from typing import (
    Any,
    Callable,
    ClassVar,
    Generator,
    Generic,
    Iterable,
    Literal,
    NoReturn,
    Self,
    Sequence,
    Type,
    final,
    overload,
)
import warnings

import numpy as np

from ..config import config
from ..typing import ArrayLikeT, HashableT, Number, T
from .base import InstanceRegistry
from .formatter import Formatter


class FuncUnit(Generic[ArrayLikeT], ABC):
    """
    Base class for function units in the PSR framework.

    A function unit can represent an operation, a variable, a constant, or a delayed constant.
    It is used to build symbolic regression trees and each function unit occupies one node in the
    tree.

    - `operation`: such as `+`, `-`, `*`, `/`, etc.
    - `variable`: such as `x0`, `x1`, etc.
    - `constant`: deterministic constant values such as `1.0`, `3.14`, etc.
    - `delayed constant`: a constant variable that is determined at fit time when fitting the
      function to data.

    The generic type for a `FuncUnit` should typically be one of `np.ndarray`, `torch.Tensor`, or
    similar types that can represent array-like data for your input data (X and y). A function unit
    should handle array-like data appropriately, including broadcasting and other tensor operations.

    Subclassing
    -----------
    The `immutable` parameter : bool, default=True. If set to `True`, instances of the subclass
    should not be modified after instantiation, especially for its core functionality. For example,
    an operation's core is the **operation** (e.g., addition); a variable's core is its column
    index in the input `X`; a constant's core is its value (e.g., `1.0`, `3.14`).

    The copy of an `immutable` instance should return itself to reduce memory usage. Otherwise, a
    new instance should be created with the same core attributes, but a different object identity.

    **Note**: There is no built-in function in `FuncUnit` to enforce immutability. You must use
    the `immutable` parameter to implement custom immutability logic. The `mutate` method offers
    a context manager to temporarily allow mutations.

    **When subclassing `FuncUnit`**

    - consider the `immutable` parameter and its implications for your subclass.
    - implement the `evaluate` method and follow the same signature as the base class.
    - implement the `reinit` method for getting a new **non-singleton** instance of the same
      function unit.
    """

    _immutable: ClassVar[bool] = True
    _mutation_error: ClassVar[Exception] = ValueError(
        f"{__name__} is immutable and cannot be modified. "
        "Use context manager `with <instance>.mutate()` to temporarily allow modifications."
    )

    def __init_subclass__(cls, immutable: bool = True, **kwargs: Any) -> None:
        """
        set up the subclass

        Parameters
        ----------
        immutable : bool, default=True
            Whether the class instances should be immutable.
        """
        cls._immutable = immutable
        cls._mutation_error = ValueError(
            f"{cls.__name__} is immutable and cannot be modified. "
            "Use context manager `with <instance>.mutate()` to temporarily allow modifications."
        )
        super().__init_subclass__(**kwargs)

    @property
    def name(self) -> str:
        """
        Get the name/representation of the function unit.

        Returns
        -------
        str
            The name or representation of the function unit. This is typically used for compling
            the string representation of the entire expression with the function unit.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        ## Property Setter
        Set the name/representation of the function unit.

        Parameters
        ----------
        new_name : str
            The name or representation of the function unit. This must be a valid Python identifier
            and must not end with a digit.

        Raises
        ------
        ValueError
            - If the new name is not a valid Python identifier.
            - If the new name ends with a digit.
        """
        if not new_name.isidentifier() or new_name[-1].isdigit():
            raise ValueError(
                f"Invalid {self.__class__.__name__} function unit name: {new_name}. "
                f"Must be a valid Python identifier and not end with a digit."
            )
        self._name = new_name

    @property
    def identity(self) -> str | Number:
        """
        The identity of the function unit that can be used to track back to the object. By default,
        this will be the name of the function unit.

        For example, if the `identity` is the `name` of `Add`, then using the string `Add`, the
        `identify` method should be able to retrieve the corresponding `Add` object of `Operation`.

        See Also
        --------
        identify : method to retrieve the corresponding constant object using an identity.
        """
        return self.name

    @property
    def arity(self) -> int:
        """
        Get the arity of the function unit.

        Returns
        -------
        int
            The arity of the function unit, which is the number of arguments it takes. For example,
            an operation like `+` has an arity of 2, while a variable has an arity of 0.
        """
        return self._arity

    @arity.setter
    def arity(self, new_arity: int) -> None:
        """
        ## Property Setter
        Set the arity of the function unit.

        Parameters
        ----------
        new_arity : int
            The arity of the function unit. This should be a non-negative integer.

        Raises
        ------
        ValueError
            A ValueError is raised if:

            - If the function unit is currently immutable.
            - If the new arity is not a non-negative integer.
        """
        if self.is_immutable and hasattr(self, "_arity") and not config.inplace_update_:
            raise self._mutation_error

        if new_arity < 0:
            raise ValueError(
                f"Invalid {self.__class__.__name__} function unit arity: {new_arity}. "
                "Arity must be a non-negative integer."
            )
        self._arity = new_arity

    @property
    def weight(self) -> float:
        """
        Get the weight of the function unit.

        Returns
        -------
        float
            The weight/priority of the function unit for selection in the genetic programming
            process. The weight is relative within the same type of function unit, e.g., Operation,
            Variable, etc.

            The weight should be non-negative. Function units with a weight of 0. are ignored
            during the genetic programming process.
        """
        return self._weight

    @weight.setter
    def weight(self, new_weight: int | float) -> None:
        """
        ## Property Setter
        Set the weight/priority of the function unit.

        Parameters
        ----------
        new_weight : int | float
            The new weight/priority of the function unit. This must be a non-negative value.

        Raises
        ------
        ValueError
            If the new weight is negative.
        """
        if new_weight < 0:
            raise ValueError(
                f"Invalid {self.__class__.__name__} function unit weight: {new_weight}. "
                "Weight must be a non-negative value."
            )
        self._weight = float(new_weight)

    @property
    def cost(self) -> int | float:
        """
        Get the cost/complexity of the function unit.

        The cost must be positive.

        Returns
        -------
        int | float
            The cost of the function unit.
        """
        return self._cost

    @cost.setter
    def cost(self, new_cost: int | float) -> None:
        """
        ## Property Setter
        Set the cost/complexity of the function unit.

        Parameters
        ----------
        new_cost : int | float
            The new cost/complexity of the function unit. This must be a positive value.

        Raises
        ------
        ValueError
            If the new cost is not positive.
        """
        if new_cost <= 0:
            raise ValueError(
                f"Invalid {self.__class__.__name__} function unit cost: {new_cost}. "
                "Cost must be a positive value."
            )
        self._cost = float(new_cost)

    @property
    def protection_rules(self) -> Sequence[bool]:
        """
        Get the protection rules for the function unit. This mostly applies to function units that
        are operators and takes arguments, e.g., operations such as `+`, `-`, `*`, `/`, etc. The
        protection rules apply to whether the string representation of the arguments needs to be
        protected with parentheses when formatting the expression.

        This property is specifically designed for the `Operation` subclass. The default
        implementation is for compatibility.

        Returns
        -------
        Sequence[bool]
            A sequence of boolean values representing the protection rules for the function unit.
            These rules are used to determine whether the operation needs to be protected with
            parentheses when formatting the expression.
        """
        if self.arity != 0:
            raise ValueError(
                f"Invalid {self.__class__.__name__} function has an arity of {self.arity}. "
                f"The default `protection_rules` must be customized to match the arity."
            )
        return tuple()

    @property
    def is_immutable(self) -> bool:
        """
        Check if the function unit is immutable.

        Returns
        -------
        bool
            True if the function unit is immutable, False otherwise.

        See Also
        --------
        mutate : context manager methods for mutating the function unit.
        """
        return getattr(self, "_immutable_t", self._immutable)

    @property
    def is_singleton(self) -> bool:
        """
        Check if the function unit is a singleton.

        This property is specifically designed for the `SingletonFuncUnit` subclass. The default
        implementation is for compatibility, and the default behavior is to return False.

        Returns
        -------
        bool
            True if the function unit is a singleton, False otherwise (default: False).

        See Also
        --------
        copy : method to make a copy of the function unit. The copy of a singleton is itself.
        """
        return False

    @property
    def is_delayed(self) -> bool:
        """
        Check if the function unit is a delayed constant.

        This property is specifically designed for the `DelayedConstant` subclass. The default
        implementation is for compatibility.

        Returns
        -------
        bool
            True if the function unit is a delayed constant, False otherwise.
        """
        return False

    @property
    def is_fitted(self) -> bool:
        """
        Check if the function unit has been fitted to the data (or does not require fitting). False
        means that the function unit requires fitting **and** has not been fitted yet.

        This property is specifically designed for the `FittedFuncUnit` subclass. The default
        implementation is for compatibility. By default, regular function units do not require
        fitting, so this should return True.

        Returns
        -------
        bool
            True if the function unit has been fitted to the data, False otherwise.
        """
        return True

    @abstractmethod
    def evaluate(
        self,
        *args: ArrayLikeT | Number,
        X: ArrayLikeT | None = None,
        C: ArrayLikeT | Sequence[Number | None] | None = None,
        **kwargs: Any,
    ) -> ArrayLikeT | Number:
        """
        Evaluate the function unit with the given arguments.

        Parameters
        ----------
        *args : ArrayLikeT | Number
            Positional arguments to evaluate the function unit.
        X : ArrayLikeT | None, default=None
            Placeholder keyword argument for the input data array, typically a 2D array-like
            structure where each row represents a data point and each column represents a variable.
        C : ArrayLikeT | Sequence[Number | None] | None, default=None
            Placeholder keyword argument for the 1D array of delayed constants. This is used to pass
            constants that are determined at fit time when fitting the function to data.
        **kwargs : Any
            Keyword arguments to evaluate the function unit.

        Returns
        -------
        ArrayLikeT | Number
            The result of evaluating the function unit.

        See Also
        --------
        forward : alias method for compatibility with PyTorch's `forward` method.
        __call__ : alias method for compatibility with PyTorch's `__call__` method.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def format(self, *args: str, protect: bool = False, **kwargs: Any) -> str:
        """
        Method to format the function unit into a string representation for the entire expression.
        For operations that take multiple arguments, the `args` parameter will contain the
        string representations of the arguments to be formatted into the operation's template.

        Parameters
        ----------
        *args : str
            String representations of the arguments to be formatted into the operation's template.
            For non-operation function units, this should be empty/omitted.
        protect : bool, default=False
            Whether the returned string should be protected with parentheses, if necessary.

            For example, if the operation is `+` and the arguments are `x` and `y`, the returned
            string representation should be formatted as `x + y` with the template `{0} + {1}`. But
            if `x + y` is part of a larger expression, it should be protected with parentheses
            to ensure the correct order of operations, resulting in `({0} + {1})`.

            For already protected expressions, this parameter should not take effect. Examples of
            protected expressions are `x`, `max(x, y)`, `exp(x)`, etc. These expressions should not
            be protected again to avoid unnecessary parentheses.
        **kwargs : Any
            Additional keyword arguments to customize the formatting behavior.
        """
        raise NotImplementedError(
            "Subclasses must implement the format method to provide a string representation."
        )

    @final
    def forward(
        self,
        *args: ArrayLikeT | Number,
        X: ArrayLikeT | None = None,
        C: ArrayLikeT | Sequence[Number | None] | None = None,
        **kwargs: Any,
    ) -> ArrayLikeT | Number:
        """
        Alias for `evaluate` to evaluate the function unit, for compatibility with PyTorch's
        `forward` method.

        Evaluate the function unit with the given arguments.

        Parameters
        ----------
        *args : ArrayLikeT | Number
            Positional arguments to evaluate the function unit.
        X : ArrayLikeT | None, default=None
            Placeholder keyword argument for the input data array, typically a 2D array-like
            structure where each row represents a data point and each column represents a variable.
        C : ArrayLikeT | Sequence[Number | None] | None, default=None
            Placeholder keyword argument for the 1D array of delayed constants. This is used to pass
            constants that are determined at fit time when fitting the function to data.
        **kwargs : Any
            Keyword arguments to evaluate the function unit.

        Returns
        -------
        ArrayLikeT | Number
            The result of evaluating the function unit.

        See Also
        --------
        evaluate : the base method for implementing the forward pass.
        __call__ : alias method for compatibility with PyTorch's `__call__` method.
        """
        return self.evaluate(*args, X=X, C=C, **kwargs)

    @final
    def __call__(
        self,
        *args: ArrayLikeT | Number,
        X: ArrayLikeT | None = None,
        C: ArrayLikeT | Sequence[Number | None] | None = None,
        **kwargs: Any,
    ) -> ArrayLikeT | Number:
        """
        Alias for the `forward` method to evaluate the function unit, for compatibility with
        PyTorch's `__call__` method.

        Evaluate the function unit with the given arguments.

        Parameters
        ----------
        *args : ArrayLikeT | Number
            Positional arguments to evaluate the function unit.
        X : ArrayLikeT | None, default=None
            Placeholder keyword argument for the input data array, typically a 2D array-like
            structure where each row represents a data point and each column represents a variable.
        C : ArrayLikeT | Sequence[Number | None] | None, default=None
            Placeholder keyword argument for the 1D array of delayed constants. This is used to pass
            constants that are determined at fit time when fitting the function to data.
        **kwargs : Any
            Keyword arguments to evaluate the function unit.

        Returns
        -------
        ArrayLikeT | Number
            The result of evaluating the function unit.

        See Also
        --------
        evaluate : the base method for implementing the forward pass.
        forward : the base method for implementing the forward pass for compatibility with
            PyTorch's `forward` method.
        """
        return self.forward(*args, X=X, C=C, **kwargs)

    @contextmanager
    def mutate(self) -> Generator[Self, None, None]:
        """
        Context manager to allow temporary mutation of the instance.
        """
        self._immutable_t = False
        try:
            yield self
        finally:
            # restore to class level default
            del self._immutable_t

    def copy(self, deep: bool = False) -> Self:
        """
        Create a copy of the function unit. By default, the copy of an immutable function unit is
        itself - duplicated instances for an immutable function unit is redundant. For a mutable
        function unit, a copy is created to allow independent modification.

        Parameters
        ----------
        deep : bool, default=False
            Whether to create a deep copy of the function unit. For a shallow copy, some attributes
            may be shared between the original and the copy.

        Returns
        -------
        Self
            A copy of the function unit.

        See Also
        --------
        reinit : method to reinitialize the function unit, no matter if it immutable or not.
        """
        if self.is_immutable or self.is_singleton:
            return self
        return self.reinit(deep=deep)

    @abstractmethod
    def reinit(self, deep: bool = False) -> Self:
        """
        Reinitialize the function unit and get a new non-singleton instance (new object identity),
        regardless of immutability. The new instance should have the same core attributes.

        Parameters
        ----------
        deep : bool, default=False
            Whether to create a deep copy of the function unit. For a shallow copy, some attributes
            may be shared between the original and the copy.

        Returns
        -------
        Self
            A new **non-singleton** instance of the function unit with the same core attributes.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def identify(cls, key: str | Number, /, *, init: bool = False) -> Self | None:
        """
        Class method to identify a function unit by a key or some identifier.

        Parameters
        ----------
        key :  str | Number
            The key or identifier to look up the function unit. This should typically be a string or
            a number (int or float). The Number type should specifically
            refer to `Constant` function units.
        init : bool, default=False
            Whether to initialize a new instance of the function unit if not found.

        Returns
        -------
        FuncUnit | None
            The identified function unit, or None if not found and init failed/not applied.
        """
        raise NotImplementedError

    @classmethod
    @final
    def integrated_identify(
        cls,
        key: str | Number,
        /,
        *,
        types: Iterable[type["FuncUnit[ArrayLikeT]"]] | None = None,
        custom_registry: dict[str | Number, "FuncUnit[ArrayLikeT]"] | None = None,
        init: bool = False,
    ) -> "FuncUnit[ArrayLikeT] | None":
        """
        Integrated identify method that checks the specified types to identify function units.

        Parameters
        ----------
        key : str | Number
            The key or identifier to look up the function unit. This should typically be a string or
            a number (int or float). The Number type should specifically refer to `Constant`
            function units.
        types : Iterable[type["FuncUnit[ArrayLikeT]"]] | None
            The types of function units to look up, in order. By default, the order will be:
            `Operation`, `Variable`, `Constant`, `DelayedConstant`. First match is returned.

            Automatic parsing of `types` may fail if the user does not provide the correct types
            explicitly and implemented custom subclasses. Define types explicitly to avoid issues.
        custom_registry : dict[str | Number, FuncUnit[ArrayLikeT]]
            A custom registry to look up function units. This allows for dynamic identification
            of function units that may not be present in the default registry.
        init : bool, default=False
            Whether to initialize a new instance of the function unit if not found. Same with
            `types`, the first initializable type will be used.

        Returns
        -------
        FuncUnit[ArrayLikeT] | None
            The identified function unit, or None if not found and init failed/not applied.
        """
        if (
            custom_registry is not None
            and (val := custom_registry.get(key)) is not None
        ):
            return val

        if types is None:
            subcls = cls.__subclasses__()
            types = subcls[0].__subclasses__() + subcls[1:]

        for subcls in types:
            if (result := subcls.identify(key, init=False)) is not None:
                return result

        if init is False:
            raise ValueError(
                f"Function unit '{key}' not found and initialization is disabled."
            )

        for subcls in types:
            if (result := subcls.identify(key, init=True)) is not None:
                return result

        raise ValueError(f"Function unit '{key}' not found and initialization failed.")

    def __copy__(self) -> Self:
        """
        Create a copy of the function unit.

        Returns
        -------
        Self
            A copy of the function unit.
        """
        return self.copy()

    def __deepcopy__(self) -> Self:
        """
        Create a deep copy of the function unit.

        Returns
        -------
        Self
            A deep copy of the function unit.
        """
        return self.copy(deep=True)

    def __bool__(self) -> Literal[True]:
        """
        Check if the function unit is truthy.

        Returns
        -------
        Literal[True]
            Always returns True for function units.
        """
        return True

    def __str__(self) -> str:
        """
        String representation of the function unit.
        """
        return self.name

    def __eq__(self, other: Any) -> bool:
        """
        Check if two function units are equal. By default, they are considered equal if they

        - have the same class type
        - have the same name
        - have the same arity

        Parameters
        ----------
        other : Any
            The other object to compare with.

        Returns
        -------
        bool
            True if the other object is a function unit and has the same name and arity, False
            otherwise.
        """
        if not isinstance(other, FuncUnit):
            return False
        if not isinstance(other, self.__class__):
            return False
        if self.name != other.name or self.arity != other.arity:
            return False
        return True

    @abstractmethod
    def __reduce__(self) -> str | tuple[Any, ...]:
        return super().__reduce__()


class SingletonFuncUnit(
    FuncUnit[ArrayLikeT],
    InstanceRegistry[HashableT],
    Generic[ArrayLikeT, HashableT],
    immutable=True,
):
    """
    A base class for singleton function units.

    This class is used to implement the singleton pattern for function units, ensuring that only
    one instance of a function unit with a given name exists. It provides a mechanism to create,
    retrieve, and delete instances of function units.

    Parameters
    ----------
    singleton : bool, default=True
        Whether to create a singleton instance of the function unit. When creating a singleton
        instance, it is stored in the class-level dictionary of instances. Otherwise, a new instance
        is created each time, which is not recommended in most cases.

    Properties
    ----------
    _instances : dict[Hashable, Self]
        A class-level dictionary that stores all instances of the function unit, keyed by their
        names or custom hashable keys. Do not open this dictionary directly; use the provided
        methods to interact with function unit instances.

        See :class:`psr.base.base.InstanceRegistry` for more information.
    key : Hashable
        The key/name of the function unit.
    immutable : bool
        Whether the function unit is immutable. By default, singleton function units are immutable
        after creation/initialization. This can be used to prevent accidental modification of the
        function unit after it has been created.
    """

    @abstractmethod
    def __new__(cls, *args: Any, singleton: bool = True, **kwargs: Any) -> Self:
        """
        Create a new instance of the function unit. This method is overridden in subclasses to
        implement the singleton pattern.
        """
        return super().__new__(cls)

    def to_singleton(self) -> Self:
        """
        Register a non-singleton instance of the function unit into the class-level
        dictionary to make it singleton.

        This method is a no-op for indexed function units, as they are not designed to be singletons.
        It is provided for compatibility with the `FuncUnit` interface.

        Returns
        -------
        Self
            The indexed function unit instance itself.
        """
        if not self.is_singleton:
            self.add_instance(self.key, self)
        return self

    @property
    def is_singleton(self) -> bool:
        """
        Check if the function unit is a singleton, i.e., is registered in the class-level dictionary
        of instances and is the only instance corresponding to its `key` among all singleton
        instances of the same class.


        Returns
        -------
        bool
            True if the function unit is a singleton, False otherwise.

        See Also
        --------
        copy : method to make a copy of the function unit. The copy of a singleton is itself.
        """
        return self.__class__.has_instance(self.key, self)


class IndexedFuncUnit(ABC):
    """
    A base class for indexed function units. Should be used with either `FuncUnit` or
    `IndexedFuncUnit` when subclassing.

    An example of indexed function units is variables. The input data X is expected to be a 2D array
    and each column represents a variable. The column index is used to identify the variable, and
    thus variables are indexed.

    For indexed function units, their name/string representation is typically formatted as
    `{prefix}{index}`. Indexed function units of the same class type share one prefix, and the index
    in the string is typically 1-based. For example, `X1, X2, ...` can be used to represent the
    first variable, the second variable, and so on.

    Indexed function units of different class types must have different prefixes to avoid confusion.

    Subclassing
    -----------
    When subclassing `IndexedFuncUnit`, you must provide the prefix either:

    - Use `SubClass(..., IndexedFuncUnit, prefix="your_prefix")`. *higher priority*
    - Define a class-level attribute `_prefix` with the desired prefix value in the subclass body.

    If both methods are used, subclass argument takes precedence. The prefix must be a valid python
    identifier and may not conflict with existing prefixes.

    Properties
    ----------
    _prefix : `str`, the prefix for the indexed function unit. This is used in the class body for
        initialization.
    _prefix_dict : `dict[str, Type["IndexedFuncUnit"]]`, a dictionary mapping prefix names to their
        corresponding class types. This is used to ensure that indexed function units of different
        class types have different prefixes.
    prefix : `str`, the prefix for the indexed function unit.
    set : class method to set/update the prefix for the indexed function unit.
    """

    _prefix: str
    _prefix_dict: dict[str, Type["IndexedFuncUnit"]] = {}

    def __init_subclass__(cls, prefix: str | None = None, **kwargs: Any) -> None:
        if not isinstance(prefix, str) and prefix is not None:
            raise ValueError("Invalid prefix argument. Must be a string.")

        _prefix = getattr(cls, "_prefix", None)
        if not isinstance(_prefix, str) and _prefix is not None:
            raise ValueError("Invalid _prefix class attribute. Must be a string.")

        prefix = prefix or _prefix
        if not prefix:
            raise ValueError(
                "Must provide either a prefix argument or a _prefix class attribute."
            )

        if not prefix.isidentifier() or prefix[-1].isdigit():
            raise ValueError(
                f"Invalid prefix: {prefix!r}. Must be a valid Python identifier "
                "and not end with a digit."
            )

        if (existing_cls := cls._prefix_dict.get(prefix)) is not None:
            if existing_cls is cls:
                return
            if not config.inplace_update_:
                raise ValueError(
                    f"Prefix {prefix!r} is used by another class ({existing_cls.__name__!r}). "
                    f"Claimed prefixes: {', '.join(cls.get_prefix_list())}."
                )

        cls._prefix = prefix
        cls._prefix_dict = IndexedFuncUnit._prefix_dict
        cls._prefix_dict[prefix] = cls
        super().__init_subclass__(**kwargs)

    @property
    def prefix(self) -> str:
        """
        Get the prefix name for the indexed function unit. Typically, the prefix is used to identify
        a specific type of function unit (e.g., variables, delayed constants), which can be
        formatted as `{prefix}{index}` (index is 1-based).

        The prefix is typically used in the class body for initialization for subclasses with
        `_prefix = <your_prefix>` or in the subclass attribute `prefix`.

        Returns
        -------
        str
            The prefix name for the indexed function unit.
        """
        return self.__class__._prefix

    @prefix.setter
    def prefix(self, value: str) -> NoReturn:
        """
        ## Property Setter
        Set the prefix name for the indexed function unit.

        **Illegal Operation**: The prefix of an indexed function unit cannot be changed from an
        instance. You must use the class method `set` instead.

        **Caution**: Changing the prefix will affect all instances of this class.

        Raises
        ------
        ValueError
            Always raised when trying to change the prefix from an instance.

        See Also
        --------
        set : the class method to set/update the prefix for the indexed function unit.
        """
        raise ValueError(
            "Cannot change the prefix of an indexed function unit from an instance. "
            "Use the class method `set` instead."
        )

    @classmethod
    def set(cls, *, prefix: str) -> None:
        """
        Set/update the prefix for the indexed function unit.

        **Caution**: Changing the prefix will affect all instances of this class.

        Parameters
        ----------
        prefix : str (keyword-only)
            The new prefix to set for the indexed function unit, which should

            1. Be a valid Python identifier.
            2. Not end with a digit.
            3. Not conflict with existing prefixes.

        Raises
        ------
        ValueError
            If the prefix is invalid or conflicts with existing prefixes.
        """
        prev_prefix = cls._prefix
        if prev_prefix == prefix:
            return

        if not prefix.isidentifier() or prefix[-1].isdigit():
            raise ValueError(
                f"Invalid prefix name: {prefix}. Must be a valid Python identifier "
                "and not end with a digit."
            )

        if cls._prefix_dict.setdefault(prefix, cls) is not cls:
            raise ValueError(
                f"Prefix name '{prefix}' has been claimed by another class."
            )

        cls._prefix_dict.pop(prev_prefix, None)
        cls._prefix = prefix

    @classmethod
    @overload
    def get(
        cls, *, prefix: str, default: Type["IndexedFuncUnit"]
    ) -> Type["IndexedFuncUnit"]: ...
    @classmethod
    @overload
    def get(cls, *, prefix: str, default: T = None) -> Type["IndexedFuncUnit"] | T: ...

    @classmethod
    def get(
        cls, *, prefix: str, default: Type["IndexedFuncUnit"] | T = None
    ) -> Type["IndexedFuncUnit"] | T:
        """
        Get the class type associated with a given prefix.

        Parameters
        ----------
        prefix : str (keyword-only)
            The prefix to look up.
        default : Type["IndexedFuncUnit"] | Any, optional (keyword-only)
            The default value to return if the prefix is not found.

        Returns
        -------
        Type["IndexedFuncUnit"] | T
            The class type associated with the given prefix, or the default value if not found.
        """
        return cls._prefix_dict.get(prefix, default)

    @classmethod
    def pop(cls, *, prefix: str, break_registry: bool = False) -> None:
        """
        Remove a prefix from the class-level dictionary of prefixes.

        **Danger**: The prefix of a class should **NOT** be removed from the registry once the class
        is created. Use `set` to change the prefix instead.

        Parameters
        ----------
        prefix : str (keyword-only)
            The prefix to remove.
        break_registry : bool, default=False (keyword-only)
            Whether to break the registry and allow the prefix to be removed.

            **Warning**: This operation can lead to inconsistencies if not handled carefully.

        Raises
        ------
        ValueError
            A ValueError is raised when

            - If `break_registry` is False - safety measure kicks in.
            - If the prefix is for another defined class. This can happen if the user used private
              methods/properties or `break_registry` was performed.
        """
        if not break_registry:
            raise ValueError(
                "The prefix is bound with a defined class and cannot be removed after class "
                "creation. Use `set` to change the prefix instead."
            )
        if cls._prefix_dict.get(prefix, None) is cls:
            del cls._prefix_dict[prefix]
        else:
            raise ValueError("Inconsistent registry state. Prefix mismatch.")

    @classmethod
    def get_prefix(cls) -> str:
        """
        Get the prefix for the indexed function unit.

        Returns
        -------
        str
            The prefix for the indexed function unit.
        """
        return cls._prefix

    @classmethod
    def get_prefix_list(cls) -> list[str]:
        """
        Get a list of all registered prefixes. Use the list to find new prefixes for new classes.

        Returns
        -------
        list[str]
            A list of all registered prefix names.
        """
        return list(cls._prefix_dict.keys())


class Operation(SingletonFuncUnit[ArrayLikeT, str], Generic[ArrayLikeT]):
    """
    Represents an operation in the symbolic regression tree.

    This class is used to encapsulate operations such as addition, subtraction, multiplication,
    division, etc. It can be subclassed to implement specific operations. An operation should take
    at least one argument and return a value of the same type as the input.

    Note that singleton mode is implemented for operations with the same name, so creating an
    operation with an existing name will return the existing instance and the input parameters
    will be ignored.
    """

    @property
    def key(self) -> str:
        """
        Alias for `name`. The `key` is used to identify the operation instance in the class-level
        instance regictry (`dict`).
        """
        return self.name

    def __new__(
        cls,
        name: str,
        /,
        arity: int | None = None,
        operation: (
            Callable[[*tuple[ArrayLikeT | Number, ...]], ArrayLikeT | Number] | None
        ) = None,
        formatter: Formatter | tuple[str, Sequence[bool], bool] | None = None,
        singleton: bool = True,
        no_warning: bool = False,
        weight: int | float = 1.0,
        cost: int | float = 1.0,
        *args: Any,
    ) -> Self:
        """
        Singleton mode implementation for operations with the same name.

        Returns
        -------
        Self
            The created or existing operation instance.
        """
        if not singleton or not config.allow_singleton_:
            return super().__new__(cls)

        if instance := cls.get_instance(name):
            if no_warning or config.multiprocessing_ or config.inplace_update_:
                pass
            elif (
                any(x is not None for x in [arity, operation, formatter])
                or weight != instance.weight
                or cost != instance.cost
            ):
                warnings.warn(
                    f"Operation '{name}' already exists. Returning existing instance. "
                    "The input parameters are ignored."
                )
            return instance

        instance = super().__new__(cls)
        cls.add_instance(name, instance, check_key_mismatch=False)
        return instance

    def __init__(
        self,
        name: str,
        /,
        arity: int | None = None,
        operation: (
            Callable[[*tuple[ArrayLikeT | Number, ...]], ArrayLikeT | Number] | None
        ) = None,
        formatter: Formatter | tuple[str, Sequence[bool], bool] | None = None,
        singleton: bool = True,
        no_warning: bool = False,
        weight: int | float = 1.0,
        cost: int | float = 1.0,
        *args: Any,
    ) -> None:
        """
        Initialize the operation with a callable that defines the operation's behavior. Note that
        singleton mode is implemented for operations with the same name, so creating an operation
        with an existing name will return the existing instance.

        Parameters
        ----------
        name : str
            The name of the operation. The name must be a valid Python identifier.
        arity : int | None
            The number of arguments the operation takes. This is used to validate the number of
            arguments passed to the operation during evaluation. This should be at least 1.

            Must be provided when initializing a new or non-singleton operation.
        operation : Callable[[*tuple[ArrayLikeT | Number, ...]], ArrayLikeT | Number] | None
            A callable that takes any number of arguments and returns a value of type T/int/float.
            For example, a callable that takes two arguments and returns their sum.

            - The callable must have `**kwargs` to allow for flexible argument passing.
            - The callable must be serializable using `pickle`, which means it cannot be a lambda
              function or a nested function. If you need to use a lambda function, you can serialize
              it using `dill` or `cloudpickle` to ensure it can be pickled and unpickled correctly.

            Must be provided when initializing a new or non-singleton operation.
        formatter : Formatter | tuple[str, Sequence[bool], bool] | None
            A template/formatter for the operation, used for formatting the mathematical expression
            that uses this operation.

            See the `Formatter` class in :class:`psr.base.formatter.Formatter` for more details. If
            a tuple is provided, it should contain:

            - `template: str`: The template string to use for formatting.
            - `protection_rules: Sequence[bool]`: The protection rules to apply to the formatted
              string.
            - `needs_protection: bool`: Whether the formatted string needs protection.

            Must be provided when initializing a new or non-singleton operation.
        singleton : bool, default=True
            Whether to create a singleton instance of the operation. If True, the operation will be
            stored in the class-level dictionary of instances. If False, a new instance will be
            created each time, which is not recommended in most cases.

            To suppress singleton mode while deserializing (loading a pickled :func:`Operation`
            instance), use the context manager :method:`psr.config.config.sandbox`. Otherwise, the
            load may fail due to `name` conflicts.
        no_warning : bool, default=False
            Whether to suppress warnings about existing operation with the same name, in which case,
            the input parameter may be ignored.
        weight : int | float, default=1.0
            The weight of the operation in all `Operation` instances. This is used for randomization
            purposes in the genetic programming process for symbolic regression.  Should be
            non-negative.
        cost : int | float, default=1.0
            The cost/complexity of the operation. This is used to penalize more complex operations
            during the genetic programming process. Should be a positive value.
        *args : Any, **not used**
            Additional positional arguments to pass to the constructor. This is added for better
            serialization/deserialization support between different package versions.

        Raises
        ------
        RuntimeError
            - If the instance could not be created.
        ValueError

            - If the name is not a valid Python identifier.
            - If the operation is not callable.
            - If the operation does not have at least `arity` arguments.
            - If the operation is not serializable using `pickle`.
        """
        if hasattr(self, "_name") and not config.inplace_update_:
            # the instance was initialized before and inplace update is requested
            return

        if arity is None:
            raise ValueError("`arity` must be provided")
        if operation is None:
            raise ValueError("`operation` must be provided")
        if formatter is None:
            raise ValueError("`formatter` must be provided")

        try:
            self.name = name
            self.arity = arity
            self.operation = operation

            if isinstance(formatter, tuple):
                formatter = Formatter(*formatter)
            self.formatter = formatter
            self.weight = weight
            self.cost = cost
        except Exception as e:
            self.__class__.remove_instance(self.key, self, error="ignore")
            raise e

    @property
    def name(self) -> str:
        """
        Get the name of the operation.

        Returns
        -------
        str
            The name of the operation, which is typically a valid Python identifier.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        ## Property Setter
        Set the name of the operation. Typically, name should only be set during initialization.

        Parameters
        ----------
        new_name : str
            The name of the operation, which must be a valid Python identifier and not end with a
            digit.

        Raises
        ------
        ValueError

            - If the instance is immutable.
            - If the value is not a valid Python identifier.
            - If the value ends with a digit.
            - If there is a conflict with an existing instance.
        """
        if self.is_immutable and hasattr(self, "_name") and not config.inplace_update_:
            raise self._mutation_error

        if not new_name.isidentifier() or new_name[-1].isdigit():
            raise ValueError(
                f"Invalid {self.__class__.__name__} name: {new_name}. "
                "Must be a valid Python identifier and not end with a digit."
            )

        if not hasattr(self, "_name"):
            # still initializing the instance
            self._name = new_name
            return

        if not self.is_singleton:
            # the instance is not registered - keep unregistered
            self._name = new_name
            return

        self.__class__.rename_instance(self._name, new_name)
        self._name = new_name

    @property
    def arity(self) -> int:
        """
        Get the arity (number of arguments) of the operation.

        Returns
        -------
        int
            The arity of the operation.
        """
        return self._arity

    @arity.setter
    def arity(self, new_arity: int) -> None:
        """
        ## Property Setter
        Set the arity (number of arguments) of the operation.

        Parameters
        ----------
        new_arity : int
            The new arity of the operation. This must be a positive integer.

        Raises
        ------
        ValueError
            If the new arity is not a positive integer.
        """
        if new_arity <= 0:
            raise ValueError(
                f"Invalid {self.__class__.__name__} arity: {new_arity}. "
                "Must be a positive integer."
            )

        self._arity = new_arity

    @property
    def operation(
        self,
    ) -> Callable[[*tuple[ArrayLikeT | Number, ...]], ArrayLikeT | Number]:
        """
        Get the operation callable.

        Returns
        -------
        Callable[[*tuple[ArrayLikeT | Number, ...]], ArrayLikeT | Number]
            The callable that defines the operation's behavior.
        """
        return self._operation

    @operation.setter
    def operation(
        self, value: Callable[[*tuple[ArrayLikeT | Number, ...]], ArrayLikeT | Number]
    ) -> None:
        """
        ## Property Setter
        Set the operation callable.

        Parameters
        ----------
        value : Callable[[*tuple[ArrayLikeT | Number, ...]], ArrayLikeT | Number]
            The callable that defines the operation's behavior. This must be a serializable callable
            that can be pickled and unpickled.

        Raises
        ------
        ValueError

            - If the value is not callable.
            - If the value does not have at least `arity` arguments.
            - If the value does not have a valid Python identifier name.
            - If the value is not serializable using `pickle`.
        """
        if (
            self.is_immutable
            and hasattr(self, "_operation")
            and not config.inplace_update_
        ):
            raise self._mutation_error

        if not callable(value):
            raise ValueError(
                f"Invalid {self.__class__.__name__} operation: {value}. Must be a callable."
            )

        # Inspect the function's signature
        signature = inspect.signature(value)
        parameters = signature.parameters.values()
        has_varargs = any(
            param.kind == inspect.Parameter.VAR_POSITIONAL for param in parameters
        )

        if not hasattr(value, "__code__") or (
            value.__code__.co_argcount < self.arity and not has_varargs
        ):
            raise ValueError(
                f"Invalid {self.__class__.__name__} operation: {value}. "
                f"Must take at least {self.arity} arguments."
            )

        if not hasattr(value, "__name__") or not value.__name__.isidentifier():
            raise ValueError(
                f"Invalid {self.__class__.__name__} operation: {value}. "
                "Must be a valid Python identifier."
            )

        # check if the callable is serializable
        try:
            pickle.dumps(value)
        except pickle.PicklingError:
            raise ValueError(
                f"Invalid {self.__class__.__name__} operation: {value}. "
                "Must be a serializable callable."
            )

        self._operation = value

    @property
    def protection_rules(self) -> Sequence[bool]:
        """
        Get the protection rules for the operation's formatter. For example, if the formatter /
        template is `{0} + exp({1})`, the protection rules will be `[True, False]`, indicating
        that the first argument (the left-hand side of the `+` operation) needs to be protected
        with parentheses, while the second argument (the right-hand side of the `+` operation) does
        not.

        Returns
        -------
        Sequence[bool]
            A sequence of boolean values representing the protection rules for the operation.
            These rules are used to determine whether the operation needs to be protected with
            parentheses when formatting the expression.
        """
        return self.formatter.protection_rules

    def evaluate(
        self, *args: ArrayLikeT | Number, X: Any = None, C: Any = None, **kwargs: Any
    ) -> ArrayLikeT | Number:
        """
        Evaluate the operation with the given arguments.

        Parameters
        ----------
        *args : ArrayLikeT | Number
            Positional arguments to evaluate the operation.
        X : Any, default=None
            Placeholder keyword argument for the input data array, typically a 2D array-like
            structure where each row represents a data point and each column represents a variable.
            **NOT USED**
        C : Any, default=None
            Placeholder keyword argument for the array of delayed constants, typically a 1D
            array-like structure where each element represents a delayed constant. **NOT USED**
        **kwargs : Any
            Keyword arguments to evaluate the operation.

        Returns
        -------
        ArrayLikeT | Number
            The result of evaluating the operation.
        """
        return self.operation(*args, **kwargs)

    def format(self, *args: str, protect: bool = False, **kwargs: Any) -> str:
        """
        Format the operation into a string representation for the entire expression.

        Parameters
        ----------
        *args : str
            String representations of the arguments to be formatted into the operation's template.
            For example, if the operation is `+` and the arguments are `x` and `y`, the returned
            string representation should be formatted as `x + y` with the template `{0} + {1}`.
        protect : bool, default=False
            Whether the returned string should be protected with parentheses, if necessary.
        **kwargs : Any
            Additional keyword arguments to customize the formatting behavior. Not used here.

        Returns
        -------
        str
            The formatted string representation of the operation.
        """
        s = self.formatter.template.format(*args)
        if protect and self.formatter.needs_protection:
            return f"({s})"
        return s

    def reinit(self, deep: bool = False) -> Self:
        """
        Reinitialize the operation and get a new non-singleton instance (new object identity),
        regardless of immutability. The new instance should have the same core attributes.

        Parameters
        ----------
        deep : bool, default=False
            Whether to create a deep copy of the operation. For a shallow copy, some attributes may
            be shared between the original and the copy, e.g., the `operation` and `formatter`.

        Returns
        -------
        Self
            A new **non-singleton** instance of the operation with the same core attributes.
        """
        return self.__class__(
            self.name,
            arity=self.arity,
            operation=self.operation if not deep else deepcopy(self.operation),
            formatter=self.formatter if not deep else self.formatter.copy(),
            singleton=False,
            weight=self.weight,
        )

    @classmethod
    @overload
    def identify(cls, key: Number, /, *, init: bool = False) -> None: ...
    @classmethod
    @overload
    def identify(cls, key: str, /, *, init: bool = False) -> Self | None: ...

    @classmethod
    def identify(cls, key: str | Number, /, *, init: bool = False) -> Self | None:
        """
        Identify an operation by its key/identifier.

        Parameters
        ----------
        key : str | Number
            The key/identifier of the operation to identify. This should be the `name` attribute
            of a registered operation.
        init : bool, default=False
            Whether to initialize the operation if it is not found. **NOT USED**. An operation
            cannot be initialized with a name.

        Returns
        -------
        Self | None
            The identified operation, or None if not found and init failed/not applied.
        """
        if not isinstance(key, str):
            return None

        key = key.strip()
        if not key.isidentifier():
            return None
        return cls.get_instance(key)

    def __repr__(self) -> str:
        """
        Return a string representation of the operation.

        Returns
        -------
        str
            A string representation of the operation.
        """
        return (
            f"Operation({self.name}, arity={self.arity}, singleton="
            f"{self.is_singleton}, weight={self.weight})"
        )

    def __eq__(self, other: object) -> bool:
        """
        Check if two operations are equal. Two operations are only equal if they have

        - (are of the same type)
        - the same arity
        - the same operation
        - the same formatter

        Parameters
        ----------
        other : object
            The other object to compare against.

        Returns
        -------
        bool
            True if the operations are equal, False otherwise.
        """
        if self is other:
            return True
        if (
            not isinstance(other, self.__class__)
            or self.arity != other.arity
            or self.operation != other.operation
            or self.formatter != other.formatter
        ):
            return False
        return True

    def __reduce__(
        self,
    ) -> (
        tuple[type[Self], tuple[Any, ...]]
        | tuple[type[Self], tuple[Any, ...], dict[str, Any]]
    ):
        """
        Serialize the :class:`Operation` instance for pickling. When in subprocess mode, make sure
        to initialize the function units in the main process first and use singleton mode for
        :class:`Operation`'s - this will save time and memory.

        Returns
        -------
        tuple[type[Self], tuple[Any, ...]] | tuple[type[Self], tuple[Any, ...], dict[str, Any]]
            A tuple containing the class type and the constructor arguments (and any additional
            state).
        """
        if (sgl := self.is_singleton) and config._multiprocessing:
            return (self.__class__, (self._name,))

        return (
            self.__class__,
            (
                self._name,
                self._arity,
                self._operation,
                self.formatter.to_tuple(),
                sgl,
            ),
            {"_weight": self._weight, "_cost": self._cost},
        )


class Variable(
    SingletonFuncUnit[ArrayLikeT, int], IndexedFuncUnit, Generic[ArrayLikeT], prefix="X"
):
    """
    Represents a variable in the symbolic regression tree.

    This class is used to encapsulate variables that can be used in mathematical expressions.
    Variables are typically used to represent input data or parameters in the symbolic regression
    process.

    In the implementation, the input data should be a 2D array-like structure where each row
    represents a data point and each column represents a variable. The variable's index in the
    array is used to reference the specific variable during evaluation.

    Note that singleton mode is used for variables with the same name, so creating a duplicate
    variable with the same variable index will return the existing instance.
    """

    @property
    def key(self) -> int:
        """
        Alias for `index`. The `key` is used to identify the variable instance in the class-level
        instance regictry (`dict`).
        """
        return self.index

    def __new__(
        cls,
        index: int,
        /,
        prefix: str | None = None,
        name: str | None = None,
        singleton: bool = True,
        no_warning: bool = False,
        weight: int | float = 1.0,
        cost: int | float = 1.0,
        *args: Any,
    ) -> Self:
        """
        Singleton mode implementation for variables with the same index

        Returns
        -------
        Self
            The created or existing variable instance.
        """
        if not singleton or not config.allow_singleton_:
            return super().__new__(cls)

        if instance := cls.get_instance(index):
            if no_warning or config.multiprocessing_ or config.inplace_update_:
                pass
            elif (
                any(x is not None for x in [prefix, name])
                or weight != instance.weight
                or cost != instance.cost
            ):
                warnings.warn(
                    f"Variable with index '{index}' already exists. Returning existing instance. "
                    "The input parameters are ignored."
                )
            return instance

        instance = super().__new__(cls)
        cls.add_instance(index, instance, check_key_mismatch=False)
        return instance

    def __init__(
        self,
        index: int,
        /,
        prefix: str | None = None,
        name: str | None = None,
        singleton: bool = True,
        no_warning: bool = False,
        weight: int | float = 1.0,
        cost: int | float = 1.0,
        *args: Any,
    ) -> None:
        """
        Initialize the variable with its index.

        Parameters
        ----------
        index : int
            The index of the variable in the input data array.
        prefix : str | None
            The **prefix** name of variables. All variables share the same prefix. A variable will
            have a name formatted as "{prefix}{index+1}" where `{index}` is the variable's `index`,
            unless a specified `name` is provided.

            - If None, the default prefix will be used with no update (original default is `X`).
            - If string, the prefix must be a valid Python identifier, preferably just a single
              uppercase letter. This will change the default prefix for **all** variables, including
              those created in the past and future.

        name : str | None
            The name of the variable. If None, a default name using the prefix will be generated.
            The name must be a valid Python identifier, if provided.

            **Note**: For custom variable names, you need to make sure that different variables are
            not created with the same name. Otherwise, this could cause ambiguity in an expression.
        singleton : bool, default=True
            Whether to enable singleton mode for the variable. If True, the variable will be stored
            in the class-level dictionary of instances. If False, a new instance will be created
            each time the variable is instantiated, which is not recommended in most cases.

            To suppress singleton mode while deserializing (loading a pickled :func:`Operation`
            instance), use the context manager :method:`psr.config.config.sandbox`. Otherwise, the
            load may fail due to `index` conflicts.
        no_warning : bool, default=False
            Whether to suppress warnings about existing variable with the same index, in which case,
            the input parameter may be ignored.
        weight : int | float, default=1.0
            The weight of the variable in all `Variable` instances. This is used for randomization
            purposes in the genetic programming process for symbolic regression.  Should be
            non-negative.
        cost : int | float, default=1.0
            The cost of the variable in all `Variable` instances. This is used for regularization
            in the genetic programming process for symbolic regression. Should be non-negative.
        *args : Any, **not used**
            Additional positional arguments to pass to the constructor. This is added for better
            serialization/deserialization support between different package versions.
        """
        if hasattr(self, "_index") and not config.inplace_update_:
            # the instance was initialized before and inplace update is requested
            return

        try:
            self.index = index
            if prefix is not None:
                self.set(prefix=prefix)
            self.name = name
            self.weight = weight
            self.cost = cost
        except Exception as e:
            self.__class__.remove_instance(self.key, self, error="ignore")
            raise e

    @property
    def index(self) -> int:
        """
        Get the index of the variable in the input data array.

        Returns
        -------
        int
            The index of the variable in the input data array.
        """
        return self._index

    @index.setter
    def index(self, value: int) -> None:
        """
        ## Property Setter
        Set the index of the variable in the input data array.

        Parameters
        ----------
        value : int
            The index of the variable in the input data array. This must be a non-negative integer.

        Raises
        ------
        ValueError

            - If the variable is immutable.
            - If the value is not a non-negative integer.
        """
        if self.is_immutable and hasattr(self, "_index") and not config.inplace_update_:
            raise self._mutation_error

        if value < 0:
            raise ValueError(
                f"Invalid {self.__class__.__name__} variable index: {value}. "
                "Index must be a non-negative integer."
            )

        if not hasattr(self, "_index"):
            # still initializing the instance
            self._index = value
            return

        if not self.is_singleton:
            # the instance is not registered - keep unregistered
            self._index = value
            return

        self.__class__.rename_instance(self._index, value)
        self._index = value

    @property
    def name(self) -> str:
        """
        Get the name of the variable.

        Returns
        -------
        str
            The name of the variable, which is typically a valid Python identifier.
        """
        return self._name or f"{self.prefix}{self.index+1:d}"

    @name.setter
    def name(self, new_name: str | None) -> None:
        """
        ## Property Setter
        Set the name of the variable.

        Parameters
        ----------
        new_name : str | None
            The new name of the variable. If None, the name will be set to the default (evaluated
            at runtime). If string, the name must be a valid Python identifier and not end with a
            digit.

        Raises
        ------
        ValueError

            - If the new name is not a valid Python identifier.
            - If the new name ends with a digit.
        """
        if new_name is None:
            self._name = new_name
            return

        if not new_name.isidentifier() or new_name[-1].isdigit():
            raise ValueError(
                f"Invalid {self.__class__.__name__} function unit name: {new_name}. "
                f"Must be a valid Python identifier and not end with a digit."
            )
        self._name = new_name

    @property
    def arity(self) -> int:
        """
        Get the arity of the variable, which is always 0.

        Returns
        -------
        int
            The arity of the variable, which is always 0 since a variable is not an operation and it
            does not process any arguments.
        """
        return 0

    @arity.setter
    def arity(self, new_arity: int) -> NoReturn:
        """
        ## Property Setter
        Not allowed: variables should always have an arity of 0.

        Raises
        ------
        ValueError
            Always raises a ValueError since the arity of a variable cannot be changed.
        """
        raise ValueError("Arity of a variable cannot be changed.")

    def evaluate(
        self, *args: Any, X: ArrayLikeT | None = None, C: Any = None, **kwargs: Any
    ) -> ArrayLikeT | Number:
        """
        Evaluate the variable with the given arguments.

        Parameters
        ----------
        *args : Any
            Positional arguments to evaluate the variable. **NOT USED**
        X : ArrayLikeT | None, default=None
            Keyword argument for the input data array, typically a 2D array-like structure where
            each row represents a data point and each column represents a variable.
        C : Any, default=None
            Placeholder keyword argument for the array of delayed constants, typically a 1D
            array-like structure where each element represents a delayed constant. **NOT USED**
        **kwargs : Any
            Keyword arguments to evaluate the variable.

        Returns
        -------
        ArrayLikeT | Number
            The result of evaluating the variable.
        """
        if X is None:
            raise ValueError("Input data array X must be provided.")
        return X[:, self.index]

    def format(self, *args: str, protect: bool = False, **kwargs: Any) -> str:
        """
        Format the variable into a string representation for the entire expression.

        Parameters
        ----------
        *args : str
            String representations of the arguments to be formatted into the variable's template.
            For variables, this should be empty/omitted.
        protect : bool, default=False
            Whether the returned string should be protected with parentheses, if necessary.

            A variable name is typically already protected, so this parameter should not
            take effect for variables.
        **kwargs : Any
            Additional keyword arguments to customize the formatting behavior. Not used here.

        Returns
        -------
        str
            The string representation of the variable. If the default format `X{index}` is used,
            the index will be 1-indexed in the string representation.
        """
        return self.name

    def reinit(self, deep: bool = False) -> Self:
        """
        Reinitialize the variable and get a new non-singleton instance (new object identity),
        regardless of immutability. The new instance should have the same core attributes.

        Parameters
        ----------
        deep : bool, default=False
            Whether to create a deep copy of the variable. This parameter is ignored since the new
            copy should always be a deep copy.

        Returns
        -------
        Self
            A new **non-singleton** instance of the variable with the same core attributes.
        """
        return self.__class__(
            self.index, name=self._name, singleton=False, weight=self.weight
        )

    @classmethod
    @overload
    def identify(cls, key: Number, /, *, init: bool = False) -> None: ...
    @classmethod
    @overload
    def identify(cls, key: str, /, *, init: bool = False) -> Self | None: ...

    @classmethod
    def identify(cls, key: str | Number, /, *, init: bool = False) -> Self | None:
        """
        Identify a variable by its key.

        Parameters
        ----------
        key : str | Number
            The key to identify the variable.
        init : bool, default=False
            Whether to initialize the variable if not found.

        Returns
        -------
        Self | None
            The identified variable, or None if not found and initialization failed/not applied.
        """
        if not isinstance(key, str):
            return None

        key = key.strip()
        if not key.isidentifier():
            return None

        num = re.match(f"^{cls.get_prefix()}([1-9]\\d*)$", key)
        if num:
            index = int(num.group(1)) - 1
            if init:
                return cls(index)  # singleton mode
            return cls.get_instance(index)

        # pattern mismatch -> must match custom name
        for instance in cls._instances.values():
            if not isinstance(instance, cls):
                continue
            if instance._name == key:
                return instance

        return None

    def __repr__(self) -> str:
        """
        Return a string representation of the variable.

        Returns
        -------
        str
            A string representation of the variable.
        """
        return (
            f"Variable({self.index}, name={self.name}, singleton"
            f"={self.is_singleton}, weight={self.weight})"
        )

    def __eq__(self, other: object) -> bool:
        """
        Check if two variables are equal. Two variables are only equal if they are of the same type
        and have the same index.

        Parameters
        ----------
        other : object
            The other object to compare against.

        Returns
        -------
        bool
            True if the variables are equal, False otherwise.
        """
        if isinstance(other, Variable) and self.index == other.index:
            return True
        return False

    def __reduce__(
        self,
    ) -> (
        tuple[type[Self], tuple[Any, ...]]
        | tuple[type[Self], tuple[Any, ...], dict[str, Any]]
    ):
        """
        Serialize the :class:`Variable` instance for pickling. When in subprocess mode, make sure to
        initialize the function units in the main process first and use singleton mode for
        :class:`Variable`'s - this will save time and memory.

        Returns
        -------
        tuple[type[Self], tuple[Any, ...]] | tuple[type[Self], tuple[Any, ...], dict[str, Any]]
            A tuple containing the class type, the constructor arguments (and the state dictionary).
        """
        if (sgl := self.is_singleton) and config._multiprocessing:
            return (self.__class__, (self._index,))
        return (
            self.__class__,
            (self._index, self._prefix, self._name, sgl),
            {"_weight": self._weight, "_cost": self._cost},
        )


class Constant(SingletonFuncUnit[ArrayLikeT, Number], Generic[ArrayLikeT]):
    """
    A class representing a constant value in a mathematical expression. A constant value is a fixed
    value (number) that does not change. Example: `3.14`, `2.718`, etc.

    Note that constant values are singletons, meaning that there is only one instance of a constant
    for each unique value. The value itself must be hashable and immutable to be used as keys
    in a dictionary.
    """

    @property
    def key(self) -> Number:
        """
        Alias for `value`. The `key` is used to identify the constant instance in the class-level
        instance regictry (`dict`).
        """
        return self._value

    def __new__(
        cls,
        value: Number,
        /,
        name: str | None = None,
        needs_protection: bool = False,
        singleton: bool = True,
        no_warning: bool = False,
        weight: int | float = 1.0,
        cost: int | float = 1.0,
        *args: Any,
    ) -> Self:
        """
        singleton mode implementation for constants with the same **value**

        Returns
        -------
        Self
            The created or existing constant instance.
        """
        if not singleton or not config.allow_singleton_:
            return super().__new__(cls)

        if instance := cls.get_instance(value):
            if no_warning or config.multiprocessing_ or config.inplace_update_:
                pass
            elif (
                name is not None
                or needs_protection != instance.needs_protection
                or weight != instance.weight
                or cost != instance.cost
            ):
                warnings.warn(
                    f"Constant with value {value} already exists. Returning existing instance. "
                    "The input parameters are ignored."
                )
            return instance

        instance = super().__new__(cls)
        cls.add_instance(value, instance, check_key_mismatch=False)
        return instance

    def __init__(
        self,
        value: Number,
        /,
        name: str | None = None,
        needs_protection: bool = False,
        singleton: bool = True,
        no_warning: bool = False,
        weight: int | float = 1.0,
        cost: int | float = 1.0,
        *args: Any,
    ) -> None:
        """
        Initialize the constant with its value.

        Parameters
        ----------
        value : Number
            The value of the constant. Must be hashable. Compatible types include `int` and `float`.
            The value must be finite.
        name : str | None, default=None
            The string representation of the constant's name. If None, the name will be set to the
            string representation of the constant's `value`. The name is not required to be a valid
            Python identifier.
        needs_protection : bool, default=False
            Whether the constant value needs to be protected with parentheses when formatted. For
            example, if the `name` is a mathematical expression `1 + e`, it should be protected with
            parentheses to ensure correct evaluation order.
        singleton : bool, default=True
            Whether to enable singleton mode for the constant. If True, the constant will be stored
            in the class-level dictionary of instances. If False, a new instance will be created
            each time the constant is instantiated, which is not recommended in most cases.

            To suppress singleton mode while deserializing (loading a pickled :func:`Operation`
            instance), use the context manager :method:`psr.config.config.sandbox`. Otherwise, the
            load may fail due to `value` conflicts.
        no_warning : bool, default=False
            Whether to suppress warnings about existing constant with the same value, in which case,
            the input parameter may be ignored.
        weight : int | float, default=1.0
            The weight of the constant in all `Constant` instances. This is used for randomization
            purposes in the genetic programming process for symbolic regression. Should be
            non-negative.
        cost : int | float, default=1.0
            The cost of the constant in all `Constant` instances. This is used for regularization
            in the genetic programming process for symbolic regression. Should be non-negative.
        *args : Any, **not used**
            Additional positional arguments to pass to the constructor. This is added for better
            serialization/deserialization support between different package versions.
        """
        if hasattr(self, "_value") and not config.inplace_update_:
            # the instance was initialized before and inplace update is requested
            return

        try:
            self.value = value
            self.name = name
            self.needs_protection = needs_protection
            self.weight = weight
            self.cost = cost
        except Exception as e:
            self.__class__.remove_instance(self.key, self, error="ignore")
            raise e

    @property
    def name(self) -> str:
        """
        Get the name of the constant.

        Returns
        -------
        str
            The string representation of the constant's value.
        """
        return self._name or str(self.value)

    @name.setter
    def name(self, new_name: str | None) -> None:
        """
        ## Property Setter
        Set the name of the constant.

        Parameters
        ----------
        new_name : str | None
            The string representation of the constant's name. If None, the name will be set to
            the string representation of the constant's value. The name is not required to be a
            valid Python identifier, and any leading/trailing whitespace will be stripped.
        """
        self._name = None if new_name is None else new_name.strip()

    @property
    def identity(self) -> Number:
        """
        The identity of a constant that can be used to track back to the object. This identity is
        the same as the constant's value.

        See Also
        --------
        identify : method to retrieve the corresponding constant object using an identity.
        """
        return self.value

    @property
    def value(self) -> Number:
        """
        Get the value of the constant.

        Returns
        -------
        Number
            The value of the constant.
        """
        return self._value

    @value.setter
    def value(self, new_value: Number) -> None:
        """
        ## Property Setter
        Set the value of the constant.

        Parameters
        ----------
        new_value : Number
            The value of the constant. This must be a valid number (int or float). Complex numbers
            are not supported yet. The number must be finite.

        Raises
        ------
        ValueError

            - If the instance is immutable.
            - If there is a conflict with an existing constant.
        """
        if self.is_immutable and hasattr(self, "_value") and not config.inplace_update_:
            raise self._mutation_error

        # check if the value is finite
        if not np.isfinite(new_value):
            raise ValueError("Constant value must be finite.")

        if not hasattr(self, "_value"):
            # still initializing the instance
            self._value = new_value
            return

        if self.is_singleton:
            # the instance is not registered - keep unregistered
            self._value = new_value
            return

        self.__class__.rename_instance(self._value, new_value)
        self._value = new_value

    @property
    def arity(self) -> int:
        """
        Get the arity of the constant, which is always 0.

        Returns
        -------
        int
            The arity of the constant, which is always 0 since a constant does not take any
            arguments.
        """
        return 0

    @arity.setter
    def arity(self, new_arity: int) -> NoReturn:
        """
        ## Property Setter
        Not allowed: constants should always have an arity of 0.

        Raises
        ------
        ValueError
            Always raises a ValueError since the arity of a constant cannot be changed.
        """
        raise ValueError("Arity of a constant cannot be changed.")

    @property
    def needs_protection(self) -> bool:
        """
        Check if the `name` of the constant needs protection when formatting the expression. The
        default `name` compiled from `value` should not need protection. Custom names may need
        protection with brackets.

        Returns
        -------
        bool
            Whether the constant needs protection when formatting the expression.
        """
        return self._needs_protection

    @needs_protection.setter
    def needs_protection(self, value: bool) -> None:
        """
        ## Property Setter
        Set the protection status of the constant.

        Parameters
        ----------
        value : bool
            Whether the constant needs protection when formatting the expression.
        """
        self._needs_protection = value

    def evaluate(
        self, *args: Any, X: Any = None, C: Any = None, **kwargs: Any
    ) -> Number:
        """
        Evaluate the constant with the given arguments.

        Parameters
        ----------
        *args : ArrayLikeT | Number
            Positional arguments to evaluate the constant. Ignored since a constant does not depend
            on any arguments. **NOT USED**
        X : Any, default=None
            Placeholder keyword argument for the input data array. **NOT USED**
        C : Any, default=None
            Placeholder keyword argument for the array of constants. **NOT USED**
        **kwargs : Any
            Keyword arguments to evaluate the constant. **NOT USED**

        Returns
        -------
        Number
            The value of the constant.
        """
        return self.value

    def format(self, *args: str, protect: bool = False, **kwargs: Any) -> str:
        """
        Format the constant into a string representation for the entire expression.

        Parameters
        ----------
        *args : str
            String representations of the arguments to be formatted into the constant's template.
            For constants, this should be empty/omitted.
        protect : bool, default=False
            Whether the returned string should be protected with parentheses, if necessary.

            A constant value is typically already protected, so this parameter should not take
            effect for constants.
        **kwargs : Any
            Additional keyword arguments to customize the formatting behavior. Not used here.

        Returns
        -------
        str
            The string representation of the constant.
        """
        if protect and self.needs_protection:
            return f"({self.name})"
        return self.name

    def reinit(self, deep: bool = False) -> Self:
        """
        Reinitialize the constant and get a new non-singleton instance (new object identity),
        regardless of immutability. The new instance should have the same core attributes.

        Parameters
        ----------
        deep : bool, default=False
            Whether to create a deep copy of the constant. This parameter is ignored since the new
            copy should always be a deep copy.

        Returns
        -------
        Self
            A new **non-singleton** instance of the constant with the same core attributes.
        """
        return self.__class__(
            self.value,
            name=self._name,
            needs_protection=self.needs_protection,
            singleton=False,
            weight=self.weight,
        )

    @classmethod
    @overload
    def identify(cls, key: Number, /, *, init: Literal[True]) -> Self: ...
    @classmethod
    @overload
    def identify(
        cls, key: Number, /, *, init: Literal[False] = False
    ) -> Self | None: ...
    @classmethod
    @overload
    def identify(cls, key: str, /, *, init: bool = False) -> Self | None: ...

    @classmethod
    def identify(cls, key: str | Number, /, *, init: bool = False) -> Self | None:
        """
        Identify a constant by its key.

        Parameters
        ----------
        key : str | Number
            The key to identify the constant.
        init : bool, default=False
            Whether to initialize the constant if not found.

        Returns
        -------
        Self | None
            The identified constant, or None if not found and initialization failed/not applied.
        """
        if isinstance(key, Number):
            if init:
                return cls(key)  # singleton mode
            return cls.get_instance(key)

        # for a string, check if there is an exact match
        for instance in cls._instances.values():
            if instance._name == key:
                return instance

        if not init:
            return None

        try:
            return cls(float(key))
        except ValueError:
            return None

    def __repr__(self) -> str:
        """
        Return a string representation of the constant.

        Returns
        -------
        str
            A string representation of the constant.
        """
        return (
            f"Constant({self.value}, name={self._name}, needs_protection="
            f"{self.needs_protection}, singleton={self.is_singleton}, weight={self.weight})"
        )

    def __eq__(self, other: object) -> bool:
        """
        Check if two constants are equal. Two constants are only equal if they are of the same type
        and have the same value.

        Parameters
        ----------
        other : object
            The other object to compare against.

        Returns
        -------
        bool
            True if the constants are equal, False otherwise.
        """
        if isinstance(other, Constant) and self.value == other.value:
            return True
        return False

    def __reduce__(
        self,
    ) -> (
        tuple[type[Self], tuple[Any, ...]]
        | tuple[type[Self], tuple[Any, ...], dict[str, Any]]
    ):
        """
        Serialize the :class:`Constant` instance for pickling. When in subprocess mode, make sure to
        initialize the function units in the main process first and use singleton mode for
        :class:`Constant`'s - this will save time and memory.

        Returns
        -------
        tuple[type[Self], tuple[Any, ...]] | tuple[type[Self], tuple[Any, ...], dict[str, Any]]
            A tuple containing the class type, the constructor arguments (and the state dictionary).
        """
        if (sgl := self.is_singleton) and config._multiprocessing:
            return (self.__class__, (self._value,))
        return (
            self.__class__,
            (self._value, self._name, self._needs_protection, self._weight, sgl),
            {"_weight": self._weight, "_cost": self._cost},
        )


class DelayedConstant(
    FuncUnit[ArrayLikeT], IndexedFuncUnit, Generic[ArrayLikeT], immutable=False
):
    """
    Represents a delayed constant in the symbolic regression tree.

    A delayed constant is a constant value that is determined at fit time when fitting the function
    to data. It is used to represent constants that are not known until the fitting process occurs.

    In the implementation, to evaluate an expression containing a delayed constant, the input data
    must also include an array of delayed constants (e.g., guess values) subject to optimization.
    The value of the delayed constant is resolved with the provided values from the array and the
    index of the delayed constant in the array. The index of an delayed constant is dynamically
    updated prior to the evaluation of the expression, and the union of the indices of all delayed
    constants in an expression should be [0, 1, ..., n-1], where n is the number of delayed
    constants.

    Each delayed constant should be a unique instance. Do not attempt to share delayed constants
    within the same expression tree or different expression trees. **Always use the `copy` method
    to create a new instance of a delayed constant.**

    A delayed constant has an `initial_guess` and `bounds` defined at the class level. They are
    defined for the purpose of optimization during the fitting process. To use different guesses or
    bounds, you must make a subclass of `DelayedConstant` and define them per class. Check the
    examples and parameters for more details. (You can directly use `DelayedConstant` with the
    defaults, as well.)

    **See the subclassing parameters and examples below.**

    Parameters
    ----------
    prefix : str | None, default=None
        The **prefix** name of delayed constants. All delayed constants share the same prefix. A
        delayed constant will have a name formatted as "{prefix}{index+1}" if `index` is set, or
        just "{prefix}" if `index` is not set.

        - If None, the default prefix will be used with no update (original default is `C`).
        - If string, the prefix must be a valid Python identifier, preferably just a single
          uppercase letter. This will change the default prefix for **all** delayed constants,
          including those created in the past and future.

    initial_guess : Number, default=0.0
        The initial guess value for the delayed constant. This value is used as the starting point
        for optimization during the fitting process. Must be a finite number.
    bounds : tuple[Number | None, Number | None], default=(None, None)
        The lower and upper bounds for the delayed constant. These bounds are used to constrain the
        optimization process.

        For `initial_guess` and `bounds`, see the `x0` and `bounds` parameters in
        `scipy.optimize.minimize`.
    weight : int | float, default=1. (keyword-only)
        The weight of the delayed constant in all `DelayedConstant` instances. This is used for
        randomization purposes in the genetic programming process for symbolic regression.  Should
        be non-negative.

    Examples
    --------
    >>> # 1. use explicit subclassing - no type hint though
    >>> class DelayedConstantPos(
    ...     DelayedConstant, prefix="C_p", initial_guess=1.0, bounds=(0, None),
    ...     weight=1.0, cost=2.0
    ... ):
    ...     pass
    >>> # 2. use built-in class method with type hint
    >>> DelayedConstantNeg = DelayedConstant.create_subclass(
    ...     "DelayedConstantNeg", prefix="C_n", initial_guess=-1.0, bounds=(None, 0),
    ...     weight=1.0, cost=2.0
    ... )
    """

    _prefix: str = "C"
    _initial_guess: Number = 1.0
    _bounds: tuple[Number | None, Number | None] = (None, None)
    _weight: Number = 1.0
    _cost: Number = 2.0

    def __init_subclass__(
        cls,
        prefix: str = "C",
        initial_guess: Number = 0.0,
        bounds: tuple[Number | None, Number | None] = (None, None),
        weight: Number = 1.0,
        cost: Number = 2.0,
        **kwargs: Any,
    ) -> None:
        """
        Initialize a subclass of :class:`DelayedConstant`. Each :class:`DelayedConstant` class or
        subclass (and its instances) can only carry one unique `key` and one unique `initial_guess`,
        and one unique `bounds`. Thus, to get a new instance with a different configuration, you
        must create a new subclass.

        Parameters
        ----------
        prefix : str, default="C"
            The prefix for the delayed constant. Must be a valid Python identifier and may not end
            with a digit.

            The prefix must be unique from existing :class:`IndexedFuncUnit` subclasses.
        initial_guess : Number, default=0.0
            The initial guess value for the delayed constant. Must be a finite number.
        bounds : tuple[Number | None, Number | None], default=(None, None)
            The lower and upper bounds for the delayed constant.
        weight : Number, default=1.0
            The weight of the delayed constant. Should be non-negative.
        cost : Number, default=2.0
            The cost/complexity of the delayed constant. Should be non-negative.

        See Also
        --------
        create_subclass : Class method to dynamically create a new subclass of DelayedConstant.
        """
        low, high = bounds
        if low is not None and high is not None and np.isclose(low, high):
            raise ValueError(
                "Invalid bounds: lower bound must be smaller than upper bound."
            )
        if low is not None and initial_guess < low:
            raise ValueError("Invalid initial guess: must be greater than lower bound.")
        if high is not None and initial_guess > high:
            raise ValueError("Invalid initial guess: must be smaller than upper bound.")
        cls._bounds = (low, high)

        if not np.isfinite(initial_guess):
            raise ValueError("Invalid initial guess: must be a finite number.")
        cls._initial_guess = np.clip(initial_guess, low, high).item()

        if weight < 0:
            raise ValueError("Weight must be a non-negative number.")
        cls._weight = weight

        if cost < 0:
            raise ValueError("Cost must be a non-negative number.")
        cls._cost = cost

        # check if there is any `DelayedConstant` with the same initial guess and bounds
        for sub in IndexedFuncUnit._prefix_dict.values():
            if config.inplace_update_:
                break

            if sub is cls:  # ignore a duplicate
                continue
            if not issubclass(sub, DelayedConstant):
                continue

            s_low, s_high = sub._bounds
            if low != s_low or (
                low is not None and s_low is not None and not np.isclose(low, s_low)
            ):
                continue
            if high != s_high or (
                high is not None and s_high is not None and not np.isclose(high, s_high)
            ):
                continue

            initial_guess = float(np.clip(initial_guess, low, high))
            if not np.isclose(sub._initial_guess, initial_guess):
                continue

            raise ValueError(
                f"Found existing class `{sub.__name__}` with the same configuration. "
                f"Use `DelayedConstant.get(prefix={sub.get_prefix()})` to retrieve the class."
            )

        super().__init_subclass__(prefix=prefix, **kwargs)

    @classmethod
    def create_subclass(
        cls,
        name: str,
        module_name: str | None = None,
        /,
        *,
        prefix: str,
        initial_guess: Number,
        bounds: tuple[Number | None, Number | None],
        weight: Number = 1.0,
        cost: Number = 2.0,
    ) -> Type["DelayedConstant[ArrayLikeT]"]:
        """
        Dynamically create and return a new subclass of DelayedConstant.

        Parameters
        ----------
        name : str (positional)
            The name of the new subclass.
        prefix : str (keyword-only)
            The prefix for the delayed constant. Must be provided and should be unique from existing
            prefixes.
        initial_guess : Number (keyword-only)
            The initial guess value for the delayed constant. The default for the original class is
            0.0. When making a new subclass, this should be a different value.
        bounds : tuple[Number | None, Number | None] (keyword-only)
            The lower and upper bounds for the delayed constant. The default for the original class
            is (None, None). When making a new subclass, this should be a different value.

            At least one of `initial_guess` or `bounds` should be different from the original class,
            and other defined subclasses before the creation.
        weight : Number, default=1.0 (keyword-only)
            The weight of the delayed constant. Should be non-negative.
        cost : Number, default=2.0 (keyword-only)
            The cost/complexity of the delayed constant. Should be non-negative.

        Returns
        -------
        Type[DelayedConstant[ArrayLikeT]]
            The newly created subclass of :class:`DelayedConstant`.

        Raises
        ------
        ValueError
            If the name is not a valid Python identifier.
        """
        if not name.isidentifier():
            raise ValueError(
                f"Invalid class name: {name!r}. Must be a valid Python identifier."
            )

        # check if the class name has been used by another subclass
        module_name = module_name or __name__
        module = sys.modules[module_name]
        existing_cls = module.__dict__.get(name, None)
        if existing_cls:
            raise ValueError(
                f"Class name {name!r} is already used by another subclass."
            )

        # Dynamically create the subclass
        new_cls: type["DelayedConstant[ArrayLikeT]"] = type(
            name,
            (cls,),
            {"__module__": module_name},
            prefix=prefix,
            initial_guess=initial_guess,
            bounds=bounds,
            weight=weight,
            cost=cost,
        )
        # Register the class in the module's global namespace
        setattr(module, name, new_cls)

        # if existing_cls:
        #     inplace_cls_update(existing_cls, new_cls)
        return new_cls

    def __new__(
        cls,
        prefix: str | None = None,
        initial_guess: Number | None = None,
        bounds: tuple[Number | None, Number | None] | None = None,
        weight: Number = 1.0,
        cost: Number = 2.0,
        *args: Any,
    ) -> Self:
        """
        Create a new instance if no argument is provided or update the current class with the input
        parameters when :func:`psr.config.Config.inplace_update` is called, and return an instance
        of the update class.
        """
        instance = super().__new__(cls)
        if prefix is None or config.multiprocessing_:
            return instance

        if config.allow_singleton_ and not config.inplace_update_:
            # not in sandbox mode; no inplace update allowed
            raise ValueError("Inplace update is not allowed/enabled.")

        # not in multiprocessing - the other parameters must be provided
        if not prefix.isidentifier() or prefix[-1].isdigit():
            raise ValueError(
                f"Invalid prefix: {prefix!r}. Must be a valid Python identifier "
                "and not end with a digit."
            )
        if initial_guess is None or not np.isfinite(initial_guess) or bounds is None:
            raise ValueError(
                "Must provide a finite `initial_guess`, and provide `bounds`."
            )
        if any(b is not None and np.isnan(b) for b in bounds):
            raise ValueError(f"Invalid bounds: {bounds!r}. Must not contain NaN.")
        iguess: int | float = np.clip(initial_guess, *bounds).item()
        if weight < 0:
            raise ValueError(f"Invalid weight: {weight!r}. Must be non-negative.")
        if cost < 0:
            raise ValueError(f"Invalid cost: {cost!r}. Must be non-negative.")

        if config.inplace_update_:
            if cls.get(prefix=prefix) is not cls:
                cls._prefix_dict[prefix] = cls
            cls._prefix = prefix
            cls._initial_guess = iguess
            cls._bounds = bounds
            cls._weight = weight
            cls._cost = cost
            return instance

        # in sandbox mode - still return the same class, but store data in instance
        setattr(instance, "prefix_", prefix)
        setattr(instance, "initial_guess_", iguess)
        setattr(instance, "bounds_", bounds)
        setattr(instance, "weight_", weight)
        setattr(instance, "cost_", cost)

        return instance

    def __init__(
        self,
        prefix: str | None = None,
        initial_guess: Number | None = None,
        bounds: tuple[Number | None, Number | None] | None = None,
        weight: Number = 1.0,
        cost: Number = 2.0,
        *args: Any,
    ) -> None:
        """
        Create a new instance if no argument is provided or dynamically create a new subclass with
        the input parameters (similar to the :func:`create_subclass` method) and return an instance
        of it.

        **Note**: `prefix`, `class_name` and `weight` may be ignored or altered if in sandbox mode
        (:func:`psr.config.config.sandbox`), either when an existing (sub)class instance of
        :class:`DelayedConstant` is found with the same `initial_guess` and `bounds`, or when
        `prefix` or `class_name` conflicts with existing ones. In such cases, the original values
        will be stored in `prefix_`, `class_name_`, ..., properties of the returned **instance**.
        In normal mode, an exception is raised in such cases.

        See `__new__` for more details.

        Parameters
        ----------
        prefix : str | None
            The prefix for the delayed constant. If not provided, a new instance of the current
            class in returned.
        class_name : str | None
            The class name for the delayed constant to create a new subclass.
        initial_guess : Number | None
            The initial guess for the delayed constant to create a new subclass.
        bounds : tuple[Number | None, Number | None] | None
            The bounds for the delayed constant to create a new subclass.
        weight : Number
            The weight for the delayed constant to create a new subclass. Should be non-negative.
        cost : Number
            The cost for the delayed constant to create a new subclass. Should be non-negative.
        *args : Any, **not used**
            Additional positional arguments to pass to the constructor. This is added for better
            serialization/deserialization support between different package versions.

        See Also
        --------
        create_subclass : Class method to dynamically create new subclasses.
        """
        self.index = None
        self.fitted_value = None

        if prefix and config.inplace_update_:
            self.weight = weight
            self.cost = cost

    @property
    def index(self) -> int | None:
        """
        Get the index of the delayed constant.

        Returns
        -------
        int | None
            The index of the delayed constant, or None if not set.
        """
        return self._index

    @index.setter
    def index(self, new_index: int | None) -> None:
        """
        ## Property Setter
        Set the index of the delayed constant.

        Parameters
        ----------
        new_index : int | None
            The new index of the delayed constant, or None to unset it.

        Raises
        ------
        ValueError
            If the new index is not a non-negative integer or None.
        """
        if new_index is not None and new_index < 0:
            raise ValueError("Invalid index: must be a non-negative integer or None")

        self._index = new_index

    @property
    def name(self) -> str:
        """
        Get the name of the delayed constant.

        Returns
        -------
        str
            The name of the delayed constant.
        """
        if (index := self._index) is not None:
            return f"{self.prefix}{index+1:d}"

        return self.prefix

    @name.setter
    def name(self, new_name: str) -> NoReturn:
        """
        ## Property Setter
        Illegal operation. The name of a delayed constant is automatically compiled with the prefix
        for the class (and the index). Only the prefix can be updated, which can be done with the
        prefix setter `self.prefix = <new_prefix>`.

        Raises
        ------
        ValueError
            If the name of the delayed constant is attempted to be set.

        See Also
        --------
        update_prefix : class method to update the default prefix for all delayed constants.
        """
        raise ValueError(
            f"The name of a delayed constant cannot be set. "
            f"Only the prefix can be updated."
        )

    @property
    def arity(self) -> int:
        """
        Get the arity of the delayed constant, which is always 0.

        Returns
        -------
        int
            The arity of the delayed constant, which is always 0 since a delayed constant is not an
            operation and it does not process any arguments.
        """
        return 0

    @arity.setter
    def arity(self, new_arity: int) -> NoReturn:
        """
        ## Property Setter
        Not allowed: delayed constants should always have an arity of 0.

        Raises
        ------
        ValueError
            Always raises a ValueError since the arity of a delayed constant cannot be changed.
        """
        raise ValueError("Arity of a delayed constant cannot be changed.")

    @property
    def weight(self) -> Number:
        """
        Get the weight of the delayed constant. Only the class attribute can be accessed.

        Setting the weight for an instance will affect **all instances** of the class.

        Returns
        -------
        Number
            The weight of the delayed constant (class attribute).
        """
        return self.__class__._weight

    @weight.setter
    def weight(self, new_weight: Number) -> None:
        """
        ## Property Setter
        Set the weight of the delayed constant. This will set the weight for the class attribute.

        Parameters
        ----------
        new_weight : Number
            The new weight for the delayed constant.

        Raises
        ------
        ValueError
            If the new weight is not a non-negative number.
        """
        if new_weight < 0:
            raise ValueError("Invalid weight: must be a non-negative number.")
        self.__class__._weight = new_weight

    @property
    def cost(self) -> Number:
        """
        Get the cost of the delayed constant. Only the class attribute can be accessed.

        Setting the cost for an instance will affect **all instances** of the class.

        Returns
        -------
        Number
            The cost of the delayed constant.
        """
        return self.__class__._cost

    @cost.setter
    def cost(self, new_cost: Number) -> None:
        """
        ## Property Setter
        Set the cost of the delayed constant. This will set the cost for the class attribute.

        Parameters
        ----------
        new_cost : Number
            The new cost for the delayed constant.

        Raises
        ------
        ValueError
            If the new cost is not a non-negative number.
        """
        if new_cost < 0:
            raise ValueError("Invalid cost: must be a non-negative number.")
        self.__class__._cost = new_cost

    @property
    def initial_guess(self) -> Number:
        """
        Get the initial guess for the delayed constant. Only the class attribute can be accessed.

        Returns
        -------
        Number
            The initial guess for the delayed constant.
        """
        return self.__class__._initial_guess

    @initial_guess.setter
    def initial_guess(self, value: Number) -> NoReturn:
        """
        ## Property Setter
        Set the initial guess for the delayed constant.

        **Illegal operation**: The initial guess is a class attribute fixed at class creation. It
        cannot be changed. Create a new subclass of `DelayedConstant` with the desired initial
        guess, instead.

        Raises
        ------
        ValueError
            Always raises a ValueError since the initial guess cannot be changed.
        """
        raise ValueError(
            "Initial guess cannot be changed. "
            "Define a new subclass of `DelayedConstant` instead."
        )

    @property
    def bounds(self) -> tuple[Number | None, Number | None]:
        """
        Get the bounds for the delayed constant. Only the class attribute can be accessed.

        Returns
        -------
        tuple[Number | None, Number | None]
            The lower and upper bounds for the delayed constant.
        """
        return self.__class__._bounds

    @bounds.setter
    def bounds(self, value: tuple[Number | None, Number | None]) -> NoReturn:
        """
        ## Property Setter
        Set the bounds for the delayed constant.

        **Illegal operation**: The bounds are a class attribute fixed at class creation. They cannot
        be changed. Create a new subclass of `DelayedConstant` with the desired initial guess,
        instead.

        Raises
        ------
        ValueError
            Always raises a ValueError since the bounds cannot be changed.
        """
        raise ValueError(
            "Bounds of a delayed constant cannot be changed. "
            "Define a new subclass of `DelayedConstant` instead."
        )

    @property
    def vbounds(self) -> tuple[Number, Number]:
        """
        Value-based bounds for the delayed constant after mapping `None` to infinity.

        Returns
        -------
        tuple[Number, Number]
            The value-based bounds for the delayed constant.
        """
        bounds = self.__class__._bounds
        return (
            bounds[0] if bounds[0] is not None else float("-inf"),
            bounds[1] if bounds[1] is not None else float("inf"),
        )

    @property
    def is_delayed(self) -> bool:
        """
        Check if the function unit is a delayed constant.

        Returns
        -------
        bool
            True if the function unit is a delayed constant, False otherwise.
        """
        return True

    @property
    def is_fitted(self) -> bool:
        """
        Check if the function unit is fitted.

        Returns
        -------
        bool
            True if the function unit is fitted, False otherwise.
        """
        return self.fitted_value is not None

    @property
    def fitted_value(self) -> Number | None:
        """
        Get the fitted value of the delayed constant.

        Returns
        -------
        Number | None
            The fitted value of the delayed constant, or None if not set.
        """
        return self._fitted_value

    @fitted_value.setter
    def fitted_value(self, value: Number | None) -> None:
        """
        ## Property Setter
        Set the fitted value of the delayed constant.

        Parameters
        ----------
        value : Number | None
            The new fitted value to set for the delayed constant.
        """
        self._fitted_value = value

    def evaluate(
        self,
        *args: Any,
        X: Any = None,
        C: ArrayLikeT | Sequence[Number | None] | None = None,
        **kwargs: Any,
    ) -> ArrayLikeT | Number:
        """
        Evaluate the delayed constant with the given arguments.

        Parameters
        ----------
        *args : Any
            Positional arguments to evaluate the delayed constant. **NOT USED**
        X : Any, default=None
            Placeholder keyword argument for the input data array, typically a 2D array-like
            structure where each row represents a data point and each column represents a variable.
            **NOT USED**
        C : ArrayLikeT | Sequence[Number | None] | None, default=None
            Placeholder keyword argument for the array of delayed constants, typically a 1D
            array-like structure where each element represents a delayed constant.

            This parameter is optional if the delayed constant has been fitted. Otherwise, it must
            be provided.
        **kwargs : Any
            Keyword arguments to evaluate the delayed constant.

        Returns
        -------
        ArrayLikeT | Number
            The value of the delayed constant from the provided array of delayed constants.
        """
        if self.index is None:
            raise IndexError(
                "The index of the delayed constant is not set. "
                "Did you forget to run an automatic index assignment?"
            )

        if C is None:
            if (fitted_value := self.fitted_value) is None:
                raise ValueError(
                    "Array of delayed constants C must be provided if not fitted."
                )
            return fitted_value

        if (value := C[self.index]) is not None:
            return value

        if (fitted_value := self.fitted_value) is None:
            raise ValueError(
                "Array of delayed constants C must be provided if not fitted."
            )
        return fitted_value

    def format(
        self,
        *args: str,
        protect: bool = False,
        C: ArrayLikeT | Sequence[Number | None] | None = None,
        C_use_fitted: bool = False,
        C_protection_rules: Sequence[bool | None] | None = None,
        **kwargs: Any,
    ) -> str:
        """
        Format the delayed constant into a string representation for the entire expression.

        Parameters
        ----------
        *args : str
            String representations of the arguments to be formatted into the delayed constant's
            template. For delayed constants, this should be empty/omitted.
        protect : bool, default=False
            Whether the returned string should be protected with parentheses, if necessary.

            A delayed constant is typically already protected, so this parameter should not take
            effect for delayed constants.
        C : ArrayLikeT | Sequence[Number | None] | None
            An optional sequence of known delayed constants to use when formatting delayed
            constants. Instead of using annotations such as `C1`, this can be used to provide
            the actual values.

            If `C` is provided, the delayed constant will be formatted using the value at its
            index in `C`, unless `C_use_fitted` is set to True and the fitted value is available.
        C_use_fitted : bool, default=False
            Whether to use the fitted value from the delayed constant, if available, instead of
            the value from the previous input argument `C`.
        C_protection_rules : Sequence[bool | None] | None
            An optional sequence of protection rules for the delayed constants, corresponding to the
            elements in `C`. If provided, this will be used to determine whether each delayed
            constant should be protected with parentheses, if necessary. Unless specified as True,
            the protection will not be applied.
        **kwargs : Any
            Additional keyword arguments to customize the formatting behavior. Not used here.

        Returns
        -------
        str
            The string representation of the delayed constant. The number in the string will be
            1-indexed.
        """
        index = self.index
        protect = bool(
            protect
            and C_protection_rules is not None
            and index is not None
            and len(C_protection_rules) > index
            and C_protection_rules[index]
        )

        s = self.name  # default
        if C_use_fitted and self.is_fitted:
            # use fitted value
            s = str(self.fitted_value).strip()
        elif C is not None:
            # use provided constants
            if index is None:
                raise ValueError(
                    "Found delayed constant without index. "
                    "Remove the input argument `C` or set the index."
                )
            if len(C) > index:
                s = str(C[index]).strip()

        if protect:
            return f"({s})"
        return s

    def reinit(self, deep: bool = False) -> Self:
        """
        Reinitialize the delayed constant and get a new non-singleton instance (new object identity)
        , regardless of immutability. The new instance should have the same core attributes.

        Parameters
        ----------
        deep : bool, default=False
            Whether to create a deep copy of the delayed constant. This parameter is ignored since
            the new copy should always be a deep copy.

        Returns
        -------
        Self
            A new **non-singleton** instance of the delayed constant with the same core attributes.
        """
        return self.__class__()

    @classmethod
    @overload
    def identify(cls, key: Number, /, *, init: bool = False) -> None: ...
    @classmethod
    @overload
    def identify(cls, key: str, /, *, init: bool = False) -> Self | None: ...

    @classmethod
    def identify(cls, key: str | Number, /, *, init: bool = False) -> Self | None:
        """
        Identify a delayed constant by its key.

        Parameters
        ----------
        key : str | Number
            The key to identify the delayed constant.
        init : bool, default=False
            Whether to initialize the delayed constant if not found. **NOT USED**: A delayed
            constant cannot be initialized from a string/key.

        Returns
        -------
        Self | None
            The identified delayed constant, or None if not found.
        """
        if not isinstance(key, str):
            return None

        key = key.strip()
        if not key.isidentifier():
            return None

        for prefix, subcls in IndexedFuncUnit._prefix_dict.items():
            if not issubclass(subcls, cls):
                continue
            num = re.match(f"^{prefix}([1-9]\\d*|)$", key)
            if not num:
                continue
            # DelayedConstant is always unique
            return subcls()
        return None

    def __repr__(self) -> str:
        """
        Return a string representation of the delayed constant.

        Returns
        -------
        str
            A string representation of the delayed constant.
        """
        return (
            f"{self.__class__.__name__}({self.name}, initial_guess={self.initial_guess}, "
            f"bounds={self.bounds}, weight={self.weight})"
        )

    def __str__(self) -> str:
        """
        Return a string representation of the delayed constant.

        Returns
        -------
        str
            A string representation of the delayed constant.
        """
        if (fitted_value := self.fitted_value) is not None:
            return f"{self.name}@{fitted_value:.3g}"
        return self.name

    def __eq__(self, other: object) -> bool:
        """
        Check if two delayed constants are equal. Two delayed constants are only equal if they are
        of the same class type. **The index value is ignored.**

        Parameters
        ----------
        other : object
            The other object to compare against.

        Returns
        -------
        bool
            True if the delayed constants are equal, False otherwise.
        """
        if self.__class__ is other.__class__:
            return True
        if not isinstance(other, DelayedConstant):
            return False
        if self.initial_guess != other.initial_guess:
            return False
        if not self.bounds == other.bounds:
            return False
        return True

    def __reduce__(
        self,
    ) -> tuple[type[Self], tuple[Any, ...], dict[str, Any]]:
        """
        Serialize the :class:`DelayedConstant` instance for pickling. When in subprocess mode,
        make sure to initialize the function units in the main process first for
        :class:`DelayedConstant`'s - this will save time and memory.

        Returns
        -------
        tuple[type[Self], tuple[Any, ...], dict[str, Any]]
            A tuple containing the class type, the constructor arguments (and the state dictionary).
        """
        cls = self.__class__
        state: dict[str, Any] = {
            "_index": self._index,
            "_fitted_value": self._fitted_value,
        }
        if config._multiprocessing:
            return (cls, tuple(), state)
        return (
            cls,
            (
                cls._prefix,
                cls._initial_guess,
                cls._bounds,
                cls._weight,
                cls._cost,
            ),
            state,
        )
