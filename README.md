# extractText


A simple tool for extracting text from PDF, EPUB, TXT, and DOCX files. This library was primarily developed for personal use in various NLP-related projects.


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
