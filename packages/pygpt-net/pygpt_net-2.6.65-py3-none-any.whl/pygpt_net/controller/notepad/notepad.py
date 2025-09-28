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

from typing import Optional, Tuple

from PySide6.QtCore import QTimer
from PySide6.QtGui import QTextCursor

from pygpt_net.core.tabs.tab import Tab
from pygpt_net.item.notepad import NotepadItem
from pygpt_net.ui.widget.tabs.body import TabBody
from pygpt_net.ui.widget.textarea.notepad import NotepadWidget
from pygpt_net.utils import trans


class Notepad:
    def __init__(self, window=None):
        """
        Notepad controller

        :param window: Window instance
        """
        self.window = window
        self.opened_once = False
        self.opened_idx = set()

    def get_next_suffix(self) -> int:
        """
        Get next notepad suffix

        :return: next notepad suffix
        """
        tabs_core = self.window.core.tabs
        tabs = tabs_core.get_tabs_by_type(Tab.TAB_NOTEPAD)
        idx = tabs_core.count_by_type(Tab.TAB_NOTEPAD)
        for tab in tabs:
            title = tab.title or ""
            try:
                num = int(title.rsplit(" ", 1)[-1])
                if num > idx:
                    idx = num
            except (ValueError, IndexError):
                continue
        return idx + 1

    def is_opened(self, idx: int) -> bool:
        """
        Get next available notepad index

        :return: next available notepad index
        """
        tabs = self.window.core.tabs.get_tabs_by_type(Tab.TAB_NOTEPAD)
        return any(tab.data_id == idx for tab in tabs)

    def create(
            self,
            idx: Optional[int] = None,
            tab: Optional[Tab] = None,
    ) -> Tuple[TabBody, int, int]:
        """
        Create notepad widget

        :param idx: notepad idx
        :param tab: existing tab to use (optional)
        :return: notepad widget (TabBody)
        """
        tabs_core = self.window.core.tabs
        existing_tabs = tabs_core.get_tabs_by_type(Tab.TAB_NOTEPAD)
        used_ids = {t.data_id for t in existing_tabs}

        if idx is None:
            idx = 1
        while idx in used_ids:
            idx += 1

        suffix = self.get_next_suffix()

        data_id = idx
        widget = NotepadWidget(self.window)
        widget.id = idx
        widget.textarea.id = idx
        self.window.ui.notepad[data_id] = widget

        title = trans('output.tab.notepad') + " " + str(suffix)
        if tab:
            if not tab.title:
                tab.title = title

        child = tabs_core.from_widget(widget)
        child.on_delete = self.on_delete
        return child, idx, data_id

    def on_delete(self, body: TabBody):
        """
        On delete notepad tab

        :param body: TabBody instance
        """
        tab = body.owner
        if tab.type != Tab.TAB_NOTEPAD:
            return
        idx = tab.data_id
        if idx in self.window.ui.notepad:
            self.window.ui.notepad[idx].on_delete()
            del self.window.ui.notepad[idx]
        if idx in self.opened_idx:
            self.opened_idx.discard(idx)
        self.update()

    def load(self):
        """Load all notepads contents"""
        self.window.core.notepad.load_all()
        items = self.window.core.notepad.get_all()
        num_notepads = self.get_num_notepads()
        if len(items) == 0:
            if num_notepads > 0:
                for idx in range(1, num_notepads + 1):
                    item = NotepadItem()
                    item.idx = idx
                    items[idx] = item

        if num_notepads > 0:
            for idx, item in items.items():
                widget = self.window.ui.notepad.get(idx)
                if widget is not None:
                    widget.setText(item.content)

    def get_notepad_name(self, idx: int):
        """
        Get notepad name

        :param idx: notepad idx
        :return: notepad name
        """
        num = self.get_num_notepads()
        if num > 1:
            title = trans('text.context_menu.copy_to.notepad') + ' ' + str(idx)
        else:
            title = trans('text.context_menu.copy_to.notepad')
        item = self.window.core.notepad.get_by_id(idx)
        if item is None:
            return None
        if item.initialized and item.title is not None and len(item.title) > 0:
            title = item.title
        return title

    def save(self, idx: int):
        """
        Save notepad contents

        :param idx: notepad idx
        """
        core_notepad = self.window.core.notepad
        item = core_notepad.get_by_id(idx)
        if item is None:
            item = NotepadItem()
            item.idx = idx
            core_notepad.items[idx] = item

        widget = self.window.ui.notepad.get(idx)
        if widget is not None:
            text = widget.toPlainText()
            if item.content != text:
                item.content = text
                core_notepad.update(item)
            self.update()

    def save_all(self):
        """Save all notepads contents"""
        items = self.window.core.notepad.get_all()
        num_notepads = self.get_num_notepads()
        if num_notepads > 0:
            ui_notepad = self.window.ui.notepad
            for tab in self.window.core.tabs.get_tabs_by_type(Tab.TAB_NOTEPAD):
                idx = tab.data_id
                widget = ui_notepad.get(idx)
                if widget is None:
                    continue
                if idx in items:
                    prev_content = str(items[idx].content)
                    text = widget.toPlainText()
                    if prev_content != text:
                        items[idx].content = text
                        self.window.core.notepad.update(items[idx])
            self.update()

    def setup(self):
        """Setup all notepads"""
        self.load()

    def append_text(self, text: str, idx: int):
        """
        Append text to notepad

        :param text: text to append
        :param idx: notepad idx
        """
        widget = self.window.ui.notepad.get(idx)
        if widget is None:
            return
        dt = ""
        prev_text = widget.toPlainText()
        need_nl = prev_text.strip() != ""
        textarea = widget.textarea
        cursor = textarea.textCursor()
        cursor.movePosition(QTextCursor.End)
        to_insert = (("\n" if need_nl else "") + dt + text.strip())
        cursor.insertText(to_insert)
        textarea.setTextCursor(cursor)
        self.save(idx)

    def get_num_notepads(self) -> int:
        """
        Get number of notepads

        :return: number of notepads
        """
        return self.window.core.tabs.count_by_type(Tab.TAB_NOTEPAD)

    def get_current_active(self) -> int:
        """
        Get current notepad idx

        :return: current notepad index
        """
        tabs_ctrl = self.window.controller.ui.tabs
        if self.is_active():
            tab = tabs_ctrl.get_current_tab()
            if tab is not None:
                return tab.data_id
        return 1

    def is_active(self) -> bool:
        """
        Check if notepad tab is active

        :return: True if notepad tab is active
        """
        return self.window.controller.ui.tabs.get_current_type() == Tab.TAB_NOTEPAD

    def open(self):
        """Open notepad"""
        if self.get_num_notepads() == 0:
            return
        if self.window.controller.ui.tabs.get_current_type() != Tab.TAB_NOTEPAD:
            idx = self.window.core.tabs.get_min_idx_by_type(Tab.TAB_NOTEPAD)
            if idx is not None:
                tabs = self.window.ui.layout.get_active_tabs()
                tabs.setCurrentIndex(idx)
        self.window.activateWindow()

    def update(self):
        """Update notepads UI"""
        pass

    def reload(self):
        """Reload notepads"""
        self.window.core.notepad.locked = True
        self.window.core.notepad.reset()
        self.load()
        self.window.core.notepad.locked = False

    def switch_to_tab(self, idx: Optional[int] = None):
        """
        Switch to notepad tab

        :param idx: notepad idx
        """
        if idx is None:
            idx = self.get_first_notepad_tab_idx()
        tabs = self.window.ui.layout.get_active_tabs()
        tab = self.window.core.tabs.get_tab_by_index(idx)
        if tab is not None:
            tabs.setCurrentIndex(idx)
        else:
            tabs.setCurrentIndex(self.get_first_notepad_tab_idx())

    def get_first_notepad_tab_idx(self) -> int:
        """
        Get first notepad tab index

        :return: first notepad tab index
        """
        return self.window.core.tabs.get_min_idx_by_type(Tab.TAB_NOTEPAD)

    def get_current_notepad_text(self) -> str:
        """
        Get current notepad text

        :return: current notepad text
        """
        idx = self.get_current_active()
        widget = self.window.ui.notepad.get(idx)
        return widget.toPlainText() if widget is not None else ""

    def get_notepad_text(self, idx: int) -> str:
        """
        Get notepad text

        :param idx: notepad index
        :return: notepad text
        """
        widget = self.window.ui.notepad.get(idx)
        return widget.toPlainText() if widget is not None else ""

    def clear(self, idx: int) -> bool:
        """
        Clear notepad contents

        :param idx: notepad idx
        """
        widget = self.window.ui.notepad.get(idx)
        if widget is not None:
            widget.textarea.clear()
            self.save(idx)
            return True
        return False

    def on_open(
            self,
            tab_idx: int,
            column_idx: int = 0
    ):
        """
        On open notepad tab

        :param tab_idx: current tab idx
        :param column_idx: column idx
        """
        tab = self.window.controller.ui.tabs.get_current_tab()
        if tab is None:
            return
        if tab.type == Tab.TAB_NOTEPAD:
            idx = tab.data_id
            widget = self.window.ui.notepad.get(idx)
            if widget is None:
                return
            if idx not in self.opened_idx:
                QTimer.singleShot(0, widget.scroll_to_bottom)
            if not widget.opened:
                widget.opened = True
            if idx not in self.opened_idx:
                self.opened_idx.add(idx)

    def focus_opened(self, tab = None):
        """Focus opened notepad"""
        if tab is None:
            tab = self.window.controller.ui.tabs.get_current_tab()
        if tab is not None and tab.type == Tab.TAB_NOTEPAD:
            widget = self.window.ui.notepad.get(tab.data_id)
            if widget is not None:
                QTimer.singleShot(100, widget.textarea.setFocus)