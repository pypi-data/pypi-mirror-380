#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.26 17:00:00                  #
# ================================================== #

from typing import Dict, Any, Tuple, Optional

from agents import (
    Agent as OpenAIAgent,
    Runner,
)

from pygpt_net.core.agents.bridge import ConnectionContext
from pygpt_net.core.bridge import BridgeContext
from pygpt_net.core.types import (
    AGENT_MODE_OPENAI,
    AGENT_TYPE_OPENAI,
)

from pygpt_net.item.ctx import CtxItem
from pygpt_net.item.model import ModelItem

from pygpt_net.provider.api.openai.agents.remote_tools import is_computer_tool, append_tools
from pygpt_net.provider.api.openai.agents.computer import Agent as ComputerAgent, LocalComputer
from pygpt_net.provider.api.openai.agents.response import StreamHandler
from pygpt_net.provider.api.openai.agents.experts import get_experts

from ..base import BaseAgent

class Agent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super(Agent, self).__init__(*args, **kwargs)
        self.id = "openai_agent_base"
        self.type = AGENT_TYPE_OPENAI
        self.mode = AGENT_MODE_OPENAI
        self.name = "Simple agent"

    def get_agent(self, window, kwargs: Dict[str, Any]):
        """
        Return Agent provider instance

        :param window: window instance
        :param kwargs: keyword arguments
        :return: Agent provider instance
        """
        context = kwargs.get("context", BridgeContext())
        preset = context.preset
        system_prompt = kwargs.get("system_prompt", "")
        agent_name = preset.name if preset else "Agent"
        model = kwargs.get("model", ModelItem())
        tools = kwargs.get("function_tools", [])
        handoffs = kwargs.get("handoffs", [])
        kwargs = {
            "name": agent_name,
            "instructions": system_prompt,
            "model": window.core.agents.provider.get_openai_model(model),
        }
        if handoffs:
            kwargs["handoffs"] = handoffs

        tool_kwargs = append_tools(
            tools=tools,
            window=window,
            model=model,
            preset=preset,
            allow_local_tools=True,
            allow_remote_tools=True,
        )
        kwargs.update(tool_kwargs)  # update kwargs with tools
        return OpenAIAgent(**kwargs)

    async def run(
            self,
            window: Any = None,
            agent_kwargs: Dict[str, Any] = None,
            previous_response_id: str = None,
            messages: list = None,
            ctx: CtxItem = None,
            stream: bool = False,
            bridge: ConnectionContext = None,
            use_partial_ctx: Optional[bool] = False,
    ) -> Tuple[CtxItem, str, str]:
        """
        Run agent (async)

        :param window: Window instance
        :param agent_kwargs: Additional agent parameters
        :param previous_response_id: ID of the previous response (if any)
        :param messages: Conversation messages
        :param ctx: Context item
        :param stream: Whether to stream output
        :param bridge: Connection context for agent operations
        :param use_partial_ctx: Use partial ctx per cycle
        :return: Current ctx, final output, last response ID
        """
        final_output = ""
        response_id = None
        model = agent_kwargs.get("model", ModelItem())
        verbose = agent_kwargs.get("verbose", False)
        tools = agent_kwargs.get("function_tools", [])
        context = agent_kwargs.get("context", BridgeContext())
        preset = context.preset if context else None

        # add experts
        experts = get_experts(
            window=window,
            preset=preset,
            verbose=verbose,
            tools=tools,
        )
        if experts:
            agent_kwargs["handoffs"] = experts

        agent = self.get_agent(window, agent_kwargs)
        max_steps = agent_kwargs.get("max_iterations", 10)
        kwargs = {
            "input": messages,
            "max_turns": int(max_steps),
        }
        if model.provider == "openai":
            if previous_response_id:
                kwargs["previous_response_id"] = previous_response_id

        tool_kwargs = {
            "window": window,
            "model": model,
            "preset": preset,
            "is_expert_call": False,
        }

        ctx.set_agent_name(agent.name)
        # call computer agent if computer tool is enabled
        if is_computer_tool(**tool_kwargs):
            computer = LocalComputer(window)
            agent = ComputerAgent(
                computer=computer,
                ctx=ctx,
                stream=stream,
                bridge=bridge,
            )
            items = messages
            output_items, response_id = agent.run(
                input=items,
                debug=verbose,
            )
            if output_items[-1]["type"] == "message":
                if verbose:
                    print("Final response:", response_id, output_items[-1])
                final_output = output_items[-1]["content"][0]["text"]

        # call default agent
        else:
            if not stream:
                result = await Runner.run(
                    agent,
                    **kwargs
                )
                final_output, last_response_id = window.core.api.openai.responses.unpack_agent_response(result, ctx)
                response_id = result.last_response_id
                if verbose:
                    print("Final response:", result)
            else:
                result = Runner.run_streamed(
                    agent,
                    **kwargs
                )
                handler = StreamHandler(window, bridge)
                async for event in result.stream_events():
                    if bridge.stopped():
                        result.cancel()
                        bridge.on_stop(ctx)
                        break
                    final_output, response_id = handler.handle(event, ctx)

        return ctx, final_output, response_id


