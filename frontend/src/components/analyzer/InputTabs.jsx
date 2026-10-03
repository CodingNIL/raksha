import { Image, MessageSquare } from "lucide-react";

function InputTabs({ mode, setMode }) {
  return (
    <div className="flex border-b border-black/5">
      <button
        onClick={() => setMode("text")}
        className={`flex flex-1 items-center justify-center gap-2 px-5 py-4 text-sm font-semibold transition ${
          mode === "text"
            ? "bg-[#f0f7f5] text-[#0f766e]"
            : "text-[#697773] hover:bg-black/[0.02]"
        }`}
      >
        <MessageSquare size={18} />
        Paste Text
      </button>

      <button
        onClick={() => setMode("image")}
        className={`flex flex-1 items-center justify-center gap-2 px-5 py-4 text-sm font-semibold transition ${
          mode === "image"
            ? "bg-[#f0f7f5] text-[#0f766e]"
            : "text-[#697773] hover:bg-black/[0.02]"
        }`}
      >
        <Image size={18} />
        Upload Screenshot
      </button>
    </div>
  );
}

export default InputTabs;