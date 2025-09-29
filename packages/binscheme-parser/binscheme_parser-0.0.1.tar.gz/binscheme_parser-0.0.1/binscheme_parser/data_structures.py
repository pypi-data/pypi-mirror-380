
from dataclasses import dataclass, field
from typing import Dict, List, Any, Tuple, Optional

@dataclass
class Type:
    pass

@dataclass
class IntegerType(Type):
    bits: int
    signed: bool
    endian: str

@dataclass
class FloatType(Type):
    bits: int

@dataclass
class BitType(Type):
    bits: int

@dataclass
class SchemeType(Type):
    name: str

@dataclass
class FieldReference:
    path: str

@dataclass
class EnumMemberReference:
    path: str

@dataclass
class ArrayType(Type):
    element_type: Type
    size: Any # int or FieldReference

@dataclass
class StringType(Type):
    encoding: str
    size: Any # int or FieldReference

@dataclass
class Field:
    name: str
    type: Type
    default: Any = None

@dataclass
class ConditionalBlock:
    condition: Optional[Tuple[Any, str, Any]]
    fields: Dict[str, Field] = field(default_factory=dict)

@dataclass
class Scheme:
    name: str
    fields: Dict[str, Field] = field(default_factory=dict)
    conditional_blocks: List[ConditionalBlock] = field(default_factory=list)

@dataclass
class Enum:
    name: str
    base_type: IntegerType
    values: Dict[str, int] = field(default_factory=dict)

@dataclass
class Instance:
    name: str
    scheme_name: str
    values: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SchemaCollection:
    schemes: Dict[str, Scheme] = field(default_factory=dict)
    enums: Dict[str, Enum] = field(default_factory=dict)
    instances: Dict[str, Instance] = field(default_factory=dict)
