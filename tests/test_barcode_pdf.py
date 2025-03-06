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



