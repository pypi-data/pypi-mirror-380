#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.02 22:00:00                  #
# ================================================== #

import copy
import json
from typing import Optional

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QStandardItem
from PySide6.QtCore import Qt, QTimer

from pygpt_net.item.assistant import AssistantStoreItem
from pygpt_net.utils import trans


class VectorStore:
    def __init__(self, window=None):
        """
        Assistant vector store editor controller

        :param window: Window instance
        """
        self.window = window
        self.dialog = False
        self.config_initialized = False
        self.current = None
        self.width = 800
        self.height = 500
        self.id = "assistant.store"
        self.options = {
            "id": {
                "type": "text",
                "label": "assistant.store.id",
                "read_only": True,
                "value": "",
            },
            "name": {
                "type": "text",
                "label": "assistant.store.name",
                "value": "",
            },
            "expire_days": {
                "type": "int",
                "label": "assistant.store.expire_days",
                "value": 0,
            },
            "status": {
                "type": "textarea",
                "label": "assistant.store.status",
                "read_only": True,
                "value": "",
            },
        }
        # Mapping of current files list rows to file IDs
        self._files_row_to_id = []

    def get_options(self) -> dict:
        """
        Get options dict

        :return: options dict
        """
        return self.options

    def get_option(self, key: str) -> Optional[dict]:
        """
        Get option by key

        :param key: option key
        :return: option dict
        """
        if key in self.options:
            return self.options[key]

    def setup(self):
        """Set up vector store editor"""
        idx = None
        self.window.assistant_store.setup(idx)  # widget dialog setup

    def toggle_editor(self):
        """Toggle vector store editor dialog"""
        if self.dialog:
            self.close()
        else:
            self.open()

    def reset(self):
        """Reset vector store editor"""
        self.current = None
        if self.dialog:
            self.init()

    def open(self, force: bool = False):
        """
        Open vector store editor dialog

        :param force: force open dialog
        """
        if not self.config_initialized:
            self.setup()
            self.config_initialized = True
        if not self.dialog or force:
            self.current = self.window.controller.assistant.editor.get_selected_store_id()
            self.init()
            self.window.ui.dialogs.open(
                "assistant.store",
                width=self.width,
                height=self.height,
            )
            self.dialog = True

    def close(self):
        """Close vector store editor dialog"""
        if self.dialog:
            self.window.ui.dialogs.close('assistant.store')
            self.dialog = False

    def init(self):
        """Initialize vector store editor options"""
        self.reload_items()

        # select the first store if not selected
        if self.current is None:
            self.current = self.get_first_visible()

        # assign store to config dialog fields
        options = copy.deepcopy(self.get_options())  # copy options
        if self.current is not None and self.window.core.assistants.store.has(self.current):
            store = self.window.core.assistants.store.items[self.current]
            data_dict = store.to_dict()
            for key in options:
                if key in data_dict:
                    value = data_dict[key]
                    options[key]["value"] = value
                    if key == "status":
                        options[key]["value"] = json.dumps(value, indent=4)  # as JSON to textarea

            self.set_tab_by_id(self.current)

            # load and apply options to config dialog
            self.window.controller.config.load_options(self.id, options)
        else:
            self.current = None  # reset if not exists
            self.window.controller.config.load_options(self.id, options)

        self.update_files_list()

    def refresh_status(self):
        """Reload store status"""
        if self.current is not None:  # TODO: reset on profile reload
            if self.window.core.assistants.store.has(self.current):
                self.window.update_status(trans('status.sending'))
                QApplication.processEvents()
                store = self.window.core.assistants.store.items[self.current]
                self.refresh_store(store)
                self.window.update_status(trans('status.assistant.saved'))
                self.update()  # update stores list in assistant dialog
                self.update_files_list()

    def refresh_store(
            self,
            store: AssistantStoreItem,
            update: bool = True
    ):
        """
        Refresh store by ID

        :param store : store object
        :param update: update store after refresh
        """
        # update from API
        self.window.core.assistants.store.update_status(store.id)
        self.window.core.assistants.store.update(store)

        if update and store.id == self.current:
            self.update_current()

    def refresh_by_idx(self, idx: int):
        """
        Refresh store by idx

        :param idx: store idx
        """
        store_id = self.get_by_tab_idx(idx)
        if store_id is not None:
            self.refresh_by_store_id(store_id)

    def refresh_by_store_id(self, store_id: str):
        """
        Refresh store by ID

        :param store_id: store id
        """
        if store_id is not None and store_id in self.window.core.assistants.store.items:
            store = self.window.core.assistants.store.items[store_id]
            if store is not None:
                self.window.update_status(trans('status.sending'))
                QApplication.processEvents()
                self.refresh_store(store)
                self.window.update_status(trans('status.assistant.saved'))
                self.update()
                if self.current == store_id:
                    self.update_files_list()

    def update_current(self):
        """Update current store"""
        if self.current is not None and self.window.core.assistants.store.has(self.current):
            store = self.window.core.assistants.store.items[self.current]
            # update textarea
            option = copy.deepcopy(self.get_option("status"))
            option["value"] = json.dumps(store.status, indent=4)
            self.window.controller.config.apply(self.id, "status", option)

            # update name
            option = copy.deepcopy(self.get_option("name"))
            option["value"] = store.name
            self.window.controller.config.apply(self.id, "name", option)

            # update expire days
            option = copy.deepcopy(self.get_option("expire_days"))
            option["value"] = store.expire_days
            self.window.controller.config.apply(self.id, "expire_days", option)

    def save_btn(self):
        """Save vector store editor and close dialog"""
        self.window.update_status("Saving...")
        self.save()
        self.refresh_status()
        self.window.update_status("Saved.")

    def save(self, persist: bool = True):
        """
        Save vector store editor

        :param persist: persist to file and close dialog
        """
        if self.current is not None:
            current = self.window.core.assistants.store.items[self.current].to_dict()
            options = copy.deepcopy(self.get_options())  # copy options
            data_dict = {}
            for key in options:
                if key == "status":
                    data_dict[key] = current[key]  # use initial value
                    continue  # skip status
                value = self.window.controller.config.get_value(
                    parent_id="assistant.store",
                    key=key,
                    option=options[key],
                )
                data_dict[key] = value
            self.window.core.assistants.store.items[self.current].from_dict(data_dict)

        # save config
        if persist:
            self.window.update_status(trans('status.sending'))
            QApplication.processEvents()
            if self.current is not None:
                store = self.window.core.assistants.store.update(
                    self.window.core.assistants.store.items[self.current]
                )
                if store is None:
                    self.window.update_status(trans('status.error'))
                    self.window.ui.dialogs.alert("Failed to save vector store")
                    return

            self.update()  # update stores list in assistant dialog
            self.window.update_status(trans("info.settings.saved"))
            self.restore_selection()
            self.update_files_list()

    def reload_items(self):
        """Reload list items"""
        items = self.window.core.assistants.store.items
        self.window.assistant_store.update_list("assistant.store.list", items)
        self.restore_selection()

    def restore_selection(self):
        """Restore selection"""
        if self.current is not None:
            idx = self.get_tab_by_id(self.current)
            if idx is not None:
                self.set_by_tab(idx)

    def select(self, idx: int):
        """
        Select store by idx

        :param idx: idx on list
        """
        self.save(persist=False)
        self.current = self.get_by_tab_idx(idx)
        self.init()
        self.update_files_list()

    def new(self):
        """Create new vector store"""
        self.window.update_status(trans('status.sending'))
        QApplication.processEvents()

        store = self.window.core.assistants.store.create()
        if store is None:
            self.window.update_status(trans('status.error'))
            self.window.ui.dialogs.alert("Failed to create new vector store")
            return

        self.window.update_status(trans('status.assistant.saved'))

        self.window.core.assistants.store.update(store)
        self.update()  # update stores list in assistant dialog

        # switch to created store
        self.current = store.id
        idx = self.get_tab_by_id(self.current)
        self.set_by_tab(idx)
        self.init()
        self.restore_selection()
        self.refresh_by_store_id(store.id)
        self.update_files_list()

    def delete_by_idx(
            self,
            idx: int,
            force: bool = False
    ):
        """
        Delete store by idx

        :param idx: store idx
        :param force: force delete
        """
        store_id = self.get_by_tab_idx(idx)
        self.delete(store_id, force=force)

    def delete(
            self,
            store_id: Optional[str] = None,
            force: bool = False
    ):
        """
        Delete store by idx

        :param store_id: store id
        :param force: force delete
        """
        if not force:
            self.window.ui.dialogs.confirm(
                type="assistant.store.delete",
                id=store_id,
                msg=trans("dialog.assistant.store.delete.confirm"),
            )
            return

        if store_id is None:
            self.window.ui.dialogs.alert("Please select vector store first.")
            return

        self.window.update_status(trans('status.sending'))
        QApplication.processEvents()
        if self.current == store_id:
            self.current = None
        try:
            print("Deleting store: {}".format(store_id))
            if self.window.core.assistants.store.delete(store_id):
                self.window.controller.assistant.batch.remove_store_from_assistants(store_id)
                self.window.update_status(trans('status.deleted'))
                self.window.core.assistants.store.save()
                self.window.controller.assistant.files.update()
                self.update()  # update stores list in assistant dialog
                self.init()
                self.restore_selection()
                self.update_files_list()
            else:
                self.window.update_status(trans('status.error'))
        except Exception as e:
            self.window.update_status(trans('status.error'))
            self.window.ui.dialogs.alert(e)

    def set_by_tab(self, idx: int):
        """
        Set current list by tab index

        :param idx: tab index
        """
        store_idx = 0
        for id in self.window.core.assistants.store.get_ids():
            if self.window.core.assistants.store.is_hidden(id):
                continue
            if store_idx == idx:
                self.current = id
                break
            store_idx += 1
        current = self.window.ui.models['assistant.store.list'].index(idx, 0)
        self.window.ui.nodes['assistant.store.list'].setCurrentIndex(current)

    def set_tab_by_id(self, store_id: str):
        """
        Set current list to id

        :param store_id: store id
        """
        idx = self.get_tab_idx(store_id)
        current = self.window.ui.models['assistant.store.list'].index(idx, 0)
        self.window.ui.nodes['assistant.store.list'].setCurrentIndex(current)

    def get_tab_idx(self, store_id: str) -> int:
        """
        Get list index (including hidden)

        :param store_id: model id
        :return: list index
        """
        store_idx = None
        i = 0
        for id in self.window.core.assistants.store.get_ids():
            if self.window.core.assistants.store.is_hidden(id):
                continue
            if id == store_id:
                store_idx = i
                break
            i += 1
        return store_idx

    def get_tab_by_id(self, store_id: str) -> int:
        """
        Get list index (including hidden)

        :param store_id: store id
        :return: list index
        """
        idx = None
        i = 0
        for id in self.window.core.assistants.store.get_ids():
            if self.window.core.assistants.store.is_hidden(id):
                continue
            if id == store_id:
                idx = i
                break
            i += 1
        return idx

    def get_by_tab_idx(self, idx: int) -> Optional[str]:
        """
        Get key by list index (including hidden)

        :param idx: list index
        :return: store id / key
        """
        store_idx = 0
        for id in self.window.core.assistants.store.get_ids():
            if self.window.core.assistants.store.is_hidden(id):
                continue
            if store_idx == idx:
                return id
            store_idx += 1
        return None

    def get_first_visible(self) -> Optional[str]:
        """
        Get first visible store ID (including hidden)

        :return: store id
        """
        for id in self.window.core.assistants.store.get_ids():
            if not self.window.core.assistants.store.is_hidden(id):
                return id
        return None

    def open_by_idx(self, idx: int):
        """
        Open editor by tab index

        :param idx: list index
        """
        store = self.window.core.assistants.store.get_by_idx(idx)
        if store is None:
            return
        self.current = store
        self.open(force=True)

    def update(self):
        """Update vector store editor"""
        self.reload_items()
        self.window.controller.assistant.editor.update_store_list()  # update stores list in assistant dialog
        self.update_files_list()

    def set_hide_thread(self, state: bool):
        """
        Toggle show thread stores

        :param state: state
        """
        self.window.core.config.set("assistant.store.hide_threads", state)
        self.update()

    # ==================== Files  ====================

    def update_files_list(self):
        """
        Update files list view for the current store based on local DB.
        This method does not hit the API; it reflects local state.
        """
        model_id = 'assistant.store.files.list'
        if 'assistant.store.files.list' not in self.window.ui.models:
            return  # files panel not initialized yet
        model = self.window.ui.models[model_id]
        try:
            model.removeRows(0, model.rowCount())
        except Exception:
            pass

        self._files_row_to_id = []

        if self.current is None:
            return

        files_db = self.window.core.assistants.files
        if files_db is None:
            return

        # Resolve store files collection from DB
        try:
            store_files = files_db.get_by_store_or_thread(self.current, None) or {}
        except Exception as e:
            self.window.core.debug.log(e)
            store_files = {}

        i = 0
        for file_id, file_obj in store_files.items():
            if isinstance(file_obj, dict):
                data = file_obj
            else:
                data = {}
                for key in ('id', 'file_id', 'name', 'filename', 'bytes', 'size', 'usage_bytes', 'status'):
                    try:
                        if hasattr(file_obj, key):
                            data[key] = getattr(file_obj, key)
                    except Exception:
                        pass
                if not data and hasattr(file_obj, 'to_dict'):
                    try:
                        data = file_obj.to_dict()
                    except Exception:
                        data = {}

            # Choose display name
            name = data.get('filename') or data.get('name') or file_id
            # Choose size
            size_val = None
            for k in ('bytes', 'size', 'usage_bytes'):
                if data.get(k) is not None:
                    size_val = data.get(k)
                    break

            # Human-readable size if possible
            size_txt = ""
            try:
                if size_val:
                    size_txt = self.window.core.filesystem.sizeof_fmt(int(size_val))
            except Exception:
                pass

            extra = []
            if size_txt:
                extra.append(size_txt)
            if data.get('status'):
                extra.append(str(data.get('status')))
            label = name
            if extra:
                label += " ({})".format(", ".join(extra))

            item = QStandardItem(label)
            item.setEditable(False)
            item.setData(file_id, Qt.UserRole)
            model.setItem(i, 0, item)
            self._files_row_to_id.append(data['file_id'] if 'file_id' in data else file_id)
            i += 1

    def delete_file_by_idx(self, idx: int, force: bool = False):
        """
        Delete a single file from the current store by row index in files list.
        This uses API to remove the file from a remote store, then triggers async re-import
        of files for the current store to keep the local DB in sync.

        :param idx: row index in files list
        :param force: force delete without confirmation
        """
        if self.current is None:
            self.window.ui.dialogs.alert("Please select vector store first.")
            return

        if not force:
            self.window.ui.dialogs.confirm(
                type='assistant.file.delete',
                id=idx,
                msg=trans('confirm.assistant.store.file.delete'),
            )
            return

        model_id = 'assistant.store.files.list'
        if model_id not in self.window.ui.models:
            return
        if idx < 0 or idx >= len(self._files_row_to_id):
            return

        file_id = self._files_row_to_id[idx]
        if not file_id:
            return

        # Update UI state
        self.window.update_status(trans('status.sending'))
        QApplication.processEvents()

        try:
            api = self.window.core.api.openai.store
            removed = False

            # Prefer store-scoped removal if available
            if hasattr(api, 'remove_store_file'):
                try:
                    api.remove_store_file(self.current, file_id)
                    removed = True
                except Exception as e:
                    self.window.core.debug.log(e)

            # Fallback: remove by file_id only
            if not removed and hasattr(api, 'remove_file'):
                try:
                    api.remove_file(file_id)
                    removed = True
                except Exception as e:
                    self.window.core.debug.log(e)

            if not removed:
                raise RuntimeError("Remove file API not available.")

            # Remove from local DB
            try:
                self.window.core.assistants.files.delete_by_file_id(file_id)
            except Exception as e:
                self.window.core.debug.log(e)

            # Optimistic UI update: remove row from the model immediately
            try:
                self.window.ui.models[model_id].removeRow(idx)
                # also update index map
                try:
                    del self._files_row_to_id[idx]
                except Exception:
                    pass
            except Exception:
                pass

            # Trigger re-import for the current store to refresh local DB and UI elsewhere
            try:
                self.window.update_status("Refreshing status...")
                QTimer.singleShot(1000, lambda: self.window.controller.assistant.store.refresh_status())
            except Exception as e:
                self.window.core.debug.log(e)

            self.window.update_status(trans('status.deleted'))

        except Exception as e:
            self.window.update_status(trans('status.error'))
            self.window.ui.dialogs.alert("Failed to delete file: {}".format(e))
            self.window.core.debug.log(e)
            self.update_files_list()