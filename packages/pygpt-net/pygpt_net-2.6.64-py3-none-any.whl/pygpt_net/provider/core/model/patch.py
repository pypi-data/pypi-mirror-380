#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.12 00:00:00                  #
# ================================================== #

from packaging.version import parse as parse_version, Version

from pygpt_net.core.types import (
    MODE_RESEARCH,
    MODE_CHAT,
    MODE_AGENT_OPENAI,
    MODE_COMPUTER,
    MODE_EXPERT
)

# old patches moved here
from .patches.patch_before_2_6_42 import Patch as PatchBefore2_6_42

class Patch:
    def __init__(self, window=None):
        self.window = window

    def execute(self, version: Version) -> bool:
        """
        Migrate to current app version

        :param version: current app version
        :return: True if migrated
        """
        data = self.window.core.models.items
        base_data = self.window.core.models.get_base()
        from_base = self.window.core.models.from_base
        updated = False

        # get version of models config
        current = self.window.core.models.get_version()
        old = parse_version(current)

        # check if models file is older than current app version
        if old < version:

            # --------------------------------------------
            # previous patches for versions before 2.6.42
            if old < parse_version("2.6.42"):
                patcher = PatchBefore2_6_42(self.window)
                data, updated = patcher.execute(version)
            # --------------------------------------------

            # > 2.6.42 below:
            # pass

        # update file
        if updated:
            data = dict(sorted(data.items()))
            self.window.core.models.items = data
            self.window.core.models.save()

            # also patch any missing models, only if models file is older than 2.5.84
            if old < parse_version("2.5.84"):
                self.window.core.models.patch_missing()

        return updated
