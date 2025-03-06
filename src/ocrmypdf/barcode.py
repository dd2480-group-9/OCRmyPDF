from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import letter
import random

def create_pdf_with_barcode(output_filename, barcode_data):
    c = canvas.Canvas(output_filename, pagesize=letter)

    #Generate Random number for barcode 
    
    # Generate barcode
    barcode = code128.Code128(barcode_data, barWidth=0.5, barHeight=50)
    
    # Add barcode to last page on PDF
    barcode.drawOn(c, 100, 500)  # (x, y) position
    
    c.drawString(100, 480, f"Barcode: {barcode_data}")  # Label under barcode
    
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
