#!/usr/bin/python -tt
# coding=utf-8

import sys
import pdb
def decimal_to_binario(decimal_number):
	int_decimal_number = int(decimal_number)
	binary_array = []

	binary_string = ""
	while int_decimal_number > 0:
		binary_array.append(int_decimal_number%2)
		int_decimal_number = int_decimal_number //2

	return ''.join([str(number) for number in reversed(binary_array)])

def test(got, expected):
	if got == expected:
		prefix = "OK"
	else:
		prefix = "WRONG ANSWER"
	print("{} got {} expected {}".format(prefix,repr(got),repr(expected)))

def main():
	if len(sys.argv) != 2:
		print(
			"""
			Meaning
			de = 'decimal'
			bi = 'binari'
			hex = 'hexadecimal'
			base62 = 'base62'
			"""
		)
		print(
			"""
			USAGE: 
			python 12_decimal_to_binario.py { --de_to_bi } <decimal_number>
			or
			python 12_decimal_to_binario.py { --test } 
			"""
		)
		sys.exit(1)

	options = sys.argv[1:]
	option = options[0]
	# pdb.set_trace()
	if options[0] == "--de_to_bi":
		file_number = options[1]
		decimal_to_binario(file_number)
	elif options[0] == "--test":
		test(decimal_to_binario(123),'1111011')
		test(decimal_to_binario(98),'1100010')
		test(decimal_to_binario(6546546),'11000111110010001110010')

if __name__=="__main__":
	main()

