"""
Suspicious text patterns for the fraud detection engine.

This module contains deterministic patterns for identifying
common digital fraud and scam signals.

The patterns support:
- English
- Bengali
- Hindi
- Banglish
- Hinglish
- Mixed-language financial-message formats

Important:
- These patterns identify suspicious signals.
- They do NOT independently declare a message fraudulent.
- Contextual interpretation is handled by the LLM layer.
"""

FRAUD_PATTERNS = {

   # ------------------------------------------------------------------
   # 1. GUARANTEED RETURNS
   # ------------------------------------------------------------------

   "guaranteed_returns": [

       # English
       r"\bguaranteed\s+(?:return|returns|profit|profits)\b",
       r"\bguaranteed\s+\d+(?:\.\d+)?\s*%",
       r"\bguaranteed\s+\d+(?:\.\d+)?\s*%\s*(?:return|returns|profit|profits)\b",
       r"\bguaranteed\s+income\b",
       r"\bguaranteed\s+profit\b",
       r"\bguaranteed\s+(?:investment\s+)?(?:return|returns|profit|profits)\b",
       r"\bguaranteed\s+investment\s+(?:return|returns|profit|profits)\b",
       r"\bno\s+risk\s+(?:investment|return|profit)\b",
       r"\bguaranteed\s+(?:money|earnings|income)\b",

       # Banglish
       r"\bguaranteed\s+(?:profit|return)\b",
       r"\b(?:guaranteed|sure)\s+(?:labh|profit|return)\b",

       # Bengali
r"নিশ্চিত\s+(?:লাভ|রিটার্ন|আয়)",
       r"(?:গ্যারান্টিড|নিশ্চিত)\s+(?:লাভ|রিটার্ন)",
       r"(?:গ্যারান্টি|নিশ্চিত)\s+(?:লাভ|রিটার্ন)",

       # Hindi
       r"गारंटीड\s+(?:मुनाफा|रिटर्न|लाभ)",
       r"गारंटी\s+(?:मुनाफा|रिटर्न|लाभ)",
       r"निश्चित\s+(?:मुनाफा|रिटर्न|लाभ)",
   ],


   # ------------------------------------------------------------------
   # 2. UNREALISTIC RETURNS
   # ------------------------------------------------------------------

   "unrealistic_returns": [

       # English
       r"\b\d{2,3}(?:\.\d+)?\s*(?:%|percent)\s*(?:return|returns|profit|profits)\b",

       r"\b(?:return|returns|profit|profits)\s+(?:of\s+)?\d{2,3}(?:\.\d+)?\s*(?:%|percent)(?!\w)",

       r"\binvestment\s+(?:return|returns|profit|profits)\s+(?:of\s+)?\d{2,3}(?:\.\d+)?\s*(?:%|percent)(?!\w)",

       r"\bguaranteed\s+investment\s+(?:return|returns|profit|profits)\s+(?:of\s+)?\d{2,3}(?:\.\d+)?\s*(?:%|percent)(?!\w)",

       r"\bearn\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)(?!\w)",

       r"\bget\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)\s*(?:return|returns|profit|profits)?\b",

       r"\bmake\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)\s*(?:return|returns|profit|profits)?\b",

       r"\b(?:double|triple)\s+(?:your\s+)?money\b",

       r"\bdouble\s+your\s+investment\b",

       r"\bhuge\s+(?:return|profit|returns|profits)\b",

       r"\bmassive\s+(?:return|profit|returns|profits)\b",

       r"\b(?:extraordinary|exceptional)\s+(?:return|profit|returns|profits)\b",

       # Banglish
       r"\b\d{2,3}(?:\.\d+)?\s*(?:%|percent)\s*(?:guaranteed\s+)?(?:profit|labh|return)\b",

       # Bengali percentage + profit/return
       r"\d{2,3}(?:\.\d+)?\s*%\s*(?:নিশ্চিত\s+)?(?:লাভ|রিটার্ন)",

       # Hindi percentage + profit/return
       r"\d{2,3}(?:\.\d+)?\s*%\s*(?:गारंटीड\s+)?(?:मुनाफा|लाभ|रिटर्न)",
   ],


   # ------------------------------------------------------------------
   # 3. NO LOSS CLAIM
   # ------------------------------------------------------------------

   "no_loss_claim": [

       # English
       r"\bno\s+loss\b",
       r"\bzero\s+loss\b",
       r"\byou\s+cannot\s+lose\b",
       r"\byou\s+will\s+not\s+lose\b",
       r"\bnever\s+lose\s+money\b",
       r"\b100%\s+safe\b",
       r"\bno\s+chance\s+of\s+loss\b",
       r"\bguaranteed\s+no\s+loss\b",

       # Bengali
       r"কোনও\s+ক্ষতি\s+নেই",
       r"কোনো\s+ক্ষতি\s+নেই",
       r"ক্ষতি\s+হবে\s+না",
       r"কোনও\s+লোকসান\s+নেই",
       r"কোনো\s+লোকসান\s+নেই",

       # Hindi
       r"कोई\s+नुकसान\s+नहीं",
       r"कोई\s+हानि\s+नहीं",
       r"नुकसान\s+नहीं\s+होगा",
   ],


   # ------------------------------------------------------------------
   # 4. URGENCY
   # ------------------------------------------------------------------

   "urgency": [

       # English
       r"\bact\s+now\b",
       r"\bact\s+immediately\b",
       r"\bdo\s+it\s+now\b",
       r"\bdo\s+this\s+now\b",
       r"\bimmediately\b",
       r"\burgent(?:ly)?\b",
       r"\bright\s+now\b",
       r"\bas\s+soon\s+as\s+possible\b",
       r"\blimited\s+time\b",
       r"\blimited\s+offer\b",
       r"\btoday\s+only\b",
       r"\bwithin\s+\d+\s*(?:minutes?|hours?)\b",
       r"\bexpires?\s+(?:today|soon)\b",
       r"\blast\s+chance\b",
       r"\btime\s+sensitive\b",

       # Banglish
       r"\bekhoni\b",
       r"\bekhon\s+e\b",
       r"\btaratari\b",
       r"\bshigroi\b",
       r"\bakhoni\b",

       # Hinglish
       r"\babhi\b",
       r"\bturant\b",
       r"\bjaldi\b",
       r"\bfauran\b",
       r"\bforan\b",

       # Bengali
       r"এখনই",
       r"তাড়াতাড়ি",
       r"শীঘ্রই",
       r"আজই",
       r"জরুরি",
       r"অবিলম্বে",

       # Hindi
       r"अभी",
       r"तुरंत",
       r"जल्दी",
       r"आज\s+ही",
       r"तत्काल",
       r"अति\s+आवश्यक",
   ],


   # ------------------------------------------------------------------
   # 5. SOCIAL PRESSURE
   # ------------------------------------------------------------------

   "social_pressure": [

       # English
       r"\bdon'?t\s+tell\s+anyone\b",
       r"\bkeep\s+this\s+secret\b",
       r"\bsecret\s+investment\b",
       r"\byou\s+must\s+trust\s+me\b",
       r"\btrust\s+me\b",
       r"\bif\s+you\s+don'?t\s+act\b",
       r"\byou\s+will\s+lose\s+this\s+opportunity\b",
       r"\bdon'?t\s+miss\s+(?:this\s+)?opportunity\b",
       r"\bact\s+before\s+it'?s\s+too\s+late\b",

       # Banglish
       r"\bkauke\s+bolo\s+na\b",
       r"\bgopon\s+rakho\b",

       # Bengali
       r"কাউকে\s+বলবেন\s+না",
       r"গোপন\s+রাখুন",
       r"এই\s+সুযোগ\s+মিস\s+করবেন\s+না",

       # Hindi
       r"किसी\s+को\s+मत\s+बताओ",
       r"गुप्त\s+रखें",
       r"यह\s+मौका\s+मत\s+गंवाएं",
   ],


   # ------------------------------------------------------------------
   # 6. IMPERSONATION
   # ------------------------------------------------------------------

   "impersonation": [

       # English
       r"\b(?:i'?m|i\s+am)\s+(?:from|a)\s+(?:sebi|rbi|bank|government)\b",
       r"\b(?:sebi|rbi)\s+(?:officer|official|agent)\b",
       r"\b(?:bank|government)\s+official\b",
       r"\b(?:official|authorized)\s+(?:representative|agent)\b",
       r"\b(?:sebi|rbi|bank)\s+representative\b",
       r"\b(?:bank|sebi|rbi)\s+support\s+team\b",

       # Bengali
       r"আমি\s+(?:সেবি|আরবিআই|ব্যাংক|সরকার)\s+থেকে",
       r"(?:ব্যাংক|সরকারি)\s+কর্মকর্তা",

       # Hindi
       r"मैं\s+(?:सेबी|आरबीआई|बैंक|सरकार)\s+से",
       r"(?:बैंक|सरकारी)\s+अधिकारी",
   ],


   # ------------------------------------------------------------------
   # 7. FAKE REGULATORY CLAIM
   # ------------------------------------------------------------------

   "fake_regulatory_claim": [

       # English
       r"\bsebi\s+approved\b",
       r"\bsebi\s+certified\b",
       r"\bsebi\s+guaranteed\b",
       r"\brbi\s+approved\b",
       r"\brbi\s+certified\b",
       r"\bgovernment\s+approved\s+investment\b",
       r"\bgovernment\s+guaranteed\s+returns\b",
       r"\bofficially\s+approved\s+returns\b",
       r"\bgovernment\s+approved\s+returns\b",

       # Bengali
       r"সেবি\s+অনুমোদিত",
       r"আরবিআই\s+অনুমোদিত",
       r"সরকারি\s+অনুমোদিত",

       # Hindi
       r"सेबी\s+अनुमोदित",
       r"आरबीआई\s+अनुमोदित",
       r"सरकार\s+द्वारा\s+अनुमोदित",
   ],


   # ------------------------------------------------------------------
   # 8. PAYMENT REQUEST
   # ------------------------------------------------------------------

   "payment_request": [

       # English
       r"\bpay\s+(?:a\s+)?(?:fee|charge|deposit)\b",
       r"\bsend\s+(?:money|payment|funds)\b",
       r"\btransfer\s+(?:money|funds)\b",
       r"\bprocessing\s+fee\b",
       r"\bregistration\s+fee\b",
       r"\bactivation\s+fee\b",
       r"\bdeposit\s+(?:money|funds)\b",

       # Indian currency amounts
       r"\bsend\s+(?:rs\.?|inr|₹)\s*\d[\d,]*(?:\.\d+)?\b",
       r"\bsend\s+\d[\d,]*(?:\.\d+)?\s*(?:rs\.?|inr|₹)\b",
       r"\btransfer\s+(?:rs\.?|inr|₹)\s*\d[\d,]*(?:\.\d+)?\b",
       r"\btransfer\s+\d[\d,]*(?:\.\d+)?\s*(?:rs\.?|inr|₹)\b",
       r"\bpay\s+(?:rs\.?|inr|₹)\s*\d[\d,]*(?:\.\d+)?\b",
       r"\bpay\s+\d[\d,]*(?:\.\d+)?\s*(?:rs\.?|inr|₹)\b",

       r"\bmake\s+(?:a\s+)?payment\b",
       r"\bmake\s+(?:the\s+)?payment\b",
       r"\bsend\s+the\s+payment\b",
       r"\bpay\s+immediately\b",

       # Banglish
       r"\b\d[\d,]*\s*(?:taka|tk)\s+(?:send|pathao|dao|diye\s+dao|dite\s+hobe)\b",
       r"\b(?:taka|tk)\s+(?:send|pathao|dao)\b",

       # Hinglish
       r"\b\d[\d,]*\s*(?:rupaye|rupay|rupees)\s+(?:send|bhejo|bhej|do|dena|dena\s+hoga|karo)\b",
       r"\b(?:rupaye|rupay|rupees)\s+(?:send|bhejo|bhej|do|dena|karo)\b",

       # Bengali
       r"\d[\d,]*\s*(?:টাকা|টাকায়)\s+(?:পাঠান|পাঠাও|দিন|দিতে\s+হবে)",
       r"(?:টাকা|অর্থ)\s+(?:পাঠান|পাঠাও|দিন|দিতে\s+হবে)",
       r"পেমেন্ট\s+(?:করুন|করো)",
       r"টাকা\s+পাঠান",

       # Hindi
       r"\d[\d,]*\s*(?:रुपये|रुपए|रूपये)\s+(?:भेजें|भेजो|दो|देना\s+होगा)",
       r"(?:रुपये|रुपए|रूपये)\s+(?:भेजें|भेजो|दो|देना\s+होगा)",
       r"पैसे\s+(?:भेजें|भेजो|दो)",
       r"भुगतान\s+(?:करें|करो)",
   ],


   # ------------------------------------------------------------------
   # 9. PERSONAL ACCOUNT PAYMENT
   # ------------------------------------------------------------------

   "personal_account_payment": [

       # English
       r"\bsend\s+(?:money|payment)\s+to\s+my\s+(?:account|upi)\b",
       r"\btransfer\s+(?:money|funds)\s+to\s+my\s+(?:account|upi)\b",
       r"\bpay\s+(?:me|my\s+account)\b",
       r"\bpersonal\s+(?:bank\s+)?account\b",
       r"\bmy\s+personal\s+upi\b",
       r"\bsend\s+(?:money|payment)\s+to\s+my\s+personal\s+(?:account|upi)\b",
       r"\btransfer\s+(?:money|funds)\s+to\s+my\s+personal\s+(?:account|upi)\b",

       # Bengali
       r"আমার\s+(?:ব্যক্তিগত|পার্সোনাল)\s+(?:অ্যাকাউন্ট|UPI)",
       r"আমার\s+অ্যাকাউন্টে\s+টাকা\s+পাঠান",

       # Hindi
       r"मेरे\s+(?:व्यक्तिगत|पर्सनल)\s+(?:अकाउंट|UPI)",
       r"मेरे\s+अकाउंट\s+में\s+पैसे\s+भेजें",
   ],


   # ------------------------------------------------------------------
   # 10. SENSITIVE DATA REQUEST
   # ------------------------------------------------------------------

   "sensitive_data_request": [

       # English
       r"\bsend\s+(?:me\s+)?(?:your\s+)?otp\b",
       r"\bshare\s+(?:your\s+)?otp\b",
       r"\bgive\s+(?:me\s+)?(?:your\s+)?otp\b",
       r"\bprovide\s+(?:your\s+)?otp\b",
       r"\benter\s+(?:your\s+)?otp\b",

       r"\bsend\s+(?:me\s+)?(?:your\s+)?pin\b",
       r"\bshare\s+(?:your\s+)?pin\b",
       r"\bgive\s+(?:me\s+)?(?:your\s+)?pin\b",
       r"\bprovide\s+(?:your\s+)?pin\b",
       r"\benter\s+(?:your\s+)?pin\b",

       r"\bshare\s+(?:your\s+)?password\b",
       r"\bsend\s+(?:me\s+)?(?:your\s+)?password\b",
       r"\bprovide\s+(?:your\s+)?password\b",
       r"\benter\s+(?:your\s+)?password\b",

       r"\bshare\s+(?:your\s+)?cvv\b",
        r"\bsend\s+(?:me\s+)?(?:your\s+)?cvv\b",
        r"\bprovide\s+(?:your\s+)?cvv\b",
       r"\bsend\s+(?:your\s+)?card\s+details\b",
       r"\bshare\s+(?:your\s+)?card\s+details\b",

       r"\benter\s+(?:your\s+)?bank\s+details\b",
        r"\bsend\s+(?:me\s+)?(?:your\s+)?bank\s+details\b",
       r"\bprovide\s+(?:your\s+)?bank\s+details\b",
       r"\bshare\s+(?:your\s+)?bank\s+details\b",

       # Bengali OTP
       r"\bOTP\b.{0,30}\b(?:দিন|দাও|দিবেন|দেওয়া)\b",
       r"\b(?:আমাকে|আপনাকে|আপনার)\b.{0,30}\bOTP\b",

       # Hindi OTP
       r"\bOTP\b.{0,30}\b(?:भेजो|भेजिए|भेजें|दो|दीजिए)\b",
       r"\b(?:मुझे|अपना|आपका|आपको)\b.{0,30}\bOTP\b",

       # Generic mixed-language OTP
       r"\bOTP\b.{0,40}\b(?:verify|verification|account)\b",

       # Bengali sensitive information
       r"(?:আপনার|তোমার)\s+(?:OTP|পিন|পাসওয়ার্ড|CVV)\s+(?:দিন|দাও|পাঠান|পাঠাও)",
       r"(?:OTP|পিন|পাসওয়ার্ড|CVV)\s+(?:দিন|দাও|পাঠান|পাঠাও)",

       # Hindi sensitive information
       r"(?:अपना|आपका|आपके)\s+(?:OTP|PIN|पासवर्ड|CVV)\s+(?:दें|दो|भेजें|भेजो)",
       r"(?:OTP|PIN|पासवर्ड|CVV)\s+(?:दें|दो|भेजें|भेजो)",
   ],


   # ------------------------------------------------------------------
   # 11. UNKNOWN APP / APK
   # ------------------------------------------------------------------

   "unknown_app_or_apk": [

       # English
       r"\binstall\s+(?:this\s+)?apk\b",
       r"\bdownload\s+(?:this\s+)?apk\b",
       r"\binstall\s+(?:this\s+)?app\b",
       r"\bdownload\s+(?:this\s+)?app\b",
       r"\binstall\s+(?:our\s+)?application\b",
       r"\bdownload\s+(?:our\s+)?application\b",
       r"\binstall\s+this\s+application\b",
       r"\bdownload\s+this\s+application\b",
       r"\binstall\s+unknown\s+apk\b",

       # Banglish
       r"\b(?:ei|eta)\s+apk\s+install\s+koro\b",
       r"\b(?:ei|eta)\s+app\s+install\s+koro\b",

       # Bengali
       r"(?:এই|এটা)\s+APK\s+ইনস্টল\s+করুন",
       r"(?:এই|এটা)\s+অ্যাপ\s+ইনস্টল\s+করুন",

       # Hindi
       r"(?:यह|इस)\s+APK\s+इंस्टॉल\s+करें",
       r"(?:यह|इस)\s+ऐप\s+इंस्टॉल\s+करें",
   ],


   # ------------------------------------------------------------------
   # 12. WITHDRAWAL / RECOVERY FEE
   # ------------------------------------------------------------------

   "withdrawal_or_recovery_fee": [

       # English
       r"\bwithdrawal\s+fee\b",
       r"\brecovery\s+fee\b",
       r"\bpay\s+(?:a\s+)?(?:processing\s+)?fee\s+to\s+withdraw\b",
       r"\bpay\s+(?:a\s+)?(?:processing\s+)?fee\s+to\s+recover\b",
       r"\bpay\s+(?:a\s+)?(?:processing\s+)?fee\s+to\s+release\b",
       r"\bunlock\s+(?:your\s+)?(?:account|funds)\b",
       r"\brelease\s+(?:your\s+)?funds\b",
       r"\bfee\s+to\s+release\s+funds\b",
       r"\bpay\s+to\s+withdraw\b",
       r"\bpay\s+to\s+recover\s+(?:your\s+)?money\b",
       r"\bpay\s+to\s+release\s+(?:your\s+)?funds\b",

       # Bengali
       r"উত্তোলন\s+ফি",
       r"রিকভারি\s+ফি",
       r"টাকা\s+তুলতে\s+ফি\s+দিন",
       r"টাকা\s+ছাড়াতে\s+ফি\s+দিন",

       # Hindi
       r"निकासी\s+शुल्क",
       r"रिकवरी\s+फीस",
       r"पैसे\s+निकालने\s+के\s+लिए\s+फीस\s+दें",
       r"पैसे\s+रिलीज़\s+करने\s+के\s+लिए\s+फीस\s+दें",
   ],
}
