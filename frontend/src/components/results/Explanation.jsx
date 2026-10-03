function Explanation({ explanation }) {
  if (!explanation) return null;

  const items = Array.isArray(explanation)
    ? explanation
    : [explanation];

  const formattedItems = items
    .map((item) => {
      if (typeof item === "string") {
        return item;
      }

      if (item && typeof item === "object") {
        return (
          item.text ||
          item.summary ||
          item.explanation ||
          item.reason ||
          null
        );
      }

      return null;
    })
    .filter(Boolean);

  if (formattedItems.length === 0) {
    return null;
  }

  return (
    <div className="rounded-2xl bg-[#f7f8f6] p-5">
      <p className="mb-3 text-xs font-semibold uppercase tracking-[0.14em] text-[#0f766e]">
        Explanation
      </p>

      <div className="space-y-2">
        {formattedItems.map((item, index) => (
          <p
            key={index}
            className="whitespace-pre-wrap break-words text-sm leading-7 text-[#52615d]"
          >
            {item}
          </p>
        ))}
      </div>
    </div>
  );
}

export default Explanation;