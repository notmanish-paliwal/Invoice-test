import streamlit as st
import pandas as pd
import pdfplumber
import pytesseract
from PIL import Image
import json

from extractor import extract_invoice_data


st.set_page_config(page_title="Invoice OCR", layout="wide")
st.title("Invoice Data Extractor")

uploaded_files = st.file_uploader(
    "Upload up to 5 invoice PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


results = []

if uploaded_files:
    if len(uploaded_files) > 5:
        st.error("You can upload a maximum of 5 PDFs only.")
    else:
        st.success(f"{len(uploaded_files)} file(s) uploaded")

        if st.button("Process Invoices"):
            with st.spinner("Extracting invoice data..."):
                for file in uploaded_files:
                    try:
                        raw_text = extract_text_from_pdf(file)
                        groq_output = extract_invoice_data(raw_text)

                        data = json.loads(groq_output)
                        data["file_name"] = file.name
                        results.append(data)

                    except Exception as e:
                        st.error(f"Error processing {file.name}: {e}")

if results:
    df = pd.DataFrame(results)
    st.subheader("Extracted Invoice Data")
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="invoice_data.csv",
        mime="text/csv"
    )