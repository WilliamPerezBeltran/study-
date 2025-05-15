import numpy as np
import cv2
from PIL import Image
import pytesseract

img = cv2.imread('uploaded_image.png', cv2.IMREAD_COLOR)
img = cv2.blur(img, (5, 5))

#HSV (hue, saturation, value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

#Applying threshold on pixels' Value (or Brightness)
thresh = cv2.adaptiveThreshold(v, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

#Finding contours
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Filling contours
contours = cv2.drawContours(img,np.array(contours),-1,(255,255,255),-1)

#To black and white
grayImage = cv2.cvtColor(contours, cv2.COLOR_BGR2GRAY)

#And inverting it
#Setting all `dark` pixels to white
grayImage[grayImage > 200] = 0
#Setting relatively clearer pixels to black
grayImage[grayImage < 100] = 255
#Write the temp file
cv2.imwrite('temp.png',grayImage)

#Read it with tesseract
text = pytesseract.image_to_string(Image.open('temp.png'),config='tessedit_char_whitelist=0123456789 -psm 6 ')

#Output
print("####  Raw text ####")
print(text)
print()
print("#### Extracted digits ####")
print([''.join([y for y in x if y.isdigit()]) for x in text.split('\n')])
