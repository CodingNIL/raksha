# Raksha

> **Understand before you act.**

Raksha is a digital safety assistant that helps users examine suspicious messages and screenshots for signals commonly associated with financial scams and fraudulent requests.

Instead of simply labeling a message as "safe" or "fraudulent", Raksha presents the detected indicators, supporting evidence, risk assessment, explanation, and safer next steps so users can make more informed decisions.

---

## What Raksha Does

Raksha accepts two types of input:

- **Text** — paste a suspicious message directly.
- **Screenshot** — upload a screenshot of a message and let Raksha extract the text before analyzing it.

The analysis looks for signals such as:

- Urgency and pressure
- Payment requests
- Impersonation
- Sensitive information requests
- Personal-account payment requests
- Suspicious applications or APKs
- Guaranteed-return claims
- Withdrawal or recovery fees
- Fake regulatory claims
- Other recognizable scam patterns

The result is presented through a structured interface containing:

- Risk level
- Risk score
- Detected indicators
- Supporting evidence
- Analyzed message
- Explanation
- Safer next steps
- Language and analysis status

---

## Risk Assessment

Raksha currently uses three assessment levels:

| Assessment | Meaning |
|---|---|
| **LOW APPARENT RISK** | No major risk signals were detected in the submitted content. |
| **NEEDS VERIFICATION** | Some warning signals were detected and the request should be independently verified. |
| **HIGH-RISK PATTERN** | Multiple significant signals associated with potentially harmful or fraudulent requests were detected. |

The assessment is based on detected signals in the submitted content. It is **not a guarantee that a message is safe or fraudulent**.

---

## How It Works

```text
User Input
    │
    ├── Text
    │
    └── Screenshot
           │
           ▼
     Text Extraction
           │
           ▼
   Content Normalization
           │
           ▼
   Signal Detection
           │
           ▼
      LLM Analysis
        (optional)
           │
           ▼
    Risk Calculation
           │
           ▼
 Evidence + Explanation
           │
           ▼
     Safer Next Steps