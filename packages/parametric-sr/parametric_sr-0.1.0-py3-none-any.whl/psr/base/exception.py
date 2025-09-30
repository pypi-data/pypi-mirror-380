"""
exception classes for the module
"""


class InvalidTreeError(Exception):
    """
    Exception raised when an object is not a valid tree structure.

    A valid tree structure is defined as a directed acyclic graph (DAG) with an in-degree of at most
    1 for each node, meaning each node can have at most one parent.

    """

    def __init__(self, msg: str | None = None) -> None:
        """
        Initializes the InvalidTreeError with a custom error message.

        Parameters
        ----------
        msg : str | None, default=None
            The error message to display. If None, a default message will be used.
        """
        msg = msg or "Not a valid tree/arborescence."
        super().__init__(msg)
