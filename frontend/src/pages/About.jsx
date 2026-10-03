import {
  ArrowRight,
  Eye,
  HeartHandshake,
  ShieldCheck,
  Sparkles,
} from "lucide-react";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";
import Card from "../components/common/Card";

function About() {
  const principles = [
    {
      icon: Eye,
      title: "Clarity over certainty",
      description:
        "Raksha focuses on showing the signals behind an assessment instead of pretending that every message can be classified with absolute certainty.",
    },
    {
      icon: HeartHandshake,
      title: "People stay in control",
      description:
        "The goal is to help people pause, understand, and verify—not to make important decisions on their behalf.",
    },
    {
      icon: ShieldCheck,
      title: "Safety before action",
      description:
        "Raksha encourages safer behavior when a request involves money, sensitive information, urgency, or other warning signals.",
    },
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
              About Raksha
            </p>

            <h1 className="mt-4 text-4xl font-bold tracking-[-0.03em] text-[#17211f] sm:text-5xl lg:text-6xl">
              Built to help you
              <span className="block text-[#0f766e]">
                pause before you act.
              </span>
            </h1>

            <p className="mx-auto mt-6 max-w-2xl text-base leading-7 text-[#52615d] sm:text-lg sm:leading-8">
              Raksha is a digital safety assistant that helps people
              examine suspicious messages, understand warning signals,
              and make more informed decisions.
            </p>
          </div>
        </section>

        {/* Story */}
        <section className="px-5 pb-20 sm:px-8">
          <div className="mx-auto grid max-w-6xl gap-6 lg:grid-cols-[1.05fr_0.95fr]">
            <Card className="p-7 sm:p-9">
              <p className="text-sm font-semibold uppercase tracking-[0.16em] text-[#0f766e]">
                The problem
              </p>

              <h2 className="mt-3 text-2xl font-bold tracking-tight text-[#17211f] sm:text-3xl">
                Suspicious messages often rely on pressure.
              </h2>

              <p className="mt-5 text-sm leading-7 text-[#697773] sm:text-base">
                A message can look convincing while asking you to act
                immediately, send money, share sensitive information,
                install an unfamiliar application, or trust an unexpected
                identity.
              </p>

              <p className="mt-4 text-sm leading-7 text-[#697773] sm:text-base">
                In those moments, having a second layer of analysis can
                make it easier to slow down and examine what is actually
                being asked.
              </p>
            </Card>

            <Card className="bg-[#eef7f4] p-7 sm:p-9">
              <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-white text-[#0f766e] shadow-sm">
                <Sparkles size={21} />
              </div>

              <p className="mt-6 text-sm font-semibold uppercase tracking-[0.16em] text-[#0f766e]">
                The idea
              </p>

              <h2 className="mt-3 text-2xl font-bold tracking-tight text-[#17211f] sm:text-3xl">
                Turn uncertainty into something you can inspect.
              </h2>

              <p className="mt-5 text-sm leading-7 text-[#52615d] sm:text-base">
                Instead of simply returning a label, Raksha breaks an
                assessment into signals, evidence, explanation, and safer
                next steps.
              </p>
            </Card>
          </div>
        </section>

        {/* Principles */}
        <section className="border-y border-black/5 bg-white px-5 py-20 sm:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="max-w-2xl">
              <p className="text-sm font-semibold uppercase tracking-[0.18em] text-[#0f766e]">
                What Raksha stands for
              </p>

              <h2 className="mt-3 text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
                Designed around responsible assistance.
              </h2>

              <p className="mt-4 text-base leading-7 text-[#697773]">
                The interface and analysis flow are built around a simple
                principle: useful technology should help people understand
                a situation without taking away their agency.
              </p>
            </div>

            <div className="mt-10 grid gap-5 md:grid-cols-3">
              {principles.map((principle) => {
                const Icon = principle.icon;

                return (
                  <Card
                    key={principle.title}
                    className="p-6 sm:p-7"
                  >
                    <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-[#e5f3ef] text-[#0f766e]">
                      <Icon size={21} />
                    </div>

                    <h3 className="mt-6 text-xl font-bold text-[#17211f]">
                      {principle.title}
                    </h3>

                    <p className="mt-3 text-sm leading-6 text-[#697773]">
                      {principle.description}
                    </p>
                  </Card>
                );
              })}
            </div>
          </div>
        </section>

        {/* How Raksha approaches analysis */}
        <section className="px-5 py-20 sm:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="grid gap-10 lg:grid-cols-[0.85fr_1.15fr] lg:items-center">
              <div>
                <p className="text-sm font-semibold uppercase tracking-[0.18em] text-[#0f766e]">
                  Behind the experience
                </p>

                <h2 className="mt-3 text-3xl font-bold tracking-tight text-[#17211f] sm:text-4xl">
                  Analysis that stays explainable.
                </h2>

                <p className="mt-5 text-base leading-7 text-[#697773]">
                  Raksha combines structured analysis with language and
                  image processing to turn submitted content into a
                  readable safety assessment.
                </p>
              </div>

              <div className="space-y-3">
                {[
                  [
                    "01",
                    "Extract",
                    "Read the submitted text or extract text from an uploaded screenshot.",
                  ],
                  [
                    "02",
                    "Identify",
                    "Look for recognizable signals and supporting evidence.",
                  ],
                  [
                    "03",
                    "Assess",
                    "Combine detected signals into a structured risk assessment.",
                  ],
                  [
                    "04",
                    "Explain",
                    "Present the findings and safer actions in plain language.",
                  ],
                ].map(([number, title, description]) => (
                  <div
                    key={number}
                    className="flex gap-4 rounded-2xl border border-black/5 bg-white p-5 shadow-[0_8px_30px_rgba(23,33,31,0.04)]"
                  >
                    <span className="shrink-0 pt-0.5 text-sm font-semibold text-[#a0aaa7]">
                      {number}
                    </span>

                    <div>
                      <h3 className="font-bold text-[#17211f]">
                        {title}
                      </h3>

                      <p className="mt-1 text-sm leading-6 text-[#697773]">
                        {description}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
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
              Understand before you act.
            </h2>

            <p className="mx-auto mt-4 max-w-xl text-base leading-7 text-[#b7c2bf]">
              Have something you're unsure about? Let Raksha help you
              inspect the signals before you decide what to do next.
            </p>

            <a
              href="/#analyzer"
              className="mt-7 inline-flex items-center gap-2 rounded-full bg-white px-7 py-3.5 text-sm font-semibold text-[#17211f] shadow-sm transition hover:bg-[#eef7f4]"
            >
              Try Raksha
              <ArrowRight size={17} />
            </a>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default About;