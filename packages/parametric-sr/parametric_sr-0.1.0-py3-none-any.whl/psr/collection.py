"""
module for implementing collection of things, e.g., function units, and, collections of function
units
"""

from collections import defaultdict
from contextlib import contextmanager
from typing import (
    Any,
    Generator,
    Generic,
    Hashable,
    Iterable,
    Literal,
    NoReturn,
    Optional,
    Self,
    Sequence,
    TypeVar,
    cast,
    final,
    overload,
)
import warnings

import numpy as np
from numpy.typing import NDArray

from .base.func_unit import FuncUnit, Operation, Variable, Constant, DelayedConstant
from .func_unit import (
    get_operations,
    get_variables,
    get_constants,
    get_delayed_constants,
)
from .func_unit import DelayedConstantOptions, SequenceOfDelayedConstantOptions
from .typing import (
    ArrayLikeT,
    Number,
    OperationOptions,
    PSRCollectionOptions,
    RngGeneratorSeed,
    T,
)
from .utils import noquote_str


class _Missing:
    """
    Marker class for missing values.
    """

    @final
    def __bool__(self) -> bool:
        return False


_missing = _Missing()
KeyT = TypeVar("KeyT", bound=Hashable)
ValueT = TypeVar("ValueT")
FuncUnitT = TypeVar("FuncUnitT", bound=FuncUnit)

FuncUnitTypes = (
    Operation[ArrayLikeT]
    | Variable[ArrayLikeT]
    | Constant[ArrayLikeT]
    | DelayedConstant[ArrayLikeT]
)


class Collection(Generic[KeyT, ValueT]):
    """
    A dictionary-like and list-like collection of key-value pairs, each with a weight value used
    for random selection from the collection. The keys are not hashed though; they are stored in
    a list instead. Therefore, only use the class for small to medium-sized collections.

    **Warning**: If your key type is `int` or `slice`, index-based access may lead to unexpected
    behavior since it can be interpreted as a key (`dict-like`) and an index/slice (`list-like`),
    especially when using `__getitem__` and `__delitem__`. Use replacement methods such as
    `set_value`, `set_weight`, `pop`, `popitem` instead.

    Subclassing
    -----------
    Subclasses of `Collection` can:

    1. use the `immutable` (bool) argument in their constructors
    2. define `_immutable` (bool) in the class body

    to specify whether the collection should be immutable or not. Any `True` definition will make
    the subclass collection immutable: the keys of the collection cannot be modified after
    instantiation; only the values and weights are allowed to be modified.

    Attributes
    ----------
    keys : list[KeyT], the keys for the collection.
    values : list[ValueT], the values for the collection.
    weights : NDArray[np.float64], the weights for the collection.
    has_equal_len : bool, whether the collection has equal lengths for keys, values, and weights.
    is_immutable : bool, whether the collection class is immutable. The keys of an immutable
        collection cannot be modified after instantiation; only the values and weights are allowed
        to be modified.

    Methods
    -------
    select : method to select a random item from the collection; or multiple items
    check : check if the keys, values, and weights are aligned
    items : dict-like, iterator over the items (key, value, weight)
    iter : dict-like, iterator over the items (key, value, weight)
    index : list-like, get the index of an item by its key
    get : dict-like, get the value and weight of an item by its key
    set_value : set the value of an existing item by its key
    set_weight : set the weight of an existing item by its key
    insert : list-like, insert a new item into the collection at the specified index
    pop : list-like | dict-like, remove an item by its key (higher priority) or index
    popitem : list-like pop, remove and return an item by its index (default last)
    clear : dict-like, remove all items from the collection (a warning will be issued)
    update : dict-like, update the collection with a new collection of the same type
    mutate : context manager to allow temporary mutation of an immutable collection.
    __getitem__ : list-like | dict-like, get the value(s) and weight(s) of an item by the key(s)
    __setitem__ : dict-like, set the value and weight of an item by its key (existing or new)
    __delitem__ : list-like | dict-like, remove an item by key, index, or slice
    __add__, __iadd__ : list-like, add one new item to the collection with (key, value, weight)
    __sub__, __isub__ : list-like, remove item(s) from the collection with key(s)
    __contains__ : dict-like, check if a key or value is in the collection
    __len__ : list-like, get the number of items in the collection
    __iter__ : dict-like, get an iterator over the keys
    __repr__ : get a string representation of the collection

    Examples
    --------
    >>> import numpy as np
    >>> col: Collection[str, str] = Collection("abcdef", "ABCDEF")  # str -> list[str] conversion
    >>> rng = np.random.default_rng(42)
    >>> print(col.select(rng))
    ('e', 'E', np.float64(1.0))
    >>> print(col.select(rng))
    ('c', 'C', np.float64(1.0))
    >>> rng = np.random.default_rng(42)
    >>> print(col.select(rng))  # reproducible
    ('e', 'E', np.float64(1.0))
    >>> col + ("g", "G", 1.0)
    """

    _immutable = False

    def __init_subclass__(cls, immutable: bool = False, **kwargs) -> None:
        cls._immutable = immutable or cls._immutable
        return super().__init_subclass__(**kwargs)

    def __init__(
        self,
        keys: Optional[Sequence[KeyT]] = None,
        values: Optional[Sequence[ValueT]] = None,
        /,
        weights: Optional[Sequence[float]] = None,
        empty: bool = True,
        *args: Any,
    ) -> None:
        """
        Initialize a collection instance with aligned keys, values, and weights, or just an empty
        collection.

        Parameters
        ----------
        keys : Sequence[KeyT], optional
            The keys for the collection. The keys must be hashable and non-empty, unless
            `empty=True`.

            A key **cannot** be a list; it should be hashable such as str, int, float, tuple, etc.
            This is type-hinted but not enforced.
        values : Sequence[ValueT], optional
            The values for the collection. Must match the size of keys, unless `empty=True`.
        weights : Sequence[float], optional
            The weights for the collection. Must match the size of keys, unless `empty=True`. The
            weights are used for random selection from the collection. They should be non-negative.
            At least one weight must be positive. An item with a weight of 0 will never be selected.
        empty : bool, default=True
            Whether to create an empty collection. If `empty=True`, the collection will be
            initialized with empty keys, values, and weights.
        *args : Any, **not used**
            Additional positional arguments to pass to the constructor. This is added for better
            serialization/deserialization support between different package versions.
        """
        if keys is None and values is None and weights is None and empty:
            self._keys: list[KeyT] = []
            self._values: list[ValueT] = []
            self._weights: NDArray[np.float64] = np.array([], dtype=np.float64)
            return

        if keys is None or values is None:
            raise ValueError("Collection must contain keys and values.")

        n = len(keys)
        if n == 0:
            raise ValueError("Collection must contain at least one item.")
        self._keys = list(keys)

        if len(values) != n:
            raise ValueError(
                "Collection must contain the same number of values as keys."
            )
        self._values = list(values)

        if weights is None:
            self._weights: NDArray[np.float64] = np.repeat(1.0, n)
        elif len(weights) != n:
            raise ValueError(
                "Collection must contain the same number of weights as keys."
            )
        else:
            self._weights = np.array(weights, dtype=np.float64)
            if np.any(self._weights < 0):
                raise ValueError("Collection weights must be non-negative.")
            if np.allclose(self._weights, 0):
                raise ValueError("Collection weights cannot all be zero.")

    @property
    def keys(self) -> list[KeyT]:
        """
        The keys for items in the collection.

        Returns
        -------
        list[KeyT]
            The keys for items in the collection.
        """
        return self._keys

    @keys.setter
    def keys(self, new_keys: Sequence[KeyT]) -> NoReturn:
        """
        ## Property Setter
        **Illegal operation**: keys cannot be directly set.

        See Also
        --------
        update : method to update the items.
        __setitem__ : method to update a specific item.
        """
        raise ValueError("Cannot set the keys directly.")

    @property
    def values(self) -> list[ValueT]:
        """
        The values for items in the collection.

        Returns
        -------
        list[ValueT]
            The values for items in the collection.
        """
        return self._values

    @values.setter
    def values(self, new_values: Sequence[ValueT]) -> NoReturn:
        """
        ## Property Setter
        **Illegal operation**: values cannot be directly set.

        See Also
        --------
        update : method to update the items.
        __setitem__ : method to update a specific item.
        """
        raise ValueError("Cannot set the values directly.")

    @property
    def weights(self) -> NDArray[np.float64]:
        """
        The weights for items in the collection for random selection. Weights must be non-negative
        and have at least one positive value. Items with a weight of 0 will never be selected.

        Returns
        -------
        NDArray[np.float64]
            The weights for items in the collection as a numpy array (for vectorized operations).
        """
        return self._weights

    @weights.setter
    def weights(self, new_weights: Optional[Sequence[float]]) -> NoReturn:
        """
        ## Property Setter
        **Illegal operation**: weights cannot be directly set.

        See Also
        --------
        update : method to update the items.
        __setitem__ : method to update a specific item.
        """
        raise ValueError("Cannot set the weights directly.")

    @property
    def has_equal_len(self) -> bool:
        """
        Check if the collection has equal length for keys, values, and weights.

        Returns
        -------
        bool
            True if the collection has equal length for keys, values, and weights, False otherwise.
        """
        return len(self._keys) == len(self._values) == len(self._weights)

    @property
    def is_immutable(self) -> bool:
        """
        Check if the collection is immutable.

        Returns
        -------
        bool
            True if the collection is immutable, False otherwise.

        See Also
        --------
        mutate : context manager to allow temporary mutation of the collection.
        """
        return self._immutable

    @overload
    def select(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: None = None,
        replace: bool = True,
    ) -> tuple[KeyT, ValueT, np.float64]: ...
    @overload
    def select(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: int,
        replace: bool = True,
    ) -> tuple[list[KeyT], list[ValueT], NDArray[np.float64]]: ...

    def select(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: None | int = None,
        replace: bool = True,
    ) -> (
        tuple[KeyT, ValueT, np.float64]
        | tuple[list[KeyT], list[ValueT], NDArray[np.float64]]
    ):
        """
        Randomly select an item or multiple items from the collection. The weights are used to
        weight the probability.

        Parameters
        ----------
        seed : RngGeneratorSeed, optional
            Random number generator seed. See `numpy.random.default_rng` for more information.
        slicing : slice, optional
            A slice object to specify a subset of the collection to select from.
        size : int, optional
            The number of items to select. This is analogous to the `size` parameter in
            `numpy.random.Generator.choice`.

            - If None, a single item will be selected and returned; the elements in the returned
              tuple will be for a single item.
            - If `size` is specified, multiple items will be selected and returned; the elements
              in the returned tuple will be an iterable of the selected items, even when `size=1`.

        replace : bool, default=True
            Whether to replace the selected items in the collection when selecting multiple items.
            Only applicable when `size` is specified and larger than 1.

        Returns
        -------
        tuple[KeyT, ValueT, np.float64] | tuple[list[KeyT], list[ValueT], NDArray[np.float64]]
            The key(s), value(s), and weight(s) of the selected item(s).

        Raises
        ------
        ValueError

            - If the collection is invalid (mismatched lengths, invalid weights, empty, etc.)
            - If the collection is empty after slicing.
            - If the provided size is not positive.
        """
        self.check(error="raise")
        rng = np.random.default_rng(seed)

        # Sample a key based on its weight
        keys = self._keys[slicing]
        if (n := len(keys)) == 0:
            raise ValueError("Invalid slicing: cannot select from an empty collection.")

        values = self._values[slicing]
        weights = self._weights[slicing]
        _weights = weights / np.sum(weights)
        if size is None:
            idx = rng.choice(n, p=_weights)
            return keys[idx], values[idx], weights[idx]

        if not size > 0:
            raise ValueError("Size must be a positive integer.")
        idxs = rng.choice(n, size=size, replace=replace, p=_weights)
        return [keys[i] for i in idxs], [values[i] for i in idxs], weights[idxs]

    def check(self, /, error: Literal["raise", "warn", "ignore"] = "warn") -> None:
        """
        Check if the collection is valid. A collection is valid when the following conditions are
        all met:

        - keys, values, and weights are all present.
        - keys, values, and weights have the same length and not empty.
        - weights are non-negative and have at least one positive value.

        Parameters
        ----------
        error : Literal["raise", "warn", "ignore"], optional
            The error handling strategy when the collection is invalid.

            - "raise": ValueError
            - "warn": UserWarning
            - "ignore": No action - no check will be performed.

        Raises
        ------
        ValueError
            If the collection is invalid and the error handling strategy is "raise".
        UserWarning
            If the collection is invalid and the error handling strategy is "warn".
        """
        if error == "ignore":
            return

        msg = ""

        n = len(self._keys)
        if n == 0:
            msg = f"{self.__class__.__name__} is empty."
        elif len(self._values) != n:
            msg = f"{self.__class__.__name__} values are not aligned with keys."
        elif len(self._weights) != n:
            msg = f"{self.__class__.__name__} weights are not aligned with keys."
        elif np.any(self._weights < 0):
            msg = f"{self.__class__.__name__} weights must be non-negative."
        elif np.allclose(self._weights, 0):
            msg = f"{self.__class__.__name__} weights cannot all be zero."

        if not msg:
            return

        if error == "raise":
            raise ValueError(msg)
        elif error == "warn":
            warnings.warn(msg)

    def items(self) -> Generator[tuple[KeyT, ValueT, np.float64], None, None]:
        """
        Iterate over the items in the collection. `dict-like`

        Yields
        ------
        tuple[KeyT, ValueT, np.float64]
            The key, value, and weight of each item in the collection.
        """
        for key, value, weight in zip(self._keys, self._values, self._weights):
            yield key, value, weight

    def iter(self) -> Generator[tuple[KeyT, ValueT, np.float64], None, None]:
        """
        Iterate over the items in the collection. The same as `items()`. `dict-like`

        Yields
        ------
        tuple[KeyT, ValueT, np.float64]
            The key, value, and weight of each item in the collection.
        """
        yield from self.items()

    def index(self, key: Any, /) -> int:
        """
        Find the index of the given key in the collection. `list-like`

        Parameters
        ----------
        key : Any
            The key to find in the collection. Only exact matches are considered.

        Returns
        -------
        int
            The index of the key in the collection.

        Raises
        ------
        KeyError
            If the key is not found in the collection.
        """
        try:
            return self._keys.index(key)
        except ValueError:
            raise KeyError(f"Key {key!r} not found in collection.")

    def get(self, key: KeyT, default: T = None, /) -> tuple[ValueT, np.float64] | T:
        """
        Get the value and weight of the item with the given key. `dict-like`

        Parameters
        ----------
        key : KeyT
            The key of the item to retrieve.
        default : T, optional
            The default value to return if the key is not found.

        Returns
        -------
        tuple[ValueT, np.float64] | T
            The value and weight of the item with the given key, or the default value.

        Raises
        ------
        ValueError
            If the collection is invalid and cannot be accessed.
        """
        try:
            idx = self.index(key)
            if not self.has_equal_len:
                raise ValueError("Collection has mismatched lengths.")
            return self._values[idx], self._weights[idx]
        except KeyError:
            return default

    def set_value(
        self,
        key: KeyT | int,
        value: ValueT,
        /,
        *,
        key_only: bool = True,
        error: Literal["raise", "warn", "ignore"] = "ignore",
    ) -> None:
        """
        Set the value of an existing item in the collection by **key** or **index**. Key match
        precedes index match if the key type itself is int.

        By default, index match is not enabled unless `key_only=False`.

        Parameters
        ----------
        key : KeyT | int
            The key or index of the item to update. Key match precedes index match if the key type
            itself is int.
        value : ValueT
            The new value to set for the item.
        key_only : bool, default=True
            If True, the `key` parameter is seen as a **key** and **not an index**. If False, index
            match will proceed if key match failed and `key` is an integer.
        error : Literal["raise", "warn", "ignore"], default="ignore"
            The error handling strategy to use when checking the collection **after** a successful
            set operation. Updating existing values should not disrupt the collection's integrity;
            thus, the default is "ignore".

        Raises
        ------
        ValueError

            - If the collection has mismatched lengths (keys/values/weights).
            - If the collection is invalid after the set operation.

        KeyError
            If the key is not found.
        IndexError
            If the index is out of bounds.

        See Also
        --------
        set_weight : method to set the weight of an existing item in the collection.
        __setitem__ : dict-like method to set a new item or update an existing item
        """
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        try:
            idx = self.index(key)
        except KeyError as e:
            if not isinstance(key, int) or key_only:
                raise e
            idx = key
        self._values[idx] = value
        self.check(error=error)

    def set_weight(
        self,
        key: KeyT | int,
        weight: Optional[float],
        /,
        *,
        key_only: bool = True,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> None:
        """
        Set the weight of an existing item in the collection by **key** or **index**. Key match
        precedes index match if the key type itself is int.

        By default, index match is not enabled unless `key_only=False`.

        Parameters
        ----------
        key : KeyT | int
            The key or index of the item to update. Key match precedes index match if the key type
            itself is int.
        weight : float, optional
            The new weight to set for the item.
        key_only : bool, default=True
            If True, the `key` parameter is seen as a **key** and **not an index**. If False, index
            match will proceed if key match failed and `key` is an integer.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use when checking the collection **after** a successful
            set operation.

        Raises
        ------
        ValueError

            - If the collection has mismatched lengths (keys/values/weights).
            - If the weight is invalid (e.g., negative).
            - If the collection is invalid after the set operation.

        KeyError
            If the key is not found.
        IndexError
            If the index is out of bounds.

        See Also
        --------
        set_value : set the value of an existing item by its key.
        __setitem__ : dict-like method to set a new item or update an existing item.
        """
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        weight = 1.0 if weight is None else weight
        if weight < 0:
            raise ValueError("Weight must be non-negative.")

        try:
            idx = self.index(key)
        except KeyError as e:
            if not isinstance(key, int) or key_only:
                raise e
            idx = key
        self._weights[idx] = weight
        self.check(error=error)

    def insert(
        self,
        index: int,
        key: KeyT,
        value: ValueT,
        /,
        *,
        weight: Optional[float] = None,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> None:
        """
        Insert a new item into the collection at the specified index. `list-like`

        Parameters
        ----------
        index : int
            The index at which to insert the new item. If -1, the item is appended to the end.
        key : KeyT
            The key of the new item.
        value : ValueT
            The value of the new item.
        weight : float, optional
            The weight of the new item. If None, the default weight is used.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use when checking the collection **after** a successful
            insert operation.

        Raises
        ------
        ValueError

            - If the collection is immutable.
            - If the collection has mismatched lengths (keys/values/weights).
            - If the weight is invalid (e.g., negative).
            - If the collection is invalid after the insert operation.

        IndexError
            If the index is out of bounds.

        See Also
        --------
        set_value : set the value of an existing item by its key.
        __setitem__ : dict-like method to set a new item or update an existing item.
        """
        if self.is_immutable:
            raise ValueError("Cannot insert into an immutable collection.")
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        weight = 1.0 if weight is None else weight
        if weight < 0:
            raise ValueError("Weight must be non-negative.")

        self._keys.insert(index, key)
        self._values.insert(index, value)
        self._weights = np.insert(self._weights, index, weight)

        self.check(error=error)

    @overload
    def pop(
        self,
        key: KeyT | int,
        /,
        *,
        key_only: bool = True,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> tuple[KeyT, ValueT, np.float64]: ...
    @overload
    def pop(
        self,
        key: KeyT | int,
        default: T,
        /,
        *,
        key_only: bool = True,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> tuple[KeyT, ValueT, np.float64] | T: ...

    def pop(
        self,
        key: KeyT | int,
        default: T = _missing,
        /,
        *,
        key_only: bool = True,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> tuple[KeyT, ValueT, np.float64] | T:
        """
        Pop an item from the collection by **key** or **index**. Key search precedes index search.
        If the key/index is not found, return the default value. `list-like, dict-like`

        By default, index match is not enabled unless `key_only=False`.

        Parameters
        ----------
        key : KeyT | int
            The key or index of the item to pop.
        default : T, optional
            The default value to return if the key is not found. Must be provided explicitly;
            otherwise, a KeyError will be raised if the key is not found.
        key_only : bool, default=True
            If True, the `key` parameter is seen as a **key** and **not an index**. If False, index
            match will proceed if key match failed and `key` is an integer.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use when checking the collection **after** a successful
            pop operation.

        Returns
        -------
        tuple[KeyT, ValueT, np.float64] | T
            The key, value, and weight of the item with the given key, or the default value.

        Raises
        ------
        ValueError

            - If the collection is immutable.
            - If the collection is invalid before or after popping.

        KeyError, IndexError
            If the key/index is not found in the collection and a default value is not provided.
        """
        if self.is_immutable:
            raise ValueError("Cannot pop from an immutable collection.")
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        try:
            idx = self.index(key)
        except KeyError as e:
            if not isinstance(key, int) or key_only:
                if default is not _missing:
                    return default
                raise e
            idx = key

        key = self._keys.pop(idx)
        value = self._values.pop(idx)
        weight = self._weights[idx]
        self._weights = np.delete(self._weights, idx)

        self.check(error=error)
        return key, value, weight

    def popitem(
        self, index: int = -1, /, error: Literal["raise", "warn", "ignore"] = "warn"
    ) -> tuple[KeyT, ValueT, np.float64]:
        """
        Pop an item from the collection by **index**. `list-like`

        Parameters
        ----------
        index : int
            The index of the item to pop.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use when checking the collection **after** a successful
            pop operation.

        Returns
        -------
        tuple[KeyT, ValueT, np.float64]
            The key, value, and weight of the item at the given index.

        Raises
        ------
        ValueError

            - If the collection is immutable.
            - If the collection is invalid before or after popping.

        IndexError
            If the index is out of bounds.
        """
        if self.is_immutable:
            raise ValueError("Cannot pop from an immutable collection.")
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        key = self._keys.pop(index)
        value = self._values.pop(index)
        weight = self._weights[index]
        self._weights = np.delete(self._weights, index)

        self.check(error=error)
        return key, value, weight

    def clear(self, error: Literal["warn", "ignore"] = "warn") -> None:
        """
        Clear all items in the collection. `dict-like`

        Parameters
        ----------
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use when checking the collection **after** a successful
            clear operation. By default, a warning will be issued if the collection is invalid.

        Raises
        ------
        ValueError
            If the collection is immutable.
        UserWarning
            If `error` is "warn" because of the empty collection after clearing.
        """
        if self.is_immutable:
            raise ValueError("Cannot clear an immutable collection.")

        self._keys.clear()
        self._values.clear()
        self._weights = np.empty((0,), dtype=np.float64)

        if error == "warn":
            warnings.warn("Collection is empty after clearing.")

    def update(
        self, new_col: Self, /, *, error: Literal["raise", "warn", "ignore"] = "warn"
    ) -> None:
        """
        Update the collection with new items from another collection. `dict-like`

        Parameters
        ----------
        new_col : Self
            The new collection to update from.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use when checking the collection **after** a successful
            update operation.

        Raises
        ------
        ValueError
            If the collection is invalid before or after update.
        """
        for key, value, weight in new_col.items():
            self.__setitem__(key, (value, weight), error="ignore")
        self.check(error=error)

    @contextmanager
    def mutate(self) -> Generator[Self, None, None]:
        """
        Context manager to allow temporary mutation of the instance.
        """
        self._immutable = False
        try:
            yield self
        finally:
            # restore to class level default
            del self._immutable

    @overload
    def __getitem__(
        self, index: KeyT | int | slice, /, *, key_only: Literal[True]
    ) -> tuple[KeyT, ValueT, np.float64]: ...
    @overload
    def __getitem__(
        self, index: KeyT | int, /, *, key_only: bool = False
    ) -> tuple[KeyT, ValueT, np.float64]: ...
    @overload
    def __getitem__(
        self, index: slice, /, *, key_only: bool = False
    ) -> tuple[list[KeyT], list[ValueT], NDArray[np.float64]]: ...

    def __getitem__(
        self, index: KeyT | int | slice, /, *, key_only: bool = False
    ) -> (
        tuple[KeyT, ValueT, np.float64]
        | tuple[list[KeyT], list[ValueT], NDArray[np.float64]]
    ):
        """
        Get item(s) from the collection with a key, an index, or a slice. If the keys for the items
        are of type slice, then a slice is first considered as a key and then as a slicing strategy.
        The match order is key value, index, and slice, whichever can be parsed correctly first.
        `list-like, dict-like`

        Parameters
        ----------
        index : KeyT | int | slice
            A key, an index, or a slice to select item(s) from the collection. The match order is
            key value, index, and slice, whichever can be parsed correctly first.
        key_only : bool, default=False
            If True, the `index` parameter can only be seen as a key, and not as an index or slice.

        Returns
        -------
        tuple[KeyT, ValueT, np.float64] | tuple[list[KeyT], list[ValueT], NDArray[np.float64]]
            The key(s), value(s), and weight(s) of the item(s) at the given index.

        Raises
        ------
        ValueError
            If the collection is invalid and cannot be accessed.
        IndexError
            If the index is out of bounds.
        TypeError
            If the index cannot be resolved.
        """
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        try:
            index = self.index(index)
        except KeyError as e:
            if key_only:
                raise e

        if isinstance(index, int):
            return self._keys[index], self._values[index], self._weights[index]
        elif isinstance(index, slice):
            return self._keys[index], self._values[index], self._weights[index]
        else:
            raise TypeError("Invalid index type.")

    def __setitem__(
        self,
        key: KeyT,
        value_weight: tuple[ValueT, float | None],
        *,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> None:
        """
        Set a new item or update an existing item in the collection by **key**. `dict-like`

        Parameters
        ----------
        key : KeyT
            The key of the item to set.
        value_weight : tuple[ValueT, float | None]
            The value and weight of the item to set. A None weight is by default treated as 1.0.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use to check the collection **after** a successful set
            operation.

        Raises
        ------
        ValueError

            - If the collection is invalid before or after setting.
            - If the provided weight is negative.
            - If the collection is immutable and a new key is being added.

        See Also
        --------
        set_value : specifically update the values for existing items.
        set_weight : specifically update the weights for existing items.
        """
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        value, weight = value_weight
        weight = 1.0 if weight is None else weight
        if weight < 0:
            raise ValueError("Weight must be non-negative.")

        try:
            # existing key
            idx = self.index(key)
            self._values[idx] = value
            self._weights[idx] = weight
        except KeyError:
            # new key
            if self.is_immutable:
                raise ValueError("Cannot add to an immutable collection.")
            self._keys.append(key)
            self._values.append(value)
            self._weights = np.append(self._weights, weight)

        self.check(error=error)

    def __delitem__(
        self,
        index: KeyT | int | slice,
        *,
        key_only: bool = False,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> None:
        """
        Delete item(s) from the collection by **key** or **index**. The match order is key value,
        index, and slice, whichever can be parsed correctly first. `list-like, dict-like`

        Parameters
        ----------
        index : KeyT | int | slice
            A key, an index, or a slice to select item(s) from the collection for deletion. The
            match order is key value, index, and slice, whichever can be parsed correctly first.
        key_only : bool, default=False
            If True, the `index` parameter can only be seen as a key, and not as an index or slice.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use to check the collection **after** a successful delete
            operation.

        Raises
        ------
        ValueError

            - If the collection is immutable.
            - If the collection is invalid before or after deletion.
            - If the index cannot be found or parsed.
        """
        if self.is_immutable:
            raise ValueError("Cannot delete from an immutable collection.")
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        try:
            index = self.index(index)
        except KeyError as e:
            if key_only:
                raise e

        if isinstance(index, int):
            del self._keys[index]
            del self._values[index]
            self._weights = np.delete(self._weights, index)
        elif isinstance(index, slice):
            del self._keys[index]
            del self._values[index]
            self._weights = np.delete(self._weights, index)

        self.check(error=error)

    def __contains__(self, item: Any) -> bool:
        """
        If a **key** or **value** is in the collection. `list-like, dict-like`

        Returns
        -------
        bool
            True if the key/value is in the collection, False otherwise.
        """
        return item in self._keys or item in self._values

    def __add__(
        self,
        other: tuple[KeyT, ValueT, float | None],
        /,
        *,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> Self:
        """
        Add a **new** item to the collection with (key, value, weight).

        Parameters
        ----------
        other : tuple[KeyT, ValueT, float]
            The (key, value, weight) to add to the collection.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use to check the collection **after** a successful add
            operation.

        Returns
        -------
        Self
            The updated collection.

        Raises
        ------
        ValueError

            - If the collection is immutable.
            - If the key already exists in the collection.
            - If the collection is invalid before or after adding.

        See Also
        --------
        __setitem__ : dict-like method to set a new item or update an existing item.
        """
        if self.is_immutable:
            raise ValueError("Cannot add to an immutable collection.")

        key, value, weight = other
        if key in self._keys:
            raise ValueError(f"Key {key!r} already exists in the collection.")
        self.__setitem__(key, (value, weight), error=error)
        return self

    def __iadd__(
        self,
        other: tuple[KeyT, ValueT, float | None],
        /,
        *,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> Self:
        """
        Same as `__add__`
        """
        return self.__add__(other, error=error)

    def __sub__(
        self,
        other: KeyT | list[KeyT],
        /,
        *,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> Self:
        """
        Remove an item or a **list** of items from the collection with key(s). A bare key cannot be
        of type list, and a list input must be a list of keys instead of a bare key.

        Parameters
        ----------
        other : KeyT | list[KeyT]
            The key or list of keys to remove from the collection. A list must be a list of keys
            instead of a single key.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use to check the collection **after** a successful remove
            operation.

        Returns
        -------
        Self
            The updated collection.

        Raises
        ------
        ValueError

            - If the collection is immutable.
            - If a key does not exist in the collection.
            - If the collection is invalid before or after removal.
        """
        if self.is_immutable:
            raise ValueError("Cannot delete from an immutable collection.")

        if isinstance(other, list):
            for key in other:
                self.__delitem__(key, key_only=True, error="ignore")
        else:
            self.__delitem__(other, key_only=True, error="ignore")
        self.check(error=error)
        return self

    def __isub__(
        self,
        other: KeyT | list[KeyT],
        /,
        *,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> Self:
        """
        Same as `__sub__`
        """
        return self.__sub__(other, error=error)

    def __len__(self) -> int:
        """
        Get the number of items in the collection. `list-like`

        Returns
        -------
        int
            The number of items in the collection.

        Raises
        ------
        ValueError
            If the collection has mismatched lengths of keys/values/weights.
        """
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")
        return len(self._keys)

    def __iter__(self) -> Generator[KeyT, None, None]:
        """
        Iterate over the keys of the items in the collection. `dict-like`

        Yields
        -------
        KeyT
            The key of the current item in the collection.
        """
        for key in self._keys:
            yield key

    def __repr__(self) -> str:
        """
        The string representation of the collection.

        Returns
        -------
        str
            The string representation of the collection.

        Raises
        ------
        ValueError
            If the collection has mismatched lengths of keys/values/weights.
        """
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")

        keys, values, weights = self._keys, self._values, self._weights
        weights = weights.round(2).tolist()
        if len(keys) > 4:
            elli = noquote_str("...")
            keys = keys[:4] + [elli]
            values = values[:4] + [elli]
            weights = weights[:4] + [elli]
        return (
            f"{self.__class__.__name__}(keys={keys!r}, values={values!r}, "
            f"weights={weights!r})"
        )

    def __reduce__(
        self,
    ) -> tuple[type[Self], tuple[list[KeyT], list[ValueT], list[float]]]:
        """
        Serialize a :class:`Collection` instance.

        Returns
        -------
        tuple[type[Self], tuple[list[KeyT], list[ValueT], list[float]]]
            The class type and the serialized data.
        """
        return (self.__class__, (self.keys, self.values, self.weights.tolist()))


class FuncUnitCollection(Collection[KeyT, FuncUnitT], Generic[KeyT, FuncUnitT]):
    """
    A collection of function units that can be selected randomly for symbolic regression.

    The keys for function unit collections are by default the `.identity` attributes of the function
    units, the values are the function units themselves, and the weights are the `.weight`
    attributes of the function units.

    In addition to the base class :class:`Collection`, this class is designed specifically for when
    the values in the collection are function units. Thus, this class also implements `add` and
    `sub` methods to manage the collection with values (function units).

    **Warning**: If your key type is `int` or `slice`, index-based access may lead to unexpected
    behavior since it can be interpreted as a key (`dict-like`) and an index/slice (`list-like`),
    especially when using `__getitem__` and `__delitem__`. Use replacement methods such as
    `set_value`, `set_weight`, `pop`, `popitem` instead.

    Subclassing
    -----------
    To specify the attribute of the function unit to use as the key in the collection, subclass this
    class and do one of the following:

    - use the `key_attr` argument at class definition time, e.g.,
        ```python
        class MyFuncUnitCollection(FuncUnitCollection, key_attr="my_custom_key"):
            pass
        ```
    - define `_key_attr` in the class body, e.g.,
        ```python
        class MyFuncUnitCollection(FuncUnitCollection):
            _key_attr = "my_custom_key"
        ```

    The first option precedes the seconds one. The `key_attr` defaults to `identity`; it must be a
    valid python identifier.

    Methods
    -------
    add : add one or more function units to the collection.
    sub : remove one or more function units from the collection.
    vselect : randomly select a function unit from the collection; or multiple function units.

    Notes
    -----
    For **type hint**, this class accepts two generic types: `KeyT` and `FuncUnitT`.

    - `KeyT`: The type of the identity property of the function units. The `_key_attr` class
        attribute is the property name used to access the identity value from the function unit.
    - `FuncUnitT`: The type of the function units themselves.

    While you can define `KeyT` and `FuncUnitT` as specific types, they are actually **dependent**.
    `KeyT` should be the return type of the `.<_key_attr>` property of a `FuncUnitT`. This is **not
    enforced** and you will **not get type warnings** if they are mismatched. You must ensure their
    compatibility yourself if you shall use custom type hints.
    """

    _key_attr: str = "identity"

    def __init_subclass__(cls, key_attr: str | None = None, **kwargs) -> None:
        """
        Initialize a subclass of FuncUnitCollection and set the custom hook of the key attribute of
        a function unit for the function units in the collection.

        Parameters
        ----------
        key_attr : str | None
            The name of the attribute to use as the key in the collection.
        """
        key_attr = key_attr or cls._key_attr
        if not key_attr.isidentifier():
            raise ValueError(
                f"Invalid property name: {key_attr!r}. Must be a valid identifier."
            )
        cls._key_attr = key_attr
        return super().__init_subclass__(**kwargs)

    @property
    def key_attr(self) -> str:
        """
        The name of the attribute to use as the key in the collection for a function unit (`value`).

        Returns
        -------
        str
            The name of the attribute to use as the key in the collection.
        """
        return self.__class__._key_attr

    def add(
        self,
        other: FuncUnitT | Iterable[FuncUnitT],
        /,
        *,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> Self:
        """
        Add one or more function units to the collection.

        Parameters
        ----------
        other : FuncUnitT | Iterable[FuncUnitT]
            The function unit(s) to add to the collection. A function unit should not be iterable,
            and thus an iterable must be an iterable of `FuncUnit` types.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use after adding the function unit(s).

        Returns
        -------
        Self
            The updated collection.

        Raises
        ------
        TypeError
            If the function unit(s) are not of the expected type.
        ValueError

            - If the collection is corrupted before or after adding the function unit(s).
            - If any provided function unit is invalid.
        """
        if isinstance(other, Iterable):
            if not all(isinstance(unit, FuncUnit) for unit in other):
                raise TypeError("Expected an iterable of `FuncUnit` types.")
            others = list(other)
        else:
            others = [other]

        for unit in others:
            _id = cast(KeyT, getattr(unit, self.key_attr))
            self.__setitem__(_id, (unit, unit.weight), error="ignore")
        self.check(error=error)
        return self

    def sub(
        self,
        other: FuncUnitT | Iterable[FuncUnitT],
        /,
        *,
        error: Literal["raise", "warn", "ignore"] = "warn",
    ) -> Self:
        """
        Remove one or more function units from the collection.

        Parameters
        ----------
        other : FuncUnitT | Iterable[FuncUnitT]
            The function unit(s) to remove from the collection. A function unit should not be
            iterable, and thus an iterable must be an iterable of `FuncUnit` types.
        error : Literal["raise", "warn", "ignore"], default="warn"
            The error handling strategy to use after removing the function unit(s).

        Returns
        -------
        Self
            The updated collection.

        Raises
        ------
        TypeError
            If the function unit(s) are not of the expected type.
        ValueError

            - If the collection is corrupted before or after removing the function unit(s).
            - If any provided function unit is invalid.
        """
        if isinstance(other, Iterable):
            if not all(isinstance(unit, FuncUnit) for unit in other):
                raise TypeError("Expected an iterable of `FuncUnit` types.")
            others = list(other)
        else:
            others = [other]

        for unit in others:
            _id = cast(KeyT, getattr(unit, self.key_attr))
            self.__delitem__(_id, error="ignore")
        self.check(error=error)
        return self

    @overload
    def vselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: None = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitT: ...
    @overload
    def vselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: int,
        replace: bool = True,
        copy: bool = True,
    ) -> list[FuncUnitT]: ...

    def vselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: None | int = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitT | list[FuncUnitT]:
        """
        Randomly select an item from the collection and return (a copy of) its `value`, or multiple
        items and their (copies of) values. The weights are used to weight the probability.

        Parameters
        ----------
        seed : RngGeneratorSeed, optional
            Random number generator seed. See `numpy.random.default_rng` for more information.
        slicing : slice, default=slice(None)
            A slice object to specify which items to consider for selection.
        size : int | None, default=None
            The number of items to select. This is analogous to the `size` parameter in
            `numpy.random.Generator.choice`.

            - If None, a single item will be selected and returned; the elements in the returned
              tuple will be for a single item.
            - If `size` is specified, multiple items will be selected and returned; the elements
              in the returned tuple will be an iterable of the selected items, even when `size=1`.

        replace : bool, default=True
            Whether to replace the selected items in the collection when selecting multiple items.
            Only applicable when `size` is specified and larger than 1.
        copy : bool, default=True
            Whether to return a copy of the selected item. When using a function unit to build a
            :class:`psr.expression.Expression` in the symbolic regression pipeline, it is
            recommended to always use a copy of a function unit to construct a node to avoid
            cross-referencing issues.

        Returns
        -------
        FuncUnitT | list[FuncUnitT]
            The selected item(s) or a copy of it/them.

        Raises
        ------
        ValueError

            - If the collection is invalid (mismatched lengths, invalid weights, empty, etc.)
            - If the collection is empty after slicing.
            - If the provided `size` is not larger than 0.

        See Also
        --------
        select : method to select an item and return its (key, value, weight); or multiple items.
        """
        if size is None:
            val = self.select(seed, slicing=slicing)[1]
            return val.copy() if copy else val

        val = self.select(seed, slicing=slicing, size=size, replace=replace)[1]
        return [v.copy() if copy else v for v in val]


class OperationCollection(
    FuncUnitCollection[str, Operation[ArrayLikeT]], Generic[ArrayLikeT], key_attr="name"
):
    """
    A collection of mathematical operations that can be selected randomly for symbolic regression.

    A collection of operations has the following properties:

    - `keys`: the `name` property of each operation.
    - `values`: the `Operation` instances themselves.
    - `weights`: the relative weights of each operation (default to the `weight` property of each
      operation).
    """

    def express_add(
        self,
        names: OperationOptions | Sequence[OperationOptions] | None = None,
        **kwargs: Any,
    ) -> Self:
        """
        Express addition of operations with :func:`psr.func_unit.get_operations`.

        Parameters
        ----------
        names : OperationOptions | Sequence[OperationOptions] | None, default=None
            The names of the operations to add. If None, all operations are added. The operations
            must be unique from existing operations in the collection and from each other.
        **kwargs : Any
            Additional keyword arguments to pass to :func:`psr.func_unit.get_operations`.

        Returns
        -------
        Self
            The updated collection.

        See Also
        --------
        psr.func_unit.get_operations : function to retrieve operations.
        """
        ops = get_operations(names=names, **kwargs)
        ops = cast(Operation[ArrayLikeT] | list[Operation[ArrayLikeT]], ops)
        return self.add(ops)


class VariableCollection(
    FuncUnitCollection[int, Variable[ArrayLikeT]], Generic[ArrayLikeT], key_attr="index"
):
    """
    A collection of variables that can be selected randomly for symbolic regression.

    A collection of variables has the following properties:

    - `keys`: the `index` property of each variable.
    - `values`: the `Variable` instances themselves.
    - `weights`: the relative weights of each variable (default to the `weight` property of each
      variable).

    **Warning**: If your key type is `int` or `slice`, index-based access may lead to unexpected
    behavior since it can be interpreted as a key (`dict-like`) and an index/slice (`list-like`),
    especially when using `__getitem__` and `__delitem__`. Use replacement methods such as
    `set_value`, `set_weight`, `pop`, `popitem` instead.
    """

    def express_add(
        self,
        indices: int | Sequence[int],
        **kwargs: Any,
    ) -> None:
        """
        Express addition of variables with :func:`psr.func_unit.get_variables`.

        Parameters
        ----------
        indices : int | Sequence[int]
            The max index or indices of the variables to retrieve.

            - `int`: The number of variables to retrieve/initialize. The indices will be [0, 1, ...,
              n-1]. This should be the number of features to expect in the input data `X`.
            - `Sequence[int]`: A specific list of indices to retrieve. Should be a subset of [0, 1,
              ..., n-1], where `n` is the number of features to expect in the input data `X`.

            The parsed variables will be added to the collection. They must be unique from existing
            variables in the collection and from each other.
        **kwargs : Any
            Additional keyword arguments to pass to :func:`psr.func_unit.get_variables`.

        See Also
        --------
        psr.func_unit.get_variables : function to retrieve variables.
        """
        vars = get_variables(indices=indices, **kwargs)
        vars = cast(Variable[ArrayLikeT] | list[Variable[ArrayLikeT]], vars)
        self.add(vars)

    def cap(self, n_features: int, /) -> None:
        """
        Regulate the variables in the collection such that it only contains
        :class:`psr.func_unit.Variable` instances with indices from `0` to `<n_features> - 1`.

        This is used in :func:`psr.psr.ParametricSR.fit` to set the variables available for fitting.

        Parameters
        ----------
        n_features : int
            The number of features to keep in the collection. This should be the number of features
            to expect in the input data `X`.

        Raises
        ------
        ValueError
            If the number of features is invalid.
        """
        if n_features <= 0:
            raise ValueError("Invalid number of features.")
        self.clear("ignore")
        self.express_add(n_features)


class ConstantCollection(
    FuncUnitCollection[Number, Constant[ArrayLikeT]],
    Generic[ArrayLikeT],
    key_attr="value",
):
    """
    A collection of constants that can be selected randomly for symbolic regression.

    A collection of constants has the following properties:

    - `keys`: the `value` property of each constant.
    - `values`: the `Constant` instances themselves.
    - `weights`: the relative weights of each constant (default to the `weight` property of each
      constant).

    **Warning**: If your key type is `int` or `slice`, index-based access may lead to unexpected
    behavior since it can be interpreted as a key (`dict-like`) and an index/slice (`list-like`),
    especially when using `__getitem__` and `__delitem__`. Use replacement methods such as
    `set_value`, `set_weight`, `pop`, `popitem` instead.
    """

    def express_add(
        self,
        values: Number | Sequence[Number] = (-3, -2, -1, 1, 2, 3),
        **kwargs: Any,
    ) -> Self:
        """
        Express addition of constants with :func:`psr.func_unit.get_constants`.

        Parameters
        ----------
        values : Number | Sequence[Number], default (-3, -2, -1, 1, 2, 3)
            The value(s) of the constants(s) to retrieve/initalize. The parsed constants will be
            added to the collection. They must be unique from existing constants in the collection
            and from each other.
        **kwargs : Any
            Additional keyword arguments to pass to :func:`psr.func_unit.get_constants`.

        Returns
        -------
        Self
            The updated collection.

        See Also
        --------
        psr.func_unit.get_constants : function to retrieve constants.
        """
        consts = get_constants(values=values, **kwargs)
        consts = cast(Constant[ArrayLikeT] | list[Constant[ArrayLikeT]], consts)
        return self.add(consts)


class DelayedConstantCollection(
    FuncUnitCollection[str, DelayedConstant[ArrayLikeT]],
    Generic[ArrayLikeT],
    key_attr="prefix",
):
    """
    A collection of delayed constants that can be selected randomly for symbolic regression.

    A collection of delayed constants has the following properties:

    - `keys`: the `prefix` property of each delayed constant (class).
    - `values`: the `DelayedConstant` instances themselves.
    - `weights`: the relative weights of each delayed constant (default to the `weight` property of
      each delayed constant).
    """

    def express_add(
        self,
        prefixes: DelayedConstantOptions | SequenceOfDelayedConstantOptions = "C",
        **kwargs: Any,
    ) -> Self:
        """
        Express addition of delayed constants with :func:`psr.func_unit.get_delayed_constants`.

        Parameters
        ----------
        prefixes : DelayedConstantOptions | SequenceOfDelayedConstantOptions, default "C"
            The prefix(es) of the delayed constant(s) to retrieve/initalize. The parsed delayed
            constants will be added to the collection. They must be unique from existing delayed
            constants in the collection and from each other.
        **kwargs : Any
            Additional keyword arguments to pass to :func:`psr.func_unit.get_delayed_constants`.

        Returns
        -------
        Self
            The updated collection.

        See Also
        --------
        psr.func_unit.get_delayed_constants : function to retrieve delayed constants.
        """
        dconsts = get_delayed_constants(prefixes=prefixes, **kwargs)
        dconsts = cast(
            DelayedConstant[ArrayLikeT] | list[DelayedConstant[ArrayLikeT]], dconsts
        )
        return self.add(dconsts)

    def sync(self) -> None:
        """
        Synchronize the collection with the current state of the function units in the environment.

        This method updates the collection to reflect any changes made to the underlying delayed
        constants, typically after an inplace environment update happened with
        :func:`psr.config.Config.inplace_update`.
        """
        for key, value in zip(self._keys, self._values):
            if (cls := value.get(prefix=key)) and issubclass(cls, DelayedConstant):
                self.set_value(key, cls(), key_only=True)


class PSRCollection(
    Collection[PSRCollectionOptions, FuncUnitCollection[str | Number, FuncUnitTypes]],
    Generic[ArrayLikeT],
    immutable=True,
):
    """
    A collection of [function unit collections] for parametric symbolic regression.

    This collection is structured with the following attributes:

    - `keys`: the names of the collections. This should a list of 4 immutable elements:

        - "operations": `arity >= 1`
        - <<<<<<<< `arity_sep` >>>>>>>>
        - "variables": `arity = 0`
        - "constants": `arity = 0`
        - "delayed_constants": `arity = 0`

    - `values`: the function unit collections themselves, in the same order as the keys.
    - `weights`: the relative weights of each collection (default to uniform weights).

    By default, a PSRCollection should be immutable and maintains exactly the same structure as the
    above description with the 4 keys. A `arity_sep` property is included to separate function unit
    collections with a positive arity (`[0:arity_sep]`) and no arity (`[arity_sep:]`). If you have
    to mutate an instantiated PSRCollection:

    1. use the `mutate` context manager to enter mutation mode.
    2. use the `insert` method to add new function unit collections, the `popitem` method to remove
       a collection by its index, or the `pop` method to remove a collection by its key.
    3. update the `arity_sep` property to reflect the new structure; collections with positive
       arities should be before the separator (`[0:arity_sep]`), and those with zero arities should
       be after (`[arity_sep:]`).

    Attributes
    ----------
    operations, variables, constants, delayed_constants : the collection of each function type
    arity_sep : int, the index separating function units with positive arity from those with zero
        arity

    Methods
    -------
    iselect : randomly select 1) one or more function unit collections, and 2) one function unit
        from each
    nselect : `iselect` but only from function unit collections with no arity (zero arity)
    pselect : `iselect` but only from function unit collections with positive arity
    """

    def __init__(
        self,
        operations: Collection[str, Operation[ArrayLikeT]] | None = None,
        variables: Collection[int, Variable[ArrayLikeT]] | None = None,
        constants: Collection[Number, Constant[ArrayLikeT]] | None = None,
        delayed_constants: Collection[str, DelayedConstant[ArrayLikeT]] | None = None,
        weights: Sequence[float] | None = (1.0, 1.0, 1.0, 0.75),
        arity_sep: int = 1,
        *args: Any,
    ) -> None:
        """
        Initialize the PSRCollection with operations, variables, constants, and delayed constants.

        Parameters
        ----------
        operations : Collection[str, Operation[ArrayLikeT]] | None
            The collection of operations to include in the PSRCollection. If None, the default
            collection will be used, which includes (arity shown in the brackets):
            > add[2], sub[2], mul[2], div[2], square[1], pow[2], neg[1], abs[1], inv[1], log[1],
            exp[1], sqrt[1], sin[1], cos[1]
        variables : Collection[int, Variable[ArrayLikeT]] | None
            The collection of variables to include in the PSRCollection. If None, an empty
            collection will be used; use the `self.variables.add` method with
            :func:`psr.func_unit.get_variables` to add variables dynamically at runtime,
            corresponding to your input data X. You can also use `self.variables.express_add` to add
            variables in bulk.
        constants : Collection[Number, Constant[ArrayLikeT]] | None
            The collection of constants to include in the PSRCollection. If None, the default
            collection will be used, which includes:
            > -3, -2, -1, 1, 2, 3
        delayed_constants : Collection[str, DelayedConstant[ArrayLikeT]] | None
            The collection of delayed constants to include in the PSRCollection. If None, the
            default collection will be used, which only include a delayed constant with initial
            guess of 0 and bounds of [None, None] (no bounds).
        weights : Sequence[float] | None, default=(1.0, 1.0, 1.0, 0.5)
            The relative weights of each collection (default to uniform weights but with lower
            weight for delayed constants).
        arity_sep : int, default=1
            The index separating function units with positive arity from those with zero arity.
            For example, in the collection, there are [Operation, Variables, Constant,
            DelayedConstant]; only `Operation` has positive arity, hence the separator index of `1`.
        *args : Any, **not used**
            Additional positional arguments to pass to the constructor. This is added for better
            serialization/deserialization support between different package versions.
        """
        keys: list[PSRCollectionOptions] = [
            "operations",
            "variables",
            "constants",
            "delayed_constants",
        ]

        if operations is None:
            operations = OperationCollection().express_add()
        if variables is None:
            variables = VariableCollection()
        if constants is None:
            constants = ConstantCollection().express_add()
        if delayed_constants is None:
            delayed_constants = DelayedConstantCollection().express_add()

        values = [operations, variables, constants, delayed_constants]

        super().__init__(keys, values, weights=weights, empty=False)
        self.arity_sep = arity_sep

    @property
    def arity_sep(self) -> int:
        """
        Returns the arity separator index value. Function unit collections with positive arity
        should be before this index (`[0:self.arity_sep)`), and those with zero arity should be
        after it (`[self.arity_sep:]`).

        Returns
        -------
            int: The arity separator value.
        """
        return self._arity_sep

    @arity_sep.setter
    def arity_sep(self, value: int) -> None:
        """
        ## Property Setter
        Sets the arity separator index for the collection.

        Raises
        ------
        ValueError

            - If the collection is immutable
            - If the collection has mismatched lengths
            - If the arity separator index out of bounds
            - If the arity separator index is incorrect: it does not correctly separate function
            units with positive arity from those with zero arity

        See Also
        --------
        mutate : context manager to temporarily allow mutation of the collection.
        """

        if self.is_immutable and hasattr(self, "_arity_sep"):
            raise ValueError(
                "Cannot modify the arity separator index of an immutable collection"
            )
        if not self.has_equal_len:
            raise ValueError("Collection has mismatched lengths.")
        if value < 0 or value > len(self._keys):
            raise ValueError("Arity separator index out of bounds")

        for i, col in enumerate(self.values):
            checker = lambda x: x > 0 if i < value else x == 0
            if not all(checker(func_unit.arity) for func_unit in col.values):
                raise ValueError("Incorrect arity separator index")

        self._arity_sep = value

    @property
    def operations(self) -> OperationCollection[ArrayLikeT]:
        """
        The collection for operations.

        Returns
        -------
        OperationCollection[ArrayLikeT]
            The operations collection.
        """
        val = self["operations"][1]
        val = cast(OperationCollection[ArrayLikeT], val)
        return val

    @property
    def variables(self) -> VariableCollection[ArrayLikeT]:
        """
        The collection for variables.

        Returns
        -------
        VariableCollection[ArrayLikeT]
            The variables collection.
        """
        val = self["variables"][1]
        val = cast(VariableCollection[ArrayLikeT], val)
        return val

    @property
    def constants(self) -> ConstantCollection[ArrayLikeT]:
        """
        The collection for constants.

        Returns
        -------
        ConstantCollection[ArrayLikeT]
            The constants collection.
        """
        val = self["constants"][1]
        val = cast(ConstantCollection[ArrayLikeT], val)
        return val

    @property
    def delayed_constants(self) -> DelayedConstantCollection[ArrayLikeT]:
        """
        The collection for delayed constants.

        Returns
        -------
        DelayedConstantCollection[ArrayLikeT]
            The delayed constants collection.
        """
        val = self["delayed_constants"][1]
        val = cast(DelayedConstantCollection[ArrayLikeT], val)
        return val

    @overload
    def iselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: None = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitTypes: ...
    @overload
    def iselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: int,
        replace: bool = True,
        copy: bool = True,
    ) -> list[FuncUnitTypes]: ...

    def iselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        slicing: slice = slice(None),
        size: None | int = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitTypes | list[FuncUnitTypes]:
        """
        Un**i**t selection. First select a function unit collection, and then select a function unit
        from the selected collection. Or first select multiple function unit collections, and then
        select one function unit from each.

        Parameters
        ----------
        seed : RngGeneratorSeed, default=None
            The random seed to use for selection.
        slicing : slice, default=slice(None)
            The slicing to apply to the selection of a function unit collection. By default, all
            collections are considered.
        size : int | None, default=None
            The number of items to select. This is analogous to the `size` parameter in
            `numpy.random.Generator.choice`.
            - If None, a single item will be selected and returned; the elements in the returned
            tuple will be for a single item.
            - If `size` is specified, multiple items will be selected and returned; the elements
            in the returned tuple will be an iterable of the selected items, even when `size=1`.
        replace : bool, default=True
            Whether to replace the selected items in the collection when selecting multiple items.
            Only applicable when `size` is specified and larger than 1.
        copy : bool, default=True
            Whether to create a copy of the selected function unit. By default, this is set to True
            because when building a :class:`psr.expression.Expression` tree, the node values should
            not be cross-referenced in different parts of the tree or different trees.

        Returns
        -------
        FuncUnitTypes | list[FuncUnitTypes]
            The (copy of the) selected function unit(s).

        See Also
        --------
        nselect : selection of a function unit with no arity (zero arity).
        pselect : selection of a function unit with a positive arity.
        """
        rng = np.random.default_rng(seed)
        if size is None:
            func_col = self.select(rng, slicing=slicing)[1]
            return func_col.vselect(rng, copy=copy)

        func_cols = self.select(rng, slicing=slicing, size=size, replace=replace)[1]

        col_type_dict: dict[int, FuncUnitCollection[str | Number, FuncUnitTypes]] = {}
        col_type_counts: dict[int, int] = defaultdict(int)
        for col in func_cols:
            _id = id(col)
            col_type_counts[_id] += 1
            col_type_dict[_id] = col

        selections: list[FuncUnitTypes] = []
        for _id, count in col_type_counts.items():
            col = col_type_dict[_id]
            if count < 2:
                selections.append(col.vselect(rng, copy=copy))
                continue
            selections.extend(col.vselect(rng, size=count, replace=replace, copy=copy))

        assert (
            len(selections) == size
        ), f"Expected {size} selections, but got {len(selections)}"
        return selections

    @overload
    def nselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        size: None = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitTypes: ...
    @overload
    def nselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        size: int,
        replace: bool = True,
        copy: bool = True,
    ) -> list[FuncUnitTypes]: ...

    def nselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        size: None | int = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitTypes | list[FuncUnitTypes]:
        """
        Selection of a function unit with no arity (zero arity).

        Parameters
        ----------
        seed : RngGeneratorSeed, default=None
            The random seed to use for selection.
        size : int | None, default=None
            The number of items to select. This is analogous to the `size` parameter in
            `numpy.random.Generator.choice`.

            - If None, a single item will be selected and returned; the elements in the returned
              tuple will be for a single item.
            - If `size` is specified, multiple items will be selected and returned; the elements
              in the returned tuple will be an iterable of the selected items, even when `size=1`.

        replace : bool, default=True
            Whether to replace the selected items in the collection when selecting multiple items.
            Only applicable when `size` is specified and larger than 1.
        copy : bool, default=True
            Whether to create a copy of the selected function unit. By default, this is set to True
            because when building a :class:`psr.expression.Expression` tree, the node values should
            not be cross-referenced in different parts of the tree or different trees.

        Returns
        -------
        FuncUnitTypes | list[FuncUnitTypes]
            The (copy of the) selected function unit(s).

        See Also
        --------
        iselect : selection of a function unit with any arity.
        pselect : selection of a function unit with a positive arity.
        """
        return self.iselect(
            seed,
            slicing=slice(self.arity_sep, None),
            size=size,
            replace=replace,
            copy=copy,
        )

    @overload
    def pselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        size: None = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitTypes: ...
    @overload
    def pselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        size: int,
        replace: bool = True,
        copy: bool = True,
    ) -> list[FuncUnitTypes]: ...

    def pselect(
        self,
        seed: RngGeneratorSeed = None,
        /,
        *,
        size: None | int = None,
        replace: bool = True,
        copy: bool = True,
    ) -> FuncUnitTypes | list[FuncUnitTypes]:
        """
        Selection of a function unit with a positive arity.

        Parameters
        ----------
        seed : RngGeneratorSeed, default=None
            The random seed to use for selection.
        size : int | None, default=None
            The number of items to select. This is analogous to the `size` parameter in
            `numpy.random.Generator.choice`.

            - If None, a single item will be selected and returned; the elements in the returned
              tuple will be for a single item.
            - If `size` is specified, multiple items will be selected and returned; the elements
              in the returned tuple will be an iterable of the selected items, even when `size=1`.

        replace : bool, default=True
            Whether to replace the selected items in the collection when selecting multiple items.
            Only applicable when `size` is specified and larger than 1.
        copy : bool, default=True
            Whether to create a copy of the selected function unit. By default, this is set to True
            because when building a :class:`psr.expression.Expression` tree, the node values should
            not be cross-referenced in different parts of the tree or different trees.

        Returns
        -------
        FuncUnitTypes | list[FuncUnitTypes]
            The (copy of the) selected function unit(s).

        See Also
        --------
        iselect : selection of a function unit with any arity.
        nselect : selection of a function unit with no arity (zero arity).
        """
        return self.iselect(
            seed,
            slicing=slice(0, self.arity_sep),
            size=size,
            replace=replace,
            copy=copy,
        )

    def sync(self) -> None:
        """
        Synchronize the collection with the current state of the function units in the environment.

        This method updates the collection to reflect any changes made to the underlying delayed
        constants, typically after an inplace environment update happened with
        :func:`psr.config.Config.inplace_update`.
        """
        self.delayed_constants.sync()

    def __reduce__(self) -> tuple[type[Self], tuple[Any, ...]]:
        """
        Serialize the object for pickling.

        Returns
        -------
        tuple[type[Self], tuple[Any, ...]]
            The class and the serialized data.
        """
        return (self.__class__, (*self.values, self.weights.tolist(), self.arity_sep))
