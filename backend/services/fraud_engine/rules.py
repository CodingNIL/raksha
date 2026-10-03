"""
Rule-based fraud signal detector.

This module applies the patterns defined in patterns.py
and returns detected fraud signals along with evidence.

It also performs basic contextual filtering so that
legitimate warning messages are not automatically treated
as fraud requests.
"""

import re

from .patterns import FRAUD_PATTERNS


# ------------------------------------------------------------------
# NEGATION / WARNING PHRASES
# ------------------------------------------------------------------

NEGATION_PATTERNS = [
    r"\bnever\b",
    r"\bdo\s+not\b",
    r"\bdon'?t\b",
    r"\bdo\s+not\s+share\b",
    r"\bdon'?t\s+share\b",
    r"\bdo\s+not\s+give\b",
    r"\bdon'?t\s+give\b",
    r"\bdo\s+not\s+send\b",
    r"\bdon'?t\s+send\b",
    r"\bdo\s+not\s+provide\b",
    r"\bdon'?t\s+provide\b",
    r"\bavoid\s+sharing\b",
    r"\bavoid\s+sending\b",
    r"\bavoid\s+giving\b",
]


# Bengali standalone negation/warning words.
#
# IMPORTANT:
# Do not simply search for the characters "না".
# For example, "আপনার" contains "না", but it is NOT
# a negation. We therefore require a Bengali word boundary
# using the surrounding non-Bengali-letter context.
BENGALI_NEGATION_PATTERNS = [
    r"(?<![\u0980-\u09FF])না(?![\u0980-\u09FF])",
    r"(?<![\u0980-\u09FF])করবেন\s+না(?![\u0980-\u09FF])",
    r"(?<![\u0980-\u09FF])করবেননা(?![\u0980-\u09FF])",
    r"(?<![\u0980-\u09FF])দেবেন\s+না(?![\u0980-\u09FF])",
    r"(?<![\u0980-\u09FF])দেবেননা(?![\u0980-\u09FF])",
]


def is_negated(text: str, match_start: int) -> bool:
    """
    Check whether a detected phrase is preceded by a
    negation or warning phrase.

    Example:

        "Never share your OTP"

    The phrase "share your OTP" should not be treated
    as a request for an OTP.

    Args:
        text: Complete normalized text.
        match_start: Character position where the match begins.

    Returns:
        True if the match appears to be negated.
    """

    # Look at the text immediately before the detected phrase.
    context_start = max(0, match_start - 50)

    previous_text = text[context_start:match_start].lower()

    # English negation/warning phrases.
    for pattern in NEGATION_PATTERNS:
        if re.search(pattern, previous_text, flags=re.IGNORECASE):
            return True

    # Bengali negation/warning phrases.
    for pattern in BENGALI_NEGATION_PATTERNS:
        if re.search(pattern, previous_text):
            return True

    return False


def has_following_bengali_negation(
    text: str,
    match_end: int,
    max_chars: int = 16,
) -> bool:
    """
    Check whether a sensitive-data request is followed by
    an actual standalone Bengali negation.

    Example that SHOULD be treated as a warning:

        "OTP দিন না"

    Example that MUST NOT be treated as a negation:

        "OTP দিন আপনার account verify করার জন্য"

    The old implementation searched for the two characters
    "না" anywhere in the following text. That incorrectly
    matched words such as "আপনার".
    """

    following_text = text[match_end:match_end + max_chars]

    for pattern in BENGALI_NEGATION_PATTERNS:
        if re.search(pattern, following_text):
            return True

    return False


def find_pattern_matches(
    text: str,
    pattern: str,
    check_following_negation: bool = False,
) -> list[str]:
    """
    Find regex matches while filtering out basic negated contexts.

    Args:
        text: Normalized text.
        pattern: Regex pattern.
        check_following_negation: Whether to check for Bengali
            post-match negation.

    Returns:
        List of valid matched phrases.
    """

    matches = []

    for match in re.finditer(
        pattern,
        text,
        flags=re.IGNORECASE,
    ):
        match_text = match.group(0).strip()

        if not match_text:
            continue

        # Ignore matches that occur inside a warning/negated sentence.
        if is_negated(text, match.start()):
            continue

        # For sensitive-data requests, check for a real
        # standalone Bengali negation after the match.
        if check_following_negation:
            if has_following_bengali_negation(
                text,
                match.end(),
            ):
                continue

        if match_text not in matches:
            matches.append(match_text)

    return matches


def detect_rule_signals(text: str) -> dict:
    """
    Detect fraud signals using predefined regex patterns.

    Args:
        text: Normalized user message.

    Returns:
        Dictionary containing:

        {
            "signals": [...],
            "evidence": {
                "signal_name": [...]
            }
        }
    """

    if not text or not text.strip():
        return {
            "signals": [],
            "evidence": {},
        }

    detected_signals = []
    evidence = {}

    for signal_name, patterns in FRAUD_PATTERNS.items():

        matches = []

        for pattern in patterns:

            pattern_matches = find_pattern_matches(
                text,
                pattern,
                check_following_negation=(
                    signal_name == "sensitive_data_request"
                ),
            )

            for match_text in pattern_matches:

                if match_text not in matches:
                    matches.append(match_text)

        if matches:
            detected_signals.append(signal_name)
            evidence[signal_name] = matches

    return {
        "signals": detected_signals,
        "evidence": evidence,
    }