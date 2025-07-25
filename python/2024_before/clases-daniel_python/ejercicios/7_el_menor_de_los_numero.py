"""

1.hago un ciclo que recorra la lista
2.creo un acumulador el cual  guarde el valor menor2
3.hago un if el cual compare los valores en la lista
4.
5.
"""
import pdb

def menor():
	arr = [12,23,34,45,54,43,23,22,1,2,3,4,56,7,89,9]

	first_time = True
	for x in arr:
		if first_time:
			menor = x
			first_time = False
		else:
			if x < menor:
				menor = x
	print(arr)
	print(menor)


	

def main():
	menor()

if __name__=='__main__':
	main()
