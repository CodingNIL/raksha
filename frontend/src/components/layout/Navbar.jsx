import { useState } from "react";
import {
  Menu,
  ShieldCheck,
  X,
} from "lucide-react";

function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);

  const currentPath = window.location.pathname;

  const navItems = [
    {
      label: "Analyze",
      href: "/",
    },
    {
      label: "How it works",
      href: "/how-it-works",
    },
    {
      label: "Safety",
      href: "/safety",
    },
    {
      label: "History",
      href: "/history",
    },
    {
      label: "About",
      href: "/about",
    },
  ];

  const isActive = (href) => {
    return currentPath === href;
  };

  const closeMobileMenu = () => {
    setMobileOpen(false);
  };

  return (
    <header className="sticky top-0 z-50 border-b border-black/5 bg-[#f7f8f6]/90 backdrop-blur-xl">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Brand */}
          <a
            href="/"
            onClick={closeMobileMenu}
            className="flex shrink-0 items-center gap-2.5"
          >
            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-[#0f766e] text-white shadow-sm">
              <ShieldCheck
                size={20}
                strokeWidth={2.2}
              />
            </div>

            <span className="text-lg font-bold tracking-tight text-[#17211f]">
              Raksha
            </span>
          </a>

          {/* Desktop navigation */}
          <nav className="hidden items-center gap-1 md:flex">
            {navItems.map((item) => {
              const active = isActive(item.href);

              return (
                <a
                  key={item.href}
                  href={item.href}
                  className={`rounded-full px-3.5 py-2 text-sm font-medium transition ${
                    active
                      ? "bg-[#e5f3ef] text-[#0f766e]"
                      : "text-[#52615d] hover:bg-black/[0.03] hover:text-[#17211f]"
                  }`}
                >
                  {item.label}
                </a>
              );
            })}
          </nav>

          {/* Desktop CTA */}
          <a
            href="/#analyzer"
            className="hidden rounded-full bg-[#17211f] px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-[#26332f] md:block"
          >
            Try Raksha
          </a>

          {/* Mobile menu button */}
          <button
            type="button"
            onClick={() => setMobileOpen((open) => !open)}
            aria-label={
              mobileOpen
                ? "Close navigation menu"
                : "Open navigation menu"
            }
            aria-expanded={mobileOpen}
            className="flex h-10 w-10 items-center justify-center rounded-xl border border-black/5 bg-white text-[#17211f] transition hover:bg-black/[0.03] md:hidden"
          >
            {mobileOpen ? (
              <X size={20} />
            ) : (
              <Menu size={20} />
            )}
          </button>
        </div>

        {/* Mobile navigation */}
        {mobileOpen && (
          <div className="border-t border-black/5 py-4 md:hidden">
            <nav className="flex flex-col gap-1">
              {navItems.map((item) => {
                const active = isActive(item.href);

                return (
                  <a
                    key={item.href}
                    href={item.href}
                    onClick={closeMobileMenu}
                    className={`rounded-xl px-4 py-3 text-sm font-medium transition ${
                      active
                        ? "bg-[#e5f3ef] text-[#0f766e]"
                        : "text-[#52615d] hover:bg-black/[0.03] hover:text-[#17211f]"
                    }`}
                  >
                    {item.label}
                  </a>
                );
              })}

              <a
                href="/#analyzer"
                onClick={closeMobileMenu}
                className="mt-2 rounded-xl bg-[#17211f] px-4 py-3 text-center text-sm font-semibold text-white transition hover:bg-[#26332f]"
              >
                Try Raksha
              </a>
            </nav>
          </div>
        )}
      </div>
    </header>
  );
}

export default Navbar;
