from barcode import Code128
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import random

def create_pdf_with_barcode(barcode_path, barcode_data):
    """
    Function that generates a pdf and adds a png
    
    param: 
     barcode_path : string that contains path of the barcode png 
     barcode_data : string of barcode numbers

    returns: c an instance of the canvas 

    """
    filename = "barcode.pdf"
    c = canvas.Canvas(filename, pagesize=letter)   # creates a canvas instance 
    c.drawImage(f"{barcode_path}.png", 100, 500, width=400, height=200) # Creates image on pdf
    c.drawString(100, 480, f"Barcode: {barcode_data}")  # Additional text alongside png on pdf
    c.save()   # saves all edits to given path in drawImage 
    return c

def generate_barcode(barcode_data):
   """
   Function that generates a png of a barcode and saves it as barcode.png in current directory
   param:
    barcode_data : string of barcode numbers
   return: 
    barcode_path: string containing path of where png has been saved 
   """
   current_directory = os.getcwd()  # Gets current directory path
   barcode_filename = "barcode"     # Filename of png being created 
   
   barcode_path = os.path.join(current_directory, barcode_filename)  # joining path and name 
   
   barcode = Code128(barcode_data, writer=ImageWriter()) # Creates barcode 
   
   barcode.save(barcode_path) # Saves the barcode to path (adding .png)  
   
   return barcode_path

def generate_barcode_number():
    """
    This function generates a random 6 digit number to use for creating a barcode. 
    Param : None 
    Returns : string : barcode numbers in the form of a string 
    """

    barcode_number = random.randint(0, 999999)  # Generate a number between 0 and 999999
    barcode_data = f"{barcode_number:06d}"  # Format it as a 6-digit string with leading zeros
    return barcode_data

if __name__ == "__main__":
    # Example of usage
    """
    Example of usage: 
        This should generate a file named barcode.png containing 6 random numbers
        This should also generate a file named hejdå.pdf with that barcode and an additional text with the barcode number
    """
    numbers = generate_barcode_number()
    path = generate_barcode(numbers)
    output = "hejdå.pdf"
    create_pdf_with_barcode(path, numbers)