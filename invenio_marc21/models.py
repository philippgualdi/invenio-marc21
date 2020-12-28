# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Graz University of Technology.
#
# invenio-Marc21 is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Marc21 database models."""

# TODO: uncomment to create a new table for the lom records.
# from __future__ import absolute_import, print_function

# from invenio_db import db
# from invenio_records.models import RecordMetadataBase


# class MarcMetadata(db.Model, RecordMetadataBase):
#     """Represent a Marc21."""

#     __tablename__ = 'Marc21_metadata'
#     __table_args__ = {'extend_existing': True}
#     __versioned__ = {'versioning': False}

#     is_deleted = db.Column(
#         db.Boolean(name="ck_invenio-marc21_metadata_is_deleted"),
#         nullable=True,
#         default=False
#     )
#     """Was the lom soft-deleted."""

#     def delete(self):
#         """Mark the mARC21 for deletion."""
#         self.is_deleted = True
