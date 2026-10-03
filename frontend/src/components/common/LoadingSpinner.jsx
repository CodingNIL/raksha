import { Loader2 } from "lucide-react";

function LoadingSpinner({ size = 24 }) {
  return (
    <Loader2
      size={size}
      className="animate-spin text-[#0f766e]"
    />
  );
}

export default LoadingSpinner;