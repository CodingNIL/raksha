"""
Multilingual OCR extraction service.

Extracts text from an image and returns plain text that can be
passed into the existing fraud-analysis pipeline.

Supported practical cases:
- English
- Banglish
- Hinglish
- Bengali script + English
- Hindi script + English
- Bengali/Hindi mixed with English

EasyOCR is used because the fraud-analysis backend needs reliable
recognition of Bengali and Hindi scripts in addition to Latin text.
"""

from io import BytesIO
from typing import Any

import numpy as np
from PIL import Image, UnidentifiedImageError
import easyocr


# Readers are initialized lazily so importing the backend does not
# immediately load large OCR models into memory.
_READERS: dict[str, easyocr.Reader] = {}


class OCRExtractionError(ValueError):
    """Raised when OCR input cannot be decoded or processed."""


def _get_reader(language: str) -> easyocr.Reader:
    """
    Return a cached EasyOCR reader for the requested language group.

    Args:
        language:
            "en" for Latin-script text,
            "bn" for Bengali + English,
            "hi" for Hindi + English.

    Returns:
        Cached EasyOCR Reader instance.
    """

    if language not in _READERS:
        if language == "bn":
            languages = ["bn", "en"]
        elif language == "hi":
            languages = ["hi", "en"]
        else:
            languages = ["en"]

        _READERS[language] = easyocr.Reader(
            languages,
            gpu=False,
        )

    return _READERS[language]


def _prepare_image(image_bytes: bytes) -> np.ndarray:
    """
    Validate image bytes and convert them into an RGB NumPy array.

    Narrow/short screenshots are upscaled to improve OCR quality.

    Args:
        image_bytes:
            Raw image bytes.

    Returns:
        RGB image as a NumPy array.

    Raises:
        OCRExtractionError:
            If the image cannot be decoded.
    """

    if not image_bytes:
        raise OCRExtractionError("Image is empty.")

    try:
        with Image.open(BytesIO(image_bytes)) as image:
            image.verify()

        # verify() invalidates the image object for further use,
        # so reopen the image before converting it.
        with Image.open(BytesIO(image_bytes)) as image:
            image = image.convert("RGB")

            width, height = image.size

            # Small/narrow screenshots can be difficult for OCR.
            # Upscale them before recognition.
            if height < 150:
                scale = 3
                image = image.resize(
                    (width * scale, height * scale),
                    Image.Resampling.LANCZOS,
                )

            return np.asarray(image)

    except (UnidentifiedImageError, OSError, ValueError) as exc:
        raise OCRExtractionError(
            "Invalid or unsupported image."
        ) from exc


def _extract_results(result: list[Any]) -> list[tuple[str, float]]:
    """
    Convert EasyOCR output into text/confidence pairs.

    Args:
        result:
            Raw EasyOCR result.

    Returns:
        List of (text, confidence) tuples.
    """

    extracted: list[tuple[str, float]] = []

    for item in result:
        if not item or len(item) < 3:
            continue

        text = str(item[1]).strip()

        if not text:
            continue

        try:
            confidence = float(item[2])
        except (TypeError, ValueError):
            confidence = 0.0

        extracted.append((text, confidence))

    return extracted


def _run_reader(
    image_array: np.ndarray,
    language: str,
) -> list[tuple[str, float]]:
    """
    Run one EasyOCR language model.

    Args:
        image_array:
            RGB NumPy image.
        language:
            Reader language group.

    Returns:
        Extracted text/confidence pairs.
    """

    reader = _get_reader(language)

    try:
        result = reader.readtext(
            image_array,
            detail=1,
        )
    except Exception as exc:
        raise OCRExtractionError(
            "OCR processing failed."
        ) from exc

    return _extract_results(result)


def _contains_bengali(text: str) -> bool:
    """Return True when Bengali Unicode characters are present."""

    return any(
        "\u0980" <= character <= "\u09ff"
        for character in text
    )


def _contains_devanagari(text: str) -> bool:
    """Return True when Devanagari Unicode characters are present."""

    return any(
        "\u0900" <= character <= "\u097f"
        for character in text
    )


def _latin_result_is_strong(
    results: list[tuple[str, float]],
) -> bool:
    """
    Decide whether the English OCR result is strong enough to use.

    This is useful for English, Banglish, and Hinglish screenshots,
    where loading an Indian-script recognition model is unnecessary.
    """

    if not results:
        return False

    text = " ".join(item[0] for item in results).strip()

    if len(text) < 8:
        return False

    average_confidence = sum(
        confidence for _, confidence in results
    ) / len(results)

    return average_confidence >= 0.45


def _score_script_result(
    results: list[tuple[str, float]],
    script: str,
) -> float:
    """
    Score a Bengali/Hindi OCR result.

    The score favors:
    - longer extracted text,
    - higher OCR confidence,
    - presence of the expected native script.

    This is only used to choose between OCR recognition models.
    It does not determine fraud risk.
    """

    if not results:
        return 0.0

    text = " ".join(item[0] for item in results).strip()

    if not text:
        return 0.0

    average_confidence = sum(
        confidence for _, confidence in results
    ) / len(results)

    if script == "bn":
        has_native_script = _contains_bengali(text)
    else:
        has_native_script = _contains_devanagari(text)

    native_bonus = 1.0 if has_native_script else 0.0

    # Keep the length contribution bounded so a very long but poor
    # OCR result cannot dominate confidence completely.
    length_score = min(len(text) / 200.0, 1.0)

    return (
        average_confidence * 2.0
        + length_score
        + native_bonus * 2.0
    )


def _select_script_result(
    bengali_results: list[tuple[str, float]],
    hindi_results: list[tuple[str, float]],
) -> list[tuple[str, float]]:
    """
    Select the stronger result between Bengali and Hindi models.
    """

    bengali_score = _score_script_result(
        bengali_results,
        "bn",
    )

    hindi_score = _score_script_result(
        hindi_results,
        "hi",
    )

    if bengali_score == 0.0 and hindi_score == 0.0:
        return []

    if bengali_score >= hindi_score:
        return bengali_results

    return hindi_results


def extract_text_from_image(image_bytes: bytes) -> str:
    """
    Extract multilingual text from image bytes.

    The function first uses the English model because it is the most
    appropriate model for English, Banglish, and Hinglish.

    If the English result contains Bengali or Devanagari text, that
    result is retained. Otherwise, Bengali and Hindi recognition
    models are evaluated to detect native-script screenshots.

    Args:
        image_bytes:
            Raw image bytes.

    Returns:
        Extracted text as a single whitespace-separated string.

    Raises:
        OCRExtractionError:
            If the image is invalid or OCR processing fails.
    """

    image_array = _prepare_image(image_bytes)

    # First pass: English model.
    #
    # This handles:
    # - English
    # - Banglish
    # - Hinglish
    # - English-heavy mixed screenshots
    english_results = _run_reader(
        image_array,
        "en",
    )

    english_text = " ".join(
        text for text, _ in english_results
    ).strip()

    # If native Bengali or Devanagari characters somehow appear in
    # the first result, preserve that result rather than performing
    # additional OCR passes.
    if _contains_bengali(english_text):
        return english_text

    if _contains_devanagari(english_text):
        return english_text

    # Strong Latin-script OCR is sufficient for English/Banglish/
    # Hinglish. This avoids loading additional models unnecessarily.
    if _latin_result_is_strong(english_results):
        return english_text

    # Weak/empty Latin OCR means the image may contain Bengali or
    # Hindi native script. Evaluate both supported Indian-script
    # models and select the stronger result.
    bengali_results = _run_reader(
        image_array,
        "bn",
    )

    hindi_results = _run_reader(
        image_array,
        "hi",
    )

    selected_results = _select_script_result(
        bengali_results,
        hindi_results,
    )

    if selected_results:
        return " ".join(
            text for text, _ in selected_results
        ).strip()

    # If the script-specific models found nothing, return whatever
    # the English model found instead of silently discarding OCR.
    return english_text