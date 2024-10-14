import pytesseract
from PIL import Image

# Manually specify the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'E:\Python\text Extraxter\Text-Extracter-From-Images\Tessract\tesseract.exe'

# Load your image
img = Image.open('image.png')

# Extract text from the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
