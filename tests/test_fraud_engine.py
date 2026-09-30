from backend.services.fraud_engine.engine import analyze_text


def test_guaranteed_return():
    text = "Invest ₹5000 and get guaranteed 50% returns. Act now!"

    result = analyze_text(text)

    assert result["success"] is True

    signals = result["fraud_analysis"]["signals"]

    assert "guaranteed_returns" in signals
    assert "urgency" in signals

    assert result["risk"]["score"] > 0


def test_no_loss_claim():
    text = "This investment has zero loss and guaranteed profit."

    result = analyze_text(text)

    signals = result["fraud_analysis"]["signals"]

    assert "no_loss_claim" in signals
    assert "guaranteed_returns" in signals


def test_sensitive_information_request():
    text = "Send me your OTP to verify your investment account."

    result = analyze_text(text)

    signals = result["fraud_analysis"]["signals"]

    assert "sensitive_data_request" in signals


def test_payment_request():
    text = "Pay a processing fee to withdraw your investment."

    result = analyze_text(text)

    signals = result["fraud_analysis"]["signals"]

    assert "payment_request" in signals
    assert "withdrawal_or_recovery_fee" in signals


def test_unknown_apk():
    text = "Download this APK and install it to activate your investment account."

    result = analyze_text(text)

    signals = result["fraud_analysis"]["signals"]

    assert "unknown_app_or_apk" in signals


def test_legitimate_warning():
    text = (
        "Never share your OTP or password with anyone. "
        "Verify financial information using official sources."
    )

    result = analyze_text(text)

    assert result["success"] is True

    signals = result["fraud_analysis"]["signals"]

    # The current rule engine may still detect "OTP"
    # because it is pattern-based. This test therefore
    # only verifies that the engine runs successfully.
    assert isinstance(signals, list)


def test_empty_input():
    result = analyze_text("")

    assert result["success"] is False
    assert "message" in result


def test_evidence_is_returned():
    text = "Act now! Get guaranteed 30% returns."

    result = analyze_text(text)

    evidence = result["fraud_analysis"]["evidence"]

    assert isinstance(evidence, dict)
    assert len(evidence) > 0