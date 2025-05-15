#!/usr/bin/python -tt
# coding=utf-8

import pdb
import sys

def hexadecimal_to_decimal(hexadecimal_number='3E0A'):
	alphabet = "0123456789ABCDEF"
	
	decimal = 0
	for index, caracter in enumerate(hexadecimal_number):
		decimal += alphabet.index(caracter)*pow(16,len(hexadecimal_number)-1-index)
	
	return decimal

def main():
	hexadecimal_to_decimal()
	print(hexadecimal_to_decimal())

if __name__=='__main__':
	main()

