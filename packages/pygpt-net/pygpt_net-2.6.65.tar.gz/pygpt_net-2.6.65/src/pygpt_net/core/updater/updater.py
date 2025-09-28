#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.11 00:00:00                  #
# ================================================== #

import copy
import os
import shutil
import json
import ssl
import time
from typing import Tuple
import locale

from urllib.request import urlopen, Request

from PySide6.QtCore import QObject, Signal, Slot, QRunnable
from packaging.version import parse as parse_version, Version

from pygpt_net.utils import trans


class Updater:
    def __init__(self, window=None):
        """
        Updater core (config data patcher)

        :param window: Window instance
        """
        self.window = window
        self.thanks = None  # cache

    def patch(self):
        """Patch config data to current version"""
        try:
            version = self.get_app_version()

            # migrate DB
            self.migrate_db()

            self.patch_config(version)
            self.patch_models(version)
            self.patch_presets(version)
            self.patch_ctx(version)
            self.patch_indexes(version)
            self.patch_assistants(version)
            self.patch_attachments(version)
            self.patch_notepad(version)
        except Exception as e:
            self.window.core.debug.log(e)
            print("Failed to patch config data!")

    def migrate_db(self):
        """Migrate database"""
        try:
            self.window.core.db.migrate()
        except Exception as e:
            self.window.core.debug.log(e)
            print("Failed to migrate database!")

    def patch_config(self, version: Version):
        """
        Migrate config to current app version

        :param version: current app version
        """
        if self.window.core.config.patch(version):
            print("Migrated config. [OK]")

    def patch_models(self, version: Version):
        """
        Migrate models to current app version

        :param version: current app version
        """
        if self.window.core.models.patch(version):
            print("Migrated models. [OK]")

    def patch_presets(self, version: Version):
        """
        Migrate presets to current app version

        :param version: current app version
        """
        if self.window.core.presets.patch(version):
            print("Migrated presets. [OK]")

    def patch_ctx(self, version: Version):
        """
        Migrate ctx to current app version

        :param version: current app version
        """
        if self.window.core.ctx.patch(version):
            print("Migrated ctx. [OK]")

    def patch_assistants(self, version: Version):
        """
        Migrate assistants to current app version

        :param version: current app version
        """
        if self.window.core.assistants.patch(version):
            print("Migrated assistants. [OK]")

    def patch_attachments(self, version: Version):
        """
        Migrate attachments to current app version

        :param version: current app version
        """
        if self.window.core.attachments.patch(version):
            print("Migrated attachments. [OK]")

    def patch_indexes(self, version: Version):
        """
        Migrate indexes to current app version

        :param version: current app version
        """
        if self.window.core.idx.patch(version):
            print("Migrated indexes. [OK]")

    def patch_notepad(self, version: Version):
        """
        Migrate notepad to current app version

        :param version: current app version
        """
        if self.window.core.notepad.patch(version):
            print("Migrated notepad. [OK]")

    def patch_dir(
            self,
            dir_name: str = "",
            force: bool = False
    ):
        """
        Patch directory (replace all files)

        :param dir_name: directory name
        :param force: force update
        """
        try:
            # directory
            dst_dir = os.path.join(self.window.core.config.path, dir_name)
            src = os.path.join(self.window.core.config.get_app_path(), 'data', 'config', dir_name)
            for file in os.listdir(src):
                src_file = os.path.join(src, file)
                dst_file = os.path.join(dst_dir, file)
                if not os.path.exists(dst_file) or force:
                    shutil.copyfile(src_file, dst_file)
                    print("Patched file: {}.".format(dst_file))
        except Exception as e:
            self.window.core.debug.log(e)

    def patch_file(
            self,
            filename: str = "",
            force: bool = False
    ):
        """
        Patch file

        :param filename: file name
        :param force: force update
        """
        try:
            # file
            dst = os.path.join(self.window.core.config.path, filename)
            if not os.path.exists(dst) or force:
                src = os.path.join(self.window.core.config.get_app_path(), 'data', 'config', filename)
                # make backup of old file
                if os.path.exists(dst):
                    shutil.copyfile(dst, dst + '.backup')
                    print("Backup file: {}.".format(dst + '.backup'))
                shutil.copyfile(src, dst)
                print("Patched file: {}.".format(dst))
        except Exception as e:
            self.window.core.debug.log(e)

    def patch_css(
            self,
            filename: str = "",
            force: bool = False
    ):
        """
        Patch css file

        :param filename: file name
        :param force: force update
        """
        try:
            # file
            dst = os.path.join(self.window.core.config.path, 'css', filename)
            if not os.path.exists(dst) or force:
                src = os.path.join(self.window.core.config.get_app_path(), 'data', 'css', filename)
                # make backup of old file
                if os.path.exists(dst):
                    shutil.copyfile(dst, dst + '.backup')
                    print("Backup css file: {}.".format(dst + '.backup'))
                shutil.copyfile(src, dst)
                print("Patched css file: {}.".format(dst))
        except Exception as e:
            self.window.core.debug.log(e)

    def get_app_version(self) -> Version:
        """
        Get the current app version.

        :return: version (packaging.version.Version)
        """
        return parse_version(self.window.meta['version'])

    def get_updater_url(self) -> str:
        """
        Get the app updates info url.

        :return: updater url
        """
        return self.window.meta['website'] + "/api/version?v=" + str(self.window.meta['version'])

    def get_thanks(self) -> Tuple[str, str, str]:
        """
        Get contributors, donates and sponsors

        :return: people list
        """
        url = self.get_updater_url()
        self.thanks = ""
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = True
            req = Request(
                url=url,
                headers={'User-Agent': 'Mozilla/5.0'},
            )
            response = urlopen(req, context=ctx, timeout=5)
            data_json = json.loads(response.read())
            if "thanks" in data_json:
                self.thanks = self.parse_thanks(data_json["thanks"])
        except Exception as e:
            self.window.core.debug.log(e)
            print("Failed to fetch data")

        return self.thanks

    def get_fetch_thanks(self) -> Tuple[str, str, str]:
        """
        Get contributors, donates and sponsors

        :return: (contributors, donates, sponsors)
        """
        if self.thanks is None:
            return self.get_thanks()
        return self.thanks

    def check_silent(self) -> Tuple[bool, str, str, str, str, str]:
        """
        Check version in background

        :return: (is_new, newest_version, newest_build, changelog, download_windows, download_linux)
        """
        url = self.get_updater_url()
        is_new = False
        newest_version = ""
        newest_build = ""
        changelog = ""
        download_windows = ""
        download_linux = ""

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = True
            req = Request(
                url=url,
                headers={'User-Agent': 'Mozilla/5.0'},
            )
            response = urlopen(req, context=ctx, timeout=5)
            data_json = json.loads(response.read())
            newest_version = data_json["version"]
            newest_build = data_json["build"]

            # check correct version for Microsoft Store, Snap Store, etc.
            if self.window.core.platforms.is_windows():
                if self.window.core.platforms.is_ms_store():
                    if "version_windows_store" in data_json:
                        newest_version = data_json["version_windows_store"]
                    if "build_windows_store" in data_json:
                        newest_build = data_json["build_windows_store"]
                else:
                    if "version_windows" in data_json:
                        newest_version = data_json["version_windows"]
                    if "build_windows" in data_json:
                        newest_build = data_json["build_windows"]
            elif self.window.core.platforms.is_snap():
                if "version_snap" in data_json:
                    newest_version = data_json["version_snap"]
                if "build_snap" in data_json:
                    newest_build = data_json["build_snap"]

            # changelog, download links
            changelog = ""
            download_windows = ""
            download_linux = ""
            if "changelog" in data_json:
                changelog = data_json["changelog"]
            if "download_windows" in data_json:
                download_windows = data_json["download_windows"]
            if "download_linux" in data_json:
                download_linux = data_json["download_linux"]
            if "thanks" in data_json:
                self.thanks = self.parse_thanks(data_json["thanks"])

            parsed_newest_version = parse_version(newest_version)
            parsed_current_version = parse_version(self.window.meta['version'])
            if parsed_newest_version > parsed_current_version:
                is_new = parsed_newest_version > parsed_current_version

            # save last check time and version
            self.window.core.config.set("updater.check.bg.last_time", time.time())
            self.window.core.config.set("updater.check.bg.last_version", newest_version)

        except Exception as e:
            self.window.core.debug.log(e)
            print("Failed to check for updates")

        return is_new, newest_version, newest_build, changelog, download_windows, download_linux

    def parse_thanks(self, people: str) -> str:
        """
        Parse people list

        :param people: people list
        :return: parsed people list
        """
        people_list = [x.strip() for x in people.split(",")]
        sorted_people = sorted(people_list, key=locale.strxfrm)
        return ", ".join(sorted_people)

    def check(self, force: bool = False) -> bool:
        """
        Check for updates

        :param force: force show version dialog
        :return: True if force show version dialog
        """
        print("Checking for updates...")
        is_new, version, build, changelog, download_windows, download_linux = self.check_silent()
        if is_new or force:
            self.show_version_dialog(
                version,
                build,
                changelog,
                download_windows,
                download_linux,
                is_new
            )
            return True
        print("No updates available.")
        return False

    def show_version_dialog(
            self,
            version: str,
            build: str,
            changelog: str,
            download_windows: str,
            download_linux: str,
            is_new: bool = False
    ):
        """
        Display version dialog

        :param version: version number
        :param build: build date
        :param changelog: changelog
        :param download_windows: windows download link
        :param download_linux: linux download link
        :param is_new: True if is new version available
        """
        self.window.ui.dialog['update'].set_data(
            is_new,
            version,
            build,
            changelog,
            download_windows,
            download_linux
        )
        self.window.ui.dialogs.open('update', height=600)

    def post_check_config(self) -> bool:
        """
        Check for missing config keys and add them.

        :return: True if updated
        """
        base = self.window.core.config.get_base()
        data = self.window.core.config.all()
        updated = False

        # check for any missing keys
        for key in base:
            if key not in data:
                data[key] = copy.deepcopy(base[key])  # copy base value
                updated = True

        # update file
        if updated:
            data = dict(sorted(data.items()))
            self.window.core.config.data = data
            self.window.core.config.save()

        return updated

    @Slot(str, str, str, str, str)
    def handle_new_version(
            self,
            version: str,
            build: str,
            changelog: str,
            download_windows: str = "",
            download_linux: str = ""
    ):
        """
        Handle new version signal

        :param version: version number
        :param build: build date
        :param changelog: changelog
        :param download_windows: download link for windows
        :param download_linux: download link for linux
        """
        if self.window.ui.tray.is_tray:
            self.window.ui.tray.show_msg(
                trans("notify.update.title"),
                version + " (" + build + ")",
            )

        # always show dialog
        self.show_version_dialog(
            version,
            build,
            changelog,
            download_windows,
            download_linux,
            True
        )

    def run_check(self, force: bool = False):
        """
        Run check for updates in background

        :param force: force show version dialog
        """
        worker = UpdaterWorker()
        worker.window = self.window
        worker.checker = self.check_silent
        worker.force = force
        worker.signals.version_changed.connect(self.handle_new_version)
        self.window.threadpool.start(worker)


class UpdaterSignals(QObject):
    version_changed = Signal(str, str, str, str, str)


class UpdaterWorker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.signals = UpdaterSignals()
        self.args = args
        self.kwargs = kwargs
        self.last_check_time = None
        self.window = None
        self.checker = None
        self.force = False

    @Slot()
    def run(self):
        try:
            # if background check is not enabled, abort
            if not self.window.core.config.get("updater.check.bg") and not self.force:
                return

            # check
            parsed_prev_checked = None
            last_checked = self.window.core.config.get("updater.check.bg.last_version")
            if last_checked is not None and last_checked != "":
                parsed_prev_checked = parse_version(last_checked)

            if self.force:
                print("Checking for updates...")

            is_new, version, build, changelog, download_windows, download_linux = self.checker()
            if is_new:
                if self.force or (parsed_prev_checked is None or parsed_prev_checked < parse_version(version)):
                    self.signals.version_changed.emit(
                        version,
                        build,
                        changelog,
                        download_windows,
                        download_linux,
                    )
                return
            if self.force:
                print("No updates available.")

        except Exception as e:
            self.window.core.debug.log(e)
            print("Failed to check for updates")

        finally:
            self.cleanup()

    def cleanup(self):
        """Cleanup resources after worker execution."""
        sig = self.signals
        self.signals = None
        if sig is not None:
            try:
                sig.deleteLater()
            except RuntimeError:
                pass