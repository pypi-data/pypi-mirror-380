#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.25 18:00:00                  #
# ================================================== #

import platform
import os
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtSvg import QSvgRenderer

from pygpt_net.config import Config


class Platforms:

    def __init__(self, window=None):
        """
        Platform core

        :param window: Window instance
        """
        self.window = window

    @staticmethod
    def prepare():
        """Pre-initialize application"""
        dpi_scaling = True
        dpi_factor = '1'

        try:
            config = Config()
            config.load_config(False)
            if config.has('layout.dpi.scaling'):
                dpi_scaling = config.get('layout.dpi.scaling')
            if config.has('layout.dpi.factor'):
                dpi_factor = str(config.get('layout.dpi.factor'))
        except Exception as e:
            pass

        os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = dpi_factor
        os.environ['QT_SCALE_FACTOR'] = dpi_factor

        if not dpi_scaling:
            if hasattr(QtCore.Qt, 'AA_DisableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling, True)
            if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, False)
        else:
            if hasattr(QtCore.Qt, 'AA_DisableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling, False)
            if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    def init(self):
        """Initialize platform"""
        pass

    def get_os(self) -> str:
        """
        Return OS name

        :return: OS name
        """
        return platform.system()

    def get_architecture(self) -> str:
        """
        Return platform architecture

        :return: platform architecture
        """
        return platform.machine()

    def is_linux(self) -> bool:
        """
        Return True if OS is Linux

        :return: True if OS is Linux
        """
        return self.get_os() == 'Linux' or sys.platform.startswith("linux")

    def is_mac(self) -> bool:
        """
        Return True if OS is MacOS

        :return: True if OS is MacOS
        """
        return self.get_os() == 'Darwin' or sys.platform == "darwin"

    def is_windows(self) -> bool:
        """
        Return True if OS is Windows

        :return: True if OS is Windows
        """
        return self.get_os() == 'Windows' or sys.platform.startswith("win")

    def is_snap(self) -> bool:
        """
        Return True if app is running as snap

        :return: True if app is running as snap
        """
        return "SNAP" in os.environ \
               and "SNAP_NAME" in os.environ \
               and os.environ["SNAP_NAME"] == Config.SNAP_NAME

    def is_ms_store(self) -> bool:
        """
        Return True if app is running as Microsoft Store app

        :return: True if app is running as Microsoft Store app
        """
        path = os.path.join(self.window.core.config.get_app_path(), '.ms_store')
        if os.path.exists(path):
            return True
        return False

    def get_as_string(self, env_suffix: bool = True) -> str:
        """
        Return platform as string

        :param env_suffix: include environment suffix
        :return: platform as string
        """
        if env_suffix:
            return self.get_os() + ', ' + self.get_architecture() + self.get_env_suffix()
        return self.get_os() + ', ' + self.get_architecture()

    def get_env_suffix(self) -> str:
        """
        Return platform suffix as string

        :return: platform as string
        """
        suffix = ''
        if self.is_snap():
            suffix = ' (snap)'
        elif self.window.core.config.is_compiled():
            suffix = ' (standalone)'
            if self.is_windows():
                if not self.is_ms_store():
                    suffix = ' (standalone)'
                else:
                    suffix = ' (MS Store)'
        return suffix

    def is_svg_supported(self) -> bool:
        """Check if SVG is supported"""
        try:
            data = """
            <svg height="100" width="100">
              <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
            </svg>
            """
            renderer = QSvgRenderer(data.encode('utf-8'))
            return renderer.isValid()
        except Exception as e:
            return False
