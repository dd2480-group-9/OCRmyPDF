import os
from PyPDF2 import PdfReader
from src import create_pdf_with_barcode

def test_create_pdf_with_barcode():
    '''This is a test to see that the create_pdf_with_barcode creates a barcode label on the pdf.'''
   
    test_filename = "test_barcode.pdf"
    barcode_data = "123456789"
    
    create_pdf_with_barcode(test_filename, barcode_data)

    # assert os.path.exists(test_filename), "PDF not created with create_pdf_with_barcode"

    with open(test_filename, "rb") as file:
        reader = PdfReader(file)

        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            assert barcode_data in text, "Barcode not found in PDF"
    
    os.remove(test_filename) # Cleanup after test 

