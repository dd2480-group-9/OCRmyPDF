import os
import pytest
from pypdf import PdfReader
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from ocrmypdf.addbarcode_pdf import create_pdf_with_barcode, generate_barcode, generate_barcode_number
from ocrmypdf.addbarcode import append_barcode_to_pdf

# Define test file names
TEST_PDF = "test_barcode.pdf"
TEST_ORIGINAL_PDF = "test_original.pdf"
TEST_BARCODE_PDF = "test_barcode.pdf"
TEST_OUTPUT_PDF = "test_output.pdf"


def test_generate_barcode_number():
    """Test that barcode number is a 6-digit string containing only digits."""
    barcode_number = generate_barcode_number()
    assert isinstance(barcode_number, str), "Barcode number should be a string"
    assert len(barcode_number) == 6, "Barcode number should be 6 digits"
    assert barcode_number.isdigit(), "Barcode number should contain only digits"


def test_generate_barcode():
    """Test that barcode PNG is created successfully."""
    barcode_data = generate_barcode_number()
    barcode_path = generate_barcode(barcode_data)
    
    assert os.path.exists(barcode_path + ".png"), "Barcode image was not created"
    
    # Check if the file is a PNG image
    with Image.open(barcode_path + ".png") as img:
        assert img.format == "PNG", "Generated barcode image is not in PNG format"

    # Cleaning
    os.remove(barcode_path + ".png")


def test_create_pdf_with_barcode():
    """Test that a PDF containing the barcode is created and if the barcode data is in it."""
    barcode_data = generate_barcode_number()
    barcode_path = generate_barcode(barcode_data)
    create_pdf_with_barcode(barcode_path, barcode_data)
    
    assert os.path.exists("barcode.pdf"), "Barcode PDF was not created"

    reader = PdfReader("barcode.pdf")
    extracted_text = "".join([page.extract_text() or "" for page in reader.pages])

    assert barcode_data in extracted_text, "Barcode number not found in PDF"

    # Cleaning
    os.remove(barcode_path + ".png")
    os.remove("barcode.pdf")


def test_append_barcode_to_pdf():
    """Test that the barcode PDF is appended as the last page to the original PDF."""
    
    # Generates a dummy pdf
    c = canvas.Canvas(TEST_ORIGINAL_PDF, pagesize=letter)
    c.drawString(100, 700, "This is a test PDF with original content.")
    c.showPage()
    c.save()

    # Generate the barcode PDF
    barcode_data = generate_barcode_number()
    barcode_path = generate_barcode(barcode_data)
    create_pdf_with_barcode(barcode_path, barcode_data)
    append_barcode_to_pdf(TEST_ORIGINAL_PDF, "barcode.pdf", TEST_OUTPUT_PDF)
    
    # Ensures the output file exists
    assert os.path.exists(TEST_OUTPUT_PDF), "Output PDF was not created."

    original_reader = PdfReader(TEST_ORIGINAL_PDF)
    output_reader = PdfReader(TEST_OUTPUT_PDF)

     # Ensures the number of pages is correct
    assert len(output_reader.pages) == len(original_reader.pages) + 1, "Barcode page was not appended correctly."

    # Ensure the first page content is unchanged
    original_text = original_reader.pages[0].extract_text()
    output_text = output_reader.pages[0].extract_text()
    assert original_text == output_text, "Original PDF content was modified."

    # Ensures that barcode is in the last page
    last_page_text = output_reader.pages[-1].extract_text() or ""
    assert barcode_data in last_page_text, "Barcode page was not found at the last position"

    # Ensures that there is no barcode in other pages before last page
    for page_num in range(len(output_reader.pages) - 1):
        page_text = output_reader.pages[page_num].extract_text() or ""
        assert barcode_data not in page_text, "Barcode should only be on the last page"

    # Cleaning
    os.remove(barcode_path + ".png")
    os.remove(TEST_ORIGINAL_PDF)
    os.remove("barcode.pdf")
    os.remove(TEST_OUTPUT_PDF)
