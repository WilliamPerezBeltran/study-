#valor suministrado 4
#resultado: 1 4 4 9 9 9 16 16 16 16 16

import sys
import pdb

def palindromo(n):
	new_array = []
	for x in range(len(n)-1,-1,-1):
		new_array.append(n[x])
	reverse = ''.join(new_array) 
	if n == reverse:
		return "la palabra {} es palindromo ==>> {} = {}".format(n,n,reverse)
	else:
		return "la palabra {} no es palindromo ==>> {} = {}".format(n,n,reverse)



def main():
	arg = sys.argv[1:]
	print(palindromo(arg[0]))

if __name__=='__main__':
	main()
