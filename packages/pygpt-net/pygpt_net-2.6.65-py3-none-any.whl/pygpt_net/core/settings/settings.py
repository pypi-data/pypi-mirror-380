#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.24 23:00:00                  #
# ================================================== #

import copy
import json
import os
import shutil
from typing import Optional, Dict, Any, List

from PySide6.QtWidgets import QApplication

from pygpt_net.core.events import RenderEvent
from pygpt_net.utils import trans


class Settings:
    def __init__(self, window=None):
        """
        Settings core

        :param window: Window instance
        """
        self.window = window

        # prepare cfg ids
        self.ids = ['settings', 'editor']
        self.active = {}
        self.options = {}
        self.sections = {}
        self.initialized = False

        # prepare active
        for id in self.ids:
            self.active[id] = False

    def get_options(self, id: Optional[str] = None) -> Dict[str, Any]:
        """
        Return options for given id

        :param id: settings id
        :return: dictionary of options
        """
        if not self.initialized:
            self.load()
        if id is None:
            return self.options
        if id in self.options:
            return self.options[id]

    def get_sections(self, id: Optional[str] = None) -> Dict[str, Any]:
        """
        Return sections for given id

        :param id: settings id
        :return: dictionary of options
        """
        if not self.initialized:
            self.load()
        if id is None:
            return self.sections
        if id in self.sections:
            return self.sections[id]

    def get_persist_options(self) -> List[str]:
        """
        Return persist options keys (options that should be persisted when loading defaults)

        :return: list of keys
        """
        if not self.initialized:
            self.load()
        persist_options = []
        for option in self.options:
            if 'persist' in self.options[option] and self.options[option]['persist']:
                persist_options.append(option)
        return persist_options

    def load(self):
        """Load settings options"""
        self.options = self.window.core.config.get_options()
        self.sections = self.window.core.config.get_sections()
        self.initialized = True

    def load_user_settings(self):
        """Load user config (from user home dir)"""
        # replace config with user base config
        self.window.core.config.load_config()

    def load_app_settings(self):
        """Load base app config (from app root dir)"""
        # persist important and non-settings values
        settings_options = self.get_options()
        persist_options = self.get_persist_options()
        all_options = self.window.core.config.all()
        persist_values = {}
        for option in all_options:
            if option in persist_options or option not in settings_options:
                persist_values[option] = copy.deepcopy(self.window.core.config.get(option))

        # save current config backup
        self.window.core.config.save('config.json.backup')

        # replace config with app base config
        self.window.core.config.from_base_config()

        # restore persisted values
        for option in persist_values:
            self.window.core.config.set(option, persist_values[option])

    def load_default_editor(self):
        """Load defaults from file"""
        file = self.window.ui.dialog['config.editor'].file
        self.load_editor(file)
        self.window.update_status(f"Restored from user file: {file}")

    def load_default_editor_app(self):
        """Load defaults from file (app)"""
        file = self.window.ui.dialog['config.editor'].file
        basename = os.path.basename(file)
        if basename.endswith(".css"):
            path = str(os.path.join(self.window.core.config.get_app_path(), "data", "css", basename))
            self.load_editor(file, path)
            self.window.update_status(f"Restored from app defaults: {basename}")
        elif basename.endswith(".json"):
            path = str(os.path.join(self.window.core.config.get_app_path(), "data", "config", basename))
            self.load_editor(file, path)
            self.window.update_status(f"Restored from app defaults: {basename}")

    def load_editor(
            self,
            file: Optional[str] = None,
            path: Optional[str] = None
    ):
        """
        Load file to editor

        :param file: file name (JSON/CSS)
        :param path: file path (force load) or None
        """
        # load file
        if path is None:
            if file.endswith('.json'):
                path = os.path.join(self.window.core.config.get_user_path(), file)
            elif file.endswith('.css'):
                path = os.path.join(self.window.core.config.get_user_path(), 'css', file)
            self.window.ui.paths['config'].setText(path)

        self.window.ui.dialog['config.editor'].file = file

        try:
            with open(path, 'r', encoding="utf-8") as f:
                txt = f.read()
                self.window.ui.editor['config'].setPlainText(txt)
        except Exception as e:
            self.window.core.debug.log(e)
            self.window.update_status(f"Error loading file: {e}")

    def save_editor(self):
        """Save file to disk"""
        file = self.window.ui.dialog['config.editor'].file
        path = None
        data = self.window.ui.editor['config'].toPlainText()

        # check if this is a valid JSON
        if file.endswith('.json'):
            try:
                json.loads(data)
            except Exception as e:
                self.window.update_status(f"This is not a valid JSON: {e}")
                self.window.ui.dialogs.alert(f"This is not a valid JSON: {e}")
                return
            path = os.path.join(self.window.core.config.get_user_path(), file)
        elif file.endswith('.css'):
            path = os.path.join(self.window.core.config.get_user_path(), 'css', file)

        if path is None:
            self.window.update_status("Error saving file: invalid file name")
            return

        # make backup of current file
        backup_file = file + '.backup'
        if file.endswith('.css'):
            backup_path = os.path.join(self.window.core.config.get_user_path(), "css", backup_file)
        else:
            backup_path = os.path.join(self.window.core.config.get_user_path(), backup_file)
        if os.path.isfile(path):
            shutil.copyfile(path, backup_path)
            self.window.update_status(f"Created backup file: {backup_file}")

        prev_content = None
        if os.path.isfile(path):
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    prev_content = f.read()
            except Exception as e:
                pass

        # save changes to current file
        try:
            with open(path, 'w', encoding="utf-8") as f:
                f.write(data)
            self.window.update_status(f"Saved file: {path}")
        except Exception as e:
            self.window.core.debug.log(e)
            self.window.update_status(f"Error saving file: {path}")
            return  # abort if error

        if prev_content == data:
            self.window.update_status(f"Saved file: {path}")
            self.window.ui.dialogs.alert(f"Saved file: {path}")
            return  # no changes made, no need to reload

        if file in ("config.json", "models.json") or file.endswith('.css'):
            self.window.update_status(trans("status.reloading"))

        QApplication.processEvents() # process events to update UI

        try:
            if file == "config.json":
                self.window.core.config.load_config()  # reload config
            elif file == "models.json":
                self.window.core.models.load()  # reload models
            elif file.endswith('.css'):
                self.window.dispatch(RenderEvent(RenderEvent.ON_THEME_CHANGE))
                self.window.controller.theme.reload(force=True)  # reload theme
            self.window.update_status(f"Saved file: {path}")
            self.window.ui.dialogs.alert(f"Saved file: {path}")
        except Exception as e:
            self.window.core.debug.log(e)
            self.window.update_status(f"Error reloading saved file: {path}")


