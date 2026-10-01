"""
Suspicious text patterns for the fraud detection engine.

These patterns detect common fraud signals before
contextual AI reasoning is added.

The patterns support:
- English
- Mixed English + Bengali
- Mixed English + Hindi
- Common multilingual financial-message formats
"""

FRAUD_PATTERNS = {

    "guaranteed_returns": [
        r"\bguaranteed\s+(?:return|returns|profit|profits)\b",
        r"\bguaranteed\s+\d+(?:\.\d+)?\s*%",
        r"\bguaranteed\s+\d+(?:\.\d+)?\s*%\s*(?:return|returns|profit|profits)\b",
        r"\bguaranteed\s+income\b",
        r"\bguaranteed\s+profit\b",
        r"\bno\s+risk\s+(?:investment|return|profit)\b",
    ],


    "unrealistic_returns": [
        r"\b\d{2,3}(?:\.\d+)?\s*%\s*(?:return|returns|profit|profits)\b",
        r"\b(?:return|returns|profit|profits)\s+(?:of\s+)?\d{2,3}(?:\.\d+)?\s*%\b",
        r"\bearn\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)\b",
        r"\bget\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)\s*(?:return|returns|profit|profits)?\b",
        r"\bmake\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)\s*(?:return|returns|profit|profits)?\b",
        r"\b(?:double|triple)\s+(?:your\s+)?money\b",
        r"\bdouble\s+your\s+investment\b",
        r"\bhuge\s+(?:return|profit|returns|profits)\b",
        r"\bmassive\s+(?:return|profit|returns|profits)\b",
        r"\b(?:extraordinary|exceptional)\s+(?:return|profit|returns|profits)\b",
    ],


    "no_loss_claim": [
        r"\bno\s+loss\b",
        r"\bzero\s+loss\b",
        r"\byou\s+cannot\s+lose\b",
        r"\byou\s+will\s+not\s+lose\b",
        r"\bnever\s+lose\s+money\b",
        r"\b100%\s+safe\b",
    ],


    "urgency": [
        r"\bact\s+now\b",
        r"\bact\s+immediately\b",
        r"\bdo\s+it\s+now\b",
        r"\blimited\s+time\b",
        r"\blimited\s+offer\b",
        r"\btoday\s+only\b",
        r"\bwithin\s+\d+\s*(?:minutes?|hours?)\b",
        r"\bexpires?\s+(?:today|soon)\b",
        r"\blast\s+chance\b",
    ],


    "social_pressure": [
        r"\bdon'?t\s+tell\s+anyone\b",
        r"\bkeep\s+this\s+secret\b",
        r"\bsecret\s+investment\b",
        r"\byou\s+must\s+trust\s+me\b",
        r"\btrust\s+me\b",
        r"\bif\s+you\s+don'?t\s+act\b",
        r"\byou\s+will\s+lose\s+this\s+opportunity\b",
    ],


    "impersonation": [
        r"\b(?:i'?m|i\s+am)\s+(?:from|a)\s+(?:sebi|rbi|bank|government)\b",
        r"\b(?:sebi|rbi)\s+(?:officer|official|agent)\b",
        r"\b(?:bank|government)\s+official\b",
        r"\b(?:official|authorized)\s+(?:representative|agent)\b",
    ],


    "fake_regulatory_claim": [
        r"\bsebi\s+approved\b",
        r"\bsebi\s+certified\b",
        r"\bsebi\s+guaranteed\b",
        r"\brbi\s+approved\b",
        r"\bgovernment\s+approved\s+investment\b",
        r"\bgovernment\s+guaranteed\s+returns\b",
        r"\bofficially\s+approved\s+returns\b",
    ],


    "payment_request": [
        r"\bpay\s+(?:a\s+)?(?:fee|charge|deposit)\b",
        r"\bsend\s+(?:money|payment|funds)\b",
        r"\btransfer\s+(?:money|funds)\b",
        r"\bprocessing\s+fee\b",
        r"\bregistration\s+fee\b",
        r"\bactivation\s+fee\b",
        r"\bdeposit\s+(?:money|funds)\b",
    ],


    "personal_account_payment": [
        r"\bsend\s+(?:money|payment)\s+to\s+my\s+(?:account|upi)\b",
        r"\btransfer\s+(?:money|funds)\s+to\s+my\s+(?:account|upi)\b",
        r"\bpay\s+(?:me|my\s+account)\b",
        r"\bpersonal\s+(?:bank\s+)?account\b",
        r"\bmy\s+personal\s+upi\b",
    ],


    "sensitive_data_request": [

        # -------------------------------------------------------------
        # English
        # -------------------------------------------------------------

        r"\bsend\s+(?:me\s+)?(?:your\s+)?otp\b",
        r"\bshare\s+(?:your\s+)?otp\b",
        r"\bgive\s+(?:me\s+)?(?:your\s+)?otp\b",

        r"\bsend\s+(?:me\s+)?(?:your\s+)?pin\b",
        r"\bshare\s+(?:your\s+)?pin\b",
        r"\bgive\s+(?:me\s+)?(?:your\s+)?pin\b",

        r"\bshare\s+(?:your\s+)?password\b",
        r"\bsend\s+(?:me\s+)?(?:your\s+)?password\b",

        r"\bshare\s+(?:your\s+)?cvv\b",
        r"\bsend\s+(?:your\s+)?card\s+details\b",

        r"\benter\s+(?:your\s+)?bank\s+details\b",
        r"\bprovide\s+(?:your\s+)?bank\s+details\b",

        # -------------------------------------------------------------
        # Multilingual / mixed-language OTP requests
        #
        # These intentionally detect OTP + a request verb.
        # They allow Bengali/Hindi words between the request and OTP.
        # -------------------------------------------------------------

        # Bengali:
        # "আমাকে OTP দিন"
        # "আপনার OTP দিন"
        r"\bOTP\b.{0,30}\b(?:দিন|দাও|দিবেন|দাওয়া)\b",

        r"\b(?:আমাকে|আপনাকে|আপনার)\b.{0,30}\bOTP\b",

        # Hindi:
        # "मुझे अपना OTP भेजो"
        # "अपना OTP भेजो"
        r"\bOTP\b.{0,30}\b(?:भेजो|भेजिए|भेजें|दो|दीजिए)\b",

        r"\b(?:मुझे|अपना|आपका|आपको)\b.{0,30}\bOTP\b",

        # Generic mixed-language OTP request:
        # Useful when English OTP is combined with an Indian-language
        # request phrase.
        r"\b(?:OTP)\b.{0,40}\b(?:verify|verification|account)\b",
    ],


    "unknown_app_or_apk": [
        r"\binstall\s+(?:this\s+)?apk\b",
        r"\bdownload\s+(?:this\s+)?apk\b",
        r"\binstall\s+(?:this\s+)?app\b",
        r"\bdownload\s+(?:this\s+)?app\b",
        r"\binstall\s+(?:our\s+)?application\b",
        r"\bdownload\s+(?:our\s+)?application\b",
    ],


    "withdrawal_or_recovery_fee": [
        r"\bwithdrawal\s+fee\b",
        r"\brecovery\s+fee\b",
        r"\bpay\s+(?:a\s+)?(?:processing\s+)?fee\s+to\s+withdraw\b",
        r"\bpay\s+(?:a\s+)?(?:processing\s+)?fee\s+to\s+recover\b",
        r"\bpay\s+(?:a\s+)?(?:processing\s+)?fee\s+to\s+release\b",
        r"\bunlock\s+(?:your\s+)?(?:account|funds)\b",
        r"\brelease\s+(?:your\s+)?funds\b",
        r"\bfee\s+to\s+release\s+funds\b",
    ],
}