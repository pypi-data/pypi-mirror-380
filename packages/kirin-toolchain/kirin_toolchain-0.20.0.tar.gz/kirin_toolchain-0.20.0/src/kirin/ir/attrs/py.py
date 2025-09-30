from typing import TYPE_CHECKING, Any, Type, TypeVar
from dataclasses import dataclass

from typing_extensions import Protocol, runtime_checkable

from kirin.print import Printer
from kirin.ir.attrs.abc import Attribute
from kirin.serialization.base.serializationunit import SerializationUnit

if TYPE_CHECKING:
    from kirin.serialization.base.serializer import Serializer
    from kirin.serialization.base.deserializer import Deserializer

from .data import Data
from .types import PyClass, TypeAttribute

T = TypeVar("T")


@dataclass
class PyAttr(Data[T]):
    """Python attribute for compile-time values.
    This is a generic attribute that holds a Python value.

    The constructor takes a Python value and an optional type attribute.
    If the type attribute is not provided, the type of the value is inferred
    as `PyClass(type(value))`.

    !!! note "Pretty Printing"
        This object is pretty printable via
        [`.print()`][kirin.print.printable.Printable.print] method.
    """

    name = "PyAttr"
    data: T

    def __init__(self, data: T, pytype: TypeAttribute | None = None):
        self.data = data

        if pytype is None:
            self.type = PyClass(type(data))
        else:
            self.type = pytype

    def __hash__(self) -> int:
        return hash((self.type, self.data))

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, PyAttr):
            return False

        return self.type == value.type and self.data == value.data

    def print_impl(self, printer: Printer) -> None:
        printer.plain_print(repr(self.data))
        with printer.rich(style="comment"):
            printer.plain_print(" : ")
            printer.print(self.type)

    def unwrap(self) -> T:
        return self.data

    def is_structurally_equal(
        self, other: Attribute, context: dict | None = None
    ) -> bool:
        if not isinstance(other, PyAttr):
            return False
        if self.type != other.type:
            return False
        if isinstance(self.data, StructurallyEqual) and isinstance(
            other.data, StructurallyEqual
        ):
            return self.data.is_structurally_equal(other.data, context=context)
        return self.data == other.data

    def serialize(self, serializer: "Serializer") -> "SerializationUnit":
        return serializer.serialize_pyattr(self)

    @classmethod
    def deserialize(
        cls: Type["PyAttr"], serUnit: "SerializationUnit", deserializer: "Deserializer"
    ) -> "PyAttr":
        return deserializer.deserialize_pyattr(serUnit)


@runtime_checkable
class StructurallyEqual(Protocol):
    def is_structurally_equal(
        self, other: Any, context: dict | None = None
    ) -> bool: ...
