#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.22 19:00:00                  #
# ================================================== #

from datetime import datetime
from logging import ERROR, WARNING, INFO, DEBUG
from typing import Any

from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QTextCursor

from pygpt_net.core.events import RenderEvent

from .fixtures import Fixtures


class Debug(QObject):
    def __init__(self, window=None):
        """
        Debug controller

        :param window: Window instance
        """
        super(Debug, self).__init__()
        self.window = window
        self.fixtures = Fixtures(window)
        self.is_logger = False  # logger window opened
        self.is_app_log = False  # app log window opened
        self.is_fake_stream = False  # fake stream enabled
        self.allow_level_change = False  # allow changing log level
        self._ids = None

    def update(self):
        """Update debug"""
        self.update_menu()
        self.fixtures.update()

    def update_menu(self):
        """Update debug menu"""
        for id in self.window.controller.dialogs.debug.get_ids():
            key = f"debug.{id}"
            if key not in self.window.ui.menu:
                continue
            if self.window.controller.dialogs.debug.is_active(id):
                self.window.ui.menu[key].setChecked(True)
            else:
                self.window.ui.menu[key].setChecked(False)

        if self.is_logger:
            self.window.ui.menu['debug.logger'].setChecked(True)
        else:
            self.window.ui.menu['debug.logger'].setChecked(False)

        if self.is_app_log:
            self.window.ui.menu['debug.app.log'].setChecked(True)
        else:
            self.window.ui.menu['debug.app.log'].setChecked(False)

    def toggle_menu(self):
        """Toggle debug menu"""
        state = self.window.core.config.get('debug')
        self.window.ui.menu['menu.debug'].menuAction().setVisible(state)

    def open_chrome_debug(self, url: str = "about:blank"):
        """
        Open Chrome debug URL

        :param url: debug URL
        """
        self.window.tools.get("web_browser").set_url(url)
        self.window.tools.get("web_browser").auto_open(load=False)

    def open_dev_tools(self) -> None:
        """
        Open dev tools for given PID (Web renderer only)

        :param pid: PID
        """
        meta = self.window.core.ctx.get_current_meta()
        if meta:
            node = self.window.core.ctx.output.get_current(meta)
            if node:
                node.show_devtools()

    def toggle_render(self):
        """Toggle render debug"""
        value = self.window.ui.menu['debug.render'].isChecked()
        self.window.core.config.set('debug.render', value)
        self.window.core.config.save()
        event = RenderEvent(RenderEvent.ON_THEME_CHANGE)
        self.window.dispatch(event)
        self.window.controller.ctx.refresh()

    def set_log_level(self, level: str = 'error'):
        """
        Switch logging level in runtime

        :param level: log level (debug, info, warning, error), default: error
        """
        if not self.allow_level_change:
            return

        print("[LOGGER] Changing log level to: " + level)
        debug = self.window.core.debug

        if level == 'debug':
            debug.switch_log_level(DEBUG)
            print("** DEBUG level enabled")
        elif level == 'info':
            debug.switch_log_level(INFO)
            print("** INFO level enabled")
        elif level == 'warning':
            debug.switch_log_level(WARNING)
            print("** WARNING level enabled")
        else:
            debug.switch_log_level(ERROR)
            print("** ERROR level enabled")

        self.window.ui.dialogs.app_log.update_log_level()

    def on_post_update(self, all: bool = False):
        """
        Update debug windows (only if active)

        :param all: update all debug windows
        """
        dialog = self.window.controller.dialogs.debug
        if self._ids is None:
            self._ids = dialog.get_ids()
        for id in self._ids:
            if dialog.is_active(id):
                dialog.update_worker(id)

    def post_setup(self):
        """Post setup debug"""
        self.connect_signals()

    def setup(self):
        """Setup debug"""
        current = self.window.core.debug.get_log_level()
        if current == ERROR:
            self.allow_level_change = True
        else:
            return
        # switch log level if set in config
        if self.window.core.config.has('log.level'):
            level = self.window.core.config.get('log.level')
            if level != "error":
                print("[LOGGER] Started with log level: " + self.window.core.debug.get_log_level_name())
                print("[LOGGER] Switching to: " + level)
                self.set_log_level(level)

        self.fixtures.setup()

    def connect_signals(self):
        """Connect signals"""
        # webengine debug signals
        if self.window.controller.chat.render.get_engine() == "web":
            signals = self.window.controller.chat.render.web_renderer.get_output_node().page().signals
            signals.js_message.connect(self.handle_js_message)

    @Slot(int, str, str)
    def handle_js_message(
            self,
            line_number: int,
            message: str,
            source_id: str
    ):
        """
        Handle JS message

        :param line_number: line number
        :param message: message
        :param source_id: source ID
        """
        data = f"[JS] Line {line_number}: {message}"
        self.log(data, window=True)

    @Slot(object)
    def handle_log(self, data: Any):
        """
        Handle log message

        :param data: message to log
        """
        self.log(data)

    def log(
            self,
            data: Any,
            window: bool = True
    ):
        """
        Log message to console or logger window

        :param data: text to log
        :param window: True if log to window, False if log to console
        """
        if not window:
            print(str(data))
            return

        if not self.is_logger or data is None or str(data).strip() == "":
            return

        data = datetime.now().strftime('%H:%M:%S.%f') + ': ' + str(data)
        cur = self.window.logger.textCursor()  # Move cursor to end of text
        cur.movePosition(QTextCursor.End)
        s = str(data) + "\n"
        while s:
            head, sep, s = s.partition("\n")  # Split line at LF
            cur.insertText(head)  # Insert text at cursor
            if sep:  # New line if LF
                cur.insertText("\n")
        self.window.logger.setTextCursor(cur)  # Update visible cursor

    def logger_enabled(self) -> bool:
        """
        Check if debug window is enabled

        :return: True if enabled, False otherwise
        """
        return self.is_logger

    def open_logger(self):
        """Open logger dialog"""
        self.window.ui.dialogs.open('logger', width=800, height=600)
        self.is_logger = True
        self.window.console.setFocus()  # Set focus to console input
        self.update()

    def close_logger(self):
        """Close logger dialog"""
        self.window.ui.dialogs.close('logger')
        self.is_logger = False
        self.update()

    def toggle_logger(self):
        """Toggle logger dialog"""
        if self.is_logger:
            self.close_logger()
        else:
            self.open_logger()

    def clear_logger(self):
        """Clear logger dialog"""
        self.window.logger.clear()

    def toggle(self, id: str):
        """
        Toggle debug window

        :param id: debug window to toggle
        """
        if self.window.controller.dialogs.debug.is_active(id):
            self.window.controller.dialogs.debug.hide(id)
            if id == "tabs":
                self.window.core.tabs.toggle_debug(False)
        else:
            if id == "db":
                self.window.ui.dialogs.database.viewer.update_table_view(force=True)  # update view on load
            elif id == "tabs":
                self.window.core.tabs.toggle_debug(True)
            self.window.controller.dialogs.debug.show(id)
            self.on_post_update(True)

        self.log('debug.' + id + ' toggled')

        # update menu
        self.update()

    def on_close(self, id: str):
        """
        Handle debug window close event

        :param id: debug window id
        """
        self.window.controller.dialogs.debug.active[id] = False
        self.window.controller.debug.update_menu()
        if id == "tabs":
            self.window.core.tabs.toggle_debug(False)

    def toggle_app_log(self):
        """
        Toggle app log window
        """
        id = 'app.log'
        if self.is_app_log:
            self.window.ui.dialogs.close(id)
            self.is_app_log = False
        else:
            self.window.ui.dialogs.open(id, width=800, height=600)
            self.window.ui.dialogs.app_log.reload()
            self.is_app_log = True

        self.log('debug.' + id + ' toggled')

        # update menu
        self.update()

    def reload(self):
        """Reload debug"""
        self.toggle_menu()
        self.update()
