#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.05 00:00:00                  #
# ================================================== #

from PySide6.QtCore import QObject, Signal, Slot
from pygpt_net.core.worker import Worker
from pygpt_net.item.ctx import CtxItem


class WorkerSignals(QObject):
    updated = Signal(int, object, str)


class Summarizer:
    def __init__(self, window=None):
        """
        Summarize  controller

        :param window: Window instance
        """
        self.window = window
        self.worker = None

    def summarize(
            self,
            id: int,
            ctx: CtxItem
    ):
        """
        Summarize context

        :param id: CtxMeta ID
        :param ctx: CtxItem
        """
        # make copy of ctx
        ctx_copy = CtxItem()
        ctx_copy.from_dict(ctx.to_dict())
        self.start_worker(id, ctx_copy)

    def summarizer(
            self,
            id: int,
            ctx: CtxItem,
            window,
            updated_signal: Signal
    ):
        """
        Summarize worker callback

        :param id: CtxMeta ID
        :param ctx: CtxItem
        :param window: Window instance
        :param updated_signal: WorkerSignals: updated signal
        """
        title = window.core.api.openai.summarizer.summary_ctx(ctx)
        if title:
            updated_signal.emit(id, ctx, title)
            updated_signal.disconnect()

    def start_worker(
            self,
            id: int,
            ctx: CtxItem
    ):
        """
        Handle worker thread

        :param id: CtxMeta ID
        :param ctx: CtxItem
        """
        self.worker = Worker(self.summarizer)
        self.worker.signals = WorkerSignals()
        self.worker.signals.updated.connect(self.handle_update)
        self.worker.kwargs['id'] = id
        self.worker.kwargs['ctx'] = ctx
        self.worker.kwargs['window'] = self.window
        self.worker.kwargs['updated_signal'] = self.worker.signals.updated
        self.window.threadpool.start(self.worker)

    @Slot(int, object, str)
    def handle_update(
            self,
            id: int,
            ctx: CtxItem,
            title: str
    ):
        """
        Handle update signal (make update)

        :param id: CtxMeta ID
        :param ctx: CtxItem
        :param title: CtxMeta title
        """
        refresh = True
        # prevent UI list selection loose after later update
        if ctx.internal or len(ctx.cmds) > 0:
            refresh = False
        self.window.controller.ctx.update_name(
            id,
            title,
            refresh=refresh,
        )
        self.window.controller.chat.common.focus_input()  # restore focus
        self.worker = None

