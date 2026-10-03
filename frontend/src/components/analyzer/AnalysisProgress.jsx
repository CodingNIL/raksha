import { Check, Loader2 } from "lucide-react";

function AnalysisProgress({ step = 1 }) {
  const steps = [
    "Reading your input",
    "Checking suspicious indicators",
    "Preparing safety guidance",
  ];

  return (
    <div className="rounded-3xl border border-black/5 bg-white p-8 shadow-[0_20px_60px_rgba(23,33,31,0.06)]">
      <div className="mx-auto max-w-md">
        <div className="mb-8 text-center">
          <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-[#e7f3f0] text-[#0f766e]">
            <Loader2 size={25} className="animate-spin" />
          </div>

          <h3 className="text-xl font-bold text-[#17211f]">
            Analyzing your input
          </h3>

          <p className="mt-2 text-sm text-[#7b8783]">
            Raksha is checking the available signals.
          </p>
        </div>

        <div className="space-y-4">
          {steps.map((item, index) => {
            const current = index + 1;
            const complete = current < step;
            const active = current === step;

            return (
              <div
                key={item}
                className="flex items-center gap-3"
              >
                <div
                  className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-full ${
                    complete
                      ? "bg-[#0f766e] text-white"
                      : active
                      ? "bg-[#e7f3f0] text-[#0f766e]"
                      : "bg-black/5 text-[#9aa5a1]"
                  }`}
                >
                  {complete ? (
                    <Check size={16} />
                  ) : active ? (
                    <Loader2 size={15} className="animate-spin" />
                  ) : (
                    current
                  )}
                </div>

                <span
                  className={`text-sm ${
                    active || complete
                      ? "font-medium text-[#17211f]"
                      : "text-[#9aa5a1]"
                  }`}
                >
                  {item}
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default AnalysisProgress;