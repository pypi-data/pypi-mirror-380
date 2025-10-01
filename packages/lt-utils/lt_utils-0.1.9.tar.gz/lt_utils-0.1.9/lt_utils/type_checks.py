__all__ = [
    "is_pathlike",
    "is_path_valid",
    "is_file",
    "is_dir",
    "is_valid",
    "is_num",
    "is_array",
    "is_list",
    "is_dict",
    "is_tuple",
    "is_int",
    "is_float",
    "is_bool",
    "is_str",
    "is_array_of",
    "is_dict_of",
    "is_nand",
    "is_nor",
    "is_xor",
    "is_xnor",
    "is_converse",
    "is_imply",
    "is_nimply",
    "is_file_format",
    "ArrayType",
    "is_union",
]

from typing import TypeGuard, TypeVar, get_origin
from lt_utils.common import (
    TypeAlias,
    Union,
    Any,
    List,
    Path,
    PathLike,
    Number,
    Type,
    Optional,
    Dict,
    Tuple,
    Sequence,
)

ArrayType: TypeAlias = Union[list, tuple, set]
UnionType: TypeAlias = Union[object, Any]

K = TypeVar("K")
T = TypeVar("T")


def is_union(entry: Any) -> TypeGuard[UnionType]:
    return get_origin(entry) is Union


def is_pathlike(
    entry: Any, check_if_empty: bool = False, validate: bool = False
) -> TypeGuard[Union[PathLike, Path, str, bytes]]:
    begin = isinstance(entry, (str, bytes)) or hasattr(entry, "__fspath__")
    assert (
        not validate or begin
    ), f'"{entry}" is not a valid path-like. It is a {type(entry)} type.'
    if not begin:
        return begin
    results = not check_if_empty or str(entry).strip()
    assert not validate or results, "The object is a invalid"
    return results


def is_file_format(entry: str, extensions: List[str], validate: bool = False) -> bool:
    begin = is_array(extensions)
    if begin:
        extensions = [x for x in extensions if is_str(x)]
        begin = bool(extensions)
    assert not validate or begin, "No valid extension has been provided."
    if not begin:
        return False
    f_name = Path(entry).name
    if not isinstance(extensions, tuple):
        extensions = tuple(extensions)
    results = f_name.endswith(tuple(extensions))
    assert not validate or results, (
        f"Unsupported file format for the file '{f_name}'. Use: "
        + ", ".join(extensions)
        + "."
    )
    return results


def is_path_valid(entry: PathLike, validate: bool = False) -> bool:
    if not is_pathlike(entry, validate):
        return False
    try:
        if isinstance(entry, bytes):
            entry = entry.decode(errors="ignore")
        entry = Path(str(entry))
        results = entry.exists()
    except RecursionError as e:
        print(f"RecursionError: {e} | entry: {entry}")
        results = False
    assert not validate or results, f'The path "{entry}" is not a valid path!'
    return results


def is_file(
    entry: PathLike, validate: bool = False, extensions: Optional[List[str]] = None
) -> bool:
    if not is_path_valid(entry, validate):
        return False
    try:
        if isinstance(entry, bytes):
            entry = Path(entry.decode(errors="ignore"))
        else:
            entry = Path(str(entry))
        results = entry.is_file()
    except RecursionError as e:
        print(f"RecursionError: {e}")
        results = False

    assert (
        not validate or results
    ), f"Path '{entry}' does exist but does not points into a valid file."
    if results and is_array(extensions):
        results = is_file_format(entry, extensions=extensions, validate=validate)
    return results


def is_dir(entry: PathLike, validate: bool = False) -> bool:
    if not is_path_valid(entry, validate):
        return False
    results = Path(entry).is_dir()
    assert (
        not validate or results
    ), f'The path "{entry}" does exist but does not points into a valid directory.'
    return results


def is_valid(
    entry: T,
    validate: bool = False,
) -> TypeGuard[T]:
    results = entry is not None
    assert not validate or results
    return results


def is_num(
    entry: Any,
    validate: bool = False,
) -> TypeGuard[Number]:
    results = isinstance(entry, Number)
    assert (
        results or not validate
    ), f"'{entry}' is not a valid number! It is type: {type(entry)}"
    return results


def is_array(
    entry: Any,
    check_if_empty: bool = True,
    validate: bool = False,
) -> TypeGuard[ArrayType]:
    """The type `Array` itself does not exist in python, so, here
    we do check if the value is either a `List` or a `Tuple`, with
    both can be considered one.

    Note that Lists are mutable while Tuples aren't.
    If its needed certainty, then use `is_list` or `is_tuple` instead.
    """
    result = isinstance(entry, (list, set, tuple)) and (
        not check_if_empty or bool(entry)
    )
    assert (
        not validate or result
    ), f"'{entry}' is not a valid `list`, `set` or `tuple`.'"
    return result


def is_list(
    entry: Any,
    check_if_empty: bool = True,
    validate: bool = False,
) -> TypeGuard[list]:
    result = isinstance(entry, list) and (not check_if_empty or bool(entry))
    assert not validate or result
    return result


def is_dict(
    entry: Any,
    check_if_empty: bool = True,
    validate: bool = False,
) -> TypeGuard[dict]:
    result = isinstance(entry, dict) and (not check_if_empty or bool(entry))
    assert not validate or result, f"`entry` is not a valid dictionary: `{entry}`"
    return result


def is_tuple(
    entry: Any,
    check_if_empty: bool = True,
    validate: bool = False,
) -> TypeGuard[tuple]:
    result = isinstance(entry, tuple) and (not check_if_empty or bool(entry))
    assert not validate or result
    return result


def is_int(entry: Any, validate: bool = False) -> TypeGuard[int]:
    result = isinstance(entry, int) and not isinstance(
        entry, bool
    )  # Prevents `True` being treated as `1`
    assert not validate or result
    return result


def is_float(entry: Any, validate: bool = False) -> TypeGuard[float]:
    result = isinstance(entry, float)
    assert not validate or result
    return result


def is_bool(entry: Any, validate: bool = False) -> TypeGuard[bool]:
    result = isinstance(entry, bool)
    assert not validate or result
    return result


def is_str(
    entry: Any,
    strip_str: bool = True,
    check_if_empty: bool = True,
    validate: bool = False,
) -> TypeGuard[Union[str, bytes]]:
    """Check if an entry is a string or bytes."""
    first_check = isinstance(entry, (str, bytes))
    if not first_check:
        assert (
            not validate
        ), f'"{entry}" is not a valid string, it is a type: {type(entry)}'
        return False
    results = not check_if_empty or bool(entry.strip() if strip_str else entry)
    assert not validate or results, "The provided string was a empty string!"
    return results


def is_array_of(
    entry: Any,
    item_types: Union[Type[T], Tuple[Type[T], ...]],
    validate: bool = False,
) -> TypeGuard[Sequence[T]]:
    """
    Check if entry is a sequence and all elements are of the given item_type.

    Args:
        entry: The object to check.
        item_type: The expected type of each element.
        validate: If True, raises AssertionError when check fails.

    Returns:
        True if valid, False otherwise.
    """
    is_array(entry, False, True)
    results = all([isinstance(i, item_types) for i in entry])
    assert not validate or results
    return results


def is_dict_of(
    entry: Any,
    values_types: Union[Type[T], Tuple[Type[T], ...]],
    validate: bool = False,
) -> TypeGuard[Dict[Union[Any, str], T]]:
    """Return True if d is a dict and all values match the given types."""
    is_dict(entry, False, True)
    results = all([isinstance(v, values_types) for v in entry.values()])
    assert (
        not validate or results
    ), f"Not all keys matches the type(s) '{values_types}' "
    return results


def is_nand(a: bool, b: bool):
    """[a -> b = result]
    ```
    False -> False = True
    False -> True = True
    True -> False = True
    True -> True = False
    ```
    """
    return not (a and b)


def is_nor(a: bool, b: bool):
    """[a -> b = result]
    ```
    False -> False = True
    False -> True = False
    True -> False = False
    True -> True = False
    ```
    """
    return not a and not b


def is_xor(a: bool, b: bool):
    """[a -> b = result]
    ```
    False -> False = False
    False -> True = True
    True -> False = True
    True -> True = False
    ```
    """
    return (a and not b) or (b and not a)


def is_xnor(a: bool, b: bool):
    """[a -> b = result]
    ```
    False -> False = True
    False -> True = False
    True -> False = False
    True -> True = True
    ```
    """
    return not is_xor(a, b)


def is_imply(a: bool, b: bool):
    """[a -> b = result]
    ```
    False -> False = True
    False -> True = True
    True -> False = False
    True -> True = True
    ```
    """
    return is_xnor(a, b) or (not a and b)


def is_nimply(a: bool, b: bool):
    """[a -> b = result]
    ```
    False -> False = False
    False -> True = False
    True -> False = True
    True -> True = False
    ```
    """
    return not is_imply(a, b)


def is_converse(a: bool, b: bool):
    """[a -> b = result]
    ```
    False -> False = True
    False -> True = False
    True -> False = True
    True -> True = True
    ```
    """
    return is_xnor(a, b) or (a and not b)
