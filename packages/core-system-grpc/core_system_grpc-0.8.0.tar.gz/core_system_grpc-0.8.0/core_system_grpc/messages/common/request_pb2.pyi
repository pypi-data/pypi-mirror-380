from messages.common import pagination_pb2 as _pagination_pb2
from messages.common import search_pb2 as _search_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetByShopRequest(_message.Message):
    __slots__ = ("shop_id", "pagination", "search", "fields", "embed", "order_by", "filter_type", "filters")
    SHOP_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    EMBED_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    shop_id: str
    pagination: _pagination_pb2.PaginationRequest
    search: _search_pb2.SearchRequest
    fields: str
    embed: str
    order_by: str
    filter_type: str
    filters: str
    def __init__(self, shop_id: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PaginationRequest, _Mapping]] = ..., search: _Optional[_Union[_search_pb2.SearchRequest, _Mapping]] = ..., fields: _Optional[str] = ..., embed: _Optional[str] = ..., order_by: _Optional[str] = ..., filter_type: _Optional[str] = ..., filters: _Optional[str] = ...) -> None: ...
