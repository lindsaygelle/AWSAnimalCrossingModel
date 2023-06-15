# pylint: disable=C0114,C0115
from typing import List, Optional, TypedDict  # pylint: disable=W0611


class RequestDelete(TypedDict):
    pass


class RequestGet(TypedDict):
    pass


class RequestPatch(TypedDict):
    pass


class RequestPost(TypedDict):
    birthday_day: int
    birthday_month: int
    bubble_color: str
    filename: Optional[str]
    filename_icon: str
    filename_photo: str
    gender_name: str
    gender_name_alternative: str
    hobby_name: str
    id: str
    image: Optional[str]
    image_icon: str
    image_photo: str
    image_photo_alternative: Optional[str]
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    name: Optional[str]
    name_color: str
    umbrella_hhp: Optional[str]
    umbrella_name: Optional[str]
    unique_id: str
    version: Optional[str]
    version_added: str
