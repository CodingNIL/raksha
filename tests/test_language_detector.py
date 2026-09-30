from backend.services.language.detector import (
    detect_language,
    get_language_details,
)


def test_english():
    text = "I want to invest money safely."

    result = detect_language(text)

    assert result == "en"


def test_bengali():
    text = "আমি নিরাপদে টাকা বিনিয়োগ করতে চাই।"

    result = detect_language(text)

    assert result == "bn"


def test_hindi():
    text = "मैं सुरक्षित रूप से पैसा निवेश करना चाहता हूँ।"

    result = detect_language(text)

    assert result == "hi"


def test_mixed_bengali_english():
    text = "আমি investment করতে চাই"

    result = detect_language(text)

    assert result == "mixed"


def test_mixed_hindi_english():
    text = "मैं investment करना चाहता हूँ"

    result = detect_language(text)

    assert result == "mixed"


def test_mixed_bengali_hindi():
    text = "আমি निवेश করতে চাই"

    result = detect_language(text)

    assert result == "mixed"


def test_banglish():
    text = "Ami amar taka invest korte chai."

    result = detect_language(text)

    assert result == "bn-Latn"


def test_hinglish():
    text = "Main apna paisa invest karna chahta hoon."

    result = detect_language(text)

    assert result == "hi-Latn"


def test_banglish_longer_message():
    text = (
        "Ami taka invest korte chai, "
        "kintu age bhalo kore bujhte chai."
    )

    result = detect_language(text)

    assert result == "bn-Latn"


def test_hinglish_longer_message():
    text = (
        "Main apna paisa invest karna chahta hoon, "
        "lekin pehle samajhna hai."
    )

    result = detect_language(text)

    assert result == "hi-Latn"


def test_empty_text():
    result = detect_language("")

    assert result == "unknown"


def test_numbers_only():
    result = detect_language("1234567890")

    assert result == "unknown"


def test_language_details():
    text = "আমি investment করতে চাই"

    result = get_language_details(text)

    assert result["language"] == "mixed"

    assert "character_counts" in result
    assert "transliterated_counts" in result

    assert result["character_counts"]["bengali"] > 0
    assert result["character_counts"]["latin"] > 0


def test_plain_latin_financial_message():
    text = "Please verify the investment account before making a payment."

    result = detect_language(text)

    assert result == "en"