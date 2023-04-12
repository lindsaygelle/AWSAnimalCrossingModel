"""net module that defines a Link class representing a hyperlink to
a document with a specified HTTP method."""
from typing import Literal, TypedDict

# Method: This is a type alias that defines the possible HTTP methods that can
# be used with a link. It is a Literal type, which means that the value of the
# attribute must be one of the specified strings. In this case, it can be
# either "HEAD", "DELETE", "GET", "OPTIONS", "PATCH", or "POST".
Method = Literal["HEAD", "DELETE", "GET", "OPTIONS", "PATCH", "POST"]


class Link(TypedDict):
    """Link: This class represents a hyperlink to a document with a specified
    HTTP method. It is a subclass of TypedDict, a built-in Python class for
    defining dictionaries with specific keys and value types."""

    # document: This attribute is a string representing the
    # document that the link points to.
    document: str
    # href: This attribute is a string representing the URL of the link.
    href: str
    # method: This attribute is a Method type alias that represents the HTTP
    # method that should be used to access the document. It can be one of
    # the following strings:
    # "HEAD", "DELETE", "GET", "OPTIONS", "PATCH", or "POST".
    method: Method
