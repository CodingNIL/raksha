import { useState } from "react";
import { ArrowDown, ShieldCheck } from "lucide-react";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";
import Analyzer from "../components/analyzer/Analyzer";
import AnalysisResult from "../components/results/AnalysisResult";
import useAnalysis from "../hooks/useAnalysis";

function Analyze() {
  const {
    result,
    loading,
    error,
    progressStep,
    analyzeText,
    analyzeImage,
    reset,
  } = useAnalysis();

  const [hasStarted, setHasStarted] = useState(false);

  const handleText = async (text) => {
    setHasStarted(true);
    await analyzeText(text);
  };

  const handleImage = async (file) => {
    setHasStarted(true);
    await analyzeImage(file);
  };

  const handleReset = () => {
    reset();
    setHasStarted(false);
  };

  return (
    <div className="min-h-screen bg-[#f7f8f6]">
      <Navbar />

      <main>
        {!hasStarted && (
          <section className="relative overflow-hidden px-5 sm:px-8">
            <div
              aria-hidden="true"
              className="pointer-events-none absolute left-1/2 top-20 h-72 w-72 -translate-x-1/2 rounded-full bg-[#d9eee9] opacity-40 blur-3xl"
            />

            <div className="relative mx-auto flex min-h-[calc(100vh-4rem)] max-w-7xl items-center justify-center py-20 sm:py-24">
              <div className="max-w-4xl text-center">
                <div className="mb-7 inline-flex items-center gap-2 rounded-full border border-[#cfe5df] bg-white/70 px-4 py-2 text-sm font-medium text-[#0f766e] shadow-sm backdrop-blur-sm">
                  <ShieldCheck size={17} strokeWidth={2} />
                  <span>Digital safety, before you act</span>
                </div>

                <h1 className="text-5xl font-bold leading-[1.02] tracking-[-0.04em] text-[#17211f] sm:text-6xl lg:text-7xl">
                  Understand before
                  <span className="block text-[#0f766e]">
                    you act.
                  </span>
                </h1>

                <p className="mx-auto mt-7 max-w-2xl text-base leading-7 text-[#52615d] sm:text-lg sm:leading-8">
                  Not sure about a message, payment request, or screenshot?
                  Raksha helps you identify suspicious signals and understand
                  what deserves a closer look.
                </p>

                <div className="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
                  <a
                    href="#analyzer"
                    className="inline-flex items-center justify-center gap-2 rounded-full bg-[#0f766e] px-7 py-3.5 text-sm font-semibold text-white shadow-sm transition hover:bg-[#0b625c] hover:shadow-md"
                  >
                    Check a message
                    <ArrowDown size={17} />
                  </a>

                  <a
                    href="/how-it-works"
                    className="inline-flex items-center justify-center rounded-full border border-black/10 bg-white px-7 py-3.5 text-sm font-semibold text-[#17211f] transition hover:border-black/15 hover:bg-black/[0.02]"
                  >
                    How it works
                  </a>
                </div>

                <p className="mt-6 text-xs text-[#7a8783]">
                  Raksha highlights signals. It does not replace your
                  judgment.
                </p>
              </div>
            </div>
          </section>
        )}

        <Analyzer
          onAnalyzeText={handleText}
          onAnalyzeImage={handleImage}
          loading={loading}
          progressStep={progressStep}
        />

        {error && (
          <div className="mx-auto max-w-4xl px-5 pb-8 sm:px-8">
            <div className="rounded-2xl border border-red-200 bg-red-50 p-5 text-sm leading-6 text-red-700">
              {error}
            </div>
          </div>
        )}

        {result && (
          <AnalysisResult
            result={result}
            onReset={handleReset}
          />
        )}

        {!hasStarted && (
          <section className="border-t border-black/5 px-5 py-20 sm:px-8">
            <div className="mx-auto max-w-5xl text-center">
              <p className="text-sm font-semibold uppercase tracking-[0.2em] text-[#0f766e]">
                Why Raksha
              </p>

              <h2 className="mt-3 text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
                Look for signals, not certainty.
              </h2>

              <p className="mx-auto mt-4 max-w-2xl leading-7 text-[#697773]">
                Raksha helps you understand suspicious patterns so you can
                make a more informed decision before sending money,
                sharing information, or following a link.
              </p>
            </div>
          </section>
        )}
      </main>

      <Footer />
    </div>
  );
}

export default Analyze;