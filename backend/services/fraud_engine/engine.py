"""
Core fraud detection engine for the SANGYAN project.

Pipeline:
    Input text
        ↓
    Normalization
        ↓
    Language detection
        ↓
    Rule-based fraud detection
        ↓
    Optional Gemini contextual reasoning
        ↓
    Merge rule + LLM signals/evidence/context
        ↓
    Final deterministic risk scoring
        ↓
    Safe actions
        ↓
    Structured result
"""

from backend.services.fraud_engine.normalizer import normalize_text
from backend.services.fraud_engine.rules import detect_rule_signals
from backend.services.fraud_engine.scoring import calculate_risk
from backend.services.language.detector import get_language_details
from backend.services.llm.reasoning import analyze_with_llm


def generate_safe_actions(
    signals: list[str],
) -> list[str]:
    """
    Generate safe actions based on the combined fraud signals.

    Signals may come from either:
    - the deterministic rule engine, or
    - contextual LLM reasoning.

    The LLM does not provide financial advice.
    It only helps identify contextual fraud signals
    that can improve safety guidance.
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

    if (
        "impersonation" in signals
        or "fake_regulatory_claim" in signals
    ):
        actions.append(
            "Verify the organization independently using official sources."
        )

    if (
        "urgency" in signals
        or "social_pressure" in signals
    ):
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


def merge_llm_signals(
    rule_signals: list[str],
    llm_result: dict,
) -> list[str]:
    """
    Combine deterministic rule signals with contextual LLM signals.

    Duplicate signals are removed while preserving order.
    """

    combined_signals = list(rule_signals)

    for signal in llm_result.get(
        "additional_signals",
        [],
    ):
        if signal not in combined_signals:
            combined_signals.append(signal)

    return combined_signals


def merge_llm_evidence(
    rule_evidence: dict,
    llm_result: dict,
) -> dict:
    """
    Combine rule-based evidence with contextual LLM evidence.
    """

    combined_evidence = dict(rule_evidence)

    llm_evidence = llm_result.get(
        "evidence",
        [],
    )

    if llm_evidence:
        combined_evidence[
            "llm_contextual_evidence"
        ] = llm_evidence

    return combined_evidence


def build_llm_context(
    llm_result: dict,
) -> dict:
    """
    Extract validated contextual reasoning fields
    returned by the LLM.
    """

    context = llm_result.get(
        "context",
        {},
    )

    return {
        "financial_pressure": context.get(
            "financial_pressure",
            False,
        ),
        "payment_request": context.get(
            "payment_request",
            False,
        ),
        "sensitive_information_request": context.get(
            "sensitive_information_request",
            False,
        ),
        "impersonation": context.get(
            "impersonation",
            False,
        ),
        "unrealistic_promise": context.get(
            "unrealistic_promise",
            False,
        ),
    }


def analyze_text(
    text: str,
    use_llm: bool = False,
) -> dict:
    """
    Analyze a financial message for potential fraud.

    Args:
        text:
            User-provided financial message.

        use_llm:
            Whether contextual Gemini reasoning should be used.

    Returns:
        Structured fraud-analysis result.
    """

    if not text or not text.strip():
        return {
            "success": False,
            "message": "Text cannot be empty.",
        }

    # ---------------------------------------------------------
    # 1. Normalize input
    # ---------------------------------------------------------

    normalized_text = normalize_text(text)

    # ---------------------------------------------------------
    # 2. Detect language
    # ---------------------------------------------------------

    language_details = get_language_details(
        normalized_text
    )

    # ---------------------------------------------------------
    # 3. Run deterministic rule engine
    # ---------------------------------------------------------

    # detect_rule_signals() returns:
    #
    # {
    #     "signals": [...],
    #     "evidence": {...}
    # }
    #
    # Keep this structure intact because the existing
    # fraud engine and tests depend on it.

    rule_result = detect_rule_signals(
        normalized_text
    )

    rule_signals = rule_result["signals"]
    rule_evidence = rule_result["evidence"]

    # ---------------------------------------------------------
    # 4. Initialize combined analysis
    # ---------------------------------------------------------

    combined_signals = list(
        rule_signals
    )

    combined_evidence = dict(
        rule_evidence
    )

    llm_analysis = None
    llm_status = "not_used"
    llm_context = None

    # ---------------------------------------------------------
    # 5. Optional Gemini contextual reasoning
    # ---------------------------------------------------------

    if use_llm:
        try:
            llm_analysis = analyze_with_llm(
                text=normalized_text,
                language=language_details["language"],
                rule_signals=rule_signals,
                rule_evidence=rule_evidence,
            )

            combined_signals = merge_llm_signals(
                rule_signals,
                llm_analysis,
            )

            combined_evidence = merge_llm_evidence(
                rule_evidence,
                llm_analysis,
            )

            llm_context = build_llm_context(
                llm_analysis
            )

            llm_status = "completed"

        except Exception as exc:
            llm_status = "unavailable"

            llm_analysis = {
                "available": False,
                "error": str(exc),
            }

    # ---------------------------------------------------------
    # 6. FINAL risk scoring
    # ---------------------------------------------------------
    #
    # IMPORTANT:
    # Risk scoring happens AFTER LLM signals are merged.
    #
    # This means:
    #
    #     Rule signals
    #          +
    #     LLM signals
    #          ↓
    #     Combined signals
    #          ↓
    #     Final risk score
    #
    # The LLM does NOT directly decide the risk score.
    # The deterministic scoring engine remains responsible
    # for converting recognized signals into the final score
    # and risk level.

    risk_result = calculate_risk(
        combined_signals
    )

    # ---------------------------------------------------------
    # 7. Generate safe actions
    # ---------------------------------------------------------

    # Safe actions use the same combined signal set so that
    # contextual LLM findings can also produce appropriate
    # safety guidance.

    safe_actions = generate_safe_actions(
        combined_signals
    )

    # ---------------------------------------------------------
    # 8. Return structured result
    # ---------------------------------------------------------

    return {
        "success": True,
        "input": {
            "original_text": text,
            "normalized_text": normalized_text,
        },
        "language": language_details,
        "fraud_analysis": {
    "signals": combined_signals,
    "evidence": combined_evidence,
    "entities": (
        llm_analysis.get("entities", [])
        if isinstance(llm_analysis, dict)
        else []
    ),
    "claims": (
        llm_analysis.get("claims", [])
        if isinstance(llm_analysis, dict)
        else []
    ),
    "llm_context": llm_context,
},
        "risk": {
            "score": risk_result["score"],
            "level": risk_result["level"],
            "reasons": risk_result["reasons"],
        },
        "safe_actions": safe_actions,
        "llm_analysis": llm_analysis,
        "llm_status": llm_status,
    }