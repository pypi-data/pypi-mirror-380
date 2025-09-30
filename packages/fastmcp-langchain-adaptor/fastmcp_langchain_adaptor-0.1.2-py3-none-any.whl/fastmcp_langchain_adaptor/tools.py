"""
FastMCP to LangChain Adaptor

This module provides utilities to convert FastMCP tools into LangChain
StructuredTools, enabling seamless integration between Model Context
Protocol (MCP) servers and LangChain agents.
"""

from __future__ import annotations

import json
import logging
from collections.abc import Callable
from typing import Any

from fastmcp import Client
from fastmcp.client.client import CallToolResult
from fastmcp.tools import Tool as McpTool
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import StructuredTool

logger = logging.getLogger(__name__)


def _create_langchain_tool_from_mcp(
    *,
    tool: McpTool,
    client: Client,
    progress_formatter: Callable[[dict[str, Any]], str] | None = None,
) -> StructuredTool:
    """
    Adapt a single FastMCP tool descriptor to a LangChain StructuredTool.
    Elicitation is handled by the client you constructed (via its elicitation_handler).
    Progress is forwarded to LC callbacks.

    Parameters
    ----------
    tool : McpTool
        The MCP tool descriptor.
    client : Client
        The FastMCP client configured with elicitation/progress handlers.
    progress_formatter : Callable, optional
        Optional function to format progress events before sending to LC callbacks.

    Returns
    -------
    StructuredTool
        A LangChain StructuredTool that wraps the MCP tool.
    """
    name: str = getattr(tool, "name", "mcp_tool")
    description: str = getattr(tool, "description", "") or f"MCP tool '{name}'."
    input_schema: dict[str, Any] | None = getattr(tool, "inputSchema", None) or getattr(
        tool, "input_schema", None
    )

    logger.info(f"[TOOL_CREATION] Creating LangChain tool for MCP tool: {name}")
    logger.debug(f"[TOOL_CREATION] Description: {description}")
    logger.debug(f"[TOOL_CREATION] Input schema: {input_schema}")

    # Use the MCP input schema directly or let LangChain infer from function signature
    args_schema = input_schema if input_schema else None
    infer_schema = args_schema is None
    logger.debug(f"[TOOL_CREATION] Args schema: {args_schema}, infer: {infer_schema}")

    async def _invoke(
        run_manager: CallbackManagerForToolRun | None = None, **kwargs: Any
    ) -> Any:
        # The run_manager is passed as a separate parameter by LangChain
        args = kwargs  # All kwargs are the actual tool arguments

        logger.info(f"[TOOL_INVOKE] Starting tool invocation: {name}")
        logger.debug(f"[TOOL_INVOKE] Input args: {args}")
        logger.debug(f"[TOOL_INVOKE] Run manager present: {run_manager is not None}")

        async def enhanced_progress_handler(
            progress: float, total: float | None, message: str | None
        ) -> None:
            # Forward to run_manager if available
            if run_manager:
                try:
                    # Create a meaningful status message
                    if progress_formatter:
                        # Use custom formatter
                        progress_dict = {
                            "progress": progress,
                            "total": total,
                            "message": message,
                        }
                        text = progress_formatter(progress_dict)
                    else:
                        # Default formatting
                        if total is not None:
                            text = (
                                f"[progress] {progress}/{total} – {message or ''}"
                            ).strip()
                        else:
                            text = f"[progress] {progress} – {message or ''}".strip()

                    run_manager.on_text(text, verbose=True)
                    logger.debug(
                        "[PROGRESS_HANDLER] Successfully sent text to run_manager"
                    )
                except Exception as e:  # best-effort
                    logger.warning(
                        f"[PROGRESS_HANDLER] Failed to send text to run_manager: {e}"
                    )

        logger.debug("[TOOL_INVOKE] Created enhanced progress handler")

        try:
            logger.debug(f"[TOOL_INVOKE] Opening client connection for tool: {name}")
            async with client:
                logger.debug(
                    f"[TOOL_INVOKE] Calling MCP tool '{name}' with args: {args}"
                )
                result: CallToolResult = await client.call_tool(
                    name=name,
                    arguments=args or {},
                    progress_handler=enhanced_progress_handler,
                )
                logger.info(f"[TOOL_INVOKE] Tool '{name}' completed successfully")
                logger.debug(f"[TOOL_INVOKE] Raw result: {result}")

                # Extract the main result using FastMCP hierarchy:
                # data > structured_content > content
                main_result = None
                if result.data is not None:
                    logger.debug(f"[TOOL_INVOKE] Using parsed data: {result.data}")
                    main_result = result.data
                elif result.structured_content is not None:
                    logger.debug(
                        f"[TOOL_INVOKE] Using structured content: "
                        f"{result.structured_content}"
                    )
                    main_result = result.structured_content
                elif result.content:
                    # For content blocks, extract text from first TextContent
                    if len(result.content) == 1 and hasattr(result.content[0], "text"):
                        text_content = result.content[0].text
                        logger.debug(
                            f"[TOOL_INVOKE] Processing text content: {text_content}"
                        )

                        # Try to parse as JSON if it looks like JSON
                        if text_content.strip().startswith(
                            "{"
                        ) and text_content.strip().endswith("}"):
                            try:
                                parsed = json.loads(text_content)
                                logger.debug(
                                    f"[TOOL_INVOKE] Parsed JSON from text: {parsed}"
                                )
                                main_result = parsed
                            except json.JSONDecodeError:
                                logger.debug(
                                    "[TOOL_INVOKE] Text is not valid JSON, "
                                    "using as-is"
                                )
                                main_result = text_content
                        else:
                            main_result = text_content
                    else:
                        # Multiple content blocks or non-text content - return as-is
                        logger.debug(
                            f"[TOOL_INVOKE] Using raw content blocks: {result.content}"
                        )
                        main_result = result.content
                else:
                    # Fallback - return the entire result object
                    logger.debug(
                        f"[TOOL_INVOKE] No content found, using raw result: {result}"
                    )
                    main_result = result

                logger.debug(f"[TOOL_INVOKE] Returning main result: {main_result}")
                return main_result

        except Exception as e:
            logger.error(f"[TOOL_INVOKE] Error invoking tool '{name}': {e}")
            logger.exception(f"[TOOL_INVOKE] Full exception details for tool '{name}':")
            raise

    logger.info(f"[TOOL_CREATION] Successfully created LangChain tool: {name}")

    return StructuredTool.from_function(
        name=name,
        description=description,
        args_schema=args_schema,
        coroutine=_invoke,
        infer_schema=infer_schema,
    )


def mcp_to_langchain(
    tools: list[McpTool],
    *,
    client: Client,
    progress_formatter: Callable[[dict[str, Any]], str] | None = None,
) -> list[StructuredTool]:
    """
    Convert a list of FastMCP tool descriptors into LangChain StructuredTools.

    Parameters
    ----------
    tools : list[McpTool]
        The descriptors returned by `await client.list_tools()`.
    client : Client
        The FastMCP client you created (already configured with elicitation/progress).
    progress_formatter : Optional[Callable[[dict], str]]
        Optional function to format progress events before sending to LC callbacks.

    Returns
    -------
    list[StructuredTool]
        List of LangChain StructuredTools that wrap the MCP tools.
    """
    logger.info(
        f"[MCP_TO_LANGCHAIN] Starting conversion of {len(tools)} MCP tools "
        f"to LangChain tools"
    )
    lc_tools: list[StructuredTool] = []

    for i, t in enumerate(tools):
        try:
            tool_name = getattr(t, "name", f"tool_{i}")
            logger.debug(
                f"[MCP_TO_LANGCHAIN] Processing tool {i+1}/{len(tools)}: {tool_name}"
            )
            lc_tool = _create_langchain_tool_from_mcp(
                tool=t, client=client, progress_formatter=progress_formatter
            )
            lc_tools.append(lc_tool)
            logger.debug(f"[MCP_TO_LANGCHAIN] Successfully converted tool: {tool_name}")
        except Exception as e:
            tool_name = f"tool_{i}"  # fallback name for logging
            logger.error(
                f"[MCP_TO_LANGCHAIN] Failed to convert MCP tool '{tool_name}' "
                f"to LangChain: {e}"
            )
            logger.exception(
                f"[MCP_TO_LANGCHAIN] Full exception details for tool '{tool_name}':"
            )

    logger.info(
        f"[MCP_TO_LANGCHAIN] Successfully converted {len(lc_tools)}/{len(tools)} tools"
    )
    return lc_tools
