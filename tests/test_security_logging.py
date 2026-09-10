import json
from llm_security_lab.security_logging import append_jsonl, build_security_event

def test_log(tmp_path):
    event = build_security_event(event_type="test", severity="high", source="unit", score=80)
    p = tmp_path / "events.jsonl"
    append_jsonl(event, p)
    assert json.loads(p.read_text())["score"] == 80
