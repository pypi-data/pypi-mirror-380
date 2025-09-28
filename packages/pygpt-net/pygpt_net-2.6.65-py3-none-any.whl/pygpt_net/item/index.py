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

import json
from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class IndexItem:
    id: Optional[object] = None
    name: Optional[object] = None
    store: Optional[object] = None
    items: dict = field(default_factory=dict)

    def __init__(self):
        """
        Index item
        """
        self.id = None
        self.name = None
        self.store = None
        self.items = {}

    def serialize(self) -> dict:
        """
        Serialize item to dict

        :return: serialized item
        """
        return {
            'id': self.id,
            'name': self.name,
            'store': self.store,
            'items': self.items,
        }

    def deserialize(self, data: dict):
        """
        Deserialize item from dict

        :param data: serialized item
        """
        if 'id' in data:
            self.id = data['id']
        if 'name' in data:
            self.name = data['name']
        if 'store' in data:
            self.store = data['store']
        if 'items' in data:
            self.items = data['items']

    def dump(self):
        """
        Dump item to string

        :return: serialized item
        :rtype: str
        """
        try:
            return json.dumps(self.serialize())
        except Exception as e:
            pass
        return ""

    def __str__(self):
        """To string"""
        return self.dump()