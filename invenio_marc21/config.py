# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Nice defaults for an overlay using MARC21 format."""

import copy

from invenio_records_rest.config import RECORDS_REST_ENDPOINTS
from invenio_records_rest.query import es_search_factory
from invenio_records_rest.utils import allow_all, check_elasticsearch
from invenio_records_ui.config import RECORDS_UI_ENDPOINTS

MARC21_REST_ENDPOINTS = {
    "marcid": dict(
        pid_type="marcid",
        pid_minter="marcid",
        pid_fetcher="marcid",
        default_endpoint_prefix=True,
        record_class="invenio_marc21.api:Marc21RecordBase",
        search_class="invenio_search.RecordsSearch",
        search_index=None,
        search_type=None,
        indexer_class="invenio_marc21.indexer:Marc21RecordIndexer",
        record_serializers={
            "application/json": "invenio_records_rest.serializers:json_v1_response",
            "application/marcxml+xml": (
                "invenio_marc21.serializers:marcxml_v1_response"
            ),
            "application/mods+xml": "invenio_marc21.serializers:mods_v1_response",
            "application/xml": "invenio_marc21.serializers:dublincore_v1_response",
        },
        search_serializers={
            "application/json": "invenio_records_rest.serializers:json_v1_search",
            "application/marcxml+xml": ("invenio_marc21.serializers:marcxml_v1_search"),
            "application/mods+xml": "invenio_marc21.serializers:mods_v1_search",
            "application/xml": "invenio_marc21.serializers:dublincore_v1_search",
        },
        record_loaders={
            "application/json": ("invenio_records_rest.loaders" ":json_v1"),
            "application/marcxml+json": ("invenio_marc21.loaders" ":marcxml_v1"),
        },
        list_route="/marc/",
        item_route="/marc/<pid(marcid):pid_value>",
        default_media_type="application/json",
        max_result_window=10000,
        error_handlers=dict(),
        create_permission_factory_imp=allow_all,
        read_permission_factory_imp=check_elasticsearch,
        update_permission_factory_imp=allow_all,
        delete_permission_factory_imp=allow_all,
    ),
}
