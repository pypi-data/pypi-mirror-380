#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.24 23:00:00                  #
# ================================================== #

from datetime import datetime
from typing import Optional, List

from PySide6.QtGui import QTextCursor, QTextBlockFormat

from pygpt_net.core.render.base import BaseRenderer
from pygpt_net.ui.widget.textarea.input import ChatInput
from pygpt_net.ui.widget.textarea.output import ChatOutput
from pygpt_net.item.ctx import CtxItem, CtxMeta

from .body import Body
from .helpers import Helpers
from .pid import PidData


class Renderer(BaseRenderer):
    def __init__(self, window=None):
        super(Renderer, self).__init__(window)
        """
        Plain text renderer

        :param window: Window instance
        """
        self.window = window
        self.body = Body(window)
        self.helpers = Helpers(window)
        self.pids = {}  # per node data

        # Pid-related cached methods
        self._get_pid = None
        self._get_output_node_by_meta = None
        self._get_output_node_by_pid = None
        if (self.window and hasattr(self.window, "core")
                and hasattr(self.window.core, "ctx")
                and hasattr(self.window.core.ctx, "output")):
            self._get_pid = self.window.core.ctx.output.get_pid
            self._get_output_node_by_meta = self.window.core.ctx.output.get_current_plain
            self._get_output_node_by_pid = self.window.core.ctx.output.get_by_pid

    def prepare(self):
        """
        Prepare renderer
        """
        self.pids = {}

    def fresh(self, meta: CtxMeta):
        """
        Fresh renderer

        :param meta: context PID
        """
        self.reset(meta)
        self.clear_output(meta)

    def get_pid(self, meta: CtxMeta):
        """
        Get PID for context meta

        :param meta: context PID
        """
        if self._get_pid is None:
            self._get_pid = self.window.core.ctx.output.get_pid
        return self._get_pid(meta)

    def get_or_create_pid(self, meta: CtxMeta):
        """
        Get PID for context meta and create PID data (if not exists)

        :param meta: context PID
        """
        if meta is not None:
            pid = self.get_pid(meta)
            if pid not in self.pids:
                self.pid_create(pid, meta)
            return pid

    def pid_create(self, pid, meta: CtxMeta):
        """
        Create PID data

        :param pid: PID
        :param meta: context meta
        """
        if pid is not None:
            self.pids[pid] = PidData(pid, meta)

    def get_pid_data(self, pid: int):
        """
        Get PID data for given PID

        :param pid: PID
        """
        if pid in self.pids:
            return self.pids[pid]

    def begin(
            self,
            meta: CtxMeta,
            ctx: CtxItem,
            stream: bool = False
    ):
        """
        Render begin

        :param meta: context meta
        :param ctx: context item
        :param stream: True if it is a stream
        """
        self.to_end(meta)

    def end(
            self,
            meta: CtxMeta,
            ctx: CtxItem,
            stream: bool = False
    ):
        """
        Render end

        :param meta: context meta
        :param ctx: context item
        :param stream: True if it is a stream
        """
        self.to_end(meta)

    def end_extra(
            self,
            meta: CtxMeta,
            ctx: CtxItem,
            stream: bool = False
    ):
        """
        Render end extra

        :param meta: context meta
        :param ctx: context item
        :param stream: True if it is a stream
        """
        self.to_end(meta)

    def stream_begin(
            self,
            meta: CtxMeta,
            ctx: CtxItem
    ):
        """
        Render stream begin

        :param meta: context meta
        :param ctx: context item
        """
        pass  # do nothing

    def stream_end(
            self,
            meta: CtxMeta,
            ctx: CtxItem
    ):
        """
        Render stream end

        :param meta: context meta
        :param ctx: context item
        """
        pass  # do nothing

    def append_context(
            self,
            meta: CtxMeta,
            items: List[CtxItem],
            clear: bool = True
    ):
        """
        Append all context to output

        :param meta: context meta
        :param items: context items
        :param clear: True if clear all output before append
        """
        if clear:
            self.clear_output(meta)

        for i, item in enumerate(items):
            item.idx = i
            self.append_context_item(meta, item)

    def append_input(
            self,
            meta: CtxMeta,
            item: CtxItem,
            flush: bool = True,
            append: bool = False
    ):
        """
        Append text input to output

        :param meta: context meta
        :param item: context item
        :param flush: True if flush
        :param append: True to force append node
        """
        if item.input is None or item.input == "":
            return
        if self.is_timestamp_enabled() and item.input_timestamp is not None:
            name = ""
            if item.input_name is not None and item.input_name != "":
                name = f"{item.input_name} "
            ts = datetime.fromtimestamp(item.input_timestamp)
            hour = ts.strftime("%H:%M:%S")
            text = f"{name}{hour} > {item.input}"
        else:
            text = f"> {item.input}"
        self.append_raw(meta, item, text.strip())
        self.to_end(meta)

    def append_output(
            self,
            meta: CtxMeta,
            item: CtxItem
    ):
        """
        Append text output to output

        :param meta: context meta
        :param item: context item
        """
        if item.output is None or item.output == "":
            return
        if self.is_timestamp_enabled() and item.output_timestamp is not None:
            name = ""
            if item.output_name is not None and item.output_name != "":
                name = f"{item.output_name} "
            ts = datetime.fromtimestamp(item.output_timestamp)
            hour = ts.strftime("%H:%M:%S")
            text = f"{name}{hour} {item.output}"
        else:
            text = f"{item.output}"
        self.append_raw(meta, item, text.strip())
        self.to_end(meta)

    def append_extra(
            self,
            meta: CtxMeta,
            item: CtxItem,
            footer: bool = False
    ):
        """
        Append extra data (images, files, etc.) to output

        :param meta: context meta
        :param item: context item
        :param footer: True if it is a footer
        """
        appended = set()
        pid = self.get_or_create_pid(meta)

        # images
        c = len(item.images)
        if c > 0:
            n = 1
            pd = self.pids[pid]
            already = set(pd.images_appended)
            for image in item.images:
                if image in appended or image in already:
                    continue
                try:
                    appended.add(image)
                    self.append_raw(meta, item, self.body.get_image_html(image, n, c))
                    pd.images_appended.append(image)
                    already.add(image)
                    n += 1
                except Exception as e:
                    pass

        # files and attachments, TODO check attachments
        c = len(item.files)
        if c > 0:
            n = 1
            for file in item.files:
                if file in appended:
                    continue
                try:
                    appended.add(file)
                    self.append_raw(meta, item, self.body.get_file_html(file, n, c))
                    n += 1
                except Exception as e:
                    pass

        # urls
        c = len(item.urls)
        if c > 0:
            urls_str = []
            n = 1
            pd = self.pids[pid]
            already = set(pd.urls_appended)
            for url in item.urls:
                if url in appended or url in already:
                    continue
                try:
                    appended.add(url)
                    urls_str.append(self.body.get_url_html(url, n, c))
                    pd.urls_appended.append(url)
                    already.add(url)
                    n += 1
                except Exception as e:
                    pass
            if urls_str:
                urls_joined = "\n".join(urls_str)
                self.append_raw(meta, item, f"\n{urls_joined}")

        if self.window.core.config.get('ctx.sources'):
            if item.doc_ids is not None and len(item.doc_ids) > 0:
                try:
                    docs = self.body.get_docs_html(item.doc_ids)
                    self.append_raw(meta, item, docs)
                    self.to_end(meta)
                except Exception as e:
                    pass

        # jump to end
        if len(appended) > 0:
            self.to_end(meta)

    def append_chunk(
            self,
            meta: CtxMeta,
            item: CtxItem,
            text_chunk: str,
            begin: bool = False
    ):
        """
        Append output chunk to output

        :param meta: context meta
        :param item: context item
        :param text_chunk: text chunk
        :param begin: if it is the beginning of the text
        """
        if text_chunk is None or text_chunk == "":
            return

        pid = self.get_or_create_pid(meta)
        raw_chunk = str(text_chunk)

        if begin:
            pd = self.pids[pid]
            pd.buffer = ""
            pd.is_cmd = False

            if self.is_timestamp_enabled() and item.output_timestamp is not None:
                name = ""
                if item.output_name is not None and item.output_name != "":
                    name = f"{item.output_name} "
                ts = datetime.fromtimestamp(item.output_timestamp)
                hour = ts.strftime("%H:%M:%S")
                text_chunk = f"{name}{hour}: {text_chunk}"

            text_chunk = f"\n{text_chunk}"
            self.append_block(meta)
            self.append_chunk_start(meta, item)

        self.pids[pid].append_buffer(raw_chunk)
        self.append(meta, item, self.helpers.format_chunk(text_chunk), "")

    def append_block(
            self,
            meta: CtxMeta
    ):
        """
        Append block to output

        :param meta: context meta
        """
        node = self.get_output_node(meta)
        follow = getattr(node, "was_at_bottom", None)
        follow = node.was_at_bottom() if callable(follow) else True
        cursor = node.textCursor()
        cursor.movePosition(QTextCursor.End)
        block_format = QTextBlockFormat()
        block_format.setIndent(0)
        cursor.insertBlock(block_format)
        if follow or (hasattr(node, "is_auto_scroll_enabled") and node.is_auto_scroll_enabled()):
            node.setTextCursor(cursor)
            node.ensureCursorVisible()

    def append_raw(
            self,
            meta: CtxMeta,
            ctx: CtxItem,
            text: str
    ):
        """
        Append and format raw text to output as plain text.

        :param meta: context meta
        :param ctx: context item
        :param text: text to append
        """
        node = self.get_output_node(meta)
        follow = getattr(node, "was_at_bottom", None)
        follow = node.was_at_bottom() if callable(follow) else True
        cur = node.textCursor()
        cur.movePosition(QTextCursor.End)
        if not node.document().isEmpty():
            cur.insertText("\n\n")
        cur.insertText(text.strip())
        if follow or (hasattr(node, "is_auto_scroll_enabled") and node.is_auto_scroll_enabled()):
            node.setTextCursor(cur)
            node.ensureCursorVisible()

    def append_chunk_start(self, meta: CtxMeta, ctx: CtxItem):
        """
        Append start of chunk to output

        :param meta: context meta
        :param ctx: context item
        """
        node = self.get_output_node(meta)
        follow = getattr(node, "was_at_bottom", None)
        follow = node.was_at_bottom() if callable(follow) else True
        cursor = node.textCursor()
        cursor.movePosition(QTextCursor.End)
        if follow or (hasattr(node, "is_auto_scroll_enabled") and node.is_auto_scroll_enabled()):
            node.setTextCursor(cursor)
            node.ensureCursorVisible()

    def append_context_item(
            self,
            meta: CtxMeta,
            item: CtxItem
    ):
        """
        Append context item to output

        :param meta: context meta
        :param item: context item
        """
        self.append_input(meta, item)
        self.append_output(meta, item)
        self.append_extra(meta, item)

    def append(
            self,
            meta: CtxMeta,
            ctx: CtxItem,
            text: str,
            end: str = "\n"
    ):
        """
        Append text to output.

        :param meta: context meta
        :param ctx: context item
        :param text: text to append
        :param end: end of the line character
        """
        node = self.get_output_node(meta)
        follow = getattr(node, "was_at_bottom", None)
        follow = node.was_at_bottom() if callable(follow) else True
        cur = node.textCursor()
        cur.movePosition(QTextCursor.End)
        cur.insertText(f"{str(text)}{end}")
        if follow or (hasattr(node, "is_auto_scroll_enabled") and node.is_auto_scroll_enabled()):
            node.setTextCursor(cur)
            node.ensureCursorVisible()

    def append_timestamp(
            self,
            item: CtxItem,
            text: str
    ) -> str:
        """
        Append timestamp to text

        :param item: context item
        :param text: input text
        :return: Text with timestamp (if enabled)
        """
        if item is not None \
                and self.is_timestamp_enabled() \
                and item.input_timestamp is not None:
            ts = datetime.fromtimestamp(item.input_timestamp)
            hour = ts.strftime("%H:%M:%S")
            text = f"{hour}: {text}"
        return text

    def reset(self, meta: Optional[CtxMeta] = None):
        """
        Reset

        :param meta: context meta
        """
        pid = self.get_or_create_pid(meta)
        if pid is not None:
            self.pids[pid].images_appended = []
            self.pids[pid].urls_appended = []

    def reload(self):
        """Reload output, called externally only on theme change to redraw content"""
        self.window.controller.ctx.refresh_output()  # if clear all and appends all items again

    def clear_output(self, meta: Optional[CtxMeta] = None):
        """
        Clear output

        :param meta: context meta
        """
        self.reset()
        self.get_output_node(meta).clear()

    def clear_input(self):
        """Clear input"""
        self.get_input_node().clear()

    def to_end(self, meta: CtxMeta):
        """
        Move cursor to end of output

        :param meta: context meta
        """
        node = self.get_output_node(meta)
        was_bottom = getattr(node, "was_at_bottom", None)
        was_bottom = node.was_at_bottom() if callable(was_bottom) else True
        allow = was_bottom or (hasattr(node, "is_auto_scroll_enabled") and node.is_auto_scroll_enabled())
        if not allow:
            return
        cursor = node.textCursor()
        cursor.movePosition(QTextCursor.End)
        node.setTextCursor(cursor)
        node.ensureCursorVisible()

    def is_timestamp_enabled(self) -> bool:
        """
        Check if timestamp is enabled

        :return: True if timestamp is enabled
        """
        return self.window.core.config.get('output_timestamp')

    def get_output_node(
            self,
            meta: Optional[CtxMeta] = None
    ) -> ChatOutput:
        """
        Get output node for current context.

        :param meta: context meta
        :return: output node
        """
        if self._get_output_node_by_meta is None:
            self._get_output_node_by_meta = self.window.core.ctx.output.get_current_plain
        return self._get_output_node_by_meta(meta)

    def get_input_node(self) -> ChatInput:
        """
        Get input node

        :return: input node
        """
        return self.window.ui.nodes['input']

    def get_all_nodes(self) -> list:
        """
        Return all registered nodes

        :return: list of ChatOutput nodes (tabs)
        """
        return self.window.core.ctx.output.get_all_plain()

    def clear_all(self):
        """Clear all"""
        for node in self.get_all_nodes():
            try:
                node.clear()
            except Exception as e:
                pass

    def remove_pid(self, pid: int):
        """
        Remove PID from renderer
        """
        if pid in self.pids:
            del self.pids[pid]