# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020-2025 Northwestern University.
# Copyright (C) 2025 CESNET.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""File resource configuration."""

from typing import Callable, ClassVar

from flask import Response
from flask_resources import ResourceConfig

class FileResourceConfig(ResourceConfig):
    """File resource config."""

    blueprint_name: ClassVar[None] = None
    url_prefix: ClassVar[str] = "/records/<pid_value>"
    routes: ClassVar[dict[str, str]]
    error_handlers: ClassVar[
        dict[type[BaseException], Callable[[BaseException], Response]]
    ]
