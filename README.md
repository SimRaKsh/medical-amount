# AI-powered backend service to extract, normalize, and classify financial amounts from medical bills or receipts
- A backend project Assignment, featuring OCR, digit correction, contextual classification, guardrails and clean structured JSON output.
## Features
- OCR using EasyOCR
- Handles noisy inputs (O → 0, I → 1, l → 1 corrections)
- Extracts numeric tokens and percentages
- Classifies amounts into categories (total, paid, due, discount)
- Returns provenance for each predicted value
- Guardrails for noisy documents
- Works for both text & scanned images
## Setup Instructions
- Clone the project:
```
git clone https://github.com/SimRaKsh/medical-amount.git
cd medical-amount
```
- Create & activate virtual environment (Windows):
```
python -m venv venv
venv\Scripts\activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Run the server:
```
uvicorn app.main:app --reload --port 8000
```
- Visit Swagger
```
http://127.0.0.1:8000/docs
```
- Ngrok (for public demo):
```
ngrok config add-authtoken
ngrok http 8000
```
## Architecture
medical-amount/
medical-amount/
│
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── routers/extract.py    # /extract API route
│   ├── services/
│   │   ├── ocr_service.py    # OCR + raw token extraction
│   │   ├── normalize_service.py   # Numeric cleaning + digit correction
│   │   └── classify_service.py    # total/paid/due classification
│   └── models/schemas.py     # Pydantic models
│
├── sample_inputs/            # Sample images and text
├── requirements.txt
└── README.md

## API Usage
POST /api/extract
Text Example Request:
{
"text": "Total: INR 1200 | Paid: 1000 | Due: 200 | Discount: 10%"
}
Text Example Response:
{
"currency": "INR",
"amounts":[
{"type":"total_bill","value":1200},
{"type":"paid","value":1000},
{"type":"due","value":200}
],
"status":"ok"
}
Guardrail Response:
{"status":"no_amounts_found","reason":"document too noisy"}
