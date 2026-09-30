"""
Risk scoring for detected fraud signals.

The weights and thresholds are initial values from
the SANGYAN fraud-engine build plan.
"""

SIGNAL_WEIGHTS = {
    "guaranteed_returns": 3,
    "unrealistic_returns": 2,
    "no_loss_claim": 3,
    "urgency": 1,
    "social_pressure": 1,
    "impersonation": 3,
    "fake_regulatory_claim": 3,
    "payment_request": 2,
    "personal_account_payment": 3,
    "sensitive_data_request": 3,
    "unknown_app_or_apk": 2,
    "withdrawal_or_recovery_fee": 3,
}


def calculate_risk(signals: list[str]) -> dict:
    """
    Calculate the initial risk score from detected fraud signals.

    Args:
        signals: List of detected fraud-signal names.

    Returns:
        Dictionary containing:
        - score
        - level
        - reasons
    """

    score = 0
    reasons = []

    for signal in signals:
        weight = SIGNAL_WEIGHTS.get(signal, 0)

        score += weight

        if weight > 0:
            reasons.append({
                "signal": signal,
                "weight": weight
            })

    if score <= 2:
        level = "LOW APPARENT RISK"

    elif score <= 5:
        level = "NEEDS VERIFICATION"

    else:
        level = "HIGH-RISK PATTERN"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }