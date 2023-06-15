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
    cyrus_currency: Optional[str]
    cyrus_price: Optional[int]
    exchange_currency: Optional[str]
    exchange_price: Optional[int]
    filename: Optional[str]
    filename_alternative: Optional[str]
    image: Optional[str]
    image_alternative: Optional[str]
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    is_seasonal: bool
    is_unlocked: bool
    name: Optional[str]
    sell_currency: Optional[str]
    sell_price: Optional[int]
    source_names: List[str]
    unique_id: str
    version: Optional[str]
    version_added: str
