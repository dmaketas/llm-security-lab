from dataclasses import dataclass

from .prompt_injection import assess_prompt


@dataclass(frozen=True)
class RetrievedContentRisk:
    source: str
    score: int
    level: str
    indicators: tuple[str, ...]


def assess_retrieved_content(content: str, source: str = "unknown") -> RetrievedContentRisk:
    """Assess retrieved text before it is inserted into an LLM context."""
    result = assess_prompt(content)

    return RetrievedContentRisk(
        source=source,
        score=result.score,
        level=result.level,
        indicators=result.indicators,
    )
