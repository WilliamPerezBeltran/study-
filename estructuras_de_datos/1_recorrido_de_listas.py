lista=[3,4,5,6,7,8,9,10]
print(lista)

for i in range(len(lista)):
	print("index[%d] => %d"%(i,lista[i]))


lista = lista + [34]
print(lista)
print(lista[-1])
print(lista[1:]) ## nos retorna la lista apartir de la posicion 1 hasta la final 
print(lista[1:len(lista)]) ## nos retorna la lista apartir de la posicion 1 hasta la final 
print(lista[:3]) ## retorneme los primeros n elementos  
print(lista[::-1]) ## retorna la lista al reves   