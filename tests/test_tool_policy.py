from llm_security_lab.tool_policy import ToolPolicy


def test_unlisted_tool_is_denied():
    policy = ToolPolicy(allowed_tools={"search"})
    assert policy.evaluate("send_email") == "deny"


def test_sensitive_tool_requires_approval():
    policy = ToolPolicy(
        allowed_tools={"search", "send_email"},
        require_approval_for={"send_email"},
    )
    assert policy.evaluate("send_email") == "require_approval"


def test_low_risk_tool_is_allowed():
    policy = ToolPolicy(allowed_tools={"search"})
    assert policy.evaluate("search") == "allow"
