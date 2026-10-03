import {
  AlertTriangle,
  CheckCircle2,
  Info,
  ShieldCheck,
} from "lucide-react";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";
import Card from "../components/common/Card";

function Safety() {
  const canDo = [
    "Identify suspicious patterns in submitted messages.",
    "Highlight signals such as urgency, impersonation, payment requests, and sensitive-data requests.",
    "Show evidence that contributed to the assessment.",
    "Suggest safer actions to consider before responding.",
  ];

  const cannotGuarantee = [
    "That a message is definitely a scam.",
    "That a message with no detected signals is completely safe.",
    "That every new or sophisticated scam will be detected.",
    "That the assessment replaces your own verification or judgment.",
  ];

  const safeSteps = [
    "Do not rush because a message creates urgency or pressure.",
    "Verify unexpected requests through an independent, trusted channel.",
    "Avoid sharing OTPs, passwords, PINs, or other sensitive information.",
    "Do not send money simply because a message appears convincing.",
    "When in doubt, pause and verify before taking action.",
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
              Safety first
            </p>

            <h1 className="mt-4 text-4xl font-bold tracking-[-0.03em] text-[#17211f] sm:text-5xl lg:text-6xl">
              Use the signal.
              <span className="block text-[#0f766e]">
                Keep your judgment.
              </span>
            </h1>

            <p className="mx-auto mt-6 max-w-2xl text-base leading-7 text-[#52615d] sm:text-lg sm:leading-8">
              Raksha is designed to help you slow down and understand
              suspicious patterns. Its assessment is guidance—not a
              guarantee.
            </p>
          </div>
        </section>

        {/* Core principle */}
        <section className="px-5 pb-20 sm:px-8">
          <div className="mx-auto max-w-5xl">
            <div className="rounded-3xl border border-[#cfe5df] bg-[#eef7f4] p-7 sm:p-10">
              <div className="flex flex-col gap-6 sm:flex-row sm:items-start">
                <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-white text-[#0f766e] shadow-sm">
                  <Info size={23} />
                </div>

                <div>
                  <p className="text-xs font-semibold uppercase tracking-[0.16em] text-[#0f766e]">
                    The important part
                  </p>

                  <h2 className="mt-2 text-2xl font-bold tracking-tight text-[#17211f] sm:text-3xl">
                    A low-risk result does not mean “safe.”
                  </h2>

                  <p className="mt-3 max-w-3xl text-sm leading-7 text-[#52615d] sm:text-base">
                    Raksha can only assess the signals present in the
                    content you submit. A message may still be harmful
                    even when no obvious warning signals are detected.
                    Always consider the context and verify important
                    requests independently.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Can / cannot */}
        <section className="border-y border-black/5 bg-white px-5 py-20 sm:px-8">
          <div className="mx-auto grid max-w-6xl gap-6 lg:grid-cols-2">
            <Card className="p-6 sm:p-8">
              <div className="flex items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-[#e5f3ef] text-[#0f766e]">
                  <CheckCircle2 size={19} />
                </div>

                <h2 className="text-xl font-bold text-[#17211f]">
                  What Raksha can do
                </h2>
              </div>

              <div className="mt-6 space-y-3">
                {canDo.map((item) => (
                  <div
                    key={item}
                    className="flex items-start gap-3 rounded-2xl bg-[#f7f8f6] px-4 py-3.5"
                  >
                    <CheckCircle2
                      size={17}
                      className="mt-0.5 shrink-0 text-[#0f766e]"
                    />

                    <p className="text-sm leading-6 text-[#52615d]">
                      {item}
                    </p>
                  </div>
                ))}
              </div>
            </Card>

            <Card className="p-6 sm:p-8">
              <div className="flex items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-amber-50 text-amber-600">
                  <AlertTriangle size={19} />
                </div>

                <h2 className="text-xl font-bold text-[#17211f]">
                  What Raksha cannot guarantee
                </h2>
              </div>

              <div className="mt-6 space-y-3">
                {cannotGuarantee.map((item) => (
                  <div
                    key={item}
                    className="flex items-start gap-3 rounded-2xl bg-[#f7f8f6] px-4 py-3.5"
                  >
                    <AlertTriangle
                      size={17}
                      className="mt-0.5 shrink-0 text-amber-600"
                    />

                    <p className="text-sm leading-6 text-[#52615d]">
                      {item}
                    </p>
                  </div>
                ))}
              </div>
            </Card>
          </div>
        </section>

        {/* Safe behavior */}
        <section className="px-5 py-20 sm:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="max-w-2xl">
              <p className="text-sm font-semibold uppercase tracking-[0.18em] text-[#0f766e]">
                If something feels suspicious
              </p>

              <h2 className="mt-3 text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
                Pause. Verify. Then act.
              </h2>

              <p className="mt-4 text-base leading-7 text-[#697773]">
                A few simple habits can make it harder for fraudulent
                requests to pressure you into making a quick decision.
              </p>
            </div>

            <div className="mt-10 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {safeSteps.map((step, index) => (
                <Card
                  key={step}
                  className="relative p-6"
                >
                  <span className="text-sm font-semibold text-[#a0aaa7]">
                    0{index + 1}
                  </span>

                  <h3 className="mt-4 text-lg font-bold text-[#17211f]">
                    {index === 0
                      ? "Slow down"
                      : index === 1
                        ? "Verify independently"
                        : index === 2
                          ? "Protect sensitive information"
                          : index === 3
                            ? "Question payment requests"
                            : "When unsure, pause"}
                  </h3>

                  <p className="mt-2 text-sm leading-6 text-[#697773]">
                    {step}
                  </p>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="border-t border-black/5 bg-[#17211f] px-5 py-20 sm:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-white/10 text-[#bde4dc]">
              <ShieldCheck size={24} />
            </div>

            <h2 className="mt-5 text-3xl font-bold tracking-tight text-white sm:text-4xl">
              Unsure about a message?
            </h2>

            <p className="mx-auto mt-4 max-w-xl text-base leading-7 text-[#b7c2bf]">
              Take a moment to examine the signals before you respond,
              send money, or share information.
            </p>

            <a
              href="/#analyzer"
              className="mt-7 inline-flex items-center rounded-full bg-white px-7 py-3.5 text-sm font-semibold text-[#17211f] shadow-sm transition hover:bg-[#eef7f4]"
            >
              Check a message
            </a>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default Safety;