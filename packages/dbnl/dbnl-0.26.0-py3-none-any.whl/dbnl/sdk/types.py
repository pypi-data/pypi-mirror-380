from dataclasses import dataclass
from typing import Literal, TypedDict, Union

import pyarrow as pa
from dataclasses_json import dataclass_json

PrimitiveTypeLiteral = Literal[
    "boolean",
    "int",
    "long",
    "float",
    "double",
    "string",
    "category",
    "timestamp",
    "timestamptz",
]
ContainerTypeLiteral = Literal["list", "map", "struct"]


class ListTypeDict(TypedDict):
    type: Literal["list"]
    value_type: "DataTypeDict"


class MapTypeDict(TypedDict):
    type: Literal["map"]
    key_type: "DataTypeDict"
    value_type: "DataTypeDict"


class FieldDict(TypedDict):
    name: str
    type: "DataTypeDict"


class StructTypeDict(TypedDict):
    type: Literal["struct"]
    fields: list[FieldDict]


DataTypeDict = Union[PrimitiveTypeLiteral, ListTypeDict, MapTypeDict, StructTypeDict]


@dataclass_json
@dataclass(repr=False)
class ListType:
    value_type: "DataType"
    type: str = "list"

    def __str__(self) -> str:
        return f"list<{self.value_type}>"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(type={self.type!r}, value_type={self.value_type!r})"


@dataclass_json
@dataclass(repr=False)
class MapType:
    key_type: "DataType"
    value_type: "DataType"
    type: str = "map"

    def __str__(self) -> str:
        return f"map<{self.key_type}, {self.value_type}>"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(type={self.type!r}, key_type={self.key_type!r}, value_type={self.value_type!r})"
        )


@dataclass_json
@dataclass(repr=False)
class Field:
    name: str
    type: "DataType"

    def __str__(self) -> str:
        return f"{self.name}: {self.type}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, type={self.type!r})"


@dataclass_json
@dataclass(repr=False)
class StructType:
    fields: list[Field]
    type: str = "struct"

    def __str__(self) -> str:
        return f"struct<{', '.join([str(f) for f in self.fields])}>"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(type={self.type!r}, fields=[{', '.join([repr(f) for f in self.fields])}])"


DataType = Union[PrimitiveTypeLiteral, ListType, MapType, StructType]


def datatype_dict_from_arrow(dtype: pa.DataType) -> DataTypeDict:
    if pa.types.is_int64(dtype):
        return "long"
    elif pa.types.is_integer(dtype):
        return "int"
    elif pa.types.is_float64(dtype):
        return "double"
    elif pa.types.is_floating(dtype):
        return "float"
    elif pa.types.is_boolean(dtype):
        return "boolean"
    elif pa.types.is_string(dtype):
        return "string"
    elif pa.types.is_dictionary(dtype):
        assert isinstance(dtype, pa.DictionaryType)
        if pa.types.is_integer(dtype.index_type) and pa.types.is_string(dtype.value_type):
            return "category"
        # fallback to just treat as underlying type
        return datatype_dict_from_arrow(dtype.value_type)
    elif pa.types.is_timestamp(dtype):
        assert isinstance(dtype, pa.TimestampType)
        if dtype.tz is not None:
            return "timestamptz"
        return "timestamp"
    elif pa.types.is_list(dtype):
        assert isinstance(dtype, pa.ListType)
        value_type = dtype.value_type
        return {
            "type": "list",
            "value_type": datatype_dict_from_arrow(value_type),
        }
    elif pa.types.is_map(dtype):
        assert isinstance(dtype, pa.MapType)
        key_type = dtype.key_type
        value_type = dtype.item_type
        return {
            "type": "map",
            "key_type": datatype_dict_from_arrow(key_type),
            "value_type": datatype_dict_from_arrow(value_type),
        }
    elif pa.types.is_struct(dtype):
        assert isinstance(dtype, pa.StructType)
        return {
            "type": "struct",
            "fields": [
                {
                    "name": dtype.field(i).name,
                    "type": datatype_dict_from_arrow(dtype.field(i).type),
                }
                for i in range(dtype.num_fields)
            ],
        }
    else:
        raise ValueError(f"Unsupported data type: {dtype}")


def datatype_from_datatype_dict(d: DataTypeDict) -> DataType:
    if isinstance(d, str):
        return d
    elif d["type"] == "list":
        return ListType(value_type=datatype_from_datatype_dict(d["value_type"]))
    elif d["type"] == "map":
        return MapType(
            key_type=datatype_from_datatype_dict(d["key_type"]), value_type=datatype_from_datatype_dict(d["value_type"])
        )
    elif d["type"] == "struct":
        return StructType(
            fields=[Field(name=f["name"], type=datatype_from_datatype_dict(f["type"])) for f in d["fields"]]
        )
    else:
        raise ValueError(f"Unsupported data type: {d}")


def is_compatible(pa_dtype: pa.DataType, dtype: DataType) -> bool:
    """Checks if an arrow datatype is compatible with a dbnl datatype.
    :param pa_dtype: arrow datatype
    :param dtype: dbnl datatype
    :return: True if compatible, False otherwise.
    """
    if dtype == "boolean":
        return pa.types.is_boolean(pa_dtype)
    elif dtype == "int":
        return pa.types.is_integer(pa_dtype)
    elif dtype == "long":
        return pa.types.is_integer(pa_dtype)
    elif dtype == "float":
        return pa.types.is_floating(pa_dtype)
    elif dtype == "double":
        return pa.types.is_floating(pa_dtype)
    elif dtype == "string":
        return pa.types.is_string(pa_dtype)
    elif dtype == "timestamp":
        return pa.types.is_timestamp(pa_dtype)
    elif dtype == "timestamptz":
        if not pa.types.is_timestamp(pa_dtype):
            return False
        assert isinstance(pa_dtype, pa.TimestampType)
        return pa_dtype.tz is not None
    elif dtype == "category":
        if not pa.types.is_dictionary(pa_dtype):
            return False
        assert isinstance(pa_dtype, pa.DictionaryType)
        return pa.types.is_string(pa_dtype.value_type)
    elif dtype.type == "list":
        if not pa.types.is_list(pa_dtype):
            return False
        assert isinstance(dtype, ListType)
        assert isinstance(pa_dtype, pa.ListType)
        return is_compatible(pa_dtype.value_type, dtype.value_type)
    elif dtype.type == "map":
        if not pa.types.is_map(pa_dtype):
            return False
        assert isinstance(dtype, MapType)
        assert isinstance(pa_dtype, pa.MapType)
        return is_compatible(pa_dtype.key_type, dtype.key_type) and is_compatible(pa_dtype.item_type, dtype.value_type)
    elif dtype.type == "struct":
        if not pa.types.is_struct(pa_dtype):
            return False
        assert isinstance(dtype, StructType)
        if len(dtype.fields) != pa_dtype.num_fields:
            return False
        for i in range(pa_dtype.num_fields):
            field = next((f for f in dtype.fields if f.name == pa_dtype.field(i).name), None)
            if field is None or not is_compatible(pa_dtype.field(i).type, field.type):
                return False
        return True
    else:
        return False
