#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.18 01:00:00                  #
# ================================================== #

import json

from PySide6.QtCore import Signal, Slot

from pygpt_net.core.bridge.context import BridgeContext
from pygpt_net.core.events import Event, KernelEvent
from pygpt_net.core.worker import Worker, WorkerSignals


class Command:
    def __init__(self, window=None):
        """
        Commands dispatch controller

        :param window: Window instance
        """
        self.window = window
        self.stop = False
        self.flush_events = [
            Event.CMD_EXECUTE,
            Event.CMD_INLINE,
        ]

    def dispatch(
            self,
            event: Event,
            all: bool = False,
            execute_only: bool = False
    ):
        """
        Dispatch cmd execute event (command execution)

        :param event: event object
        :param all: True to dispatch to all plugins
        :param execute_only: True to dispatch only to plugins with execute event
        """
        self.window.core.debug.info(f"Dispatch CMD event begin: {event.name}")
        if self.window.core.debug.enabled():
            self.window.core.debug.debug(f"EVENT BEFORE: {str(event)}")

        # begin reply stack
        if event.name in self.flush_events:
            self.window.controller.kernel.replies.clear()

        for id in self.window.core.plugins.get_ids():
            force = False
            if all:
                if execute_only:
                    if event.name == Event.CMD_EXECUTE:
                        force = True
                    else:
                        force = False
                else:
                    force = True
            if self.window.controller.plugins.is_enabled(id) or force:
                if event.stop or (event.name == Event.CMD_EXECUTE and self.is_stop()):
                    if self.is_stop():
                        self.stop = False  # unlock needed here
                    break
                if self.window.core.debug.enabled():
                    self.window.core.debug.debug(f"Apply [{event.name}] to plugin: {id}")

                self.window.stateChanged.emit(self.window.STATE_BUSY)
                self.window.core.dispatcher.apply(id, event)

        # flush reply stack
        if event.name in self.flush_events:
            self.window.controller.kernel.replies.flush()

    def dispatch_only(self, event: Event):
        """
        Dispatch cmd execute event only (command execution)

        :param event: event object
        """
        self.window.core.debug.info(f"Dispatch CMD event begin: {event.name}")
        if event.name in self.flush_events:
            self.window.controller.kernel.replies.clear()
        for id in self.window.core.plugins.get_ids():
            self.window.core.dispatcher.apply(id, event)
        if event.name in self.flush_events:
            self.window.controller.kernel.replies.flush()

    def dispatch_async(self, event: Event):
        """
        Dispatch async cmd event (command execution)

        :param event: event object
        """
        worker = Worker(self.worker)
        worker.signals = WorkerSignals()
        worker.signals.finished.connect(self.handle_finished)
        worker.kwargs['event'] = event
        worker.kwargs['window'] = self.window
        worker.kwargs['finished_signal'] = worker.signals.finished
        self.window.threadpool.start(worker)

    def worker(
            self,
            event: Event,
            window,
            finished_signal: Signal
    ):
        """
        Command worker callback

        :param event: event object
        :param window: Window instance
        :param finished_signal: WorkerSignals: finished signal
        """
        for id in window.core.plugins.get_ids():
            if window.controller.plugins.is_enabled(id):
                if event.stop or (event.name == Event.CMD_EXECUTE and self.is_stop()):
                    if self.is_stop():
                        self.stop = False  # unlock needed here
                    break
                window.core.dispatcher.apply(id, event, is_async=True)
        finished_signal.emit(event)
        finished_signal.disconnect()  # disconnect signal to avoid memory leaks

    def is_stop(self) -> bool:
        """
        Check if stop is requested

        :return: True if stop is requested
        """
        return self.stop

    def handle_debug(self, data: any):
        """
        Handle thread debug log

        :param data to log
        """
        self.window.core.debug.info(data)

    @Slot(object)
    def handle_finished(self, event: Event):
        """
        Handle command execution finish (response from sync execution)

        :param event: event object
        """
        ctx = event.ctx
        if ctx is not None:
            self.window.core.debug.info("Reply...")
            if self.window.core.debug.enabled():
                self.window.core.debug.debug(f"CTX REPLY: {str(ctx)}")

            self.window.update_status("")  # Clear status
            if ctx.reply:
                data = json.dumps(ctx.results)
                if ctx.extra_ctx:
                    data = ctx.extra_ctx  # if extra content is set, use it as data to send
                prev_ctx = self.window.core.ctx.as_previous(ctx)  # copy result to previous ctx and clear current ctx

                context = BridgeContext()
                context.ctx = prev_ctx
                context.prompt = data
                extra = {
                    "force": True,
                    "internal": ctx.internal,
                }
                event = KernelEvent(KernelEvent.INPUT_SYSTEM, {
                    'context': context,
                    'extra': extra,
                })
                self.window.dispatch(event)