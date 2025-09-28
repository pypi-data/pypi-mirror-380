#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.15 23:00:00                  #
# ================================================== #

from PySide6.QtCore import Slot, QTimer

from pygpt_net.core.bridge.context import BridgeContext
from pygpt_net.plugin.base.plugin import BasePlugin
from pygpt_net.core.events import Event, KernelEvent
from pygpt_net.item.ctx import CtxItem

from .config import Config


class Plugin(BasePlugin):

    SLEEP_TIME = 1000  # 1 second

    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        self.id = "cmd_mouse_control"
        self.name = "Mouse And Keyboard"
        self.description = "Provides ability to control mouse and keyboard"
        self.prefix = "Mouse"
        self.order = 100
        self.allowed_cmds = [
            "get_mouse_position",
            "mouse_move",
            "mouse_click",
            "mouse_scroll",
            "mouse_drag",
            "get_screenshot",
            "keyboard_key",
            "keyboard_keys",
            "keyboard_type",
            "wait",
        ]
        self.use_locale = True
        self.worker = None
        self.config = Config(self)
        self.init_options()

    def init_options(self):
        """Initialize options"""
        self.config.from_defaults(self)

    def handle(self, event: Event, *args, **kwargs):
        """
        Handle dispatched event

        :param event: event object
        :param args: event args
        :param kwargs: event kwargs
        """
        name = event.name
        data = event.data
        ctx = event.ctx

        if name == Event.CMD_SYNTAX:
            self.cmd_syntax(data)

        elif name == Event.CMD_EXECUTE:
            self.cmd(
                ctx,
                data['commands'],
            )
        elif name == Event.SYSTEM_PROMPT:
            if self.cmd_exe():
                data['value'] = self.on_system_prompt(data['value'])

    def cmd_syntax(self, data: dict):
        """
        Event: CMD_SYNTAX

        :param data: event data dict
        """
        for option in self.allowed_cmds:
            if self.has_cmd(option):
                data['cmd'].append(self.get_cmd(option))  # append command

    def cmd(self, ctx: CtxItem, cmds: list):
        """
        Event: CMD_EXECUTE

        :param ctx: CtxItem
        :param cmds: commands dict
        """
        from .worker import Worker

        is_cmd = False
        my_commands = []
        for item in cmds:
            if item["cmd"] in self.allowed_cmds:
                my_commands.append(item)
                is_cmd = True

        if not is_cmd:
            return

        # set state: busy
        self.cmd_prepare(ctx, my_commands)

        try:
            worker = Worker()
            worker.from_defaults(self)
            worker.cmds = my_commands
            worker.ctx = ctx

            if not self.is_async(ctx):
                worker.run()
                return
            worker.run_async()

        except Exception as e:
            self.error(e)

    def handle_call(self, item: dict):
        """
        Handle call command
        This method is used to handle a single command call, typically from the agent

        :param item: command item to execute
        :return:
        """
        from .worker import Worker

        item["params"]["no_screenshot"] = True  # do not take screenshot for single command call
        worker = Worker()
        worker.from_defaults(self)
        worker.cmds = [item]
        worker.ctx = CtxItem()
        worker.run()  # sync

    @Slot(list, object, dict)
    def handle_finished_more(self, responses: list, ctx: CtxItem = None, extra_data: dict = None):
        """
        Handle finished responses signal

        :param responses: responses list
        :param ctx: context (CtxItem)
        :param extra_data: extra data
        """
        # dispatch response (reply) - collect all responses and make screenshot only once at the end
        with_screenshot = True
        for response in responses:
            if ("result" in response
                    and "no_screenshot" in response["result"]
                    and response["result"]["no_screenshot"]):
                with_screenshot = False
            if ctx is not None:
                ctx.results.append(response)
                ctx.reply = True
        self.handle_delayed(ctx, with_screenshot)

    @Slot(object, bool)
    def handle_delayed(self, ctx: CtxItem, with_screenshot: bool = True):
        """
        Handle delayed screenshot

        :param ctx: context (CtxItem)
        :param with_screenshot: if True then take screenshot, otherwise just dispatch context
        """
        if self.get_option_value("allow_screenshot") and with_screenshot:
            QTimer.singleShot(self.SLEEP_TIME, lambda: self.delayed_screenshot(ctx))
            return

        context = BridgeContext()
        context.ctx = ctx
        event = KernelEvent(KernelEvent.REPLY_ADD, {
            'context': context,
            'extra': {},
        })
        self.window.dispatch(event)

    def delayed_screenshot(self, ctx: CtxItem):
        """
        Delayed screenshot handler

        :param ctx: context (CtxItem)
        """
        self.window.controller.attachment.clear_silent()
        path = self.window.controller.painter.capture.screenshot(attach_cursor=True,
                                                                 silent=True)  # attach screenshot
        img_path = self.window.core.filesystem.make_local(path)
        ctx.images.append(img_path)
        context = BridgeContext()
        context.ctx = ctx
        event = KernelEvent(KernelEvent.REPLY_ADD, {
            'context': context,
            'extra': {},
        })
        self.window.dispatch(event)


    def on_system_prompt(self, prompt: str) -> str:
        """
        Event: SYSTEM_PROMPT

        :param prompt: prompt
        :return: updated prompt
        """
        if prompt is not None and prompt.strip() != "":
            prompt += "\n\n"
        return prompt + self.get_option_value("prompt")
