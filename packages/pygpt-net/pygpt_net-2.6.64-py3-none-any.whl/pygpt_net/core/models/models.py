#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.17 19:00:00                  #
# ================================================== #

import copy
from typing import Optional, List, Dict

from httpx_socks import SyncProxyTransport
from openai import DefaultHttpxClient
from packaging.version import Version

from pygpt_net.core.types import (
    MODE_CHAT,
    MODE_LANGCHAIN,
    MODE_LLAMA_INDEX,
    MODE_RESEARCH,
    MULTIMODAL_TEXT,
    MULTIMODAL_IMAGE,
    MULTIMODAL_AUDIO,
    MULTIMODAL_VIDEO,
    MODEL_DEFAULT_MINI,
)
from pygpt_net.item.model import ModelItem
from pygpt_net.provider.core.model.json_file import JsonFileProvider

from .ollama import Ollama

class Models:
    def __init__(self, window=None):
        """
        Models core

        :param window: Window instance
        """
        self.window = window
        self.provider = JsonFileProvider(window)
        self.ollama = Ollama(window)
        self.default = MODEL_DEFAULT_MINI
        self.items = {}
        self.multimodal = [
            MULTIMODAL_TEXT,
            MULTIMODAL_IMAGE,
            MULTIMODAL_AUDIO,
            MULTIMODAL_VIDEO,
        ]

    def install(self):
        """Install provider data"""
        self.provider.install()

    def patch(self, app_version: Version) -> bool:
        """
        Patch provider data

        :param app_version: app version
        :return: True if data was patched
        """
        return self.provider.patch(app_version)

    def patch_missing(self) -> bool:
        """
        Patch missing models

        :return: True if models were patched
        """
        base_items = self.get_base()
        updated = False

        for key, base in base_items.items():
            if key not in self.items:
                self.items[key] = copy.deepcopy(base)
                updated = True

        existing_ids = {it.id for it in self.items.values()}
        for key, base in base_items.items():
            if base.id not in existing_ids:
                self.items[key] = copy.deepcopy(base)
                existing_ids.add(base.id)
                updated = True

        for key, base in base_items.items():
            item = self.items.get(key)
            if not item:
                continue
            if base.input != item.input:
                item.input = base.input
                updated = True
            if base.output != item.output:
                item.output = base.output
                updated = True

        for item in self.items.values():
            if isinstance(item.input, list) and not item.input:
                item.input = ["text"]
                updated = True
            if isinstance(item.output, list) and not item.output:
                item.output = ["text"]
                updated = True

        if updated:
            self.save()

        return updated

    def from_base(self, key: str) -> Optional[ModelItem]:
        """
        Get model from base models

        :param key: model name
        :return: model config object or None
        """
        items = self.get_base()
        return items.get(key)

    def get(self, key: str) -> ModelItem:
        """
        Return model config

        :param key: model name
        :return: model config object
        """
        return self.items.get(key)

    def get_ids(self) -> List[str]:
        """
        Return models ids

        :return: model ids list
        """
        return list(self.items.keys())

    def get_id_by_idx_all(self, idx: int) -> str:
        """
        Return model id by index

        :param idx: model idx
        :return: model id
        """
        return list(self.items.keys())[idx]

    def has(self, model: str) -> bool:
        """
        Check if model exists

        :param model: model name
        :return: True if model exists
        """
        return model in self.items

    def is_allowed(
            self,
            model: str,
            mode: str
    ) -> bool:
        """
        Check if model is allowed for mode

        :param model: model name
        :param mode: mode name
        :return: True if model is allowed for mode
        """
        return model in self.items and mode in self.items[model].mode

    def get_id(
            self,
            key: str
    ) -> str:
        """
        Return model internal ID

        :param key: model key
        :return: model id
        """
        item = self.items.get(key)
        return item.id if item else None

    def get_by_idx(
            self,
            idx: int,
            mode: str
    ) -> str:
        """
        Return model by index

        :param idx: model idx
        :param mode: mode name
        :return: model name
        """
        items = self.get_by_mode(mode)
        return list(items.keys())[idx]

    def get_by_mode(
            self,
            mode: str
    ) -> Dict[str, ModelItem]:
        """
        Return models for mode

        :param mode: mode name
        :return: models dict for mode
        """
        return {k: v for k, v in self.items.items() if mode in v.mode}

    def get_next(
            self,
            model: str,
            mode: str
    ) -> str:
        """
        Return next model

        :param model: current model
        :param mode: mode name
        :return: next model
        """
        items = self.get_by_mode(mode)
        keys = list(items.keys())
        idx = keys.index(model)
        if idx + 1 < len(keys):
            return keys[idx + 1]
        return keys[0]

    def get_prev(
            self,
            model: str,
            mode: str
    ) -> str:
        """
        Return previous model

        :param model: current model
        :param mode: mode name
        :return: previous model
        """
        items = self.get_by_mode(mode)
        keys = list(items.keys())
        idx = keys.index(model)
        if idx - 1 >= 0:
            return keys[idx - 1]
        return keys[-1]

    def create_id(self):
        """
        Create new model id

        :return: new model id
        """
        prefix = "model-"
        used = set()
        for k in self.items.keys():
            if isinstance(k, str) and k.startswith(prefix):
                suffix = k[len(prefix):]
                if suffix.isdigit():
                    used.add(int(suffix))
        n = 0
        while n in used:
            n += 1
        return f"{prefix}{n:03d}"

    def get_multimodal_list(self) -> List[str]:
        """
        Return available multimodal types

        :return: list of multimodal types
        """
        return self.multimodal

    def create_empty(self, append: bool = True) -> ModelItem:
        """
        Create new empty model

        :param append: if True, append model to items
        :return: new model

        """
        id = self.create_id()
        model = ModelItem()
        model.id = id
        model.name = "New model"
        model.input = ["text"]
        model.output = ["text"]
        if append:
            self.items[id] = model
        return model

    def get_all(self) -> Dict[str, ModelItem]:
        """
        Return all models

        :return: all models
        """
        return self.items

    def from_defaults(self) -> ModelItem:
        """
        Create default model

        :return: new model
        """
        model = ModelItem()
        model.id = self.default
        model.name = self.default
        model.tokens = 4096
        model.ctx = 128000
        model.input = ["text"]
        model.output = ["text"]
        model.provider = "openai"
        model.mode = ["chat"]
        return model

    def delete(self, model: str):
        """
        Delete model

        :param model: model name
        """
        if model in self.items:
            del self.items[model]

    def has_model(
            self,
            mode: str,
            model: str
    ) -> bool:
        """
        Check if model exists for mode

        :param mode: mode name
        :param model: model name
        :return: True if model exists for mode
        """
        item = self.items.get(model)
        return bool(item and mode in item.mode)

    def get_default(self, mode: str) -> Optional[str]:
        """
        Return default model for mode

        :param mode: mode name
        :return: default model name
        """
        items = self.get_by_mode(mode)
        if not items:
            return None
        return next(iter(items))

    def get_tokens(self, model: str) -> int:
        """
        Return model tokens

        :param model: model name
        :return: number of tokens
        """
        if model in self.items:
            return self.items[model].tokens
        return 1

    def get_num_ctx(self, model: str) -> int:
        """
        Return model context window tokens

        :param model: model name
        :return: number of ctx tokens
        """
        if model in self.items:
            return self.items[model].ctx
        return 4096

    def restore_default(
            self,
            model: Optional[str] = None
    ):
        """
        Restore default models

        :param model: model name
        """
        if model is None:
            self.load_base()
            return

        items = self.provider.load_base()
        if model in items:
            self.items[model] = items[model]

    def get_base(self) -> Dict[str, ModelItem]:
        """
        Get base models

        :return: base models
        """
        return self.provider.load_base()

    def load_base(self):
        """Load models base"""
        self.items = self.get_base()
        self.sort_items()

    def load(self):
        """Load models"""
        self.items = self.provider.load()
        self.sort_items()

    def sort_items(self):
        """Sort items"""
        if self.items:
            self.items = dict(sorted(self.items.items(), key=lambda x: x[1].name.lower()))

    def save(self):
        """Save models"""
        self.provider.save(self.items)

    def get_supported_mode(
            self,
            model: ModelItem,
            mode: str
    ) -> str:
        """
        Get supported mode

        :param model: ModelItem
        :param mode: mode (initial)
        :return: mode (supported)
        """
        prev_mode = mode
        if model.is_supported(MODE_CHAT) and mode != MODE_LLAMA_INDEX:
            if prev_mode != MODE_CHAT:
                self.window.core.debug.info(
                    "WARNING: Switching to chat mode (model not supported in: {})".format(prev_mode))
            return MODE_CHAT

        if model.is_supported(MODE_RESEARCH):
            if prev_mode != MODE_RESEARCH:
                self.window.core.debug.info(
                    "WARNING: Switching to research mode (model not supported in: {})".format(mode))
            mode = MODE_RESEARCH

        elif model.is_supported(MODE_LLAMA_INDEX):
            if prev_mode != MODE_LLAMA_INDEX:
                self.window.core.debug.info(
                    "WARNING: Switching to llama_index mode (model not supported in: {})".format(mode))
            mode = MODE_LLAMA_INDEX

        return mode

    def prepare_client_args(
            self,
            mode: str = MODE_CHAT,
            model: ModelItem = None
    ) -> Dict[str, str]:
        """
        Prepare chat client arguments

        :param mode: mode name
        :param model: ModelItem
        :return: client arguments dict
        """
        cfg = self.window.core.config
        args = {
            "api_key": cfg.get('api_key'),
            "organization": cfg.get('organization_key'),
        }

        if cfg.has('api_endpoint'):
            endpoint = cfg.get('api_endpoint')
            if endpoint:
                args["base_url"] = endpoint

        if cfg.has('api_proxy'):
            proxy = cfg.get('api_proxy')
            if proxy and cfg.get('api_proxy.enabled', False):
                args["api_proxy"] = proxy
                transport = SyncProxyTransport.from_url(proxy)
                args["http_client"] = DefaultHttpxClient(transport=transport)

        if model is not None:
            if model.provider == "x_ai":
                args["api_key"] = cfg.get('api_key_xai', "")
                args["base_url"] = cfg.get('api_endpoint_xai', "")
                self.window.core.debug.info("[api] Using client: xAI")
            elif model.provider == "perplexity":
                args["api_key"] = cfg.get('api_key_perplexity', "")
                args["base_url"] = cfg.get('api_endpoint_perplexity', "")
                self.window.core.debug.info("[api] Using client: Perplexity")
            elif model.provider == "google":
                args["api_key"] = cfg.get('api_key_google', "")
                args["base_url"] = cfg.get('api_endpoint_google', "")
                self.window.core.debug.info("[api] Using client: Google")
            elif model.provider == "anthropic":
                args["api_key"] = cfg.get('api_key_anthropic', "")
                args["base_url"] = cfg.get('api_endpoint_anthropic', "")
                self.window.core.debug.info("[api] Using client: Anthropic")
            elif model.provider == "deepseek_api":
                args["api_key"] = cfg.get('api_key_deepseek', "")
                args["base_url"] = cfg.get('api_endpoint_deepseek', "")
                self.window.core.debug.info("[api] Using client: Deepseek API")
            elif model.provider == "mistral_ai":
                args["api_key"] = cfg.get('api_key_mistral', "")
                args["base_url"] = cfg.get('api_endpoint_mistral', "")
                self.window.core.debug.info("[api] Using client: Mistral AI API")
            elif model.provider == "huggingface_router":
                args["api_key"] = cfg.get('api_key_hugging_face', "")
                args["base_url"] = cfg.get('api_endpoint_hugging_face', "")
                self.window.core.debug.info("[api] Using client: HuggingFace Router API")
            elif model.provider == "open_router":
                args["api_key"] = cfg.get('api_key_open_router', "")
                args["base_url"] = cfg.get('api_endpoint_open_router', "")
                self.window.core.debug.info("[api] Using client: OpenRouter API")
            elif model.provider == "ollama":
                args["api_key"] = "ollama"
                args["base_url"] = self.window.core.models.ollama.get_base_url() + "/v1"
                self.window.core.debug.info("[api] Using client: Ollama")
            else:
                self.window.core.debug.info("[api] Using client: OpenAI (default)")

            if model.provider != "openai":
                if "organization" in args:
                    del args["organization"]
        else:
            self.window.core.debug.info("[api] No model provided, using default OpenAI client")
        return args

    def get_openrouter_model(self, model: ModelItem) -> str:
        """
        Get OpenRouter model by model id

        :param model: ModelItem
        :return: OpenRouter model id
        """
        if isinstance(model, str):
            model = self.get(model)
        if not model or model.provider != "open_router":
            return model.id if model else None

        # OpenRouter: add web search remote tool (if enabled)
        # https://openrouter.ai/docs/features/web-search
        model_id = model.id
        is_web = self.window.controller.chat.remote_tools.enabled(model, "web_search")  # web search config
        if is_web:
            if not model_id.endswith(":online"):
                model_id += ":online"
        else:
            if model_id.endswith(":online"):
                model_id = model_id.replace(":online", "")
        return model_id

    def is_tool_call_allowed(self, mode: str, model: ModelItem) -> bool:
        """
        Check if native tool call is allowed for model and mode

        :param mode: Mode name
        :param model: ModelItem
        :return: True if tool call is allowed, False otherwise
        """
        if mode == MODE_LLAMA_INDEX:
            if model.provider == "google":
                stream = self.window.core.config.get('stream', False)
                use_react = self.window.core.config.get("llama.idx.react", False)
                if stream:
                    return bool(use_react)
        if model.tool_calls:
            return True
        return False

    def get_version(self) -> str:
        """
        Get config version

        :return: config version
        """
        return self.provider.get_version()