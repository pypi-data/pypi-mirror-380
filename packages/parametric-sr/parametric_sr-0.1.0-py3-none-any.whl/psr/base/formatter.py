"""
formatter module for compiling string representations for expressions
"""

from dataclasses import dataclass, field
import re
from typing import Self, Sequence


@dataclass
class Formatter:
    """
    Formatter class for compiling string representations for operations in expressions.

    Parameters
    ----------
    template : str
        The template string to use for formatting. For example, for an addition, the template should
        be `{0} + {1}` or `{} + {}`.

        - Do NOT use curly brackets for non-formatting purposes.
        - Do not mix manual and automatic field numbering.
        - Only include ordered numbers in the curly brackets. `"{name}".format(name="psr")` is not
          supported.

    protection_rules : Sequence[bool], optional
        The protection rules to apply to the formatted string. The number of rules should correspond
        to the number of format placeholders in the `template`.

        - For example, for a multiplication with the template `{0} * {1}`, the protection rules
          should be `(True, True)`, since if `{0}` or `{1}` is a complex expression, it should be
          protected with brackets first.
        - Some other operations do not require protection, such as `exp({0})`, `max({0}, {1})`.

    needs_protection : bool, optional (default=True)
        Whether the formatted string needs protection before being integrated with other formatters.
        For example, if the root template is `{0} * {1}`, and the current formatter does not need
        protection, then the protection rule for `{0}` will be ignored (no brackets added).
    """

    template: str
    protection_rules: Sequence[bool] = field(default_factory=tuple)
    needs_protection: bool = True

    def __post_init__(self) -> None:
        args: list[str] = re.findall(r"\{(\d+|)\}", self.template)
        if not all(arg == "" or arg.isdigit() for arg in args):
            raise ValueError(
                "Invalid template string. "
                "All format placeholders must be either empty or numeric."
            )

        use_auto = "" in args
        use_manual = any(arg.isdigit() for arg in args)
        if use_auto and use_manual:
            raise ValueError(
                "Invalid template string. "
                "You should not mix manual and automatic field numbering."
            )

        n_args = 0
        if use_auto:
            n_args = len(args)
        elif use_manual:
            n_args = max(int(arg) for arg in args if arg.isdigit()) + 1

        n_rules = len(self.protection_rules)
        if n_args != n_rules:
            raise ValueError(
                f"Invalid protection rules. The number of protection rules (n={n_rules}) "
                f"must match the number of format placeholders (n={n_args})."
            )
        self.n_args = n_args

    def copy(self) -> Self:
        """
        Create a copy of the formatter instance.

        Returns
        -------
        Formatter
            A copy of the formatter instance.
        """
        return self.__class__(
            template=self.template,
            protection_rules=self.protection_rules,
            needs_protection=self.needs_protection,
        )

    def format(self, *args: Self | str, protect: bool = False) -> str:
        """
        Format the string representation of the operation using the provided template, protection
        rules, and arguments.

        Arguments
        ---------
        *args : Self | str
            The arguments to be formatted into the formatter/template. These should be instances
            of the Formatter class or strings, and the number of arguments must match the number
            of format placeholders in the template.
        protect : bool, default=False
            Whether protection is requested for the returned string. A protected string can be
            plugged into an expression as a safely encapsulated sub-expression.

        Returns
        -------
        str
            The (protected) formatted string.
        """
        template = self.template
        if protect and self.needs_protection:
            template = f"({template})"

        if len(args) == 0:
            return template

        return template.format(
            *(
                arg.format(protect=prule)
                for arg, prule in zip(args, self.protection_rules)
            )
        )

    def to_tuple(self) -> tuple[str, Sequence[bool], bool]:
        """
        Convert the formatter instance to a tuple representation.

        Returns
        -------
        tuple[str, Sequence[bool], bool]
            A tuple containing the template string, protection rules, and needs_protection flag.
        """
        return (self.template, self.protection_rules, self.needs_protection)

    @classmethod
    def from_tuple(cls, data: tuple[str, Sequence[bool], bool], /) -> Self:
        """
        Create a formatter instance from a tuple representation.

        Parameters
        ----------
        data : tuple[str, Sequence[bool], bool]
            A tuple containing the template string, protection rules, and needs_protection flag.

        Returns
        -------
        Formatter
            A new formatter instance.
        """
        template, protection_rules, needs_protection = data
        return cls(
            template=template,
            protection_rules=protection_rules,
            needs_protection=needs_protection,
        )

    def __reduce__(self) -> tuple[type[Self], tuple[str, Sequence[bool], bool]]:
        """
        Serialize the formatter instance for pickling.

        Returns
        -------
        tuple[type[Self], tuple[str, Sequence[bool], bool]]
            A tuple containing the class type and the tuple representation of the instance (the
            `__init__` parameters).
        """
        return (
            self.__class__,
            self.to_tuple(),
        )
