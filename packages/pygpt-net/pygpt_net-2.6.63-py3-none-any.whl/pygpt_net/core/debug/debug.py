#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.12 20:00:00                  #
# ================================================== #

import gc
import os
import sys
import threading
import time
import traceback
import logging

from pathlib import Path
from typing import Any, Tuple

import psutil
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication

from pygpt_net.config import Config
from pygpt_net.core.types.console import Color

from .console import Console

class Debug:
    def __init__(self, window=None):
        """
        Debug core

        :param window: Window instance
        """
        self.window = window
        self.console = Console(window)
        self.pause_idx = 1
        self._process = psutil.Process(os.getpid())

    @staticmethod
    def init(level: int = logging.ERROR):
        """
        Initialize logger and error handler

        :param level: log level (default: ERROR)
        """
        workdir = Config.prepare_workdir()
        Path(workdir).mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=str(Path(workdir) / 'app.log'),
            filemode='a',
            encoding='utf-8',
        )

        def handle_exception(exc_type, value, tb):
            """
            Handle uncaught exception

            :param exc_type: exception type
            :param value: exception value
            :param tb: traceback
            """
            logger = logging.getLogger()
            if not getattr(handle_exception, "_handling", False):
                handle_exception._handling = True
                try:
                    logger.error("Uncaught exception:", exc_info=(exc_type, value, tb))
                    traceback.print_exception(exc_type, value, tb)
                finally:
                    handle_exception._handling = False
            else:
                traceback.print_exception(exc_type, value, tb)

        sys.excepthook = handle_exception

    def update_logger_path(self):
        """Update log file path"""
        path = os.path.join(Config.prepare_workdir(), 'app.log')
        level = self.get_log_level()
        logger = logging.getLogger()
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
            handler.close()
        file_handler = logging.FileHandler(filename=str(Path(path)), mode='a', encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.setLevel(level)
        logger.addHandler(file_handler)

    def switch_log_level(self, level: int):
        """
        Set log level

        :param level: log level
        """
        logging.getLogger().setLevel(level)

    def get_log_level(self) -> int:
        """
        Get log level

        :return: log level
        """
        return logging.getLogger().getEffectiveLevel()

    def get_log_level_name(self) -> str:
        """
        Get current log level name

        :return: log level name
        """
        return self.get_log_level_name_by_id(
            self.get_log_level()
        )

    def get_log_level_name_by_id(self, id: int) -> str:
        """
        Get log level name by id

        :param id: log level id
        :return: log level name
        """
        mapping = {
            logging.ERROR: "error",
            logging.WARNING: "warning",
            logging.INFO: "info",
            logging.DEBUG: "debug",
        }
        return mapping.get(id, "unknown")

    def info(self, message: Any = None, console: bool = True):
        """
        Handle info message

        :param message: message to log
        :param console: print to console

        """
        self.log(
            message,
            logging.INFO,
            console=console,
        )

    def debug(self, message: Any = None, console: bool = True):
        """
        Handle debug message

        :param message: message to log
        :param console: print to console
        """
        self.log(
            message,
            logging.DEBUG,
            console=console,
        )

    def warning(self, message: Any = None, console: bool = True):
        """
        Handle warning message

        :param message: message to log
        :param console: print to console
        """
        self.log(
            message,
            logging.WARNING,
            console=console,
        )

    def error(self, message: Any = None, console: bool = True):
        """
        Handle error message

        :param message: message to log
        :param console: print to console
        """
        self.log(
            message,
            logging.ERROR,
            console=console,
        )

    def log(self, message: Any = None, level: int = logging.ERROR, console: bool = True):
        """
        Handle logger message (by level), default level is ERROR

        :param message: message to log
        :param level: logging level (default: ERROR)
        :param console: print to console if True
        """
        if message is None:
            return

        logger = logging.getLogger()
        enabled = self.has_level(level)

        try:
            if isinstance(message, str):
                if enabled:
                    logger.log(level, message)
                    if console:
                        print(message)
            elif isinstance(message, Exception):
                is_sys, data = self.parse_exception(message)
                msg = f"Exception: {message}"
                if not is_sys:
                    msg += f"\n{data}"
                logger.log(level, msg, exc_info=is_sys)
                if enabled and console and data:
                    print(data)
            else:
                if enabled:
                    logger.log(level, message)
                    if console:
                        print(message)
        except Exception:
            pass

        try:
            if enabled and self.window is not None:
                t = threading.current_thread()
                thread_suffix = "" if t is threading.main_thread() else f" [THREAD: {t.ident}]"
                self.window.logger_message.emit(str(message) + thread_suffix)
        except Exception:
            pass

    def parse_exception(self, e: Any = None, limit: int = 4) -> Tuple[bool, str]:
        """
        Parse exception traceback

        :param e: exception
        :param limit: limit of traceback
        :return: sys error, parsed exception as string
        """
        is_sys = False
        type_name = ""
        etype, value, tb = sys.exc_info()
        if etype is None and e is not None:
            tb = e.__traceback__
            type_name = type(e).__name__
            value = str(e)
        else:
            if etype is not None:
                is_sys = True
                type_name = etype.__name__

        traceback_details = traceback.extract_tb(tb)
        if len(traceback_details) >= limit:
            last_calls = traceback_details[-limit:]
        else:
            last_calls = traceback_details
        formatted_traceback = ""
        if last_calls:
            formatted_traceback = "".join(traceback.format_list(last_calls))

        data = ""
        if type_name:
            data += "Type: {}".format(type_name)
        if value:
            data += "Message: {}".format(value)
        if formatted_traceback:
            data += "\nTraceback: {}".format(formatted_traceback)

        return is_sys, data

    def parse_alert(self, msg: Any) -> str:
        """
        Parse alert message

        :param msg: message to parse
        :return: parsed message
        """
        if isinstance(msg, Exception):
            is_sys, data = self.parse_exception(msg)
            return "Exception: {}\n{}".format(str(msg), data)
        return str(msg)

    def has_level(self, level: int) -> bool:
        """
        Check if logging level is enabled

        :param level: logging level
        :return: True if enabled
        """
        return logging.getLogger().isEnabledFor(level)

    def enabled(self) -> bool:
        """
        Check if debug is enabled

        :return: True if enabled
        """
        if self.window is not None and self.window.controller.debug.logger_enabled():
            return True
        if self.has_level(logging.DEBUG):
            return True
        return False

    def begin(self, id: str):
        """
        Begin debug data (debug window)

        :param id: debug id
        """
        self.window.controller.dialogs.debug.begin(id)

    def end(self, id: str):
        """
        End debug data (debug window)

        :param id: debug id
        """
        self.window.controller.dialogs.debug.end(id)

    def add(self, id: str, k: str, v: Any):
        """
        Append debug entry (debug window)

        :param id: debug id
        :param k: key
        :param v: value
        """
        self.window.controller.dialogs.debug.add(id, k, v)

    def print_memory_usage(self, label="") -> str:
        """
        Print memory usage of the current process

        :param label: label for memory usage
        :return: formatted memory usage string
        """
        rss_mb = self._process.memory_info().rss / (1024 * 1024)
        uss_mb = getattr(self._process.memory_full_info(), "uss", 0) / 1024 / 1024
        data =  f"RSS={rss_mb:.0f} MB  USS={uss_mb:.0f} MB"

        children_parts = []
        for c in self._process.children(recursive=True):
            children_parts.append(
                f"{c.pid} {c.name()} {round(c.memory_info().rss / 1024 / 1024)} MB"
            )
        if children_parts:
            data += "\n" + "\n".join(children_parts)
        print(f"[{label}] {data}")
        return data

    def mem(self, label: str = "") -> str:
        """
        Print memory usage and collect garbage

        :param label: label for memory usage
        :return: formatted memory usage string
        """
        res = ""
        print("\n\n------------------------------------")
        print(f"{Color.BOLD}{label} Memory Usage{Color.ENDC}")
        print("------------------------------------")

        all_objects = len(gc.get_objects())
        unreachable_objects = gc.collect()

        num_widgets = len(QApplication.allWidgets())
        num_threads = self.window.threadpool.activeThreadCount()

        stats = []
        stats.append(f"[GC] All: {all_objects}, Unreachable: {unreachable_objects}")

        res += self.print_memory_usage(label)

        try:
            from pympler import asizeof, summary, muppy
            objs = muppy.get_objects()
            sum_by_type = summary.summarize(objs)
            summary.print_(sum_by_type)

            pids = self.window.controller.chat.render.web_renderer.pids
            total_bytes = asizeof.asizeof(pids)
            pids_total_mb = total_bytes / (1024 * 1024)
            count_pids = len(pids)

            meta = self.window.core.ctx.meta
            total_bytes = asizeof.asizeof(meta)
            meta_total_mb = total_bytes / (1024 * 1024)
            count_meta = len(meta)

            ctx_items = self.window.core.ctx.get_items()
            total_bytes = asizeof.asizeof(ctx_items)
            ctx_total_mb = total_bytes / (1024 * 1024)
            count_ctx = len(ctx_items)

            stats.append(f"Pids: {pids_total_mb:.4f} MB ({count_pids})")
            stats.append(f"CtxMeta: {meta_total_mb:.4f} MB ({count_meta})")
            stats.append(f"CtxItems: {ctx_total_mb:.4f} MB ({count_ctx})")

        except ImportError:
            err = "Pympler is not installed, skipping detailed memory report. Install it with 'pip install pympler'"
            res += err
            print(err)

        stats.append(f"Widgets: {num_widgets}")
        stats.append(f"Threadpool: {num_threads}")

        # count all QObjects in app
        qobjects = sum(1 for obj in QApplication.allWidgets() if isinstance(obj, QObject))
        stats.append(f"QObjects: {qobjects}")

        res += "\n" + "\n".join(stats)
        print("\n".join(stats))
        return res

    def trace(self):
        """
        Print current stack trace

        Prints the current stack trace and returns it as a string.
        """
        stack = traceback.format_stack()
        formatted_trace = "".join(stack)
        print(formatted_trace)
        return formatted_trace

    def pause(self, *args):
        """
        Pause execution

        Pause execution and print traceback.

        :param args: objects to dump
        """
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        t = threading.current_thread()
        thread_info = "[MAIN THREAD]" if t is threading.main_thread() else f"[THREAD: {t.ident}]"
        print(f"\n{Color.FAIL}{Color.BOLD}<DEBUG: PAUSED> #{self.pause_idx} {dt}{Color.ENDC}")
        print(f"\n{Color.BOLD}{thread_info}{Color.ENDC}")
        print("------------------------------>")
        self.pause_idx += 1

        for index, arg in enumerate(args):
            print(f"\n{Color.BOLD}Dump {index + 1}:{Color.ENDC}")
            print(f"{Color.BOLD}Type: {type(arg)}{Color.ENDC}")
            print(arg)

        if args:
            print("\n\n")

        traceback.print_stack()

        input(f"<------------------------------\n\n{Color.OKGREEN}Paused. Press Enter to continue...{Color.ENDC}")
        print(f"------------------------------\n{Color.OKGREEN}{Color.BOLD}<RESUMED>{Color.ENDC}\n")