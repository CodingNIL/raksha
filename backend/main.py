"""
FastAPI application for the SANGYAN fraud detection system.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.services.fraud_engine.engine import analyze_text


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

    return analyze_text(
        text=request.text,
        use_llm=request.use_llm,
    )