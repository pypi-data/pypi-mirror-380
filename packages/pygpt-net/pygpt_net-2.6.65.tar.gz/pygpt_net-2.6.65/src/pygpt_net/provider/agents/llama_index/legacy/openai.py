#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.12 19:00:00                  #
# ================================================== #

from typing import Dict, Any

from pygpt_net.core.types import (
    AGENT_MODE_STEP,
    AGENT_TYPE_LLAMA,
)

from ...base import BaseAgent

class OpenAIAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super(OpenAIAgent, self).__init__(*args, **kwargs)
        self.id = "openai_legacy"
        self.type = AGENT_TYPE_LLAMA
        self.mode = AGENT_MODE_STEP
        self.name = "OpenAI"

    def get_agent(self, window, kwargs: Dict[str, Any]):
        """
        Return Agent provider instance

        :param window: window instance
        :param kwargs: keyword arguments
        :return: Agent provider instance
        """
        from llama_index.agent.openai import OpenAIAgent as Agent

        tools = kwargs.get("tools", [])
        verbose = kwargs.get("verbose", False)
        llm = kwargs.get("llm", None)
        chat_history = kwargs.get("chat_history", [])
        max_iterations = kwargs.get("max_iterations", 10)
        return Agent.from_tools(
            tools=tools,
            llm=llm,
            chat_history=chat_history,
            max_iterations=max_iterations,
            verbose=verbose,
        )
