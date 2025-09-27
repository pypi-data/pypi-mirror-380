#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.14 13:00:00                  #
# ================================================== #

from typing import Dict, Any

from pygpt_net.core.types import (
    AGENT_MODE_ASSISTANT,
    AGENT_TYPE_LLAMA,
)
from pygpt_net.core.bridge.context import BridgeContext

from ...base import BaseAgent


class OpenAIAssistantAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super(OpenAIAssistantAgent, self).__init__(*args, **kwargs)
        self.id = "openai_assistant"
        self.type = AGENT_TYPE_LLAMA
        self.mode = AGENT_MODE_ASSISTANT
        self.name = "OpenAI Assistant (Legacy)"

    def get_agent(self, window, kwargs: Dict[str, Any]):
        """
        Return Agent provider instance

        :param window: window instance
        :param kwargs: keyword arguments
        :return: Agent provider instance
        """
        from llama_index.agent.openai import OpenAIAssistantAgent as Agent

        context = kwargs.get("context", BridgeContext())
        preset = context.preset
        tools = kwargs.get("tools", [])
        verbose = kwargs.get("verbose", False)
        model = context.model
        system_prompt = self.get_option(preset, "base", "prompt")
        ctx = context.ctx
        thread_id = None
        assistant_id = None
        name = "Assistant"
        if (ctx is not None
                and ctx.output_name is not None
                and ctx.output_name != ""):
            name = ctx.output_name

        # get assistant_id and thread_id from ctx
        if (ctx is not None
                and ctx.meta is not None):
            if ctx.meta.assistant is not None:
                assistant_id = ctx.meta.assistant
            if ctx.meta.thread is not None:
                thread_id = ctx.meta.thread

        # get assistant_id from preset
        preset_assistant_id = self.get_option(preset, "base", "assistant_id")
        if (preset_assistant_id is not None
                and preset_assistant_id != ""):
            assistant_id = preset_assistant_id  # override assistant_id from ctx

        kwargs = {
            "tools": tools,
            "verbose": verbose,
        }
        if thread_id is not None:
            kwargs["thread_id"] = thread_id

        if assistant_id is not None:
            kwargs["assistant_id"] = assistant_id
            return Agent.from_existing(**kwargs)
        else:
            kwargs["name"] = name
            kwargs["instructions"] = system_prompt
            kwargs["openai_tools"] = [{"type": "code_interpreter"}, {"type": "file_search"}]
            kwargs["model"] = model.id
            return Agent.from_new(**kwargs)

    def get_options(self) -> Dict[str, Any]:
        """
        Return Agent options

        :return: dict of options
        """
        return {
            "base": {
                "label": "Base prompt",
                "options": {
                    "prompt": {
                        "type": "textarea",
                        "label": "Prompt",
                        "description": "Base prompt",
                        "default": "",
                    },
                }
            },
            "assistant": {
                "label": "Assistant config",
                "options": {
                    "assistant_id": {
                        "type": "text",
                        "label": "Assistant ID",
                        "description": "OpenAI Assistant ID, asst_abcd1234...",
                        "default": "",
                    },
                }
            },
        }
