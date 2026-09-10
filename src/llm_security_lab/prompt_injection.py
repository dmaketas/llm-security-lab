from dataclasses import dataclass
import re

@dataclass(frozen=True)
class PromptRisk:
    score: int
    level: str
    indicators: tuple[str, ...]

_PATTERN_SPECS = (
    ("instruction_override",
     r"\b(ignore|disregard|forget|override)\b.{0,60}\b(previous|prior|above|system|developer|instructions?)\b", 35),
    ("system_prompt_request",
     r"\b(system prompt|hidden instructions|developer message|internal instructions|secret instructions)\b", 30),
    ("role_override",
     r"\b(you are now|act as if|new instructions|replace your instructions|switch roles?)\b", 25),
    ("secret_exfiltration",
     r"\b(api key|password|secret|token|credential|private key)\b.{0,60}\b(show|print|reveal|send|return|expose|leak)\b", 40),
    ("tool_manipulation",
     r"\b(call|invoke|run|execute|use)\b.{0,45}\b(tool|function|api|connector)\b.{0,60}\b(without approval|without permission|regardless|bypass)\b", 35),
    ("authorization_bypass",
     r"\b(bypass|disable|ignore|circumvent)\b.{0,45}\b(authorization|permission|access control|safety|policy|guardrail)\b", 40),
)

_PATTERNS = tuple(
    (name, re.compile(pattern, re.IGNORECASE | re.DOTALL), weight)
    for name, pattern, weight in _PATTERN_SPECS
)

def assess_prompt(text: str) -> PromptRisk:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indicators = []
    score = 0
    for name, pattern, weight in _PATTERNS:
        if pattern.search(text):
            indicators.append(name)
            score += weight
    score = min(score, 100)
    level = "high" if score >= 60 else "medium" if score >= 30 else "low"
    return PromptRisk(score, level, tuple(indicators))
