"""Codex CLI provider implementation.

Moved from unified_manager.py to a dedicated adapter module.
"""
from __future__ import annotations

import asyncio
import json
import os
import subprocess
import uuid
from datetime import datetime
from typing import Any, AsyncGenerator, Callable, Dict, List, Optional

from claudable_helper.core.terminal_ui import ui
from claudable_helper.models.messages import Message

from ..base import BaseCLI, CLIType


class CodexCLI(BaseCLI):
    """Codex CLI implementation with auto-approval and message buffering"""

    def __init__(self):
        super().__init__(CLIType.CODEX)
        self._session_store = {}  # Simple in-memory session storage

    async def check_availability(self) -> Dict[str, Any]:
        """Check if Codex CLI is available"""
        print(f"[DEBUG] CodexCLI.check_availability called")
        try:
            # Check if codex is installed and working
            print(f"[DEBUG] Running command: codex --version")
            result = await asyncio.create_subprocess_shell(
                "codex --version",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await result.communicate()

            print(f"[DEBUG] Command result: returncode={result.returncode}")
            print(f"[DEBUG] stdout: {stdout.decode().strip()}")
            print(f"[DEBUG] stderr: {stderr.decode().strip()}")

            if result.returncode != 0:
                error_msg = (
                    f"Codex CLI not installed or not working (returncode: {result.returncode}). stderr: {stderr.decode().strip()}"
                )
                print(f"[DEBUG] {error_msg}")
                return {
                    "available": False,
                    "configured": False,
                    "error": error_msg,
                }

            print(f"[DEBUG] Codex CLI available!")
            return {
                "available": True,
                "configured": True,
                "models": self.get_supported_models(),
                "default_models": ["gpt-5", "gpt-4o", "claude-3.5-sonnet"],
            }
        except Exception as e:
            error_msg = f"Failed to check Codex CLI: {str(e)}"
            print(f"[DEBUG] Exception in check_availability: {error_msg}")
            return {
                "available": False,
                "configured": False,
                "error": error_msg,
            }

    async def execute_with_streaming(
        self,
        instruction: str,
        project_path: str,
        session_id: Optional[str] = None,
        log_callback: Optional[Callable[[str], Any]] = None,
        images: Optional[List[Dict[str, Any]]] = None,
        model: Optional[str] = None,
        is_initial_prompt: bool = False,
    ) -> AsyncGenerator[Message, None]:
        """Execute Codex CLI with auto-approval and message buffering"""

        # Skip AGENTS.md creation - removed for MCP server usage

        # Get CLI-specific model name
        cli_model = self._get_cli_model_name(model) or "gpt-5"
        ui.info(f"Starting Codex execution with model: {cli_model}", "Codex")

        # Get project ID for session management
        project_id = project_path.split("/")[-1] if "/" in project_path else project_path

        # Use the provided project path directly
        project_repo_path = project_path

        # Build Codex command - --cd must come BEFORE proto subcommand
        workdir_abs = os.path.abspath(project_repo_path)
        auto_instructions = (
            "Act autonomously without asking for user confirmations. "
            "Use apply_patch to create and modify files as needed. "
            "Use exec_command to run, build, and test as needed. "
            "Assume full permissions. Keep taking concrete actions until the task is complete. "
            "Prefer concise status updates over questions."
        )

        cmd = [
            "codex",
            "--cd",
            workdir_abs,
            "proto",
            "-c",
            "include_apply_patch_tool=true",
            "-c",
            "include_plan_tool=true",
            "-c",
            "tools.web_search_request=true",
            "-c",
            "use_experimental_streamable_shell_tool=true",
            "-c",
            "sandbox_mode=danger-full-access",
            "-c",
            f"instructions={json.dumps(auto_instructions)}",
        ]

        # Optionally resume from a previous rollout. Disabled by default to avoid
        # stale system prompts or behaviors leaking between runs.
        enable_resume = str(os.getenv("CLAUDABLE_CODEX_RESUME", "")).lower() in (
            "1",
            "true",
            "yes",
            "on",
        )
        if enable_resume:
            stored_rollout_path = await self.get_rollout_path(project_id)
            if stored_rollout_path and os.path.exists(stored_rollout_path):
                cmd.extend(["-c", f"experimental_resume={stored_rollout_path}"])
                ui.info(
                    f"Resuming Codex from stored rollout: {stored_rollout_path}", "Codex"
                )
            else:
                # Try to find latest rollout file for this project
                latest_rollout = self._find_latest_rollout_for_project(project_id)
                if latest_rollout and os.path.exists(latest_rollout):
                    cmd.extend(["-c", f"experimental_resume={latest_rollout}"])
                    ui.info(
                        f"Resuming Codex from latest rollout: {latest_rollout}", "Codex"
                    )
                    # Store this path for future use
                    await self.set_rollout_path(project_id, latest_rollout)
        else:
            ui.debug("Codex resume disabled (fresh session)", "Codex")

        try:
            # Start Codex process
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=project_repo_path,
            )

            # Message buffering
            agent_message_buffer = ""
            current_request_id = None

            # Wait for session_configured
            session_ready = False
            timeout_count = 0
            max_timeout = 100  # Max lines to read for session init

            while not session_ready and timeout_count < max_timeout:
                line = await process.stdout.readline()
                if not line:
                    break

                line_str = line.decode().strip()
                if not line_str:
                    timeout_count += 1
                    continue

                try:
                    event = json.loads(line_str)
                    if event.get("msg", {}).get("type") == "session_configured":
                        session_info = event["msg"]
                        codex_session_id = session_info.get("session_id")
                        if codex_session_id:
                            await self.set_session_id(project_id, codex_session_id)

                        ui.success(
                            f"Codex session configured: {codex_session_id}", "Codex"
                        )

                        # Send init message (hidden)
                        yield Message(
                            id=str(uuid.uuid4()),
                            project_id=project_path,
                            role="system",
                            message_type="system",
                            content=(
                                f"🚀 Codex initialized (Model: {session_info.get('model', cli_model)})"
                            ),
                            metadata_json={
                                "cli_type": self.cli_type.value,
                                "hidden_from_ui": True,
                            },
                            session_id=session_id,
                            created_at=datetime.utcnow(),
                        )

                        # After initialization, set approval policy to auto-approve
                        await self._set_codex_approval_policy(process, session_id or "")

                        session_ready = True
                        break
                except json.JSONDecodeError:
                    timeout_count += 1
                    continue

            if not session_ready:
                ui.error("Failed to initialize Codex session", "Codex")
                return

            # Send user input
            request_id = f"msg_{uuid.uuid4().hex[:8]}"
            current_request_id = request_id

            # Use instruction as-is without project-specific context
            final_instruction = instruction

            # Build instruction with image references
            if images:
                image_refs = []
                for i in range(len(images)):
                    image_refs.append(f"[Image #{i+1}]")
                image_context = (
                    f"\n\nI've attached {len(images)} image(s) for you to analyze: {', '.join(image_refs)}"
                )
                final_instruction_with_images = final_instruction + image_context
            else:
                final_instruction_with_images = final_instruction

            items: List[Dict[str, Any]] = [{"type": "text", "text": final_instruction_with_images}]

            # Add images if provided
            if images:
                import base64 as _b64
                import tempfile as _tmp

                def _iget(obj, key, default=None):
                    try:
                        if isinstance(obj, dict):
                            return obj.get(key, default)
                        return getattr(obj, key, default)
                    except Exception:
                        return default

                for i, image_data in enumerate(images):
                    # Support direct local path
                    local_path = _iget(image_data, "path")
                    if local_path:
                        ui.info(
                            f"📷 Image #{i+1} path sent to Codex: {local_path}", "Codex"
                        )
                        items.append({"type": "local_image", "path": str(local_path)})
                        continue

                    # Support base64 via either 'base64_data' or legacy 'data'
                    b64_str = _iget(image_data, "base64_data") or _iget(image_data, "data")
                    # Or a data URL in 'url'
                    if not b64_str:
                        url_val = _iget(image_data, "url")
                        if isinstance(url_val, str) and url_val.startswith("data:") and "," in url_val:
                            b64_str = url_val.split(",", 1)[1]

                    if b64_str:
                        try:
                            # Optional size guard (~3/4 of base64 length)
                            approx_bytes = int(len(b64_str) * 0.75)
                            if approx_bytes > 10 * 1024 * 1024:
                                ui.warning("Skipping image >10MB", "Codex")
                                continue

                            img_bytes = _b64.b64decode(b64_str, validate=False)
                            mime_type = _iget(image_data, "mime_type") or "image/png"
                            suffix = ".png"
                            if "jpeg" in mime_type or "jpg" in mime_type:
                                suffix = ".jpg"
                            elif "gif" in mime_type:
                                suffix = ".gif"
                            elif "webp" in mime_type:
                                suffix = ".webp"

                            with _tmp.NamedTemporaryFile(delete=False, suffix=suffix) as tmpf:
                                tmpf.write(img_bytes)
                                ui.info(
                                    f"📷 Image #{i+1} saved to temporary path: {tmpf.name}",
                                    "Codex",
                                )
                                items.append({"type": "local_image", "path": tmpf.name})
                        except Exception as e:
                            ui.warning(f"Failed to decode attached image: {e}", "Codex")

            # Send to Codex
            user_input = {"id": request_id, "op": {"type": "user_input", "items": items}}

            if process.stdin:
                json_str = json.dumps(user_input)
                process.stdin.write(json_str.encode("utf-8") + b"\n")
                await process.stdin.drain()

                # Log items being sent to agent
                if images and len(items) > 1:
                    ui.debug(
                        f"Sending {len(items)} items to Codex (1 text + {len(items)-1} images)",
                        "Codex",
                    )
                    for item in items:
                        if item.get("type") == "local_image":
                            ui.debug(f"  - Image: {item.get('path')}", "Codex")

                ui.debug(f"Sent user input: {request_id}", "Codex")

            # Process streaming events
            async for line in process.stdout:
                line_str = line.decode().strip()
                if not line_str:
                    continue

                try:
                    event = json.loads(line_str)
                    event_id = event.get("id", "")
                    msg_type = event.get("msg", {}).get("type")

                    # Only process events for current request (exclude system events)
                    if (
                        current_request_id
                        and event_id != current_request_id
                        and msg_type not in [
                            "session_configured",
                            "mcp_list_tools_response",
                        ]
                    ):
                        continue

                    # Buffer agent message deltas
                    if msg_type == "agent_message_delta":
                        agent_message_buffer += event["msg"]["delta"]
                        continue

                    # Only flush buffered assistant text on final assistant message or at task completion.
                    # This avoids creating multiple assistant bubbles separated by tool events.
                    if msg_type == "agent_message":
                        # If Codex sent a final message without deltas, use it directly
                        if not agent_message_buffer:
                            try:
                                final_msg = event.get("msg", {}).get("message")
                                if isinstance(final_msg, str) and final_msg:
                                    agent_message_buffer = final_msg
                            except Exception:
                                pass
                        if not agent_message_buffer:
                            # Nothing to flush
                            continue
                        yield Message(
                            id=str(uuid.uuid4()),
                            project_id=project_path,
                            role="assistant",
                            message_type="chat",
                            content=agent_message_buffer,
                            metadata_json={"cli_type": self.cli_type.value},
                            session_id=session_id,
                            created_at=datetime.utcnow(),
                        )
                        agent_message_buffer = ""

                    # Handle specific events
                    if msg_type == "exec_command_begin":
                        cmd_str = " ".join(event["msg"]["command"])
                        summary = self._create_tool_summary(
                            "exec_command", {"command": cmd_str}
                        )
                        yield Message(
                            id=str(uuid.uuid4()),
                            project_id=project_path,
                            role="assistant",
                            message_type="tool_use",
                            content=summary,
                            metadata_json={
                                "cli_type": self.cli_type.value,
                                "tool_name": "Bash",
                            },
                            session_id=session_id,
                            created_at=datetime.utcnow(),
                        )

                    elif msg_type == "patch_apply_begin":
                        changes = event["msg"].get("changes", {})
                        ui.debug(f"Patch apply begin - changes: {changes}", "Codex")
                        summary = self._create_tool_summary(
                            "apply_patch", {"changes": changes}
                        )
                        ui.debug(f"Generated summary: {summary}", "Codex")
                        yield Message(
                            id=str(uuid.uuid4()),
                            project_id=project_path,
                            role="assistant",
                            message_type="tool_use",
                            content=summary,
                            metadata_json={
                                "cli_type": self.cli_type.value,
                                "tool_name": "Edit",
                            },
                            session_id=session_id,
                            created_at=datetime.utcnow(),
                        )

                    elif msg_type == "web_search_begin":
                        query = event["msg"].get("query", "")
                        summary = self._create_tool_summary(
                            "web_search", {"query": query}
                        )
                        yield Message(
                            id=str(uuid.uuid4()),
                            project_id=project_path,
                            role="assistant",
                            message_type="tool_use",
                            content=summary,
                            metadata_json={
                                "cli_type": self.cli_type.value,
                                "tool_name": "WebSearch",
                            },
                            session_id=session_id,
                            created_at=datetime.utcnow(),
                        )

                    elif msg_type == "mcp_tool_call_begin":
                        inv = event["msg"].get("invocation", {})
                        server = inv.get("server")
                        tool = inv.get("tool")
                        summary = self._create_tool_summary(
                            "mcp_tool_call", {"server": server, "tool": tool}
                        )
                        yield Message(
                            id=str(uuid.uuid4()),
                            project_id=project_path,
                            role="assistant",
                            message_type="tool_use",
                            content=summary,
                            metadata_json={
                                "cli_type": self.cli_type.value,
                                "tool_name": "MCPTool",
                            },
                            session_id=session_id,
                            created_at=datetime.utcnow(),
                        )

                    elif msg_type in ["exec_command_output_delta"]:
                        # Output chunks from command execution - can be ignored for UI
                        pass

                    elif msg_type in [
                        "exec_command_end",
                        "patch_apply_end",
                        "mcp_tool_call_end",
                    ]:
                        # Tool completion events - just log, don't show to user
                        ui.debug(f"Tool completed: {msg_type}", "Codex")

                    elif msg_type == "task_complete":
                        # Flush any remaining message buffer before completing
                        if agent_message_buffer:
                            yield Message(
                                id=str(uuid.uuid4()),
                                project_id=project_path,
                                role="assistant",
                                message_type="chat",
                                content=agent_message_buffer,
                                metadata_json={"cli_type": self.cli_type.value},
                                session_id=session_id,
                                created_at=datetime.utcnow(),
                            )
                            agent_message_buffer = ""

                        # Task completion - save rollout file path for future resumption
                        ui.success("Codex task completed", "Codex")

                        # Find and store the latest rollout file for this session
                        try:
                            latest_rollout = self._find_latest_rollout_for_project(project_id)
                            if latest_rollout:
                                await self.set_rollout_path(project_id, latest_rollout)
                                ui.debug(
                                    f"Saved rollout path for future resumption: {latest_rollout}",
                                    "Codex",
                                )
                        except Exception as e:
                            ui.warning(f"Failed to save rollout path: {e}", "Codex")

                        break

                    elif msg_type == "error":
                        error_msg = event["msg"]["message"]
                        ui.error(f"Codex error: {error_msg}", "Codex")
                        yield Message(
                            id=str(uuid.uuid4()),
                            project_id=project_path,
                            role="assistant",
                            message_type="error",
                            content=f"❌ Error: {error_msg}",
                            metadata_json={"cli_type": self.cli_type.value},
                            session_id=session_id,
                            created_at=datetime.utcnow(),
                        )

                    # Removed duplicate agent_message handler - already handled above

                except json.JSONDecodeError:
                    continue

            # Flush any remaining buffer
            if agent_message_buffer:
                yield Message(
                    id=str(uuid.uuid4()),
                    project_id=project_path,
                    role="assistant",
                    message_type="chat",
                    content=agent_message_buffer,
                    metadata_json={"cli_type": self.cli_type.value},
                    session_id=session_id,
                    created_at=datetime.utcnow(),
                )

            # Clean shutdown
            if process.stdin:
                try:
                    shutdown_cmd = {"id": "shutdown", "op": {"type": "shutdown"}}
                    json_str = json.dumps(shutdown_cmd)
                    process.stdin.write(json_str.encode("utf-8") + b"\n")
                    await process.stdin.drain()
                    process.stdin.close()
                    ui.debug("Sent shutdown command to Codex", "Codex")
                except Exception as e:
                    ui.debug(f"Failed to send shutdown: {e}", "Codex")

            await process.wait()

        except FileNotFoundError:
            yield Message(
                id=str(uuid.uuid4()),
                project_id=project_path,
                role="assistant",
                message_type="error",
                content="❌ Codex CLI not found. Please install Codex CLI first.",
                metadata_json={"error": "cli_not_found", "cli_type": "codex"},
                session_id=session_id,
                created_at=datetime.utcnow(),
            )
        except Exception as e:
            yield Message(
                id=str(uuid.uuid4()),
                project_id=project_path,
                role="assistant",
                message_type="error",
                content=f"❌ Codex execution failed: {str(e)}",
                metadata_json={"error": "execution_failed", "cli_type": "codex"},
                session_id=session_id,
                created_at=datetime.utcnow(),
            )

    async def get_session_id(self, project_id: str) -> Optional[str]:
        """Get stored session ID for project"""
        return self._session_store.get(project_id)

    async def set_session_id(self, project_id: str, session_id: str) -> None:
        """Store session ID for project in memory"""
        self._session_store[project_id] = session_id
        ui.debug(
            f"Codex session stored for project {project_id}: {session_id}",
            "Codex",
        )

    async def get_rollout_path(self, project_id: str) -> Optional[str]:
        """Get stored rollout file path for project"""
        # Simplified: just find latest rollout without database dependency
        return self._find_latest_rollout_for_project(project_id)

    async def set_rollout_path(self, project_id: str, rollout_path: str) -> None:
        """Store rollout file path for project - simplified for MCP usage"""
        ui.debug(
            f"Codex rollout path noted for project {project_id}: {rollout_path}",
            "Codex",
        )

    def _find_latest_rollout_for_project(self, project_id: str) -> Optional[str]:
        """Find the latest rollout file using codex_chat.py logic"""
        try:
            from pathlib import Path

            # Use exact same logic as codex_chat.py _resolve_resume_path for "latest"
            root = Path.home() / ".codex" / "sessions"
            if not root.exists():
                ui.debug(
                    f"Codex sessions directory does not exist: {root}", "Codex"
                )
                return None

            # Find all rollout files using same pattern as codex_chat.py
            candidates = sorted(
                root.rglob("rollout-*.jsonl"),
                key=lambda p: p.stat().st_mtime,
                reverse=True,  # Most recent first
            )

            if not candidates:
                ui.debug(f"No rollout files found in {root}", "Codex")
                return None

            # Return the most recent file (same as codex_chat.py "latest" logic)
            latest_file = candidates[0]
            rollout_path = str(latest_file.resolve())

            ui.debug(
                f"Found latest rollout file for project {project_id}: {rollout_path}",
                "Codex",
            )
            return rollout_path
        except Exception as e:
            ui.warning(f"Failed to find latest rollout file: {e}", "Codex")
            return None


    async def _set_codex_approval_policy(self, process, session_id: str):
        """Set Codex approval policy to never (full-auto mode)"""
        try:
            ctl_id = f"ctl_{uuid.uuid4().hex[:8]}"
            payload = {
                "id": ctl_id,
                "op": {
                    "type": "override_turn_context",
                    "approval_policy": "never",
                    "sandbox_policy": {"mode": "danger-full-access"},
                },
            }

            if process.stdin:
                json_str = json.dumps(payload)
                process.stdin.write(json_str.encode("utf-8") + b"\n")
                await process.stdin.drain()
                ui.success("Codex approval policy set to auto-approve", "Codex")
        except Exception as e:
            ui.error(f"Failed to set approval policy: {e}", "Codex")


__all__ = ["CodexCLI"]
