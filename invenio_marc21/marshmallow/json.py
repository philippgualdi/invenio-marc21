# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Graz University of Technology.
#
# invenio-records-lom is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from dojson import Overdo
from dojson.contrib.marc21 import marc21
from dojson.contrib.marc21.utils import create_record, load
from invenio_records_rest.schemas.fields import PersistentIdentifier, SanitizedUnicode
from invenio_rest.serializer import BaseSchema
from marshmallow import fields, post_load, pre_dump


class MarcxmlMetadataSchemaV1(BaseSchema):
    """Marcxml metadata."""

    id = PersistentIdentifier()

    schema = SanitizedUnicode(required=False)
    record = SanitizedUnicode(required=True)

    @post_load
    def postload(self, item, many, **kwargs):
        item["record"] = marc21.do(create_record(item["record"]))
        return item


class MarcSchemaV1(BaseSchema):
    """Marc schema."""

    metadata = fields.Nested(MarcxmlMetadataSchemaV1)
    created = fields.Str(dump_only=True)
    updated = fields.Str(dump_only=True)
    id = PersistentIdentifier()
