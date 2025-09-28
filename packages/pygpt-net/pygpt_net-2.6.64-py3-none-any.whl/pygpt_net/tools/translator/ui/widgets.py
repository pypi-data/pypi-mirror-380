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

from PySide6.QtCore import Qt, Slot, QObject, Signal
from PySide6.QtGui import QAction, QIcon, QKeySequence, QFontMetrics
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QTextEdit, QWidget, QSplitter, QPushButton, QLabel

from pygpt_net.core.text.finder import Finder
from pygpt_net.ui.widget.option.combo import OptionCombo

from pygpt_net.ui.widget.textarea.search_input import SearchInput
from pygpt_net.utils import trans

class ToolWidget:
    def __init__(self, window=None, tool=None):
        """
        Translator widget

        :param window: Window instance
        :param tool: Tool instance
        """
        self.window = window
        self.tool = tool  # tool instance
        self.left_column = None  # left column
        self.right_column = None  # right column
        self.splitter = None  # splitter
        self.model_select = None  # model select combobox
        self.status = None  # status label
        self.tab = None  # tab
        self.loading = False  # loading flag
        self.initialized = False  # initialized flag

    def set_tab(self, tab):
        """
        Set tab

        :param tab: Tab
        """
        self.tab = tab

    def setup(self, all: bool = True) -> QVBoxLayout:
        """
        Setup widget body

        :param all: If True, setup all widgets (dialog)
        :return: QVBoxLayout
        """
        self.left_column = TextColumn(self.window, self.tool, container=self, id="left")
        self.right_column = TextColumn(self.window, self.tool, container=self, id="right")

        self.left_column.textarea.textChanged.connect(self.save_config)
        self.right_column.textarea.textChanged.connect(self.save_config)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.left_column)
        self.splitter.addWidget(self.right_column)

        option = {
            "type": "combo",
            "label": "menu.tools.translator.model",
            "use": "models",
            "value": "gpt-4o-mini",
        }
        self.model_select = OptionCombo(
            window=self.window,
            parent_id="translator",
            id="model_select",
            option=option,
        )
        self.model_select.set_keys(
            self.window.controller.config.placeholder.apply_by_id('models')
        )
        self.model_select.set_value("gpt-4o-mini")  # default model
        self.model_select.combo.currentIndexChanged.connect(self.save_config)

        model_label = QLabel(trans("translator.label.model"))
        model_layout = QHBoxLayout()
        model_layout.addWidget(model_label)
        model_layout.addWidget(self.model_select)
        model_widget = QWidget()
        model_widget.setLayout(model_layout)

        self.status = QLabel("Status: Ready")
        footer = QHBoxLayout()
        footer.addWidget(self.status)
        footer.addStretch(1)
        footer.addWidget(model_widget)
        footer.setContentsMargins(10, 5, 10, 5)

        layout = QVBoxLayout()
        layout.addWidget(self.splitter, 1)
        layout.addLayout(footer)

        self.tool.signals.load_config.connect(self.load_config)
        self.tool.signals.replace.connect(self.replace_content)
        self.tool.signals.append.connect(self.append_content)
        self.tool.signals.set_status.connect(self.set_status)
        self.tool.signals.on_load.connect(self.on_load)

        self.initialized = True  # mark as initialized
        return layout

    def on_load(self):
        """
        On dialog load (focus on left column)
        """
        if self.left_column:
            self.left_column.on_load()

    @Slot(str)
    def set_status(self, message: str):
        """
        Set status message

        :param message: Status message
        """
        if self.status:
            self.status.setText(f"{message}")

    def translate(self, id: str):
        """
        Translate content from the specified column

        :param id: Column ID (left or right)
        """
        if self.loading or not self.initialized:
            return
        src_lang = self.left_column.lang_select.get_value() if id == "left" else self.right_column.lang_select.get_value()
        dst_lang = self.right_column.lang_select.get_value() if id == "left" else self.left_column.lang_select.get_value()
        text = self.left_column.textarea.toPlainText() if id == "left" else self.right_column.textarea.toPlainText()
        model = self.model_select.get_value()
        self.tool.signals.translate.emit(id, model, text, src_lang, dst_lang)

    @Slot(dict)
    def load_config(self, config: dict):
        """
        Load configuration

        :param config: Configuration dictionary
        """
        self.loading = True
        if "model" in config:
            self.model_select.set_value(config["model"])
        if "language_left" in config:
            self.left_column.lang_select.set_value(config["language_left"])
        if "language_right" in config:
            self.right_column.lang_select.set_value(config["language_right"])
        if "content_left" in config:
            self.left_column.textarea.setPlainText(config["content_left"])
        if "content_right" in config:
            self.right_column.textarea.setPlainText(config["content_right"])
        self.loading = False

    def save_config(self):
        """
        Save configuration

        :return: Configuration dictionary
        """
        if self.loading or not self.initialized:
            return
        config = {
            "model": "",
            "language_left": "",
            "language_right": "",
            "content_left": "",
            "content_right": ""
        }
        if self.model_select:
            config["model"] = self.model_select.get_value()
        if self.left_column.lang_select:
            config["language_left"] = self.left_column.lang_select.get_value()
        if self.right_column.lang_select:
            config["language_right"] = self.right_column.lang_select.get_value()
        if self.left_column.textarea:
            config["content_left"] = self.left_column.textarea.toPlainText()
        if self.right_column.textarea:
            config["content_right"] = self.right_column.textarea.toPlainText()
        self.tool.signals.save_config.emit(config)

    @Slot(str)
    def set_content(self, content: str, id: str = None):
        """
        Set output content

        :param content: Content
        :param id: Column ID (left or right)
        """
        if id == "left":
            self.left_column.textarea.setPlainText(content)
        elif id == "right":
            self.right_column.textarea.setPlainText(content)

    @Slot(str, str)
    def replace_content(self, id: str, content: str):
        """
        Replace content in the specified column

        :param id: Column ID (left or right)
        :param content: Content to replace
        """
        if id == "left":
            self.left_column.textarea.setPlainText(content)
        elif id == "right":
            self.right_column.textarea.setPlainText(content)

    @Slot(str, str)
    def append_content(self, id: str, content: str):
        """
        Append content to the specified column

        :param id: Column ID (left or right)
        :param content: Content to append
        """
        if id == "left":
            self.left_column.textarea.append(content)
        elif id == "right":
            self.right_column.textarea.append(content)

class TextColumn(QWidget):
    def __init__(
            self,
            window=None,
            tool=None,
            container=None,
            id=None
    ):
        """
        Text column widget

        :param window: main window
        :param tool: Tool instance
        :param id: Column ID
        :param container: Container widget (optional)
        """
        super(TextColumn, self).__init__(window)
        self.id = id
        self.window = window
        self.tool = tool
        self.container = container  # parent
        self.setContentsMargins(0, 0, 0, 0)
        self.setProperty('class', 'translator-column')

        self.lang_input = SearchInput(window)  # search input for languages
        self.lang_input.setPlaceholderText(trans("translator.search.placeholder"))
        self.lang_input.on_clear = self.on_clear
        self.lang_input.on_search = self.on_search
        self.lang_input.setMinimumWidth(200)  # set max width for search input

        option = {
            "type": "combo",
            "label": "menu.tools.translator.language",
            "use": "languages",
            "value": "en",
        }
        self.lang_select = OptionCombo(
            window=self.window,
            parent_id="translator",
            id="language_select",
            option=option,
        )
        self.lang_select.combo.currentIndexChanged.connect(self.container.save_config)
        self.lang_select.set_keys(
            self.window.controller.config.placeholder.apply_by_id('languages')
        )
        self.lang_select.set_value("en") # default language
        self.lang_select.setMinimumWidth(200)
        if self.id == "left":
            self.lang_select.set_value("-") # auto-detect

        self.textarea = TextareaField(window, id=self.id)
        self.textarea.setTabChangesFocus(True)
        self.textarea.setReadOnly(False)

        lang_layout = QHBoxLayout()
        lang_layout.addWidget(self.lang_input)
        lang_layout.addWidget(self.lang_select)
        lang_layout.setContentsMargins(0, 0, 0, 0)

        lang_widget = QWidget()
        lang_widget.setLayout(lang_layout)

        label = "Translate"
        if id == "left":
            label = trans("translator.btn.left")
        elif id == "right":
            label = trans("translator.btn.right")
        self.btn_translate = QPushButton(label, self)
        self.btn_translate.setProperty('class', 'translator-button')
        self.btn_translate.clicked.connect(
            lambda: self.container.translate(self.id)
        )

        self.layout = QVBoxLayout()
        self.layout.addWidget(lang_widget, 0)
        self.layout.addWidget(self.textarea, 1)
        self.layout.addWidget(self.btn_translate)
        self.setLayout(self.layout)

    def on_load(self):
        """
        Load content from the tool
        """
        if self.textarea:
            self.textarea.setFocus()

    def on_search(self, search_text: str):
        """
        Search languages based on the input text

        :param search_text: Text to search in languages
        """
        key = self.window.core.text.find_lang_id_by_search_string(search_text)
        if key:
            self.lang_select.set_value(key)

    def on_clear(self):
        """
        Clear search input
        """
        self.lang_input.clear()
        self.on_search("")


class TextareaField(QTextEdit):
    def __init__(self, window=None, id=None):
        """
        Textarea widget

        :param window: main window
        """
        super().__init__(window)
        self.window = window
        self.id = id  # assigned in setup
        self.setReadOnly(False)
        self.setAcceptRichText(False)
        self.value = 12
        self.max_font_size = 42
        self.min_font_size = 8
        self.setProperty('class', 'translator-textarea')
        self.default_stylesheet = ""
        self.setStyleSheet(self.default_stylesheet)
        self.tab = None
        self.finder = Finder(window, self)
        self.installEventFilter(self)

        self._icon_volume = QIcon(":/icons/volume.svg")
        self._icon_save = QIcon(":/icons/save.svg")
        self._icon_search = QIcon(":/icons/search.svg")
        self._icon_clear = QIcon(":/icons/clear.svg")
        self._seq_find = QKeySequence("Ctrl+F")

        # tabulation
        metrics = QFontMetrics(self.font())
        space_width = metrics.horizontalAdvance(" ")
        self.setTabStopDistance(4 * space_width)

    def set_tab(self, tab):
        """
        Set tab

        :param tab: Tab
        """
        self.tab = tab

    def eventFilter(self, source, event):
        """
        Focus event filter

        :param source: source
        :param event: event
        """
        """
        if event.type() == event.Type.FocusIn:
            if self.tab is not None:
                col_idx = self.tab.column_idx
                self.window.controller.ui.tabs.on_column_focus(col_idx)
        """
        return super().eventFilter(source, event)

    def contextMenuEvent(self, event):
        """
        Context menu event

        :param event: Event
        """
        menu = self.createStandardContextMenu()
        cursor = self.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            # plain text
            plain_text = cursor.selection().toPlainText()

            # audio read
            action = QAction(self._icon_volume, trans('text.context_menu.audio.read'), menu)
            action.triggered.connect(self.audio_read_selection)
            menu.addAction(action)

            # copy to (without current)
            excluded = []
            if self.id == "left":
                excluded = ["translator_left"]
            elif self.id == "right":
                excluded = ["translator_right"]
            copy_to_menu = self.window.ui.context_menu.get_copy_to_menu(menu, selected_text, excluded=excluded)
            if copy_to_menu is not None:
                menu.addMenu(copy_to_menu)

            # save as (selected)
            action = QAction(self._icon_save, trans('action.save_selection_as'), menu)
            action.triggered.connect(lambda pt=plain_text: self.window.controller.chat.common.save_text(pt))
            menu.addAction(action)
        else:
            # save as (all)
            action = QAction(self._icon_save, trans('action.save_as'), menu)
            action.triggered.connect(lambda: self.window.controller.chat.common.save_text(self.toPlainText()))
            menu.addAction(action)

        action = QAction(self._icon_search, trans('text.context_menu.find'), menu)
        action.triggered.connect(self.find_open)
        action.setShortcut(self._seq_find)
        menu.addAction(action)

        action = QAction(self._icon_clear, trans('translators.menu.file.clear'), menu)
        action.triggered.connect(self.action_clear)
        menu.addAction(action)

        menu.exec_(event.globalPos())
        menu.deleteLater()

    def action_clear(self):
        """
        Clear content
        """
        if self.id == "left":
            self.window.tools.get("translator").clear_left()
        elif self.id == "right":
            self.window.tools.get("translator").clear_right()

    def audio_read_selection(self):
        """
        Read selected text (audio)
        """
        self.window.controller.audio.read_text(self.textCursor().selectedText())

    def find_open(self):
        """Open find dialog"""
        self.window.controller.finder.open(self.finder)

    def on_update(self):
        """On content update"""
        self.finder.clear()  # clear finder

    def keyPressEvent(self, e):
        """
        Key press event

        :param e: Event
        """
        if e.key() == Qt.Key_F and e.modifiers() & Qt.ControlModifier:
            self.find_open()
            return
        self.finder.clear(restore=True, to_end=False)
        super().keyPressEvent(e)

    def update_stylesheet(self, data: str):
        """
        Update stylesheet

        :param data: stylesheet CSS
        """
        combined = self.default_stylesheet + data
        if combined != self.styleSheet():
            self.setStyleSheet(combined)

    def wheelEvent(self, event):
        """
        Wheel event: set font size

        :param event: Event
        """
        if event.modifiers() & Qt.ControlModifier:
            delta = 1 if event.angleDelta().y() > 0 else -1
            new_value = max(self.min_font_size, min(self.max_font_size, self.value + delta))
            if new_value != self.value:
                self.value = new_value
                self.update_stylesheet(f"QTextEdit {{ font-size: {self.value}px }};")
            event.accept()
            return
        super().wheelEvent(event)

    def focusInEvent(self, e):
        """
        Focus in event

        :param e: focus event
        """
        self.window.controller.finder.focus_in(self.finder)
        super().focusInEvent(e)

    def focusOutEvent(self, e):
        """
        Focus out event

        :param e: focus event
        """
        super().focusOutEvent(e)
        self.window.controller.finder.focus_out(self.finder)


class ToolSignals(QObject):
    update = Signal(str)  # data
    reload = Signal(str)  # path
    load_config = Signal(dict)  # load config
    save_config = Signal(dict)  # save config
    replace = Signal(str, str)  # update column content: id, content
    append = Signal(str, str)  # append to column content: id, content
    translate = Signal(str, str, str, str, str)  # translate content: id, model, text, src_lang, dst_lang
    set_status = Signal(str)  # set status message
    on_load = Signal()  # on load (focus on right column)
