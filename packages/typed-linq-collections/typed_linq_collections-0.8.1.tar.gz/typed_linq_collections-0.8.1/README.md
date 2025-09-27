# Typed Linq Collections

Linq for Python with full type annotions. 
Query any built in Iterable or use one of the queryable collections that are drop in replacements for standard collections.
Name collisions with the standard library are resolved by prefixing the built in with q. qcount etc.

- **Rich Query API**: Almost the full Enumerable set of operators from .net gives excellent support for filtering, mapping, grouping, and more in a fluent API
- **Comprehensive type annotions**: Gives you full autocomplete and static error analysis if using pyright with vscode or PyCharm. In vscode refactoring within the lambdas work like a charm
- **Lazy Evaluation**: Memory efficient query execution with deferred evaluation for every operation other than the to_* methods which create new collections 
- **Drop-in compatible collection types**: Collection types that seamlessly replace and interoperate with standard Python collections
- **Numeric Specializations**: Dedicated types for `int`, `float`, `Decimal`, and `Fraction` collections
- **Extensible Design**: QIterable is an abstract class/mixin that can be subclassed by any Iterable type to add full querying capabilities

## Quick Start

```python
from typed_linq_collections.collections.q_list import QList
from typed_linq_collections.q_iterable import query


fruits = ("apple", "apricot", "mango", "melon", "peach", "pineapple")
def test_querying_built_in_collections() -> None:
    fruits_by_first_character = (query(fruits)
                                 .group_by(lambda fruit: fruit[0])
                                 .where(lambda group: group.key in {"a", "p"})
                                 .to_list())

    assert fruits_by_first_character == [['apple', 'apricot'], ['peach', 'pineapple']]

def test_querying_with_queryable_collections() -> None:
    fruits_by_first_character = (QList(fruits)
                                 .group_by(lambda fruit: fruit[0])
                                 .where(lambda group: group.key in {"a", "p"})
                                 .to_list())

    assert fruits_by_first_character == [['apple', 'apricot'], ['peach', 'pineapple']]

def test_numeric_operations() -> None:
    total_lenght_of_fruits = (query(fruits)
                              .select(len)
                              .as_ints() # get's you a QIntIterable with numeric operations support. typed so that it is only available on a QIterable[int]
                              .sum())

    assert total_lenght_of_fruits == 36
```

## Collection Types

### Core Collections
Drop in replacements for the built in collections.
- **`QList[T]`** - Queryable list (mutable sequence)
- **`QSequence[T]`** - Queryable immutable sequence
- **`QSet[T]`** - Queryable set (mutable)
- **`QFrozenSet[T]`** - Queryable frozen set (immutable)
- **`QDict[K, V]`** - Queryable dictionary
- **`QDefaultDict[K, V]`** - Queryable default dictionary

### Numeric Collections
Specialized collections with additional numeric operations:

- **`QIntIterable`** - For integer collections
- **`QFloatIterable`** - For float collections
- **`QDecimalIterable`** - For Decimal collections
- **`QFractionIterable`** - For Fraction collections
- 
and so on with equivalents for QList, QSet, QDict, QFrozenSet, QDefaultDict.
