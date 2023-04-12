"""database module that defines a Record class 
representing a record in a database."""
from datetime import datetime
from typing import TypedDict, Union

# Id: This is a type alias that defines the possible types for the id
# attribute. It is a Union type, which means that the attribute can be
# one of the specified types. In this case, it can be either an int or a str.
Id = Union[int, str]


class Record(TypedDict):
    """Record: This class represents a record in a database. It is a subclass
    of TypedDict, a built-in Python class for defining dictionaries with
    specific keys and value types."""

    # id: This attribute is an Id type alias representing the unique
    # identifier of the record. It can be either an integer or a string.
    id: Id
    # created_at: This attribute is a datetime object representing the
    # date and time the record was created.
    created_at: datetime
    # updated_at: This attribute is a datetime object representing the
    # date and time the record was last updated.
    updated_at: datetime
