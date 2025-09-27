# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
# Copyright (C) 2023 TU Wien.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Resources module to create REST APIs."""

from typing import Any, Callable, ParamSpec, TypeAlias, TypeVar

from flask_resources import Resource
from invenio_records_resources.resources.errors import ErrorHandlersMixin
from invenio_records_resources.resources.records.config import RecordResourceConfig
from invenio_records_resources.services.records.service import RecordService

P = ParamSpec("P")
R = TypeVar("R")
Decorator: TypeAlias = Callable[[Callable[P, R]], Callable[P, R]]

class RecordResource(ErrorHandlersMixin, Resource):
    """Record resource."""

    service: RecordService

    def __init__(
        self, config: RecordResourceConfig, service: RecordService
    ) -> None: ...
    def create_url_rules(self) -> list[dict[str, Any]]: ...
    def search(self) -> tuple[dict[str, Any], int]: ...
    def create(self) -> tuple[dict[str, Any], int]: ...
    def read(self) -> tuple[dict[str, Any], int]: ...
    def update(self) -> tuple[dict[str, Any], int]: ...
    def delete(self) -> tuple[str, int]: ...

# Decorators
request_data: Decorator
request_read_args: Decorator
request_view_args: Decorator
request_headers: Decorator
request_search_args: Decorator
request_extra_args: Decorator
