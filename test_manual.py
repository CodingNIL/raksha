from pprint import pprint

from backend.services.fraud_engine.engine import analyze_text


TEST_MESSAGES = [
    # English
    "Invest ₹5000 and get guaranteed 50% returns. Act now!",

    # English sensitive-data request
    "Send me your OTP to verify your investment account.",

    # English withdrawal scam
    "Pay a processing fee to withdraw your investment.",

    # English APK scam
    "Download this APK and install it to activate your investment account.",

    # English impersonation
    "I am a SEBI officer. Send your details immediately.",

    # English social pressure
    "Don't tell anyone about this secret investment. Trust me.",

    # Legitimate English warning
    "Never share your OTP or password with anyone. Always verify financial information through official sources.",

    # Legitimate financial education
    "I want to learn how mutual funds work before investing.",

    # Bengali + English
    "আমাকে OTP দিন আপনার investment account verify করার জন্য।",

    # Hindi + English
    "मुझे अपना OTP भेजो investment account verify करने के लिए।",

    # Banglish
    "Ami amar taka invest korte chai kintu ora guaranteed profit debe.",

    # Hinglish
    "Main apna paisa invest karna chahta hoon lekin ye log guaranteed return bol rahe hain.",
]


def print_result(number: int, text: str, result: dict) -> None:

    print("\n" + "=" * 80)
    print(f"TEST {number}")
    print("=" * 80)

    print("\nINPUT:")
    print(text)

    print("\nLANGUAGE:")

    language = result["language"]

    print(f"  Detected : {language['language']}")

    print(f"  Character counts:")
    print(f"    Bengali      : {language['character_counts']['bengali']}")
    print(f"    Devanagari   : {language['character_counts']['devanagari']}")
    print(f"    Latin        : {language['character_counts']['latin']}")

    print("  Transliteration counts:")
    print(f"    Bengali      : {language['transliterated_counts']['bengali']}")
    print(f"    Hindi        : {language['transliterated_counts']['hindi']}")

    print("\nFRAUD SIGNALS:")

    signals = result["fraud_analysis"]["signals"]

    if signals:
        for signal in signals:
            print(f"  - {signal}")
    else:
        print("  - No fraud signals detected")

    print("\nEVIDENCE:")

    evidence = result["fraud_analysis"]["evidence"]

    if evidence:

        for signal, matches in evidence.items():

            print(f"  {signal}:")

            for match in matches:
                print(f"    - {match}")

    else:
        print("  - No evidence found")

    print("\nRISK:")

    risk = result["risk"]

    print(f"  Score : {risk['score']}")
    print(f"  Level : {risk['level']}")

    print("\nSAFE ACTIONS:")

    for action in result["safe_actions"]:
        print(f"  - {action}")


def main():

    print("\n")
    print("=" * 80)
    print("SANGYAN FRAUD DETECTION ENGINE")
    print("MULTILINGUAL MANUAL TEST")
    print("=" * 80)

    for number, text in enumerate(TEST_MESSAGES, start=1):

        result = analyze_text(text)

        if result["success"]:

            print_result(
                number,
                text,
                result
            )

        else:

            print("\nERROR:")
            print(result["message"])

    print("\n" + "=" * 80)
    print("MULTILINGUAL MANUAL TEST COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()