#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.06 01:00:00                  #
# ================================================== #

import json

from llama_index.core.readers.base import BaseReader

from .base import BaseLoader


class Loader(BaseLoader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "microsoft_onedrive"
        self.name = "Microsoft OneDrive"
        self.type = ["web"]
        self.instructions = [
            {
                "microsoft_onedrive": {
                    "description": "read and index files from OneDrive",
                    "args": {
                        "folder_id": {
                            "type": "str",
                            "label": "Folder ID",
                        },
                        "file_ids": {
                            "type": "list",
                            "label": "File IDs",
                            "description": "List of file ids, separated by comma (,)",
                        },
                        "mime_types": {
                            "type": "list",
                            "label": "Mime Types",
                            "description": "List of mime types, separated by comma (,)",
                        },
                        "folder_path": {
                            "type": "str",
                            "label": "Folder Path",
                        },
                        "file_paths": {
                            "type": "list",
                            "label": "File Paths",
                            "description": "List of file paths, separated by comma (,)",
                        },
                    },
                }
            }
        ]
        self.init_args = {
            "client_id" : "",
            "client_secret": None,
            "tenant_id": "consumers",
        }
        self.init_args_types = {
            "client_id": "str",
            "client_secret": "str",
            "tenant_id": "str",
        }

    def get(self) -> BaseReader:
        """
        Get reader instance

        :return: Data reader instance
        """
        from llama_index.readers.microsoft_onedrive.base import OneDriveReader
        args = self.get_args()
        return OneDriveReader(**args)

    def get_external_id(self, args: dict = None) -> str:
        """
        Get unique web content identifier

        :param args: load_data args
        :return: unique content identifier
        """
        unique = {}
        if "folder_id" in args and args.get("folder_id"):
            unique["folder_id"] = args.get("folder_id")
        if "file_ids" in args and args.get("file_ids"):
            unique["file_ids"] = args.get("file_ids")
        if "mime_types" in args and args.get("mime_types"):
            unique["mime_types"] = args.get("mime_types")
        return json.dumps(unique)

    def prepare_args(self, **kwargs) -> dict:
        """
        Prepare arguments for load_data() method

        :param kwargs: keyword arguments
        :return: args to pass to reader
        """
        args = {}
        if "folder_id" in kwargs and kwargs.get("folder_id"):
            if isinstance(kwargs.get("folder_id"), str):
                args["folder_id"] = kwargs.get("folder_id")  # folder id

        if "file_ids" in kwargs and kwargs.get("file_ids"):
            if isinstance(kwargs.get("file_ids"), list):
                args["file_ids"] = kwargs.get("file_ids")  # list of file ids
            elif isinstance(kwargs.get("file_ids"), str):
                args["file_ids"] = self.explode(kwargs.get("file_ids"))

        if "mime_types" in kwargs and kwargs.get("mime_types"):
            if isinstance(kwargs.get("mime_types"), list):
                args["mime_types"] = kwargs.get("mime_types")  # list of mime types
            elif isinstance(kwargs.get("mime_types"), str):
                args["mime_types"] = self.explode(kwargs.get("mime_types"))

        if "folder_path" in kwargs and kwargs.get("folder_path"):
            if isinstance(kwargs.get("folder_path"), str):
                args["folder_path"] = kwargs.get("folder_path")  # folder path

        if "file_paths" in kwargs and kwargs.get("file_paths"):
            if isinstance(kwargs.get("file_paths"), list):
                args["file_paths"] = kwargs.get("file_paths")  # list of file paths
            elif isinstance(kwargs.get("file_paths"), str):
                args["file_paths"] = self.explode(kwargs.get("file_paths"))
        return args
