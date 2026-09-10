from dataclasses import dataclass
from .prompt_injection import assess_prompt

@dataclass(frozen=True)
class RetrievedContentRisk:
    source: str
    score: int
    level: str
    indicators: tuple[str, ...]
    should_quarantine: bool

def assess_retrieved_content(content: str, source: str = "unknown", quarantine_threshold: int = 60) -> RetrievedContentRisk:
    if not 0 <= quarantine_threshold <= 100:
        raise ValueError("quarantine_threshold must be between 0 and 100")
    result = assess_prompt(content)
    return RetrievedContentRisk(
        source, result.score, result.level, result.indicators,
        result.score >= quarantine_threshold
    )
