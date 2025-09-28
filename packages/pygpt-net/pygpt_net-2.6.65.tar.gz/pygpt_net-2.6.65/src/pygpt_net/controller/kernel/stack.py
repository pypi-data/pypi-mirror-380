#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.23 15:00:00                  #
# ================================================== #

from typing import Any

from PySide6.QtWidgets import QApplication

from pygpt_net.core.events import KernelEvent
from pygpt_net.core.bridge.context import BridgeContext
from pygpt_net.core.ctx.reply import ReplyContext


class Stack:
    def __init__(self, window=None):
        """
        Reply stack controller

        :param window: Window instance
        """
        self.window = window
        self.current = None
        self.locked = False
        self.processed = False

    def add(self, context: ReplyContext):
        """
        Add reply to stack

        :param context: ReplyContext
        """
        self.current = context
        self.unlock()
        self.processed = False

    def has(self):
        """
        Check if reply stack has any item

        :return: True if has items
        """
        return self.current is not None

    def clear(self):
        """Clear reply stack"""
        self.current = None
        self.unlock()

    def execute(self, context: ReplyContext):
        """
        Execute reply context

        :param context: ReplyContext
        """
        if context is None:
            return

        # expert call
        if context.type == ReplyContext.EXPERT_CALL:
            self.window.core.experts.call(
                context.ctx,  # master ctx
                context.parent_id,  # expert id
                context.input,  # query
            )
        # cmd execute
        elif context.type == ReplyContext.CMD_EXECUTE:
            self.window.controller.plugins.apply_cmds(
                context.ctx,  # current ctx
                context.cmds,  # commands
            )
        # cmd execute (force)
        elif context.type == ReplyContext.CMD_EXECUTE_FORCE:
            self.window.controller.plugins.apply_cmds(
                context.ctx,  # current ctx
                context.cmds,  # commands
                all=True,
            )
        # cmd execute (inline)
        elif context.type == ReplyContext.CMD_EXECUTE_INLINE:
            self.window.controller.plugins.apply_cmds_inline(
                context.ctx,  # current ctx
                context.cmds,  # commands
            )
        # agent continue
        elif context.type == ReplyContext.AGENT_CONTINUE:
            bridge_context = BridgeContext()
            bridge_context.ctx = context.ctx
            bridge_context.prompt = context.input  # from reply context
            self.window.dispatch(KernelEvent(KernelEvent.INPUT_SYSTEM, {
                'context': bridge_context,
                'extra': {
                    "force": True,
                    "internal": True,
                },
            }))

    def is_locked(self) -> bool:
        """
        Check if reply stack is locked

        :return: True if locked
        """
        return self.locked

    def lock(self):
        """Lock reply stack"""
        self.locked = True

    def unlock(self):
        """Unlock reply stack"""
        self.locked = False

    def handle(self):
        """Handle reply stack"""
        if self.window.controller.kernel.stopped():
            self.clear()
            return

        if self.waiting():
            self.lock()
            QApplication.processEvents()
            self.execute(self.current)
            self.processed = True

    def waiting(self) -> bool:
        """
        Check if reply stack is waiting for processing

        :return: True if waiting
        """
        return self.has() and not self.is_locked()

    def log(self, data: Any):
        """
        Log data to debug

        :param data: Data to log
        """
        self.window.core.debug.info(data)
