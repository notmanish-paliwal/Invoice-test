import os
from groq import Groq


def extract_invoice_data(text: str) -> dict:
    """
    Sends OCR text to Groq and extracts structured invoice data.
    """

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set")

    client = Groq(api_key=api_key)

    prompt = f"""
    Extract the following fields from the invoice text and return ONLY valid JSON.

    Fields:
    - invoice_number
    - invoice_date
    - vendor_name
    - total_amount

    Invoice Text:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You extract structured invoice data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content