import Card from "../common/Card";
import { SearchCheck } from "lucide-react";

function formatEvidenceItem(item) {
  if (typeof item === "string") {
    return item;
  }

  if (!item || typeof item !== "object") {
    return null;
  }

  return (
    item.text ||
    item.description ||
    item.reason ||
    item.evidence ||
    item.explanation ||
    null
  );
}

function EvidenceList({ evidence = [] }) {
  const items = Array.isArray(evidence)
    ? evidence
    : Object.values(evidence || {});

  const formattedItems = items
    .map(formatEvidenceItem)
    .filter(Boolean);

  return (
    <Card>
      <div className="mb-5 flex items-start gap-3">
        <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-[#e5f3ef] text-[#0f766e]">
          <SearchCheck size={19} />
        </div>

        <div className="min-w-0">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#0f766e]">
            Evidence
          </p>

          <h3 className="mt-1 text-xl font-bold text-[#17211f]">
            What Raksha noticed
          </h3>
        </div>
      </div>

      {formattedItems.length === 0 ? (
        <div className="rounded-2xl border border-black/5 bg-[#f7f8f6] px-4 py-4">
          <p className="text-sm leading-6 text-[#66736f]">
            No specific evidence was returned.
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {formattedItems.map((item, index) => (
            <div
              key={index}
              className="flex min-w-0 items-start gap-3 rounded-2xl border border-black/5 bg-[#f7f8f6] px-4 py-3.5"
            >
              <span
                className="mt-[9px] h-2 w-2 shrink-0 rounded-full bg-[#0f766e]"
                aria-hidden="true"
              />

              <p className="min-w-0 flex-1 break-words text-sm leading-6 text-[#52615d]">
                {item}
              </p>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

export default EvidenceList;

