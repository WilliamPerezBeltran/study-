import pdb

"""
John works at a clothing store. He has a large pile of socks that he must pair 
by color for sale. Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

For example, there are  n =7 socks with colors ar=[,1,2,1,2,1,3,2]. There is one 
pair of color 1 and one of color 2. There are three odd socks left, one of each color. 
The number of pairs is  2.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer 
representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in ar .
The second line contains  space-separated integers describing the colors  ar[i]
of the socks in the pile.

Constraints
1<= n <= 100
1<= ar[i] <= 100 where 1<= i <= 100  

Output Format
Return the total number of matching pairs of socks that John can sell.

Sample Input

n = 9
ar =[10 20 20 10 10 30 50 10 20]
Sample Output
3
debe dar 3. 3 es el resultad

BASICAMENTE ES ENCONTRAR CUANTAS PAREJAS DE NUMEROS TIENE EL ARRAY 
BASICAMENTE ES ENCONTRAR CUANTAS PAREJAS DE NUMEROS TIENE EL ARRAY 
BASICAMENTE ES ENCONTRAR CUANTAS PAREJAS DE NUMEROS TIENE EL ARRAY 
BASICAMENTE ES ENCONTRAR CUANTAS PAREJAS DE NUMEROS TIENE EL ARRAY 
BASICAMENTE ES ENCONTRAR CUANTAS PAREJAS DE NUMEROS TIENE EL ARRAY 

"""

import sys
import pdb

# n => numbers of elements
# arr => arrays of digits

def sock_merchant(n,arr):
	arr_booleans = [False for x in range(int(n))]
	rta = 0
	for x in range(int(n)):
		for y in range(int(n)):
			if arr[x] == arr[y] and x != y:
				if arr_booleans[x] != True and arr_booleans[y] != True:

					arr_booleans[x] = True
					arr_booleans[y] = True
					rta += 1
					break
	return rta

def test(got, expected):

	if got == expected:
		prefix = 'OK'
	else:
		prefix = 'X'

	print("%s got %s expected %s"%(prefix, repr(got), repr(expected)))
	# pdb.set_trace()

def main():
	print('Test:')

	test(sock_merchant(7,[1,2,1,2,1,3,2]),2)
	test(sock_merchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]),3)

if __name__=='__main__':
	main()