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
        self.id = "google_docs"
        self.name = "Google Docs"
        self.type = ["web"]
        self.instructions = [
            {
                "google_docs": {
                    "description": "read and index files from Google Docs",
                    "args": {
                        "document_ids": {
                            "type": "list",
                            "label": "Document IDs",
                            "description": "List of document IDs to index, separated by comma (,)",
                            "required": True,
                        },
                    },
                }
            }
        ]
        self.init_args = {
            "credentials_path": "credentials.json",
            "token_path": "token.json",
        }
        self.init_args_types = {
            "credentials_path": "str",
            "token_path": "str",
        }

    def get(self) -> BaseReader:
        """
        Get reader instance

        :return: Data reader instance
        """
        from .hub.google.docs import GoogleDocsReader
        args = self.get_args()
        return GoogleDocsReader(**args)

    def get_external_id(self, args: dict = None) -> str:
        """
        Get unique web content identifier

        :param args: load_data args
        :return: unique content identifier
        """
        unique = {}
        if "document_ids" in args and args.get("document_ids"):
            unique["document_ids"] = args.get("document_ids")
        return json.dumps(unique)

    def prepare_args(self, **kwargs) -> dict:
        """
        Prepare arguments for load_data() method

        :param kwargs: keyword arguments
        :return: args to pass to reader
        """
        args = {}
        if "document_ids" in kwargs and kwargs.get("document_ids"):
            if isinstance(kwargs.get("document_ids"), list):
                args["document_ids"] = kwargs.get("document_ids")  # list of document ids
            elif isinstance(kwargs.get("document_ids"), str):
                args["document_ids"] = self.explode(kwargs.get("document_ids"))
        return args
