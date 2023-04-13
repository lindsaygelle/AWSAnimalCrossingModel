"""method"""
from enum import Enum


class Method(str, Enum):
    """`Method`: This class represents the available HTTP methods.
    It is a subclass of `Enum`."""

    # HTTP Method for retrieving resources.
    GET: str = "GET"

    # HTTP Method for submitting data to a resource.
    POST: str = "POST"

    # HTTP Method for replacing all representations of a resource.
    PUT: str = "PUT"

    # HTTP Method for updating a resource.
    PATCH: str = "PATCH"

    # HTTP Method for deleting a resource.
    DELETE: str = "DELETE"

    # HTTP Method for retrieving the available communication
    # options for a resource.
    OPTIONS: str = "OPTIONS"

    # HTTP Method for requesting that a resource be changed to a different URI.
    HEAD: str = "HEAD"

    # HTTP Method for initiating a resource retrieval that can be
    # resumed at a later time.
    CONNECT: str = "CONNECT"

    # HTTP Method for describing the communication options
    # for the target resource.
    TRACE: str = "TRACE"
