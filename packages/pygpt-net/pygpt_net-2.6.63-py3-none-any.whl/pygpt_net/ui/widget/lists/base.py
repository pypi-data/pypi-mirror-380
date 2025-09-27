#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.15 22:00:00                  #
# ================================================== #

from PySide6.QtCore import QItemSelectionModel
from PySide6.QtWidgets import QTreeView, QAbstractItemView


class BaseList(QTreeView):
    NAME = range(1)  # list of columns

    def __init__(self, window=None, id=None):
        """
        Select menu

        :param window: Window instance
        :param id: input id
        """
        super(BaseList, self).__init__(window)
        self.window = window
        self.id = id
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setIndentation(0)
        self.selection_locked = None
        self.selection = None
        self.unlocked = False
        self.clicked.connect(self.click)
        self.header().hide()
        self.v_scroll_value = 0
        self.h_scroll_value = 0

        # pending scroll values applied while updates are disabled (to avoid top flicker)
        self._pending_v_scroll_value = None
        self._pending_h_scroll_value = None

    def click(self, val):
        self.window.controller.mode.select(self.id)
        self.selection = self.selectionModel().selection()

    def lockSelection(self, selected=None, deselected=None):
        if self.selection is not None:
            self.selectionModel().select(self.selection, QItemSelectionModel.Select)

    def backup_selection(self):
        self.selection = self.selectionModel().selection()

    def restore_selection(self):
        if self.selection is not None:
            self.selectionModel().select(self.selection, QItemSelectionModel.Select)

    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return
        super(BaseList, self).mousePressEvent(event)

    def focusOutEvent(self, event):
        pass

    def selectionCommand(self, index, event=None):
        """
        Selection command
        :param index: Index
        :param event: Event
        """
        # check tmp unlock
        if self.unlocked:
            return super().selectionCommand(index, event)
        if self.selection_locked is not None and self.selection_locked():
            return QItemSelectionModel.NoUpdate
        return super().selectionCommand(index, event)

    def select_by_idx(self, idx: int):
        """
        Select item by index

        :param idx: index
        """
        if idx < 0:
            return
        model = self.model()
        if model.rowCount() > idx:
            index = model.index(idx, 0)
            prev_unlocked = self.unlocked
            self.unlocked = True
            self.selectionModel().select(
                index, QItemSelectionModel.ClearAndSelect | QItemSelectionModel.Rows
            )
            self.setCurrentIndex(index)
            self.setFocus()
            self.scrollTo(index)
            self.unlocked = prev_unlocked

    def store_scroll_position(self):
        """Store current scroll position"""
        self.v_scroll_value = self.verticalScrollBar().value()
        self.h_scroll_value = self.horizontalScrollBar().value()

    def restore_scroll_position(self):
        """Restore scroll position"""
        self.verticalScrollBar().setValue(self.v_scroll_value)
        self.horizontalScrollBar().setValue(self.h_scroll_value)

    def set_pending_v_scroll(self, value: int):
        """
        Set vertical scroll value to apply while updates are disabled.
        This prevents a visible jump to the top during model rebuild.
        """
        self._pending_v_scroll_value = int(value)

    def set_pending_h_scroll(self, value: int):
        """Optional: set horizontal pending value."""
        self._pending_h_scroll_value = int(value)

    def clear_pending_scroll(self):
        """Clear pending scroll values."""
        self._pending_v_scroll_value = None
        self._pending_h_scroll_value = None

    def apply_pending_scroll(self):
        """
        Apply pending scroll values immediately.
        IMPORTANT: Call this before re-enabling updates to avoid repaint at top.
        """
        if self._pending_v_scroll_value is not None:
            self.verticalScrollBar().setValue(self._pending_v_scroll_value)
        if self._pending_h_scroll_value is not None:
            self.horizontalScrollBar().setValue(self._pending_h_scroll_value)
        # do not clear here; let caller decide when to clear
