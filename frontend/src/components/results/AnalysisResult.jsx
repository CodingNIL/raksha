import Card from "../common/Card";
import RiskSummary from "./RiskSummary";
import RiskIndicators from "./RiskIndicators";
import EvidenceList from "./EvidenceList";
import MessagePreview from "./MessagePreview";
import Explanation from "./Explanation";
import SafeActions from "./SafeActions";

function AnalysisResult({ result, onReset }) {
  if (!result) {
    return null;
  }

  const risk = result.risk || {};

  // Actual deterministic signals from the backend
  const signals = Array.isArray(result.fraud_analysis?.signals)
    ? result.fraud_analysis.signals
    : [];

  // Deterministic evidence is an object
  const deterministicEvidence =
    result.fraud_analysis?.evidence || {};

  // LLM evidence is an array
  const llmAnalysis = result.llm_analysis || {};

  const llmEvidence = Array.isArray(llmAnalysis.evidence)
    ? llmAnalysis.evidence
    : [];

  const evidence =
    llmEvidence.length > 0
      ? llmEvidence
      : Object.values(deterministicEvidence);

  // Risk reasons are already human-readable
  const explanation =
    Array.isArray(risk.reasons) && risk.reasons.length > 0
      ? risk.reasons
      : [];

  // Only take actual message text from input.
  const analyzedText =
    result.input?.original_text ||
    result.input?.normalized_text ||
    "";

  // OCR text for screenshot analysis
  const ocrText =
    typeof result.ocr_text === "string"
      ? result.ocr_text
      : "";

  return (
    <section className="mx-auto w-full max-w-5xl px-5 pb-20 sm:px-8">
      {/* Header */}
      <div className="mb-8 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="mb-2 text-sm font-semibold uppercase tracking-[0.16em] text-[#0f766e]">
            Analysis complete
          </p>

          <h2 className="text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
            Here's what Raksha found
          </h2>
        </div>

        <button
          type="button"
          onClick={onReset}
          className="w-fit rounded-full border border-black/10 bg-white px-5 py-2.5 text-sm font-semibold text-[#17211f] transition hover:border-black/20 hover:bg-black/[0.02]"
        >
          Analyze another
        </button>
      </div>

      <div className="space-y-6">
        {/* Risk assessment */}
        <RiskSummary
          riskLevel={risk.level}
          riskScore={risk.score}
        />

        {/* Detected indicators */}
        <Card>
          <div className="mb-5">
            <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#0f766e]">
              Detected indicators
            </p>

            <h3 className="mt-1 text-xl font-bold text-[#17211f]">
              Signals found in the message
            </h3>
          </div>

          <RiskIndicators indicators={signals} />
        </Card>

        {/* Original message / OCR */}
        <MessagePreview
          text={analyzedText}
          image={result.image_preview}
          ocrText={ocrText}
        />

        {/* Explanation */}
        <Explanation explanation={explanation} />

        {/* Evidence */}
        <EvidenceList evidence={evidence} />

        {/* Safe actions */}
        <SafeActions actions={result.safe_actions || []} />

        {/* Analysis details */}
        <Card className="bg-[#fbfcfb]">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#66736f]">
                Analysis details
              </p>

              <div className="mt-3 flex flex-wrap gap-2">
                <div className="rounded-full border border-black/5 bg-white px-3 py-1.5 text-sm text-[#52615d]">
                  Language:{" "}
                  <span className="font-semibold text-[#17211f]">
                    {result.language?.language || "Unknown"}
                  </span>
                </div>

                <div className="rounded-full border border-black/5 bg-white px-3 py-1.5 text-sm text-[#52615d]">
                  LLM:{" "}
                  <span className="font-semibold text-[#17211f]">
                    {result.llm_status === "completed"
                      ? "Completed"
                      : result.llm_status || "Not used"}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </Card>
      </div>
    </section>
  );
}

export default AnalysisResult;