#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.27 07:00:00                  #
# ================================================== #

from typing import Any

from PySide6.QtCore import Slot

from pygpt_net.core.types import MODE_AUDIO
from pygpt_net.plugin.base.plugin import BasePlugin
from pygpt_net.provider.audio_output.base import BaseProvider
from pygpt_net.core.events import Event
from pygpt_net.item.ctx import CtxItem

from .config import Config


class Plugin(BasePlugin):
    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        self.id = "audio_output"
        self.name = "Audio Output"
        self.type = ['audio.output']
        self.description = "Enables audio/voice output (speech synthesis)"
        self.prefix = "Audio Output"
        self.input_text = None
        self.playback = None
        self.order = 1
        self.use_locale = True
        self.output_file = "output.mp3"
        self.config = Config(self)
        self.worker = None

    def init_options(self):
        """Initialize options"""
        self.config.from_defaults(self)
        self.init_provider()

    def init_provider(self):
        """Initialize provider options"""
        providers = self.get_providers()
        for id in providers:
            providers[id].init(self)

    def get_providers(self) -> dict:
        """
        Get audio output providers

        :return: providers dict
        """
        return self.window.core.audio.get_providers("output")

    def get_provider_options(self) -> list:
        """Get provider options"""
        options = []
        providers = self.get_providers()
        for id in providers:
            options.append({id: providers[id].name})
        return options

    def init_tabs(self) -> dict:
        """
        Initialize provider tabs

        :return: dict of tabs
        """
        tabs = {}
        tabs["general"] = "General"
        providers = self.get_providers()
        for id in providers:
            tabs[id] = providers[id].name
        return tabs

    def setup_ui(self):
        """
        Setup UI
        """
        pass

    def attach(self, window):
        """
        Attach window

        :param window: Window instance
        """
        self.window = window

        # register provider tabs
        self.tabs = self.init_tabs()

        # register options
        self.init_options()

    def get_provider(self) -> BaseProvider:
        """
        Get audio output provider

        :return: provider instance
        """
        current = self.get_option_value("provider")
        providers = self.get_providers()
        if current not in providers:
            raise Exception("Provider '{}' not found!".format(current))
        return providers[current]

    def handle(self, event: Event, *args, **kwargs):
        """
        Handle dispatched event

        :param event: event object
        :param args: args
        :param kwargs: kwargs
        """
        name = event.name
        data = event.data
        ctx = event.ctx
        mode = self.window.core.config.get("mode")

        if name == Event.INPUT_BEFORE:
            self.on_input_before(data['value'])

        elif name == Event.CTX_AFTER:
            if mode == MODE_AUDIO:
                return  # skip if audio mode
            self.stop_audio()
            self.on_generate(ctx, event)

        elif name == Event.AUDIO_READ_TEXT:
            self.stop_audio()
            self.on_generate(ctx, event)

        elif name == Event.AUDIO_PLAYBACK:
            self.stop_audio()
            self.on_playback(ctx, event)

        elif name == Event.AUDIO_OUTPUT_STOP:
            self.stop_audio()

    def on_input_before(self, text: str):
        """
        Event: INPUT_BEFORE

        :param text: text to read
        """
        self.input_text = text

    def on_generate(self, ctx: CtxItem, event: Event):
        """
        Events: CTX_AFTER, AUDIO_READ_TEXT

        :param ctx: CtxItem
        :param event: Event
        """
        from .worker import Worker

        # check if provider is configured
        if not self.get_provider().is_configured():
            msg = self.get_provider().get_config_message()
            self.window.ui.dialogs.alert(msg)
            return

        name = event.name
        text = ctx.output
        cache_file = None
        if event.data is not None and isinstance(event.data, dict) and "cache_file" in event.data:
            cache_file = event.data["cache_file"]

        # check for audio read allowed. Prevents reading audio in commands, results, etc.
        if name == Event.CTX_AFTER:
            if not ctx.audio_read_allowed():
                return  # abort if audio read is not allowed (commands, results, etc.)

        # cache ctx
        cache_enabled = self.window.core.config.get("audio.cache.enabled", False)
        max_files = int(self.window.core.config.get("audio.cache.max_files", 10))
        if cache_enabled:
            # delete old if max
            if max_files > 0:
                self.window.core.audio.delete_old_cache(max_files)
            if not cache_file:
                # gen cache file path if exists
                tmp_cache_file, is_cached = self.window.core.audio.prepare_cache_path(text)
                if is_cached:
                    event = Event(Event.AUDIO_PLAYBACK, ctx=ctx)
                    event.data = {"audio_file": tmp_cache_file}
                    return self.on_playback(ctx, event)  # playback cached audio file
                else:
                    if tmp_cache_file:
                        cache_file = tmp_cache_file  # store cache file

        try:
            if text is not None and len(text) > 0:
                self.stop_audio()

                worker = Worker()
                worker.from_defaults(self)
                worker.ctx = ctx
                worker.event = name
                worker.cache_file = cache_file
                worker.text = self.window.core.audio.clean_text(text)
                worker.mode = "generate"

                # signals
                worker.signals.playback.connect(self.handle_playback)
                worker.signals.error_playback.connect(self.handle_playback_error)
                worker.signals.stop.connect(self.handle_stop)
                worker.signals.volume_changed.connect(self.handle_volume)

                # only for manual reading
                if name == Event.AUDIO_READ_TEXT:
                    self.window.controller.audio.on_begin(worker.text)

                backend = self.window.core.config.get("audio.output.backend", "native")
                if backend == "native":
                    worker.generate()
                else:
                    worker.run_async()
                self.worker = worker

        except Exception as e:
            self.error(e)

    def on_playback(self, ctx: CtxItem, event: Event):
        """
        Events: AUDIO_PLAYBACK

        :param ctx: CtxItem
        :param event: Event
        """
        from .worker import Worker

        try:
            self.stop_audio()

            worker = Worker()
            worker.from_defaults(self)
            worker.audio_file = event.data["audio_file"]
            worker.mode = "playback"

            # signals
            worker.signals.playback.connect(self.handle_playback)
            worker.signals.error_playback.connect(self.handle_playback_error)
            worker.signals.stop.connect(self.handle_stop)
            worker.signals.volume_changed.connect(self.handle_volume)

            if not self.window.controller.audio.ui.recording:
                self.window.controller.audio.on_begin("")

            backend = self.window.core.config.get("audio.output.backend", "native")
            if backend == "native":
                worker.play()
            else:
                worker.run_async()

            self.worker = worker

        except Exception as e:
            self.error(e)

    def destroy(self):
        """Destroy thread"""
        pass

    def set_status(self, status: str):
        """
        Set status

        :param status: status text
        """
        self.window.ui.plugin_addon['audio.output'].set_status(status)

    def stop_audio(self):
        """
        Event: AUDIO_OUTPUT_STOP

        Stop playing the audio
        """
        if self.worker is not None:
            self.worker.stop()
        self.window.core.audio.output.stop(signals=None)
        self.handle_volume(0.0)

    @Slot(object)
    def handle_playback_error(self, err: Any):
        """
        Send error message to logger and alert dialog

        :param err: error message
        """
        self.error(err)
        if self.window.core.platforms.is_snap():
            self.window.ui.dialogs.open(
                'snap_audio_output',
                width=400,
                height=200
            )

    @Slot(str)
    def handle_playback(self, event: str):
        """
        Handle thread playback object

        :param event: event name
        """
        self.window.controller.audio.on_play(event)

    @Slot()
    def handle_stop(self):
        """Handle thread playback stop"""
        self.stop_audio()

    @Slot(float)
    def handle_volume(self, volume: float):
        """
        Handle thread playback volume

        :param volume: volume level
        """
        self.window.controller.audio.ui.on_output_volume_change(int(volume))
