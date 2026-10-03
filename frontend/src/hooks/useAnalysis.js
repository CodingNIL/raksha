import { useState } from "react";
import {
  analyzeImage as analyzeImageRequest,
  analyzeText as analyzeTextRequest,
} from "../services/api";

function useAnalysis() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [progressStep, setProgressStep] = useState(1);

  const saveHistory = (data, type, originalInput = "") => {
    try {
      const existing = JSON.parse(
        localStorage.getItem("raksha_history") || "[]"
      );

      const risk = data?.risk || {};

      const signals = Array.isArray(
        data?.fraud_analysis?.signals
      )
        ? data.fraud_analysis.signals
        : [];

      const language =
        data?.language?.language || "Unknown";

      // Text analysis uses the original submitted text.
      // Screenshot analysis uses OCR text from result.ocr.text.
      const preview =
        type === "text"
          ? originalInput
          : data?.ocr?.text || "";

      const entry = {
        id: Date.now(),
        createdAt: new Date().toISOString(),

        type,

        preview,

        riskLevel: risk.level || "UNKNOWN",

        riskScore:
          typeof risk.score === "number"
            ? risk.score
            : Number(risk.score) || 0,

        signals,

        language,

        // Store the complete backend result so
        // "View analysis" can display it later.
        result: data,
      };

      localStorage.setItem(
        "raksha_history",
        JSON.stringify(
          [entry, ...existing].slice(0, 20)
        )
      );
    } catch {
      // History is optional.
      // Analysis should still work if saving fails.
    }
  };

  const analyzeText = async (text) => {
    if (!text?.trim()) return;

    setLoading(true);
    setError("");
    setResult(null);
    setProgressStep(1);

    try {
      const progressTimer = setTimeout(() => {
        setProgressStep(2);
      }, 700);

      const data = await analyzeTextRequest(text, true);

      clearTimeout(progressTimer);
      setProgressStep(3);

      await new Promise((resolve) =>
        setTimeout(resolve, 250)
      );

      setResult(data);

      saveHistory(data, "text", text);
    } catch (err) {
      setError(
        err.message ||
          "Something went wrong while analyzing the message."
      );
    } finally {
      setLoading(false);
    }
  };

  const analyzeImage = async (file) => {
    if (!file) return;

    if (file.size > 5 * 1024 * 1024) {
      setError("The image must be smaller than 5 MB.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);
    setProgressStep(1);

    try {
      const progressTimer = setTimeout(() => {
        setProgressStep(2);
      }, 1000);

      const data = await analyzeImageRequest(file, true);

      clearTimeout(progressTimer);
      setProgressStep(3);

      await new Promise((resolve) =>
        setTimeout(resolve, 250)
      );

      setResult(data);

      // Screenshot history stores OCR text from:
      // data.ocr.text
      saveHistory(data, "image");
    } catch (err) {
      setError(
        err.message ||
          "Something went wrong while analyzing the screenshot."
      );
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setResult(null);
    setError("");
    setLoading(false);
    setProgressStep(1);
  };

  return {
    result,
    loading,
    error,
    progressStep,
    analyzeText,
    analyzeImage,
    reset,
  };
}

export default useAnalysis;