#!/usr/bin/python -tt
# coding=utf-8

# https://es.wikipedia.org/wiki/Sistema_hexadecimal
# https://codippa.com/convert-hex-to-decimal-in-python/
"""
# hex string
num_hex = '0F'  
# convert hex to decimal
num_dec = int(num_hex, 16)
print('Value in hex:', num_hex)
print('Value in decimal:', num_dec)

"""


import pdb
import sys

def hexadecimal_to_decimal(hexadecimal_number='3E0A'):
	# convert hex to decimal
	return int(hexadecimal_number,16)
	
def main():
	print(hexadecimal_to_decimal())

if __name__=='__main__':
	main()

