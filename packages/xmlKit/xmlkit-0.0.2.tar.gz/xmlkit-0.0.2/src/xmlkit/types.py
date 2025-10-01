"""Type aliases for xmlkit module."""

from typing import Any, Protocol, TYPE_CHECKING
from collections.abc import Callable, Container, Generator, Mapping

# Handle _typeshed imports conditionally for type checking only
if TYPE_CHECKING:
    from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
else:
    # Fallback types for runtime
    type ReadableBuffer = bytes | bytearray | memoryview

    # From typeshed
    class SupportsRead[T](Protocol[T]):
        def read(self, length: int = ..., /) -> T: ...
    class SupportsWrite[T](Protocol[T]):
        def write(self, s: T, /) -> object: ...

# Type aliases for commonly used complex types
# dict as attribute value is exclusive to xmlns
type AttrValue = str | dict[str, AttrValue] | list[AttrValue] | None
type AttrDict = dict[str, AttrValue]
type PathType = list[tuple[str, AttrDict | None]]
type ItemType = str | AttrDict | None

# Type aliases for callback functions
type ItemCallback = Callable[[PathType, ItemType], bool]
type Postprocessor = Callable[[PathType, str, AttrValue], tuple[str, AttrValue]]
type Preprocessor = Callable[[str, Any], tuple[str, Any]]
type ForceOption = bool | Container[str] | Callable[[PathType, str, str], bool] | None

# Type aliases for XML input and ouput
type XmlInput = str | ReadableBuffer | SupportsRead[bytes] | Generator[ReadableBuffer]
type XmlOutput = SupportsWrite[bytes] | SupportsWrite[str]

# Other type aliases
type Indent = str | int
type Namespaces = dict[str, str] | None
type MappingNamespaces = Mapping[str, str] | None
type DictConstructor = type
type OptionalAttrDict = AttrDict | None
type OptionalAttrValue = AttrValue | None
type OptionalStr = str | None
type OptionalMappingNamespaces = Mapping[str, str] | None
type OptionalAny = Any | None
type Expat = Any