"""
Groq client for fraud-analysis reasoning.
"""

import json
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from backend.services.fraud_engine.taxonomy import get_signal_names


# Load backend/.env explicitly
BACKEND_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BACKEND_DIR / ".env"

load_dotenv(ENV_FILE)


GROQ_MODEL = "openai/gpt-oss-120b"

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 3


def get_groq_client() -> Groq:
    """Create and return a Groq client."""

    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY environment variable is not set."
        )

    return Groq(api_key=api_key)


def build_response_schema() -> dict:
    """Return the strict JSON schema expected from the LLM."""

    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "additional_signals": {
                "type": "array",
                "items": {
                    "type": "string"
                },
            },
            "evidence": {
                "type": "array",
                "items": {
                    "type": "string"
                },
            },
            "entities": {
                "type": "array",
                "items": {
                    "type": "string"
                },
            },
            "claims": {
                "type": "array",
                "items": {
                    "type": "string"
                },
            },
            "context": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "financial_pressure": {
                        "type": "boolean"
                    },
                    "payment_request": {
                        "type": "boolean"
                    },
                    "sensitive_information_request": {
                        "type": "boolean"
                    },
                    "impersonation": {
                        "type": "boolean"
                    },
                    "unrealistic_promise": {
                        "type": "boolean"
                    },
                },
                "required": [
                    "financial_pressure",
                    "payment_request",
                    "sensitive_information_request",
                    "impersonation",
                    "unrealistic_promise",
                ],
            },
            "explanation": {
                "type": "string"
            },
        },
        "required": [
            "additional_signals",
            "evidence",
            "entities",
            "claims",
            "context",
            "explanation",
        ],
    }


def validate_response(data: dict) -> dict:
    """Validate the structure returned by the LLM."""

    if not isinstance(data, dict):
        raise RuntimeError(
            "Groq response must be a JSON object."
        )

    required_fields = [
        "additional_signals",
        "evidence",
        "entities",
        "claims",
        "context",
        "explanation",
    ]

    for field in required_fields:
        if field not in data:
            raise RuntimeError(
                f"Groq response missing required field: {field}"
            )

    list_fields = [
        "additional_signals",
        "evidence",
        "entities",
        "claims",
    ]

    for field in list_fields:
        if not isinstance(data[field], list):
            raise RuntimeError(
                f"Groq field '{field}' must be a list."
            )

        for item in data[field]:
            if not isinstance(item, str):
                raise RuntimeError(
                    f"Groq field '{field}' must contain only strings."
                )

    valid_signals = set(get_signal_names())

    for signal in data["additional_signals"]:
        if signal not in valid_signals:
            raise RuntimeError(
                f"Groq returned unknown fraud signal: {signal}"
            )

    if not isinstance(data["context"], dict):
        raise RuntimeError(
            "Groq field 'context' must be an object."
        )

    context_fields = [
        "financial_pressure",
        "payment_request",
        "sensitive_information_request",
        "impersonation",
        "unrealistic_promise",
    ]

    for field in context_fields:
        if field not in data["context"]:
            raise RuntimeError(
                f"Groq context missing field: {field}"
            )

        if not isinstance(data["context"][field], bool):
            raise RuntimeError(
                f"Groq context field '{field}' must be boolean."
            )

    if not isinstance(data["explanation"], str):
        raise RuntimeError(
            "Groq field 'explanation' must be a string."
        )

    return data


def analyze_with_groq(prompt: str) -> dict:
    """Send a fraud-analysis prompt to Groq."""

    if not prompt or not prompt.strip():
        raise ValueError(
            "Groq prompt cannot be empty."
        )

    client = get_groq_client()

    response_schema = build_response_schema()

    last_error = None

    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "fraud_analysis",
                        "strict": True,
                        "schema": response_schema,
                    },
                },
            )

            if not response.choices:
                raise RuntimeError(
                    "Groq returned no choices."
                )

            message = response.choices[0].message
            response_text = message.content

            if not response_text:
                raise RuntimeError(
                    "Groq returned an empty response."
                )

            try:
                parsed_response = json.loads(
                    response_text
                )
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    "Groq returned invalid JSON."
                ) from exc

            return validate_response(
                parsed_response
            )

        except Exception as exc:
            last_error = exc

            error_text = str(exc).lower()

            temporary_error = (
                "429" in error_text
                or "rate limit" in error_text
                or "503" in error_text
                or "service unavailable" in error_text
                or "temporarily unavailable" in error_text
                or "timeout" in error_text
                or "timed out" in error_text
            )

            if (
                temporary_error
                and attempt < MAX_RETRIES - 1
            ):
                time.sleep(
                    RETRY_DELAY_SECONDS
                )
                continue

            raise RuntimeError(
                f"Groq API request failed: {last_error}"
            ) from last_error

    raise RuntimeError(
        f"Groq API request failed: {last_error}"
    )


def analyze_with_gemini(prompt: str) -> dict:
    """
    Backward-compatible wrapper.

    The existing reasoning layer still imports this name,
    but the actual provider is Groq.
    """

    return analyze_with_groq(prompt)