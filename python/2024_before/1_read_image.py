import pytesseract
from PIL import Image

value=Image.open("data/pic_table3.png")
text = pytesseract.image_to_string(value, lang="eng")    
print(text)
