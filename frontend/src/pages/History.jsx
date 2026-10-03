import { useState } from "react";
import {
  ArrowRight,
  ChevronDown,
  ChevronUp,
  Clock3,
  Image,
  MessageSquareText,
  Trash2,
} from "lucide-react";

import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";
import Card from "../components/common/Card";

import RiskSummary from "../components/results/RiskSummary";
import RiskIndicators from "../components/results/RiskIndicators";
import EvidenceList from "../components/results/EvidenceList";
import MessagePreview from "../components/results/MessagePreview";
import Explanation from "../components/results/Explanation";
import SafeActions from "../components/results/SafeActions";

function getRiskStyle(level) {
  const normalized = String(level || "").toUpperCase();

  if (normalized.includes("HIGH")) {
    return {
      badge: "border-red-100 bg-red-50 text-red-700",
      dot: "bg-red-500",
    };
  }

  if (normalized.includes("VERIFICATION")) {
    return {
      badge: "border-amber-100 bg-amber-50 text-amber-700",
      dot: "bg-amber-500",
    };
  }

  return {
    badge: "border-emerald-100 bg-emerald-50 text-emerald-700",
    dot: "bg-emerald-500",
  };
}

function formatType(type) {
  return type === "image"
    ? "Screenshot analysis"
    : "Text analysis";
}

function formatSignalName(signal) {
  const name =
    typeof signal === "string"
      ? signal
      : signal?.signal ||
        signal?.type ||
        signal?.name ||
        "";

  return String(name)
    .replace(/_/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function History() {
  const [history, setHistory] = useState(() => {
    try {
      return JSON.parse(
        localStorage.getItem("raksha_history") || "[]"
      );
    } catch {
      return [];
    }
  });

  const [expandedId, setExpandedId] = useState(null);

  const clearHistory = () => {
    const confirmed = window.confirm(
      "Clear all previous analyses?"
    );

    if (!confirmed) return;

    localStorage.removeItem("raksha_history");
    setHistory([]);
    setExpandedId(null);
  };

  const toggleAnalysis = (id) => {
    setExpandedId((currentId) =>
      currentId === id ? null : id
    );
  };

  return (
    <div className="min-h-screen bg-[#f7f8f6]">
      <Navbar />

      <main className="mx-auto max-w-5xl px-5 py-20 sm:px-8">
        {/* Header */}
        <div className="flex flex-col gap-5 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-[#0f766e]">
              History
            </p>

            <h1 className="mt-3 text-4xl font-bold tracking-tight text-[#17211f] sm:text-5xl">
              Previous analyses
            </h1>

            <p className="mt-3 max-w-xl text-sm leading-6 text-[#697773]">
              Review messages and screenshots you've previously
              analyzed with Raksha.
            </p>
          </div>

          {history.length > 0 && (
            <button
              type="button"
              onClick={clearHistory}
              className="inline-flex items-center gap-2 self-start rounded-full border border-red-200 bg-white px-4 py-2.5 text-sm font-semibold text-red-600 transition hover:bg-red-50 sm:self-auto"
            >
              <Trash2 size={16} />
              Clear history
            </button>
          )}
        </div>

        {/* Empty state */}
        {history.length === 0 ? (
          <Card className="mt-10 p-10 text-center sm:p-14">
            <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-[#e5f3ef] text-[#0f766e]">
              <Clock3 size={25} />
            </div>

            <h2 className="mt-5 text-xl font-bold text-[#17211f]">
              No analyses yet
            </h2>

            <p className="mx-auto mt-2 max-w-md text-sm leading-6 text-[#697773]">
              Once you analyze a message or screenshot, your
              previous analyses will appear here.
            </p>

            <a
              href="/#analyzer"
              className="mt-6 inline-flex items-center gap-2 rounded-full bg-[#0f766e] px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-[#0b625c]"
            >
              Analyze something
              <ArrowRight size={16} />
            </a>
          </Card>
        ) : (
          <div className="mt-10 space-y-4">
            {history.map((item) => {
              const riskStyle = getRiskStyle(
                item.riskLevel
              );

              const isImage = item.type === "image";
              const isExpanded = expandedId === item.id;

              /*
               * For old entries, use item.preview.
               * For new screenshot entries, the OCR text
               * is available at item.result.ocr.text.
               */
              const screenshotText =
                item.result?.ocr?.text || "";

              const preview =
                item.preview?.trim() ||
                (isImage
                  ? screenshotText ||
                    "No readable text was extracted from this screenshot."
                  : "No message preview available.");

              const signals = Array.isArray(item.signals)
                ? item.signals
                : [];

              const savedResult = item.result;

              return (
                <div key={item.id}>
                  {/* History card */}
                  <Card className="p-5 sm:p-6">
                    {/* Top row */}
                    <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                      <div className="flex flex-wrap items-center gap-2">
                        <div className="flex items-center gap-2 text-xs font-medium text-[#7b8783]">
                          {isImage ? (
                            <Image size={14} />
                          ) : (
                            <MessageSquareText size={14} />
                          )}

                          <span>
                            {formatType(item.type)}
                          </span>
                        </div>

                        <span className="text-[#c0c8c5]">
                          •
                        </span>

                        <span className="text-xs text-[#9aa5a1]">
                          {new Date(
                            item.createdAt
                          ).toLocaleString()}
                        </span>
                      </div>

                      <div
                        className={`inline-flex w-fit items-center gap-2 rounded-full border px-3 py-1.5 text-xs font-bold ${riskStyle.badge}`}
                      >
                        <span
                          className={`h-1.5 w-1.5 rounded-full ${riskStyle.dot}`}
                        />

                        {item.riskLevel || "UNKNOWN"}
                      </div>
                    </div>

                    {/* Preview */}
                    <p className="mt-5 line-clamp-3 text-sm leading-6 text-[#52615d]">
                      {preview}
                    </p>

                    {/* Bottom row */}
                    <div className="mt-5 flex flex-col gap-4 border-t border-black/5 pt-4 sm:flex-row sm:items-center sm:justify-between">
                      <div className="flex flex-wrap gap-2">
                        {typeof item.riskScore === "number" && (
                          <span className="rounded-full bg-[#f7f8f6] px-3 py-1.5 text-xs font-medium text-[#66736f]">
                            Score:{" "}
                            <span className="font-semibold text-[#17211f]">
                              {item.riskScore}
                            </span>
                          </span>
                        )}

                        {item.language &&
                          item.language !== "Unknown" && (
                            <span className="rounded-full bg-[#f7f8f6] px-3 py-1.5 text-xs font-medium text-[#66736f]">
                              {item.language}
                            </span>
                          )}

                        {signals
                          .slice(0, 2)
                          .map((signal, index) => {
                            const name =
                              formatSignalName(signal);

                            if (!name) return null;

                            return (
                              <span
                                key={`${name}-${index}`}
                                className="rounded-full bg-[#f7f8f6] px-3 py-1.5 text-xs font-medium text-[#66736f]"
                              >
                                {name}
                              </span>
                            );
                          })}
                      </div>

                      <button
                        type="button"
                        onClick={() =>
                          toggleAnalysis(item.id)
                        }
                        className="inline-flex items-center gap-1.5 text-sm font-semibold text-[#0f766e] transition hover:text-[#0b625c]"
                      >
                        {isExpanded
                          ? "Hide analysis"
                          : "View analysis"}

                        {isExpanded ? (
                          <ChevronUp size={15} />
                        ) : (
                          <ChevronDown size={15} />
                        )}
                      </button>
                    </div>
                  </Card>

                  {/* Expanded analysis */}
                  {isExpanded && savedResult && (
                    <div className="mt-4 space-y-6 rounded-3xl border border-black/5 bg-[#eef3f1] p-4 sm:p-6">
                      <div>
                        <p className="text-xs font-semibold uppercase tracking-[0.16em] text-[#0f766e]">
                          Saved analysis
                        </p>

                        <h2 className="mt-2 text-2xl font-bold tracking-tight text-[#17211f]">
                          Analysis details
                        </h2>
                      </div>

                      {/* Risk */}
                      <RiskSummary
                        riskLevel={
                          savedResult?.risk?.level
                        }
                        riskScore={
                          savedResult?.risk?.score
                        }
                      />

                      {/* Indicators */}
                      <Card>
                        <div className="mb-5">
                          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#0f766e]">
                            Detected indicators
                          </p>

                          <h3 className="mt-1 text-xl font-bold text-[#17211f]">
                            Signals found in the message
                          </h3>
                        </div>

                        <RiskIndicators
                          indicators={
                            savedResult
                              ?.fraud_analysis
                              ?.signals || []
                          }
                        />
                      </Card>

                      {/* Message / OCR */}
                      <MessagePreview
                        text={
                          savedResult?.input
                            ?.original_text || ""
                        }
                        image={
                          savedResult?.image_preview || ""
                        }
                        ocrText={
                          savedResult?.ocr?.text || ""
                        }
                      />

                      {/* Explanation */}
                      <Explanation
                        explanation={
                          savedResult?.risk?.reasons || []
                        }
                      />

                      {/* Evidence */}
                      <EvidenceList
                        evidence={
                          savedResult?.llm_analysis
                            ?.evidence?.length
                            ? savedResult.llm_analysis
                                .evidence
                            : savedResult
                                ?.fraud_analysis
                                ?.evidence || []
                        }
                      />

                      {/* Safe actions */}
                      <SafeActions
                        actions={
                          savedResult?.safe_actions || []
                        }
                      />
                    </div>
                  )}

                  {/* Old entry without full result */}
                  {isExpanded && !savedResult && (
                    <div className="mt-4 rounded-3xl border border-amber-100 bg-amber-50 p-5">
                      <p className="text-sm leading-6 text-amber-800">
                        This is an older history entry and does
                        not contain the complete analysis result.
                        Re-analyze this content to save the full
                        result.
                      </p>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
}

export default History;