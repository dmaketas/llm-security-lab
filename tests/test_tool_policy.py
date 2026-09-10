from llm_security_lab.tool_policy import ToolPolicy

def test_policy():
    p = ToolPolicy({"search", "send_email"}, {"send_email"})
    assert p.evaluate("search") == "allow"
    assert p.evaluate("send_email") == "require_approval"
    assert p.evaluate("delete_records") == "deny"
