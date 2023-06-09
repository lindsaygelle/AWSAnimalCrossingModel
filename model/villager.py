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
    clothing_top_id: int
    color_1: str
    color_2: str
    filename: Optional[str]
    floor_name: str
    furniture_ids: List[str]
    furniture_names: List[str]
    gender_name: str
    hobby_name: str
    image: Optional[str]
    image_house: str
    image_icon: str
    image_photo: str
    image_photo_alternative: Optional[str]
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    kitchen_id: int
    kitchen_variation_id: Optional[str]
    motto: str
    name: Optional[str]
    name_color: str
    personality_category: str
    personality_name: str
    saying: str
    song_name: str
    species_name: str
    style_1: str
    style_2: str
    umbrella_name: Optional[str]
    unique_id: str
    version: Optional[str]
    version_added: str
    wallpaper_name: str
    workbench_id: int
    workbench_variation_id: Optional[str]
