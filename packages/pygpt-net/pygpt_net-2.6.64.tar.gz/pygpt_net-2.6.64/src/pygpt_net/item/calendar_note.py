#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.05 18:00:00                  #
# ================================================== #

import datetime
import json
import time
from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class CalendarNoteItem:
    id: int = 0
    uuid: Optional[object] = None
    idx: int = 0
    year: int = 0
    month: int = 0
    day: int = 0
    status: int = 0
    title: str = ""
    content: str = ""
    deleted: bool = False
    created: int = 0
    updated: int = 0
    important: bool = False
    initialized: bool = False

    def __init__(self):
        self.id = 0
        self.uuid = None
        self.idx = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.status = 0
        self.title = ""
        self.content = ""
        self.deleted = False
        ts = int(time.time())
        self.created = ts
        self.updated = ts
        self.important = False
        self.initialized = False
        self.deleted = False

    def get_dt(self) -> str:
        """
        Convert year, month, day to key string in format: YYYY-MM-DD
        :return: key string in format: YYYY-MM-DD
        """
        return datetime.datetime(self.year, self.month, self.day).strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            'id': self.id,
            'uuid': str(self.uuid),
            'idx': self.idx,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'status': self.status,
            'title': self.title,
            'content': self.content,
            'deleted': self.deleted,
            'created': self.created,
            'updated': self.updated,
            'important': self.important,
            'initialized': self.initialized
        }

    def dump(self):
        """
        Dump item to string

        :return: serialized item
        :rtype: str
        """
        try:
            return json.dumps(self.to_dict())
        except Exception as e:
            pass
        return ""

    def __str__(self):
        """To string"""
        return self.dump()