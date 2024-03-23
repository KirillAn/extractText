import json
import ebooklib
from PyPDF2 import PdfReader
from ebooklib import epub
from bs4 import BeautifulSoup
from docx import Document

def extract_texts_from_epub(file_name):
    book = epub.read_epub(file_name)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    def chapter_to_str(chapter):
        soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
        text = [para.get_text() for para in soup.find_all('p')]
        return ' '.join(text)

    texts = {}
    for item in items:
        texts[item.get_name()] = chapter_to_str(item)

    return texts

def read_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() or ''
    return text

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
        
def read_docx_file(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def extract_text(file_path):
    if file_path.endswith('.epub'):
        return extract_texts_from_epub(file_path)
    elif file_path.endswith('.pdf'):
        return read_text_from_pdf(file_path)
    elif file_path.endswith('.txt'):
        return read_text_file(file_path)
    elif file_path.endswith('.json'):
        return read_json_file(file_path)
    elif file_path.endswith('.docx'):
        return read_docx_file(file_path)
    else:
        raise ValueError("Unsupported file type.")


