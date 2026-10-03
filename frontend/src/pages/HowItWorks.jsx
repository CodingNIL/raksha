import {
  ArrowRight,
  BrainCircuit,
  FileSearch,
  MessageSquareText,
  ShieldCheck,
} from "lucide-react";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";
import Card from "../components/common/Card";

function HowItWorks() {
  const steps = [
    {
      number: "01",
      icon: MessageSquareText,
      title: "Submit the content",
      description:
        "Paste a message or upload a screenshot containing the request you want to examine.",
    },
    {
      number: "02",
      icon: BrainCircuit,
      title: "Raksha analyzes it",
      description:
        "The system extracts relevant text and checks for patterns such as urgency, impersonation, payment requests, and other warning signals.",
    },
    {
      number: "03",
      icon: FileSearch,
      title: "Understand the result",
      description:
        "Raksha presents the detected indicators, supporting evidence, explanation, and safer next steps in one place.",
    },
  ];

  const signals = [
    "Urgent or pressure-based requests",
    "Requests involving money or payments",
    "Impersonation or suspicious identity claims",
    "Requests for sensitive information",
    "Unknown apps, APKs, or potentially unsafe links",
    "Claims involving guaranteed returns or recovery fees",
  ];

  return (
    <div className="min-h-screen bg-[#f7f8f6]">
      <Navbar />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden px-5 sm:px-8">
          <div
            aria-hidden="true"
            className="pointer-events-none absolute left-1/2 top-16 h-72 w-72 -translate-x-1/2 rounded-full bg-[#d9eee9] opacity-40 blur-3xl"
          />

          <div className="relative mx-auto max-w-4xl px-0 py-24 text-center sm:py-28">
            <div className="mx-auto mb-6 flex h-12 w-12 items-center justify-center rounded-2xl bg-[#e5f3ef] text-[#0f766e]">
              <ShieldCheck size={25} strokeWidth={2} />
            </div>

            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-[#0f766e]">
              How it works
            </p>

            <h1 className="mt-4 text-4xl font-bold tracking-[-0.03em] text-[#17211f] sm:text-5xl lg:text-6xl">
              From uncertainty to
              <span className="block text-[#0f766e]">
                clearer signals.
              </span>
            </h1>

            <p className="mx-auto mt-6 max-w-2xl text-base leading-7 text-[#52615d] sm:text-lg sm:leading-8">
              Raksha examines suspicious messages and screenshots for
              recognizable risk signals, then presents the findings in a
              way that's easier to understand.
            </p>
          </div>
        </section>

        {/* Steps */}
        <section className="px-5 pb-20 sm:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="grid gap-5 md:grid-cols-3">
              {steps.map((step, index) => {
                const Icon = step.icon;

                return (
                  <Card
                    key={step.number}
                    className="relative p-6 sm:p-7"
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-[#e5f3ef] text-[#0f766e]">
                        <Icon size={21} />
                      </div>

                      <span className="text-sm font-semibold text-[#a0aaa7]">
                        {step.number}
                      </span>
                    </div>

                    <h2 className="mt-6 text-xl font-bold text-[#17211f]">
                      {step.title}
                    </h2>

                    <p className="mt-3 text-sm leading-6 text-[#697773]">
                      {step.description}
                    </p>

                    {index < steps.length - 1 && (
                      <ArrowRight
                        size={18}
                        className="absolute -right-7 top-1/2 hidden -translate-y-1/2 text-[#a7b5b1] md:block"
                      />
                    )}
                  </Card>
                );
              })}
            </div>
          </div>
        </section>

        {/* What Raksha checks */}
        <section className="border-y border-black/5 bg-white px-5 py-20 sm:px-8">
          <div className="mx-auto grid max-w-6xl gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
            <div>
              <p className="text-sm font-semibold uppercase tracking-[0.18em] text-[#0f766e]">
                What Raksha checks
              </p>

              <h2 className="mt-3 text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
                Look for patterns that deserve attention.
              </h2>

              <p className="mt-5 max-w-xl text-base leading-7 text-[#697773]">
                Raksha doesn't need to decide whether a message is
                trustworthy on its own. Instead, it surfaces recognizable
                signals that can help you investigate the request more
                carefully.
              </p>
            </div>

            <div className="grid gap-3 sm:grid-cols-2">
              {signals.map((signal) => (
                <div
                  key={signal}
                  className="flex items-start gap-3 rounded-2xl border border-black/5 bg-[#f7f8f6] p-4"
                >
                  <div className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-lg bg-[#e5f3ef] text-[#0f766e]">
                    <ShieldCheck size={15} />
                  </div>

                  <p className="text-sm leading-6 text-[#52615d]">
                    {signal}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Result explanation */}
        <section className="px-5 py-20 sm:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="max-w-2xl">
              <p className="text-sm font-semibold uppercase tracking-[0.18em] text-[#0f766e]">
                Understanding the result
              </p>

              <h2 className="mt-3 text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
                The result is more than a label.
              </h2>

              <p className="mt-4 text-base leading-7 text-[#697773]">
                Raksha gives you several pieces of information so you can
                understand why a message received a particular assessment.
              </p>
            </div>

            <div className="mt-10 grid gap-5 md:grid-cols-3">
              <Card>
                <p className="text-sm font-semibold text-[#0f766e]">
                  Risk assessment
                </p>

                <h3 className="mt-2 text-lg font-bold text-[#17211f]">
                  A clear risk level
                </h3>

                <p className="mt-2 text-sm leading-6 text-[#697773]">
                  The result shows whether the submitted content has low
                  apparent risk, needs verification, or contains a
                  high-risk pattern.
                </p>
              </Card>

              <Card>
                <p className="text-sm font-semibold text-[#0f766e]">
                  Evidence
                </p>

                <h3 className="mt-2 text-lg font-bold text-[#17211f]">
                  What was noticed
                </h3>

                <p className="mt-2 text-sm leading-6 text-[#697773]">
                  Detected signals and supporting evidence help explain
                  what contributed to the assessment.
                </p>
              </Card>

              <Card>
                <p className="text-sm font-semibold text-[#0f766e]">
                  Next steps
                </p>

                <h3 className="mt-2 text-lg font-bold text-[#17211f]">
                  What you can do
                </h3>

                <p className="mt-2 text-sm leading-6 text-[#697773]">
                  Safer actions are provided to help you avoid rushing
                  into a potentially harmful request.
                </p>
              </Card>
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="border-t border-black/5 bg-[#eef7f4] px-5 py-20 sm:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-white text-[#0f766e] shadow-sm">
              <ShieldCheck size={24} />
            </div>

            <h2 className="mt-5 text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
              Have a message you're unsure about?
            </h2>

            <p className="mx-auto mt-4 max-w-xl text-base leading-7 text-[#697773]">
              Check the message before you respond, pay, share information,
              or follow a link.
            </p>

            <a
              href="/#analyzer"
              className="mt-7 inline-flex items-center gap-2 rounded-full bg-[#0f766e] px-7 py-3.5 text-sm font-semibold text-white shadow-sm transition hover:bg-[#0b625c] hover:shadow-md"
            >
              Analyze a message
              <ArrowRight size={17} />
            </a>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default HowItWorks;