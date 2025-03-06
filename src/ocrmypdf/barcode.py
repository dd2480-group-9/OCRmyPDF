from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import letter
import random


def create_pdf_with_barcode(output_filename, barcode_path, barcode_data):

    if not output_filename.lower().endswith(".pdf"):
        output_filename += ".pdf"  
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.drawImage(f"{barcode_path}.png", 100, 500, width=400, height=200)
    c.drawString(100, 480, f"Barcode: {barcode_data}")
    c.save()


def generate_barcode_number():
    """
    This function generates a random 6 digit number to use for creating a barcode. 
    Param : None 
    Returns : string : barcode numbers in the form of a string 
    """

    barcode_number = random.randint(0, 999999)  # Generate a number between 0 and 999999
    barcode_data = f"{barcode_number:06d}"  # Format it as a 6-digit string with leading zeros
    return barcode_data

# Usage
create_pdf_with_barcode("barcode.pdf", "123456789")
