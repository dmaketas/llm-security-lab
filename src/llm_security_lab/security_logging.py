from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Iterable

@dataclass(frozen=True)
class SecurityEvent:
    timestamp: str
    event_type: str
    severity: str
    source: str
    score: int
    indicators: tuple[str, ...]

def build_security_event(*, event_type: str, severity: str, source: str, score: int, indicators: Iterable[str] = ()) -> SecurityEvent:
    return SecurityEvent(
        datetime.now(timezone.utc).isoformat(),
        event_type, severity, source, score, tuple(indicators)
    )

def append_jsonl(event: SecurityEvent, path: str | Path) -> None:
    with Path(path).open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(event), sort_keys=True) + "\n")
