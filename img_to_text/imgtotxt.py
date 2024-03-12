from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r"Tesseract-OCR\tesseract.exe"

#Define path to image
path_to_image = 'text.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)
path_text='text-output.txt'
with open(path_text,'w') as filef:
    filef.write(str(text))


