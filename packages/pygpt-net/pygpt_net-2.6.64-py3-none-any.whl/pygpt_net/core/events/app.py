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
from typing import Optional, Dict, Any, ClassVar

from .base import BaseEvent
from ...item.ctx import CtxItem


@dataclass(slots=True)
class AppEvent(BaseEvent):
    """Events dispatched by application"""
    # static id for event family
    id: ClassVar[str] = "AppEvent"

    APP_STARTED = "app.started"
    CAMERA_CAPTURED = "camera.captured"
    CAMERA_DISABLED = "camera.disabled"
    CAMERA_ENABLED = "camera.enabled"
    CTX_ATTACHMENTS_CLEAR = "ctx.attachments.clear"
    CTX_CREATED = "ctx.created"
    CTX_END = "ctx.end"
    CTX_SELECTED = "ctx.selected"
    INPUT_CALL = "input.call"
    INPUT_ERROR = "input.error"
    INPUT_SENT = "input.sent"
    INPUT_STOPPED = "input.stopped"
    INPUT_VOICE_LISTEN_STARTED = "input.voice.listen.started"
    INPUT_VOICE_LISTEN_STOPPED = "input.voice.listen.stopped"
    MODE_SELECTED = "mode.selected"
    MODEL_SELECTED = "model.selected"
    PRESET_SELECTED = "preset.selected"
    TAB_SELECTED = "tab.switch"
    VOICE_CONTROL_STARTED = "voice.control.started"
    VOICE_CONTROL_STOPPED = "voice.control.stopped"
    VOICE_CONTROL_SENT = "voice.control.sent"
    VOICE_CONTROL_TOGGLE = "voice.control.toggle"
    VOICE_CONTROL_UNRECOGNIZED = "voice.control.unrecognized"