const samples = [
  {
    label: "Urgent payment",
    text: "Your account will be blocked today. Pay ₹2,999 immediately to avoid suspension. Click this link now.",
  },
  {
    label: "Investment",
    text: "Guaranteed 300% return in 7 days. No loss possible. Send your money now and start earning.",
  },
  {
    label: "Account verification",
    text: "Your bank KYC has expired. Share your OTP and PAN details to verify your account immediately.",
  },
];

function SampleMessages({ onSelect }) {
  return (
    <div className="mt-6">
      <p className="mb-3 text-xs font-semibold uppercase tracking-wider text-[#7b8783]">
        Try an example
      </p>

      <div className="flex flex-wrap gap-2">
        {samples.map((sample) => (
          <button
            key={sample.label}
            onClick={() => onSelect(sample.text)}
            className="rounded-full border border-black/10 bg-white px-4 py-2 text-xs font-medium text-[#52615d] transition hover:border-[#0f766e]/30 hover:bg-[#f0f7f5] hover:text-[#0f766e]"
          >
            {sample.label}
          </button>
        ))}
      </div>
    </div>
  );
}

export default SampleMessages;