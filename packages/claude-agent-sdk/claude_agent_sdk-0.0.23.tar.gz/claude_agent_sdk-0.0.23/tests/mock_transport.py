"""Mock transport implementation for testing."""

import json
from collections.abc import AsyncIterator
from typing import Any

import anyio

from claude_agent_sdk._internal.transport import Transport


class MockTransport(Transport):
    """Mock transport for testing Query and Client behavior.

    This transport allows tests to:
    - Capture all messages written by the SDK
    - Simulate responses from the CLI
    - Control message flow timing
    """

    def __init__(self):
        """Initialize mock transport."""
        self.written_messages: list[dict[str, Any]] = []
        self.messages_to_read: list[dict[str, Any]] = []
        self._ready = False
        self._read_index = 0
        self._write_delay = 0.0  # Optional delay for write operations
        self._read_delay = 0.0  # Optional delay between messages

    async def connect(self) -> None:
        """Mark transport as ready."""
        self._ready = True

    async def write(self, data: str) -> None:
        """Capture written messages.

        Args:
            data: JSON string with newline
        """
        if self._write_delay > 0:
            await anyio.sleep(self._write_delay)

        # Parse and store the message
        message = json.loads(data.strip())
        self.written_messages.append(message)

    async def read_messages(self) -> AsyncIterator[dict[str, Any]]:
        """Yield messages from the configured list.

        Yields:
            Messages added via add_message_to_read()
        """
        # Auto-respond to initialize requests
        responded_to_init = False

        while self._ready:
            # Check for initialize requests we need to respond to
            if not responded_to_init:
                for msg in self.written_messages:
                    if (
                        msg.get("type") == "control_request"
                        and msg.get("request", {}).get("subtype") == "initialize"
                    ):
                        # Auto-send initialize response
                        responded_to_init = True
                        yield {
                            "type": "control_response",
                            "response": {
                                "subtype": "success",
                                "request_id": msg.get("request_id"),
                                "response": {
                                    "commands": [],
                                    "output_style": "default",
                                    "hooks": [],  # Will be populated by Query.initialize
                                },
                            },
                        }
                        break

            # Yield any manually added messages
            if self._read_index < len(self.messages_to_read):
                if self._read_delay > 0:
                    await anyio.sleep(self._read_delay)

                message = self.messages_to_read[self._read_index]
                self._read_index += 1
                yield message
            else:
                # Small delay to avoid busy loop
                await anyio.sleep(0.01)

    async def close(self) -> None:
        """Mark transport as not ready."""
        self._ready = False

    def is_ready(self) -> bool:
        """Check if transport is ready.

        Returns:
            True if connect() was called and close() wasn't
        """
        return self._ready

    async def end_input(self) -> None:
        """No-op for mock transport."""
        pass

    # Helper methods for testing

    def add_message_to_read(self, message: dict[str, Any]) -> None:
        """Add a message that will be returned by read_messages().

        Args:
            message: Message dict to be yielded by read_messages()
        """
        self.messages_to_read.append(message)

    def add_control_request(self, subtype: str, request_id: str, **kwargs: Any) -> None:
        """Helper to add a control request message.

        Args:
            subtype: Control request subtype (e.g., "initialize", "hook_callback")
            request_id: Request ID
            **kwargs: Additional request fields
        """
        self.add_message_to_read(
            {
                "type": "control_request",
                "request_id": request_id,
                "request": {"subtype": subtype, **kwargs},
            }
        )

    def get_written_messages(self, msg_type: str | None = None) -> list[dict[str, Any]]:
        """Get written messages, optionally filtered by type.

        Args:
            msg_type: Optional message type to filter by

        Returns:
            List of written messages
        """
        if msg_type is None:
            return self.written_messages
        return [msg for msg in self.written_messages if msg.get("type") == msg_type]

    def get_control_responses(self) -> list[dict[str, Any]]:
        """Get all control response messages that were written.

        Returns:
            List of control response messages
        """
        return self.get_written_messages("control_response")

    def get_last_response(self) -> dict[str, Any] | None:
        """Get the last written message.

        Returns:
            Last written message or None if no messages
        """
        return self.written_messages[-1] if self.written_messages else None

    def clear(self) -> None:
        """Clear all messages and reset state."""
        self.written_messages.clear()
        self.messages_to_read.clear()
        self._read_index = 0

    def set_delays(self, write_delay: float = 0.0, read_delay: float = 0.0) -> None:
        """Set artificial delays for testing timing issues.

        Args:
            write_delay: Delay in seconds for write operations
            read_delay: Delay in seconds between read messages
        """
        self._write_delay = write_delay
        self._read_delay = read_delay
