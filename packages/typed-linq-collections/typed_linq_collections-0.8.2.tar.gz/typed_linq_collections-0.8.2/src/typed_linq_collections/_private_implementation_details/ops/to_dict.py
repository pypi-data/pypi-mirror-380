from __future__ import annotations

from typing import TYPE_CHECKING

# noinspection PyPep8Naming
from typed_linq_collections._private_implementation_details.q_zero_overhead_collection_contructors import ZeroImportOverheadConstructors as C

if TYPE_CHECKING:
    from typed_linq_collections._private_implementation_details.type_aliases import Selector
    from typed_linq_collections.collections.q_dict import QDict
    from typed_linq_collections.q_iterable import QIterable


def to_dict[T, TKey, TValue](self: QIterable[T], key_selector: Selector[T, TKey], value_selector: Selector[T, TValue]) -> QDict[TKey, TValue]:
    return C.dict((key_selector(item), value_selector(item)) for item in self)
