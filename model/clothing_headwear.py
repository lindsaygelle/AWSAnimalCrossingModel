# pylint: disable=C0114,C0115
from typing import List, Optional, TypedDict  # pylint: disable=W0611


class RequestDelete(TypedDict):
    pass


class RequestGet(TypedDict):
    pass


class RequestPatch(TypedDict):
    pass


class RequestPost(TypedDict):
    buy_currency: Optional[str]
    buy_price: Optional[int]
    category_name: Optional[str]
    clothing_group_id: int
    color_1: str
    color_2: str
    cyrus_currency: Optional[str]
    cyrus_price: Optional[int]
    exchange_currency: Optional[str]
    exchange_price: Optional[int]
    filename: Optional[str]
    filename_closet: str
    gender_name: str
    hha_category: Optional[str]
    hha_concept_1: Optional[str]
    hha_concept_2: Optional[str]
    hha_points: Optional[int]
    hha_series: Optional[str]
    hha_set: Optional[str]
    image: Optional[str]
    image_closet: str
    image_storage: str
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    is_available_autumn: bool
    is_available_spring: bool
    is_available_summer: bool
    is_available_winter: bool
    is_cataloged: bool
    is_craftable: bool
    is_equipment: bool
    is_feminine: bool
    is_mannequin_summer: bool
    is_mannequin_winter: bool
    is_masculine: bool
    is_sale: bool
    is_seasonal: bool
    is_unlocked: bool
    label_names: List[str]
    name: Optional[str]
    sell_currency: Optional[str]
    sell_price: Optional[int]
    size_1: Optional[float]
    size_2: Optional[float]
    sort_order: int
    source_names: List[str]
    style_1: str
    style_2: str
    unique_id: str
    variation_name: Optional[str]
    version: Optional[str]
    version_added: str
