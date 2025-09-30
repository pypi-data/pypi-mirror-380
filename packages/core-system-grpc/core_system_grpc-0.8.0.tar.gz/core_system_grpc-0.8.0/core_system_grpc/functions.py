import json
from typing import Type, Union
import logging
from core_system_grpc.services.product_service_pb2_grpc import (
    ProductServiceStub,
)
from core_system_grpc.messages.common.request_pb2 import (
    GetByShopRequest,
)
from core_system_grpc.messages.common.pagination_pb2 import PaginationRequest
from core_system_grpc.services.shop_service_pb2_grpc import ShopServiceStub
from core_system_grpc.messages.shop.request_pb2 import (
    GetShopListRequest,
)
from core_system_grpc.services.order_service_pb2_grpc import OrderServiceStub
from core_system_grpc.services.customer_service_pb2_grpc import (
    CustomerServiceStub,
)
from google.protobuf.json_format import MessageToDict
import grpc

logging.basicConfig(level=logging.INFO)


def _make_grpc_request(
    core_grpc_host: str,
    core_grpc_port: int,
    stub_class: Type,
    method_name: str,
    shop_id: Union[str, int] = None,
    request_class: Type = GetByShopRequest,
    **kwargs,
) -> str:
    """
    공통 gRPC 요청 처리 함수

    Args:
        core_grpc_host: gRPC 호스트
        core_grpc_port: gRPC 포트
        stub_class: gRPC Stub 클래스
        method_name: 호출할 메서드명
        shop_id: 상점 ID (문자열 또는 정수로 받아서 문자열로 변환)
        **kwargs: 요청에 필요한 추가 파라미터
            filters: 필터 조건
            embed: 포함하고 싶은 관계형 모델
            fields: 포함하고 싶은 필드
            limit: 가져올 아이템 수
            offset: 가져올 아이템 시작 인덱스

    Returns:
        JSON 문자열로 변환된 응답
    """
    channel_url = f"{core_grpc_host}:{core_grpc_port}"
    with grpc.insecure_channel(channel_url) as channel:
        stub = stub_class(channel)
        # Request 객체 생성 - shop_id를 문자열로 변환
        kwargs = {**kwargs, "shop_id": str(shop_id)} if shop_id else kwargs
        request = request_class(**kwargs)

        # gRPC 메서드 호출
        method = getattr(stub, method_name)
        response = method(request)

        # 응답을 딕셔너리로 변환
        response_dict = MessageToDict(
            message=response,
            always_print_fields_with_no_presence=False,
            preserving_proto_field_name=True,
        )

        # JSON 문자열로 변환
        response_json = json.dumps(response_dict, ensure_ascii=False, indent=4)

        return response_json


def get_product_by_grpc(
    core_grpc_host: str,
    core_grpc_port: int,
    shop_id: Union[str, int],
    limit: Union[str, int],
    offset: Union[str, int],
    filters=None,
    filter_type=None,
    embed=None,
    fields=None,
):
    """
    상점별 상품 목록을 gRPC를 통해 조회합니다.

    Args:
        core_grpc_host: gRPC 호스트
        core_grpc_port: gRPC 포트
        shop_id: 상점 ID (문자열 또는 정수)
        limit: 가져올 아이템 수 (문자열 또는 정수)
        offset: 가져올 아이템 시작 인덱스 (문자열 또는 정수)
        filters: 필터 조건
        filter_type: 필터 타입
        embed: 포함하고 싶은 관계형 모델
        fields: 포함하고 싶은 필드

    Returns:
        JSON 문자열로 변환된 응답
    """
    pagination_request = PaginationRequest(limit=str(limit), offset=str(offset))
    return _make_grpc_request(
        core_grpc_host=core_grpc_host,
        core_grpc_port=core_grpc_port,
        stub_class=ProductServiceStub,
        method_name="GetProductsByShop",
        shop_id=shop_id,
        pagination=pagination_request,
        filters=filters,
        filter_type=filter_type,
        embed=embed,
        fields=fields,
    )


def get_order_by_grpc(
    core_grpc_host: str,
    core_grpc_port: int,
    shop_id: Union[str, int],
    limit: Union[str, int],
    offset: Union[str, int],
    filters=None,
    filter_type=None,
    embed=None,
    fields=None,
):
    """
    상점별 주문 목록을 gRPC를 통해 조회합니다.

    Args:
        core_grpc_host: gRPC 호스트
        core_grpc_port: gRPC 포트
        shop_id: 상점 ID (문자열 또는 정수)
        limit: 가져올 아이템 수 (문자열 또는 정수)
        offset: 가져올 아이템 시작 인덱스 (문자열 또는 정수)
        filters: 필터 조건
        filter_type: 필터 타입
        embed: 포함하고 싶은 관계형 모델
        fields: 포함하고 싶은 필드

    Returns:
        JSON 문자열로 변환된 응답
    """
    pagination_request = PaginationRequest(limit=str(limit), offset=str(offset))
    return _make_grpc_request(
        core_grpc_host=core_grpc_host,
        core_grpc_port=core_grpc_port,
        stub_class=OrderServiceStub,
        method_name="GetOrdersByShop",
        shop_id=shop_id,
        pagination=pagination_request,
        filters=filters,
        filter_type=filter_type,
        embed=embed,
        fields=fields,
    )


def get_shop_by_grpc(
    core_grpc_host: str,
    core_grpc_port: int,
    limit: Union[str, int] = None,
    offset: Union[str, int] = None,
    filters=None,
    filter_type=None,
    embed=None,
    fields=None,
):
    """
    상점 상세 정보를 gRPC를 통해 조회합니다.

    Args:
        core_grpc_host: gRPC 호스트
        core_grpc_port: gRPC 포트
        shop_id: 상점 ID (문자열 또는 정수)
        limit: 가져올 아이템 수 (문자열 또는 정수, 선택사항)
        offset: 가져올 아이템 시작 인덱스 (문자열 또는 정수, 선택사항)
        filters: 필터 조건
        filter_type: 필터 타입
        embed: 포함하고 싶은 관계형 모델
        fields: 포함하고 싶은 필드

    Returns:
        JSON 문자열로 변환된 응답
    """

    pagination_request = PaginationRequest(limit=str(limit), offset=str(offset))
    return _make_grpc_request(
        core_grpc_host=core_grpc_host,
        core_grpc_port=core_grpc_port,
        stub_class=ShopServiceStub,
        request_class=GetShopListRequest,
        method_name="GetShopList",
        pagination=pagination_request,
        filters=filters,
        filter_type=filter_type,
        embed=embed,
        fields=fields,
    )


def get_customer_by_grpc(
    core_grpc_host: str,
    core_grpc_port: int,
    shop_id: Union[str, int],
    limit: Union[str, int],
    offset: Union[str, int],
    filters=None,
    filter_type=None,
    embed=None,
    fields=None,
):
    """
    상점별 고객 목록을 gRPC를 통해 조회합니다.

    Args:
        core_grpc_host: gRPC 호스트
        core_grpc_port: gRPC 포트
        shop_id: 상점 ID (문자열 또는 정수)
        limit: 가져올 아이템 수 (문자열 또는 정수)
        offset: 가져올 아이템 시작 인덱스 (문자열 또는 정수)
        filters: 필터 조건
        filter_type: 필터 타입
        embed: 포함하고 싶은 관계형 모델
        fields: 포함하고 싶은 필드

    Returns:
        JSON 문자열로 변환된 응답
    """
    pagination_request = PaginationRequest(limit=str(limit), offset=str(offset))
    return _make_grpc_request(
        core_grpc_host=core_grpc_host,
        core_grpc_port=core_grpc_port,
        stub_class=CustomerServiceStub,
        method_name="GetCustomersByShop",
        shop_id=shop_id,
        pagination=pagination_request,
        filters=filters,
        filter_type=filter_type,
        embed=embed,
        fields=fields,
    )
