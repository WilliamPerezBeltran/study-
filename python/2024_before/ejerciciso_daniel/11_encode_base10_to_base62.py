#!/usr/bin/python -tt
# coding=utf-8

import pdb
import sys
def encode_base10_to_base62(number):
	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	arrayShortener = []

	stringShortener = ''

	while number > 0:
		arrayShortener.append(str(number%62))
		number = number//62

	for x in reversed(arrayShortener):
		stringShortener+=alphabet[int(x)]

	return stringShortener 



def main():
	arg = sys.argv[1:]
	print("pasar el número {} a base62 da: {}".format(arg[0],encode_base10_to_base62(int(arg[0]))   ))

if __name__=='__main__':
	main()

