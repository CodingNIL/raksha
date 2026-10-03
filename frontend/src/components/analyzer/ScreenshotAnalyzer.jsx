import { useRef } from "react";
import { ImagePlus, Upload, X } from "lucide-react";
import Button from "../common/Button";

function ScreenshotAnalyzer({
  file,
  setFile,
  onAnalyze,
  loading,
}) {
  const inputRef = useRef(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files?.[0];

    if (!selectedFile) return;

    setFile(selectedFile);
  };

  const removeFile = () => {
    setFile(null);

    if (inputRef.current) {
      inputRef.current.value = "";
    }
  };

  return (
    <>
      <input
        ref={inputRef}
        type="file"
        accept="image/png,image/jpeg,image/webp"
        onChange={handleFileChange}
        className="hidden"
      />

      {!file ? (
        <button
          type="button"
          onClick={() => inputRef.current?.click()}
          className="flex min-h-52 w-full flex-col items-center justify-center rounded-2xl border-2 border-dashed border-black/10 bg-[#fafbf9] p-8 text-center transition hover:border-[#0f766e]/40 hover:bg-[#f5faf8]"
        >
          <div className="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-[#e7f3f0] text-[#0f766e]">
            <Upload size={24} />
          </div>

          <h3 className="font-semibold text-[#17211f]">
            Upload a screenshot
          </h3>

          <p className="mt-2 max-w-sm text-sm leading-6 text-[#7b8783]">
            Upload a screenshot of the message, payment request,
            or conversation you want to check.
          </p>

          <span className="mt-5 rounded-full border border-black/10 bg-white px-5 py-2.5 text-sm font-semibold text-[#17211f]">
            Choose image
          </span>

          <p className="mt-3 text-xs text-[#9aa5a1]">
            PNG, JPG or WEBP · Max 5 MB
          </p>
        </button>
      ) : (
        <div className="rounded-2xl border border-black/10 bg-[#fafbf9] p-5">
          <div className="flex items-center gap-4">
            <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-[#e7f3f0] text-[#0f766e]">
              <ImagePlus size={22} />
            </div>

            <div className="min-w-0 flex-1">
              <p className="truncate text-sm font-semibold text-[#17211f]">
                {file.name}
              </p>

              <p className="mt-1 text-xs text-[#7b8783]">
                {(file.size / 1024 / 1024).toFixed(2)} MB
              </p>
            </div>

            <button
              onClick={removeFile}
              className="rounded-full p-2 text-[#697773] transition hover:bg-black/5"
            >
              <X size={18} />
            </button>
          </div>

          <div className="mt-5">
            <Button
              onClick={onAnalyze}
              loading={loading}
              icon={Upload}
              className="w-full sm:w-auto"
            >
              Analyze screenshot
            </Button>
          </div>
        </div>
      )}
    </>
  );
}

export default ScreenshotAnalyzer;