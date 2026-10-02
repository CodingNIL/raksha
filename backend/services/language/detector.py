"""
Language detection utilities for the SANGYAN fraud detection engine.

Supported language categories:

    en       -> English
    bn       -> Bengali script
    hi       -> Hindi / Devanagari script
    mixed    -> Multiple scripts/languages
    bn-Latn  -> Bengali written using Latin characters (Banglish)
    hi-Latn  -> Hindi written using Latin characters (Hinglish)
    unknown  -> No meaningful language detected
"""

import re
import unicodedata


# ============================================================================
# SCRIPT DETECTION
# ============================================================================

def count_script_characters(text: str) -> dict:
    """
    Count actual Bengali, Devanagari, and Latin LETTERS.

    Important:
    Unicode blocks also contain punctuation and symbols.

    Therefore, punctuation such as the Bengali/Hindi danda:
        ।
    must NOT be counted as Devanagari language evidence.
    """

    counts = {
        "bengali": 0,
        "devanagari": 0,
        "latin": 0,
    }

    for char in text:
        code_point = ord(char)

        # Ignore punctuation, numbers, symbols, spaces, etc.
        unicode_category = unicodedata.category(char)

        if not unicode_category.startswith("L"):
            continue

        # ----------------------------------------------------------------
        # Bengali letters
        # ----------------------------------------------------------------

        if 0x0980 <= code_point <= 0x09FF:
            counts["bengali"] += 1

        # ----------------------------------------------------------------
        # Devanagari letters
        # ----------------------------------------------------------------

        elif 0x0900 <= code_point <= 0x097F:
            counts["devanagari"] += 1

        # ----------------------------------------------------------------
        # Basic Latin letters
        # ----------------------------------------------------------------

        elif (
            0x0041 <= code_point <= 0x005A
            or
            0x0061 <= code_point <= 0x007A
        ):
            counts["latin"] += 1

    return counts


# ============================================================================
# BANGLISH VOCABULARY
# ============================================================================

"""
Distinctive Bengali transliteration words.

Common English words are deliberately excluded.
"""

BANGLISH_WORDS = {
    "ami",
    "amar",
    "amader",
    "apni",
    "apnar",
    "tumi",
    "tomar",
    "tomake",
    "tomader",

    "taka",
    "chai",
    "chao",
    "chay",

    "korbo",
    "korben",
    "korte",
    "kori",
    "korchi",
    "kore",
    "koren",
    "koro",

    "ache",
    "achhe",
    "nei",

    "hobe",
    "hoye",
    "hoy",
    "hoyechhe",
    "hoyeche",

    "jodi",
    "kintu",
    "age",
    "pore",

    "bhalo",
    "khub",
    "kichu",

    "keno",
    "kibhabe",
    "ki",

    "eta",
    "seta",
    "ekhane",
    "okhane",

    "apnake",
    "apnader",

    "din",
    "dibo",
    "nibo",
    "nite",

    "dekhte",
    "bujhte",
    "bujhi",

    "bolun",
    "bolte",
    "bolchi",

    "lagbe",
    "lagche",

    "parbo",
    "parben",

    "hocche",
    "hochhe",
}


# ============================================================================
# HINGLISH VOCABULARY
# ============================================================================

"""
Distinctive Hindi transliteration words.

Common English words are deliberately excluded.

For example, these are NOT included:

    the
    is
    a
    to
    my
    me
    safe
    account
    payment
    investment
    money
    verify
"""

HINGLISH_WORDS = {
    "main",
    "mein",

    "mera",
    "meri",
    "mere",

    "hum",
    "hamara",
    "hamari",
    "hamare",

    "aap",
    "aapka",
    "aapki",
    "aapke",

    "apka",
    "apki",
    "apke",
    "apne",

    "tum",
    "tumhara",
    "tumhari",
    "tumhare",

    "mujhe",
    "mujhko",
    "mujhse",

    "tujhe",
    "tujhko",

    "paisa",
    "paise",
    "rupaye",
    "rupay",
    "rupees",

    "abhi",
    "aaj",
    "jaldi",
    "turant",
    "turant",
    "fauran",
    "foran",

    "chahta",
    "chahti",
    "chahte",
    "chahiye",

    "karna",
    "karni",
    "karte",
    "karta",
    "karti",

    "karunga",
    "karungi",
    "karoge",
    "karogi",

    "hai",
    "hain",
    "tha",
    "thi",

    "hoga",
    "hogi",
    "honge",

    "nahi",
    "nahin",
    "mat",

    "agar",
    "lekin",
    "kyunki",
    "kyonki",

    "pehle",
    "baad",

    "accha",
    "achha",
    "acha",

    "bahut",
    "kuch",

    "kya",
    "kaise",
    "kyun",
    "kyon",

    "yeh",
    "yah",
    "woh",
    "voh",

    "iska",
    "iske",
    "iski",

    "uska",
    "uske",
    "uski",

    "isko",
    "usko",

    "samajhna",
    "samajh",

    "batao",
    "bataye",
    "batana",

    "bolna",
    "boliye",

    "dekhna",

    "dena",
    "deni",
    "dene",

    "lena",
    "leni",
    "lene",

    "sakta",
    "sakti",
    "sakte",
}


# ============================================================================
# TOKENIZATION
# ============================================================================

def tokenize_latin_text(text: str) -> list[str]:
    """
    Extract lowercase Latin-script word tokens.
    """

    return re.findall(
        r"[a-zA-Z]+",
        text.lower(),
    )


# ============================================================================
# TRANSLITERATED LANGUAGE DETECTION
# ============================================================================

def detect_transliterated_language(text: str) -> str:
    """
    Detect Banglish or Hinglish in Latin-script text.

    Returns:

        bn-Latn
        hi-Latn
        mixed
        en
    """

    tokens = tokenize_latin_text(text)

    if not tokens:
        return "unknown"

    bengali_score = 0
    hindi_score = 0

    for token in tokens:

        if token in BANGLISH_WORDS:
            bengali_score += 1

        if token in HINGLISH_WORDS:
            hindi_score += 1

    # No distinctive transliteration evidence.
    if bengali_score == 0 and hindi_score == 0:
        return "en"

    # Evidence for both languages.
    if bengali_score > 0 and hindi_score > 0:
        return "mixed"

    # Bengali transliteration.
    if bengali_score > hindi_score:
        return "bn-Latn"

    # Hindi transliteration.
    if hindi_score > bengali_score:
        return "hi-Latn"

    return "en"


# ============================================================================
# MAIN LANGUAGE DETECTOR
# ============================================================================

def detect_language(text: str) -> str:
    """
    Detect the language category of a message.

    Returns:

        en
        bn
        hi
        mixed
        bn-Latn
        hi-Latn
        unknown
    """

    if not text or not text.strip():
        return "unknown"

    text = unicodedata.normalize(
        "NFKC",
        text,
    ).strip()

    if not text:
        return "unknown"

    counts = count_script_characters(text)

    bengali_count = counts["bengali"]
    devanagari_count = counts["devanagari"]
    latin_count = counts["latin"]

    # ----------------------------------------------------------------
    # Bengali + Hindi
    # ----------------------------------------------------------------

    if bengali_count > 0 and devanagari_count > 0:
        return "mixed"

    # ----------------------------------------------------------------
    # Bengali native script
    # ----------------------------------------------------------------

    if bengali_count > 0:

        if latin_count > 0:
            return "mixed"

        return "bn"

    # ----------------------------------------------------------------
    # Hindi native script
    # ----------------------------------------------------------------

    if devanagari_count > 0:

        if latin_count > 0:
            return "mixed"

        return "hi"

    # ----------------------------------------------------------------
    # Latin-only text
    # ----------------------------------------------------------------

    if latin_count > 0:
        return detect_transliterated_language(text)

    # ----------------------------------------------------------------
    # Numbers / punctuation / symbols only
    # ----------------------------------------------------------------

    return "unknown"


# ============================================================================
# LANGUAGE DETAILS
# ============================================================================

def get_language_details(text: str) -> dict:
    """
    Return detailed language-detection information.
    """

    language = detect_language(text)

    character_counts = count_script_characters(text)

    tokens = tokenize_latin_text(text)

    transliterated_counts = {
        "bengali": 0,
        "hindi": 0,
    }

    for token in tokens:

        if token in BANGLISH_WORDS:
            transliterated_counts["bengali"] += 1

        if token in HINGLISH_WORDS:
            transliterated_counts["hindi"] += 1

    return {
        "language": language,
        "character_counts": character_counts,
        "transliterated_counts": transliterated_counts,
    }