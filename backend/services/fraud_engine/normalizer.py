"""
Text normalization utilities.

The normalizer cleans user input while preserving
the original language and meaning.
"""

import re
import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize user-provided text.

    This function:
    - Handles Unicode consistently
    - Removes unnecessary whitespace
    - Preserves the original language
    - Does NOT translate the message
    """

    if not text:
        return ""

    # Unicode normalization
    text = unicodedata.normalize("NFKC", text)

    # Normalize different types of whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text
