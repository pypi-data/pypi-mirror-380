#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.17 07:00:00                  #
# ================================================== #

import os
from typing import Optional

from PySide6.QtWidgets import QApplication

from pygpt_net.core.tabs.tab import Tab
from pygpt_net.core.events import Event, BaseEvent
from pygpt_net.item.ctx import CtxItem
from pygpt_net.utils import trans

from .ui import UI


class Audio:
    def __init__(self, window=None):
        """
        Audio/voice controller

        :param window: Window instance
        """
        self.window = window
        self.ui = UI(window)
        self.input_allowed_tabs = [
            Tab.TAB_NOTEPAD,
            Tab.TAB_CHAT,
            Tab.TAB_TOOL_CALENDAR,
        ]
        self.muted = False

    def setup(self):
        """Setup controller"""
        self.update()

        # continuous input (notepad)
        if self.window.core.config.get("audio.input.continuous", False):
            self.window.ui.plugin_addon['audio.input.btn'].continuous.setChecked(True)

        # auto turn (VAD)
        if self.window.core.config.get("audio.input.auto_turn", False):
            self.window.ui.nodes['audio.auto_turn'].box.setChecked(True)

        # loop recording
        if self.window.core.config.get("audio.input.loop", False):
            self.window.ui.nodes['audio.loop'].box.setChecked(True)

    def is_muted(self) -> bool:
        """
        Check if audio output is muted

        :return: True if muted
        """
        return self.muted

    def set_muted(self, state: bool):
        """
        Set audio output muted state

        :param state: True to mute, False to unmute
        """
        self.muted = state
        if state:
            self.toggle_output_icon(False)
        else:
            self.toggle_output_icon(True)

    def execute_input_stop(self):
        """Execute input stop (from UI)"""
        self.window.dispatch(Event(Event.AUDIO_INPUT_RECORD_TOGGLE, {
            "state": False,
            "auto": True,  # do not emit manual event
        }))

    def is_recording(self) -> bool:
        """
        Check if audio input is recording

        :return: True if recording
        """
        return self.window.core.plugins.get("audio_input").is_recording()

    def toggle_auto_turn(self):
        """Toggle auto turn setting"""
        value = self.window.ui.nodes['audio.auto_turn'].box.isChecked()
        self.window.core.config.set("audio.input.auto_turn", value)
        self.window.core.config.save()

    def toggle_loop(self):
        """Toggle loop recording setting"""
        value = self.window.ui.nodes['audio.loop'].box.isChecked()
        self.window.core.config.set("audio.input.loop", value)
        self.window.core.config.save()

    def toggle_input(
            self,
            state: bool,
            btn: bool = True
    ):
        """
        Toggle audio input

        :param state: True to enable, False to disable
        :param btn: True if called from button
        """
        self.window.dispatch(
            Event(Event.AUDIO_INPUT_TOGGLE, {
                "value": state,
            })
        )

    def toggle_output(self):
        """Toggle audio output"""
        if self.window.controller.plugins.is_enabled('audio_output'):
            self.disable_output()
        else:
            self.enable_output()

    def toggle_continuous(self, state: bool):
        """
        Toggle continuous audio input

        :param state: True to enable, False to disable
        """
        if state:
            self.window.core.config.set("audio.input.continuous", True)
        else:
            self.window.core.config.set("audio.input.continuous", False)
        self.window.core.config.save()

    def on_tab_changed(self, tab: Tab):
        """
        On tab changed event

        :param tab: Tab instance (current tab)
        """
        # input button visibility
        if self.is_input_enabled():
            if tab.type in self.input_allowed_tabs:
                self.handle_audio_input(True)  # show btn
            else:
                self.handle_audio_input(False) # hide btn

    def enable_output(self):
        """Enable audio output"""
        self.toggle_output_icon(True)
        self.window.controller.plugins.enable('audio_output')
        self.window.core.config.save()
        self.update()

    def disable_output(self):
        """Disable audio output"""
        self.toggle_output_icon(False)
        self.window.controller.plugins.disable('audio_output')
        self.window.core.config.save()
        self.update()

    def enable_input(self):
        """Enable audio input"""
        self.window.controller.plugins.enable('audio_input')
        self.window.core.config.save()
        self.update()

    def disable_input(self, update: bool = True):
        """
        Disable audio input

        :param update: True to update menu and listeners
        """
        self.window.controller.plugins.disable('audio_input')
        self.window.core.config.save()
        if update:
            self.update()

    def stop_input(self):
        """Stop audio input"""
        self.window.dispatch(
            Event(Event.AUDIO_INPUT_STOP, {
                "value": True,
            }), all=True)

    def stop_output(self):
        """Stop audio output"""
        self.window.dispatch(
            Event(Event.AUDIO_OUTPUT_STOP, {
                "value": True,
            }), all=True)

    def update(self):
        """Update UI and listeners"""
        self.update_listeners()
        self.update_menu()

    def is_output_enabled(self) -> bool:
        """
        Check if any audio output is enabled

        :return: True if enabled
        """
        if self.window.controller.plugins.is_enabled('audio_output'):
            return True
        return False

    def is_input_enabled(self) -> bool:
        """
        Check if any audio input is enabled

        :return: True if enabled
        """
        if self.window.controller.plugins.is_enabled('audio_input'):
            return True
        return False

    def update_listeners(self):
        """Update audio listeners"""
        is_output = False
        if self.window.controller.plugins.is_enabled('audio_output'):
            is_output = True
        if not is_output:
            self.stop_output()

        if not self.window.controller.plugins.is_enabled('audio_input'):
            self.toggle_input(False)
            self.stop_input()
            if self.window.ui.plugin_addon['audio.input'].btn_toggle.isChecked():
                self.window.ui.plugin_addon['audio.input'].btn_toggle.setChecked(False)

    def update_menu(self):
        """Update audio menu"""
        if self.window.controller.plugins.is_enabled('audio_output'):
            self.window.ui.menu['audio.output'].setChecked(True)
        else:
            self.window.ui.menu['audio.output'].setChecked(False)

        if self.window.controller.plugins.is_enabled('audio_input'):
            self.window.ui.menu['audio.input'].setChecked(True)
        else:
            self.window.ui.menu['audio.input'].setChecked(False)

        if self.window.controller.plugins.is_enabled('voice_control'):
            self.window.ui.menu['audio.control.plugin'].setChecked(True)
        else:
            self.window.ui.menu['audio.control.plugin'].setChecked(False)

        if self.window.controller.access.voice.is_voice_control_enabled():
            self.window.ui.menu['audio.control.global'].setChecked(True)
        else:
            self.window.ui.menu['audio.control.global'].setChecked(False)

    def read_text(
            self,
            text: str,
            cache_file: Optional[str] = None
    ):
        """
        Read text using audio output plugins

        :param text: text to read
        :param cache_file: cache file to save
        """
        if text is None or text.strip() == "":
            return

        ctx = CtxItem()
        ctx.output = text
        all = True  # to all plugins (even if disabled)
        event = Event(Event.AUDIO_READ_TEXT)
        event.ctx = ctx
        event.data = {
            "text": text,
            'cache_file': cache_file,
        }
        self.window.dispatch(event, all=all)

    def play_chat_audio(self, path: str):
        """
        Play audio file (chat multimodal response)

        :param path: audio file path
        """
        if not self.is_output_enabled():
            return
        self.play_audio(path)

    def play_audio(self, path: str):
        """
        Play audio file

        :param path: audio file path
        """
        ctx = CtxItem()
        event = Event(Event.AUDIO_PLAYBACK)
        event.ctx = ctx
        event.data = {
            'audio_file': path,
        }
        self.window.dispatch(event, all=True)

    def stop_audio(self):
        """Stop audio playback"""
        ctx = CtxItem()
        event = Event(Event.AUDIO_OUTPUT_STOP)
        event.ctx = ctx
        event.data = {}
        self.window.dispatch(event, all=True)

    def play_sound(self, filename: str):
        """
        Play sound

        :param filename: sound file name
        """
        path = os.path.join(self.window.core.config.get_app_path(), "data", "audio", filename)
        if path:
            self.play_audio(path)

    def play_event(
            self,
            text: str,
            event: Optional[BaseEvent] = None
    ):
        """
        Play event (read text or play cached audio file)

        :param text: text to read
        :param event: event
        """
        use_cache = True
        # event is required to use cache
        if event is None:
            use_cache = False
        else:
            # check if cache is allowed for this event
            if self.window.core.access.voice.cache_disabled(event.name):
                use_cache = False

            # check if not disabled in config
            if not self.window.core.config.get("access.audio.use_cache"):
                use_cache = False

        if text is None or text.strip() == "":
            return

        if use_cache:
            lang = self.window.core.config.get("lang")
            cache_dir = os.path.join(self.window.core.audio.get_cache_dir(), lang)
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir, exist_ok=True)
            cache_file = os.path.join(str(cache_dir), event.name + ".wav")
            # print("Cache file: {}".format(cache_file))
            if os.path.exists(cache_file):
                # print("Using cached file: {}".format(cache_file))
                self.play_audio(cache_file)
            else:
                self.read_text(text, cache_file)
        else:
            self.read_text(text)  # without cache

    def clear_cache(self, force: bool = False):
        """
        Clear audio cache

        :param force: True to force clear
        """
        if not force:
            self.window.ui.dialogs.confirm(
                type='audio.cache.clear',
                id=0,
                msg=trans("audio.cache.clear.confirm"),
            )
            return

        cache_dir = self.window.core.audio.get_cache_dir()
        if os.path.exists(cache_dir):
            import shutil
            shutil.rmtree(cache_dir)
        self.window.ui.dialogs.alert(trans("audio.cache.clear.success"))

    def toggle_output_icon(self, state: bool):
        """
        Toggle input icon

        :param state: True to enable, False to disable
        """
        if state:
            self.window.ui.nodes['icon.audio.output'].set_icon(":/icons/volume.svg")
        else:
            self.window.ui.nodes['icon.audio.output'].set_icon(":/icons/mute.svg")

    def toggle_input_icon(self, state: bool):
        """
        Toggle input icon

        :param state: True to enable, False to disable
        """
        if state:
            self.window.ui.nodes['icon.audio.input'].set_icon(":/icons/mic.svg")
        else:
            self.window.ui.nodes['icon.audio.input'].set_icon(":/icons/mic_off.svg")

    def on_begin(self, text: str):
        """
        On audio playback init

        :param text: text to play
        """
        if text:
            self.window.update_status(trans("status.audio.start"))
        else:
            self.window.update_status("")
        QApplication.processEvents()  # process events to update UI

    def on_play(self, event: str):
        """
        On audio playback start

        :param event: event name
        """
        if event == Event.AUDIO_READ_TEXT:
            self.window.update_status("")

    def on_stop(self):
        """
        On audio playback stopped (force)
        """
        self.window.update_status(trans("status.audio.stopped"))

    def is_playing(self) -> bool:
        """
        Check if any audio is playing

        :return: True if playing
        """
        from pygame import mixer
        try:
            mixer.init()
            return mixer.get_busy()
        except Exception as e:
            pass
        return False

    def handle_audio_input(
            self,
            is_enabled: bool
    ):
        """
        Handle audio input UI

        :param is_enabled: enable/disable audio input
        """
        # get advanced audio input option
        is_advanced = False
        data = {
            'name': 'audio.input.advanced',
            'value': is_advanced,
        }
        event = Event(Event.PLUGIN_OPTION_GET, data)
        self.window.dispatch(event)
        if 'value' in event.data:
            is_advanced = event.data['value']
        if is_enabled:
            # show/hide extra options
            tab = self.window.controller.ui.tabs.get_current_tab()
            if not tab:
                return
            if tab.type == Tab.TAB_NOTEPAD:
                self.window.controller.audio.ui.on_input_continuous_enable("input")
            else:
                self.window.controller.audio.ui.on_input_continuous_disable("input")
            if is_advanced:
                self.window.controller.audio.ui.on_input_disable("input")
                self.window.ui.plugin_addon['audio.input'].setVisible(True)
            else:
                self.window.controller.audio.ui.on_input_enable("input")
                self.window.ui.plugin_addon['audio.input'].setVisible(False)  # advanced recording
            self.toggle_input_icon(True)
        else:
            self.window.controller.audio.ui.on_input_disable("input")  # simple recording
            self.window.ui.plugin_addon['audio.input'].setVisible(False)  # advanced recording
            self.toggle_input_icon(False)

    def handle_audio_output(self, is_enabled: bool):
        """
        Handle audio output UI

        :param is_enabled: enable/disable audio output
        """
        if is_enabled:
            self.toggle_output_icon(True)
            # self.window.ui.plugin_addon['audio.output'].setVisible(True)
        else:
            self.window.ui.plugin_addon['audio.output'].setVisible(False)
            self.toggle_output_icon(False)

