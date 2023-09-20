import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Path to the scanned PDF file
pdf_file_path = "scanned_pdf.pdf"

# Path where you want to save the extracted text file
output_text_file = "extracted_text.txt"

# Convert the scanned PDF to images
images = convert_from_path(pdf_file_path)

# Initialize an empty string to store the extracted text
extracted_text = ""

# Process each page as an image
for page_number, image in enumerate(images, 1):
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    # Append the extracted text to the result
    extracted_text += f"Page {page_number}:\n{text}\n"

# Save the extracted text to a file
with open(output_text_file, "w", encoding="utf-8") as text_file:
    text_file.write(extracted_text)

print("Text extraction completed. Extracted text saved to:", output_text_file)
