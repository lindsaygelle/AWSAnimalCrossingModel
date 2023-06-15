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
    image_album: str
    image_frame: str
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    is_cataloged: bool
    is_sale: bool
    is_seasonal: bool
    is_unlocked: bool
    name: Optional[str]
    sell_currency: Optional[str]
    sell_price: Optional[int]
    size_1: Optional[float]
    size_2: Optional[float]
    source_names: List[str]
    unique_id: str
    version: Optional[str]
    version_added: str
