"""
Main fraud detection engine.

Pipeline:

User Text
    |
Normalization
    |
Language Detection
    |
Rule Detection
    |
Risk Scoring
    |
Safe Actions
"""

from .normalizer import normalize_text
from .rules import detect_rule_signals
from .scoring import calculate_risk

from backend.services.language.detector import (
    detect_language,
    get_language_details,
)


def generate_safe_actions(signals: list[str]) -> list[str]:
    """
    Generate safety recommendations based on
    detected fraud signals.
    """

    actions = []

    if "sensitive_data_request" in signals:
        actions.append(
            "Do not share OTP, PIN, password, CVV, or other sensitive information."
        )

    if "payment_request" in signals:
        actions.append(
            "Do not transfer money until the request and recipient are independently verified."
        )

    if "personal_account_payment" in signals:
        actions.append(
            "Avoid sending investment-related payments to personal accounts or UPI IDs."
        )

    if "unknown_app_or_apk" in signals:
        actions.append(
            "Do not install unknown APKs or applications received through messages."
        )

    if "impersonation" in signals or "fake_regulatory_claim" in signals:
        actions.append(
            "Verify the organization independently using official sources."
        )

    if "urgency" in signals or "social_pressure" in signals:
        actions.append(
            "Do not make rushed financial decisions because of pressure."
        )

    if "withdrawal_or_recovery_fee" in signals:
        actions.append(
            "Verify withdrawal or recovery claims before paying any fee."
        )

    if not actions:
        actions.append(
            "Verify important financial claims independently before taking action."
        )

    return actions



def analyze_text(text: str) -> dict:
    """
    Analyze a financial message.

    Returns:

    {
        language,
        fraud_analysis,
        risk,
        safe_actions
    }
    """

    if not text or not text.strip():

        return {
            "success": False,
            "message": "Please provide a message to analyze."
        }


    # ---------------------------------------------------------
    # Normalize input
    # ---------------------------------------------------------

    normalized_text = normalize_text(text)


    # ---------------------------------------------------------
    # Language detection
    # ---------------------------------------------------------

    language_details = get_language_details(
        normalized_text
    )


    # ---------------------------------------------------------
    # Fraud rule detection
    # ---------------------------------------------------------

    rule_result = detect_rule_signals(
        normalized_text
    )


    signals = rule_result["signals"]

    evidence = rule_result["evidence"]


    # ---------------------------------------------------------
    # Risk calculation
    # ---------------------------------------------------------

    risk_result = calculate_risk(
        signals
    )


    # ---------------------------------------------------------
    # Safety actions
    # ---------------------------------------------------------

    safe_actions = generate_safe_actions(
        signals
    )


    return {

        "success": True,


        "input": {

            "original_text": text,

            "normalized_text": normalized_text

        },


        "language": language_details,


        "fraud_analysis": {

            "signals": signals,

            "evidence": evidence

        },


        "risk": {

            "score": risk_result["score"],

            "level": risk_result["level"],

            "reasons": risk_result["reasons"]

        },


        "safe_actions": safe_actions

    }