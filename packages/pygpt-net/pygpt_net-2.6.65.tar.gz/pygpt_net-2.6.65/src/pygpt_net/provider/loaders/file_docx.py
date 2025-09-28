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

from llama_index.core.readers.base import BaseReader

from .base import BaseLoader


class Loader(BaseLoader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "docx"
        self.name = "Word .docx documents"
        self.extensions = ["docx"]
        self.type = ["file"]

    def get(self) -> BaseReader:
        """
        Get reader instance

        :return: Data reader instance
        """
        from llama_index.readers.file.docs import DocxReader
        return DocxReader()  # no args
