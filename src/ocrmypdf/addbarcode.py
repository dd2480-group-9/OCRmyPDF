from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

def create_barcode_pdf(barcode_image, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    c.drawImage(barcode_image, x=100, y=height-200, width=200, height=100)
    c.showPage()
    c.save()

def append_barcode_to_pdf(original_pdf, barcode_pdf, output_pdf):
    original_reader = PdfReader(original_pdf)
    barcode_reader = PdfReader(barcode_pdf)
    writer = PdfWriter()
    
    for page in original_reader.pages:
        writer.add_page(page)
    
    writer.add_page(barcode_reader.pages[0])
    
    with open(output_pdf, 'wb') as f:
        writer.write(f)

# Example usage
if __name__ == "__main__":
    create_barcode_pdf('barcode_123456.png', 'barcode_page.pdf')
    append_barcode_to_pdf('original_document.pdf', 'barcode_page.pdf', 'final_document_with_barcode.pdf') 
