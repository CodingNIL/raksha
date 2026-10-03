export const APP_NAME = "Raksha";

export const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export const MAX_IMAGE_SIZE = 5 * 1024 * 1024;

export const ACCEPTED_IMAGE_TYPES = [
  "image/png",
  "image/jpeg",
  "image/webp",
];

export const RISK_LEVELS = {
  LOW: "LOW APPARENT RISK",
  VERIFY: "NEEDS VERIFICATION",
  HIGH: "HIGH-RISK PATTERN",
};