import { Loader2 } from "lucide-react";

function Button({
  children,
  type = "button",
  variant = "primary",
  loading = false,
  disabled = false,
  icon: Icon,
  className = "",
  onClick,
}) {
  const variants = {
    primary:
      "bg-[#0f766e] text-white hover:bg-[#0b625c] shadow-sm",
    secondary:
      "bg-white text-[#17211f] border border-black/10 hover:bg-black/[0.03]",
    dark:
      "bg-[#17211f] text-white hover:bg-[#26332f]",
    ghost:
      "bg-transparent text-[#52615d] hover:bg-black/[0.04]",
  };

  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled || loading}
      className={`inline-flex items-center justify-center gap-2 rounded-full px-5 py-3 text-sm font-semibold transition disabled:cursor-not-allowed disabled:opacity-50 ${variants[variant]} ${className}`}
    >
      {loading ? (
        <Loader2 size={17} className="animate-spin" />
      ) : (
        Icon && <Icon size={17} />
      )}

      {children}
    </button>
  );
}

export default Button;