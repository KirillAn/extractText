# extractText


A simple tool for text extraction from pdf, epub, txt, and docx files. I wrote this lib mostly for personal use while working on several NLP related projects

## Installation

Install `text-extra` using pip:

```sh
pip install text-extra
```
## Usage
```py
from text_extractor import extract_text

file_path = "path/to/your/file.pdf"
extracted_text = extract_text(file_path)
print(extracted_text)
