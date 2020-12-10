# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
# Copyright (C) 2020 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module with nice defaults for MARC21 overlay."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "invenio-db>=1.0.6",
    "invenio-i18n>=1.2.0",
    "invenio-indexer>=1.1.0",
    "invenio_search>=1.3.1",
    "pytest-invenio>=1.4.0",
    "elasticsearch_dsl>=7.2.1",
    "SQLAlchemy-Continuum>=1.3.11",
]

# Should follow inveniosoftware/invenio versions
invenio_db_version = ">=1.0.4,<2.0.0"
invenio_search_version = ">=1.4.0,<2.0.0"

extras_require = {
    "docs": [
        "Sphinx>=1.5.2",
    ],
    "elasticsearch7": [
        "invenio-search[elasticsearch7]{}".format(invenio_search_version),
    ],
    "postgresql": [
        "invenio-db[postgresql,versioning]{}".format(invenio_db_version),
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for name, reqs in extras_require.items():
    if name[0] == ":" or name in ("elasticsearch7", "postgresql"):
        continue
    extras_require["all"].extend(reqs)

setup_requires = [
    "Babel>=1.3",
    "pytest-runner>=2.6.2",
]

install_requires = [
    "Flask>=0.11.1",
    "Flask-BabelEx>=0.9.4",
    "dojson>=1.3.0",
    "invenio-jsonschemas>=1.0.0",
    "invenio-records>=1.4.0a4,<2.0.0",
    "invenio-records-files>=1.2.1,<2.0.0",
    "invenio-records-ui>=1.2.0a1,<2.0.0",
    "invenio-previewer>=1.2.1,<2.0.0",
    # until fix in invenio-previewer is released
    "nbconvert[execute]>=4.1.0,<6.0.0",
    # TODO: Get from invenio-base
    "six>=1.12.0",  # Needed to pass CI tests
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("invenio_marc21", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="invenio-marc21",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="invenio MARC21",
    license="MIT",
    author="Graz University of Technology",
    author_email="info@tugraz.at",
    url="https://github.com/tu-graz-library/invenio-marc21",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "invenio_marc21 = invenio_marc21:InvenioMARC21",
        ],
        "invenio_i18n.translations": [
            "messages = invenio_marc21",
        ],
        "invenio_jsonschemas.schemas": [
            "marc21 = dojson.contrib.marc21.schemas",
        ],
        "invenio_search.mappings": [
            "marc21 = invenio_marc21.mappings",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Development Status :: 3 - Alpha",
    ],
)
