from pprint import pprint

from backend.services.fraud_engine.engine import analyze_text


TEST_MESSAGES = [
    # ---------------------------------------------------------
    # TEST 1: Guaranteed returns
    # ---------------------------------------------------------
    "Invest ₹5000 and get guaranteed 50% returns. Act now!",

    # ---------------------------------------------------------
    # TEST 2: Sensitive information
    # ---------------------------------------------------------
    "Send me your OTP to verify your investment account.",

    # ---------------------------------------------------------
    # TEST 3: Payment + withdrawal fee
    # ---------------------------------------------------------
    "Pay a processing fee to withdraw your investment.",

    # ---------------------------------------------------------
    # TEST 4: Unknown APK
    # ---------------------------------------------------------
    "Download this APK and install it to activate your investment account.",

    # ---------------------------------------------------------
    # TEST 5: Impersonation
    # ---------------------------------------------------------
    "I am a SEBI officer. Send your details immediately.",

    # ---------------------------------------------------------
    # TEST 6: Social pressure
    # ---------------------------------------------------------
    "Don't tell anyone about this secret investment. Trust me.",

    # ---------------------------------------------------------
    # TEST 7: More legitimate financial text
    # ---------------------------------------------------------
    "Never share your OTP or password with anyone. "
    "Always verify financial information through official sources.",

    # ---------------------------------------------------------
    # TEST 8: Simple harmless message
    # ---------------------------------------------------------
    "I want to learn how mutual funds work before investing.",
]


def print_result(number: int, text: str, result: dict) -> None:
    """
    Print one fraud-analysis result in a readable format.
    """

    print("\n" + "=" * 70)
    print(f"TEST {number}")
    print("=" * 70)

    print("\nINPUT:")
    print(text)

    print("\nSIGNALS:")

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
    """
    Run all manual fraud-engine tests.
    """

    print("\n")
    print("=" * 70)
    print("SANGYAN FRAUD DETECTION ENGINE")
    print("STEP 1.9 - MANUAL TEST")
    print("=" * 70)

    for number, text in enumerate(TEST_MESSAGES, start=1):

        result = analyze_text(text)

        if result["success"]:
            print_result(number, text, result)

        else:
            print("\nERROR:")
            print(result["message"])

    print("\n" + "=" * 70)
    print("MANUAL TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()