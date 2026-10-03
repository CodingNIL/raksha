import { ShieldCheck } from "lucide-react";

function Footer() {
  return (
    <footer className="border-t border-black/5 bg-white">
      <div className="mx-auto max-w-7xl px-5 py-12 sm:px-8">
        <div className="grid gap-10 md:grid-cols-[1.5fr_1fr_1fr]">
          {/* Brand */}
          <div>
            <a
              href="/"
              className="inline-flex items-center gap-2.5"
            >
              <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-[#0f766e] text-white">
                <ShieldCheck size={19} strokeWidth={2.2} />
              </div>

              <span className="text-lg font-bold tracking-tight text-[#17211f]">
                Raksha
              </span>
            </a>

            <p className="mt-4 max-w-sm text-sm leading-6 text-[#697773]">
              Understand suspicious messages and identify signals that
              deserve a closer look before you act.
            </p>
          </div>

          {/* Explore */}
          <div>
            <p className="text-xs font-semibold uppercase tracking-[0.16em] text-[#0f766e]">
              Explore
            </p>

            <nav className="mt-4 flex flex-col items-start gap-3 text-sm text-[#52615d]">
              <a
                href="/"
                className="transition hover:text-[#0f766e]"
              >
                Analyze
              </a>

              <a
                href="/how-it-works"
                className="transition hover:text-[#0f766e]"
              >
                How it works
              </a>

              <a
                href="/safety"
                className="transition hover:text-[#0f766e]"
              >
                Safety
              </a>

              <a
                href="/history"
                className="transition hover:text-[#0f766e]"
              >
                History
              </a>

              <a
                href="/about"
                className="transition hover:text-[#0f766e]"
              >
                About
              </a>
            </nav>
          </div>

          {/* Important note */}
          <div>
            <p className="text-xs font-semibold uppercase tracking-[0.16em] text-[#0f766e]">
              Remember
            </p>

            <p className="mt-4 text-sm leading-6 text-[#697773]">
              Raksha highlights signals and patterns. Its assessment should
              be used as guidance, not as a guarantee that a message is
              safe or fraudulent.
            </p>
          </div>
        </div>

        <div className="mt-10 flex flex-col gap-3 border-t border-black/5 pt-6 sm:flex-row sm:items-center sm:justify-between">
          <p className="text-xs text-[#9aa5a1]">
            © {new Date().getFullYear()} Raksha
          </p>

          <p className="text-xs text-[#9aa5a1]">
            Understand before you act.
          </p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;