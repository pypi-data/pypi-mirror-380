"""Tests for the hooks decorator API."""

import anyio

from claude_agent_sdk.hooks import (
    PreToolUseHookResponse,
    clear_registry,
    get_registry,
    post_tool_use,
    pre_tool_use,
)
from claude_agent_sdk.hooks.executor import execute_hook


class TestHooksAPI:
    """Test the decorator-based hooks API."""

    def setup_method(self):
        """Clear registry before each test."""
        clear_registry()

    def test_decorator_registers_and_executes(self):
        """Test that decorators register hooks and they execute properly."""

        async def _test():
            executed = []

            # Test pre_tool_use decorator
            @pre_tool_use(matcher="Bash", timeout=5)
            def check_dangerous_commands(tool_name, tool_input):
                executed.append(("pre", tool_name, tool_input.to_dict()))
                if "rm -rf /" in tool_input.get("command", ""):
                    return PreToolUseHookResponse(
                        permission_decision="deny",
                        permission_decision_reason="Dangerous command blocked",
                    )
                return None  # Allow

            # Verify registration
            registry = get_registry()
            hooks = registry.get_hooks("PreToolUse")
            assert len(hooks) == 1
            assert hooks[0].matcher == "Bash"
            assert hooks[0].timeout == 5

            # Test execution with dangerous command
            result = await execute_hook(
                check_dangerous_commands,
                {"tool_name": "Bash", "tool_input": {"command": "rm -rf /"}},
            )
            assert isinstance(result, PreToolUseHookResponse)
            assert result.permission_decision == "deny"
            assert "Dangerous command blocked" in result.permission_decision_reason

            # Test execution with safe command
            result = await execute_hook(
                check_dangerous_commands,
                {"tool_name": "Bash", "tool_input": {"command": "ls -la"}},
            )
            assert result is None  # Allowed

            # Verify hook was called
            assert len(executed) == 2
            assert executed[0][0] == "pre"
            assert executed[0][1] == "Bash"

        anyio.run(_test)

    def test_registry_lifecycle(self):
        """Test registry clear and isolation between tests."""

        # Register some hooks
        @pre_tool_use()
        def hook1():
            pass

        @post_tool_use(matcher="Write")
        def hook2():
            pass

        registry = get_registry()
        assert len(registry.get_hooks("PreToolUse")) == 1
        assert len(registry.get_hooks("PostToolUse")) == 1

        # Clear registry
        clear_registry()
        assert len(registry.get_hooks("PreToolUse")) == 0
        assert len(registry.get_hooks("PostToolUse")) == 0

        # Register new hooks - verify no interference
        @pre_tool_use(matcher="Read")
        def hook3():
            pass

        assert len(registry.get_hooks("PreToolUse")) == 1
        assert registry.get_hooks("PreToolUse")[0].matcher == "Read"

    def test_parameter_introspection(self):
        """Test that hooks only receive the parameters they request."""

        async def _test():
            received_params = {}

            # Hook that only wants tool_name
            def minimal_hook(tool_name):
                received_params["minimal"] = {"tool_name": tool_name}
                return None

            # Hook that wants multiple params
            def full_hook(tool_name, tool_input, tool_use_id):
                received_params["full"] = {
                    "tool_name": tool_name,
                    "tool_input": tool_input.to_dict(),
                    "tool_use_id": tool_use_id,
                }
                return None

            # Test minimal hook - should only get tool_name
            await execute_hook(
                minimal_hook,
                {
                    "tool_name": "TestTool",
                    "tool_input": {"data": "test"},
                    "extra": "ignored",
                },
                tool_use_id="123",
            )

            assert "minimal" in received_params
            assert received_params["minimal"] == {"tool_name": "TestTool"}

            # Test full hook - should get all requested params
            await execute_hook(
                full_hook,
                {
                    "tool_name": "TestTool",
                    "tool_input": {"data": "test"},
                    "extra": "also_ignored",
                },
                tool_use_id="456",
            )

            assert "full" in received_params
            assert received_params["full"]["tool_name"] == "TestTool"
            assert received_params["full"]["tool_input"] == {"data": "test"}
            assert received_params["full"]["tool_use_id"] == "456"

        anyio.run(_test)
