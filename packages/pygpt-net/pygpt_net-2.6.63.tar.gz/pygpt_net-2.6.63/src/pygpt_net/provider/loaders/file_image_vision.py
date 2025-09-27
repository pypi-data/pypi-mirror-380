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
        self.id = "image_vision"
        self.name = "Image (vision)"
        self.extensions = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"]
        self.type = ["file"]
        self.init_args = {
            "use_local": False,  # use local model instead of API
            "keep_image": False,
            "local_prompt": "Question: describe what you see in this image. Answer:",
            "api_prompt": "Describe what is visible in the image, do it as accurately as possible, "
                          "including a comprehensive description of all details",
            "api_model": "gpt-4o",
            "api_tokens": 1000,
        }
        self.init_args_types = {
            "use_local": "bool",
            "keep_image": "bool",
            "local_prompt": "str",
            "api_prompt": "str",
            "api_model": "str",
            "api_tokens": "int",
        }

    def get(self) -> BaseReader:
        """
        Get reader instance

        :return: Data reader instance
        """
        from .hub.image_vision.base import ImageVisionLLMReader
        args = self.get_args()
        args["window"] = self.window  # pass window instance
        if self.window is not None:
            args["use_local"] = self.window.core.config.get("llama.hub.loaders.use_local", False)
        return ImageVisionLLMReader(**args)
