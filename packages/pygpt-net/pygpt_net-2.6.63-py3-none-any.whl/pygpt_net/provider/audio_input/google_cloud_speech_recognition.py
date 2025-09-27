#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.06 01:00:00                  #
# ================================================== #

from .base import BaseProvider
from pygpt_net.utils import parse_args


class GoogleCloudSpeechRecognition(BaseProvider):
    def __init__(self, *args, **kwargs):
        """
        Goggle Cloud (via Speech Recognition) provider

        :param args: args
        :param kwargs: kwargs
        """
        super(GoogleCloudSpeechRecognition, self).__init__(*args, **kwargs)
        self.plugin = kwargs.get("plugin")
        self.id = "google_cloud_speech_recognition"
        self.name = "Google Cloud"

    def init_options(self):
        """Initialize options"""
        self.plugin.add_option(
            "google_cloud_args",
            type="dict",
            value=[
                {
                    "name": "language",
                    "value": "en-US",
                    "type": "str",
                }
            ],
            keys={
                'name': 'text',
                'value': 'text',
                'type': {
                    "type": "combo",
                    "use": "var_types",
                },
            },
            label="Additional keywords arguments",
            description="Additional keywords arguments for r.recognize_google_cloud(audio, **kwargs)",
            tooltip="Provide additional keywords arguments for recognize_google_cloud()",
            tab="google_cloud_speech_recognition",
            urls=["https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst"],
        )

    def transcribe(self, path: str) -> str:
        """
        Audio to text transcription

        :param path: path to audio file to transcribe
        :return: transcribed text
        """
        import speech_recognition as sr
        args = {}
        additional_args = parse_args(self.plugin.get_option_value('google_cloud_args'))
        if additional_args:
            args.update(additional_args)

        r = sr.Recognizer()
        file = sr.AudioFile(path)
        with file as source:
            audio = r.record(source)
        return r.recognize_google_cloud(audio, **args)

    def is_configured(self) -> bool:
        """
        Check if provider is configured

        :return: True if configured, False otherwise
        """
        return True

    def get_config_message(self) -> str:
        """
        Return message to display when provider is not configured

        :return: message
        """
        return ""
