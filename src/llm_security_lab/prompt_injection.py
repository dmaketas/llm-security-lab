from dataclasses import dataclass
import re


@dataclass(frozen=True)
class PromptRisk:
    score: int
    level: str
    indicators: tuple[str, ...]


_PATTERNS: tuple[tuple[str, re.Pattern[str], int], ...] = (
    (
        "instruction_override",
        re.compile(
            r"\b(ignore|disregard|forget)\b.{0,40}\b(previous|prior|above|system)\b",
            re.IGNORECASE | re.DOTALL,
        ),
        35,
    ),
    (
        "system_prompt_request",
        re.compile(
            r"\b(system prompt|hidden instructions|developer message|internal instructions)\b",
            re.IGNORECASE,
        ),
        30,
    ),
    (
        "role_override",
        re.compile(
            r"\b(you are now|act as if|new instructions|replace your instructions)\b",
            re.IGNORECASE,
        ),
        25,
    ),
    (
        "secret_exfiltration",
        re.compile(
            r"\b(api key|password|secret|token|credential)\b.{0,40}\b(show|print|reveal|send|return)\b",
            re.IGNORECASE | re.DOTALL,
        ),
        35,
    ),
)


def assess_prompt(text: str) -> PromptRisk:
    """Return a simple heuristic risk assessment for a prompt."""
    indicators: list[str] = []
    score = 0

    for name, pattern, weight in _PATTERNS:
        if pattern.search(text):
            indicators.append(name)
            score += weight

    score = min(score, 100)

    if score >= 60:
        level = "high"
    elif score >= 30:
        level = "medium"
    else:
        level = "low"

    return PromptRisk(score=score, level=level, indicators=tuple(indicators))
