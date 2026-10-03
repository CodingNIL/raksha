import Card from "../common/Card";
import { MessageSquareText } from "lucide-react";

function MessagePreview({ text, image, ocrText }) {
  const displayText = ocrText || text;

  if (!displayText && !image) {
    return null;
  }

  return (
    <Card>
      <div className="mb-5">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#0f766e]">
          Analyzed message
        </p>

        <h3 className="mt-1 text-xl font-bold text-[#17211f]">
          Message content
        </h3>
      </div>

      {image && (
        <div className="mb-5 overflow-hidden rounded-2xl border border-black/5 bg-[#f7f8f6]">
          <img
            src={image}
            alt="Uploaded message"
            className="max-h-[420px] w-full object-contain"
          />
        </div>
      )}

      {displayText && (
        <div className="flex min-w-0 gap-3 rounded-2xl border border-black/5 bg-[#f7f8f6] p-4">
          <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-white text-[#0f766e]">
            <MessageSquareText size={18} />
          </div>

          <p className="min-w-0 break-words whitespace-pre-wrap text-sm leading-6 text-[#52615d]">
            {displayText}
          </p>
        </div>
      )}
    </Card>
  );
}

export default MessagePreview;