#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.01 19:00:00                  #
# ================================================== #

class ConnectionContext:
    def __init__(
            self,
            stopped: callable = None,
            on_step: callable = None,
            on_stop: callable = None,
            on_error: callable = None,
            on_next: callable = None,
            on_next_ctx: callable = None,
    ):
        """
        Initialize connection context for agent operations.

        :param stopped: stop callback function to be called when stop event occurs
        :param on_step: stream step callback function to be called for each step in the process
        :param on_stop: callback function to be called when the process is stopped
        :param on_error: error callback function to be called when an error occurs
        :param on_next: next callback function to be called for the next step in the process
        :param on_next_ctx: new ctx in cycle
        """
        self.stopped = stopped
        self.on_step = on_step
        self.on_stop = on_stop
        self.on_error = on_error
        self.on_next = on_next
        self.on_next_ctx = on_next_ctx