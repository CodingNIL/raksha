"""
LLM reasoning integration for the SANGYAN fraud detection engine.

This module connects:
    rule-based fraud analysis
            ↓
    prompt builder
            ↓
    Gemini client

It does not calculate the final fraud risk score.
The deterministic fraud engine remains responsible for scoring.
"""

from backend.services.llm.client import analyze_with_gemini
from backend.services.llm.prompt_builder import (
    build_fraud_reasoning_prompt,
)


def analyze_with_llm(
    text: str,
    language: str,
    rule_signals: list[str],
    rule_evidence: dict,
) -> dict:
    """
    Perform contextual fraud reasoning using the LLM.

    Args:
        text: Original user message.
        language: Detected language.
        rule_signals: Signals already detected by the rule engine.
        rule_evidence: Evidence already detected by the rule engine.

    Returns:
        Validated LLM fraud-analysis response.
    """

    if not text or not text.strip():
        raise ValueError(
            "Text cannot be empty."
        )

    prompt = build_fraud_reasoning_prompt(
        text=text,
        language=language,
        rule_signals=rule_signals,
        rule_evidence=rule_evidence,
    )

    return analyze_with_gemini(prompt)