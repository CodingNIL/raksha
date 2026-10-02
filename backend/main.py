"""
FastAPI application for the SANGYAN fraud detection system.
"""

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.services.fraud_engine.engine import analyze_text

# API input limits
MAX_TEXT_LENGTH = 10_000
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

from backend.services.ocr.extractor import OCRExtractionError, extract_text_from_image


# ---------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------

app = FastAPI(
    title="SANGYAN Fraud Detection API",
    description=(
        "API for multilingual digital fraud and scam detection."
    ),
    version="1.0.0",
)


# ---------------------------------------------------------
# CORS configuration
# ---------------------------------------------------------
#
# Allows the frontend application to communicate with
# the FastAPI backend during development.
#
# We currently allow common local development origins.
# This can be restricted to the deployed frontend domain
# before production deployment.
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# Request model
# ---------------------------------------------------------

class AnalyzeRequest(BaseModel):
    """
    Request body for fraud analysis.
    """

    text: str
    use_llm: bool = False


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/")
def root():
    """
    Basic API health check.
    """

    return {
        "success": True,
        "message": "SANGYAN Fraud Detection API is running."
    }


# ---------------------------------------------------------
# Fraud analysis endpoint
# ---------------------------------------------------------

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    """
    Analyze a financial message for potential fraud signals.
    """

    if not request.text or not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty.",
        )

    if len(request.text) > MAX_TEXT_LENGTH:
        raise HTTPException(
            status_code=413,
            detail=f"Text exceeds maximum length of {MAX_TEXT_LENGTH} characters.",
        )

    return analyze_text(
        text=request.text,
        use_llm=request.use_llm,
    )

# ---------------------------------------------------------
# Image fraud analysis endpoint
# ---------------------------------------------------------

@app.post("/analyze-image")
async def analyze_image(
    image: UploadFile = File(...),
    use_llm: bool = False,
):
    """
    Extract text from an uploaded image and run the existing
    fraud-analysis pipeline on the OCR output.
    """

    if image.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image type. Allowed types: JPEG, PNG, WEBP.",
        )

    image_bytes = await image.read()

    if len(image_bytes) > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Image exceeds maximum size of 5 MB.",
        )

    if not image_bytes:
        raise HTTPException(
            status_code=400,
            detail="Uploaded image is empty.",
        )

    try:
        extracted_text = extract_text_from_image(image_bytes)
    except OCRExtractionError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    if not extracted_text:
        return {
            "success": False,
            "message": "No readable text found in image.",
            "ocr": {
                "text": "",
                "filename": image.filename,
            },
        }

    result = analyze_text(
        text=extracted_text,
        use_llm=use_llm,
    )

    result["ocr"] = {
        "text": extracted_text,
        "filename": image.filename,
    }

    return result
