from __future__ import annotations

from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TYPE_CHECKING, cast

from typed_linq_collections._private_implementation_details.q_zero_overhead_collection_contructors import ZeroImportOverheadConstructors as C
from typed_linq_collections.q_iterable import QIterable

if TYPE_CHECKING:
    from typed_linq_collections.collections.numeric.q_decimal_types import QDecimalIterable
    from typed_linq_collections.collections.numeric.q_float_types import QFloatIterable
    from typed_linq_collections.collections.numeric.q_fraction_types import QFractionIterable
    from typed_linq_collections.collections.numeric.q_int_types import QIntIterable

class CheckedCast[TValue]:
    __slots__: tuple[str, ...] = ("_type",)
    def __init__(self, type: type[TValue]) -> None:
        self._type: type[TValue] = type

    def __call__(self, value: object) -> TValue:
        if not isinstance(value, self._type): raise TypeError(f"Expected {self._type.__name__}, got {type(value).__name__}")
        return value

_checked_cast_int = CheckedCast(int)
_checked_cast_float = CheckedCast(float)
_checked_cast_fraction = CheckedCast(Fraction)
_checked_cast_decimal = CheckedCast(Decimal)

class QCast[TItem]:
    __slots__: tuple[str, ...] = ("_iterable",)
    def __init__(self, iterable: QIterable[TItem]) -> None:
        self._iterable: QIterable[TItem] = iterable

    @property
    def checked(self) -> QCheckedCast[TItem]:
        return QCheckedCast(self._iterable)

    def int(self) -> QIntIterable:
        return C.int_iterable(lambda: (cast(Iterable[int], self._iterable)))

    def float(self) -> QFloatIterable:
        return C.float_iterable(lambda: (cast(Iterable[float], self._iterable)))

    def fraction(self) -> QFractionIterable:
        return C.fraction_iterable(lambda: (cast(Iterable[Fraction], self._iterable)))

    def decimal(self) -> QDecimalIterable:
        return C.decimal_iterable(lambda: cast(Iterable[Decimal], self._iterable))

    def to[TNew](self, _type: type[TNew]) -> QIterable[TNew]:  # pyright: ignore
        return cast(QIterable[TNew], self._iterable)

class QCheckedCast[TItem]:
    __slots__: tuple[str, ...] = ("_iterable",)
    def __init__(self, iterable: QIterable[TItem]) -> None:
        self._iterable: QIterable[TItem] = iterable

    def int(self) -> QIntIterable:
        return C.int_iterable(lambda: self._iterable.select(_checked_cast_int))

    def float(self) -> QFloatIterable:
        return C.float_iterable(lambda: self._iterable.select(_checked_cast_float))

    def fraction(self) -> QFractionIterable:
        return C.fraction_iterable(lambda: self._iterable.select(_checked_cast_fraction))

    def decimal(self) -> QDecimalIterable:
        return C.decimal_iterable(lambda: self._iterable.select(_checked_cast_decimal))

    def to[TNew](self, _type: type[TNew]) -> QIterable[TNew]:  # pyright: ignore
        return self._iterable.select(CheckedCast(_type))
