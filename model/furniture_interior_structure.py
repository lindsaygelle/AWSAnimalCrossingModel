# pylint: disable=C0114,C0115
from typing import List, Optional, TypedDict  # pylint: disable=W0611


class RequestDelete(TypedDict):
    pass


class RequestGet(TypedDict):
    pass


class RequestPatch(TypedDict):
    pass


class RequestPost(TypedDict):
    body_category: str
    buy_currency: Optional[str]
    buy_price: Optional[int]
    can_customize_body: bool
    can_customize_pattern: bool
    category_name: Optional[str]
    color_1: str
    color_2: str
    cyrus_currency: Optional[str]
    cyrus_price: Optional[int]
    exchange_currency: Optional[str]
    exchange_price: Optional[int]
    filename: Optional[str]
    hha_category: Optional[str]
    hha_concept_1: Optional[str]
    hha_concept_2: Optional[str]
    hha_points: Optional[int]
    hha_series: Optional[str]
    hha_set: Optional[str]
    image: Optional[str]
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    is_cataloged: bool
    is_craftable: bool
    is_interactive: bool
    is_outdoors: bool
    is_sale: bool
    is_seasonal: bool
    is_surface: bool
    is_unlocked: bool
    kit_category: Optional[str]
    kit_currency: Optional[str]
    kit_price: Optional[int]
    lighting_category: Optional[str]
    name: Optional[str]
    pattern_category: Optional[str]
    pattern_name: Optional[str]
    sell_currency: Optional[str]
    sell_price: Optional[int]
    size_1: Optional[float]
    size_2: Optional[float]
    source_names: List[str]
    unique_id: str
    variation_id: Optional[str]
    variation_name: Optional[str]
    version: Optional[str]
    version_added: str
