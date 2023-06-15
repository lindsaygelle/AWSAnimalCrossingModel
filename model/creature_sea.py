# pylint: disable=C0114,C0115
from typing import List, Optional, TypedDict  # pylint: disable=W0611


class RequestDelete(TypedDict):
    pass


class RequestGet(TypedDict):
    pass


class RequestPatch(TypedDict):
    pass


class RequestPost(TypedDict):
    availability_northern: List[str]
    availability_sourthern: List[str]
    buy_currency: Optional[str]
    buy_price: Optional[int]
    color_1: str
    color_2: str
    cyrus_currency: Optional[str]
    cyrus_price: Optional[int]
    description: str
    exchange_currency: Optional[str]
    exchange_price: Optional[int]
    filename: Optional[str]
    filename_critterpedia: str
    filename_furniture: str
    filename_icon: str
    hha_category: Optional[str]
    hha_concept_1: Optional[str]
    hha_concept_2: Optional[str]
    hha_points: Optional[int]
    hha_series: Optional[str]
    hha_set: Optional[str]
    image: Optional[str]
    image_critterpedia: str
    image_furniture: str
    image_icon: str
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    is_surface: bool
    is_unlocked: bool
    lighting_category: Optional[str]
    name: Optional[str]
    rate_maximum: int
    rate_minimum: int
    saying: str
    sell_currency: Optional[str]
    sell_price: Optional[int]
    size_1: Optional[float]
    size_2: Optional[float]
    unique_id: str
    version: Optional[str]
    version_added: str
