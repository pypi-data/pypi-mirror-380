#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.05 01:00:00                  #
# ================================================== #

from .anthropic import ApiAnthropic
from .google import ApiGoogle
from .openai import ApiOpenAI
from .x_ai import ApiXAI

class Api:

    def __init__(self, window=None):
        """
        API wrappers

        :param window: Window instance
        """
        self.window = window
        self.anthropic = ApiAnthropic(window)
        self.google = ApiGoogle(window)
        self.openai = ApiOpenAI(window)
        self.xai = ApiXAI(window)