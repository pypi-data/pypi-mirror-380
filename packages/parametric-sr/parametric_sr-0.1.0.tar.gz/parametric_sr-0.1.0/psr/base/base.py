from abc import ABC, abstractmethod
from typing import (
    Any,
    Final,
    Generic,
    Literal,
    MutableMapping,
    Optional,
    Self,
    final,
    overload,
)
from weakref import WeakValueDictionary

from ..typing import HashableT, T


class _Missing:
    """
    Marker class for missing values.
    """

    @final
    def __bool__(self) -> bool:
        return False


_missing: Final[_Missing] = _Missing()


class InstanceRegistry(Generic[HashableT], ABC):
    """
    A base class for registering, tracking, and managing instances of a class. A class attribute
    `_instances` is used to store all instances of the class, keyed by specified hashable keys from
    the `key` property of an instance, and valued by the instances themselves.

    Attributes
    ----------
    _instances : dict[Hashable, Self], `class-level`
        A class-level dictionary that stores instances of the class, keyed by their `key` property.
        Do not access this dictionary directly; use the provided methods to interact with class
        instance registry.
    key : Hashable, `instance-level`
        The key to identify the instance within the registry.

    Subclassing
    -----------
    This class is designed to be subclassed. When creating a subclass, you must override the `key`
    property to provide a unique identifier for each instance. The `key` should be hashable and try
    not to use `None` as a key.

    Additionally, you can provide a `weakref` argument when creating a subclass. Use:

    - `weakref=True` to use a `WeakValueDictionary` for the instance registry.
    - `weakref=False` to use a regular dictionary for the instance registry.
    - `weakref=None` to use the default behavior from the class body definition of `_instances`.

    See Also
    --------
    get_all_instances : class method to get all instances in the registry.
    get_instance : class method to get an instance by key.
    has_instance : class method to check if a key/instance exists in the registry.
    add_instance : class method to add an instance to the registry.
    remove_instance : class method to remove an instance from the registry.
    remove_all_instances : class method to remove all instances from the registry.
    rename_instance : class method to rename an instance in the registry.
    sync_registry : class method to synchronize the keys in the registry with the instances.
    """

    _instances: MutableMapping[HashableT, Self] = {}

    def __init_subclass__(cls, weakref: bool | None = None, **kwargs: Any) -> None:
        """
        subclassing hook to create a new instance registry (`dict`) for each subclass.

        Parameters
        ----------
        weakref : bool | None
            Whether to use a weak reference dictionary for the instance registry.

            - `None`: Use the default behavior from the class body definition of `_instances`.
            - `True`: Use a `WeakValueDictionary` for the instance registry.
            - `False`: Use a regular dictionary for the instance registry.
        """
        if weakref is None:
            cls._instances = type(cls._instances)()
        elif weakref:
            cls._instances = WeakValueDictionary()
        else:
            cls._instances = {}
        super().__init_subclass__(**kwargs)

    @property
    @abstractmethod
    def key(self) -> HashableT:
        """
        The key to represent the instance within the registry. While this is not enforced at the
        runtime, you **must** update the registry with the class method `rename_instance` if the key
        property of the instance is changed. Otherwise, there will be inconsistencies.

        Subclassing
        -----------
        This property must be overridden in subclasses to provide a custom key.

        Returns
        -------
        HashableT
            The key to represent the instance within the registry.

        See Also
        --------
        rename_instance : method for renaming an instance.
        remove_instance : method for deleting instances.
        __del__ : method for deleting instances.
        """
        raise NotImplementedError

    @classmethod
    def get_all_instances(
        cls,
    ) -> MutableMapping[HashableT, Self]:
        """
        Get all instances in the registry.

        **Warning**: This method returns the original class-level dictionary of instances. You
        should **not** modify this dictionary directly, as it may lead to unexpected behavior.

        Returns
        -------
        MutableMapping[HashableT, Self]
            A dictionary containing all instances in the registry, where the values are the
            instances themselves.
        """
        return cls._instances

    @classmethod
    @overload
    def get_instance(cls, key: HashableT, default: Self, /) -> Self: ...
    @classmethod
    @overload
    def get_instance(
        cls, key: HashableT, default: Optional[T] = None, /
    ) -> Self | T | None: ...

    @classmethod
    def get_instance(
        cls, key: HashableT, default: Optional[T] = None, /
    ) -> Self | T | None:
        """
        Get an instance with a key.

        Parameters
        ----------
        key : HashableT
            The key to represent the instance within the registry.
        default : Self | Any, optional
            The default value to return if the key does not exist.

        Returns
        -------
        Self | T | None
            The instance if the key exists, otherwise the default value.
        """
        return cls._instances.get(key, default)

    @classmethod
    @overload
    def has_instance(
        cls, key: HashableT, value: Self | _Missing = _missing, /
    ) -> bool: ...
    @classmethod
    @overload
    def has_instance(cls, key: HashableT, value: Any, /) -> Literal[False]: ...

    @classmethod
    def has_instance(cls, key: HashableT, value: Self | Any = _missing, /) -> bool:
        """
        Check if an instance with the given key (and value) exists in the class registry.

        Parameters
        ----------
        key : HashableT
            The key of the instance.
        value : Self | Any, optional
            The exact instance to check for existence. If provided, both the key and value/instance
            must match for this to return True.

        Returns
        -------
        bool
            True if the key exists (and the instance under that key matches the provided value).
        """
        if value is _missing:
            return key in cls._instances
        return cls._instances.get(key, _missing) is value

    @classmethod
    def add_instance(
        cls,
        key: HashableT,
        instance: Self,
        /,
        *,
        check_key_mismatch: bool = True,
        overwrite: bool = False,
    ) -> None:
        """
        Add an instance to the class-level instance regictry (`dict`).

        Parameters
        ----------
        key : HashableT
            The key to represent the instance within the registry.
        instance : Self
            The instance to add. Its `key` property must match the `key` parameter.
        check_key_mismatch : bool, default=True
            Whether to check if the `key` parameter matches the `key` property of the instance.
            If True, a ValueError will be raised if they do not match.
        overwrite : bool, default=False (keyword-only)
            Whether to overwrite an existing instance with the same key. If False and a different
            instance with the same key already exists, a ValueError will be raised.

        Raises
        ------
        ValueError
            - If an instance with the same key already exists and `overwrite` is False.
            - If `check_key_mismatch` and the instance's key does not match the provided key.
        """
        if not overwrite and instance is not cls.get_instance(key, instance):
            raise ValueError(
                f"`{cls.__name__}` instance with the key {key!r} already exists. "
                "Use `overwrite=True` to overwrite the existing instance."
            )
        if check_key_mismatch and instance.key != key:
            raise ValueError(f"Key mismatch: {instance.key!r} != {key!r}")
        cls._instances[key] = instance

    @classmethod
    def remove_instance(
        cls,
        key: HashableT,
        value: Self | Any = _missing,
        /,
        *,
        error: Literal["raise", "ignore"] = "raise",
    ) -> None:
        """
        Remove an instance from the class-level instance regictry (`dict`).

        Parameters
        ----------
        key : Hashable
            The key to be removed and its corresponding instance.
        value : Self | None, optional
            The value (instance) to be removed. If None, the key is used to find the instance to
            remove. If provided, both the `key` and `value` must match an existing instance for
            removal to succeed.
        error : Literal["raise", "ignore"], default="raise"
            The error handling strategy when no match is found with the key (and the value). If
            "raise", a KeyError will be raised. If "ignore", no action will be taken.

        Raises
        ------
        KeyError
            If `error` is "raise", and one of the follow errors happens:
            - the specified key does not exist.
            - the key exists, but its corresponding value **is** not the provided instance.
        """
        if not key in cls._instances:
            if error == "raise":
                raise KeyError(
                    f"Key {key!r} does not exist in {cls.__name__} instances."
                )
            return

        if value is not _missing and value is not cls._instances[key]:
            if error == "raise":
                raise KeyError(
                    f"Key {key!r} exists, but its corresponding value "
                    "is not the provided instance (not the same object)."
                )
            return

        del cls._instances[key]

    @classmethod
    def remove_all_instances(cls) -> None:
        """
        Remove all instances from the class-level instance regictry (`dict`).

        **Danger**: This operation will remove all instances without any confirmation.
        """
        cls._instances.clear()

    @classmethod
    def rename_instance(cls, old_key: HashableT, new_key: HashableT, /) -> None:
        """
        Rename an existing instance and update its key in the instance registry.

        **Danger**: this operation may break references to the instance and the class registry.
        Make sure the instance stored under the `old_key` has a `key` property equal to your
        `new_key`.

        Parameters
        ----------
        old_key : HashableT
            The old key of the instance.
        new_key : HashableT
            The new key to use for the instance.

        Raises
        ------
        KeyError
            If the `old_key` does not exist.
        ValueError
            If a different instance with the `new_key` already exists.
        """
        if old_key == new_key:
            return

        obj = object()
        old_value = cls.get_instance(old_key, obj)
        if old_value is obj:
            raise KeyError(
                f"{cls.__name__} instance with the key {old_key!r} does not exist."
            )

        new_value = cls.get_instance(new_key, obj)
        if new_value is not obj and new_value is not old_value:
            raise ValueError(
                f"A different instance {cls.__name__} with the key {new_key!r} already "
                "exists. Remove it first to proceed."
            )

        cls._instances[new_key] = cls._instances.pop(old_key)

    @classmethod
    def sync_registry(cls) -> None:
        """
        Sync the registry such that the `key` of an instance is the `key` property of the instance.
        This method will update the registry to ensure that the keys are consistent with the
        instance properties.

        Raises
        ------
        ValueError
            If the instances have conflicting keys.
        """
        set_: set[HashableT] = set()
        for k in cls._instances.keys():
            if k in set_:
                raise ValueError(
                    f"Duplicate key {k!r} found in {cls.__name__} instances. "
                    "Ensure that each instance has a unique key."
                )
            set_.add(k)

        _instances = type(cls._instances)()
        for val in cls._instances.values():
            _instances[val.key] = val
        cls._instances = _instances

    def register(self, overwrite: bool = False) -> None:
        """
        Register the current instance in the class-level instance registry (`dict`).

        This method will add the instance to the registry, allowing it to be retrieved later using
        it key.

        Parameters
        ----------
        overwrite : bool, default=False
            Whether to overwrite an existing instance with the same key.

        Raises
        ------
        ValueError
            If a different instance with the same key already exists in the registry.
        """
        self.__class__.add_instance(self.key, self, overwrite=overwrite)


class WeakInstanceRegistry(InstanceRegistry[HashableT], weakref=True):
    """
    :class:`InstanceRegistry` that uses weak references to store instances. When the reference count
    for an instance drops to zero, the instance will be automatically removed from the registry.
    """

    _instances = WeakValueDictionary()

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """
        subclassing hook to create a new instance registry (`dict`) for each subclass.
        """
        cls._instances = WeakValueDictionary()
        super().__init_subclass__(**kwargs)
