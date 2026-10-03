"""
LLM prompt builder for the SANGYAN fraud detection engine.

This module prepares structured information for an LLM
reasoning layer.

The LLM will be used for:
- contextual reasoning
- additional fraud-signal identification
- evidence extraction
- entity extraction
- claim identification

The LLM must NOT:
- provide investment advice
- recommend buying or selling
- predict prices
- make financial decisions for the user
"""

from services.fraud_engine.taxonomy import get_taxonomy


def build_fraud_reasoning_prompt(
    text: str,
    language: str,
    rule_signals: list[str],
    rule_evidence: dict,
) -> str:
    """
    Build the structured reasoning prompt for the LLM layer.
    """

    taxonomy = get_taxonomy()

    taxonomy_lines = []

    for signal, details in taxonomy.items():
        taxonomy_lines.append(
            f"- {signal}: {details['description']}"
        )

    taxonomy_text = "\n".join(taxonomy_lines)

    signals_text = (
        ", ".join(rule_signals)
        if rule_signals
        else "None"
    )

    evidence_text = str(rule_evidence)

    prompt = f"""
You are a fraud-analysis reasoning component for a
financial scam detection system.

Your task is to analyze the provided message for fraud
signals and suspicious contextual behavior.

IMPORTANT SAFETY RULES:

1. Do not provide investment advice.
2. Do not recommend buying, selling, or holding any security.
3. Do not predict prices or investment returns.
4. Do not make financial decisions for the user.
5. Do not assume that a message is fraudulent merely because
   it contains financial terminology.
6. Base conclusions on evidence present in the message.
7. Distinguish suspicious signals from legitimate financial
   education or warnings.

SUPPORTED FRAUD TAXONOMY:

{taxonomy_text}

STRICT SIGNAL OUTPUT RULE:

The "additional_signals" field may contain ONLY signal names
from the SUPPORTED FRAUD TAXONOMY listed above.

Do NOT put contextual observations, reasoning concepts,
or context field names into "additional_signals".

For example, these are NOT valid additional_signals:
- financial_pressure
- unrealistic_promise
- suspicious_instructions
- sensitive_information_request

Those concepts must be represented using the appropriate
"context" boolean fields when applicable.

Only add a signal to "additional_signals" when the message
provides evidence supporting one of the official taxonomy
categories.

Never invent a new fraud category or create a new signal name.

MESSAGE LANGUAGE:

{language}

USER MESSAGE:

{text}

RULE-BASED SIGNALS ALREADY DETECTED:

{signals_text}

RULE-BASED EVIDENCE:

{evidence_text}

ANALYSIS TASK:

1. Identify any ADDITIONAL fraud signals supported by the
   message context.

2. IMPORTANT:
   "additional_signals" MUST contain ONLY official signal
   names from the supported fraud taxonomy.

3. Identify the strongest pieces of evidence.

4. Identify important entities such as:
   - organizations
   - regulators
   - banks
   - apps
   - websites
   - payment identifiers

5. Identify important claims made by the sender.

6. Determine whether the message contains:
   - financial pressure
   - requests for money
   - requests for sensitive information
   - impersonation
   - unrealistic promises
   - suspicious instructions

7. Represent these contextual observations in the
   appropriate "context" fields. Do NOT put their names
   into "additional_signals" unless that exact name is also
   an official taxonomy signal.

8. Do not invent facts that are not present in the message.

CONTEXT FIELD RULES:

- "financial_pressure" is a boolean context field.
- "payment_request" is a boolean context field.
- "sensitive_information_request" is a boolean context field.
- "impersonation" is a boolean context field.
- "unrealistic_promise" is a boolean context field.

These context fields are NOT fraud signal names and must
never be inserted into "additional_signals".

EXPLANATION LANGUAGE REQUIREMENT:

The "explanation" field is user-facing.

The explanation must preserve the existing fraud-warning
and evidence-based behavior. Multilingual support is an
additional accessibility feature and must NOT replace,
remove, weaken, or shorten the important safety warning.

Follow these rules:

- If the message is in English, write ONE clear explanation in English.
- If the message is not in English, write the explanation in TWO parts:
  1. First, provide a clear English explanation.
  2. Immediately after that, provide the same explanation in the
     user's detected language or language style.
- For Bengali script, provide English first and then Bengali.
- For Hindi/Devanagari script, provide English first and then Hindi.
- For Banglish (Bengali written using Latin characters), provide
  English first and then natural Banglish.
- For Hinglish (Hindi written using Latin characters), provide
  English first and then natural Hinglish.
- For mixed-language messages, provide English first and then
  explain the message using the dominant detected language/style,
  preserving meaningful code-switching where appropriate.
- Separate the English and user-language explanations clearly.
- Use labels such as "English:" and the appropriate language label
  such as "Bengali:", "Hindi:", "Banglish:", or "Hinglish:".
- The English explanation must always appear first for non-English
  messages.
- Do not translate the user's message merely for analysis.
- The second explanation should communicate the same safety meaning
  as the English explanation.
- Do not remove warnings, evidence, risk context, or recommended
  safety behavior when producing the second-language explanation.
- Keep important safety guidance explicit, such as warnings against
  sending money or sharing OTPs, PINs, passwords, or other sensitive
  information when the message contains such risks.
- Keep fraud category names such as "guaranteed_returns",
  "payment_request", and "impersonation" unchanged when they need
  to be referenced as technical signal names.
- Keep both explanations concise, clear, evidence-based, and easy
  for the original user to understand.
- Do not add facts that are not present in the message.

Return ONLY JSON using this structure:

{{
    "additional_signals": [],
    "evidence": [],
    "entities": [],
    "claims": [],
    "context": {{
        "financial_pressure": false,
        "payment_request": false,
        "sensitive_information_request": false,
        "impersonation": false,
        "unrealistic_promise": false
    }},
    "explanation": ""
}}
"""

    return prompt.strip()
