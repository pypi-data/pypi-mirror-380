#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.16 22:00:00                  #
# ================================================== #

from .access import Access
from .agent import Agent
from .assistant import Assistant
from .attachment import Attachment
from .audio import Audio
from .calendar import Calendar
from .camera import Camera
from .chat import Chat
from .command import Command
from .config import Config
from .ctx import Ctx
from .debug import Debug
from .dialogs import Dialogs
from .files import Files
from .finder import Finder
from .idx import Idx
from .kernel import Kernel
from .lang import Lang
from .launcher import Launcher
from .layout import Layout
from .media import Media
from .mode import Mode
from .model import Model
from .notepad import Notepad
from .painter import Painter
from .plugins import Plugins
from .realtime import Realtime
from .presets import Presets
from .settings import Settings
from .theme import Theme
from .tools import Tools
from .ui import UI

from pygpt_net.utils import trans, mem_clean


class Controller:
    def __init__(self, window=None):
        """
        Main controller

        :param window: Window instance
        """
        self.window = window
        self.access = Access(window)
        self.agent = Agent(window)
        self.assistant = Assistant(window)
        self.attachment = Attachment(window)
        self.audio = Audio(window)
        self.calendar = Calendar(window)
        self.camera = Camera(window)
        self.chat = Chat(window)
        self.command = Command(window)
        self.config = Config(window)
        self.ctx = Ctx(window)
        self.debug = Debug(window)
        self.dialogs = Dialogs(window)
        self.files = Files(window)
        self.finder = Finder(window)
        self.idx = Idx(window)
        self.kernel = Kernel(window)
        self.lang = Lang(window)
        self.launcher = Launcher(window)
        self.layout = Layout(window)
        self.media = Media(window)
        self.mode = Mode(window)
        self.model = Model(window)
        self.notepad = Notepad(window)
        self.painter = Painter(window)
        self.plugins = Plugins(window)
        self.presets = Presets(window)
        self.realtime = Realtime(window)
        self.settings = Settings(window)
        self.theme = Theme(window)
        self.tools = Tools(window)
        self.ui = UI(window)
        self.reloading = False

    def setup(self):
        """Setup controller"""
        self.debug.setup()  # prepare log level
        self.kernel.init()
        self.chat.init()

        # setup layout
        self.layout.setup()
        self.ui.setup()
        self.ui.tabs.setup()

        # setup controllers
        self.lang.setup()
        self.assistant.setup()
        self.chat.setup()
        self.agent.setup()
        self.tools.setup()
        self.ctx.setup()
        self.presets.setup()
        self.idx.setup()
        self.ui.update_tokens()
        self.dialogs.setup()
        self.audio.setup()
        self.attachment.setup()
        self.camera.setup_ui()
        self.access.setup()
        self.realtime.setup()
        self.media.setup()

    def post_setup(self):
        """Post-setup, after plugins are loaded"""
        self.settings.setup()
        self.plugins.settings.setup()
        self.model.editor.setup()
        self.launcher.post_setup()
        self.calendar.setup()  # after everything is loaded
        self.painter.setup()  # load previous image if exists
        self.debug.post_setup()  # post setup debug after all loaded
        self.ui.tabs.restore_data()  # restore opened tabs data

        # show license terms dialog
        if not self.window.core.config.get('license.accepted'):
            self.dialogs.info.toggle(
                'license',
                width=500,
                height=480,
            )
            self.window.ui.dialog['info.license'].setFocus()

    def after_setup(self):
        """After-setup, after all loaded"""
        self.plugins.update()

    def on_update(self):
        """On app main loop update"""
        pass

    def init(self):
        """Init base settings"""
        self.settings.load()

    def reload(self):
        """Reload components"""
        self.reloading = True  # lock
        self.presets.lock()

        print(trans("status.reloading.profile.begin"))

        try:
            self.ui.tabs.locked = True  # lock tabs
            self.window.core.reload()  # db, config, patch, etc.
            self.ui.tabs.reload()
            self.ctx.reload()
            self.ui.tabs.locked = False  # unlock tabs

            self.settings.reload()
            self.assistant.reload()
            self.attachment.reload()
            self.window.core.agents.custom.reload()
            self.presets.reload()
            self.idx.reload()
            self.agent.reload()
            self.calendar.reload()
            self.plugins.reload()
            self.painter.reload()
            self.notepad.reload()
            self.files.reload()
            self.lang.reload()
            self.debug.reload()
            self.chat.reload()
            self.media.reload()
            self.window.tools.on_reload()
            self.access.reload()
            self.tools.reload()

            # post-reload
            self.ui.tabs.reload_after()
            self.ctx.reload_after()
            self.kernel.restart()
            self.theme.reload_all()  # do not reload theme if no change

        except Exception as e:
            self.window.core.debug.log(e)

        self.reloading = False  # unlock
        self.presets.unlock()

        try:
            mem_clean(force=True)  # try to clean memory
        except Exception:
            pass

        print(trans("status.reloading.profile.end"))
