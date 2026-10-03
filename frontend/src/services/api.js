
const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

async function parseResponse(response) {
  const data = await response.json().catch(() => null);

  if (!response.ok) {
    throw new Error(
      data?.detail ||
        data?.message ||
        `Request failed with status ${response.status}`
    );
  }

  return data;
}

export async function analyzeText(text, useLLM = true) {
  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text,
      use_llm: useLLM,
    }),
  });

  const data = await parseResponse(response);

  console.log("========== RAKSHA BACKEND RESPONSE ==========");
  console.log(data);
  console.log("==============================================");

  return data;
}

export async function analyzeImage(file, useLLM = true) {
  const formData = new FormData();

  formData.append("image", file);
  formData.append("use_llm", String(useLLM));

  const response = await fetch(`${API_BASE_URL}/analyze-image`, {
    method: "POST",
    body: formData,
  });

  const data = await parseResponse(response);

  console.log("========== RAKSHA IMAGE RESPONSE ==========");
  console.log(data);
  console.log("============================================");

  return data;
}

export async function checkHealth() {
  const response = await fetch(`${API_BASE_URL}/`);

  const data = await parseResponse(response);

  console.log("========== RAKSHA HEALTH RESPONSE ==========");
  console.log(data);
  console.log("=============================================");

  return data;
}

