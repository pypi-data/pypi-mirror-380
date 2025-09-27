#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.11.23 00:00:00                  #
# ================================================== #

from sqlalchemy import text

from .base import BaseMigration


class Version20241215110000(BaseMigration):
    def __init__(self, window=None):
        super(Version20241215110000, self).__init__(window)
        self.window = window

    def up(self, conn):
        conn.execute(text("""
        ALTER TABLE ctx_group ADD COLUMN additional_ctx_json TEXT;
        """))
