#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.04 00:00:00                  #
# ================================================== #

from dataclasses import dataclass
from typing import Optional, ClassVar

from .base import BaseEvent
from ...item.ctx import CtxItem


@dataclass(slots=True)
class RealtimeEvent(BaseEvent):
    """
    Realtime events

    - RT_OUTPUT_AUDIO_DELTA - audio output chunk (with payload)
    - RT_OUTPUT_READY - audio output is ready (STREAM_BEGIN)
    - RT_OUTPUT_TEXT_DELTA - text chunk (delta)
    - RT_OUTPUT_AUDIO_END - audio output ended (STREAM_END)
    - RT_OUTPUT_TURN_END - audio output turn ended (TURN_END)
    - RT_OUTPUT_AUDIO_ERROR - audio output error (STREAM_ERROR)
    - RT_OUTPUT_AUDIO_VOLUME_CHANGED - audio output volume changed (volume level)
    """
    # static id for event family
    id: ClassVar[str] = "RealtimeEvent"

    # realtime events
    RT_OUTPUT_AUDIO_DELTA = "rt.output.audio.delta"
    RT_OUTPUT_AUDIO_END = "rt.output.audio.end"
    RT_OUTPUT_AUDIO_ERROR = "rt.output.audio.error"
    RT_OUTPUT_AUDIO_VOLUME_CHANGED = "rt.output.audio.volume.changed"
    RT_OUTPUT_AUDIO_COMMIT = "rt.output.audio.commit"
    RT_OUTPUT_READY = "rt.output.audio.ready"
    RT_OUTPUT_TEXT_DELTA = "rt.output.text.delta"
    RT_OUTPUT_TURN_END = "rt.output.turn.end"
    RT_INPUT_AUDIO_DELTA = "rt.input.audio.delta"
    RT_INPUT_AUDIO_MANUAL_START = "rt.input.audio.manual.start"
    RT_INPUT_AUDIO_MANUAL_STOP = "rt.input.audio.manual.stop"