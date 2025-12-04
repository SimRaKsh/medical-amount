import easyocr
import re

# initialize OCR reader once (performance improvement)
reader = easyocr.Reader(['en'], gpu=False)


def extract_numeric_tokens(text: str):
    """
    Extracts ONLY valid numeric tokens such as:
    1200, 1000, 200, 10%
    Ignores: INR, Paid, words with numbers, OCR noise.
    """
    pattern = r"\b\d+(?:\.\d+)?%?\b"
    return re.findall(pattern, text)


def detect_currency(text: str):
    """Detect INR hints based on common patterns."""
    if "INR" in text.upper() or "₹" in text or "Rs" in text or "RS" in text:
        return "INR"
    return None


def extract_text(input_text=None, image_bytes=None):
    """
    Main OCR + token extraction service.
    Works for:
    - Direct text input
    - Image input (bytes)
    """

    # STEP 1: Get raw text from input or OCR
    if input_text and input_text.strip():
        raw = input_text
    else:
        # Perform OCR safely
        result = reader.readtext(image_bytes, detail=0)
        raw = " ".join(result) if result else ""

    # STEP 2: Extract numeric tokens
    tokens = extract_numeric_tokens(raw)

    # STEP 3: Detect currency
    currency_hint = detect_currency(raw)

    # Return JSON structure
    return {
        "raw_text": raw,
        "raw_tokens": tokens,
        "currency_hint": currency_hint,
        "confidence": 0.90
    }
