#!/usr/bin/python -tt
# coding=utf-8

import pdb
def encode_base10_to_base62(number=100):
	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	arrayShortener = []

	stringShortener = ''

	while number > 0:
		arrayShortener.append(str(number%62))
		number = number//62

	for x in reversed(arrayShortener):
		stringShortener+=alphabet[int(x)]

	return stringShortener 

def decode_base10_to_base62(base_62='1C'):
	len_of_string_base_62 = len(base_62) - 1
	result = 0
	for x in array_get_current_position(base_62):
		result = result + (x * pow(62,len_of_string_base_62))
		len_of_string_base_62-=1 

	return result

def array_get_current_position(string):
	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	array_get_current_position = []
	for current_string in list(string):
		for index,caracter in enumerate(alphabet):
			if  caracter == current_string:
				array_get_current_position.append(index)
	
	return array_get_current_position

def main():
	print("pasar el número 100 a base62 da: ",encode_base10_to_base62())
	print("y decodificar el numero 1C en base62 a base10 da: ",decode_base10_to_base62())

if __name__=='__main__':
	main()