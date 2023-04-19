from typing import Literal, Union

from .database import Id, Record
from .net import Link

# DocumentCategory: A string literal that represents the
# category of a document in the HHA data.
DocumentCategory = Literal["HHACategory"]
# DocumentCollection: A string literal that represents the
# collection of a document in the HHA data.
DocumentCollection = Literal["HHACollection"]
# DocumentConcept: A string literal that represents the
# concept of a document in the HHA data
DocumentConcept = Literal["HHAConcept"]
# DocumentSeries: A string literal that represents the
# series of a document in the HHA data.
DocumentSeries = Literal["HHASeries"]
# Document: A union of the four document types above,
# representing any kind of HHA document.
Document = Union[
    DocumentCategory, DocumentCollection, DocumentConcept, DocumentSeries
]


class Basic(Record):
    """`Basic`: A record representing basic HHA data, with fields
    including the document type, id, link, and name."""

    # document: This attribute is a string representing the
    # document that the link points to
    document: Document
    # id: This attribute is an Id type alias representing the unique
    # identifier of the record. It can be either an integer or a string.
    id: Id
    link: Link
    name: str


class CategoryBasic(Record):
    """`CategoryBasic`: A record representing basic category data,
    with a document field of type DocumentCategory."""

    document: DocumentCategory


class CollectionBasic(Record):
    """`CollectionBasic`: A record representing basic collection data,
    with a document field of type DocumentCollection."""

    document: DocumentCollection


class ConceptBasic(Record):
    """`ConceptBasic`: A record representing basic concept data,
    with a document field of type DocumentConcept."""

    document: DocumentConcept


class SeriesBasic(Record):
    """SeriesBasic: A record representing basic series data,
    with a document field of type DocumentSeries."""

    document: DocumentSeries
