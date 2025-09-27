# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2024 CERN.
# Copyright (C) 2020-2025 Northwestern University.
# Copyright (C) 2023 Graz University of Technology.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Record Service API."""

from typing import Any, Callable, ClassVar, Sequence

import marshmallow as ma
from invenio_indexer.api import RecordIndexer
from invenio_records.dumpers import Dumper
from invenio_records_resources.records import Record
from invenio_records_resources.services.base import ServiceConfig
from invenio_records_resources.services.base.links import Link
from invenio_records_resources.services.records.components.base import ServiceComponent
from invenio_records_resources.services.records.params import ParamInterpreter
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_search import RecordsSearchV2

class SearchOptions:
    """Search options."""

    search_cls: ClassVar[type[RecordsSearchV2]]
    query_parser_cls: ClassVar[type[QueryParser]]
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    sort_default: ClassVar[str] = "bestmatch"
    sort_default_no_query: ClassVar[str] = "newest"
    sort_options: ClassVar[dict[str, dict[str, Any]]]
    facets: ClassVar[dict[str, Any]]
    pagination_options: ClassVar[dict[str, int]]
    params_interpreters_cls: ClassVar[list[type[ParamInterpreter]]] | property

class RecordServiceConfig(ServiceConfig):
    """Service factory configuration."""

    # Record specific configuration
    record_cls: ClassVar[type[Record]]
    indexer_cls: ClassVar[type[RecordIndexer]]
    indexer_queue_name: ClassVar[str]
    index_dumper: ClassVar[Dumper | None]
    # inverse relation mapping, stores which fields relate to which record type
    relations: ClassVar[dict[str, Any]]

    # Search configuration
    search: ClassVar[type[SearchOptions]]

    # Service schema
    schema: ClassVar[type[ma.Schema] | None]

    # Definition of those is left up to implementations

    @property
    def links_item(
        self,
    ) -> dict[
        str, Callable[..., Any] | Link
    ]: ...  # keep typing to be able to use property
    @property
    def links_search(
        self,
    ) -> dict[
        str, Callable[..., Any] | Link
    ]: ...  # keep typing to be able to use property
    @property
    def components(
        self,
    ) -> Sequence[type[ServiceComponent]]: ...  # keep typing to be able to use property
