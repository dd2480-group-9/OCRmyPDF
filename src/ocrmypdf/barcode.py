from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import letter

def create_pdf_with_barcode(output_filename, barcode_data):
    c = canvas.Canvas(output_filename, pagesize=letter)
    
    # Generate barcode
    barcode = code128.Code128(barcode_data, barWidth=0.5, barHeight=50)
    
    # Draw barcode on PDF
    barcode.drawOn(c, 100, 500)  # (x, y) position
    
    c.drawString(100, 480, f"Barcode: {barcode_data}")  # Label under barcode
    
    c.save()

# Usage
create_pdf_with_barcode("barcode.pdf", "123456789")
