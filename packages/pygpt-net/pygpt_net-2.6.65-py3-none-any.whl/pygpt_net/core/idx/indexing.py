#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.21 07:00:00                  #
# ================================================== #

import datetime
import os
import time

from pathlib import Path
from typing import Optional, Tuple, List, Dict, Any

from sqlalchemy import text

from llama_index.core.indices.base import BaseIndex
from llama_index.core.schema import Document
from llama_index.core import SimpleDirectoryReader

from pygpt_net.item.model import ModelItem
from pygpt_net.provider.loaders.base import BaseLoader
from pygpt_net.utils import parse_args, pack_arg


class Indexing:
    def __init__(self, window=None):
        """
        Indexing core

        :param window: Window instance
        """
        self.window = window
        self.loaders = {
            "file": {},  # file loaders
            "web": {},   # web loaders
        }
        self.data_providers = {}  # data providers (loaders)
        self.external_instructions = {}
        self.external_config = {}
        self.last_call = None

    def register_loader(self, loader: BaseLoader):
        """
        Register data loader

        :param loader: data loader instance
        """
        # check if compiled version is allowed
        is_compiled = self.window.core.config.is_compiled() or self.window.core.platforms.is_snap()
        if not loader.allow_compiled and is_compiled:
            self.window.core.idx.log(f"Loader not allowed in compiled version: {loader.id}" )
            return

        loader.attach_window(self.window)
        self.data_providers[loader.id] = loader  # cache loader
        extensions = loader.extensions  # available extensions
        types = loader.type  # available types

        if "file" in types:
            loader.set_args(self.get_loader_arguments(loader.id, "file"))  # set reader arguments
            try:
                for ext in extensions:
                    self.loaders["file"][ext] = loader  # set reader instance, by file extension
            except ImportError as e:
                msg = f"Error while registering data loader: {loader.id} - {e}"
                self.window.core.debug.log(msg)
                self.window.core.debug.log(e)

        if "web" in types:
            loader.set_args(self.get_loader_arguments(loader.id, "web"))  # set reader arguments
            try:
                self.loaders["web"][loader.id] = loader # set reader instance, by id
                if loader.instructions:
                    for item in loader.instructions:
                        cmd = list(item.keys())[0]
                        self.external_instructions[cmd] = item[cmd]
                if loader.init_args:
                    for key in loader.init_args:
                        if loader.id not in self.external_config:
                            self.external_config[loader.id] = {}
                        self.external_config[loader.id][key] = {
                            "key": key,
                            "value": loader.init_args[key],
                            "type": "str",  # default = str
                            "label": key,
                            "description": None,
                        }
                        # from config
                        if key in loader.args:
                            self.external_config[loader.id][key]["value"] = loader.args[key]
                        if key in loader.init_args_types:
                            self.external_config[loader.id][key]["type"] = loader.init_args_types[key]
                        if key in loader.init_args_labels:
                            self.external_config[loader.id][key]["label"] = loader.init_args_labels[key]
                        if key in loader.init_args_desc:
                            self.external_config[loader.id][key]["description"] = loader.init_args_desc[key]

            except ImportError as e:
                msg = f"Error while registering data loader: {loader.id} - {e}"
                self.window.core.debug.log(msg)
                self.window.core.debug.log(e)

    def get_loader(self, loader: str) -> Optional[BaseLoader]:
        """
        Get data loader by id

        :param loader: loader id
        :return: data loader instance
        """
        if loader in self.data_providers:
            return self.data_providers[loader]
        return None

    def update_loader_args(
            self,
            loader: str,
            args: Dict[str, Any]
    ):
        """
        Update loader arguments

        :param loader: loader id
        :param args: keyword arguments
        """
        if loader in self.data_providers:
            self.data_providers[loader].set_args(args)
            reader = self.data_providers[loader]  # get data reader instance
            self.loaders["web"][loader] = reader  # update reader instance

            # update in config
            config = self.window.core.config.get("llama.hub.loaders.args")
            if config is None:
                config = []
            loader_key = "web_" + loader
            for arg in args:
                found = False
                for item in config:
                    if item["loader"] == loader_key and item["name"] == arg:
                        item["value"] = args[arg]
                        found = True
                if not found:
                    type = "str"
                    if arg in self.data_providers[loader].init_args_types:
                        type = self.data_providers[loader].init_args_types[arg]
                    # pack value
                    value = pack_arg(args[arg], type)
                    config.append({
                        "loader": loader_key,
                        "name": arg,
                        "value": value,
                        "type": type
                    })

    def reload_loaders(self):
        """Reload loaders (update arguments)"""
        self.window.core.idx.log("Reloading data loaders...")
        for loader in self.data_providers.values():
            self.register_loader(loader)
        self.window.core.idx.log("Data loaders reloaded.")

    def get_external_instructions(self) -> Dict[str, Any]:
        """
        Get external instructions

        :return: dict of external instructions
        """
        return self.external_instructions

    def get_external_config(self) -> Dict[str, Any]:
        """
        Get external config

        :return: dict of external config
        """
        return self.external_config

    def get_online_loader(self, ext: str):
        """
        Get online loader by extension (deprecated)

        :param ext: file extension
        """
        loaders = self.window.core.config.get("llama.hub.loaders")
        if loaders is None or not isinstance(loaders, list):
            return None
        ext = ext.lower()
        for loader in loaders:
            check = loader["ext"].lower()
            if "," in check:
                extensions = check.replace(" ", "").split(",")
            else:
                extensions = [check.strip()]
            if ext in extensions:
                return loader["loader"]

    def get_data_providers(self) -> Dict[str, BaseLoader]:
        """
        Get data providers

        :return: dict of data providers (loaders)
        """
        return self.data_providers

    def get_loader_arguments(
            self,
            id: str,
            type: str = "file"
    ) -> Dict[str, Any]:
        """
        Get keyword arguments for loader

        :param id: loader id
        :param type: loader type (file, web)
        :return: dict of keyword arguments
        """
        name = type + "_" + id
        args = {}
        data = self.window.core.config.get("llama.hub.loaders.args")
        if isinstance(data, list):
            data_args = []
            # collect keyword arguments for loader
            for item in data:
                if item["loader"] == name:
                    data_args.append(item)
            args = parse_args(data_args)  # parse arguments
        return args

    def is_excluded(self, ext: str) -> bool:
        """
        Check if extension is excluded

        :param ext: file extension
        :return: True if excluded
        """
        if ext in self.loaders["file"]:
            if not self.window.core.config.get("llama.idx.excluded.force"):
                return False

        excluded = self.window.core.config.get("llama.idx.excluded.ext")
        if excluded is not None and excluded != "":
            excluded = excluded.replace(" ", "").split(",")
            if ext.lower() in excluded:
                return True
        return False

    def is_excluded_path(self, path: str) -> bool:
        """
        Check if path is excluded

        :param path: file path
        :return: True if excluded
        """
        data_dir = self.window.core.config.get_user_dir("data")
        # interpreter files
        excluded = [
            os.path.join(data_dir, ".interpreter.output.py"),
            os.path.join(data_dir, ".interpreter.input.py"),
            os.path.join(data_dir, ".interpreter.current.py"),
            os.path.join(data_dir, ".interpreter.kernel.json"),
            os.path.join(data_dir, ".canvas.html"),
        ]
        if path in excluded:
            return True
        return False

    def is_allowed(self, path: str) -> bool:
        """
        Check if path is allowed for indexing

        :param path: file path
        :return: True if allowed
        """
        if os.path.isdir(path):
            return True
        ext = os.path.splitext(path)[1][1:]  # get extension
        ext = ext.lower()
        if self.is_excluded_path(path):
            return False
        if ext in self.loaders["file"] and not self.window.core.config.get("llama.idx.excluded.force"):
            return True
        if self.is_excluded(ext):
            return False
        return True

    def get_documents(
            self,
            path: str,
            force: bool = False,
            silent: bool = False,
            loader_kwargs: Optional[Dict[str, Any]] = None,
    ) -> List[Document]:
        """
        Get documents from path using data loaders

        :param path: path to data
        :param force: force reading
        :param silent: disable logging
        :param loader_kwargs: additional keyword arguments for loader
        :return: list of documents
        """
        # TODO: if .zip then unpack here, and return path to /tmp
        if not silent:
            self.window.core.idx.log(f"Reading documents from path: {path}")
        if os.path.isdir(path):
            reader = SimpleDirectoryReader(
                input_dir=path,
                recursive=True,
                exclude_hidden=False,
            )
            documents = reader.load_data()
        else:
            # get extension
            ext = os.path.splitext(path)[1][1:].lower()

            # check if not excluded extension
            if self.is_excluded(ext) and not force:
                if not silent:
                    self.window.core.idx.log(f"Ignoring excluded extension: {ext}")
                return []

            # check if not excluded path
            if self.is_excluded_path(path) and not force:
                if not silent:
                    self.window.core.idx.log(f"Ignoring excluded path: {path}")
                return []

            # check if archive (zip, tar)
            if self.window.core.filesystem.packer.is_archive(path):
                tmp_path = self.window.core.filesystem.packer.unpack(path)
                if tmp_path:
                    return self.get_documents(tmp_path, force=force, silent=silent, loader_kwargs=loader_kwargs)

            if ext in self.loaders["file"]:
                if not silent:
                    self.window.core.idx.log(f"Using loader for: {ext}")
                reader = self.loaders["file"][ext].get()  # get data reader instance

                # use custom loader method if available
                if hasattr(reader, "load_data_custom") and loader_kwargs:
                    documents = reader.load_data_custom(file=Path(path), **loader_kwargs)
                else:
                    documents = reader.load_data(file=Path(path))
            else:
                if not silent:
                    self.window.core.idx.log(f"Using default SimpleDirectoryReader for: {ext}")
                reader = SimpleDirectoryReader(input_files=[path])
                documents = reader.load_data()

        # append custom metadata
        self.window.core.idx.metadata.append_file_metadata(documents, path)
        return documents

    def read_text_content(
            self,
            path: str,
            loader_kwargs: Optional[Dict[str, Any]] = None
    ) -> Tuple[str, List[Document]]:
        """
        Get content from file using loaders

        :param path: path to file
        :param loader_kwargs: additional keyword arguments for data loader
        :return: text content, list of documents
        """
        docs = self.get_documents(
            path,
            force=True,  # allow excluded extensions
            silent=True,
            loader_kwargs=loader_kwargs,
        )
        data = []
        for doc in docs:
            data.append(doc.text)
        return "\n".join(data), docs

    def read_web_content(
            self,
            url: str,
            type: str = "webpage",
            extra_args: Optional[Dict[str, Any]] = None
    ) -> Tuple[str, List[Document]]:
        """
        Get content from external resource

        :param url: external url to index
        :param type: type of URL (webpage, feed, etc.)
        :param extra_args: extra arguments for loader
        :return: text content, list of documents
        """
        docs = self.read_web(url, type, extra_args)
        data = []
        for doc in docs:
            data.append(doc.text)
        return "\n".join(data), docs

    def read_web(
            self,
            url: str,
            type: str = "webpage",
            extra_args: Optional[Dict[str, Any]] = None,
    ) -> List[Document]:
        """
        Read data from external resource

        :param url: external url to index
        :param type: type of URL (webpage, feed, etc.)
        :param extra_args: extra arguments for loader
        :return: list of documents
        """
        documents = []

        # check if web loader for defined type exists
        if type not in self.loaders["web"]:
            raise ValueError("No web loader for type: {}".format(type))

        try:
            if "url" not in extra_args:
                extra_args["url"] = url

            # get unique external content identifier
            unique_id = self.data_providers[type].get_external_id(extra_args)
            self.window.core.idx.log(f"Loading web documents from: {unique_id}")
            self.window.core.idx.log(f"Using web loader for type: {type}")

            args = self.data_providers[type].prepare_args(**extra_args)

            # get documents from external resource
            documents = self.loaders["web"][type].get().load_data(
                **args
            )
        except Exception as e:
            self.window.core.debug.log(e)
        return documents

    def prepare_document(self, doc: Document):
        """
        Prepare document to store

        :param doc: Document
        """
        # fix empty date in Pinecode
        if "last_accessed_date" in doc.metadata and doc.metadata["last_accessed_date"] is None:
            if "creation_date" in doc.metadata:
                doc.metadata["last_accessed_date"] = doc.metadata["creation_date"]

    def index_files(
            self,
            idx: str,
            index: BaseIndex,
            path: Optional[str] = None,
            is_tmp: bool = False,
            replace: Optional[bool] = None,
            recursive: Optional[bool] = None
    ) -> Tuple[dict, list]:
        """
        Index all files in directory

        :param idx: index name
        :param index: index instance
        :param path: path to file or directory
        :param is_tmp: True if temporary index
        :param replace: True if replace old document
        :param recursive: True if recursive indexing
        :return: dict with indexed files, errors
        """
        if recursive is not None:
            if recursive:
                return self.index_files_recursive(idx, index, path, is_tmp, replace)
        else:
            if self.window.core.config.get("llama.idx.recursive"):
                return self.index_files_recursive(idx, index, path, is_tmp, replace)

        indexed = {}
        errors = []
        files = []
        if os.path.isdir(path):
            files = [os.path.join(path, f)
                     for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        elif os.path.isfile(path):
            files = [path]

        for file in files:   # per file to allow use of multiple loaders
            try:
                if self.is_stopped():  # force stop
                    break

                # force replace or not old document
                if replace is not None:
                    if replace:
                        file_id = self.window.core.idx.files.get_id(file)
                        self.remove_old_file(idx, file_id, force=True)
                else:
                    # if auto, only replace if not temporary
                    if not is_tmp:
                        file_id = self.window.core.idx.files.get_id(file)
                        self.remove_old_file(idx, file_id)

                # index new version of file
                documents = self.get_documents(file)
                for d in documents:
                    if self.is_stopped():  # force stop
                        break

                    self.prepare_document(d)
                    self.index_document(index, d)
                    indexed[file] = d.id_  # add to index
                    self.window.core.idx.log(f"Inserted document: {d.id_}, metadata: {d.metadata}")
            except Exception as e:
                errors.append(str(e))
                print(f"Error while indexing file: {file}")
                self.window.core.debug.log(e)
                if self.stop_enabled():
                    break  # break loop if error

        return indexed, errors

    def index_files_recursive(
            self,
            idx: str,
            index: BaseIndex,
            path: Optional[str] = None,
            is_tmp: bool = False,
            replace: Optional[bool] = None
    ) -> Tuple[dict, list]:
        """
        Index all files in directory and subdirectories recursively.

        :param idx: index name
        :param index: index instance
        :param path: path to file or directory
        :param is_tmp: True if temporary index
        :param replace: True if replace old document
        :return: dict with indexed files, errors
        """
        indexed = {}
        errors = []
        is_break = False

        # directory
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        # remove old file from index if exists
                        file_id = self.window.core.idx.files.get_id(file_path)

                        if self.is_stopped():  # force stop
                            break

                        # force replace or not old document
                        if replace is not None:
                            if replace:
                                self.remove_old_file(idx, file_id, force=True)
                        else:
                            # if auto, only replace if not temporary
                            if not is_tmp:
                                self.remove_old_file(idx, file_id)

                        # index new version of file
                        documents = self.get_documents(file_path)
                        for d in documents:
                            if self.is_stopped():  # force stop
                                break

                            self.prepare_document(d)
                            self.index_document(index, d)
                            indexed[file_path] = d.id_  # add to index
                            self.window.core.idx.log(f"Inserted document: {d.id_}, metadata: {d.metadata}")
                    except Exception as e:
                        errors.append(str(e))
                        print(f"Error while indexing file: {file_path}")
                        self.window.core.debug.log(e)
                        if self.stop_enabled():
                            is_break = True
                            break  # break loop if error

                if is_break or self.is_stopped():
                    break  # stop os.walk if error or forced stop

        # file
        elif os.path.isfile(path):
            try:
                # remove old file from index if exists
                file_id = self.window.core.idx.files.get_id(path)

                # force replace or not old document
                if replace is not None:
                    if replace:
                        self.remove_old_file(idx, file_id, force=True)
                else:
                    # if auto, only replace if not temporary
                    if not is_tmp:
                        self.remove_old_file(idx, file_id)

                # index new version of file
                documents = self.get_documents(path)
                for d in documents:
                    if self.is_stopped():  # force stop
                        break

                    self.prepare_document(d)
                    self.index_document(index, d)
                    indexed[path] = d.id_  # add to index
                    self.window.core.idx.log(f"Inserted document: {d.id_}, metadata: {d.metadata}")
            except Exception as e:
                errors.append(str(e))
                print(f"Error while indexing file: {path}")
                self.window.core.debug.log(e)

        return indexed, errors

    def get_db_data_from_ts(
            self,
            updated_ts: int = 0
    ) -> List[Document]:
        """
        Get data from database from timestamp

        :param updated_ts: timestamp
        :return: list of documents
        """
        db = self.window.core.db.get_db()
        documents = []
        query = f"""
        SELECT
            'Human: ' || ctx_item.input || '\nAssistant: ' || ctx_item.output AS text,
            ctx_item.input_ts AS input_ts,
            ctx_item.meta_id AS meta_id,
            ctx_item.id AS item_id
        FROM 
            ctx_item
        LEFT JOIN
            ctx_meta
        ON
            ctx_item.meta_id = ctx_meta.id
        WHERE
            ctx_meta.updated_ts > {updated_ts}
        """
        with db.connect() as connection:
            result = connection.execute(text(query))
            for item in result.fetchall():
                data = item._asdict()
                doc = Document(
                    text=data["text"],
                    metadata={
                        "ctx_date": str(datetime.datetime.fromtimestamp(int(data["input_ts"]))),
                        "ctx_id": data["meta_id"],
                        "item_id": data["item_id"],
                        "indexed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )
                documents.append(doc)
        return documents

    def get_db_meta_ids_from_ts(
            self,
            updated_ts: int = 0
    ) -> List[int]:
        """
        Get IDs of meta from database from timestamp

        :param updated_ts: timestamp
        :return: list of IDs
        """
        db = self.window.core.db.get_db()
        ids = []
        query = f"""
        SELECT
            id
        FROM 
            ctx_meta
        WHERE
            ctx_meta.updated_ts > {updated_ts}
        """
        with db.connect() as connection:
            result = connection.execute(text(query))
            for row in result.fetchall():
                data = row._asdict()
                ids.append(data["id"])
        return ids

    def get_db_data_by_id(
            self,
            id: int = 0,
            updated_ts: int = 0
    ) -> List[Document]:
        """
        Get data from database by meta id

        :param id: ctx meta id
        :param updated_ts: timestamp from which to get data
        :return: list of documents
        """
        db = self.window.core.db.get_db()
        documents = []
        query = f"""
        SELECT
            'Human: ' || input || '\nAssistant: ' || output AS text,
            input_ts AS input_ts,
            meta_id AS meta_id,
            id AS item_id
        FROM ctx_item
        WHERE meta_id = {id}
        """
        # restrict to updated data if from timestamp is given
        if updated_ts > 0:
            query += f" AND (input_ts > {updated_ts} OR output_ts > {updated_ts})"
        with db.connect() as connection:
            result = connection.execute(text(query))
            for item in result.fetchall():
                data = item._asdict()
                doc = Document(
                    text=data["text"],
                    metadata={
                        "ctx_date": str(datetime.datetime.fromtimestamp(int(data["input_ts"]))),
                        "ctx_id": data["meta_id"],
                        "item_id": data["item_id"],
                        "indexed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )
                documents.append(doc)
        return documents

    def index_db_by_meta_id(
            self,
            idx: str,
            index: BaseIndex,
            id: int = 0,
            from_ts: int = 0
    ) -> Tuple[int, List[str]]:
        """
        Index data from database by meta id

        :param idx: index name
        :param index: index instance
        :param id: ctx meta id
        :param from_ts: timestamp from which to index
        :return: number of indexed documents, errors
        """
        errors = []
        n = 0
        try:
            # remove old document from index if indexing by ID only and not from timestamp
            if from_ts == 0:
                self.window.core.idx.log(f"Indexing documents from database by meta id: {id}")
                self.remove_old_meta_id(idx, id)
            elif from_ts > 0:
                self.window.core.idx.log(f"Indexing documents from database by meta id: {id} from timestamp: {from_ts}")

            # get items from database
            documents = self.get_db_data_by_id(id, from_ts)
            for d in documents:
                if self.is_stopped():  # force stop
                    break

                self.index_document(index, d)
                doc_id = d.id_
                self.window.core.idx.log(f"Inserted ctx DB document: {n+1} / {len(documents)}, id: {d.id_}, metadata: {d.metadata}")
                self.window.core.ctx.idx.set_meta_as_indexed(id, idx, doc_id)  # update ctx
                n += 1
        except Exception as e:
            errors.append(str(e))
            self.window.core.debug.log(e)
        return n, errors

    def index_db_from_updated_ts(
            self,
            idx: str,
            index: BaseIndex,
            from_ts: int = 0
    ) -> Tuple[int, List[str]]:
        """
        Index data from database from timestamp

        :param idx: index name
        :param index: index instance
        :param from_ts: timestamp
        :return: number of indexed documents, errors
        """
        self.window.core.idx.log(f"Indexing documents from database from timestamp: {from_ts}")
        errors = []
        n = 0
        ids = self.get_db_meta_ids_from_ts(from_ts)
        for id in ids:
            if self.is_stopped():  # force stop
                break

            indexed, errs = self.index_db_by_meta_id(idx, index, id, from_ts)
            n += indexed
            errors.extend(errs)
        return n, errors

    def index_url(
            self,
            idx: str,
            index: BaseIndex,
            url: str,
            type="webpage",
            extra_args: Optional[Dict[str, Any]] = None,
            is_tmp: bool = False,
            replace: Optional[bool] = None
    ) -> Tuple[int, List[str]]:
        """
        Index data from external (remote) resource

        :param idx: index name
        :param index: index instance
        :param url: external url to index
        :param type: type of URL (webpage, feed, etc.)
        :param extra_args: extra arguments for loader
        :param is_tmp: True if temporary index
        :param replace: True if force replace old document
        :return: number of indexed documents, errors
        """
        errors = []
        n = 0

        # check if web loader for defined type exists
        if type not in self.loaders["web"]:
            raise ValueError(f"No web loader for type: {type}")

        try:
            # remove old content from index if already indexed
            loader = self.loaders["web"][type].get()

            # additional keyword arguments for data loader
            if extra_args is None:
                extra_args = {}

            # override URL if provided in load_data args
            if "url" not in extra_args:
                extra_args["url"] = url

            # get unique external content identifier
            unique_id = self.data_providers[type].get_external_id(extra_args)

            # remove old document from index
            if replace is not None:
                if replace:
                    self.remove_old_external(idx, unique_id, type, force=True)
            else:
                # if auto, only replace if not temporary
                if not is_tmp:
                    self.remove_old_external(idx, unique_id, type)

            self.window.core.idx.log(f"Loading web documents from: {unique_id}")
            self.window.core.idx.log(f"Using web loader for type: {type}")

            args = self.data_providers[type].prepare_args(**extra_args)

            # get documents from external resource
            documents = loader.load_data(
                **args
            )

            # append custom metadata
            self.window.core.idx.metadata.append_web_metadata(documents, type, args)

            for d in documents:
                if self.is_stopped():  # force stop
                    break

                self.index_document(index, d)
                doc_id = d.id_  # URL is used as document ID
                if not is_tmp:
                    self.window.core.idx.external.set_indexed(
                        content=unique_id,
                        type=type,
                        idx=idx,
                        doc_id=doc_id,
                    )  # update external index
                self.window.core.idx.log(f"Inserted web document: {n+1} / {len(documents)}, id: {d.id_}, metadata: {d.metadata}")
                n += 1
        except Exception as e:
            errors.append(str(e))
            self.window.core.debug.log(e)
        return n, errors

    def index_urls(
            self,
            idx: str,
            index: BaseIndex,
            urls: list,
            type="webpage",
            extra_args: Optional[Dict[str, Any]] = None,
            is_tmp: bool = False
    ) -> Tuple[int, List[str]]:
        """
        Index data from URLs

        :param idx: index name
        :param index: index instance
        :param urls: list of urls
        :param type: type of URL (webpage, feed, etc.)
        :param extra_args: extra arguments for loader
        :param is_tmp: True if temporary index
        :return: number of indexed documents, errors
        """
        errors = []
        n = 0

        # check if web loader for defined type exists
        if type not in self.loaders["web"]:
            msg = f"No web loader for type: {type}"
            errors.append(msg)
            self.window.core.debug.log(msg)
            return n, errors

        for url in urls:
            if self.is_stopped():  # force stop
                break

            indexed, errs = self.index_url(
                idx=idx,
                index=index,
                url=url,
                type=type,
                extra_args=extra_args,
                is_tmp=is_tmp,
            )
            n += indexed
            errors.extend(errs)
        return n, errors

    def remove_old_meta_id(
            self,
            idx: str,
            id: int = 0,
            force: bool = False
    ) -> bool:
        """
        Remove old meta id from index

        :param idx: index name
        :param id: ctx meta id
        :param force: force remove
        :return: True if removed, False if not
        """
        # abort if not configured to replace old documents
        if not self.window.core.config.get("llama.idx.replace_old") and not force:
            return False

        store = self.window.core.idx.get_current_store()
        if self.window.core.idx.ctx.exists(store, idx, id):
            doc_id = self.window.core.idx.ctx.get_doc_id(store, idx, id)
            if doc_id:
                self.window.core.idx.log(f"Removing old document id: {doc_id}")
                try:
                    self.window.core.idx.storage.remove_document(
                        id=idx,
                        doc_id=doc_id,
                    )
                except Exception as e:
                    self.window.core.debug.log(e)
                return True
        return False

    def remove_old_file(
            self,
            idx: str,
            file_id: str,
            force: bool = False
    ) -> bool:
        """
        Remove old file from index

        :param idx: index name
        :param file_id: file id
        :param force: force remove
        :return: True if removed, False if not
        """
        # abort if not configured to replace old documents
        if not self.window.core.config.get("llama.idx.replace_old") and not force:
            return False

        store = self.window.core.idx.get_current_store()
        if self.window.core.idx.files.exists(store, idx, file_id):
            doc_id = self.window.core.idx.files.get_doc_id(store, idx, file_id)
            if doc_id:
                self.window.core.idx.log(f"Removing old document id: {doc_id}")
                try:
                    self.window.core.idx.storage.remove_document(
                        id=idx,
                        doc_id=doc_id,
                    )
                except Exception as e:
                    self.window.core.debug.log(e)
                return True
        return False

    def remove_old_external(
            self,
            idx: str,
            content: str,
            type: str,
            force: bool = False
    ) -> bool:
        """
        Remove old file from index

        :param idx: index name
        :param content: content
        :param type: type
        :param force: force remove
        :return: True if removed, False if not
        """
        # abort if not configured to replace old documents
        if not self.window.core.config.get("llama.idx.replace_old") and not force:
            return False

        store = self.window.core.idx.get_current_store()
        if self.window.core.idx.external.exists(store, idx, content, type):
            doc_id = self.window.core.idx.external.get_doc_id(store, idx, content, type)
            if doc_id:
                self.window.core.idx.log(f"Removing old document id: {doc_id}")
                try:
                    self.window.core.idx.storage.remove_document(
                        id=idx,
                        doc_id=doc_id,
                    )
                except Exception as e:
                    self.window.core.debug.log(e)
                return True
        return False

    def index_document(
            self,
            index: BaseIndex,
            doc: Document
    ):
        """
        Index document

        :param index: index instance
        :param doc: document
        """
        self.apply_rate_limit()  # apply RPM limit
        """
        try:
            # display embedding model info
            if index._embed_model is not None:
                self.window.core.idx.log("Embedding model: {}".format(index.service_context.embed_model.model_name))
        except Exception as e:
            self.window.core.debug.log(e)
        """
        index.insert(document=doc)

    def index_attachment(
            self,
            file_path: str,
            index_path: str,
            model: Optional[ModelItem] = None,
            documents: Optional[List[Document]] = None,
    ) -> list:
        """
        Index context attachment

        :param file_path: path to file to index
        :param index_path: index path
        :param model: model
        :param documents: list of documents (optional)
        :return: response
        """
        if model is None:
            model = self.window.core.models.from_defaults()

        llm, embed_model = self.window.core.idx.llm.get_service_context(model=model, stream=False, auto_embed=True)
        index = self.window.core.idx.storage.get_ctx_idx(
            index_path,
            llm=llm,
            embed_model=embed_model,
        )  # get or create ctx index

        idx = f"tmp:{index_path}"  # tmp index id
        self.window.core.idx.log(f"Indexing to context attachment index: {idx}... using model: {model.id}")

        doc_ids = []
        if documents is None:
            documents = self.get_documents(file_path)
        for d in documents:
            if self.is_stopped():  # force stop
                break
            self.prepare_document(d)
            self.index_document(index, d)
            doc_ids.append(d.id_)  # add to index

        self.window.core.idx.storage.store_ctx_idx(index_path, index)
        return doc_ids

    def index_attachment_web(
            self,
            url: str,
            index_path: str,
            model: Optional[ModelItem] = None,
            documents: Optional[List[Document]] = None,
    ) -> list:
        """
        Index context attachment

        :param url: URL to index
        :param index_path: index path
        :param model: model
        :param documents: list of documents (optional)
        :return: response
        """
        if model is None:
            model = self.window.core.models.from_defaults()

        llm, embed_model = self.window.core.idx.llm.get_service_context(model=model, stream=False, auto_embed=True)
        index = self.window.core.idx.storage.get_ctx_idx(index_path, llm, embed_model)  # get or create ctx index

        idx = f"tmp:{index_path}"  # tmp index id
        self.window.core.idx.log(f"Indexing to context attachment index: {idx}...")

        web_type = self.get_webtype(url)
        doc_ids = []
        if documents is None:
            documents = self.read_web(
                url=url,
                type=web_type,
                extra_args={},
            )
        for d in documents:
            if self.is_stopped():  # force stop
                break
            self.prepare_document(d)
            self.index_document(index, d)
            doc_ids.append(d.id_)  # add to index

        self.window.core.idx.storage.store_ctx_idx(index_path, index)
        return doc_ids

    def get_webtype(self, url: str) -> str:
        """
        Get web loader type by URL

        :param url: URL
        :return: web loader type
        """
        type = "webpage"  # default
        for id in self.data_providers:
            loader = self.data_providers[id]
            if hasattr(loader, "is_supported_attachment"):
                if loader.is_supported_attachment(url):
                    type = id
                    break
        print(f"Selected web data loader: {type}")
        return type

    def remove_attachment(
            self,
            index_path: str,
            doc_id: str
    ) -> bool:
        """
        Remove document from index

        :param index_path: index path
        :param doc_id: document ID
        :return: True if success
        """
        model = self.window.core.models.from_defaults()
        llm, embed_model = self.window.core.idx.llm.get_service_context(model=model, stream=False)
        index = self.window.core.idx.storage.get_ctx_idx(index_path, llm, embed_model)  # get or create ctx index
        index.delete_ref_doc(doc_id)
        self.window.core.idx.storage.store_ctx_idx(index_path, index)
        return True

    def apply_rate_limit(self):
        """Apply API calls RPM limit"""
        max_per_minute = 60
        if self.window.core.config.has("llama.idx.embeddings.limit.rpm"):
            max_per_minute = int(self.window.core.config.get("llama.idx.embeddings.limit.rpm")) # per minute
        if max_per_minute <= 0:
            return
        interval = datetime.timedelta(minutes=1) / max_per_minute
        now = datetime.datetime.now()
        if self.last_call is not None:
            time_since_last_call = now - self.last_call
            if time_since_last_call < interval:
                sleep_time = (interval - time_since_last_call).total_seconds()
                self.window.core.idx.log(f"RPM limit: sleep for {sleep_time} seconds")
                time.sleep(sleep_time)
        self.last_call = now

    def stop_enabled(self) -> bool:
        """
        Check if stop on error is enabled

        :return: True if enabled
        """
        return self.window.core.config.get('llama.idx.stop.error')

    def is_stopped(self) -> bool:
        """
        Check if indexing is stopped

        :return: True if stopped
        """
        return self.window.controller.idx.is_stopped()
