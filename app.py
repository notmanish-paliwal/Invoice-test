from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import tempfile
import pandas as pd
from ocr import extract_text_from_pdf
from extractor import extract_invoice_fields

st.set_page_config(page_title="Invoice OCR", layout="wide")

st.title("Invoice Data Extractor")

uploaded_files = st.file_uploader(
    "Upload up to 5 invoice PDFs",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    if len(uploaded_files) > 5:
        st.error("You can upload only 5 PDFs")
    else:
        results = []

        with st.spinner("Processing invoices..."):
            for file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(file.read())
                    text = extract_text_from_pdf(tmp.name)
                    data = extract_invoice_fields(text)
                    results.append(data)

        df = pd.DataFrame(results)

        st.subheader("Extracted Invoice Data")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download CSV",
            csv,
            "invoice_data.csv",
            "text/csv"
        )