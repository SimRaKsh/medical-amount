from fastapi import APIRouter, UploadFile, File, Form
from app.services.ocr_service import extract_text
from app.services.normalize_service import normalize_amounts
from app.services.classify_service import classify_amounts
import base64

router = APIRouter()

@router.post("/extract")
async def extract_endpoint(text: str = None, image_base64: str = None):
    if not text and not image_base64:
        return {"status":"no_input","reason":"Provide image or text"}

    image_bytes = None
    if image_base64:
        image_bytes = base64.b64decode(image_base64)

    # Step 1 - OCR
    ocr = extract_text(input_text=text, image_bytes=image_bytes)
    tokens = ocr["raw_tokens"]

    if len(tokens) == 0:
        return {"status":"no_amounts_found","reason":"document too noisy"}

    # Step 2 - Normalize
    normalized = normalize_amounts(tokens)
    amounts = normalized["normalized_amounts"]

    # Step 3 - Classify
    classified = classify_amounts(ocr["raw_text"], amounts)

    # Step 4 - Final Output
    final = {
    "currency": ocr["currency_hint"] or "INR",
    "amounts": [
        {
            "type": a["type"],
            "value": a["value"],
            "source": f"text: '{ocr['raw_text']}'"
        }
        for a in classified["amounts"]
    ],
    "status": "ok"
}

    return final
