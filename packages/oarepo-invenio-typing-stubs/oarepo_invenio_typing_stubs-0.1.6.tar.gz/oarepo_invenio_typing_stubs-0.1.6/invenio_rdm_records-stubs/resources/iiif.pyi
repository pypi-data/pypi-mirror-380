from abc import ABC, abstractmethod
from typing import Any, Callable

import marshmallow as ma
from flask import Response
from flask_resources import Resource, ResourceConfig, ResponseHandler
from invenio_records_resources.resources.errors import ErrorHandlersMixin
from invenio_records_resources.resources.records.resource import (
    request_headers as request_headers,
)
from invenio_records_resources.resources.records.resource import (
    request_read_args as request_read_args,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from werkzeug.utils import cached_property

class IIIFResourceConfig(ResourceConfig, ConfiguratorMixin):
    blueprint_name: str
    url_prefix: str
    routes: dict[str, str]
    request_view_args: dict[str, ma.fields.Field]
    request_read_args: dict[str, ma.fields.Field]
    request_headers: dict[str, ma.fields.Field]
    response_handler: dict[str, ResponseHandler]
    supported_formats: dict[str, str]
    proxy_cls: Any
    error_handlers: dict[type, Any]

def with_iiif_content_negotiation(
    serializer: type,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...

iiif_request_view_args: Any

class IIIFResource(ErrorHandlersMixin, Resource):
    service: Any
    def __init__(self, config: IIIFResourceConfig, service: Any) -> None: ...
    @cached_property
    def proxy(self) -> Callable[[], Any] | None: ...
    @staticmethod
    def proxy_pass(f: Callable[..., Any]) -> Callable[..., Any]: ...
    def create_url_rules(self) -> list[Any]: ...
    def _get_record_with_files(self) -> Any: ...
    def manifest(self) -> tuple[dict[str, Any], int]: ...
    def sequence(self) -> tuple[dict[str, Any], int]: ...
    def canvas(self) -> tuple[dict[str, Any], int]: ...
    def base(self) -> Any: ...
    def info(self) -> tuple[dict[str, Any], int]: ...
    def image_api(self) -> Response: ...

class IIIFProxy(ABC):
    def should_proxy(self) -> bool: ...
    @abstractmethod
    def proxy_request(self) -> Any: ...
    def __call__(self) -> Any: ...

class IIPServerProxy(IIIFProxy):
    @property
    def server_url(self) -> str | None: ...
    def proxy_request(self) -> Response | None: ...
    def _rewrite_url(self) -> str: ...
