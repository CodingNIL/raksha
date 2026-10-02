"""
Gemini client for fraud-analysis reasoning.

This module:
- Creates the Gemini client securely from GEMINI_API_KEY.
- Uses Gemini Interactions API.
- Requests structured JSON output.
- Retries temporary service errors.
- Validates the returned structure.
"""

import json
import os
import time

from google import genai

from backend.services.fraud_engine.taxonomy import (
    get_signal_names,
)


GEMINI_MODEL = "gemini-3.8-flash"

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 3

# Detailed fraud-analysis prompts may take longer than
# the SDK default HTTP timeout.
GEMINI_TIMEOUT_MS = 120000


def get_gemini_client() -> genai.Client:
    """
    Create and return a Gemini client.

    The API key must be supplied through GEMINI_API_KEY.
    """

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY environment variable is not set."
        )

    return genai.Client(
        api_key=api_key,
        http_options={
            "timeout": GEMINI_TIMEOUT_MS
        },
    )


def build_response_schema() -> dict:
    """
    Return the structured JSON schema expected from Gemini.
    """

    return {
        "type": "object",
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
    """
    Validate the basic structure returned by Gemini.

    Validation errors are raised as RuntimeError because
    malformed model responses are treated as runtime
    service failures.
    """

    if not isinstance(data, dict):
        raise RuntimeError(
            "Gemini response must be a JSON object."
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
                f"Gemini response missing required field: {field}"
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
                f"Gemini field '{field}' must be a list."
            )

    valid_signals = set(
        get_signal_names()
    )

    for signal in data["additional_signals"]:
        if not isinstance(signal, str):
            raise RuntimeError(
                "Gemini additional_signals must contain only strings."
            )

        if signal not in valid_signals:
            raise RuntimeError(
                f"Gemini returned unknown fraud signal: {signal}"
            )

    if not isinstance(data["context"], dict):
        raise RuntimeError(
            "Gemini field 'context' must be an object."
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
                f"Gemini context missing field: {field}"
            )

        if not isinstance(
            data["context"][field],
            bool,
        ):
            raise RuntimeError(
                f"Gemini context field '{field}' must be boolean."
            )

    if not isinstance(
        data["explanation"],
        str,
    ):
        raise RuntimeError(
            "Gemini field 'explanation' must be a string."
        )

    return data


def analyze_with_gemini(prompt: str) -> dict:
    """
    Send a fraud-analysis prompt to Gemini.

    Temporary API failures are retried.
    """

    if not prompt or not prompt.strip():
        raise ValueError(
            "Gemini prompt cannot be empty."
        )

    client = get_gemini_client()

    response_schema = build_response_schema()

    last_error = None

    for attempt in range(MAX_RETRIES):
        try:
            interaction = client.interactions.create(
                model=GEMINI_MODEL,
                input=prompt,
                response_format={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": response_schema,
                },
            )

            response_text = interaction.output_text

            if not response_text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            try:
                parsed_response = json.loads(
                    response_text
                )
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    "Gemini returned invalid JSON."
                ) from exc

            return validate_response(
                parsed_response
            )

        except Exception as exc:
            last_error = exc

            error_text = str(exc).lower()

            temporary_error = (
                "503" in error_text
                or "service unavailable" in error_text
                or "temporarily unavailable" in error_text
                or "high demand" in error_text
                or "429" in error_text
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
                f"Gemini API request failed: {last_error}"
            ) from last_error

    raise RuntimeError(
        f"Gemini API request failed: {last_error}"
    )