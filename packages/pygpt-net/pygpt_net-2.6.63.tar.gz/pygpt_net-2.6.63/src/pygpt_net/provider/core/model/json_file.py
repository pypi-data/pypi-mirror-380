#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.07.17 21:00:00                  #
# ================================================== #

import json
import os
import shutil
from typing import Optional, Dict, Any

from packaging.version import Version

from pygpt_net.provider.core.model.base import BaseProvider
from pygpt_net.item.model import ModelItem

from .patch import Patch


class JsonFileProvider(BaseProvider):
    def __init__(self, window=None):
        super(JsonFileProvider, self).__init__(window)
        self.window = window
        self.patcher = Patch(window)
        self.id = "json_file"
        self.type = "model"
        self.config_file = 'models.json'

    def install(self):
        """Install provider data files"""
        dst = os.path.join(self.window.core.config.path, self.config_file)
        if not os.path.exists(dst):
            src = os.path.join(self.window.core.config.get_app_path(), 'data', 'config', self.config_file)
            shutil.copyfile(src, dst)
        else:
            # check if models file is correct - if not, then restore from base models
            try:
                with open(dst, 'r', encoding="utf-8") as file:
                    json.load(file)
            except json.JSONDecodeError:
                print("RECOVERY: Models file `{}` is corrupted. Restoring from base models.".format(dst))
                backup_dst = os.path.join(self.window.core.config.path, 'models.bak.json')
                if os.path.exists(backup_dst):
                    os.remove(backup_dst)
                shutil.copyfile(dst, backup_dst)
                os.remove(dst)
                print("RECOVERY: Backup of corrupted models file created: {}".format(backup_dst))
                src = os.path.join(self.window.core.config.get_app_path(), 'data', 'config', self.config_file)
                shutil.copyfile(src, dst)
                print("RECOVERY: Restored models file from base models: {}".format(src))

    def get_version(self) -> Optional[str]:
        """
        Get data version

        :return: version
        """
        path = os.path.join(self.window.core.config.path, self.config_file)
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            if data == "" or data is None:
                return
            if '__meta__' in data and 'version' in data['__meta__']:
                return data['__meta__']['version']

    def load_base(self) -> Optional[Dict[str, ModelItem]]:
        """
        Load base models config from base JSON file

        :return: models dict
        """
        path = os.path.join(self.window.core.config.get_app_path(), 'data', 'config', self.config_file)
        return self.load(path)

    def load(self, path: Optional[str] = None) -> Optional[Dict[str, ModelItem]]:
        """
        Load models config from JSON file

        :param path: path to JSON file, if None then use default path
        """
        items = {}
        if path is None:
            path = os.path.join(self.window.core.config.path, self.config_file)

        if not os.path.exists(path):
            print("FATAL ERROR: {} not found!".format(path))
            return None
        try:
            with open(path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                if data == "" or data is None:
                    return {}

                # migrate from old versions < 2.0.49
                if 'items' not in data:
                    for id in data:
                        if id == '__meta__':
                            continue
                        item = data[id]
                        model = ModelItem()
                        self.deserialize(item, model)
                        items[id] = model
                    items = dict(sorted(items.items(), key=lambda item: item[0]))  # sort by key
                    if self.window.core.config.path in path:
                        # only if path is in config path, otherwise it's base config
                        print("Loaded models: {}".format(path))
                    print("Migrating old version: {}".format(path))
                    self.save(items)
                    return items

                # deserialize
                for id in data['items']:
                    item = data['items'][id]
                    model = ModelItem()
                    self.deserialize(item, model)
                    items[id] = model
                items = dict(sorted(items.items(), key=lambda x: x[1].name.lower()))
                if self.window.core.config.path in path:
                    # only if path is in config path, otherwise it's base config
                    print("Loaded models: {}".format(path))

        except Exception as e:
            self.window.core.debug.log(e)

        return items

    def save(self, items: Dict[str, ModelItem]):
        """
        Save models config to JSON file

        :param items: models dict
        """
        path = os.path.join(self.window.core.config.path, self.config_file)
        try:
            data = {}
            ary = {}

            # serialize
            for id in items:
                model = items[id]
                ary[id] = self.serialize(model)

            data['__meta__'] = self.window.core.config.append_meta()
            data['items'] = ary
            dump = json.dumps(data, indent=4)
            with open(path, 'w', encoding="utf-8") as f:
                f.write(dump)

        except Exception as e:
            self.window.core.debug.log(e)

    def remove(self, id: str):
        pass

    def truncate(self):
        pass

    def patch(self, version: Version) -> bool:
        """
        Migrate models to current app version

        :param version: current app version
        :return: True if updated
        """
        return self.patcher.execute(version)

    @staticmethod
    def serialize(item: ModelItem) -> Dict[str, Any]:
        """
        Serialize item to dict

        :param item: item to serialize
        :return: serialized item
        """
        return {
            'id': item.id,
            'name': item.name,
            'mode': item.mode,
            # 'langchain': item.langchain,
            'llama_index': item.llama_index,
            'ctx': item.ctx,
            'tokens': item.tokens,
            'default': item.default,
            'input': item.input,
            'output': item.output,
            'extra': item.extra,
            'imported': item.imported,
            'provider': item.provider,
            'tool_calls': item.tool_calls,
        }

    @staticmethod
    def deserialize(data: Dict[str, Any], item: ModelItem):
        """
        Deserialize item from dict

        :param data: serialized item
        :param item: item to deserialize
        """
        if 'id' in data:
            item.id = data['id']
        if 'name' in data:
            item.name = data['name']
        if 'mode' in data:
            item.mode = data['mode']
        # if 'langchain' in data:
            # item.langchain = data['langchain']
        if 'llama_index' in data:
            item.llama_index = data['llama_index']
        if 'ctx' in data:
            item.ctx = data['ctx']
        if 'tokens' in data:
            item.tokens = data['tokens']
        if 'default' in data:
            item.default = data['default']
        if 'input' in data:
            item.input = data['input']
        if 'output' in data:
            item.output = data['output']
        if 'extra' in data:
            item.extra = data['extra']
        if 'imported' in data:
            item.imported = data['imported']
        if 'provider' in data:
            item.provider = data['provider']
        if 'tool_calls' in data:
            item.tool_calls = data['tool_calls']

    def dump(self, item: ModelItem) -> str:
        """
        Dump to string

        :param item: item to dump
        :return: dumped item as string (json)
        """
        return json.dumps(self.serialize(item))
