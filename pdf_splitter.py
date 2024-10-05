import os
import math
import fitz  # PyMuPDF
from PIL import Image
import io

def split_pdf_to_a0_tiles(input_pdf, output_directory):
    # A0 size in points (1 point = 1/72 inch)
    a0_width, a0_height = 3370.39, 4767.87

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Open the PDF file
    doc = fitz.open(input_pdf)
    
    # Assuming the map is on the first page
    page = doc[0]
    
    # Get the size of the PDF page
    pdf_width = page.rect.width
    pdf_height = page.rect.height
    
    # Calculate the number of tiles needed
    tiles_x = math.ceil(pdf_width / a0_width)
    tiles_y = math.ceil(pdf_height / a0_height)
    
    # Create tiles
    for i in range(tiles_x):
        for j in range(tiles_y):
            # Calculate the crop box for this tile
            left = i * a0_width
            bottom = pdf_height - (j + 1) * a0_height
            right = min((i + 1) * a0_width, pdf_width)
            top = pdf_height - j * a0_height
            
            # Create a rectangle for cropping
            rect = fitz.Rect(left, bottom, right, top)
            
            # Get the cropped pixmap
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
            
            # Convert pixmap to PIL Image
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            
            # Save as PNG
            output_filename = os.path.join(output_directory, f'tile_{i}_{j}.png')
            img.save(output_filename, 'PNG')
            
            print(f'Saved tile {i}_{j}')
    
    # Close the document
    doc.close()

# Usage
input_pdf = 'path/to/your/large_map.pdf'
output_directory = 'path/to/output/tiles'
split_pdf_to_a0_tiles(input_pdf, output_directory)
