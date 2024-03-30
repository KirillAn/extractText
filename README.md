# extractText


A simple tool for extracting text from PDF, EPUB, TXT, and DOCX files. This library was primarily developed for personal use in various NLP-related projects.

## Parsers used:

pdfplumber, pytesseract, PyPDF2, pdf2image and PIL for **PDF** processing

ebooklib, bs4 for **EPUB**

docx for **DOCX**






## Installation

Install `text-extra` using pip:

```sh
pip install text-extra
```
## Usage
```py
from text_extractor import extract_text

extracted_text = extract_text(file_path)
if isinstance(extracted_text, dict):
    for key, value in extracted_text.items():
        print(f"--- {key} ---\n{value}\n")
else:
    print(extracted_text)
