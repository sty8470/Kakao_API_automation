import os, sys
current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_path)
img_path = os.path.normpath(os.path.join(current_path, 'img'))
pic_path = os.path.normpath(os.path.join(img_path, 'num_friend.png'))

from PIL import Image
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = pic_path
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])
