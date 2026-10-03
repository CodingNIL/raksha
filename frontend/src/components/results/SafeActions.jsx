import Card from "../common/Card";
import { CheckCircle2, ShieldCheck } from "lucide-react";

function SafeActions({ actions = [] }) {
  if (!Array.isArray(actions) || actions.length === 0) {
    return null;
  }

  return (
    <Card>
      <div className="mb-5 flex items-start gap-3">
        <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-[#e5f3ef] text-[#0f766e]">
          <ShieldCheck size={19} />
        </div>

        <div className="min-w-0">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#0f766e]">
            What to do next
          </p>

          <h3 className="mt-1 text-xl font-bold text-[#17211f]">
            Safer next steps
          </h3>

          <p className="mt-1 text-sm leading-6 text-[#66736f]">
            Consider these steps before responding to the request.
          </p>
        </div>
      </div>

      <div className="space-y-3">
        {actions.map((action, index) => (
          <div
            key={`${action}-${index}`}
            className="flex min-w-0 items-start gap-3 rounded-2xl border border-[#dceee9] bg-[#f4faf8] px-4 py-3.5"
          >
            <CheckCircle2
              size={18}
              className="mt-0.5 shrink-0 text-[#0f766e]"
            />

            <p className="min-w-0 break-words text-sm leading-6 text-[#40504c]">
              {action}
            </p>
          </div>
        ))}
      </div>
    </Card>
  );
}

export default SafeActions;