import re

def classify_amounts(text, amounts):
    text_lower = text.lower()

    # Split text by '|'
    segments = re.split(r"\s*\|\s*", text_lower)

    results = []

    for amt in amounts:
        amt_str = str(amt)
        label = "unknown"

        for segment in segments:

            # MATCH FULL NUMBER ONLY, not substring
            if re.search(rf"\b{amt_str}\b", segment):

                if "total" in segment:
                    label = "total_bill"
                elif "paid" in segment:
                    label = "paid"
                elif "due" in segment:
                    label = "due"
                elif "discount" in segment:
                    label = "discount"

                break  # Stop scanning segments

        results.append({
            "type": label,
            "value": amt
        })

    return {
        "amounts": results,
        "confidence": 0.95
    }
