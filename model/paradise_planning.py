# pylint: disable=C0114,C0115
from typing import List, Optional, TypedDict  # pylint: disable=W0611


class RequestDelete(TypedDict):
    pass


class RequestGet(TypedDict):
    pass


class RequestPatch(TypedDict):
    pass


class RequestPost(TypedDict):
    filename: Optional[str]
    furniture_ids: List[str]
    furniture_names: List[str]
    image: Optional[str]
    internal_category: str
    internal_id: Optional[int]
    internal_name: str
    name: Optional[str]
    song_name: str
    title: str
    unique_id: str
    version: Optional[str]
    version_added: str
    villager_thought: str
