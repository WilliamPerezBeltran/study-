
from PIL import Image
import io
import base64
 
with open("aa.jpg", "rb") as imageFile:
	str = base64.b64encode(imageFile.read())
	print(str)
	f = io.BytesIO(base64.b64decode(str))
	pilimage = Image.open(f)