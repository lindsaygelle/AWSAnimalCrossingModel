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
    can_customize: bool
    cyrus_currency: Optional[str]
    cyrus_price: Optional[int]
    exchange_currency: Optional[str]
    exchange_price: Optional[int]
    filename: Optional[str]
    image: Optional[str]
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    is_cataloged: bool
    is_craftable: bool
    is_sale: bool
    is_seasonal: bool
    is_unlocked: bool
    kit_category: Optional[str]
    kit_currency: Optional[str]
    kit_price: Optional[int]
    name: Optional[str]
    sell_currency: Optional[str]
    sell_price: Optional[int]
    source_names: List[str]
    unique_id: str
    variation_id: Optional[str]
    variation_name: Optional[str]
    version: Optional[str]
    version_added: str
