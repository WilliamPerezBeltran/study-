"""
averiguar si  dos listas son iguales. Si no es asi, especificar la 
primera posición en la cual se hicieron difierentes

"""

import pdb

def same_length(arr1=[1,2,3,4,5,6,7,8],arr2=[1,2,3,4,5,10,23,45]):
	if len(arr1)==len(arr2):
		for r in range(len(arr1)):
			if arr1[r] != arr2[r]:
				return ("en la posicion",r+1," con contenido ",arr2[r],"y contenido",arr1[r], "inicia la diferenciacion de las listas")
				break


	elif len(arr1)>len(arr2):
		return "no son iguales ya que la lista 1 es mas larga"

	elif len(arr1)<len(arr2):
		return "no son iguales ya que la lista 2 es mas larga"
		



	

def main():
	print(same_length())

if __name__=='__main__':
	main()
