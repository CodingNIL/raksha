import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Card from "../common/Card";
import InputTabs from "./InputTabs";
import TextAnalyzer from "./TextAnalyzer";
import ScreenshotAnalyzer from "./ScreenshotAnalyzer";
import SampleMessages from "./SampleMessages";
import AnalysisProgress from "./AnalysisProgress";

function Analyzer({
  onAnalyzeText,
  onAnalyzeImage,
  loading,
  progressStep,
}) {
  const [mode, setMode] = useState("text");
  const [text, setText] = useState("");
  const [file, setFile] = useState(null);

  const handleTextAnalyze = () => {
    onAnalyzeText(text);
  };

  const handleImageAnalyze = () => {
    onAnalyzeImage(file);
  };

  return (
    <section id="analyzer" className="px-5 py-20 sm:px-8">
      <div className="mx-auto max-w-4xl">

        <div className="mb-8 text-center">
          <p className="mb-3 text-sm font-semibold uppercase tracking-[0.2em] text-[#0f766e]">
            Check before you act
          </p>

          <h2 className="text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
            What are you unsure about?
          </h2>

          <p className="mx-auto mt-3 max-w-xl text-[#52615d]">
            Paste a suspicious message or upload a screenshot.
            Raksha will look for signals that deserve your attention.
          </p>
        </div>

        <AnimatePresence mode="wait">
          {loading ? (
            <motion.div
              key="loading"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
            >
              <AnalysisProgress step={progressStep} />
            </motion.div>
          ) : (
            <motion.div
              key="analyzer"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
            >
              <Card className="overflow-hidden">
                <InputTabs
                  mode={mode}
                  setMode={setMode}
                />

                <div className="p-6 sm:p-8">
                  {mode === "text" ? (
                    <>
                      <TextAnalyzer
                        text={text}
                        setText={setText}
                        onAnalyze={handleTextAnalyze}
                        loading={loading}
                      />

                      <SampleMessages
                        onSelect={setText}
                      />
                    </>
                  ) : (
                    <ScreenshotAnalyzer
                      file={file}
                      setFile={setFile}
                      onAnalyze={handleImageAnalyze}
                      loading={loading}
                    />
                  )}
                </div>
              </Card>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  );
}

export default Analyzer;