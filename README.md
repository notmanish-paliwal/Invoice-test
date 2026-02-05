# Invoice-test
📄 Invoice Data Extraction Web Application

Project Description

This project is a full-stack invoice data extraction web application that automates the process of reading invoice PDFs and converting unstructured text into structured, machine-readable data. It uses Optical Character Recognition (OCR) and a Large Language Model to extract key invoice fields accurately and present them in a user-friendly interface.

Users can upload multiple invoice PDFs, view extracted data in a tabular format, and download the results as a CSV file for further processing or analysis.

The application is designed to be simple, scalable, and suitable for real-world business use cases such as accounting automation, finance operations, and document processing workflows.

Key Features
	•	Upload up to five invoice PDF files at a time
	•	Extracts invoice text using OCR
	•	Converts unstructured text into structured data using LLM-based extraction
	•	Displays extracted results in a clean tabular format
	•	Allows users to download extracted data as a CSV file
	•	Fully built using Python, including the frontend
	•	Modular and extensible backend architecture

Extracted Invoice Fields

The system extracts the following fields from each invoice:
	•	Invoice Number
	•	Invoice Date
	•	Vendor / Supplier Name
	•	Total Amount
	•	Tax Amount
	•	Currency
	•	Source File Name

These fields can be easily extended based on business requirements.

Technology Stack

Frontend
	•	Streamlit (Python-based web UI)

Backend
	•	Python
	•	Tesseract OCR for text extraction
	•	Groq Large Language Model for structured data extraction

Data Handling
	•	Pandas for tabular data processing
	•	CSV export functionality


System Architecture
	1.	User uploads PDF invoices through the web interface.
	2.	PDF files are converted into images.
	3.	OCR is applied to extract raw text from invoice images.
	4.	The extracted text is sent to the LLM for structured data extraction.
	5.	The structured data is collected and displayed in a table.
	6.	Users can download the final data as a CSV file.

Installation and Setup
	1.	Ensure Python is installed on the system.
	2.	Install required dependencies: pip install -r requirements.txt
    3.	Start the application: streamlit run app.py

Usage Instructions
	1.	Open the web application in a browser.
	2.	Upload up to five invoice PDF files.
	3.	Click on Process Invoices.
	4.	View extracted invoice data in the table.
	5.	Download the extracted data using the Download CSV button.

Assumptions and Limitations
	•	OCR accuracy depends on the quality of the invoice PDF.
	•	Scanned or low-resolution invoices may produce partial results.
	•	The application currently supports a fixed set of invoice fields.
	•	Batch uploads are limited to five files per request to ensure performance.


Future Enhancements
	•	Support for bulk invoice processing (large folders)
	•	Field-level confidence scoring
	•	Invoice validation and duplicate detection
	•	Support for regional tax structures (e.g., GST breakdown)
	•	Role-based access and authentication
	•	API-based access for enterprise integration

Intended Use

This project is suitable for:
	•	Finance and accounting automation
	•	Invoice digitization workflows
	•	Proof-of-concepts for OCR + AI document processing
	•	Small to medium business invoice management systems
	
Usage Instructions
	1.	Open the web application in a browser.
	2.	Upload up to five invoice PDF files.
	3.	Click on Process Invoices.
	4.	View extracted invoice data in the table.
	5.	Download the extracted data using the Download CSV button.


Assumptions and Limitations
	•	OCR accuracy depends on the quality of the invoice PDF.
	•	Scanned or low-resolution invoices may produce partial results.
	•	The application currently supports a fixed set of invoice fields.
	•	Batch uploads are limited to five files per request to ensure performance.

Future Enhancements
	•	Support for bulk invoice processing (large folders)
	•	Field-level confidence scoring
	•	Invoice validation and duplicate detection
	•	Support for regional tax structures (e.g., GST breakdown)
	•	Role-based access and authentication
	•	API-based access for enterprise integration

Intended Use

This project is suitable for:
	•	Finance and accounting automation
	•	Invoice digitization workflows
	•	Proof-of-concepts for OCR + AI document processing
	•	Small to medium business invoice management systems
