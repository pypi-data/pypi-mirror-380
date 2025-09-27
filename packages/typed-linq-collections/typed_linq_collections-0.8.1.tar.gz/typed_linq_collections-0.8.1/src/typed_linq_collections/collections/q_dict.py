from __future__ import annotations

from typing import TYPE_CHECKING, override

# noinspection PyPep8Naming
from typed_linq_collections._private_implementation_details.q_zero_overhead_collection_contructors import ZeroImportOverheadConstructors as C
from typed_linq_collections.collections.q_key_value_pair import KeyValuePair
from typed_linq_collections.q_iterable import QIterable

if TYPE_CHECKING:
    from collections.abc import Iterable

class QDict[TKey, TItem](dict[TKey, TItem], QIterable[TKey]):
    __slots__: tuple[str, ...] = ()
    def __init__(self, elements: Iterable[tuple[TKey, TItem]] = ()) -> None:
        super().__init__(elements)

    def qitems(self) -> QIterable[KeyValuePair[TKey, TItem]]: return C.lazy_iterable(lambda: self.items()).select(KeyValuePair)

    @override
    def _optimized_length(self) -> int: return len(self)
