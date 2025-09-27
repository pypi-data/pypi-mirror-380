#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.15 23:00:00                  #
# ================================================== #

import os
import time
import uuid

from PySide6.QtCore import Slot

from pygpt_net.plugin.base.plugin import BasePlugin
from pygpt_net.core.events import Event
from pygpt_net.item.ctx import CtxItem

from .config import Config
from .docker import Docker
from .builder import Builder
from .ipython import LocalKernel
from .ipython import DockerKernel
from .output import Output
from .runner import Runner

from pygpt_net.utils import trans


class Plugin(BasePlugin):
    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        self.id = "cmd_code_interpreter"
        self.name = "Code Interpreter (v2)"
        self.description = "Provides Python/HTML/JS code execution"
        self.prefix = "Code"
        self.type = [
            'interpreter',
        ]
        self.order = 100
        self.allowed_cmds = [
            # "ipython_execute_new",
            "ipython_execute",
            "ipython_kernel_restart",
            "code_execute",
            "code_execute_file",
            "code_execute_all",
            "get_python_output",
            "get_python_input",
            "clear_python_output",
            "render_html_output",
            "get_html_output",
        ]
        self.use_locale = True
        self.docker = Docker(self)
        self.runner = Runner(self)
        self.ipython_docker = DockerKernel(self)
        self.ipython_local = LocalKernel(self)
        self.builder = Builder(self)
        self.output = Output(self)
        self.worker = None
        self.config = Config(self)
        self.init_options()

    def init_options(self):
        """Initialize options"""
        self.config.from_defaults(self)

    def make_temp_file_path(self, extension: str = "png"):
        """
        Make temporary file path for code execution

        :param extension: file extension
        :return: temporary file path
        """
        name = uuid.uuid4().hex + f".{extension}"
        dir = os.path.join(self.window.core.config.get_user_dir('data'), "tmp")
        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)
        return os.path.join(dir, name)

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
        silent = data.get("silent", False)

        if name == Event.CMD_SYNTAX:
            self.cmd_syntax(data)

        elif name == Event.CMD_EXECUTE:
            self.cmd(
                ctx,
                data['commands'],
                silent,
            )

        elif name == Event.TOOL_OUTPUT_RENDER:
            if data['tool'] == self.id:
                data['html'] = self.output.handle(ctx, data['content'])

    def cmd_syntax(self, data: dict):
        """
        Event: CMD_SYNTAX

        :param data: event data dict
        """
        # get current working directory
        legacy_data = self.window.core.config.get_user_dir('data')
        ipython_data = legacy_data

        for item in self.allowed_cmds:
            if self.has_cmd(item):
                cmd = self.get_cmd(item)
                if item in ["ipython_execute", "ipython_execute_new"]:
                    if self.get_option_value("sandbox_ipython"):
                        cmd["instruction"] += (
                            "\nIPython works in Docker container. Directory /data is the container's workdir - "
                            "directory is mapped as volume in host machine to: {}").format(ipython_data)
                    else:
                        cmd["instruction"] += (
                            "\nIPython works in local environment. Directory {} is the workdir - "
                            "use it by default to save files: {}").format(ipython_data, legacy_data)
                elif item in ["code_execute", "code_execute_file", "code_execute_all"]:
                    if self.get_option_value("sandbox_docker"):
                        cmd["instruction"] += (
                            "\nPython works in Docker container. Directory /data is the container's workdir - "
                            "directory is mapped as volume in host machine to: {}").format(legacy_data)
                    else:
                        cmd["instruction"] += (
                            "\nPython works in local environment. Directory {} is the workdir - "
                            "use it by default to save files: {}").format(legacy_data, legacy_data)
                data['cmd'].append(cmd)  # append command

    def cmd(self, ctx: CtxItem, cmds: list, silent: bool = False):
        """
        Event: CMD_EXECUTE

        :param ctx: CtxItem
        :param cmds: commands dict
        :param silent: silent mode
        """
        from .worker import Worker

        is_cmd = False
        force = False
        my_commands = []
        for item in cmds:
            if item["cmd"] in self.allowed_cmds:
                my_commands.append(item)
                is_cmd = True
                if "force" in item and item["force"]:
                    force = True  # call from tool

        if not is_cmd:
            return

        # ipython
        if self.get_option_value("sandbox_ipython"):
            ipython_commands = [
                "ipython_execute_new",
                "ipython_execute",
                "ipython_kernel_restart",
            ]
            if any(x in [x["cmd"] for x in my_commands] for x in ipython_commands):
                # check for Docker installed
                if not self.get_interpreter().is_docker_installed():
                    # snap version
                    if self.window.core.platforms.is_snap():
                        self.error(trans('ipython.docker.install.snap'))
                        self.window.update_status(trans('ipython.docker.install.snap'))
                    # other versions
                    else:
                        self.error(trans('ipython.docker.install'))
                        self.window.update_status(trans('ipython.docker.install'))
                    return
                # check if image exists
                if not self.get_interpreter().is_image():
                    self.error(trans('ipython.image.build'))
                    self.window.update_status(trans('ipython.docker.build.start'))
                    self.builder.build_image()
                    return

        # legacy python
        if self.get_option_value("sandbox_docker"):
            sandbox_commands = [
                "code_execute",
                "code_execute_all",
                "code_execute_file",
            ]
            if any(x in [x["cmd"] for x in my_commands] for x in sandbox_commands):
                # check for Docker installed
                if not self.docker.is_docker_installed():
                    # snap version
                    if self.window.core.platforms.is_snap():
                        self.error(trans('docker.install.snap'))
                        self.window.update_status(trans('docker.install.snap'))
                    # other versions
                    else:
                        self.error(trans('docker.install'))
                        self.window.update_status(trans('docker.install'))
                    return
                # check if image exists
                if not self.docker.is_image():
                    self.error(trans('docker.image.build'))
                    self.window.update_status(trans('docker.build.start'))
                    self.docker.build()
                    return

        # set state: busy
        if not silent:
            self.cmd_prepare(ctx, my_commands)

        try:
            worker = Worker()
            worker.from_defaults(self)
            worker.cmds = my_commands
            worker.ctx = ctx

            # connect signals
            worker.signals.output.connect(self.handle_interpreter_output)
            worker.signals.output_begin.connect(self.handle_interpreter_output_begin)
            worker.signals.output_end.connect(self.handle_interpreter_output_end)
            worker.signals.clear.connect(self.handle_interpreter_clear)
            worker.signals.html_output.connect(self.handle_html_output)
            worker.signals.ipython_output.connect(self.handle_ipython_output)
            self.get_interpreter().attach_signals(worker.signals)
            self.runner.attach_signals(worker.signals)

            if (not self.is_async(ctx) and not force) or ctx.async_disabled:
                worker.run()
                return
            worker.run_async()

        except Exception as e:
            self.error(e)

    @Slot(object)
    def handle_ipython_output(self, data):
        """
        Handle IPython output

        :param data: output data
        """
        if not self.get_option_value("attach_output"):
            return
        # if self.is_threaded():
        # return
        # print(data)
        cleaned_data = self.get_interpreter().remove_ansi(data)
        self.window.tools.get("interpreter").append_output(cleaned_data)
        if self.window.tools.get("interpreter").is_opened():
            self.window.update_status("")

    @Slot(object, str)
    def handle_interpreter_output(self, data, type):
        """
        Handle interpreter output

        :param data: output data
        :param type: output type
        """
        if not self.get_option_value("attach_output"):
            return
        self.window.tools.get("interpreter").append_output(data, type)

    @Slot(str)
    def handle_interpreter_output_begin(self, type: str):
        """
        Handle interpreter output begin

        :param type: output type
        """
        self.window.tools.get("interpreter").output_begin(type)

    @Slot(str)
    def handle_interpreter_output_end(self, type: str):
        """
        Handle interpreter output end

        :param type: output type
        """
        self.window.tools.get("interpreter").output_end(type)

    @Slot()
    def handle_interpreter_clear(self):
        """Handle interpreter clear"""
        self.window.tools.get("interpreter").clear_output()

    @Slot(object)
    def handle_html_output(self, data):
        """
        Handle HTML/JS canvas output

        :param data: HTML/JS code
        """
        self.window.tools.get("html_canvas").set_output(data)
        self.window.tools.get("html_canvas").auto_open()

    @Slot(str)
    def handle_python_run(self, code: str):
        """
        Handle Python code run

        :param code: Python code to execute
        """
        cmd = "code_execute"
        if self.window.tools.get("interpreter").is_ipython():
            cmd = "ipython_execute"
            if self.get_option_value("fresh_kernel"):
                self.get_interpreter().restart_kernel()
                time.sleep(1)
        self.window.tools.get("interpreter").clear_output()
        commands = [
            {
                "cmd": cmd,
                "params": {
                    "code": code,
                    "path": ".interpreter.current.py",
                },
                "silent": True,
                "force": True,
            }
        ]
        event = Event(Event.CMD_EXECUTE, {
            'commands': commands,
            'silent': True,
        })
        event.ctx = CtxItem()  # tmp
        self.handle(event)
        self.window.tools.get("interpreter").auto_open()

    def get_interpreter(self):
        """
        Get interpreter

        :return: interpreter
        """
        if self.get_option_value("sandbox_ipython"):
            return self.ipython_docker
        else:
            return self.ipython_local
