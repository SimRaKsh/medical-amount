def normalize_token(t):
    # Fix common OCR errors: O→0, I→1, l→1
    corrected = (
        t.replace("O", "0").replace("o", "0")
         .replace("I", "1").replace("l", "1")
    )

    # Convert percentages skip
    if "%" in corrected:
        return None

    try:
        return int(corrected)
    except:
        return None

def normalize_amounts(tokens):
    cleaned = []

    for t in tokens:
        if "%" in t:
            continue  # skip discount %
        cleaned.append(int(t))

    return {
        "normalized_amounts": cleaned,
        "normalization_confidence": 0.9
    }
