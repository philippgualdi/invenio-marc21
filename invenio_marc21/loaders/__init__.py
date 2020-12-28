# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Graz University of Technology.
#
# invenio-records-lom is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Loaders.

Think of loaders as the definition of your input formats for records.

You only need loaders if you plan to allow creation of records via the REST API.

The loaders are responsible for transforming a request payload (external representation) into the internal JSON format.
"""

from __future__ import absolute_import, print_function

from invenio_records_rest.loaders.marshmallow import marshmallow_loader

from ..marshmallow import MarcxmlMetadataSchemaV1

marcxml_v1 = marshmallow_loader(MarcxmlMetadataSchemaV1)

__all__ = ("marcxml_v1",)
