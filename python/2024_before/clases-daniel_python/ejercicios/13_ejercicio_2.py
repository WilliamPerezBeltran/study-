"""
comparar dos lista y decir todos las pocisiones en donde son diferentes

"""
def comparacion(arr1=[1,2,3,4,5,6],arr2=[1,3,4,5,6,8]):
	
	lista_comparaciones_diferentes=[]
	
	if len(arr1)==len(arr2):
		for p in range(len(arr1)):

			if arr1[p] != arr2[p]:
				lista_comparaciones_diferentes.append(p+1)

		if lista_comparaciones_diferentes == []:
			return("todo esta igual")

		else:
			return ("en la posiciones",lista_comparaciones_diferentes,"estan las diferencias de las listas")
				

def main():
	print(comparacion())

if __name__=='__main__':
	main()