from PIL import Image
from pytesseract import pytesseract
from numpy import array

# Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Define path to image
path_to_image = 'sample_matrix.JPG'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open image with PIL
img = Image.open(path_to_image)

arr = array(img)

# Extract text from image
text = pytesseract.image_to_string(img)

print(text)
print("ARRAY")
print(arr)
