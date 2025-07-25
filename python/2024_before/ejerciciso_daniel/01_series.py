#valor suministrado 4
#resultado: 1 4 4 9 9 9 16 16 16 16 16

import sys
import pdb

def way_one_serie(n):
	new_array = []
	for x in range(1,int(n)+1):
		for y in range(x):
			new_array.append(x*x)
	return new_array 

def way_two_serie(n):
	return [x*x for x in range(1,int(n)+1) for y in range(x)]

def main():
	arg = sys.argv[1:]
	print(way_one_serie(arg[0]))
	print(way_two_serie(arg[0]))

if __name__=='__main__':
	main()
