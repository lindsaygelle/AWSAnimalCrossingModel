# pylint: disable=C0114,C0115
from typing import List, Optional, TypedDict  # pylint: disable=W0611


class RequestDelete(TypedDict):
    pass


class RequestGet(TypedDict):
    pass


class RequestPatch(TypedDict):
    pass


class RequestPost(TypedDict):
    back_color: str
    body_color: str
    buy_currency: Optional[str]
    buy_price: Optional[int]
    cyrus_currency: Optional[str]
    cyrus_price: Optional[int]
    exchange_currency: Optional[str]
    exchange_price: Optional[int]
    filename: Optional[str]
    foot_color: Optional[str]
    head_color: Optional[str]
    image: Optional[str]
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    name: Optional[str]
    pen_color_1: Optional[str]
    pen_color_2: Optional[str]
    pen_color_3: Optional[str]
    pen_color_4: Optional[str]
    sell_currency: Optional[str]
    sell_price: Optional[int]
    unique_id: str
    version: Optional[str]
    version_added: str
