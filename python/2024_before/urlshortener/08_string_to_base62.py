#!/usr/bin/python -tt
# coding=utf-8

import sys
import hashlib

def string_to_base62(url):
	#convert string to md5
	md5 = hashlib.md5()
	md5.update(url.encode('utf-8'))
	#convert md5 to exadecimal
	hexa = md5.hexdigest()
	#convet hexadecimal to decimal 
	decimal = int(hexa,16)
	#convert decimal to base62
	return convert_decimal_to_base62(decimal)

def convert_decimal_to_base62(number):
	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	arrayShortener = []
	stringShortener = ''
	while number > 0:
		arrayShortener.append(number%62)
		number = number//62

	for position in reversed(arrayShortener):
		stringShortener+=alphabet[position]

	return stringShortener

def main():
	arg = sys.argv[1:]
	print(string_to_base62(arg[0]))

if __name__=='__main__':
	main()
