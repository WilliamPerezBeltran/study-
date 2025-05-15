# lista = [44,42,56,86,52,17]
lista = [4,2,6,8,5,7]

print("array para ordenar = %s"%(str(lista)) )

def swap(mayor, menor):
	pivote = mayor
	lista[x] = menor
	lista[x+1] = pivote

for i in range(len(lista)):
	print('i',i)
	for x in range(len(lista)-1):
		print('x',x)

		if lista[x] > lista[x+1]:
			swap(lista[x],lista[x+1])
			print(lista)


