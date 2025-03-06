import os
import pytest
from pypdf import PdfReader
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from ocrmypdf.addbarcode import append_barcode_to_pdf, create_pdf_with_barcode, generate_barcode, generate_barcode_number

TEST_PDF = "test_barcode.pdf"
TEST_ORIGINAL_PDF = "test_original.pdf"
TEST_BARCODE_PDF = "test_barcode.pdf"
TEST_OUTPUT_PDF = "test_output.pdf"


def test_generate_barcode_number():
    barcode_number = generate_barcode_number()
    assert isinstance(barcode_number, str), "Barcode number should be a string"
    assert len(barcode_number) == 6, "Barcode number should be 6 digits"
    assert barcode_number.isdigit(), "Barcode number should contain only digits"

def test_generate_barcode():
    barcode_data = generate_barcode_number()
    barcode_path = generate_barcode(barcode_data)
    assert os.path.exists(barcode_path + ".png"), "Barcode image was not created"
    
    with Image.open(barcode_path + ".png") as img:
        assert img.format == "PNG", "Generated barcode image is not PNG format"

    os.remove(barcode_path + ".png")  


def test_create_pdf_with_barcode():
    barcode_data = generate_barcode_number()
    barcode_path = generate_barcode(barcode_data)
    create_pdf_with_barcode(TEST_PDF, barcode_path, barcode_data)
    assert os.path.exists(TEST_PDF), "PDF was not created"

    reader = PdfReader(TEST_PDF)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text() or ""

    assert barcode_data in extracted_text, "Barcode not in PDF"

    os.remove(barcode_path + ".png")
    os.remove(TEST_PDF)


def test_append_barcode_to_pdf():
    
    c = canvas.Canvas(TEST_ORIGINAL_PDF, pagesize=letter)
    c.drawString(100, 700, "This is a test PDF with original content.")
    c.showPage()
    c.save()

    barcode_data = generate_barcode_number()
    barcode_path = generate_barcode(barcode_data)
    create_pdf_with_barcode(TEST_BARCODE_PDF, barcode_path, barcode_data)

    append_barcode_to_pdf(TEST_ORIGINAL_PDF, TEST_BARCODE_PDF, TEST_OUTPUT_PDF)
    
    assert os.path.exists(TEST_OUTPUT_PDF), "Output PDF was not created."

    original_reader = PdfReader(TEST_ORIGINAL_PDF)
    output_reader = PdfReader(TEST_OUTPUT_PDF)

    assert len(output_reader.pages) == len(original_reader.pages) + 1, "Barcode page was not appended correctly."

    original_text = original_reader.pages[0].extract_text()
    output_text = output_reader.pages[0].extract_text()
    
    assert original_text == output_text, "Original PDF content in 1st page was modified."

    last_page_text = output_reader.pages[-1].extract_text() or ""
    assert barcode_data in last_page_text, "Barcode page was not found at the last position"

    for page_num in range(len(output_reader.pages) - 1):
        page_text = output_reader.pages[page_num].extract_text() or ""
        assert barcode_data not in page_text, "Barcode should only be on the last page"

    os.remove(barcode_path + ".png")
    os.remove(TEST_ORIGINAL_PDF)
    os.remove(TEST_BARCODE_PDF)
    os.remove(TEST_OUTPUT_PDF)
