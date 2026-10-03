"""
Fraud taxonomy for the SANGYAN fraud detection engine.

These are the fraud-signal categories that the system can identify.
"""

FRAUD_TAXONOMY = {
    "guaranteed_returns": {
        "name": "Guaranteed Returns",
        "description": (
            "Claims that investment returns or profits are guaranteed."
        )
    },

    "unrealistic_returns": {
        "name": "Unrealistic Returns",
        "description": (
            "Promises unusually high or unrealistic investment returns."
        )
    },

    "no_loss_claim": {
        "name": "No-Loss Claim",
        "description": (
            "Claims that the investor cannot lose money."
        )
    },

    "urgency": {
        "name": "Urgency",
        "description": (
            "Creates pressure to act immediately or within a short period."
        )
    },

    "social_pressure": {
        "name": "Social Pressure",
        "description": (
            "Uses pressure, fear, authority, or social influence "
            "to force a decision."
        )
    },

    "impersonation": {
        "name": "Impersonation",
        "description": (
            "Pretends to represent a regulator, bank, broker, company, "
            "official, or another trusted entity."
        )
    },

    "fake_regulatory_claim": {
        "name": "Fake Regulatory Claim",
        "description": (
            "Uses false or suspicious claims involving regulatory "
            "approval, registration, certification, or authority."
        )
    },

    "payment_request": {
        "name": "Payment Request",
        "description": (
            "Requests money, fees, deposits, transfers, or other payments."
        )
    },

    "personal_account_payment": {
        "name": "Personal Account Payment",
        "description": (
            "Requests payment to a personal bank account, UPI ID, "
            "wallet, or other personal payment destination."
        )
    },

    "sensitive_data_request": {
        "name": "Sensitive Data Request",
        "description": (
            "Requests sensitive information such as OTP, PIN, password, "
            "card details, or other confidential information."
        )
    },

    "unknown_app_or_apk": {
        "name": "Unknown App or APK",
        "description": (
            "Asks the user to install an unknown application, APK, "
            "or suspicious software."
        )
    },

    "withdrawal_or_recovery_fee": {
        "name": "Withdrawal or Recovery Fee",
        "description": (
            "Requests a fee to withdraw funds, recover money, "
            "release an investment, or unlock an account."
        )
    }
}


def get_taxonomy():
    """
    Return the complete fraud taxonomy.
    """
    return FRAUD_TAXONOMY


def get_signal_names():
    """
    Return all fraud-signal category names.
    """
    return list(FRAUD_TAXONOMY.keys())
