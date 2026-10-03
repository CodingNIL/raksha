function Card({ children, className = "" }) {
  return (
    <div
      className={`w-full min-w-0 overflow-hidden rounded-3xl border border-black/5 bg-white p-5 shadow-[0_8px_30px_rgba(23,33,31,0.04)] sm:p-6 ${className}`}
    >
      {children}
    </div>
  );
}

export default Card;