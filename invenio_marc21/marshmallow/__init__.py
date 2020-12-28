# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Graz University of Technology.
#
# invenio-records-lom is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Schemas for marshmallow."""

from __future__ import absolute_import, print_function

from .json import MarcSchemaV1, MarcxmlMetadataSchemaV1

__all__ = (
    "MarcxmlMetadataSchemaV1",
    "MarcSchemaV1",
)
