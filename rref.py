from PIL import Image
from pytesseract import pytesseract
from sympy import *

# Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Define path to image
path_to_image = 'images/sample_matrix.JPG'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(img)

print(text)

# Split the text into rows and columns
rows = text.split('\n')
matrix = [row.split() for row in rows]

# Convert the strings in the matrix to integers
matrix = [[int(cell) for cell in row] for row in matrix]


# Print the matrix
print(matrix)

# RREF CALC
M = Matrix(matrix)
print("Matrix : {} ".format(M))

# Use sympy.rref() method
M_rref = M.rref()

print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))

# import pytesseract
# from PIL import Image

# # path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# # Define path to tessaract.exe
# path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# # Define path to image
# path_to_image = 'images/sample_matrix.JPG'

# # Point tessaract_cmd to tessaract.exe
# pytesseract.tesseract_cmd = path_to_tesseract

# # Open image with PIL
# img = Image.open(path_to_image)

# # Extract text from image
# text = pytesseract.image_to_string(img)

# # Split the text into rows and columns
# rows = text.split('\n')
# matrix = [row.split() for row in rows]

# # Convert the strings in the matrix to integers
# matrix = [[int(cell) for cell in row] for row in matrix]

# # Print the matrix
# print(matrix)
