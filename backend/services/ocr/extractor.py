"""
OCR extraction service.

Extracts text from an image and returns plain text that can be
passed into the existing fraud-analysis pipeline.
"""

from io import BytesIO

from PIL import Image, UnidentifiedImageError
from rapidocr_onnxruntime import RapidOCR


_OCR = RapidOCR()


class OCRExtractionError(ValueError):
    """Raised when OCR input cannot be decoded or processed."""


def extract_text_from_image(image_bytes: bytes) -> str:
    """
    Extract text from image bytes using RapidOCR.

    Args:
        image_bytes: Raw image bytes.

    Returns:
        Extracted text as a single normalized whitespace-separated string.

    Raises:
        OCRExtractionError: If the image is invalid or OCR fails.
    """

    if not image_bytes:
        raise OCRExtractionError("Image is empty.")

    try:
        image = Image.open(BytesIO(image_bytes))
        image.load()
    except (UnidentifiedImageError, OSError) as exc:
        raise OCRExtractionError("Invalid or unsupported image.") from exc

    try:
        result, _ = _OCR(image)
    except Exception as exc:
        raise OCRExtractionError("OCR processing failed.") from exc

    if not result:
        return ""

    text_parts = []

    for item in result:
        if not item:
            continue

        # RapidOCR returns detection entries whose second element
        # is the recognized text.
        if len(item) >= 2 and item[1]:
            text_parts.append(str(item[1]))

    return " ".join(text_parts).strip()
