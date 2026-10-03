"""
Suspicious text patterns for the fraud detection engine.

This module contains deterministic patterns for identifying
common digital fraud and scam signals.

Supported languages:
- English
- Bengali
- Hindi
- Banglish
- Hinglish
- Mixed-language financial messages

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
        r"\b(?:guaranteed|sure)\s+(?:labh|laabh|profit|return)\b",
        r"\b(?:nischit|nishchit)\s+(?:labh|profit|return)\b",

        # Bengali
        r"নিশ্চিত\s+(?:লাভ|রিটার্ন|আয়)",
        r"(?:গ্যারান্টিড|গ্যারান্টি|নিশ্চিত)\s+(?:লাভ|রিটার্ন|আয়|প্রফিট)",
        r"নিশ্চিতভাবে\s+(?:লাভ|রিটার্ন|আয়)",

        # Hindi
        r"गारंटीड\s+(?:मुनाफा|रिटर्न|लाभ|कमाई)",
        r"गारंटी\s+(?:मुनाफा|रिटर्न|लाभ)",
        r"निश्चित\s+(?:मुनाफा|रिटर्न|लाभ|कमाई)",
        r"पक्का\s+(?:मुनाफा|रिटर्न|लाभ)",
    ],


    # ------------------------------------------------------------------
    # 2. UNREALISTIC RETURNS
    # ------------------------------------------------------------------

    "unrealistic_returns": [

        # English
        r"\b\d{2,3}(?:\.\d+)?\s*(?:%|percent)\s*(?:return|returns|profit|profits)\b",
        r"\b(?:return|returns|profit|profits)\s+(?:of\s+)?\d{2,3}(?:\.\d+)?\s*(?:%|percent)\b",
        r"\binvestment\s+(?:return|returns|profit|profits)\s+(?:of\s+)?\d{2,3}(?:\.\d+)?\s*(?:%|percent)\b",
        r"\bearn\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)\b",
        r"\bget\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)",
        r"\bmake\s+\d{2,3}(?:\.\d+)?\s*(?:%|percent)",
        r"\b(?:double|triple)\s+(?:your\s+)?money\b",
        r"\bdouble\s+your\s+investment\b",
        r"\bhuge\s+(?:return|profit|returns|profits)\b",
        r"\bmassive\s+(?:return|profit|returns|profits)\b",
        r"\b(?:extraordinary|exceptional)\s+(?:return|profit|returns|profits)\b",

        # Banglish
        r"\b\d{2,3}(?:\.\d+)?\s*%\s*(?:guaranteed\s+)?(?:profit|labh|return)\b",
        r"\b(?:double|triple)\s+(?:tomar|apnar)\s+money\b",
        r"\b\d+\s*(?:hazar|lakh|lac)\s+(?:labh|profit)\b",

        # Bengali
        r"\d{2,3}(?:\.\d+)?\s*%\s*(?:নিশ্চিত\s+)?(?:লাভ|রিটার্ন|প্রফিট)",
        r"\d+\s*(?:হাজার|লাখ)\s+(?:লাভ|প্রফিট)",
        r"(?:দ্বিগুণ|তিনগুণ)\s+(?:টাকা|লাভ|রিটার্ন)",
        r"টাকা\s+দ্বিগুণ",
        r"অল্প\s+টাকায়\s+বেশি\s+লাভ",

        # Hindi
        r"\d{2,3}(?:\.\d+)?\s*%\s*(?:गारंटीड\s+)?(?:मुनाफा|लाभ|रिटर्न)",
        r"\d+\s*(?:हजार|लाख)\s+(?:मुनाफा|लाभ|प्रॉफिट)",
        r"(?:दोगुना|तीनगुना)\s+(?:पैसा|मुनाफा|रिटर्न)",
        r"पैसा\s+दोगुना",
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

        # Banglish
        r"\b(?:kono|konoi)\s+(?:loss|lokshan)\s+nei\b",
        r"\bloss\s+hobe\s+na\b",

        # Bengali
        r"কোনও\s+ক্ষতি\s+নেই",
        r"কোনো\s+ক্ষতি\s+নেই",
        r"কোনও\s+লোকসান\s+নেই",
        r"কোনো\s+লোকসান\s+নেই",
        r"ক্ষতি\s+হবে\s+না",
        r"লোকসান\s+হবে\s+না",
        r"শতভাগ\s+নিরাপদ",

        # Hindi
        r"कोई\s+नुकसान\s+नहीं",
        r"कोई\s+हानि\s+नहीं",
        r"नुकसान\s+नहीं\s+होगा",
        r"हानि\s+नहीं\s+होगी",
        r"शत\s+प्रतिशत\s+सुरक्षित",
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
        r"\bajkei\b",

        # Hinglish
        r"\babhi\b",
        r"\bturant\b",
        r"\bjaldi\b",
        r"\bfauran\b",
        r"\bforan\b",
        r"\babhi\s+ke\s+abhi\b",

        # Bengali
        r"এখনই",
        r"তাড়াতাড়ি",
        r"শীঘ্রই",
        r"আজই",
        r"জরুরি",
        r"অবিলম্বে",
        r"এক্ষুণি",
        r"এখন\s+করুন",
        r"আজ\s+করলে",
        r"পরে\s+করলে",

        # Hindi
        r"अभी",
        r"तुरंत",
        r"जल्दी",
        r"फौरन",
        r"आज\s+ही",
        r"तत्काल",
        r"अति\s+आवश्यक",
        r"अभी\s+करें",
        r"आज\s+करें",
        r"बाद\s+में\s+करने\s+पर",
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
        r"\bei\s+sujog\s+miss\s+koro\s+na\b",

        # Bengali
        r"কাউকে\s+বলবেন\s+না",
        r"কাউকে\s+বলবে\s+না",
        r"গোপন\s+রাখুন",
        r"গোপন\s+রাখবেন",
        r"এই\s+সুযোগ\s+মিস\s+করবেন\s+না",
        r"সুযোগ\s+হারাবেন",
        r"আমাকে\s+বিশ্বাস\s+করুন",
        r"পরে\s+এই\s+সুবিধা\s+থাকবে\s+না",

        # Hindi
        r"किसी\s+को\s+मत\s+बताओ",
        r"किसी\s+को\s+मत\s+बताएं",
        r"गुप्त\s+रखें",
        r"गुप्त\s+रखिए",
        r"यह\s+मौका\s+मत\s+गंवाएं",
        r"मौका\s+खो\s+देंगे",
        r"मुझ\s+पर\s+भरोसा\s+करें",
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
        r"\b(?:cyber\s+crime|police)\s+(?:officer|official)\b",
        r"\b(?:income\s+tax|customs|electricity)\s+(?:officer|official)\b",

        # Banglish
        r"\bami\s+(?:bank|rbi|sebi|police)\s+(?:theke|theke\s+bolchi)\b",
        r"\bbank\s+theke\s+bolchi\b",
        r"\bpolice\s+theke\s+bolchi\b",

        # Bengali
        r"আমি\s+(?:ব্যাংক|ব্যাঙ্ক|RBI|SEBI|পুলিশ|সরকার)\s+থেকে",
        r"আমি\s+ব্যাংক\s+থেকে\s+বলছি",
        r"আমি\s+পুলিশ\s+থেকে\s+বলছি",
        r"(?:ব্যাংক|ব্যাঙ্ক|সরকারি|পুলিশ)\s+কর্মকর্তা",
        r"(?:ব্যাংক|ব্যাঙ্ক)\s+অফিসার",
        r"সাইবার\s+ক্রাইম\s+অফিসার",

        # Hindi
        r"मैं\s+(?:बैंक|RBI|SEBI|पुलिस|सरकार)\s+से",
        r"मैं\s+बैंक\s+से\s+बोल\s+रहा\s+हूँ",
        r"मैं\s+पुलिस\s+से\s+बोल\s+रहा\s+हूँ",
        r"(?:बैंक|सरकारी|पुलिस)\s+अधिकारी",
        r"साइबर\s+क्राइम\s+अधिकारी",
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
        r"SEBI\s+অনুমোদিত",
        r"SEBI\s+অনুমোদন",
        r"RBI\s+অনুমোদিত",
        r"RBI\s+অনুমোদন",
        r"সরকারি\s+অনুমোদিত",
        r"সরকার\s+অনুমোদিত",
        r"সরকারের\s+গ্যারান্টি",

        # Hindi
        r"SEBI\s+अनुमोदित",
        r"SEBI\s+से\s+मान्यता",
        r"RBI\s+अनुमोदित",
        r"RBI\s+से\s+मान्यता",
        r"सरकार\s+द्वारा\s+अनुमोदित",
        r"सरकारी\s+गारंटी",
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

        # English amount + rupees forms
        r"\b(?:send|pay|transfer)\s+\d[\d,]*(?:\.\d+)?\s*(?:rupee|rupees)\b",
        r"\b(?:send|pay|transfer)\s+\d[\d,]*(?:\.\d+)?\s*(?:rs\.?|inr)\b",

        # General payment phrases
        r"\bmake\s+(?:a\s+)?payment\b",
        r"\bmake\s+(?:the\s+)?payment\b",
        r"\bsend\s+the\s+payment\b",
        r"\bpay\s+immediately\b",

        # Banglish
        r"\b\d[\d,]*\s*(?:taka|tk)\s+(?:send|pathao|dao|diye\s+dao|dite\s+hobe)\b",
        r"\b(?:taka|tk)\s+(?:send|pathao|dao|dite\s+hobe)\b",
        r"\btaka\s+(?:pathate|pathan|pathao)\b",
        r"\baccount\s+e\s+taka\s+(?:dao|pathao|pathan)\b",

        # Hinglish
        r"\b\d[\d,]*\s*(?:rupaye|rupay|rupees)\s+(?:send|bhejo|bhej|do|dena|dena\s+hoga|karo)\b",
        r"\b(?:rupaye|rupay|rupees)\s+(?:send|bhejo|bhej|do|dena|karo)\b",
        r"\bpaise\s+(?:bhejo|bhej|do|dena)\b",

        # Bengali
        r"\d[\d,]*\s*(?:টাকা|টাকায়)\s+(?:পাঠান|পাঠাও|দিন|দিতে\s+হবে)",
        r"(?:টাকা|অর্থ)\s+(?:পাঠান|পাঠাও|দিন|দিতে\s+হবে)",
        r"পেমেন্ট\s+(?:করুন|করো|করতে\s+হবে)",
        r"টাকা\s+পাঠান",
        r"টাকা\s+দিতে\s+হবে",
        r"অ্যাকাউন্টে\s+টাকা\s+(?:দিন|পাঠান|করুন)",
        r"টাকা\s+দেওয়ার\s+সময়",
        r"টাকা\s+দেওয়ার\s+সময়",

        # Hindi
        r"\d[\d,]*\s*(?:रुपये|रुपए|रूपये)\s+(?:भेजें|भेजो|दो|देना\s+होगा)",
        r"(?:रुपये|रुपए|पैसे)\s+(?:भेजें|भेजो|दो|देना\s+होगा)",
        r"भुगतान\s+(?:करें|करो)",
        r"पैसे\s+भेजें",
        r"पैसे\s+देने\s+होंगे",
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

        # Banglish
        r"\bamar\s+(?:personal|private)\s+account\b",
        r"\bamar\s+account\s+e\s+taka\s+(?:dao|pathao)\b",
        r"\bamar\s+UPI\s+te\s+(?:pathao|taka\s+dao)\b",

        # Bengali
        r"আমার\s+(?:ব্যক্তিগত|পার্সোনাল)\s+(?:অ্যাকাউন্ট|ব্যাংক\s+অ্যাকাউন্ট|UPI)",
        r"আমার\s+অ্যাকাউন্টে\s+টাকা\s+(?:পাঠান|দিন)",
        r"আমার\s+UPI\s+তে\s+টাকা\s+(?:পাঠান|দিন)",
        r"আমার\s+ব্যক্তিগত\s+অ্যাকাউন্টে\s+টাকা",

        # Hindi
        r"मेरे\s+(?:व्यक्तिगत|पर्सनल)\s+(?:अकाउंट|खाते|UPI)",
        r"मेरे\s+अकाउंट\s+में\s+पैसे\s+(?:भेजें|डालें)",
        r"मेरे\s+UPI\s+पर\s+पैसे\s+(?:भेजें|डालें)",
        r"मेरे\s+व्यक्तिगत\s+खाते\s+में",
    ],


    # ------------------------------------------------------------------
    # 10. SENSITIVE DATA REQUEST
    # ------------------------------------------------------------------

    "sensitive_data_request": [

        # English - OTP
        r"\bsend\s+(?:me\s+)?(?:your\s+)?otp\b",
        r"\bshare\s+(?:your\s+)?otp\b",
        r"\bgive\s+(?:me\s+)?(?:your\s+)?otp\b",
        r"\bprovide\s+(?:your\s+)?otp\b",
        r"\benter\s+(?:your\s+)?otp\b",

        # English - PIN
        r"\bsend\s+(?:me\s+)?(?:your\s+)?pin\b",
        r"\bshare\s+(?:your\s+)?pin\b",
        r"\bgive\s+(?:me\s+)?(?:your\s+)?pin\b",
        r"\bprovide\s+(?:your\s+)?pin\b",
        r"\benter\s+(?:your\s+)?pin\b",

        # English - password
        r"\bshare\s+(?:your\s+)?password\b",
        r"\bsend\s+(?:me\s+)?(?:your\s+)?password\b",
        r"\bprovide\s+(?:your\s+)?password\b",
        r"\benter\s+(?:your\s+)?password\b",

        # English - card/bank data
        r"\bshare\s+(?:your\s+)?cvv\b",
        r"\bsend\s+(?:me\s+)?(?:your\s+)?cvv\b",
        r"\bprovide\s+(?:your\s+)?cvv\b",
        r"\bsend\s+(?:your\s+)?card\s+details\b",
        r"\bshare\s+(?:your\s+)?card\s+details\b",
        r"\benter\s+(?:your\s+)?bank\s+details\b",
        r"\bsend\s+(?:me\s+)?(?:your\s+)?bank\s+details\b",
        r"\bprovide\s+(?:your\s+)?bank\s+details\b",
        r"\bshare\s+(?:your\s+)?bank\s+details\b",
        r"\bshare\s+(?:your\s+)?aadhaar\b",
        r"\bshare\s+(?:your\s+)?pan\b",

        # Banglish
        r"\b(?:tomar|apnar)\s+otp\s+(?:dao|daw|pathao|den|din)\b",
        r"\botp\s+(?:dao|daw|pathao|den|din)\b",
        r"\b(?:tomar|apnar)\s+(?:pin|password|cvv)\s+(?:dao|daw|pathao|den|din)\b",
        r"\b(?:aadhaar|aadhar|pan)\s+details\s+(?:dao|pathao|den)\b",

        # Bengali
        r"(?:আপনার|তোমার)\s+OTP\s+(?:দিন|দাও|দিবেন|পাঠান|পাঠাও)",
        r"আমাকে\s+OTP\s+(?:দিন|দাও|দিবেন|পাঠান|পাঠাও)",
        r"OTP\s+(?:দিন|দাও|দিবেন|পাঠান|পাঠাও)",
        r"(?:আপনার|তোমার)\s+(?:PIN|পিন|পাসওয়ার্ড|পাসওয়ার্ড|CVV)\s+(?:দিন|দাও|দিবেন|পাঠান|পাঠাও)",
        r"আমাকে\s+(?:PIN|পিন|পাসওয়ার্ড|পাসওয়ার্ড|CVV)\s+(?:দিন|দাও|দিবেন|পাঠান|পাঠাও)",
        r"(?:আপনার|তোমার)\s+(?:আধার|আধার কার্ড|প্যান|PAN)\s+(?:নম্বর|তথ্য|ডিটেইলস)\s+(?:দিন|দাও|পাঠান)",
        r"(?:আধার|আধার কার্ড)\s+(?:নম্বর|তথ্য)\s+দিন",
        r"ব্যাংক\s+ডিটেইলস\s+(?:দিন|পাঠান)",
        r"কার্ডের\s+ডিটেইলস\s+(?:দিন|পাঠান)",

        # Hindi
        r"(?:अपना|आपका|आपके)\s+OTP\s+(?:दें|दो|भेजें|भेजो)",
        r"मुझे\s+OTP\s+(?:दो|दें|दीजिए|भेजो|भेजें)",
        r"OTP\s+(?:दें|दो|भेजें|भेजो)",
        r"(?:अपना|आपका|आपके)\s+(?:PIN|पिन|पासवर्ड|CVV)\s+(?:दें|दो|भेजें|भेजो)",
        r"मुझे\s+(?:PIN|पिन|पासवर्ड|CVV)\s+(?:दो|दें|दीजिए|भेजो|भेजें)",
        r"(?:आधार|आधार\s+कार्ड|PAN)\s+(?:नंबर|जानकारी|डिटेल)\s+(?:दें|भेजें)",
        r"बैंक\s+डिटेल\s+(?:दें|भेजें)",
        r"कार्ड\s+डिटेल\s+(?:दें|भेजें)",
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
        r"\b(?:ei|eta)\s+app\s+download\s+koro\b",
        r"\bapp\s+ta\s+download\s+koro\b",

        # Bengali
        r"(?:এই|এটা)\s+APK\s+ইনস্টল\s+করুন",
        r"(?:এই|এটা)\s+অ্যাপ\s+ইনস্টল\s+করুন",
        r"(?:এই|এটা)\s+অ্যাপ\s+ডাউনলোড\s+করুন",
        r"অ্যাপটা\s+ডাউনলোড\s+করুন",
        r"এই\s+অ্যাপ\s+ইনস্টল\s+করুন",

        # Hindi
        r"(?:यह|इस)\s+APK\s+इंस्टॉल\s+करें",
        r"(?:यह|इस)\s+ऐप\s+इंस्टॉल\s+करें",
        r"(?:यह|इस)\s+ऐप\s+डाउनलोड\s+करें",
        r"ऐप\s+डाउनलोड\s+करें",
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

        # Banglish
        r"\bwithdraw\s+fee\b",
        r"\baccount\s+unlock\s+korte\s+fee\b",
        r"\btaka\s+tulte\s+fee\b",
        r"\btaka\s+ferot\s+petey\s+fee\b",

        # Bengali
        r"উত্তোলন\s+ফি",
        r"রিকভারি\s+ফি",
        r"টাকা\s+তুলতে\s+ফি\s+দিন",
        r"টাকা\s+ছাড়াতে\s+ফি\s+দিন",
        r"অ্যাকাউন্ট\s+আনলক\s+করতে\s+ফি",
        r"টাকা\s+ফেরত\s+পেতে\s+ফি",
        r"টাকা\s+তোলার\s+জন্য\s+ফি",

        # Hindi
        r"निकासी\s+शुल्क",
        r"रिकवरी\s+फीस",
        r"पैसे\s+निकालने\s+के\s+लिए\s+फीस\s+दें",
        r"पैसे\s+रिलीज़\s+करने\s+के\s+लिए\s+फीस",
        r"अकाउंट\s+अनलॉक\s+करने\s+के\s+लिए\s+फीस",
        r"पैसे\s+वापस\s+पाने\s+के\s+लिए\s+फीस",
    ],
}