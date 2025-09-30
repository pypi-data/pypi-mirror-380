"""
configuration for the parametric symbolic regression (PSR) package.
"""

from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import ClassVar, Generator

from .typing import NumpyErrState


@dataclass
class Config:
    """
    Configuration for the PSR package.
    """

    # class variables to control the PSR environment
    _context_lock: ClassVar[bool] = False  # to prevent nested context managers
    _inplace_update: ClassVar[bool] = False  # see `inplace_update()`
    _allow_singleton: ClassVar[bool] = True  # see `sandbox()`
    _multiprocessing: ClassVar[bool] = False  # see `multiprocess()`

    # numpy error state for when evaluating an :class:`psr.expression.Expression`
    np_errstate: NumpyErrState = field(default_factory=lambda: {"all": "ignore"})

    # random noise level for the initial guess of a DelayedConstant
    initial_guess_noise_scale: float | None = 1.0

    @property
    def allow_singleton_(self) -> bool:
        """
        Whether to allow singleton instances in the PSR environment. Default is `True`.

        See Also
        --------
        sandbox : Context manager for sandboxing the imports and disallow singleton instances.
        """
        return self.__class__._allow_singleton

    @classmethod
    @contextmanager
    def sandbox(cls) -> Generator[None, None, None]:
        """
        Context manager for sandboxing the PSR environment.

        This can be used to import/deserialize a singleton :class:`~psr.base.func_unit.FunctionUnit`
        instance and avoid skipped import due to a *cache* hit in the :class:`~psr.base.base.InstanceRegistry`.

        This guarantees the imported instance is imported as a new instance, and not the cached one.
        And the existing instances are not affected.

        **Note**: Use the :func:`sandbox` context manager for importing a single
        :class:`~psr.base.func_unit.FunctionUnit` instance at a time **only**. Do not attempt to use
        this context manager to deserialize an object with multiple :class:`~psr.base.func_unit.FunctionUnit`
        instances. Use the :func:`inplace_update` context manager, instead.

        See Also
        --------
        inplace_update : Context manager for enabling inplace updates in the PSR environment.
        """
        if cls._context_lock:
            raise RuntimeError(
                "Cannot enter sandbox mode while context is locked. "
                "Nested context managers are not allowed."
            )

        try:
            cls._context_lock = True
            cls._allow_singleton = False
            yield
        finally:
            cls._context_lock = False
            cls._allow_singleton = True

    @property
    def inplace_update_(self) -> bool:
        """
        Whether to enforce inplace update to existing :class:`~psr.base.func_unit.FuncUnit`
        instances. Default is `False`.

        See Also
        --------
        inplace_update : Context manager for enabling inplace updates in the PSR environment.
        """
        return self.__class__._inplace_update

    @classmethod
    @contextmanager
    def inplace_update(cls) -> Generator[None, None, None]:
        """
        Context manager for enabling inplace updates in the PSR environment.

        This can be used to import/deserialize a singleton :class:`~psr.base.func_unit.FunctionUnit`
        instance and use the imported instance to perform in-place updates to existing function
        units. In other words, any existing instances that conflict with the imported one are
        updated inplace to match the imported instance. If inplace updates are not feasible, the
        existing ones may be removed.

        This can be used to sync the current function unit collection (the PSR environment) with
        a previously saved collection. For example, if you have a serialized :class:`~psr.psr.ParametricSR`
        or any instance containing :class:`~psr.collection.PSRCollection` or :class:`~psr.collection.FuncUnitCollection`,
        you can use this context manager for deserialization and sync the current environment with
        the imported one (instead of forcing the imports to comply with the current environment).

        See Also
        --------
        sandbox : Context manager for sandboxing the imports.
        """
        if cls._context_lock:
            raise RuntimeError(
                "Cannot enable inplace update while context is locked. "
                "Nested context managers are not allowed."
            )

        try:
            cls._context_lock = True
            cls._inplace_update = True
            yield
        finally:
            cls._context_lock = False
            cls._inplace_update = False

    @property
    def multiprocessing_(self) -> bool:
        """
        Whether to enable multiprocessing in the PSR environment to use simplified serialization
        methods. Default is `False`.

        See Also
        --------
        multiprocessing : Context manager for enabling multiprocessing in the PSR environment.
        """
        return self.__class__._multiprocessing

    @classmethod
    @contextmanager
    def multiprocessing(cls) -> Generator[None, None, None]:
        """
        Context manager for enabling multiprocessing in the PSR environment.

        In multiprocessing, objects are serialized and deserialized across process boundaries. This
        can create overhead and potential performance issues. This context manager can be used to
        inform certain objects to use simplified serialization methods.
        """
        if cls._context_lock:
            raise RuntimeError(
                "Cannot enable multiprocessing while context is locked. "
                "Nested context managers are not allowed."
            )

        try:
            cls._context_lock = True
            cls._multiprocessing = True
            yield
        finally:
            cls._context_lock = False
            cls._multiprocessing = False


config = Config()
"""
The global configuration instance for the `psr` module.
"""
