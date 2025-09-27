# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Record Resource Configuration."""

from typing import Any, ClassVar

import marshmallow as ma
from flask_resources import RequestBodyParser, ResourceConfig, ResponseHandler
from invenio_records_resources.resources.records.args import SearchRequestArgsSchema

class RecordResourceConfig(ResourceConfig):
    """Record resource config."""

    # Blueprint configuration
    blueprint_name: ClassVar[None] = None
    url_prefix: ClassVar[str] = "/records"
    routes: ClassVar[dict[str, str]]

    # Request parsing
    request_read_args: ClassVar[dict[str, Any]]
    request_view_args: ClassVar[dict[str, ma.fields.Field]]
    request_search_args: ClassVar[type[SearchRequestArgsSchema]]
    request_extra_args: ClassVar[dict[str, ma.fields.Field]]
    request_headers: ClassVar[dict[str, ma.fields.Field]]
    request_body_parsers: ClassVar[dict[str, RequestBodyParser]]
    default_content_type: ClassVar[str]

    # Response handling
    response_handlers: ClassVar[dict[str, ResponseHandler]]
    default_accept_mimetype: ClassVar[str]
