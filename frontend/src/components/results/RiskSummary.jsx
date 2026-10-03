import {
  AlertTriangle,
  CheckCircle2,
  ShieldAlert,
} from "lucide-react";
import Card from "../common/Card";

function getRiskConfig(level) {
  const normalized = String(level || "").toUpperCase();

  if (normalized.includes("HIGH")) {
    return {
      label: "HIGH-RISK PATTERN",
      description:
        "Several signals associated with potentially harmful or fraudulent requests were detected.",
      icon: ShieldAlert,
      iconBg: "bg-red-50",
      iconColor: "text-red-600",
      badgeBg: "bg-red-50",
      badgeColor: "text-red-700",
      border: "border-red-100",
    };
  }

  if (normalized.includes("VERIFICATION")) {
    return {
      label: "NEEDS VERIFICATION",
      description:
        "Some warning signs were detected. Verify the request independently before taking action.",
      icon: AlertTriangle,
      iconBg: "bg-amber-50",
      iconColor: "text-amber-600",
      badgeBg: "bg-amber-50",
      badgeColor: "text-amber-700",
      border: "border-amber-100",
    };
  }

  return {
    label: "LOW APPARENT RISK",
    description:
      "No major risk signals were detected, but continue to verify unexpected requests.",
    icon: CheckCircle2,
    iconBg: "bg-emerald-50",
    iconColor: "text-emerald-600",
    badgeBg: "bg-emerald-50",
    badgeColor: "text-emerald-700",
    border: "border-emerald-100",
  };
}

function RiskSummary({ riskLevel, riskScore }) {
  const config = getRiskConfig(riskLevel);
  const Icon = config.icon;

  const score =
    typeof riskScore === "number" ? riskScore : Number(riskScore) || 0;

  return (
    <Card className="overflow-hidden">
      <div className="flex min-w-0 flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex min-w-0 items-start gap-4">
          <div
            className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl ${config.iconBg} ${config.iconColor}`}
          >
            <Icon size={24} strokeWidth={2} />
          </div>

          <div className="min-w-0">
            <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#66736f]">
              Assessment
            </p>

            <div className="mt-2 flex flex-wrap items-center gap-2">
              <h3 className="break-words text-2xl font-bold tracking-tight text-[#17211f] sm:text-3xl">
                {config.label}
              </h3>
            </div>

            <p className="mt-2 max-w-2xl text-sm leading-6 text-[#66736f]">
              {config.description}
            </p>
          </div>
        </div>

        <div className="shrink-0 rounded-2xl border border-black/5 bg-[#f7f8f6] px-5 py-4 sm:min-w-[130px]">
          <p className="text-xs font-semibold uppercase tracking-[0.12em] text-[#66736f]">
            Risk score
          </p>

          <p className="mt-1 text-3xl font-bold tracking-tight text-[#17211f]">
            {score}
          </p>
        </div>
      </div>

      <div className={`mt-6 rounded-2xl border ${config.border} ${config.badgeBg} px-4 py-3`}>
        <p className={`text-sm font-medium ${config.badgeColor}`}>
          This assessment is based on signals detected in the submitted content.
        </p>
      </div>
    </Card>
  );
}

export default RiskSummary;