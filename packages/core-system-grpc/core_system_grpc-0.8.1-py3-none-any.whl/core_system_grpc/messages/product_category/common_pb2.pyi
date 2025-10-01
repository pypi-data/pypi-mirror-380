from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProductCategory(_message.Message):
    __slots__ = ("id", "shop_id", "old_category_id", "platform_id", "category_no", "category_name", "category_depth", "parent_category_no", "display_type", "full_category_name", "full_category_no", "root_category_no", "sub_category_product_display", "use_display", "product_no", "category_by_product_count", "recommend_common_exclusion", "promotion_common_exclusion", "is_deleted", "updated_at", "parent_category_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHOP_ID_FIELD_NUMBER: _ClassVar[int]
    OLD_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_DEPTH_FIELD_NUMBER: _ClassVar[int]
    PARENT_CATEGORY_NO_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FULL_CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_CATEGORY_NO_FIELD_NUMBER: _ClassVar[int]
    ROOT_CATEGORY_NO_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_PRODUCT_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    USE_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_BY_PRODUCT_COUNT_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_COMMON_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_COMMON_EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PARENT_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    shop_id: str
    old_category_id: str
    platform_id: str
    category_no: str
    category_name: str
    category_depth: str
    parent_category_no: str
    display_type: str
    full_category_name: str
    full_category_no: str
    root_category_no: str
    sub_category_product_display: str
    use_display: str
    product_no: str
    category_by_product_count: str
    recommend_common_exclusion: str
    promotion_common_exclusion: str
    is_deleted: str
    updated_at: str
    parent_category_id: str
    def __init__(self, id: _Optional[str] = ..., shop_id: _Optional[str] = ..., old_category_id: _Optional[str] = ..., platform_id: _Optional[str] = ..., category_no: _Optional[str] = ..., category_name: _Optional[str] = ..., category_depth: _Optional[str] = ..., parent_category_no: _Optional[str] = ..., display_type: _Optional[str] = ..., full_category_name: _Optional[str] = ..., full_category_no: _Optional[str] = ..., root_category_no: _Optional[str] = ..., sub_category_product_display: _Optional[str] = ..., use_display: _Optional[str] = ..., product_no: _Optional[str] = ..., category_by_product_count: _Optional[str] = ..., recommend_common_exclusion: _Optional[str] = ..., promotion_common_exclusion: _Optional[str] = ..., is_deleted: _Optional[str] = ..., updated_at: _Optional[str] = ..., parent_category_id: _Optional[str] = ...) -> None: ...
