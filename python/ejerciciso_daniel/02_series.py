# valor suministrado 5
# resultado 5 4 4 3 3 3 2 2 2 2 1 1 1 1 1

import sys 
import pdb

def way_one_serie(n):
	new_array = []
	diminish = n
	for x in range(1,n+1):
		for y in range(x):
			new_array.append(diminish)
		diminish = diminish-1
	return new_array

def main():
	arg = sys.argv[1:]
	print(*way_one_serie(int(arg[0])),sep=", ")

if __name__=='__main__':
	main()
