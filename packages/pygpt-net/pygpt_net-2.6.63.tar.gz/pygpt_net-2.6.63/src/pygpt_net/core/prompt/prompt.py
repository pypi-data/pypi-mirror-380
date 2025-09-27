#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.09 19:00:00                  #
# ================================================== #

from pygpt_net.core.events import Event
from pygpt_net.core.types import MODE_AGENT, MODE_EXPERT, MODE_LLAMA_INDEX
from pygpt_net.item.ctx import CtxItem
from pygpt_net.item.model import ModelItem

from .base import Base
from .custom import Custom
from .template import Template

class Prompt:
    def __init__(self, window=None):
        """
        Prompt core

        :param window: Window instance
        """
        self.window = window
        self.base = Base(window)
        self.custom = Custom(window)
        self.template = Template(window)

    def get(
            self,
            prompt: str,
            mode: str = None,
            model: ModelItem = None
    ) -> str:
        """
        Get system prompt content

        :param prompt: id of the prompt
        :param mode: mode
        :param model: model item
        :return: text content
        """
        return self.base.get(
            prompt=prompt,
            mode=mode,
            model=model,
        )

    def build_final_system_prompt(
            self,
            prompt: str,
            mode: str,
            model: ModelItem = None
    ) -> str:
        """
        Build final system prompt

        :param prompt: prompt
        :param mode: mode
        :param model: model item
        :return: final system prompt
        """
        # tmp dispatch event: system prompt
        event = Event(Event.SYSTEM_PROMPT, {
            'mode': self.window.core.config.get('mode'),
            'value': prompt,
            'silent': True,
        })
        self.window.dispatch(event)
        prompt = event.data['value']

        if (self.window.core.config.get('cmd')
                or self.window.controller.plugins.is_type_enabled("cmd.inline")):

            # abort if native func call enabled
            if self.window.core.command.is_native_enabled():
                return prompt

            # abort if model not supported
            # if not self.window.core.command.is_model_supports_tools(mode, model):
                # return prompt

            # cmd syntax tokens
            data = {
                'prompt': prompt,
                'silent': True,
                'syntax': [],
                'cmd': [],
            }

            # IMPORTANT: append command syntax only if at least one command is detected
            # tmp dispatch event: command syntax apply
            # full execute cmd syntax
            if self.window.core.config.get('cmd'):
                event = Event(Event.CMD_SYNTAX, data)
                self.window.dispatch(event)
                if event.data and "cmd" in event.data and event.data["cmd"]:
                    prompt = self.window.core.command.append_syntax(
                        data=event.data,
                        mode=mode,
                        model=model,
                    )

            # inline cmd syntax only
            elif self.window.controller.plugins.is_type_enabled("cmd.inline"):
                event = Event(Event.CMD_SYNTAX_INLINE, data)
                self.window.dispatch(event)
                if event.data and "cmd" in event.data and event.data["cmd"]:
                    prompt = self.window.core.command.append_syntax(
                        data=event.data,
                        mode=mode,
                        model=model,
                    )

        return prompt

    def prepare_sys_prompt(
            self,
            mode: str,
            model: ModelItem,
            sys_prompt: str,
            ctx: CtxItem,
            reply: bool,
            internal: bool,
            is_expert: bool = False,
    ) -> str:
        """
        Prepare system prompt

        :param mode: mode
        :param model: model item
        :param sys_prompt: system prompt
        :param ctx: context item
        :param reply: reply from plugins
        :param internal: internal call
        :param is_expert: called from expert
        :return: system prompt
        """
        # event: system prompt (append to system prompt)
        event = Event(Event.SYSTEM_PROMPT, {
            'mode': mode,
            'value': sys_prompt,
            'is_expert': is_expert,
        })
        self.window.dispatch(event)
        sys_prompt = event.data['value']

        # append personalized about
        about = self.window.core.config.get("personalize.about", "")
        modes = self.window.core.config.get("personalize.modes", "")
        if modes:
            modes_list = modes.split(',')
            if mode in modes_list:
                if about:
                    sys_prompt += f"\n\n{about}\n\n"

        # event: post prompt (post-handle system prompt)
        event = Event(Event.POST_PROMPT, {
            'mode': mode,
            'reply': reply,
            'internal': internal,
            'value': sys_prompt,
            'is_expert': is_expert,
        })
        event.ctx = ctx
        self.window.dispatch(event)
        sys_prompt = event.data['value']

        force_native_tools = False
        force_syntax_tools = False

        # always enable native tool calls from experts if agent used
        if is_expert:
            if self.window.core.config.get('experts.use_agent', False):
                force_syntax_tools = False
                force_native_tools = True

        # event: tools syntax apply (if tools enabled or inline plugin then append tools prompt)
        if self.window.core.config.get('cmd') or self.window.controller.plugins.is_type_enabled("cmd.inline"):
            if self.window.core.command.is_native_enabled(force=force_native_tools) and not force_syntax_tools:
                return sys_prompt  # abort syntax if native func calls enabled

            data = {
                'mode': mode,
                'prompt': sys_prompt,
                'syntax': [],
                'cmd': [],
                'is_expert': is_expert,
            }
            # IMPORTANT: append tools syntax only if at least one tool is detected
            # full execute cmd syntax
            if self.window.core.config.get('cmd'):
                event = Event(Event.CMD_SYNTAX, data)
                self.window.dispatch(event)
                if event.data and "cmd" in event.data and event.data["cmd"]:
                    sys_prompt = self.window.core.command.append_syntax(
                        data=event.data,
                        mode=mode,
                        model=model,
                    )

            # inline cmd syntax only
            elif self.window.controller.plugins.is_type_enabled("cmd.inline"):
                event = Event(Event.CMD_SYNTAX_INLINE, data)
                self.window.dispatch(event)
                if event.data and "cmd" in event.data and event.data["cmd"]:
                    sys_prompt = self.window.core.command.append_syntax(
                        data=event.data,
                        mode=mode,
                        model=model,
                    )

        return sys_prompt
