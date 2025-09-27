from __future__ import annotations

import sys
from typing import TYPE_CHECKING, SupportsIndex, overload, override

from typed_linq_collections._private_implementation_details.q_lazy_iterable import QLazyIterableImplementation
from typed_linq_collections.collections.q_sequence import QSequence
from typed_linq_collections.q_iterable import QIterable

if TYPE_CHECKING:
    from collections.abc import Iterable

class QList[TItem](list[TItem], QSequence[TItem], QIterable[TItem]):
    __slots__: tuple[str, ...] = ()
    def __init__(self, iterable: Iterable[TItem] = ()) -> None:
        super().__init__(iterable)

    @override
    def _optimized_length(self) -> int: return len(self)

    @override
    def reversed(self) -> QIterable[TItem]: return QLazyIterableImplementation[TItem](lambda: reversed(self))

    @override
    def element_at(self, index: int) -> TItem: return self[index]

    @override
    def index(self, value: TItem, start: SupportsIndex = 0, stop: SupportsIndex = sys.maxsize) -> int:
        return super().index(value, start, stop)

    @override
    def count(self, value: TItem): return super().count(value)

    @overload
    def __getitem__(self, index: SupportsIndex) -> TItem: ...

    @overload
    def __getitem__(self, index: slice) -> QList[TItem]: ...

    @override
    def __getitem__(self, index: SupportsIndex | slice) -> TItem | QList[TItem]:
        if isinstance(index, slice):
            return QList(super().__getitem__(index))
        return super().__getitem__(index)
