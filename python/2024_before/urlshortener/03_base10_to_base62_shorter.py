# #!/usr/bin/python -tt
# # coding=utf-8

# import pdb
# def encode_base10_to_base62(number=100):
# 	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 	arrayShortener = []

# 	stringShortener = ''

# 	while number > 0:
# 		arrayShortener.append(str(number%62))
# 		number = number//62

# 	for x in reversed(arrayShortener):
# 		stringShortener+=alphabet[int(x)]

# 	return stringShortener 


# def decode_base10_to_base62(base_62='1C'):
# 	result = 0
# 	for index, value in enumerate(array_get_current_position(base_62)):
# 		result = result + (value * pow(62,len(base_62)-1)-index)
# 	return result

# def array_get_current_position(string):
# 	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
# 	return [index for current_string in list(string) for index,caracter in enumerate(alphabet) if  caracter == current_string]

# def main():
# 	print("pasar el número 100 a base62 da: ",encode_base10_to_base62())
# 	print("y decodificar el numero 1C en base62 a base10 da: ",decode_base10_to_base62())

# if __name__=='__main__':
# 	main()





#!/usr/bin/python -tt
# coding=utf-8

import pdb
def encode_base10_to_base62(number=5987):
	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	arrayShortener = []

	stringShortener = ''

	while number > 0:
		arrayShortener.append(str(number%62))
		number = number//62

	for x in reversed(arrayShortener):
		stringShortener+=alphabet[int(x)]

	return stringShortener 


def decode_base10_to_base62(base_62='1yz'):
	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = 0
	for index, value in enumerate(base_62):
		result = result + (alphabet.index(value) * pow(62,len(base_62)-1-index))
	return result

def main():
	print("pasar el número 100 a base62 da: ",encode_base10_to_base62())
	print("y decodificar el numero 1C en base62 a base10 da: ",decode_base10_to_base62())

if __name__=='__main__':
	main()