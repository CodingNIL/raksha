import { Clock3, Trash2 } from "lucide-react";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";

function History() {
  const history = JSON.parse(
    localStorage.getItem("raksha_history") || "[]"
  );

  const clearHistory = () => {
    localStorage.removeItem("raksha_history");
    window.location.reload();
  };

  return (
    <div className="min-h-screen bg-[#f7f8f6]">
      <Navbar />

      <main className="mx-auto max-w-5xl px-5 py-20 sm:px-8">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-[#0f766e]">
              History
            </p>

            <h1 className="mt-3 text-4xl font-bold text-[#17211f]">
              Previous analyses
            </h1>
          </div>

          {history.length > 0 && (
            <button
              onClick={clearHistory}
              className="inline-flex items-center gap-2 self-start rounded-full border border-red-200 bg-white px-4 py-2.5 text-sm font-semibold text-red-600 transition hover:bg-red-50 sm:self-auto"
            >
              <Trash2 size={16} />
              Clear history
            </button>
          )}
        </div>

        {history.length === 0 ? (
          <div className="mt-10 rounded-3xl border border-black/5 bg-white p-10 text-center">
            <Clock3
              size={30}
              className="mx-auto text-[#9aa5a1]"
            />

            <h2 className="mt-4 font-bold text-[#17211f]">
              No analyses yet
            </h2>

            <p className="mt-2 text-sm text-[#697773]">
              Your completed analyses will appear here.
            </p>
          </div>
        ) : (
          <div className="mt-10 space-y-4">
            {history.map((item) => (
              <div
                key={item.id}
                className="rounded-3xl border border-black/5 bg-white p-6"
              >
                <div className="flex items-center justify-between gap-4">
                  <span className="text-xs font-medium text-[#9aa5a1]">
                    {new Date(item.createdAt).toLocaleString()}
                  </span>

                  <span className="rounded-full bg-[#f0f7f5] px-3 py-1 text-xs font-bold text-[#0f766e]">
                    {item.riskLevel}
                  </span>
                </div>

                <p className="mt-4 line-clamp-3 text-sm leading-6 text-[#52615d]">
                  {item.text || "Screenshot analysis"}
                </p>
              </div>
            ))}
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
}

export default History;