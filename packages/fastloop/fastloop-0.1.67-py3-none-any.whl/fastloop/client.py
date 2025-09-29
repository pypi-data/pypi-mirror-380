import asyncio
import contextlib
import json
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

import aiohttp


@dataclass
class LoopEvent:
    type: str
    loop_id: str | None = None
    data: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {"type": self.type}
        if self.loop_id:
            result["loop_id"] = self.loop_id
        if self.data:
            result.update(self.data)
        return result


@dataclass
class LoopResponse:
    success: bool
    data: dict[str, Any] | None = None
    error: str | None = None


EventCallback = Callable[[LoopEvent], None | asyncio.Task]


class LoopClient:
    def __init__(self):
        self._url: str | None = None
        self._loop_id: str | None = None
        self._has_schema: bool = False
        self._is_paused: bool = False
        self._error: str | None = None
        self._event_callback: EventCallback | None = None
        self._session: aiohttp.ClientSession | None = None

    def with_loop(
        self,
        url: str,
        event_callback: EventCallback | None = None,
        loop_id: str | None = None,
    ) -> "LoopClient":
        self._url = url
        self._loop_id = loop_id
        self._event_callback = event_callback
        return self

    async def _ensure_session(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()

    async def setup(self) -> dict[str, Any]:
        if not self._url:
            raise ValueError("Loop not configured - call with_loop first")

        try:
            event_types = await self.get_event_types()
            self._has_schema = True
            return event_types
        except Exception as err:
            raise err

    async def send(self, event_type: str, data: dict[str, Any]) -> LoopResponse:
        if not self._url:
            raise ValueError("Loop not configured - call with_loop first")

        await self._ensure_session()

        event_data = {"type": event_type, **data}

        if self._loop_id:
            event_data["loop_id"] = self._loop_id

        try:
            async with self._session.post(
                self._url, json=event_data, headers={"Content-Type": "application/json"}
            ) as response:
                if not response.ok:
                    error_text = await response.text()
                    raise Exception(f"HTTP {response.status}: {error_text}")

                result = await response.json()

                if result and result.get("loop_id"):
                    self._loop_id = result["loop_id"]

                return LoopResponse(success=True, data=result)

        except Exception as err:
            return LoopResponse(
                success=False,
                error=str(err) if isinstance(err, Exception) else "Unknown error",
            )

    async def get_event_types(self) -> dict[str, Any]:
        if not self._url:
            raise ValueError("Loop not configured - call with_loop first")

        await self._ensure_session()

        try:
            async with self._session.get(
                self._url, headers={"Content-Type": "application/json"}
            ) as response:
                if not response.ok:
                    error_text = await response.text()
                    raise Exception(f"HTTP {response.status}: {error_text}")

                return await response.json()

        except Exception as err:
            raise err

    def pause(self) -> None:
        self._is_paused = True

    def resume(self) -> None:
        self._is_paused = False

    async def stop(self) -> LoopResponse:
        if not self._url:
            raise ValueError("Loop not configured - call with_loop first")

        if not self._loop_id:
            return LoopResponse(success=False, error="No loop ID available")

        await self._ensure_session()

        try:
            stop_url = f"{self._url.rstrip('/')}/{self._loop_id}/stop"
            async with self._session.post(
                stop_url, headers={"Content-Type": "application/json"}
            ) as response:
                if not response.ok:
                    error_text = await response.text()
                    raise Exception(f"HTTP {response.status}: {error_text}")

                self._loop_id = None
                result = await response.json()
                return LoopResponse(success=True, data=result)

        except Exception as err:
            return LoopResponse(success=False, error=str(err))

    def get_status(self) -> dict[str, Any]:
        return {
            "has_schema": self._has_schema,
            "is_paused": self._is_paused,
            "error": self._error,
            "loop_id": self._loop_id,
        }

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


# Simple hook-like function for easy usage
def use_loop(
    url: str, event_callback: EventCallback | None = None, loop_id: str | None = None
) -> dict[str, Any]:
    """
    Hook-like function that returns a dictionary with send function and other utilities.

    Usage:
        def my_component():
            def handle_event(event):
                print("Received event:", event)

            loop = use_loop("http://localhost:8000/chat", event_callback=handle_event)

            return rx.button("Send", on_click=lambda: loop["send"]("user_message", {"text": "hello"}))
    """
    client = LoopClient()
    client.with_loop(url=url, event_callback=event_callback, loop_id=loop_id)

    async def send_func(event_type: str, data: dict[str, Any] | None = None):
        if data is None:
            data = {}
        return await client.send(event_type, data)

    async def setup_func():
        return await client.setup()

    async def stop_func():
        return await client.stop()

    def pause_func():
        return client.pause()

    def resume_func():
        return client.resume()

    def get_status_func():
        return client.get_status()

    return {
        "send": send_func,
        "setup": setup_func,
        "stop": stop_func,
        "pause": pause_func,
        "resume": resume_func,
        "get_status": get_status_func,
        "client": client,
    }


# Simple auto-connecting FastLoop state
class FastLoopState:
    """
    Simple FastLoop state that auto-connects and exposes attributes directly.

    Just pass the URL to __init__ and everything else is automatic.

    Usage:
        import reflex as rx
        from fastloop.client import FastLoopState

        class BrowseState(FastLoopState, rx.State):
            def __init__(self):
                super().__init__("http://localhost:8112/monitor-source")

            def event_callback(self, event):
                print("Got event:", event)

            async def on_mount(self):
                # send is available immediately
                await self.send("monitor_source_query", {"source_id": "123"})
    """

    def __init__(self, fastloop_url: str = "", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fastloop_url = fastloop_url
        self._loop_client = None
        self._auto_connected = False

        # Auto-setup if URL is provided
        if self._fastloop_url:
            self._setup_client()

    def _setup_client(self):
        """Internal setup - called automatically"""
        if not self._loop_client:
            self._loop_client = LoopClient()
            callback = getattr(self, "event_callback", None)
            self._loop_client.with_loop(url=self._fastloop_url, event_callback=callback)

    async def _auto_connect(self):
        """Auto-connect on first use"""
        if not self._auto_connected and self._loop_client:
            try:
                await self._loop_client.setup()
                self._auto_connected = True
            except Exception as e:
                print(f"FastLoop connection failed: {e}")

    async def send(
        self, event_type: str, data: dict[str, Any] | None = None
    ) -> LoopResponse:
        """Send an event to FastLoop"""
        if not self._loop_client:
            raise RuntimeError("FastLoop not configured - pass URL to __init__")

        # Auto-connect on first send
        await self._auto_connect()

        if data is None:
            data = {}

        return await self._loop_client.send(event_type, data)

    @property
    def loop_id(self) -> str:
        """Get the current loop ID"""
        if self._loop_client:
            return self._loop_client._loop_id or ""
        return ""

    @property
    def is_connected(self) -> bool:
        """Check if connected to FastLoop"""
        return self._auto_connected

    @property
    def loop_status(self) -> dict[str, Any]:
        """Get current loop status"""
        if self._loop_client:
            return self._loop_client.get_status()
        return {}

    async def stop_loop(self):
        """Stop the loop"""
        if self._loop_client:
            result = await self._loop_client.stop()
            self._auto_connected = False
            return result

    def pause_loop(self):
        """Pause the loop"""
        if self._loop_client:
            self._loop_client.pause()

    def resume_loop(self):
        """Resume the loop"""
        if self._loop_client:
            self._loop_client.resume()

    def event_callback(self, event: LoopEvent):
        """Override this to handle events"""
        pass

    def connect_to(self, url: str):
        """Connect to a FastLoop URL (alternative to passing in __init__)"""
        self._fastloop_url = url
        self._setup_client()


# Reflex integration mixin - Use this with rx.State
class LoopMixin:
    """
    Mixin class for Reflex State to add FastLoop functionality.

    Usage:
        import reflex as rx
        from fastloop.client import LoopMixin, LoopEvent

        class MyState(LoopMixin, rx.State):
            # Your state variables
            error: str = ""
            event_types: dict[str, Any] = {}
            loop_id: str = ""
            is_connected: bool = False
            is_paused: bool = False
            last_response: dict[str, Any] = {}

            async def _handle_event(self, event: LoopEvent):
                # Handle incoming events
                pass
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._loop_client = LoopClient()
        self._loop_url = ""
        self._sse_task = None

    async def connect_loop(self, url: str, loop_id: str | None = None):
        """Connect to a FastLoop instance"""
        try:
            self._loop_url = url
            self._loop_client.with_loop(
                url=url, event_callback=self._handle_event, loop_id=loop_id
            )

            event_types = await self._loop_client.setup()

            # Update state attributes if they exist
            if hasattr(self, "event_types"):
                self.event_types = event_types
            if hasattr(self, "is_connected"):
                self.is_connected = True
            if hasattr(self, "error"):
                self.error = ""

            if loop_id and hasattr(self, "loop_id"):
                self.loop_id = loop_id
                await self._start_sse_connection()

        except Exception as e:
            if hasattr(self, "error"):
                self.error = str(e)
            if hasattr(self, "is_connected"):
                self.is_connected = False

    async def send_event(self, event_type: str, data: dict[str, Any] | None = None):
        """Send an event to the loop"""
        if not self._loop_client:
            if hasattr(self, "error"):
                self.error = "Client not initialized"
            return

        if data is None:
            data = {}

        try:
            response = await self._loop_client.send(event_type, data)

            if response.success:
                if hasattr(self, "last_response"):
                    self.last_response = response.data or {}
                if hasattr(self, "error"):
                    self.error = ""

                # If this is the first successful send and we got a loop_id
                if (
                    response.data
                    and response.data.get("loop_id")
                    and hasattr(self, "loop_id")
                    and not self.loop_id
                ):
                    self.loop_id = response.data["loop_id"]
                    await self._start_sse_connection()
            else:
                if hasattr(self, "error"):
                    self.error = response.error or "Unknown error"

        except Exception as e:
            if hasattr(self, "error"):
                self.error = str(e)

    async def stop_loop(self):
        """Stop the current loop"""
        if not self._loop_client:
            return

        try:
            await self._stop_sse_connection()
            response = await self._loop_client.stop()

            if response.success:
                if hasattr(self, "loop_id"):
                    self.loop_id = ""
                if hasattr(self, "is_connected"):
                    self.is_connected = False
                if hasattr(self, "error"):
                    self.error = ""
            else:
                if hasattr(self, "error"):
                    self.error = response.error or "Failed to stop loop"

        except Exception as e:
            if hasattr(self, "error"):
                self.error = str(e)

    def pause_loop(self):
        """Pause the loop"""
        if self._loop_client:
            self._loop_client.pause()
            if hasattr(self, "is_paused"):
                self.is_paused = True

    def resume_loop(self):
        """Resume the loop"""
        if self._loop_client:
            self._loop_client.resume()
            if hasattr(self, "is_paused"):
                self.is_paused = False

    async def _handle_event(self, event: LoopEvent):
        """Handle incoming events from SSE - override this in your State class"""
        pass

    async def _start_sse_connection(self):
        """Start SSE connection for real-time events"""
        if not (hasattr(self, "loop_id") and self.loop_id) or not self._loop_url:
            return

        await self._stop_sse_connection()

        # Parse base URL for SSE endpoint
        parsed = urlparse(self._loop_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        sse_url = f"{base_url}/events/{self.loop_id}/sse"

        self._sse_task = asyncio.create_task(self._sse_listener(sse_url))

    async def _stop_sse_connection(self):
        """Stop SSE connection"""
        if self._sse_task and not self._sse_task.done():
            self._sse_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self._sse_task
            self._sse_task = None

    async def _sse_listener(self, sse_url: str):
        """Listen for SSE events"""
        try:
            if not self._loop_client._session:
                await self._loop_client._ensure_session()

            async with self._loop_client._session.get(
                sse_url,
                headers={"Accept": "text/event-stream", "Cache-Control": "no-cache"},
            ) as response:
                async for line in response.content:
                    line = line.decode("utf-8").strip()
                    if line.startswith("data: "):
                        try:
                            data = json.loads(line[6:])
                            event = LoopEvent(
                                type=data.get("type", ""),
                                loop_id=data.get("loop_id"),
                                data=data,
                            )
                            await self._handle_event(event)
                        except json.JSONDecodeError:
                            continue

        except asyncio.CancelledError:
            pass
        except Exception as e:
            if hasattr(self, "error"):
                self.error = f"SSE connection error: {e!s}"

    async def cleanup_loop(self):
        """Cleanup loop resources"""
        await self._stop_sse_connection()
        if self._loop_client:
            await self._loop_client.close()
