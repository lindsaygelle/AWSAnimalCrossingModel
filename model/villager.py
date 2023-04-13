"""`villager` module defines several classes representing data
structures related to villager characters in Animal Crossing."""
from typing import Literal, Optional

from .database import Id, Record
from .net import Link

# Document: This is a type alias that represents the possible values for the
# document attribute in the Detail, ResidentDetail, and SpecialDetail classes.
# It can be either "Villager" or "VillagerSpecial".
Document = Literal["Villager", "VillagerSpecial"]
# Gender: This is a type alias that represents the possible values for the
# gender and gender_alternative attributes in the Basic class.
# It can be either "Female", "Male", or "Other".
Gender = Literal["Female", "Male", "Other"]


class Basic(Record):
    """Basic: This class represents basic information about a villager, such
    as their name, gender, and species. It inherits from Record and adds
    several new attributes, including bubble_color, name_color, and link."""

    bubble_color: str
    gender: Gender
    gender_alternative: Optional[Gender]
    link: Link
    name: str
    name_color: str
    species: str


class Detail(Basic):
    """Detail: This class represents more detailed information about
    a villager, including their birthday, clothing, and personality.
    It inherits from Basic and adds several new attributes,
    including birth_day, clothing_id, and personality_id."""

    birth_day: int
    birth_month: int
    clothing_id: Id
    document: Document
    file_name: str
    hobby_id: Id
    image_id: Id
    internal_id: Optional[str]
    is_special: bool


class ResidentDetail(Detail):
    """ResidentDetail: This class represents detailed information about a
    regular villager. It inherits from Detail and adds several new attributes,
    including house_id, motto, and song_id. The document attribute is
    overridden to always be the string "Villager"."""

    document: Literal["Villager"]
    house_id: Id
    motto: str
    personality_id: Id
    saying: str
    song_id: Id


class SpecialDetail(Detail):
    """SpecialDetail: This class represents detailed information about a
    special villager. It inherits from Detail and adds several new attributes,
    including image_id, internal_id, and is_special. The document attribute is
    overridden to always be the string "VillagerSpecial"."""

    document: Literal["VillagerSpecial"]
