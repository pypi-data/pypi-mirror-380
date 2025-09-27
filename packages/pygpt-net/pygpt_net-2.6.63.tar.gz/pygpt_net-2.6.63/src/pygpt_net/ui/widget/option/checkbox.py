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

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QWidget, QLabel

from pygpt_net.ui.widget.anims.toggles import AnimToggle
from pygpt_net.utils import trans

class OptionCheckbox(QWidget):
    def __init__(
            self,
            window=None,
            parent_id: str = None,
            id: str = None,
            option: dict = None,
            icon = None
    ):
        """
        Settings checkbox

        :param window: main window
        :param id: option id
        :param parent_id: parent option id
        :param option: option data
        :param icon: icon
        """
        # TODO: https://pypi.org/project/QtAwesome/

        super(OptionCheckbox, self).__init__(window)
        self.window = window
        self.id = id
        self.parent_id = parent_id
        self.option = option
        self.value = False
        self.title = ""
        self.real_time = False

        # init from option data
        if self.option is not None:
            if "label" in self.option and self.option["label"] is not None \
                    and self.option["label"] != "":
                self.title = self.trans_or_not(self.option["label"])
            if "value" in self.option:
                self.value = self.option["value"]
            if "real_time" in self.option:
                self.real_time = self.option["real_time"]

        # self.box = QCheckBox(self.title, self.window)
        self.box = AnimToggle('', self.window)
        if self.value is not None:
            self.box.setChecked(self.value)
        self.box.stateChanged.connect(
            lambda: self.window.controller.config.checkbox.on_update(
                self.parent_id,
                self.id,
                self.option,
                self.box.isChecked()
            )
        )
        self.label = QLabel(self.title)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.box)

        # add icon if defined
        if icon is not None:
            ico = QLabel()
            pixmap = QIcon(icon).pixmap(24, 24)
            ico.setPixmap(pixmap)
            self.layout.addWidget(ico)


        self.layout.addWidget(self.label)
        self.layout.addStretch()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # self.layout = QHBoxLayout()
        #self.layout.addWidget(self.box)

        #self.setLayout(self.layout)

    def trans_or_not(self, label: str):
        """
        Translate label or return it as is if translation is not available

        :param label: Label to translate
        :return: Translated label or original if not found
        """
        txt = trans(label)
        if txt == label:
            if txt.startswith("dictionary."):
                # get only last part after the dot
                txt = txt.split('.')[-1].capitalize()
        return txt

    def setIcon(self, icon: str):
        """
        Set icon

        :param icon: icon
        """
        self.box.setIcon(icon)

    def setText(self, text: str):
        """
        Set label text

        :param text: text
        """
        self.label.setText(text)

    def setChecked(self, state: bool):
        """
        Set checkbox state

        :param state: state
        """
        self.box.setChecked(state)

    def isChecked(self) -> bool:
        """
        Get checkbox state

        :return: state
        """
        return self.box.isChecked()
