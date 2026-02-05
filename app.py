import streamlit as st
import pandas as pd

st.set_page_config(page_title="Invoice Extractor", layout="wide")

st.title("Invoice Data Extractor")

st.write("Upload up to 5 invoice PDFs")

files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if files:
    data = []
    for f in files[:5]:
        data.append({
            "File Name": f.name,
            "Invoice Number": "INV-001",
            "Vendor": "Sample Vendor",
            "Amount": "1000"
        })

    df = pd.DataFrame(data)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="invoices.csv",
        mime="text/csv"
    )