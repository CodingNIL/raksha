import {
  AlertCircle,
  Clock3,
  CreditCard,
  FileWarning,
  ShieldAlert,
  UserRound,
} from "lucide-react";

function getSignalName(signal) {
  if (typeof signal === "string") {
    return signal;
  }

  if (signal && typeof signal === "object") {
    return (
      signal.signal ||
      signal.type ||
      signal.name ||
      signal.indicator ||
      "Risk Indicator"
    );
  }

  return "Risk Indicator";
}

function formatSignalName(signal) {
  const name = getSignalName(signal);

  return String(name)
    .replace(/_/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function getIcon(signal) {
  const name = String(getSignalName(signal)).toLowerCase();

  if (name.includes("payment") || name.includes("money")) {
    return CreditCard;
  }

  if (name.includes("urgency") || name.includes("pressure")) {
    return Clock3;
  }

  if (
    name.includes("impersonation") ||
    name.includes("identity")
  ) {
    return UserRound;
  }

  if (
    name.includes("fake") ||
    name.includes("regulatory")
  ) {
    return FileWarning;
  }

  if (name.includes("alert")) {
    return AlertCircle;
  }

  return ShieldAlert;
}

function RiskIndicators({ indicators = [] }) {
  if (!Array.isArray(indicators) || indicators.length === 0) {
    return (
      <p className="text-sm text-[#66736f]">
        No specific risk indicators were returned.
      </p>
    );
  }

  return (
    <div className="grid min-w-0 grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
      {indicators.map((signal, index) => {
        const Icon = getIcon(signal);
        const name = formatSignalName(signal);

        const weight =
          signal &&
          typeof signal === "object" &&
          typeof signal.weight === "number"
            ? signal.weight
            : null;

        return (
          <div
            key={`${name}-${index}`}
            className="flex min-w-0 items-start gap-3 rounded-2xl border border-black/5 bg-[#f7f8f6] p-4"
          >
            <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-[#e5f3ef] text-[#0f766e]">
              <Icon size={18} />
            </div>

            <div className="min-w-0 flex-1">
              <p className="break-words font-semibold text-[#17211f]">
                {name}
              </p>

              {weight !== null && (
                <p className="mt-1 text-xs text-[#66736f]">
                  Risk weight: {weight}
                </p>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default RiskIndicators;