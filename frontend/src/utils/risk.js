export function getRiskStyle(level) {
  switch (level) {
    case "LOW APPARENT RISK":
      return {
        label: "Low apparent risk",
        tone: "low",
      };

    case "NEEDS VERIFICATION":
      return {
        label: "Needs verification",
        tone: "medium",
      };

    case "HIGH-RISK PATTERN":
      return {
        label: "High-risk pattern",
        tone: "high",
      };

    default:
      return {
        label: "Unknown",
        tone: "unknown",
      };
  }
}

export function getRiskDescription(level) {
  switch (level) {
    case "LOW APPARENT RISK":
      return "No major suspicious signals were identified in the provided input.";

    case "NEEDS VERIFICATION":
      return "Some signals deserve additional verification before you act.";

    case "HIGH-RISK PATTERN":
      return "Multiple suspicious signals were detected. Avoid acting until independently verified.";

    default:
      return "Review the available evidence before taking action.";
  }
}