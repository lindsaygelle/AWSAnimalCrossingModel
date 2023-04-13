"""`net` module that defines a Link class representing a hyperlink to
a document with a specified HTTP method. It also defines a `Response`
that can be used in HTTP response."""
from typing import Any, AnyStr, Dict, List, TypedDict, Union
from uuid import UUID

from .http.method import Method

Content = Union[Dict[AnyStr, Any], TypedDict]
Id = Union[str, UUID]


class Link(TypedDict):
    """`Link`: This class represents a hyperlink to a document with a specified
    HTTP method. It is a subclass of `TypedDict`, a built-in Python class for
    defining dictionaries with specific keys and value types."""

    # document: This attribute is a string representing the
    # document that the link points to.
    document: str
    # href: This attribute is a string representing the URL of the link.
    href: str
    # method: This attribute is a Method type alias that represents the HTTP
    # method that should be used to access the document.
    method: Method


class Response(TypedDict):
    """`Response`: This class represents a basic response.
    It is a subclass of `TypedDict`."""

    # requestId: This attribute is a required string or UUID object
    # representing the ID of the request.
    requestId: Id
    # requestTime: This attribute is a required string representing the
    # date and time the request was received.
    requestTime: str
    # requestTimeEpoch: This attribute is a required integer representing the
    # epoch time the request was received.
    requestTimeEpoch: int
    # responseId: This attribute is a required string or UUID object
    # representing the ID of the response.
    responseId: Id
    # responseTime: This attribute is a required string representing the
    # date and time the response was received.
    responseTime: str
    # responseTimeEpoch: This attribute is a required integer representing the
    # epoch time the response was received.
    responseTimeEpoch: int


class ResponseDetail(Response):
    """`ResponseDetail`: This class represents more detailed `Response`.
    It inherits from `Response` and adds the `content` attribute."""

    content: Content


class ResponseGroup(Response):
    """`ResponseGroup`: This class represents more detailed `Response`.
    It inherits from `Response` and adds the `collection` attribute."""

    collection: List[Content]
