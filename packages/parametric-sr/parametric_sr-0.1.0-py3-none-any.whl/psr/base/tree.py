"""
This module provides classes and utilities for working with trees (DAGs with max in-degree 1).
"""

from contextlib import contextmanager
from collections import defaultdict
from typing import (
    Any,
    Callable,
    Generator,
    Generic,
    Iterable,
    Literal,
    Mapping,
    Self,
    overload,
)
import textwrap

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import networkx as nx

from ..typing import R, T
from .exception import InvalidTreeError


class Tree(Generic[T]):
    """
    A class representing a tree structure by pointing to a node, its parent (if any), and its
    children (if any).

    When the parent is None, this points to the root node and represents the root of the tree.
    When the parent is not None, this points to a non-root node and represents a subtree.

    **NOTE**: Implementations of this class assume that the tree is a directed acyclic graph (DAG),
    with maximum in-degree equal to 1. Infinite loops can occur if this assumption is violated, such
    as when using this this class as an iterable with the `__iter__` method.

    Use the `is_tree` property to check if the tree is valid.
    """

    def __init__(
        self,
        value: T = None,
        idx: int = 0,
        parent: Self | None = None,
        children: Iterable[Self] | None = None,
        reindex: bool = False,
        *args: Any,
    ) -> None:
        """
        Initializes a tree/subtree. When initializing a root tree, the parent should be None.
        Otherwise, this is a subtree and should have a defined parent.

        Parameters
        ----------
        value : T
            The value/content of the node outside the tree context. This can be any type depending
            on the use case.
        idx : int
            The index of the node in the tree in depth-first search (DFS) order. The root node
            should have an index of 0.
        parent : Self | None
            The parent node of this node. If None, this node is the root of the tree.
        children : Iterable[Self] | None
            An iterable of child nodes/subtrees. If None, it is initialized as an empty list.
            If the list is empty, it indicates that this node is a leaf node.

            **NOTE**: The child nodes will be automatically linked to this instance as their parent.
        reindex : bool = False
            Whether to reindex the tree after initialization.
        *args : Any, **not used**
            Additional positional arguments to pass to the constructor. This is added for better
            serialization/deserialization support between different package versions.
        """
        self.value = value
        self.idx = idx
        self.parent = parent
        self.children = children
        if reindex:
            self.reindex()

    def validate(self, check_structure: bool = True, from_root: bool = True) -> None:
        """
        Validity check for the subtree rooted at this node. Check the `custom_validate` method for
        custom validation logic.

        First, it checks if the tree is a valid tree using the `is_tree` property.

        Then, use the `custom_validate` method to validate the node and its children recursively.
        The custom validator should return True if the node is valid (NOT the entire subtree) and
        False otherwise. For example, you can use it to check if the number of children is within a
        certain range or if the node value meets specific criteria.

        Index order is NOT checked. The custom validator should not rely on the index of the node.

        Parameters
        ----------
        check_structure : bool, default=True
            Whether to check the tree structure before applying the custom validation.

            - If True, it checks if the tree structure is valid (i.e., it is a valid tree).
            - If False, it skips the structure check and only applies the custom validation.

        from_root : bool, default=True
            If True, the validation starts from the root node. If False, it starts from this node.
            In most cases, validation only makes sense when starting from the root node, as it
            ensures a consistent and correct validation of all nodes in the tree.

        Raises
        ------
        InvalidTreeError
            If the tree structure is invalid or if the custom validation fails for any node.

        See Also
        --------
        custom_validate : a method that performs custom validation logic for the current node.
        is_tree : a property that checks if the subtree rooted at this node is a valid tree.
        """
        target = self.root if from_root else self
        if check_structure and not target.is_tree:
            raise InvalidTreeError()

        if not target.custom_validate(
            target.value, [child.value for child in target.children]
        ):
            raise InvalidTreeError(
                f"Custom validation failed for node with value: {target.value} (index {target.idx})"
            )

        for child in target.children:
            child.validate(check_structure=False, from_root=False)

    def custom_validate(self, node: T, children: Iterable[T]) -> bool:
        """
        A default custom validation function that always returns True, if not overridden.

        For custom validation logic, override this method in a subclass. You must follow the
        signature and return True if the node is valid, otherwise False. This method is only used to
        validate the current node and its children, not the entire subtree. The `validate` method
        handles the recursive validation of the entire subtree.

        **Note**: This method does not check the tree structure or index order. It is only used for
        custom validation logic.

        **Warning**: This method is called by the `validate` method, which checks the tree structure
        and calls this method for each node.

        Parameters
        ----------
        node : T
            The value of the current node.
        children : Iterable[T]
            An iterable of values of the children nodes.

        Returns
        -------
        bool
            True if the node is valid, otherwise False.
            The default implementation always returns True.

        See Also
        --------
        validate : method that calls this custom validation function.
        """
        return True

    def reindex(self, idx: int | None = None, from_root: bool = True) -> int:
        """
        Reindexes the tree nodes in depth-first search (DFS) order, by default starting from the
        root node.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

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
        """
        target = self.root if from_root else self

        if idx is None:
            idx = target.idx
        else:
            target.idx = idx

        n = 1
        for child in target.children:
            child.parent = target
            n += child.reindex(idx + n, from_root=False)

        target._n_nodes_cached = n
        return n

    def detach(
        self, value_detacher: Callable[[T], T] | None = None, as_root: bool = True
    ) -> Self:
        """
        Detaches the subtree rooted at this node from its original tree as a new copy. The purpose
        of this method is to create a new tree with the same structure and values, but without any
        references to the original tree. Cross-references between different trees can cause issues
        when manipulating the trees, so this method is useful to avoid such issues.

        Parameters
        ----------
        value_detacher : Callable[[T], T] | None, default=None
            A function that takes the value of the node (`self.value`) and returns a copy of it.
            In certain cases, `self.value` may be a mutable object that can cause cross-referencing
            issues. This custom detacher function can be used to create a new copy of the value.
        as_root : bool, default=True
            If True, the detached tree will be treated as a root tree and the parent will be set to
            None. This means that the new tree will not have any parent, and it will be a standalone
            tree.

            If False, the parent of the detached tree will be set to the original parent. In most
            cases, you should **NOT** use this option, as it can lead to cross-referencing issues.

        Returns
        -------
        Self
            A new instance of the tree with the same structure and values, but detached from the
            original tree. The detached tree will have no references to the original tree, unless
            `as_root` is False.
        """
        new_tree = self.__class__(
            value=self.value if value_detacher is None else value_detacher(self.value),
            idx=self.idx,
            parent=None if as_root else self.parent,
            children=[
                child.detach(value_detacher=value_detacher, as_root=as_root)
                for child in self.children
            ],
        )
        for child in new_tree.children:
            child.parent = new_tree
        return new_tree

    def update(self, donor: Self, validate: bool = False) -> None:
        """
        Updates the current subtree with the structure and values of the new (sub)tree in place.

        **NOTE**: The `value` and `children` of the current tree will be replaced with those of the
        new tree directly. If the new tree is a part of another tree, make sure that you use a copy
        or deepcopy of the new tree to avoid cross-referencing issues (see the `detach` method). If
        the original new tree instance is used, then both trees will share the same `value` and
        `children`, which can lead to unexpected behavior.

        Parameters
        ----------
        donor : Self
            The new tree/subtree to update the current tree with. The new tree should have the same
            type as the current tree. The `value` and `children` of the current tree will be
            replaced with those of the new tree directly.
        validate : bool, default=False
            If True, the root tree structure is validated after updating the tree.
            The root tree is also re-indexed in depth-first search (DFS) order.

        Raises
        ------
        InvalidTreeError
            If the update violates the tree structure, such as creating a cycle or invalidating the
            custom validation logic.

        See Also
        --------
        detach : detaches the subtree rooted at this node from its original tree as a new copy.
            Useful to avoid cross-referencing issues when the new tree is part of another tree.
        validate : helps to validate the tree structure after updating the tree.
            Useful to ensure that updating the tree does not violate the tree structure.
        """
        if donor is not self:
            self.value = donor.value
            self.children = donor.children
            for child in self.children:
                child.parent = self

        if not validate:
            return

        try:
            self.validate()
        except InvalidTreeError as e:
            raise InvalidTreeError(
                f"Updating tree with value `{donor.value}` violates tree structure. {e}"
            ) from e
        self.reindex()

    def add_child(
        self, child: Self, idx: int | None = None, validate: bool = False
    ) -> None:
        """
        Adds a child/subtree to this node at a given index.

        **NOTE**: The parent of the child will be set to this node. If the child is a part of
        another tree, make sure that you use a copy or deepcopy of the child to avoid
        cross-referencing issues (see the `detach` method). If the original child instance is used,
        its original root tree will be invalidated due to the new parent assignment.

        Parameters
        ----------
        child : Self
            The child node to be added. The parent of the child will be set to this node.
        validate : bool, default=False
            If True, the root tree structure is validated after adding the child.
            The root tree is also re-indexed in depth-first search (DFS) order.

        Raises
        ------
        InvalidTreeError
            If the addition of the child violates the tree structure, such as creating a cycle or
            invalidating the custom validation logic.

        See Also
        --------
        detach : detaches the subtree rooted at this node from its original tree as a new copy.
            Useful to avoid cross-referencing issues when the new child is part of another tree.
        validate : helps to validate the tree structure.
            Useful to ensure that adding the child does not violate the tree structure.
        """
        child.parent = self
        if idx is None:
            self.children.append(child)
        else:
            self.children.insert(idx, child)

        if not validate:
            return

        try:
            self.validate()
        except InvalidTreeError as e:
            raise InvalidTreeError(
                f"Adding child `{child.value}` to node `{self.value}` violates tree structure. {e}"
            )
        self.reindex()

    def remove_child(self, child: Self | int, validate: bool = False) -> None:
        """
        Removes a child/subtree from this node.

        Parameters
        ----------
        child : Self | int
            The child Tree instance or its index in the list of children to be removed.

            - If `child` is an instance of `Self`, it will be removed from the list of children.
            - If `child` is an integer, it will be treated as an index and the child at that index
              will be removed.

        validate : bool, default=False
            If True, the root tree structure is validated after adding the child.
            The root tree is also re-indexed in depth-first search (DFS) order.

        Raises
        ------
        IndexError
            If the index is out of bounds for the list of children.
        ValueError
            If the child is not in the list of children.
        InvalidTreeError
            If removing the child violates the tree structure.

        See Also
        --------
        validate : helps to validate the tree structure.
            Useful to ensure that removing the child does not violate the tree structure.
        """
        if isinstance(child, int):
            if abs(child) >= len(self.children):
                raise IndexError(
                    f"Index {child} is out of bounds for children of node `{self.value}`."
                )
            idx = child
            child = self.children[child]
        elif child in self.children:
            idx = self.children.index(child)
        else:
            raise ValueError(
                f"Child {child} is not in the list of children of node `{self.value}`."
            )

        del self.children[idx]
        if not validate:
            return

        try:
            self.validate()
        except InvalidTreeError as e:
            raise InvalidTreeError(
                f"Removing child `{child.value}` from node `{self.value}` violates tree structure. "
                f"{e}"
            )
        self.reindex()

    def replace_child(
        self, old_child: Self | int, new_child: Self, validate: bool = False
    ) -> None:
        """
        Replaces an existing child/subtree with a new child/subtree.

        **NOTE**: The parent of the new child will be set to this node. If the new child is a part
        of another tree, make sure that you use a copy or deepcopy of the new child to avoid
        cross-referencing issues (see the `detach` method). If the original new child instance is
        used, its original root tree will be invalidated due to the new parent assignment.

        Parameters
        ----------
        old_child : Self | int
            The old child Tree instance or its index in the list of children to be replaced.

            - If `old_child` is an instance of `Self`, it will be replaced in the list of children.
            - If `old_child` is an integer, it will be treated as an index and the child at that
              index will be replaced.

        new_child : Self
            The new child Tree instance to replace the old child.
        validate : bool, default=False
            If True, the root tree structure is validated after adding the child.
            The root tree is also re-indexed in depth-first search (DFS) order.

        Raises
        ------
        IndexError
            If the index is out of bounds for the list of children.
        ValueError
            If the old child is not in the list of children.
        InvalidTreeError
            If replacing the child violates the tree structure.

        See Also
        --------
        detach : detaches the subtree rooted at this node from its original tree as a new copy.
            Useful to avoid cross-referencing issues when the new child is part of another tree.
        validate : helps to validate the tree structure.
            Useful to ensure that replacing the child does not violate the tree structure.
        """
        if isinstance(old_child, int):
            if abs(old_child) >= len(self.children):
                raise IndexError(
                    f"Index {old_child} is out of bounds for children of node `{self.value}`."
                )
            idx = old_child
            old_child = self.children[old_child]
        elif old_child in self.children:
            idx = self.children.index(old_child)
        else:
            raise ValueError(
                f"Old child `{old_child}` is not in the list of children of node `{self.value}`."
            )

        try:
            self.children[idx].update(donor=new_child, validate=validate)
        except InvalidTreeError as e:
            raise InvalidTreeError(
                f"Replacing child `{old_child.value}` with `{new_child.value}` in node "
                f"`{self.value}` violates tree structure. {e}"
            )

    def getitem(
        self,
        idx: int,
        is_relative: bool = True,
        mode: Literal["local", "global"] = "local",
    ) -> Self:
        """
        Gets a child node by index.

        Parameters
        ----------
        idx : int
            The index of the child node to retrieve.
        is_relative : bool, default=True

            - If True, the index is relative and does not depend on the stored index of the node
              from `self.idx`.
            - If False, the index is absolute and must match the stored index of the node from
              `self.idx`.

        mode : Literal["local", "global"], default="local"
            The mode of indexing to use.

            - "local": Search in the subtree rooted at this node.
            - "global": Search in the entire tree, starting from the root.

        Returns
        -------
        Self
            The child node at the specified index.
        """
        root = self if mode == "local" else self.root

        if is_relative:
            return root[idx]

        for node in root:
            if node.idx == idx:
                return node
        raise IndexError(
            f"Node with the specified index {idx} not found in the {mode} tree."
        )

    def setitem(
        self,
        idx: int,
        value: Self,
        is_relative: bool = True,
        mode: Literal["local", "global"] = "local",
        validate: bool = False,
    ) -> None:
        """
        Sets a child node at the specified index.

        Parameters
        ----------
        idx : int
            The index at which to set the child node.
        value : Self
            The child node to set at the specified index.
        is_relative : bool, default=True

            - If True, the index is relative and does not depend on the stored index of the node
              from `self.idx`.
            - If False, the index is absolute and must match the stored index of the node from
              `self.idx`.

        mode : Literal["local", "global"], default="local"
            The mode of indexing to use.

            - "local": Search in the subtree rooted at this node.
            - "global": Search in the entire tree, starting from the root.

        validate : bool, default=False
            If True, the root tree structure is validated after adding the child.
            The root tree is also re-indexed in depth-first search (DFS) order.

        Raises
        ------
        IndexError
            If the index is out of bounds for the list of children.
        InvalidTreeError
            If setting the item violates the tree structure.

        See Also
        --------
        validate : helps to validate the tree structure after setting the item.
            Useful to ensure that setting the item does not violate the tree structure.
        """
        reference = self if mode == "local" else self.root

        if is_relative:
            reference[idx] = value
        else:
            for node in reference:
                if node.idx == idx:
                    node.update(donor=value, validate=validate)
                    break
            else:  # `break` not executed
                raise IndexError(
                    f"Node with specified index {idx} not found in the {mode} tree."
                )

        if not validate:
            return

        try:
            self.validate()
        except InvalidTreeError as e:
            raise InvalidTreeError(
                f"Setting item at index {idx} to `{value.value}` in the {mode} tree violates tree "
                f"structure. {e}"
            )
        self.reindex()

        raise IndexError(
            f"Node with specified index {idx} not found in the {mode} tree."
        )

    def evaluate(self, *args: R, method: str = "evaluate", **kwargs: Any) -> R:
        """
        Evaluates the subtree rooted at this node recursively, with evaluations from the children.
        The arguments and keyword arguments are recursively passed to the children nodes.

        The node's value is expected to have the specified method that takes the evaluations of the
        children as arguments, and possibly additional arguments and keyword arguments.

        Parameters
        ----------
        *args : R
            Positional arguments to pass to the evaluation function. The input type is generic
            and can be any type depending on the implementation of the specified method in the
            node's value. This allows for flexibility in how the node's value is evaluated,
            depending on the specific use case.
        method : str, default="evaluate"
            The method to call on the node's value. By default, it is "evaluate", but it can be
            changed to any other method that the node's value supports. This allows for flexibility
            in how the node's value is evaluated, depending on the specific use case.
        **kwargs : Any
            Keyword arguments to pass to the evaluation function.

        Returns
        -------
        R
            The result of evaluating the subtree. The return type is generic and can be any type
            depending on the implementation of the specified method in the node's value.

        Raises
        ------
        NotImplementedError
            If the value of the node does not have the specified method.

        See Also
        --------
        forward : alias method for compatibility with PyTorch's `forward` method.
        __call__ : alias method for compatibility with PyTorch's `__call__` method.
        """
        if not hasattr(self.value, method):
            raise NotImplementedError(
                f"The value of the node `{self.value}` does not have a `{method}` method."
            )

        return getattr(self.value, method)(
            *(
                child.evaluate(*args, method=method, **kwargs)
                for child in self.children
            ),
            *args,
            **kwargs,
        )

    def forward(self, *args: Any, **kwargs: Any) -> Any:
        """
        Alias for `evaluate` to evaluate the subtree rooted at this node, for compatibility with
        PyTorch's `forward` method.

        Parameters
        ----------
        *args : Any
            Positional arguments to pass to the evaluation function.
        **kwargs : Any
            Keyword arguments to pass to the evaluation function.

        Returns
        -------
        Any
            The result of evaluating the subtree.

        See Also
        --------
        evaluate : the base method to evaluate the subtree rooted at this node.
        __call__ : alias method for compatibility with PyTorch's `forward` method.
        """
        return self.evaluate(*args, **kwargs)

    @property
    def is_tree(self) -> bool:
        """
        If the subtree rooted at this node is a valid tree.

        A valid tree is defined as a directed acyclic graph (DAG) and each node has at most one
        parent. Check the reference from `networkx` for more :
        <https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.recognition.is_arborescence.html>

        Notes
        -----
        In certain cases, the subtree may be a valid tree, but the original root may still be
        invalid. For example, consider the following case:

        - A --> B
        - A --> C
        - B --> C

        In this case, the subtree rooted at C is valid, but the original root A is not valid (C has
        two parents). This is because the parent of the subtree is not considered in the tree
        structure validation.

        Returns
        -------
        bool
            True if the subtree is a valid tree, otherwise False.

        Examples
        >>> A, B, C = Tree("A"), Tree("B"), Tree("C")
        >>> A.add_child(B)
        >>> A.add_child(C)
        >>> B.add_child(C)
        >>> A.is_tree
        False
        >>> B.is_tree
        True
        >>> C.is_tree
        True
        """
        set_: set[int] = set()
        for node in self:
            if (id_ := id(node)) in set_:
                return False
            set_.add(id_)
            if not all(child.parent is node for child in node.children):
                return False

        if self.parent is not None:
            if (id_ := id(self.parent)) in set_:
                return False
            if not any(child is self for child in self.parent.children):
                return False

        return True

    @property
    def is_uniquely_indexed(self) -> bool:
        """
        Returns True if the subtree rooted at this node is both a valid tree and uniquely indexed,
        otherwise False.

        A uniquely indexed tree is defined as a valid tree where each node has a unique index
        regardless of its position. This means that no two distinct nodes can have the same index
        in the tree.

        Returns
        -------
        bool
            True if the subtree is valid and uniquely indexed, otherwise False.

        Notes
        -----
        The structure of the tree must also be valid, i.e., `self.is_tree` must be True, for this
        property to return True. If the tree is not valid, this property will return False.
        """
        if not self.is_tree:
            return False

        _set: set[int] = set()
        for node in self:
            if node.idx in _set:
                return False
            _set.add(node.idx)
        return True

    @property
    def parent(self) -> Self | None:
        """
        The parent node of this node. If this node is the root, a None is returned; otherwise, the
        parent node.

        Returns
        -------
        Self | None
            The parent node of this node, or None if this node is the root.
        """
        return self._parent

    @parent.setter
    def parent(self, value: Self | None) -> None:
        """
        ## Property Setter
        Sets the parent node of this node. If the value is None, then this node is seen as the root.
        Otherwise, it sets the parent to a weak reference to avoid circular references in memory.

        Parameters
        ----------
        value : Self | None
            The new parent node to set.
        """
        self._parent = value

    @property
    def children(self) -> list[Self]:
        """
        The list of child nodes of this node. If there are no children, an empty list is returned.

        Returns
        -------
        list[Self]
            The list of child nodes of this node.
        """
        return self._children

    @children.setter
    def children(self, value: Iterable[Self] | None) -> None:
        """
        ## Property Setter
        Sets the child nodes of this node. If the value is None, the children is initialized as an
        empty list. The child nodes will be automatically linked to this instance as their parent.

        Parameters
        ----------
        value : Iterable[Self] | None
            The new child nodes to set. Existing children will be replaced.

        """
        self._children = list(value) if value is not None else []
        for child in self._children:
            child.parent = self

    @property
    def _n_nodes(self) -> int:
        """
        The **cached** total number of nodes in the subtree rooted at this node.

        **WARNING**: this number is not updated automatically. It is set manually and may not
        reflect the actual number of nodes, if the tree structure is modified without updating this
        value. Use `__len__` method instead if you need to ensure correctness.

        Returns
        -------
        int
            The **cached** total number of nodes in the subtree rooted at this node.
        """
        return self._n_nodes_cached

    @_n_nodes.setter
    def _n_nodes(self, value: int) -> None:
        """
        ## Property Setter
        Sets the **cached** total number of nodes in the subtree rooted at this node. Mostly for
        reducing the overhead of counting nodes with `__len__` repeatedly.

        Parameters
        ----------
        value : int
            The total number of nodes in the subtree rooted at this node as **cached**.

        Raises
        ------
        ValueError
            If the value is less than 1.
        """
        if value < 1:
            raise ValueError("The number of nodes must be at least 1.")
        self._n_nodes_cached = value

    @property
    def root(self) -> Self:
        """
        The root node of the tree.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        If this node is the root, it returns itself. Otherwise, it traverses up to find the root.

        Returns
        -------
        Self
            The root node of the tree.

        Raises
        ------
        RecursionError, InvalidTreeError
            The root tree is not valid, i.e., it contains cycles or the parent references are
            incorrect.

        See Also
        --------
        is_root : A property that checks if this node is the root of the tree.
        is_tree : A property that checks if the subtree rooted at this node is a valid tree.
            **Note**: a valid subtree does not mean the `root` exists. The original root tree may
            still be invalid.
        """
        node = self
        s: set[int] = set()
        try:
            while True:
                if (id_ := id(node)) in s:
                    raise RecursionError("Circular reference detected.")
                s.add(id_)
                if node.parent is None:
                    return node
                node = node.parent
        except RecursionError as e:
            raise InvalidTreeError(
                f"The root tree is not valid. The root node cannot be determined. {e}"
            )

    @property
    def depth(self) -> int:
        """
        The depth of the node in the root tree (not the current subtree).

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        The root node is at depth 0, its children are at depth 1, and so on.

        Returns
        -------
        int
            The depth of the node in the root tree (not the current subtree).

        See Also
        --------
        height : the height of the subtree rooted at this node.
        widths : the widths of the subtree rooted at this node at each level.
        """
        node = self
        s: set[int] = set()
        n = 0
        try:
            while True:
                if (id_ := id(node)) in s:
                    raise RecursionError("Circular reference detected.")
                s.add(id_)
                if (node := node.parent) is None:
                    self._depth_cached = n
                    return n
                n += 1
        except RecursionError as e:
            raise InvalidTreeError(
                f"The root tree is not valid. The depth of the node in the root tree cannot be "
                f"determined. {e}"
            )

    @property
    def _depth(self) -> int:
        """
        Returns the **cached** depth of the node in the root tree (not the current subtree).

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        The root node is at depth 0, its children are at depth 1, and so on.

        Returns
        -------
        int
            The **cached** depth of the node in the root tree (not the current subtree).
        """
        return self._depth_cached

    @_depth.setter
    def _depth(self, value: int) -> None:
        """
        ## Property Setter
        Set the **cached** depth of the node in the root tree (not the current subtree).

        Parameters
        ----------
        value : int
            The depth to set as **cached**.

        Raises
        ------
        ValueError
            If the value is less than 0.
        """
        if value < 0:
            raise ValueError("Depth cannot be negative.")
        self._depth_cached = value

    @property
    def height(self) -> int:
        """
        The height of the subtree rooted at this node.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        The height is defined as the number of edges on the longest path from this node to a leaf.
        A leaf node has a height of 0.

        Returns
        -------
        int
            The height of the subtree rooted at this node.

        See Also
        --------
        depth : the depth of the node in the root tree.
        widths : the widths of the subtree rooted at this node at each level.
        no_validation : context manager to temporarily disable tree validation with the `is_tree`
            property.
        """
        if self.is_leaf:
            self._height_cached = 0
            return 0

        if getattr(self, "_validate", True) and not self.is_tree:
            raise InvalidTreeError

        try:
            n = 1 + max(child.height for child in self.children)
            self._height_cached = n
            return n
        except RecursionError as e:
            raise InvalidTreeError(
                f"The root tree is not valid. The height of the subtree rooted at this node cannot"
                f"be determined. {e}"
            )

    @property
    def _height(self) -> int:
        """
        Returns the **cached** height of the subtree rooted at this node.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        The height is defined as the number of edges on the longest path from this node to a leaf.
        A leaf node has a height of 0.

        Returns
        -------
        int
            The **cached** height of the subtree rooted at this node.
        """
        return self._height_cached

    @_height.setter
    def _height(self, value: int) -> None:
        """
        ## Property Setter
        Set the **cached** height of the subtree rooted at this node.

        Parameters
        ----------
        value : int
            The height to set as **cached**.

        Raises
        ------
        ValueError
            If the value is less than 0.
        """
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height_cached = value

    @property
    def widths(self) -> dict[int, int]:
        """
        The widths of the subtree rooted at this node at each level.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        The width is defined as the number of nodes at each level in the subtree.
        Depth starts from 0, so the root node is at depth 0 and has a width of 1.
        Depth 1 has the width of the children of the root, and so on.

        Returns
        -------
        dict[int, int]
            A dictionary of widths at each level in the subtree rooted at this node.

            - The keys are the depths (starting from 0).
            - The values are the widths at that depth.

        See Also
        --------
        depth : the depth of the node in the root tree.
        height : the height of the subtree rooted at this node.
        no_validation : context manager to temporarily disable tree validation with the `is_tree`
            property.
        """
        if getattr(self, "_validate", True) and not self.is_tree:
            raise InvalidTreeError

        width_dict: dict[int, int] = defaultdict(int)

        width_dict[0] = 1  # The root node is at depth 0

        for child in self.children:
            for depth, width in child.widths.items():
                width_dict[depth + 1] += width

        return width_dict

    @contextmanager
    def no_validation(self) -> Generator[Self, None, None]:
        """
        Context manager to temporarily disable tree validation with the `is_tree` property. This can
        be used to save some compute time and avoid repeated validations, e.g., when accessing the
        `height` and `widths` properties, and comparing trees with `__eq__`.

        Validation will be turned back on when exiting the context, regardless of the previous state
        before entering the context (and if an exception is raised).

        Yield
        ------
        Self
            The current node with validation disabled.
        """
        self._validate = False
        try:
            yield self
        finally:
            del self._validate

    @property
    def is_root(self) -> bool:
        """
        If the current node is the root of the tree or not.

        Returns
        -------
        bool
            True if the current node is the root of the tree, otherwise False.
        """
        return self.parent is None

    @property
    def is_leaf(self) -> bool:
        """
        If the current node is a leaf node (i.e., it has no children).

        Returns
        -------
        bool
            True if the current node is a leaf node (i.e., it has no children), otherwise False.
        """
        return not self.children

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Calls the `forward` method to evaluate the subtree rooted at this node.

        The arguments and keyword arguments are recursively passed to the children nodes.

        The node's value is expected to have an `evaluate` method that takes the evaluations of the
        children as arguments, and possibly additional arguments and keyword arguments.

        Returns
        -------
        Any
            The result of evaluating the subtree.

        See Also
        --------
        evaluate : the base method for evaluating the subtree
        forward : the method for evaluating the subtree with a forward pass (alias for `evaluate`).
        """
        return self.forward(*args, **kwargs)

    def __eq__(self, value: Self | Any) -> bool:
        """
        Checks if this node is the same object or has the same contents (value, index, and children)
        as the given value. Basically, checking if the two trees are equivalent.

        Returns
        -------
        bool
            True if this node is the same object or has the same contents (value, index, and
            children), otherwise False. Both trees must be structurally identical and should be
            valid trees.

        See Also
        --------
        no_validation : context manager to temporarily disable tree validation with the `is_tree`
            property.
        """
        if self is value:
            return True
        if type(value) is not type(self):
            return False
        if self.value != value.value:
            return False
        if self.idx != value.idx:
            return False
        if len(self.children) != len(value.children):
            return False
        if getattr(self, "_validate", True) and (not self.is_tree or not value.is_tree):
            return False
        return all(c1 == c2 for c1, c2 in zip(self.children, value.children))

    def __iter__(self) -> Generator[Self, None, None]:
        """
        Returns an iterator over the tree nodes in depth-first search (DFS) order.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        Yields
        ------
        Self
            The current node in the DFS traversal.
        """
        yield self
        for child in self.children:
            yield from child

    def __contains__(self, value: Self) -> bool:
        """
        Checks if the given value is in the subtree rooted at this node.

        Parameters
        ----------
        value : Self
            The node to check for containment.

        Returns
        -------
        bool
            True if the value is in the subtree, otherwise False.
        """
        return any(node == value for node in self)

    def __getitem__(self, index: int) -> Self:
        """
        Gets a child node by index.

        Parameters
        ----------
        index : int
            The index of the child node to retrieve.

        Returns
        -------
        Self
            The child node at the specified index.
        """
        for i, node in enumerate(self):
            if index == i:
                return node
        raise ValueError("Index out of bound")

    def __setitem__(self, index: int, value: Self) -> None:
        """
        Sets a child node at the specified index.

        Parameters
        ----------
        index : int
            The index at which to set the child node.
        value : Self
            The child node to set at the specified index.

        Raises
        ------
        IndexError
            If the index is out of bounds for the list of children.
        """
        self[index].update(donor=value, validate=True)

    def __len__(self) -> int:
        """
        Returns the number of nodes in the subtree rooted at this node.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        Returns
        -------
        int
            The number of nodes in the subtree rooted at this node.
        """
        n = 1 + sum(len(child) for child in self.children)
        self._n_nodes_cached = n
        return n

    def __repr__(self) -> str:
        """
        Returns a string representation of the tree node.

        The string representation includes the value, index, and the number of children.
        """
        return (
            f"{self.__class__.__name__}(value={self.value}, idx={self.idx}, "
            f"num_children={len(self.children)})"
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the tree node.

        The string representation includes the value, index, and the number of children.

        Returns
        -------
        str
            A string representation of the tree node.
        """
        return self.__repr__()

    @overload
    def to_list(
        self, *, plain: Literal[False] = False, stringify: Literal[False] = False
    ) -> list[Self]: ...
    @overload
    def to_list(
        self, *, plain: Literal[True], stringify: Literal[False] = False
    ) -> list[T]: ...
    @overload
    def to_list(
        self, *, plain: bool = False, stringify: Literal[True]
    ) -> list[str]: ...

    def to_list(
        self, *, plain: bool = False, stringify: bool = False
    ) -> list[Self] | list[T] | list[str]:
        """
        Converts the subtree rooted at this node to a list in depth-first search (DFS) order.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.

        Parameters
        ----------
        plain : bool, default=False (keyword-only)

            - If False, return a list of node objects (`Tree` instances).
            - If True, return a list of node values instead of node objects.

        stringify : bool, default=False (keyword-only)
            If True, return a list of strings instead of node objects or values.

        Returns
        -------
        list[Self] | list[T] | list[str]
            A list of nodes or their values in the subtree rooted at this node in DFS order. If
            `stringify` is True, the list objects will be converted to strings.
        """
        lst = [node.value for node in self] if plain else list(self)
        if stringify:
            lst = [str(item) for item in lst]
        return lst

    def to_graph(
        self,
        reindex: Literal["root", "self", False] = False,
        node_func: Callable[[T], Any] | None = str,
    ) -> nx.DiGraph:
        """
        Converts the subtree rooted at this node to a directed graph using `networkx`.

        **Warning**: `is_tree` must be True to ensure correctness and avoid infinite loops.
        `is_uniquely_indexed` must also be True to ensure that the graph is valid.

        Parameters
        ----------
        reindex : Literal["root", "self", False], default=False
            Whether to reindex the nodes in the graph. If "root", reindex from the root. If "self",
            reindex from this node. If False, do not reindex.
        node_func : Callable[[T], Any] | None, default=str
            A function to apply to each node's value when adding it to the graph. The function
            should take the node's value as input and return a representation for the value as the
            node value in the returned networkx graph.

            By default, the string representation of the node's value is used. Pass None to use the
            value object itself.

        Returns
        -------
        networkx.DiGraph
            A directed graph representation of the subtree rooted at this node.

        Raises
        ------
        InvalidTreeError
            If the subtree is not valid or not uniquely indexed, i.e., `is_uniquely_indexed` is
            False.
        """
        if reindex:
            self.reindex(from_root=reindex == "root")
        if not self.is_uniquely_indexed:
            raise InvalidTreeError(
                "The subtree is not valid or not uniquely indexed. Cannot convert to graph."
            )

        graph: nx.DiGraph = nx.DiGraph()
        for node in self:
            graph.add_node(  # type: ignore
                node.idx, value=node_func(node.value) if node_func else node.value
            )
        for node in self:
            if node.parent is not None:
                graph.add_edge(node.parent.idx, node.idx)  # type: ignore
        return graph

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
        Visualizes the subtree rooted at this node using `networkx` and `matplotlib`.

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
        G = self.to_graph(reindex=reindex)

        depth = max(self.depth, 4)
        widths = self.widths

        max_width = max(max(widths.values(), default=4), 4)
        if not ax:
            fig: Figure = plt.figure(figsize=(max_width * 1.6, depth * 1.2))  # type: ignore
            ax_: Axes = fig.add_subplot(111)  # type: ignore
        else:
            ax_ = ax
        ax_.set_title(  # type: ignore
            "\n".join(textwrap.wrap(str(self), width=max_width * 10)),
            fontsize=12,
        )
        pos: Mapping[int, Any] = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")  # type: ignore

        # format the node labels
        labels: dict[int, str] = {
            node[0]: f"{node[1]['value']}" for node in G.nodes(data=True)  # type: ignore
        }
        if with_index:
            labels = {k: f"{k}\n{v}" for k, v in labels.items()}

        nxdraw_kwargs.setdefault("node_size", 800)
        nxdraw_kwargs.setdefault("node_color", "#C2C2C2")
        nxdraw_kwargs.setdefault("node_shape", "s")
        nxdraw_kwargs.setdefault("font_size", 12)
        nx.draw(  # type: ignore
            G,
            pos,
            ax=ax_,
            labels=labels if with_labels else None,
            arrows=arrows,
            **nxdraw_kwargs,
        )
        return ax_

    def __del__(self) -> None:
        """
        Destructor to remove the **entire subtree** rooted at this node. This is mostly to handle
        circular references between a parent node and its children nodes.

        **Warning**: The entire subtree rooted at this node will be removed. If this is not a root
        tree (i.e., this subtree is a part of a larger tree), this may not affect the original
        root tree and the subtree may still be referenced in the original root tree. In such cases,
        use :func:`remove_child` or :func:`__delitem__` from the parent node/root tree.

        See Also
        --------
        __delitem__ : Method to delete a child node at a specific index.
        """
        parent = getattr(self, "_parent", None)
        if isinstance(parent, Tree):
            parent._children = [
                child for child in parent._children if child is not self
            ]
            self._parent = None

        while self._children:
            del self._children[0]

    def __delitem__(
        self,
        idx: int,
        /,
        *,
        is_relative: bool = True,
        mode: Literal["local", "global"] = "local",
    ) -> None:
        """
        Deletes a child node at the specified index.

        Parameters
        ----------
        idx : int
            The index of the child node to retrieve and delete.
        is_relative : bool, default=True

            - If True, the index is relative and does not depend on the stored index of the node
              from `self.idx`.
            - If False, the index is absolute and must match the stored index of the node from
              `self.idx`.

        mode : Literal["local", "global"], default="local"
            The mode of indexing to use.

            - "local": Search in the subtree rooted at this node.
            - "global": Search in the entire tree, starting from the root.

        See Also
        --------
        getitem : Method to retrieve a child node at a specific index.
        __del__ : Destructor to remove the entire subtree rooted at this node.
        """

        node = self.getitem(idx, is_relative=is_relative, mode=mode)
        parent = node.parent
        if parent is None:
            del node
        else:
            parent.remove_child(node)

    def __reduce__(self) -> tuple[type[Self], tuple[Any, ...]]:
        """
        Serialize the :class:`Tree` instance for pickling. This will treat the current tree as a
        root tree with no parent for serialization and deserialization.

        Returns
        -------
        tuple[type[Self], tuple[()]]
            A tuple containing the class type and the constructor arguments.
        """
        return (
            self.__class__,
            (self.value, self.idx, None, self.children or None, False),
        )
