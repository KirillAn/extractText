import ebooklib
import re
from ebooklib import epub
from bs4 import BeautifulSoup
from docx import Document
import pdfplumber
import pytesseract
from PIL import Image
import io
from PyPDF2 import PdfReader
from pdf2image import convert_from_path


def clean_text(text):
    return re.sub('<.*?>|\xa0+|\s+|\{\'.*?\.xhtml\'\}|\'.*?\.xhtml\'', ' ', text).strip()

def extract_texts_from_epub(file_name):
    book = epub.read_epub(file_name)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    def chapter_to_str(chapter):
        soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
        text = [para.get_text() for para in soup.find_all('p')]
        return clean_text(' '.join(text))
    texts = {}
    for item in items:
        texts[item.get_name()] = chapter_to_str(item)
    return texts

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return clean_text(file.read())

def read_docx_file(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return clean_text('\n'.join(full_text))

def crop_image(page, image_bbox, output_path='cropped_image.pdf'):
    x0, top, x1, bottom = image_bbox
    crop_bbox = (x0, top, x1, bottom)
    
    with pdfplumber.open(page.stream) as pdf:
        cropped_page = pdf.pages[0].crop(bbox=crop_bbox)
        with open(output_path, 'wb') as cropped_pdf_file:
            cropped_page.to_pdf(cropped_pdf_file)

def convert_to_images(input_path):
    images = convert_from_path(input_path)
    output_file = "PDF_image.png"
    images[0].save(output_file, "PNG")
    return output_file

def image_to_text(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

def extract_table(pdf, page_num, table_num):
    page = pdf.pages[page_num]
    table = page.extract_tables()[table_num]
    return table

def table_converter(table):
    table_string = ''
    for row in table:
        cleaned_row = [cell.replace('\n', ' ') if cell is not None else '' for cell in row]
        table_string += ' | '.join(cleaned_row) + '\n'
    return table_string.strip()

def process_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text_per_page = {}
        for pagenum, page in enumerate(pdf.pages):
            text_content = page.extract_text() or ""
            images = page.images
            for image in images:
                image_bbox = image.get("bbox")
                if image_bbox:
                    # Assuming a single image per page for simplicity
                    cropped_image_path = f'cropped_page_{pagenum}.pdf'
                    crop_image(page, image_bbox, cropped_image_path)
                    image_path = convert_to_images(cropped_image_path)
                    text_content += "\n" + image_to_text(image_path)
            tables = page.extract_tables()
            for table_num, table in enumerate(tables):
                table_content = extract_table(pdf, pagenum, table_num)
                text_content += "\n" + table_converter(table_content)
            text_per_page[pagenum] = text_content
    return text_per_page

def extract_text(file_path):
    """
    Extract text from a file based on its extension.
    """
    if file_path.endswith('.epub'):
        return extract_texts_from_epub(file_path)
    elif file_path.endswith('.pdf'):
        return process_pdf(file_path)  
    elif file_path.endswith('.txt'):
        return read_text_file(file_path)
    elif file_path.endswith('.docx'):
        return read_docx_file(file_path)
    else:
        raise ValueError("Unsupported file type.")

__all__ = ['extract_text']

