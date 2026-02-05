import json
import re
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_invoice_fields(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Return ONLY valid JSON. No explanation."
            },
            {
                "role": "user",
                "content": f"""
Extract invoice fields and return JSON ONLY in this format:

{{
  "invoice_number": "",
  "invoice_date": "",
  "vendor_name": "",
  "total_amount": "",
  "tax_amount": ""
}}

Text:
{text}
"""
            }
        ],
        temperature=0
    )

    raw = response.choices[0].message.content
    print("RAW LLM OUTPUT:", raw)

    if raw is None or raw.strip() == "":
        return {
            "invoice_number": "",
            "invoice_date": "",
            "vendor_name": "",
            "total_amount": "",
            "tax_amount": ""
        }

    raw = re.sub(r"```json|```", "", raw).strip()

    try:
        return json.loads(raw)
    except Exception:
        return {
            "invoice_number": "",
            "invoice_date": "",
            "vendor_name": "",
            "total_amount": "",
            "tax_amount": ""
        }