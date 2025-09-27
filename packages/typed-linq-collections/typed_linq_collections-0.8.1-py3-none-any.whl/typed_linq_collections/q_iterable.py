from __future__ import annotations

from abc import ABC
from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Never, Self, overload

from typed_linq_collections._private_implementation_details import ops

# noinspection PyPep8Naming
from typed_linq_collections._private_implementation_details.q_zero_overhead_collection_contructors import ZeroImportOverheadConstructors as C
from typed_linq_collections._private_implementation_details.sort_instruction import SortInstruction
from typed_linq_collections.q_errors import EmptyIterableError

if TYPE_CHECKING:
    from decimal import Decimal
    from fractions import Fraction

    from _typeshed import SupportsRichComparison

    from typed_linq_collections._private_implementation_details.type_aliases import Action1, Func, Predicate, Selector
    from typed_linq_collections.collections.numeric.q_decimal_types import QDecimalIterable
    from typed_linq_collections.collections.numeric.q_float_types import QFloatIterable
    from typed_linq_collections.collections.numeric.q_fraction_types import QFractionIterable
    from typed_linq_collections.collections.numeric.q_int_types import QIntIterable
    from typed_linq_collections.collections.q_dict import QDict
    from typed_linq_collections.collections.q_frozen_set import QFrozenSet
    from typed_linq_collections.collections.q_key_value_pair import KeyValuePair
    from typed_linq_collections.collections.q_list import QList
    from typed_linq_collections.collections.q_sequence import QSequence
    from typed_linq_collections.collections.q_set import QSet
    from typed_linq_collections.q_cast import QCast
    from typed_linq_collections.q_grouping import QGrouping
    from typed_linq_collections.q_ordered_iterable import QOrderedIterable

def query[TItem](value: Iterable[TItem]) -> QIterable[TItem]: return C.caching_iterable(value)

# note to coders, you can trust that the methods on single lines do nothing except delegate to the corresponding operations method,
# or to ZeroImportOverheadConstructors, knowing that, keeping them on single lines make it easier to read through the definitions
class QIterable[T](Iterable[T], ABC):
    __slots__: tuple[str, ...] = ()
    @property
    def cast(self) -> QCast[T]: return C.cast(self)

    def _lazy(self, factory: Func[Iterable[T]]) -> QIterable[T]:
        return C.lazy_iterable(factory)

    # region  static factory methods
    @staticmethod
    def empty() -> QIterable[Never]: return C.empty_iterable()

    @staticmethod
    @overload
    def range(stop_before: int, /) -> QIntIterable:
        """Returns a QIntIterable with values from 0 to stop_before - 1"""

    @staticmethod
    @overload
    def range(start: int, stop_before: int, step: int = 1, /) -> QIntIterable:
        """Returns a QIntIterable with values from start to stop_before - 1 in steps of step, defaulting to 1 if step is omitted"""

    @staticmethod
    def range(start_or_stop_before: int, stop_before: int | None = None, step: int = 1, /) -> QIntIterable: return C.int_iterable(lambda: ops.range(start_or_stop_before, stop_before, step))

    @staticmethod
    def repeat[TElement](element: TElement, count: int) -> QIterable[TElement]:
        """Returns a QIterable with the given element repeated count times"""
        return C.lazy_iterable(lambda: ops.repeat(element, count))

    # endregion

    # region operations on the whole collection, not the items
    def qappend(self, item: T) -> QIterable[T]: return self._lazy(lambda: ops.append(self, item))
    def prepend(self, item: T) -> QIterable[T]: return self._lazy(lambda: ops.prepend(self, item))
    def concat(self, *others: Iterable[T]) -> QIterable[T]: return self._lazy(lambda: ops.concat(self, *others))
    # endregion

    # region functional programming helpers
    def pipe[TReturn](self, action: Selector[QIterable[T], TReturn]) -> TReturn: return ops.pipe(self, action)
    def for_each(self, action: Action1[T]) -> Self:
        for item in self: action(item)
        return self
    # endregion

    def as_iterable(self) -> QIterable[T]: return self

    # region typed convertions to access type specific functionality type checkers will only allow calls if the instance is the correct type

    def as_ints(self: QIterable[int]) -> QIntIterable: return ops.as_ints(self)
    def as_floats(self: QIterable[float]) -> QFloatIterable: return ops.as_floats(self)
    def as_fractions(self: QIterable[Fraction]) -> QFractionIterable: return ops.as_fractions(self)
    def as_decimals(self: QIterable[Decimal]) -> QDecimalIterable: return ops.as_decimals(self)

    # endregion

    # region set operations
    def qexcept(self, other: Iterable[T]) -> QIterable[T]: return self._lazy(lambda: ops.qexcept(self, other))
    def qexcept_by[TKey](self, keys: Iterable[TKey], key_selector: Selector[T, TKey]) -> QIterable[T]:
        """Alias for where_key_not_in, for consistency with other set operations and for those used to the .Net API. Consider using the more descriptive where_key_not_in instead."""
        return self.where_key_not_in(keys, key_selector)
    def where_key_not_in[TKey](self, keys: Iterable[TKey], key_selector: Selector[T, TKey]) -> QIterable[T]: return self._lazy(lambda: ops.where_key_not_in(self, keys, key_selector))
    def qunion(self, other: Iterable[T]) -> QIterable[T]: return self._lazy(lambda: ops.qunion(self, other))
    def qunion_by[TKey](self, other: Iterable[T], key_selector: Selector[T, TKey]) -> QIterable[T]: return self._lazy(lambda: ops.qunion_by(self, other, key_selector))
    def qintersect(self, other: Iterable[T]) -> QIterable[T]: return self._lazy(lambda: ops.qintersect(self, other))
    def qintersect_by[TKey](self, keys: Iterable[TKey], key_selector: Selector[T, TKey]) -> QIterable[T]:
        """Alias for where_key_in, for consistency with other set operations and for those used to the .Net API. Consider using the more descriptive where_key_in instead."""
        return self.where_key_in(keys, key_selector)
    def where_key_in[TKey](self, keys: Iterable[TKey], key_selector: Selector[T, TKey]) -> QIterable[T]: return self._lazy(lambda: ops.where_key_in(self, keys, key_selector))

    def contains(self, value: T) -> bool: return ops.contains(self, value)

    # endregion

    # region filtering
    def where(self, predicate: Predicate[T]) -> QIterable[T]: return self._lazy(lambda: ops.where(self, predicate))
    def where_not_none(self) -> QIterable[T]: return self._lazy(lambda: ops.where_not_none(self))

    def distinct(self) -> QIterable[T]: return self._lazy(lambda: ops.distinct(self))
    def distinct_by[TKey](self, key_selector: Selector[T, TKey]) -> QIterable[T]: return self._lazy(lambda: ops.distinct_by(self, key_selector))

    def take(self, count: int) -> QIterable[T]: return self._lazy(lambda: ops.take(self, count))
    def take_while(self, predicate: Predicate[T]) -> QIterable[T]: return self._lazy(lambda: ops.take_while(self, predicate))
    def take_last(self, count: int) -> QIterable[T]: return self._lazy(lambda: ops.take_last(self, count))
    def skip(self, count: int) -> QIterable[T]: return self._lazy(lambda: ops.skip(self, count))
    def skip_while(self, predicate: Predicate[T]) -> QIterable[T]: return self._lazy(lambda: ops.skip_while(self, predicate))
    def skip_last(self, count: int) -> QIterable[T]: return self._lazy(lambda: ops.skip_last(self, count))

    def of_type[TResult](self, target_type: type[TResult]) -> QIterable[TResult]: return C.lazy_iterable(lambda: ops.of_type(self, target_type))

    # endregion

    # region value queries
    def qcount_by[TKey](self, key_selector: Selector[T, TKey]) -> QIterable[KeyValuePair[TKey, int]]: return ops.qcount_by(self, key_selector)
    def qcount(self, predicate: Predicate[T] | None = None) -> int: return ops.qcount(self, predicate)
    def none(self, predicate: Predicate[T] | None = None) -> bool: return not ops.any(self, predicate)
    def any(self, predicate: Predicate[T] | None = None) -> bool: return ops.any(self, predicate)
    def all(self, predicate: Predicate[T]) -> bool: return ops.all(self, predicate)

    def sequence_equal(self, other: Iterable[T]) -> bool: return ops.sequence_equal(self, other)

    # endregion

    # region aggregation methods
    @overload
    def aggregate(self, func: Callable[[T, T], T]) -> T: ...

    @overload
    def aggregate[TAccumulate](self, func: Callable[[TAccumulate, T], TAccumulate], seed: TAccumulate) -> TAccumulate: ...

    @overload
    def aggregate[TAccumulate, TResult](self, func: Callable[[TAccumulate, T], TAccumulate], seed: TAccumulate, select: Selector[TAccumulate, TResult]) -> TResult: ...

    def aggregate[TAccumulate, TResult](self, func: Callable[[T, T], T] | Callable[[TAccumulate, T], TAccumulate],
                                        seed: TAccumulate | None = None,
                                        select: Selector[TAccumulate, TResult] | None = None) -> T | TAccumulate | TResult:
        return ops.aggregate(self, func, seed, select)

    # endregion

    # region sorting
    def _order_by(self, key_selector: Selector[T, SupportsRichComparison], descending: bool) -> QOrderedIterable[T]:
        return C.ordered_iterable(lambda: self, [SortInstruction(key_selector, descending)])

    def order_by(self, key_selector: Selector[T, SupportsRichComparison]) -> QOrderedIterable[T]:
        return self._order_by(key_selector, False)
    def order_by_descending(self, key_selector: Selector[T, SupportsRichComparison]) -> QOrderedIterable[T]:
        return self._order_by(key_selector, True)

    def reversed(self) -> QIterable[T]: return self._lazy(lambda: ops.reversed(self))

    # endregion

    # region mapping/transformation methods
    def select[TReturn](self, selector: Selector[T, TReturn]) -> QIterable[TReturn]: return C.lazy_iterable(lambda: ops.select(self, selector))
    def select_index[TReturn](self, selector: Callable[[T, int], TReturn]) -> QIterable[TReturn]: return C.lazy_iterable(lambda: ops.select_index(self, selector))
    def select_many[TInner](self, selector: Selector[T, Iterable[TInner]]) -> QIterable[TInner]: return C.lazy_iterable(lambda: ops.select_many(self, selector))
    def join[TInner, TKey, TResult](self, other: Iterable[TInner], self_key: Selector[T, TKey], other_key: Selector[TInner, TKey], select: Callable[[T, TInner], TResult]) -> QIterable[TResult]: return C.lazy_iterable(lambda: ops.join(self, other, self_key, other_key, select))
    def group_join[TInner, TKey, TResult](self, other: Iterable[TInner], self_key: Selector[T, TKey], group_key: Selector[TInner, TKey], select: Callable[[T, QList[TInner]], TResult]) -> QIterable[TResult]: return C.lazy_iterable(lambda: ops.group_join(self, other, self_key, group_key, select))

    def qindex(self) -> QIterable[tuple[int, T]]: return C.lazy_iterable(lambda: ops.qindex(self))

    def zip[T2, TResult](self, second: Iterable[T2], select: Callable[[T, T2], TResult]) -> QIterable[TResult]: return C.lazy_iterable(lambda: ops.zip(self, second, select))
    def zip2[T2, T3, TResult](self, second: Iterable[T2], third: Iterable[T3], select: Callable[[T, T2, T3], TResult]) -> QIterable[TResult]: return C.lazy_iterable(lambda: ops.zip2(self, second, third, select))
    def zip3[T2, T3, T4, TResult](self, second: Iterable[T2], third: Iterable[T3], fourth: Iterable[T4], select: Callable[[T, T2, T3, T4], TResult]) -> QIterable[TResult]: return C.lazy_iterable(lambda: ops.zip3(self, second, third, fourth, select))

    def zip_tuple[T2](self, second: Iterable[T2]) -> QIterable[tuple[T, T2]]: return C.lazy_iterable(lambda: ops.zip_tuple(self, second))
    def zip_tuple2[T2, T3](self, second: Iterable[T2], third: Iterable[T3]) -> QIterable[tuple[T, T2, T3]]: return C.lazy_iterable(lambda: ops.zip_tuple2(self, second, third))
    def zip_tuple3[T2, T3, T4](self, second: Iterable[T2], third: Iterable[T3], fourth: Iterable[T4]) -> QIterable[tuple[T, T2, T3, T4]]: return C.lazy_iterable(lambda: ops.zip_tuple3(self, second, third, fourth))

    def to_dict[TKey, TValue](self, key_selector: Selector[T, TKey], value_selector: Selector[T, TValue]) -> QDict[TKey, TValue]: return ops.to_dict(self, key_selector, value_selector)

    def chunk(self, size: int) -> QIterable[QList[T]]: return C.lazy_iterable(lambda: ops.chunk(self, size))

    @overload
    def group_by[TKey](self, key: Selector[T, TKey]) -> QIterable[QGrouping[TKey, T]]:
        """Groups the elements of a sequence according to the specified key selector"""

    @overload
    def group_by[TKey, TElement](self, key: Selector[T, TKey], select: Selector[T, TElement]) -> QIterable[QGrouping[TKey, TElement]]:
        """Groups the elements of a sequence according to the specified key selector and element selector"""

    def group_by[TKey, TElement](self, key: Selector[T, TKey], select: Selector[T, TElement] | None = None) -> QIterable[QGrouping[TKey, T]] | QIterable[QGrouping[TKey, TElement]]: return ops.group_by_q(self, key, select)
    # endregion

    # region single item selecting methods
    def first(self, predicate: Predicate[T] | None = None) -> T: return ops.first(self, predicate)
    def first_or_none(self, predicate: Predicate[T] | None = None) -> T | None: return ops.first_or_none(self, predicate)
    def single(self, predicate: Predicate[T] | None = None) -> T: return ops.single(self, predicate)
    def single_or_none(self, predicate: Predicate[T] | None = None) -> T | None: return ops.single_or_none(self, predicate)
    def last(self, predicate: Predicate[T] | None = None) -> T: return ops.last(self, predicate)
    def last_or_none(self, predicate: Predicate[T] | None = None) -> T | None: return ops.last_or_none(self, predicate)

    def element_at(self, index: int) -> T: return ops.element_at(self, index)
    def element_at_or_none(self, index: int) -> T | None: return ops.element_at_or_none(self, index)

    def min_by[TKey: SupportsRichComparison](self, key_selector: Selector[T, TKey]) -> T: return ops.min_by(self, key_selector)
    def max_by[TKey: SupportsRichComparison](self, key_selector: Selector[T, TKey]) -> T: return ops.max_by(self, key_selector)

    # endregion

    # region methods subclasses may want to override for perfarmonce reasons

    def _optimized_length(self) -> int: return sum(1 for _ in self)
    def _assert_not_empty(self) -> Self:
        if not self.any(): raise EmptyIterableError()
        return self

    # region factory methods
    # note: we do not "optimize" by returning self in any subclass because the contract is to create a new independent copy
    def to_list(self) -> QList[T]: return C.list(self)
    def to_set(self) -> QSet[T]: return C.set(self)
    def to_frozenset(self) -> QFrozenSet[T]: return C.frozen_set(self)
    def to_sequence(self) -> QSequence[T]: return C.sequence(self)
    def to_built_in_list(self) -> list[T]: return list(self)

    # endregion
