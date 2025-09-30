from __future__ import annotations

__all__ = [
    "BDDFunction",
    "BDDManager",
    "BDDSubstitution",
    "BCDDFunction",
    "BCDDManager",
    "BCDDSubstitution",
    "ZBDDFunction",
    "ZBDDManager",
    "DDMemoryError",
    "DuplicateVarName",
    "BooleanOperator",
    "DDDMPFile",
    "DDDMPVersion",
]

import enum
from collections.abc import Iterable
from os import PathLike
from types import TracebackType
from typing import final

from typing_extensions import Never, Self, deprecated

class BooleanOperator(enum.Enum):
    """Binary operators on Boolean functions."""

    AND = ...
    """Conjunction ``lhs ∧ rhs``"""
    OR = ...
    """Disjunction ``lhs ∨ rhs``"""
    XOR = ...
    """Exclusive disjunction ``lhs ⊕ rhs``"""
    EQUIV = ...
    """Equivalence ``lhs ↔ rhs``"""
    NAND = ...
    """Negated conjunction ``lhs ⊼ rhs``"""
    NOR = ...
    """Negated disjunction ``lhs ⊽ rhs``"""
    IMP = ...
    """Implication ``lhs → rhs`` (or `lhs ≤ rhs)`"""
    IMP_STRICT = ...
    """Strict implication ``lhs < rhs``"""

class DDDMPVersion(enum.Enum):
    """DDDMP format version version."""

    V2_0 = ...
    """Version 2.0, bundled with `CUDD <https://github.com/cuddorg/cudd>` 3.0"""
    V3_0 = ...
    """Version 3.0, used by `BDDSampler`_ and `Logic2BDD`_

    .. _BDDSampler: https://github.com/davidfa71/BDDSampler
    .. _Logic2BDD: https://github.com/davidfa71/Extending-Logic
    """

@final
class BDDManager:
    r"""Manager for binary decision diagrams (without complement edges).

    Implements: :class:`~oxidd.protocols.BooleanFunctionManager`\
    [:class:`BDDFunction`]
    """

    @classmethod
    def __new__(cls, /, inner_node_capacity: int, apply_cache_capacity: int, threads: int) -> BDDManager:
        """Create a new manager.

        Args:
            inner_node_capacity (int): Maximum count of inner nodes
            apply_cache_capacity (int): Maximum count of apply cache entries
            threads (int): Worker thread count for the internal thread pool

        Returns:
            BDDManager: The new manager
        """

    def num_inner_nodes(self, /) -> int:
        """Get the count of inner nodes.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of inner nodes stored in this manager
        """

    def approx_num_inner_nodes(self, /) -> int:
        """Get an approximate count of inner nodes.

        For concurrent implementations, it may be much less costly to determine
        an approximation of the inner node count than an accurate count
        (:meth:`num_inner_nodes`).

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: An approximate count of inner nodes stored in this manager
        """

    def num_vars(self, /) -> int:
        """Get the number of variables in this manager.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of variables
        """

    def num_named_vars(self, /) -> int:
        """Get the number of named variables in this manager.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of named variables
        """

    def add_vars(self, /, additional: int) -> range:
        """Add ``additional`` unnamed variables to the decision diagram.

        The new variables are added at the bottom of the variable order. More
        precisely, the level number equals the variable number for each new
        variable.

        Note that some algorithms may assume that the domain of a function
        represented by a decision diagram is just the set of all variables. In
        this regard, adding variables can change the semantics of decision
        diagram nodes.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            additional (int): Count of variables to add

        Returns:
            range: The new variable numbers
        """

    def add_named_vars(self, /, names: Iterable[str]) -> range:
        """Add named variables to the decision diagram.

        This is a shorthand for :meth:`add_vars` and respective
        :meth:`set_var_name` calls. More details can be found there.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            names (Iterable[str]): Names of the new variables

        Returns:
            range: The new variable numbers

        Raises:
            ValueError: If a variable name occurs twice in ``names``. The
                exception's argument is a :class:`DuplicateVarName`.
        """

    def var_name(self, /, var: int) -> str:
        """Get ``var``'s name.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int): The variable number

        Returns:
            str: The name, or an empty string for unnamed variables

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def set_var_name(self, /, var: int, name: str) -> None:
        """Label ``var`` as ``name``.

        An empty name means that the variable will become unnamed, and cannot be
        retrieved via :meth:`name_to_var` anymore.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            var (int): The variable number
            name (str): The new variable name

        Returns:
            None

        Raises:
            ValueError: If ``name`` is not unique (and not ``""``). The
                exception's argument is a :class:`DuplicateVarName`.
            IndexError: If ``var >= self.num_vars()``
        """

    def name_to_var(self, /, name: str) -> int | None:
        """Get the variable number for the given variable name, if present.

        Note that you cannot retrieve unnamed variables.
        ``manager.name_to_var("")`` always returns ``None``.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            name (str): The variable name

        Returns:
            int | None: The variable number if found, or ``None``
        """

    def var_to_level(self, /, var: int) -> int:
        """Get the level for the given variable.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int): The variable number

        Returns:
            int: The level number

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def level_to_var(self, /, level: int) -> int:
        """Get the variable for the given level.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            level (int): The level number

        Returns:
            int: The variable number

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def gc(self, /) -> int:
        """Perform garbage collection.

        This method looks for nodes that are neither referenced by a
        :class:`BDDFunction` nor another node and removes them. The method
        works from top to bottom, so if a node is only referenced by nodes
        that can be removed, this node will be removed as well.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The count of nodes removed
        """

    def gc_count(self, /) -> int:
        """Get the count of garbage collections.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The garbage collection count
        """

    def var(self, /, var: int | str) -> BDDFunction:
        """Get the Boolean function that is true if and only if ``var`` is true.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int | str): The variable number or name

        Returns:
            BDDFunction: A Boolean function that is true if and only if the
            variable is true

        Raises:
            DDMemoryError: If the operation runs out of memory
            IndexError: If ``var`` is an ``int`` and ``var >= self.num_vars()``
            KeyError: If ``var`` is a string and
                ``self.name_to_var(var) is None``
        """

    def not_var(self, /, var: int | str) -> BDDFunction:
        """Get the Boolean function that is true if and only if ``var`` is false.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int | str): The variable number or name

        Returns:
            BDDFunction: A Boolean function that is true if and only if the
            variable is false

        Raises:
            DDMemoryError: If the operation runs out of memory
            IndexError: If ``var`` is an ``int`` and ``var >= self.num_vars()``
            KeyError: If ``var`` is a string and
                ``self.name_to_var(var) is None``
        """

    def true(self, /) -> BDDFunction:
        """Get the constant true Boolean function ``⊤``.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            BDDFunction: The constant true Boolean function ``⊤``
        """

    def false(self, /) -> BDDFunction:
        """Get the constant false Boolean function ``⊥``.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            BDDFunction: The constant false Boolean function ``⊥``
        """

    def set_var_order(self, /, order: Iterable[int]) -> None:
        """Reorder the variables according to ``order``.

        If a variable ``x`` occurs before variable ``y`` in ``order``, then
        ``x`` will be above ``y`` in the decision diagram when this function
        returns. Variables not mentioned in ``order`` will be placed in a
        position such that the least number of level swaps need to be
        performed.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            order (Iterable[int]): The variable order to establish

        Returns:
            None
        """

    def import_dddmp(self, /, file: DDDMPFile, support_vars: Iterable[int] | None = None) -> list[BDDFunction]:
        """Import the decision diagram from the DDDMP ``file``.

        Note that the support variables must also be ordered by their current
        level (lower level numbers first). To this end, you can use
        :meth:`set_var_order` with ``support_vars`` (or
        :attr:`file.support_var_order
        <oxidd.util.DDDMPFile.support_var_order>`).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            file (DDDMPFile): The DDDMP file handle
            support_vars (Iterable[int] | None): Optional mapping from support
                variables of the DDDMP file to variable numbers in this manager.
                By default, :attr:`file.support_var_order
                <oxidd.util.DDDMPFile.support_var_order>` will be used.

        Returns:
            list[BDDFunction]: The imported BDD functions
        """

    def export_dddmp(self, /, path: str | PathLike[str], functions: Iterable[BDDFunction], *, version: DDDMPVersion = DDDMPVersion.V2_0, ascii: bool = False, strict: bool = True, diagram_name: str = "") -> None:
        """Export the given decision diagram functions as DDDMP file.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[BDDFunction]): Functions to export (must be
                stored in this manager).
            version (DDDMPVersion): DDDMP format version to use
            ascii (bool): If ``True``, ASCII mode will be enforced for the
                export. By default (and if ``False``), binary mode will be used
                if supported for the decision diagram kind.
                Binary mode is currently supported for BCDDs only.
            strict (bool): If ``True`` (the default), enable `strict mode`_
            diagram_name (str): Name of the decision diagram

        Returns:
            None

        .. _`strict mode`: https://docs.rs/oxidd-dump/latest/oxidd_dump/dddmp/struct.ExportSettings.html#method.strict
        """

    def export_dddmp_with_names(self, /, path: str | PathLike[str], functions: Iterable[tuple[BDDFunction, str]], *, version: DDDMPVersion = DDDMPVersion.V2_0, ascii: bool = False, strict: bool = True, diagram_name: str = "") -> None:
        """Export the given decision diagram functions as DDDMP file.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[BDDFunction, str]]): Pairs of function
                and name. All functions must be stored in this manager.
            version (DDDMPVersion): DDDMP format version to use
            ascii (bool): If ``True``, ASCII mode will be enforced for the
                export. By default (and if ``False``), binary mode will be used
                if supported for the decision diagram kind.
                Binary mode is currently supported for BCDDs only.
            strict (bool): If ``True`` (the default), enable `strict mode`_
            diagram_name (str): Name of the decision diagram

        Returns:
            None

        .. _`strict mode`: https://docs.rs/oxidd-dump/latest/oxidd_dump/dddmp/struct.ExportSettings.html#method.strict
        """

    def visualize(self, /, diagram_name: str, functions: Iterable[BDDFunction], *, port: int = 4000) -> None:
        """Serve the given decision diagram functions for visualization.

        Blocks until the visualization has been fetched by `OxiDD-vis`_ (or
        another compatible tool).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            diagram_name (str): Name of the decision diagram
            functions (Iterable[BDDFunction]): Functions to visualize (must be
                stored in this manager)
            port (int): The port to provide the data on, defaults to 4000.

        Returns:
            None

        .. _OxiDD-vis: https://oxidd.net/vis
        """

    def visualize_with_names(self, /, diagram_name: str, functions: Iterable[tuple[BDDFunction, str]], *, port: int = 4000) -> None:
        """Serve the given decision diagram functions for visualization.

        Blocks until the visualization has been fetched by `OxiDD-vis`_ (or
        another compatible tool).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            diagram_name (str): Name of the decision diagram
            functions (Iterable[tuple[BDDFunction, str]]): Pairs of function
                and name. All functions must be stored in this manager.
            port (int): The port to provide the data on, defaults to 4000.

        Returns:
            None

        .. _OxiDD-vis: https://oxidd.net/vis
        """

    def dump_all_dot(self, /, path: str | PathLike[str], functions: Iterable[tuple[BDDFunction, str]] = []) -> None:
        """Dump the entire decision diagram in this manager as Graphviz DOT code.

        The output may also include nodes that are not reachable from
        ``functions``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[BDDFunction, str]]): Optional names for
                BDD functions

        Returns:
            None
        """

    @deprecated("Use dump_all_dot instead")
    def dump_all_dot_file(self, /, path: str | PathLike[str], functions: Iterable[tuple[BDDFunction, str]] = []) -> None:
        """Deprecated alias for :meth:`dump_all_dot`.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[BDDFunction, str]]): Optional names for
                BCDD functions

        Returns:
            None

        .. deprecated:: 0.11
           Use :meth:`dump_all_dot` instead
        """

    def __eq__(self, /, rhs: object) -> bool: ...
    def __ne__(self, /, rhs: object) -> bool: ...
    def __hash__(self, /) -> int: ...


@final
class BDDSubstitution:
    """Substitution mapping variables to replacement functions.

    Implements: :class:`~oxidd.protocols.FunctionSubst`
    """

    @classmethod
    def __new__(cls, /, pairs: Iterable[tuple[int, BDDFunction]]) -> BDDSubstitution:
        """Create a new substitution object for BDDs.

        See :meth:`BDDFunction.make_substitution` for more details.

        Args:
            pairs (Iterable[tuple[int, BDDFunction]]):
                ``(variable, replacement)`` pairs, where all variables are
                distinct. The order of the pairs is irrelevant.

        Returns:
            BDDSubstitution: The new substitution
        """


@final
class BDDFunction:
    r"""Boolean function represented as a simple binary decision diagram (BDD).

    Implements:
        :class:`~oxidd.protocols.BooleanFunctionQuant`,
        :class:`~oxidd.protocols.FunctionSubst`\ [:class:`BDDSubstitution`],
        :class:`~oxidd.protocols.HasLevel`

    All operations constructing BDDs may throw a
    :exc:`~oxidd.util.DDMemoryError` in case they run out of memory.

    Note that comparisons like ``f <= g`` are based on an arbitrary total order
    and not related to logical implications. See the
    :meth:`Function <oxidd.protocols.Function.__lt__>` protocol for more
    details.
    """

    @classmethod
    def __new__(cls, _: Never) -> Self:
        """Private constructor."""

    @property
    def manager(self, /) -> BDDManager:
        """BDDManager: The associated manager."""

    def cofactors(self, /) -> tuple[Self, Self] | None:
        r"""Get the cofactors ``(f_true, f_false)`` of ``self``.

        Let f(x₀, …, xₙ) be represented by ``self``, where x₀ is (currently) the
        top-most variable. Then f\ :sub:`true`\ (x₁, …, xₙ) = f(⊤, x₁, …, xₙ)
        and f\ :sub:`false`\ (x₁, …, xₙ) = f(⊥, x₁, …, xₙ).

        Structurally, the cofactors are simply the children in case with edge
        tags adjusted accordingly.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            tuple[Self, Self] | None: The cofactors ``(f_true, f_false)``, or
            ``None`` if ``self`` references a terminal node.

        See Also:
            :meth:`cofactor_true`, :meth:`cofactor_false` if you only need one
            of the cofactors.
        """

    def cofactor_true(self, /) -> Self | None:
        """Get the cofactor ``f_true`` of ``self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self | None: The cofactor ``f_true``, or ``None`` if ``self``
            references a terminal node.

        See Also:
            :meth:`cofactors`, also for a more detailed description
        """

    def cofactor_false(self, /) -> Self | None:
        """Get the cofactor ``f_false`` of ``self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self | None: The cofactor ``f_false``, or ``None`` if ``self``
            references a terminal node.

        See Also:
            :meth:`cofactors`, also for a more detailed description
        """

    def node_level(self, /) -> int | None:
        """Get the level of the underlying node.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            int | None: The level, or ``None`` if the node is a terminal
        """

    @deprecated("Use node_level instead")
    def level(self, /) -> int | None:
        """Deprecated alias for :meth:`node_level`.

        Returns:
            int | None: The level, or ``None`` if the node is a terminal

        .. deprecated:: 0.11
           Use :meth:`node_level` instead
        """

    def node_var(self, /) -> int | None:
        """Get the variable number for the underlying node.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            int | None: The variable number, or ``None`` if the node is a
            terminal
        """

    def __invert__(self, /) -> Self:
        """Compute the negation ``¬self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self: ``¬self``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __and__(self, rhs: Self, /) -> Self:
        """Compute the conjunction ``self ∧ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ∧ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __or__(self, rhs: Self, /) -> Self:
        """Compute the disjunction ``self ∨ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ∨ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __xor__(self, rhs: Self, /) -> Self:
        """Compute the exclusive disjunction ``self ⊕ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊕ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def nand(self, rhs: Self, /) -> Self:
        """Compute the negated conjunction ``self ⊼ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊼ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def nor(self, rhs: Self, /) -> Self:
        """Compute the negated disjunction ``self ⊽ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊽ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def equiv(self, rhs: Self, /) -> Self:
        """Compute the equivalence ``self ↔ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ↔ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def imp(self, rhs: Self, /) -> Self:
        """Compute the implication ``self → rhs`` (or ``f ≤ g``).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self → rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def imp_strict(self, rhs: Self, /) -> Self:
        """Compute the strict implication ``self < rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self < rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def ite(self, /, t: Self, e: Self) -> Self:
        """Compute the BDD for the conditional ``t if self else e``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            t (Self): Then-case; must belong to the same manager as ``self``
            e (Self): Else-case; must belong to the same manager as ``self``

        Returns:
            Self: The Boolean function ``f(v: 𝔹ⁿ) = t(v) if self(v) else e(v)``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    @classmethod
    def make_substitution(cls, pairs: Iterable[tuple[int, Self]], /) -> BDDSubstitution:
        """Create a new substitution object from pairs ``(var, replacement)``.

        The intent behind substitution objects is to optimize the case where the
        same substitution is applied multiple times. We would like to re-use
        apply cache entries across these operations, and therefore, we need a
        compact identifier for the substitution. This identifier is provided by
        the returned substitution object.

        Args:
            pairs (Iterable[tuple[int, Self]]): ``(variable, replacement)``
                pairs, where all variables are distinct. The order of the pairs
                is irrelevant.

        Returns:
            BDDSubstitution: The substitution to be used with :meth:`substitute`
        """

    def substitute(self, substitution: BDDSubstitution, /) -> Self:
        """Substitute variables in ``self`` according to ``substitution``.

        The substitution is performed in a parallel fashion, e.g.:
        ``(¬x ∧ ¬y)[x ↦ ¬x ∧ ¬y, y ↦ ⊥] = ¬(¬x ∧ ¬y) ∧ ¬⊥ = x ∨ y``

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            substitution (BDDSubstitution): A substitution object created using
                :meth:`make_substitution`. All contained DD functions must
                belong to the same manager as ``self``.

        Returns:
            Self: ``self`` with variables substituted
        """

    def forall(self, /, vars: Self) -> Self:
        """Compute the universal quantification over ``vars``.

        This operation removes all occurrences of variables in ``vars`` by
        universal quantification. Universal quantification ∀x. f(…, x, …) of a
        Boolean function f(…, x, …) over a single variable x is
        f(…, 0, …) ∧ f(…, 1, …).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∀ vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def exists(self, /, vars: Self) -> Self:
        """Compute the existential quantification over ``vars``.

        This operation removes all occurrences of variables in ``vars`` by
        existential quantification. Existential quantification ∃x. f(…, x, …) of
        a Boolean function f(…, x, …) over a single variable x is
        f(…, 0, …) ∨ f(…, 1, …).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∃ vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    @deprecated("Use exists instead")
    def exist(self, /, vars: Self) -> Self:
        """Deprecated alias for :meth:`exists`.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∃ vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory

        .. deprecated:: 0.10
           Use :meth:`exists` instead
        """

    def unique(self, /, vars: Self) -> Self:
        """Compute the unique quantification over ``vars``.

        This operation removes all occurrences of variables in ``vars`` by
        unique quantification. Unique quantification ∃!x. f(…, x, …) of a
        Boolean function f(…, x, …) over a single variable x is
        f(…, 0, …) ⊕ f(…, 1, …). Unique quantification is also known as the
        `Boolean difference <https://en.wikipedia.org/wiki/Boole%27s_expansion_theorem#Operations_with_cofactors>`_ or
        `Boolean derivative <https://en.wikipedia.org/wiki/Boolean_differential_calculus>`_.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∃! vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def apply_forall(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Combined application of ``op`` and :meth:`forall`.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∀ vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def apply_exists(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Combined application of ``op`` and :meth:`exists`.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∃ vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    @deprecated("Use apply_exists instead")
    def apply_exist(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Deprecated alias for ``apply_exists()``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∃ vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory

        .. deprecated:: 0.10
           Use :meth:`apply_exists` instead
        """

    def apply_unique(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Combined application of ``op`` and :meth:`unique`.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∃! vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def node_count(self, /) -> int:
        """Get the number of descendant nodes.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The count of descendant nodes including the node referenced by
            ``self`` and terminal nodes.
        """

    def satisfiable(self, /) -> bool:
        """Check for satisfiability.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            bool: Whether the Boolean function has at least one satisfying
            assignment
        """

    def valid(self, /) -> bool:
        """Check for validity.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            bool: Whether all assignments satisfy the Boolean function
        """

    def sat_count(self, /, vars: int) -> int:
        """Count the number of satisfying assignments.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (int): Assume that the function's domain has this many
                variables.

        Returns:
            int: The exact number of satisfying assignments
        """

    def sat_count_float(self, /, vars: int) -> float:
        """Count the number of satisfying assignments.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (int): Assume that the function's domain has this many
                variables.

        Returns:
            float: (An approximation of) the number of satisfying assignments
        """

    def pick_cube(self, /) -> list[bool | None] | None:
        """Pick a satisfying assignment.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            list[bool | None] | None: The satisfying assignment where the i-th
            value means that the i-th variable is false, true, or "don't care,"
            respectively, or ``None`` if ``self`` is unsatisfiable
        """

    def pick_cube_dd(self, /) -> Self:
        """Pick a satisfying assignment, represented as decision diagram.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            Self: The satisfying assignment as decision diagram, or ``⊥`` if
            ``self`` is unsatisfiable
        """

    def pick_cube_dd_set(self, /, literal_set: Self) -> Self:
        """Pick a satisfying assignment as DD, with choices as of ``literal_set``.

        ``literal_set`` is a conjunction of literals. Whenever there is a choice
        for a variable, it will be set to true if the variable has a positive
        occurrence in ``literal_set``, and set to false if it occurs negated in
        ``literal_set``. If the variable does not occur in ``literal_set``, then
        it will be left as don't care if possible, otherwise an arbitrary (not
        necessarily random) choice will be performed.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            literal_set (Self): Conjunction of literals to determine the choice
                for variables

        Returns:
            Self: The satisfying assignment as decision diagram, or ``⊥`` if
            ``self`` is unsatisfiable

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def eval(self, /, args: Iterable[tuple[int, bool]]) -> bool:
        """Evaluate this Boolean function with arguments ``args``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            args (Iterable[tuple[int, bool]]): ``(variable, value)`` pairs that
                determine the valuation for all variables in the function's
                domain. The order is irrelevant (except that if the valuation
                for a variable is given multiple times, the last value counts).
                Should there be a decision node for a variable not part of the
                domain, then ``False`` is used as the decision value.

        Returns:
            bool: The result of applying the function ``self`` to ``args``

        Raises:
            IndexError: If any variable number in ``args`` is greater or equal
                to ``self.manager.num_vars()``
        """

    def __eq__(self, /, rhs: object) -> bool: ...
    def __ne__(self, /, rhs: object) -> bool: ...
    def __le__(self, /, rhs: Self) -> bool: ...
    def __lt__(self, /, rhs: Self) -> bool: ...
    def __ge__(self, /, rhs: Self) -> bool: ...
    def __gt__(self, /, rhs: Self) -> bool: ...
    def __hash__(self, /) -> int: ...


@final
class BCDDManager:
    r"""Manager for binary decision diagrams with complement edges.

    Implements: :class:`~oxidd.protocols.BooleanFunctionManager`\
    [:class:`BCDDFunction`]
    """

    @classmethod
    def __new__(cls, /, inner_node_capacity: int, apply_cache_capacity: int, threads: int) -> BCDDManager:
        """Create a new manager.

        Args:
            inner_node_capacity (int): Maximum count of inner nodes
            apply_cache_capacity (int): Maximum count of apply cache entries
            threads (int): Worker thread count for the internal thread pool

        Returns:
            BCDDManager: The new manager
        """

    def num_inner_nodes(self, /) -> int:
        """Get the count of inner nodes.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of inner nodes stored in this manager
        """

    def approx_num_inner_nodes(self, /) -> int:
        """Get an approximate count of inner nodes.

        For concurrent implementations, it may be much less costly to determine
        an approximation of the inner node count than an accurate count
        (:meth:`num_inner_nodes`).

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: An approximate count of inner nodes stored in this manager
        """

    def num_vars(self, /) -> int:
        """Get the number of variables in this manager.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of variables
        """

    def num_named_vars(self, /) -> int:
        """Get the number of named variables in this manager.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of named variables
        """

    def add_vars(self, /, additional: int) -> range:
        """Add ``additional`` unnamed variables to the decision diagram.

        The new variables are added at the bottom of the variable order. More
        precisely, the level number equals the variable number for each new
        variable.

        Note that some algorithms may assume that the domain of a function
        represented by a decision diagram is just the set of all variables. In
        this regard, adding variables can change the semantics of decision
        diagram nodes.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            additional (int): Count of variables to add

        Returns:
            range: The new variable numbers
        """

    def add_named_vars(self, /, names: Iterable[str]) -> range:
        """Add named variables to the decision diagram.

        This is a shorthand for :meth:`add_vars` and respective
        :meth:`set_var_name` calls. More details can be found there.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            names (Iterable[str]): Names of the new variables

        Returns:
            range: The new variable numbers

        Raises:
            ValueError: If a variable name occurs twice in ``names``. The
                exception's argument is a :class:`DuplicateVarName`.
        """

    def var_name(self, /, var: int) -> str:
        """Get ``var``'s name.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int): The variable number

        Returns:
            str: The name, or an empty string for unnamed variables

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def set_var_name(self, /, var: int, name: str) -> None:
        """Label ``var`` as ``name``.

        An empty name means that the variable will become unnamed, and cannot be
        retrieved via :meth:`name_to_var` anymore.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            var (int): The variable number
            name (str): The new variable name

        Returns:
            None

        Raises:
            ValueError: If ``name`` is not unique (and not ``""``). The
                exception's argument is a :class:`DuplicateVarName`.
            IndexError: If ``var >= self.num_vars()``
        """

    def name_to_var(self, /, name: str) -> int | None:
        """Get the variable number for the given variable name, if present.

        Note that you cannot retrieve unnamed variables.
        ``manager.name_to_var("")`` always returns ``None``.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            name (str): The variable name

        Returns:
            int | None: The variable number if found, or ``None``
        """

    def var_to_level(self, /, var: int) -> int:
        """Get the level for the given variable.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int): The variable number

        Returns:
            int: The level number

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def level_to_var(self, /, level: int) -> int:
        """Get the variable for the given level.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            level (int): The level number

        Returns:
            int: The variable number

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def gc(self, /) -> int:
        """Perform garbage collection.

        This method looks for nodes that are neither referenced by a
        :class:`BCDDFunction` nor another node and removes them. The method
        works from top to bottom, so if a node is only referenced by nodes
        that can be removed, this node will be removed as well.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The count of nodes removed
        """

    def gc_count(self, /) -> int:
        """Get the count of garbage collections.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The garbage collection count
        """

    def var(self, /, var: int | str) -> BCDDFunction:
        """Get the Boolean function that is true if and only if ``var`` is true.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int | str): The variable number or name

        Returns:
            BCDDFunction: A Boolean function that is true if and only if the
            variable is true

        Raises:
            DDMemoryError: If the operation runs out of memory
            IndexError: If ``var`` is an ``int`` and ``var >= self.num_vars()``
            KeyError: If ``var`` is a string and
                ``self.name_to_var(var) is None``
        """

    def not_var(self, /, var: int | str) -> BCDDFunction:
        """Get the Boolean function that is true if and only if ``var`` is false.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int | str): The variable number or name

        Returns:
            BCDDFunction: A Boolean function that is true if and only if the
            variable is false

        Raises:
            DDMemoryError: If the operation runs out of memory
            IndexError: If ``var`` is an ``int`` and ``var >= self.num_vars()``
            KeyError: If ``var`` is a string and
                ``self.name_to_var(var) is None``
        """

    def true(self, /) -> BCDDFunction:
        """Get the constant true Boolean function ``⊤``.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            BCDDFunction: The constant true Boolean function ``⊤``
        """

    def false(self, /) -> BCDDFunction:
        """Get the constant false Boolean function ``⊥``.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            BCDDFunction: The constant false Boolean function ``⊥``
        """

    def set_var_order(self, /, order: Iterable[int]) -> None:
        """Reorder the variables according to ``order``.

        If a variable ``x`` occurs before variable ``y`` in ``order``, then
        ``x`` will be above ``y`` in the decision diagram when this function
        returns. Variables not mentioned in ``order`` will be placed in a
        position such that the least number of level swaps need to be
        performed.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            order (Iterable[int]): The variable order to establish

        Returns:
            None
        """

    def import_dddmp(self, /, file: DDDMPFile, support_vars: Iterable[int] | None = None) -> list[BCDDFunction]:
        """Import the decision diagram from the DDDMP ``file``.

        Note that the support variables must also be ordered by their current
        level (lower level numbers first). To this end, you can use
        :meth:`set_var_order` with ``support_vars`` (or
        :attr:`file.support_var_order
        <oxidd.util.DDDMPFile.support_var_order>`).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            file (DDDMPFile): The DDDMP file handle
            support_vars (Iterable[int] | None): Optional mapping from support
                variables of the DDDMP file to variable numbers in this manager.
                By default, :attr:`file.support_var_order
                <oxidd.util.DDDMPFile.support_var_order>` will be used.

        Returns:
            list[BCDDFunction]: The imported BCDD functions
        """

    def export_dddmp(self, /, path: str | PathLike[str], functions: Iterable[BCDDFunction], *, version: DDDMPVersion = DDDMPVersion.V2_0, ascii: bool = False, strict: bool = True, diagram_name: str = "") -> None:
        """Export the given decision diagram functions as DDDMP file.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[BCDDFunction]): Functions to export (must be
                stored in this manager).
            version (DDDMPVersion): DDDMP format version to use
            ascii (bool): If ``True``, ASCII mode will be enforced for the
                export. By default (and if ``False``), binary mode will be used
                if supported for the decision diagram kind.
                Binary mode is currently supported for BCDDs only.
            strict (bool): If ``True`` (the default), enable `strict mode`_
            diagram_name (str): Name of the decision diagram

        Returns:
            None

        .. _`strict mode`: https://docs.rs/oxidd-dump/latest/oxidd_dump/dddmp/struct.ExportSettings.html#method.strict
        """

    def export_dddmp_with_names(self, /, path: str | PathLike[str], functions: Iterable[tuple[BCDDFunction, str]], *, version: DDDMPVersion = DDDMPVersion.V2_0, ascii: bool = False, strict: bool = True, diagram_name: str = "") -> None:
        """Export the given decision diagram functions as DDDMP file.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[BCDDFunction, str]]): Pairs of function
                and name. All functions must be stored in this manager.
            version (DDDMPVersion): DDDMP format version to use
            ascii (bool): If ``True``, ASCII mode will be enforced for the
                export. By default (and if ``False``), binary mode will be used
                if supported for the decision diagram kind.
                Binary mode is currently supported for BCDDs only.
            strict (bool): If ``True`` (the default), enable `strict mode`_
            diagram_name (str): Name of the decision diagram

        Returns:
            None

        .. _`strict mode`: https://docs.rs/oxidd-dump/latest/oxidd_dump/dddmp/struct.ExportSettings.html#method.strict
        """

    def visualize(self, /, diagram_name: str, functions: Iterable[BCDDFunction], *, port: int = 4000) -> None:
        """Serve the given decision diagram functions for visualization.

        Blocks until the visualization has been fetched by `OxiDD-vis`_ (or
        another compatible tool).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            diagram_name (str): Name of the decision diagram
            functions (Iterable[BCDDFunction]): Functions to visualize (must be
                stored in this manager)
            port (int): The port to provide the data on, defaults to 4000.

        Returns:
            None

        .. _OxiDD-vis: https://oxidd.net/vis
        """

    def visualize_with_names(self, /, diagram_name: str, functions: Iterable[tuple[BCDDFunction, str]], *, port: int = 4000) -> None:
        """Serve the given decision diagram functions for visualization.

        Blocks until the visualization has been fetched by `OxiDD-vis`_ (or
        another compatible tool).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            diagram_name (str): Name of the decision diagram
            functions (Iterable[tuple[BCDDFunction, str]]): Pairs of function
                and name. All functions must be stored in this manager.
            port (int): The port to provide the data on, defaults to 4000.

        Returns:
            None

        .. _OxiDD-vis: https://oxidd.net/vis
        """

    def dump_all_dot(self, /, path: str | PathLike[str], functions: Iterable[tuple[BCDDFunction, str]] = []) -> None:
        """Dump the entire decision diagram in this manager as Graphviz DOT code.

        The output may also include nodes that are not reachable from
        ``functions``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[BCDDFunction, str]]): Optional names for
                BCDD functions

        Returns:
            None
        """

    @deprecated("Use dump_all_dot instead")
    def dump_all_dot_file(self, /, path: str | PathLike[str], functions: Iterable[tuple[BCDDFunction, str]] = []) -> None:
        """Deprecated alias for :meth:`dump_all_dot`.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[BCDDFunction, str]]): Optional names for
                BCDD functions

        Returns:
            None

        .. deprecated:: 0.11
           Use :meth:`dump_all_dot` instead
        """

    def __eq__(self, /, rhs: object) -> bool: ...
    def __ne__(self, /, rhs: object) -> bool: ...
    def __hash__(self, /) -> int: ...


@final
class BCDDSubstitution:
    """Substitution mapping variables to replacement functions.

    Implements: :class:`~oxidd.protocols.FunctionSubst`
    """

    @classmethod
    def __new__(cls, /, pairs: Iterable[tuple[int, BCDDFunction]]) -> BCDDSubstitution:
        """Create a new substitution object for BCDDs.

        See :meth:`BCDDFunction.make_substitution` for more details.

        Args:
            pairs (Iterable[tuple[int, BCDDFunction]]):
                ``(variable, replacement)`` pairs, where all variables are
                distinct. The order of the pairs is irrelevant.

        Returns:
            BCDDSubstitution: The new substitution
        """


@final
class BCDDFunction:
    r"""Boolean function as binary decision diagram with complement edges (BCDD).

    Implements:
        :class:`~oxidd.protocols.BooleanFunctionQuant`,
        :class:`~oxidd.protocols.FunctionSubst`\ [:class:`BCDDSubstitution`],
        :class:`~oxidd.protocols.HasLevel`

    All operations constructing BCDDs may throw a
    :exc:`~oxidd.util.DDMemoryError` in case they run out of memory.

    Note that comparisons like ``f <= g`` are based on an arbitrary total order
    and not related to logical implications. See the
    :meth:`Function <oxidd.protocols.Function.__lt__>` protocol for more
    details.
    """

    @classmethod
    def __new__(cls, _: Never) -> Self:
        """Private constructor."""

    @property
    def manager(self, /) -> BCDDManager:
        """BCDDManager: The associated manager."""

    def cofactors(self, /) -> tuple[Self, Self] | None:
        r"""Get the cofactors ``(f_true, f_false)`` of ``self``.

        Let f(x₀, …, xₙ) be represented by ``self``, where x₀ is (currently) the
        top-most variable. Then f\ :sub:`true`\ (x₁, …, xₙ) = f(⊤, x₁, …, xₙ)
        and f\ :sub:`false`\ (x₁, …, xₙ) = f(⊥, x₁, …, xₙ).

        Structurally, the cofactors are simply the children in case with edge
        tags adjusted accordingly.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            tuple[Self, Self] | None: The cofactors ``(f_true, f_false)``, or
            ``None`` if ``self`` references a terminal node.

        See Also:
            :meth:`cofactor_true`, :meth:`cofactor_false` if you only need one
            of the cofactors.
        """

    def cofactor_true(self, /) -> Self | None:
        """Get the cofactor ``f_true`` of ``self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self | None: The cofactor ``f_true``, or ``None`` if ``self``
            references a terminal node.

        See Also:
            :meth:`cofactors`, also for a more detailed description
        """

    def cofactor_false(self, /) -> Self | None:
        """Get the cofactor ``f_false`` of ``self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self | None: The cofactor ``f_false``, or ``None`` if ``self``
            references a terminal node.

        See Also:
            :meth:`cofactors`, also for a more detailed description
        """

    def node_level(self, /) -> int | None:
        """Get the level of the underlying node.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            int | None: The level, or ``None`` if the node is a terminal
        """

    @deprecated("Use node_level instead")
    def level(self, /) -> int | None:
        """Deprecated alias for :meth:`node_level`.

        Returns:
            int | None: The level, or ``None`` if the node is a terminal

        .. deprecated:: 0.11
           Use :meth:`node_level` instead
        """

    def node_var(self, /) -> int | None:
        """Get the variable number for the underlying node.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            int | None: The variable number, or ``None`` if the node is a
            terminal
        """

    def __invert__(self, /) -> Self:
        """Compute the negation ``¬self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self: ``¬self``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __and__(self, rhs: Self, /) -> Self:
        """Compute the conjunction ``self ∧ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ∧ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __or__(self, rhs: Self, /) -> Self:
        """Compute the disjunction ``self ∨ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ∨ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __xor__(self, rhs: Self, /) -> Self:
        """Compute the exclusive disjunction ``self ⊕ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊕ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def nand(self, rhs: Self, /) -> Self:
        """Compute the negated conjunction ``self ⊼ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊼ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def nor(self, rhs: Self, /) -> Self:
        """Compute the negated disjunction ``self ⊽ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊽ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def equiv(self, rhs: Self, /) -> Self:
        """Compute the equivalence ``self ↔ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ↔ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def imp(self, rhs: Self, /) -> Self:
        """Compute the implication ``self → rhs`` (or ``f ≤ g``).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self → rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def imp_strict(self, rhs: Self, /) -> Self:
        """Compute the strict implication ``self < rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self < rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def ite(self, /, t: Self, e: Self) -> Self:
        """Compute the BCDD for the conditional ``t if self else e``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            t (Self): Then-case; must belong to the same manager as ``self``
            e (Self): Else-case; must belong to the same manager as ``self``

        Returns:
            Self: The Boolean function ``f(v: 𝔹ⁿ) = t(v) if self(v) else e(v)``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    @classmethod
    def make_substitution(cls, pairs: Iterable[tuple[int, Self]], /) -> BCDDSubstitution:
        """Create a new substitution object from pairs ``(var, replacement)``.

        The intent behind substitution objects is to optimize the case where the
        same substitution is applied multiple times. We would like to re-use
        apply cache entries across these operations, and therefore, we need a
        compact identifier for the substitution. This identifier is provided by
        the returned substitution object.

        Args:
            pairs (Iterable[tuple[int, Self]]): ``(variable, replacement)``
                pairs, where all variables are distinct. The order of the pairs
                is irrelevant.

        Returns:
            BCDDSubstitution: The substitution to be used with
            :meth:`substitute`
        """

    def substitute(self, substitution: BCDDSubstitution, /) -> Self:
        """Substitute variables in ``self`` according to ``substitution``.

        The substitution is performed in a parallel fashion, e.g.:
        ``(¬x ∧ ¬y)[x ↦ ¬x ∧ ¬y, y ↦ ⊥] = ¬(¬x ∧ ¬y) ∧ ¬⊥ = x ∨ y``

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            substitution (BCDDSubstitution): A substitution object created using
                :meth:`make_substitution`. All contained DD functions must
                belong to the same manager as ``self``.

        Returns:
            Self: ``self`` with variables substituted
        """

    def forall(self, /, vars: Self) -> Self:
        """Compute the universal quantification over ``vars``.

        This operation removes all occurrences of variables in ``vars`` by
        universal quantification. Universal quantification ∀x. f(…, x, …) of a
        Boolean function f(…, x, …) over a single variable x is
        f(…, 0, …) ∧ f(…, 1, …).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∀ vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def exists(self, /, vars: Self) -> Self:
        """Compute the existential quantification over ``vars``.

        This operation removes all occurrences of variables in ``vars`` by
        existential quantification. Existential quantification ∃x. f(…, x, …) of
        a Boolean function f(…, x, …) over a single variable x is
        f(…, 0, …) ∨ f(…, 1, …).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∃ vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    @deprecated("Use exists instead")
    def exist(self, /, vars: Self) -> Self:
        """Deprecated alias for :meth:`exists`.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∃ vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory

        .. deprecated:: 0.10
           Use :meth:`exists` instead
        """

    def unique(self, /, vars: Self) -> Self:
        """Compute the unique quantification over ``vars``.

        This operation removes all occurrences of variables in ``vars`` by
        unique quantification. Unique quantification ∃!x. f(…, x, …) of a
        Boolean function f(…, x, …) over a single variable x is
        f(…, 0, …) ⊕ f(…, 1, …). Unique quantification is also known as the
        `Boolean difference <https://en.wikipedia.org/wiki/Boole%27s_expansion_theorem#Operations_with_cofactors>`_ or
        `Boolean derivative <https://en.wikipedia.org/wiki/Boolean_differential_calculus>`_.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (Self): Set of variables represented as conjunction thereof.
                Must belong to the same manager as ``self``.

        Returns:
            Self: ∃! vars: self

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def apply_forall(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Combined application of ``op`` and :meth:`forall`.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∀ vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def apply_exists(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Combined application of ``op`` and :meth:`exists`.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∃ vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    @deprecated("Use apply_exists instead")
    def apply_exist(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Deprecated alias for :meth:`apply_exists`.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∃ vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory

        .. deprecated:: 0.10
           Use :meth:`apply_exists` instead
        """

    def apply_unique(self, /, op: BooleanOperator, rhs: Self, vars: Self) -> Self:
        """Combined application of ``op`` and :meth:`unique`.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            op (BooleanOperator): Binary Boolean operator to apply to ``self``
                and ``rhs``
            rhs (Self): Right-hand side of the operator. Must belong to the same
                manager as ``self``.
            vars (Self): Set of variables to quantify over. Represented as
                conjunction of variables. Must belong to the same manager as
                ``self``.

        Returns:
            Self: ``∃! vars. self <op> rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def node_count(self, /) -> int:
        """Get the number of descendant nodes.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The count of descendant nodes including the node referenced by
            ``self`` and terminal nodes.
        """

    def satisfiable(self, /) -> bool:
        """Check for satisfiability.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            bool: Whether the Boolean function has at least one satisfying
            assignment
        """

    def valid(self, /) -> bool:
        """Check for validity.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            bool: Whether all assignments satisfy the Boolean function
        """

    def sat_count(self, /, vars: int) -> int:
        """Count the number of satisfying assignments.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (int): Assume that the function's domain has this many
                variables.

        Returns:
            int: The exact number of satisfying assignments
        """

    def sat_count_float(self, /, vars: int) -> float:
        """Count the number of satisfying assignments.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (int): Assume that the function's domain has this many
                variables.

        Returns:
            float: (An approximation of) the number of satisfying assignments
        """

    def pick_cube(self, /) -> list[bool | None] | None:
        """Pick a satisfying assignment.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            list[bool | None] | None: The satisfying assignment where the i-th
            value means that the i-th variable is false, true, or "don't care,"
            respectively, or ``None`` if ``self`` is unsatisfiable
        """

    def pick_cube_dd(self, /) -> Self:
        """Pick a satisfying assignment, represented as decision diagram.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            Self: The satisfying assignment as decision diagram, or ``⊥`` if
            ``self`` is unsatisfiable
        """

    def pick_cube_dd_set(self, /, literal_set: Self) -> Self:
        """Pick a satisfying assignment as DD, with choices as of ``literal_set``.

        ``literal_set`` is a conjunction of literals. Whenever there is a choice
        for a variable, it will be set to true if the variable has a positive
        occurrence in ``literal_set``, and set to false if it occurs negated in
        ``literal_set``. If the variable does not occur in ``literal_set``, then
        it will be left as don't care if possible, otherwise an arbitrary (not
        necessarily random) choice will be performed.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            literal_set (Self): Conjunction of literals to determine the choice
                for variables

        Returns:
            Self: The satisfying assignment as decision diagram, or ``⊥`` if
            ``self`` is unsatisfiable

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def eval(self, /, args: Iterable[tuple[int, bool]]) -> bool:
        """Evaluate this Boolean function with arguments ``args``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            args (Iterable[tuple[int, bool]]): ``(variable, value)`` pairs that
                determine the valuation for all variables in the function's
                domain. The order is irrelevant (except that if the valuation
                for a variable is given multiple times, the last value counts).
                Should there be a decision node for a variable not part of the
                domain, then ``False`` is used as the decision value.

        Returns:
            bool: The result of applying the function ``self`` to ``args``

        Raises:
            IndexError: If any variable number in ``args`` is greater or equal
                to ``self.manager.num_vars()``
        """

    def __eq__(self, /, rhs: object) -> bool: ...
    def __ne__(self, /, rhs: object) -> bool: ...
    def __le__(self, /, rhs: Self) -> bool: ...
    def __lt__(self, /, rhs: Self) -> bool: ...
    def __ge__(self, /, rhs: Self) -> bool: ...
    def __gt__(self, /, rhs: Self) -> bool: ...
    def __hash__(self, /) -> int: ...


@final
class ZBDDManager:
    r"""Manager for zero-suppressed binary decision diagrams.

    Implements: :class:`~oxidd.protocols.BooleanFunctionManager`\
    [:class`ZBDDFunction`]
    """

    @classmethod
    def __new__(cls, /, inner_node_capacity: int, apply_cache_capacity: int, threads: int) -> ZBDDManager:
        """Create a new manager.

        Args:
            inner_node_capacity (int): Maximum count of inner nodes
            apply_cache_capacity (int): Maximum count of apply cache entries
            threads (int): Worker thread count for the internal thread pool

        Returns:
            ZBDDManager: The new manager
        """

    def num_inner_nodes(self, /) -> int:
        """Get the count of inner nodes.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of inner nodes stored in this manager
        """

    def approx_num_inner_nodes(self, /) -> int:
        """Get an approximate count of inner nodes.

        For concurrent implementations, it may be much less costly to determine
        an approximation of the inner node count than an accurate count
        (:meth:`num_inner_nodes`).

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: An approximate count of inner nodes stored in this manager
        """

    def num_vars(self, /) -> int:
        """Get the number of variables in this manager.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of variables
        """

    def num_named_vars(self, /) -> int:
        """Get the number of named variables in this manager.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The number of named variables
        """

    def add_vars(self, /, additional: int) -> range:
        """Add ``additional`` unnamed variables to the decision diagram.

        The new variables are added at the bottom of the variable order. More
        precisely, the level number equals the variable number for each new
        variable.

        Note that some algorithms may assume that the domain of a function
        represented by a decision diagram is just the set of all variables. In
        this regard, adding variables can change the semantics of decision
        diagram nodes.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            additional (int): Count of variables to add

        Returns:
            range: The new variable numbers
        """

    def add_named_vars(self, /, names: Iterable[str]) -> range:
        """Add named variables to the decision diagram.

        This is a shorthand for :meth:`add_vars` and respective
        :meth:`set_var_name` calls. More details can be found there.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            names (Iterable[str]): Names of the new variables

        Returns:
            range: The new variable numbers

        Raises:
            ValueError: If a variable name occurs twice in ``names``. The
                exception's argument is a :class:`DuplicateVarName`.
        """

    def var_name(self, /, var: int) -> str:
        """Get ``var``'s name.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int): The variable number

        Returns:
            str: The name, or an empty string for unnamed variables

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def set_var_name(self, /, var: int, name: str) -> None:
        """Label ``var`` as ``name``.

        An empty name means that the variable will become unnamed, and cannot be
        retrieved via :meth:`name_to_var` anymore.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            var (int): The variable number
            name (str): The new variable name

        Returns:
            None

        Raises:
            ValueError: If ``name`` is not unique (and not ``""``). The
                exception's argument is a :class:`DuplicateVarName`.
            IndexError: If ``var >= self.num_vars()``
        """

    def name_to_var(self, /, name: str) -> int | None:
        """Get the variable number for the given variable name, if present.

        Note that you cannot retrieve unnamed variables.
        ``manager.name_to_var("")`` always returns ``None``.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            name (str): The variable name

        Returns:
            int | None: The variable number if found, or ``None``
        """

    def var_to_level(self, /, var: int) -> int:
        """Get the level for the given variable.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int): The variable number

        Returns:
            int: The level number

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def level_to_var(self, /, level: int) -> int:
        """Get the variable for the given level.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            level (int): The level number

        Returns:
            int: The variable number

        Raises:
            IndexError: If ``var >= self.num_vars()``
        """

    def gc(self, /) -> int:
        """Perform garbage collection.

        This method looks for nodes that are neither referenced by a
        :class:`ZBDDFunction` nor another node and removes them. The method
        works from top to bottom, so if a node is only referenced by nodes
        that can be removed, this node will be removed as well.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The count of nodes removed
        """

    def gc_count(self, /) -> int:
        """Get the count of garbage collections.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The garbage collection count
        """

    def singleton(self, /, var: int | str) -> ZBDDFunction:
        """Get the singleton set {var}.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int | str): The variable number or name

        Returns:
            ZBDDFunction: The singleton set {var}

        Raises:
            DDMemoryError: If the operation runs out of memory
            IndexError: If ``var`` is an ``int`` and ``var >= self.num_vars()``
            KeyError: If ``var`` is a string and
                ``self.name_to_var(var) is None``
        """

    def var(self, /, var: int | str) -> ZBDDFunction:
        """Get the Boolean function that is true if and only if ``var`` is true.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int | str): The variable number or name

        Returns:
            ZBDDFunction: A Boolean function that is true if and only if the
            variable is true

        Raises:
            DDMemoryError: If the operation runs out of memory
            IndexError: If ``var`` is an ``int`` and ``var >= self.num_vars()``
            KeyError: If ``var`` is a string and
                ``self.name_to_var(var) is None``
        """

    def not_var(self, /, var: int | str) -> ZBDDFunction:
        """Get the Boolean function that is true if and only if ``var`` is false.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            var (int | str): The variable number or name

        Returns:
            ZBDDFunction: A Boolean function that is true if and only if the
            variable is false

        Raises:
            DDMemoryError: If the operation runs out of memory
            IndexError: If ``var`` is an ``int`` and ``var >= self.num_vars()``
            KeyError: If ``var`` is a string and
                ``self.name_to_var(var) is None``
        """

    def empty(self, /) -> ZBDDFunction:
        """Get the ZBDD set ∅.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            ZBDDFunction: The set `∅` (or equivalently `⊥`)
        """

    def base(self, /) -> ZBDDFunction:
        """Get the ZBDD set {∅}.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            ZBDDFunction: The set `{∅}`
        """

    def true(self, /) -> ZBDDFunction:
        """Get the constant true Boolean function ``⊤``.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            ZBDDFunction: The constant true Boolean function ``⊤``
        """

    def false(self, /) -> ZBDDFunction:
        """Get the constant false Boolean function ``⊥``.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            ZBDDFunction: The constant false Boolean function ``⊥``
        """

    def set_var_order(self, /, order: Iterable[int]) -> None:
        """Reorder the variables according to ``order``.

        If a variable ``x`` occurs before variable ``y`` in ``order``, then
        ``x`` will be above ``y`` in the decision diagram when this function
        returns. Variables not mentioned in ``order`` will be placed in a
        position such that the least number of level swaps need to be
        performed.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            order (Iterable[int]): The variable order to establish

        Returns:
            None
        """

    def import_dddmp(self, /, file: DDDMPFile, support_vars: Iterable[int] | None = None) -> list[ZBDDFunction]:
        """Import the decision diagram from the DDDMP ``file``.

        Note that the support variables must also be ordered by their current
        level (lower level numbers first). To this end, you can use
        :meth:`set_var_order` with ``support_vars`` (or
        :attr:`file.support_var_order
        <oxidd.util.DDDMPFile.support_var_order>`).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            file (DDDMPFile): The DDDMP file handle
            support_vars (Iterable[int] | None): Optional mapping from support
                variables of the DDDMP file to variable numbers in this manager.
                By default, :attr:`file.support_var_order
                <oxidd.util.DDDMPFile.support_var_order>` will be used.

        Returns:
            list[ZBDDFunction]: The imported ZBDD functions
        """

    def export_dddmp(self, /, path: str | PathLike[str], functions: Iterable[ZBDDFunction], *, version: DDDMPVersion = DDDMPVersion.V2_0, ascii: bool = False, strict: bool = True, diagram_name: str = "") -> None:
        """Export the given decision diagram functions as DDDMP file.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[ZBDDFunction]): Functions to export (must be
                stored in this manager).
            version (DDDMPVersion): DDDMP format version to use
            ascii (bool): If ``True``, ASCII mode will be enforced for the
                export. By default (and if ``False``), binary mode will be used
                if supported for the decision diagram kind.
                Binary mode is currently supported for BCDDs only.
            strict (bool): If ``True`` (the default), enable `strict mode`_
            diagram_name (str): Name of the decision diagram

        Returns:
            None

        .. _`strict mode`: https://docs.rs/oxidd-dump/latest/oxidd_dump/dddmp/struct.ExportSettings.html#method.strict
        """

    def export_dddmp_with_names(self, /, path: str | PathLike[str], functions: Iterable[tuple[ZBDDFunction, str]], *, version: DDDMPVersion = DDDMPVersion.V2_0, ascii: bool = False, strict: bool = True, diagram_name: str = "") -> None:
        """Export the given decision diagram functions as DDDMP file.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[ZBDDFunction, str]]): Pairs of function
                and name. All functions must be stored in this manager.
            version (DDDMPVersion): DDDMP format version to use
            ascii (bool): If ``True``, ASCII mode will be enforced for the
                export. By default (and if ``False``), binary mode will be used
                if supported for the decision diagram kind.
                Binary mode is currently supported for BCDDs only.
            strict (bool): If ``True`` (the default), enable `strict mode`_
            diagram_name (str): Name of the decision diagram

        Returns:
            None

        .. _`strict mode`: https://docs.rs/oxidd-dump/latest/oxidd_dump/dddmp/struct.ExportSettings.html#method.strict
        """

    def visualize(self, /, diagram_name: str, functions: Iterable[ZBDDFunction], *, port: int = 4000) -> None:
        """Serve the given decision diagram functions for visualization.

        Blocks until the visualization has been fetched by `OxiDD-vis`_ (or
        another compatible tool).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            diagram_name (str): Name of the decision diagram
            functions (Iterable[ZBDDFunction]): Functions to visualize (must be
                stored in this manager)
            port (int): The port to provide the data on, defaults to 4000.

        Returns:
            None

        .. _OxiDD-vis: https://oxidd.net/vis
        """

    def visualize_with_names(self, /, diagram_name: str, functions: Iterable[tuple[ZBDDFunction, str]], *, port: int = 4000) -> None:
        """Serve the given decision diagram functions for visualization.

        Blocks until the visualization has been fetched by `OxiDD-vis`_ (or
        another compatible tool).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            diagram_name (str): Name of the decision diagram
            functions (Iterable[tuple[ZBDDFunction, str]]): Pairs of function
                and name. All functions must be stored in this manager.
            port (int): The port to provide the data on, defaults to 4000.

        Returns:
            None

        .. _OxiDD-vis: https://oxidd.net/vis
        """

    def dump_all_dot(self, /, path: str | PathLike[str], functions: Iterable[tuple[ZBDDFunction, str]] = []) -> None:
        """Dump the entire decision diagram in this manager as Graphviz DOT code.

        The output may also include nodes that are not reachable from
        ``functions``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[ZBDDFunction, str]]): Optional names for
                ZBDD functions

        Returns:
            None
        """

    @deprecated("Use dump_all_dot instead")
    def dump_all_dot_file(self, /, path: str | PathLike[str], functions: Iterable[tuple[ZBDDFunction, str]] = []) -> None:
        """Deprecated alias for :meth:`dump_all_dot`.

        Args:
            path (str | PathLike[str]): Path of the output file. If a file at
                ``path`` exists, it will be overwritten, otherwise a new one
                will be created.
            functions (Iterable[tuple[ZBDDFunction, str]]): Optional names for
                BCDD functions

        Returns:
            None

        .. deprecated:: 0.11
           Use :meth:`dump_all_dot` instead
        """

    def __eq__(self, /, rhs: object) -> bool: ...
    def __ne__(self, /, rhs: object) -> bool: ...
    def __hash__(self, /) -> int: ...


@final
class ZBDDFunction:
    """Boolean function as zero-suppressed binary decision diagram (ZBDD).

    Implements:
        :class:`~oxidd.protocols.BooleanFunction`,
        :class:`~oxidd.protocols.HasLevel`

    All operations constructing ZBDDs may throw a
    :exc:`~oxidd.util.DDMemoryError` in case they run out of memory.

    Note that comparisons like ``f <= g`` are based on an arbitrary total order
    and not related to logical implications. See the
    :meth:`Function <oxidd.protocols.Function.__lt__>` protocol for more
    details.
    """

    @classmethod
    def __new__(cls, _: Never) -> Self:
        """Private constructor."""

    @property
    def manager(self, /) -> ZBDDManager:
        """ZBDDManager: The associated manager."""

    def cofactors(self, /) -> tuple[Self, Self] | None:
        r"""Get the cofactors ``(f_true, f_false)`` of ``self``.

        Let f(x₀, …, xₙ) be represented by ``self``, where x₀ is (currently) the
        top-most variable. Then f\ :sub:`true`\ (x₁, …, xₙ) = f(⊤, x₁, …, xₙ)
        and f\ :sub:`false`\ (x₁, …, xₙ) = f(⊥, x₁, …, xₙ).

        Note that the domain of f is 𝔹\ :sup:`n+1` while the domain of
        f\ :sub:`true` and f\ :sub:`false` is 𝔹\ :sup:`n`. This is irrelevant in
        case of BDDs and BCDDs, but not for ZBDDs: For instance, g(x₀) = x₀ and
        g'(x₀, x₁) = x₀ have the same representation as BDDs or BCDDs, but
        different representations as ZBDDs.

        Structurally, the cofactors are simply the children in case with edge
        tags adjusted accordingly.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            tuple[Self, Self] | None: The cofactors ``(f_true, f_false)``, or
            ``None`` if ``self`` references a terminal node.

        See Also:
            :meth:`cofactor_true`, :meth:`cofactor_false` if you only need one
            of the cofactors.
        """

    def cofactor_true(self, /) -> Self | None:
        """Get the cofactor ``f_true`` of ``self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self | None: The cofactor ``f_true``, or ``None`` if ``self``
            references a terminal node.

        See Also:
            :meth:`cofactors`, also for a more detailed description
        """

    def cofactor_false(self, /) -> Self | None:
        """Get the cofactor ``f_false`` of ``self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self | None: The cofactor ``f_false``, or ``None`` if ``self``
            references a terminal node.

        See Also:
            :meth:`cofactors`, also for a more detailed description
        """

    def node_level(self, /) -> int | None:
        """Get the level of the underlying node.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            int | None: The level, or ``None`` if the node is a terminal
        """

    @deprecated("Use node_level instead")
    def level(self, /) -> int | None:
        """Deprecated alias for :meth:`node_level`.

        Returns:
            int | None: The level, or ``None`` if the node is a terminal

        .. deprecated:: 0.11
           Use :meth:`node_level` instead
        """

    def node_var(self, /) -> int | None:
        """Get the variable number for the underlying node.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            int | None: The variable number, or ``None`` if the node is a
            terminal
        """

    @deprecated("Use ZBDDManager.var instead")
    def var_boolean_function(self, /) -> Self:
        """Get the Boolean function v for the singleton set {v}.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            Self: The Boolean function ``v`` as ZBDD

        Raises:
            DDMemoryError: If the operation runs out of memory

        .. deprecated:: 0.11
           Use :meth:`ZBDDManager.var` instead
        """

    def subset0(self, /, var: int) -> Self:
        """Get the subset of ``self`` not containing ``var``.

        Locking behavior: acquires a shared manager lock

        Args:
            var (int):  The variable

        Returns:
            Self: ``{s ∈ self | {var} ∉ s}``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def subset1(self, /, var: int) -> Self:
        """Get the subset of ``self`` containing ``var``, with ``var`` removed.

        Locking behavior: acquires a shared manager lock

        Args:
            var (int):  The variable

        Returns:
            Self: ``{s ∖ {{var}} | s ∈ self ∧ {var} ∈ s}``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def change(self, /, var: int) -> Self:
        """Swap :meth:`subset0` and :meth:`subset1` with respect to ``var``.

        Locking behavior: acquires a shared manager lock

        Args:
            var (int): The variable

        Returns:
            Self: ``{s ∪ {{var}} | s ∈ self ∧ {var} ∉ s}
            ∪ {s ∖ {{var}} | s ∈ self ∧ {var} ∈ s}``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __invert__(self, /) -> Self:
        """Compute the negation ``¬self``.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            Self: ``¬self``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __and__(self, rhs: Self, /) -> Self:
        """Compute the conjunction ``self ∧ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ∧ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __or__(self, rhs: Self, /) -> Self:
        """Compute the disjunction ``self ∨ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ∨ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __xor__(self, rhs: Self, /) -> Self:
        """Compute the exclusive disjunction ``self ⊕ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊕ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def __sub__(self, rhs: Self, /) -> Self:
        """Compute the set difference ``self ∖ rhs``.

        Locking behavior: acquires the manager's lock for exclusive access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ∖ rhs``, or equivalently ``rhs.strict_imp(self)``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def nand(self, rhs: Self, /) -> Self:
        """Compute the negated conjunction ``self ⊼ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊼ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def nor(self, rhs: Self, /) -> Self:
        """Compute the negated disjunction ``self ⊽ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ⊽ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def equiv(self, rhs: Self, /) -> Self:
        """Compute the equivalence ``self ↔ rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self ↔ rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def imp(self, rhs: Self, /) -> Self:
        """Compute the implication ``self → rhs`` (or ``f ≤ g``).

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self → rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def imp_strict(self, rhs: Self, /) -> Self:
        """Compute the strict implication ``self < rhs``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            rhs (Self): Right-hand side operand. Must belong to the same manager
                as ``self``

        Returns:
            Self: ``self < rhs``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def ite(self, /, t: Self, e: Self) -> Self:
        """Compute the ZBDD for the conditional ``t if self else e``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            t (Self): Then-case; must belong to the same manager as ``self``
            e (Self): Else-case; must belong to the same manager as ``self``

        Returns:
            Self: The Boolean function ``f(v: 𝔹ⁿ) = t(v) if self(v) else e(v)``

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def make_node(self, /, hi: Self, lo: Self) -> Self:
        """Create a node at ``self``'s level with edges ``hi`` and ``lo``.

        ``self`` must be a singleton set at a level above the top level of
        ``hi`` and ``lo``.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            hi (Self): Edge for the case where the variable is true; must belong
                to the same manager as ``self``
            lo (Self): Edge for the case where the variable is false; must
                belong to the same manager as ``self``

        Returns:
            Self: The new ZBDD node

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def node_count(self, /) -> int:
        """Get the number of descendant nodes.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            int: The count of descendant nodes including the node referenced by
            ``self`` and terminal nodes.
        """

    def satisfiable(self, /) -> bool:
        """Check for satisfiability.

        Locking behavior: acquires the manager's lock for shared access.

        Time complexity: O(1)

        Returns:
            bool: Whether the Boolean function has at least one satisfying
            assignment
        """

    def valid(self, /) -> bool:
        """Check for validity.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            bool: Whether all assignments satisfy the Boolean function
        """

    def sat_count(self, /, vars: int) -> int:
        """Count the number of satisfying assignments.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (int): Assume that the function's domain has this many
                variables.

        Returns:
            int: The exact number of satisfying assignments
        """

    def sat_count_float(self, /, vars: int) -> float:
        """Count the number of satisfying assignments.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            vars (int): Assume that the function's domain has this many
                variables.

        Returns:
            float: (An approximation of) the number of satisfying assignments
        """

    def pick_cube(self, /) -> list[bool | None] | None:
        """Pick a satisfying assignment.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            list[bool | None] | None: The satisfying assignment where the i-th
            value means that the i-th variable is false, true, or "don't care,"
            respectively, or ``None`` if ``self`` is unsatisfiable
        """

    def pick_cube_dd(self, /) -> Self:
        """Pick a satisfying assignment, represented as decision diagram.

        Locking behavior: acquires the manager's lock for shared access.

        Returns:
            Self: The satisfying assignment as decision diagram, or ``⊥`` if
            ``self`` is unsatisfiable
        """

    def pick_cube_dd_set(self, /, literal_set: Self) -> Self:
        """Pick a satisfying assignment as DD, with choices as of ``literal_set``.

        ``literal_set`` is a conjunction of literals. Whenever there is a choice
        for a variable, it will be set to true if the variable has a positive
        occurrence in ``literal_set``, and set to false if it occurs negated in
        ``literal_set``. If the variable does not occur in ``literal_set``, then
        it will be left as don't care if possible, otherwise an arbitrary (not
        necessarily random) choice will be performed.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            literal_set (Self): Conjunction of literals to determine the choice
                for variables

        Returns:
            Self: The satisfying assignment as decision diagram, or ``⊥`` if
            ``self`` is unsatisfiable

        Raises:
            DDMemoryError: If the operation runs out of memory
        """

    def eval(self, /, args: Iterable[tuple[int, bool]]) -> bool:
        """Evaluate this Boolean function with arguments ``args``.

        Note that the domain of the Boolean function represented by ``self`` is
        implicit and may comprise a strict subset of the variables in the
        manager only. This method assumes that the function's domain
        corresponds the set of variables in ``args``. Remember that for ZBDDs,
        the domain plays a crucial role for the interpretation of decision
        diagram nodes as a Boolean function. This is in contrast to, e.g.,
        ordinary BDDs, where extending the domain does not affect the
        evaluation result.

        Locking behavior: acquires the manager's lock for shared access.

        Args:
            args (Iterable[tuple[int, bool]]): ``(variable, value)`` pairs that
                determine the valuation for all variables in the function's
                domain. The order is irrelevant (except that if the valuation
                for a variable is given multiple times, the last value counts).
                Should there be a decision node for a variable not part of the
                domain, then ``False`` is used as the decision value.

        Returns:
            bool: The result of applying the function ``self`` to ``args``

        Raises:
            IndexError: If any variable number in ``args`` is greater or equal
                to ``self.manager.num_vars()``
        """

    def __eq__(self, /, rhs: object) -> bool: ...
    def __ne__(self, /, rhs: object) -> bool: ...
    def __le__(self, /, rhs: Self) -> bool: ...
    def __lt__(self, /, rhs: Self) -> bool: ...
    def __ge__(self, /, rhs: Self) -> bool: ...
    def __gt__(self, /, rhs: Self) -> bool: ...
    def __hash__(self, /) -> int: ...


class DDMemoryError(MemoryError):
    """Exception that is raised in case a DD operation runs out of memory."""


@final
class DuplicateVarName:
    """Error details for labelling a variable with a name that is already in use."""

    @classmethod
    def __new__(cls, _: Never) -> Self:
        """Private constructor."""

    @property
    def name(self, /) -> str:
        """str: The variable name."""

    @property
    def present_var(self, /) -> int:
        """int: Variable number already using the name."""

    @property
    def added_vars(self, /) -> range:
        """range: Range of variables successfully added before the error occurred."""

    def __repr__(self, /) -> str:
        """Get a string representation.

        Returns:
            str: The string representation.
        """

    def __eq__(self, /, rhs: object) -> bool: ...
    def __ne__(self, /, rhs: object) -> bool: ...
    def __hash__(self, /) -> int: ...


@final
class DDDMPFile:
    """DDDMP header loaded as the first step of an import process."""

    @classmethod
    def __new__(cls, /, path: str | PathLike[str]) -> DDDMPFile:
        """Load a DDDMP header from file.

        Args:
            path (str | PathLike[str]): Path to the DDDMP file

        Returns:
            DDDMPFile: The loaded DDDMP header
        """

    def close(self, /) -> None:
        """Close the file handle.

        If the file is already close, this is a no-op.

        Returns:
            None
        """

    def __enter__(self, /) -> Self:
        """Enter the runtime context related to this object.

        This is a no-op.

        Returns:
            Self: This object
        """

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None, /) -> bool:
        """Exit the runtime context related to this object.

        Closes the associated file handle (via :meth:`close`).

        Args:
            exc_type (type[BaseException] | None): The exception type if an
                exception was raised within the context, or ``None``
            exc_value (BaseException | None): The exception that was raised
                within the context, or ``None``
            traceback (TracebackType | None): The traceback related to the
                exception raised within the context, or ``None``

        Returns:
            bool: ``True`` iff the exception should be suppressed
        """

    @property
    def diagram_name(self, /) -> str | None:
        """str | None: Name of the decision diagram.

        Corresponds to the DDDMP ``.dd`` field.
        """

    @property
    def num_nodes(self, /) -> int:
        """int: Number of nodes in the dumped decision diagram.

        Corresponds to the DDDMP ``.nnodes`` field.
        """

    @property
    def num_vars(self, /) -> int:
        """int: Number of all variables in the exported decision.

        Corresponds to the DDDMP ``.nvars`` field.
        """

    @property
    def num_support_vars(self, /) -> int:
        """int: Number of variables in the true support of the decision diagram.

        Corresponds to the DDDMP ``.nsuppvars`` field.
        """

    @property
    def support_vars(self, /) -> list[int]:
        """list[int]: Variables in the true support of the decision diagram.

        Concretely, these are indices of the original variable numbering. Hence,
        the list contains :attr:`num_support_vars` integers in strictly
        ascending order.

        .. admonition:: Example

           Consider a decision diagram that was created with the variables
           ``x``, ``y``, and ``z``, in this order (``x`` is the top-most
           variable). Suppose that only ``y`` and ``z`` are used by the dumped
           functions. Then, this value is ``[1, 2]``, regardless of any
           subsequent reordering.

        Corresponds to the DDDMP ``.ids`` field.
        """

    @property
    def support_var_order(self, /) -> list[int]:
        """list[int]: Order of the support variables.

        This list is always :attr:`num_support_vars` elements long and
        represents a mapping from positions to variable numbers.

        .. admonition:: Example

           Consider a decision diagram that was created with the variables
           ``x``, ``y``, and ``z`` (``x`` is the top-most variable). The
           variables were re-ordered to ``z``, ``x``, ``y``. Suppose that only
           ``y`` and ``z`` are used by the dumped functions. Then, this value is
           ``[2, 1]``.
        """

    @property
    def support_var_to_level(self, /) -> list[int]:
        r"""list[int]: Mapping from the support variables to levels.

        This list is always :attr:`num_support_vars` elements long. If the value
        at index ``i`` is ``l``, then the ``i``\ th support variable is at level
        ``l`` in the dumped decision diagram. By the ``i``\ th support variable,
        we mean the variable ``header.support_vars[i]`` in the original
        numbering.

        .. admonition:: Example

           Consider a decision diagram that was created with the variables
           ``x``, ``y``, and ``z`` (``x`` is the top-most variable). The
           variables were re-ordered to ``z``, ``x``, ``y``. Suppose that only
           ``y`` and ``z`` are used by the dumped functions. Then, this value is
           ``[2, 0]``.

        Corresponds to the DDDMP ``.permids`` field.
        """

    @property
    def auxiliary_var_ids(self, /) -> list[int]:
        """list[int]: Auxiliary variable IDs.

        This list contains :attr:`num_support_vars` elements.

        Corresponds to the DDDMP ``.auxids`` field.
        """

    @property
    def var_names(self, /) -> list[str] | None:
        """list[str] | None: Names of all variables in the decision diagram.

        If present, this list contains :attr:`num_support_vars` many elements.
        The order is the "original" variable order.

        Corresponds to the DDDMP ``.varnames`` field, but ``.orderedvarnames``
        and ``.suppvarnames`` are also considered if one of the fields is
        missing. All variable names are non-empty unless only
        ``.suppvarnames`` is given in the input (in which case only the
        names of support variables are non-empty). The return value is only
        ``None`` if neither of ``.varnames``, ``.orderedvarnames``, and
        ``.suppvarnames`` is present in the input.
        """

    @property
    def num_roots(self, /) -> int:
        """int: Number of roots.

        :meth:`Manager.import()` returns this number of roots on success.
        Corresponds to the DDDMP ``.nroots`` field.
        """

    @property
    def root_names(self, /) -> list[int] | None:
        """list[int] | None: Names of roots, if present.

        The order matches the one of the result of :meth:`Manager.import()`.

        Corresponds to the DDDMP ``.rootnames`` field.
        """
