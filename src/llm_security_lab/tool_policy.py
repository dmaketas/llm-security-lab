from dataclasses import dataclass, field


@dataclass
class ToolPolicy:
    """Minimal allow-list policy for model-triggered tool calls."""

    allowed_tools: set[str] = field(default_factory=set)
    require_approval_for: set[str] = field(default_factory=set)

    def evaluate(self, tool_name: str) -> str:
        if tool_name not in self.allowed_tools:
            return "deny"
        if tool_name in self.require_approval_for:
            return "require_approval"
        return "allow"
