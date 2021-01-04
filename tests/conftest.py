# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Pytest configuration."""

from __future__ import absolute_import, print_function

import os
from time import sleep

import pytest
from flask import Flask
from flask_babelex import Babel
from invenio_db import InvenioDB, db
from invenio_indexer import InvenioIndexer
from invenio_jsonschemas import InvenioJSONSchemas
from invenio_records import InvenioRecords
from invenio_search import InvenioSearch

from invenio_marc21 import InvenioMARC21


@pytest.fixture(scope="module")
def celery_config():
    """Override pytest-invenio fixture."""
    return {}


@pytest.fixture(scope="module")
def app_config(app_config):
    """Override pytest-invenio app_config fixture.
    For test purposes we need to enforce the configuration variables set in
    config.py. Because invenio-rdm-records is not a flavour extension, it does
    not enforce them via a config entrypoint or ext.py; only flavour
    extensions are allowed to forcefully set configuration.
    This means there is a clash between configuration set by
    invenio-records-rest and this module for instance. We want this module's
    config.py to apply in tests.
    """
    supported_configurations = [
        "MARC21_REST_ENDPOINTS",
    ]
    from invenio_marc21 import config as _config

    for config_key in supported_configurations:
        app_config[config_key] = getattr(_config, config_key, None)

    return app_config


from invenio_app.factory import create_api


@pytest.fixture(scope="module")
def create_app():
    return create_api
