import { Sparkles } from "lucide-react";
import Button from "../common/Button";

function TextAnalyzer({
  text,
  setText,
  onAnalyze,
  loading,
}) {
  return (
    <>
      <textarea
        value={text}
        onChange={(event) => setText(event.target.value)}
        placeholder="Paste the message you're unsure about..."
        className="min-h-52 w-full resize-none rounded-2xl border border-black/10 bg-[#fafbf9] p-5 text-sm leading-7 text-[#17211f] outline-none transition placeholder:text-[#9aa5a1] focus:border-[#0f766e] focus:ring-4 focus:ring-[#0f766e]/10"
      />

      <div className="mt-5 flex flex-col justify-between gap-4 sm:flex-row sm:items-center">
        <p className="text-xs text-[#7b8783]">
          Don't share passwords, OTPs, or other sensitive information.
        </p>

        <Button
          onClick={onAnalyze}
          loading={loading}
          disabled={!text.trim()}
          icon={Sparkles}
        >
          Analyze message
        </Button>
      </div>
    </>
  );
}

export default TextAnalyzer;