import hashlib

class Base62():

	_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def decode(self,url):
		#convert string to md5
		md5 = hashlib.md5()
		md5.update(url.encode('utf-8'))
		#convert md5 to exadecimal
		hexa = md5.hexdigest()
		#convet hexadecimal to decimal 
		decimal = int(hexa,16) 

		#convert decimal to base62
		array_base62 = []
		base62 = ''
		while decimal > 0:
			array_base62.append(int(decimal%62))
			decimal = decimal//62 

		for posicion in reversed(array_base62):
			base62 += self._alphabet[posicion]
		#return base62 number
		return base62 

instancia = Base62()

print(instancia.decode("https://github.com/delight-im/ShortURL/blob/master/Python/shorturl.py"))