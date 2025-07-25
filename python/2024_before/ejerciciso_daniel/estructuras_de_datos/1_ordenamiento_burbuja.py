# # ***************
# # Método de ordenamiento de burbuja 
# # revisa cada elemento de la lista con el siguiente elemento, 
# # intercambiandolos de posicion si esta en el orden equivocado
# # ***************

# # 4 2 6 8 5 7 
# # 2 4 6 8 5 7 
# # 2 4 6 8 5 7 
# # 2 4 6 5 7 8
# # 2 4 5 6 7 8 

# lista = [4,2,6]
# pivote = 0

# for i in range(len(lista)):
# 	print('-------{}'.format(i))
# 	for x in range(len(lista)-1):

# 		print("indice: %d ==> valor:%d "%(x,lista[x]))
# 		if lista[x] > lista[x+1]:
# 			pivote = lista[x+1]
# 			lista[x+1] = lista[x]
# 			lista[x] = pivote
			
# 		# print(lista)


lista = [9,8,7,6,5,4,3,2,1]

for i in range(len(lista)):
	for x in range(len(lista)-1):
		if lista[x] > lista[x+1]:
			pivote = lista[x+1]
			lista[x+1] = lista[x]
			lista[x] = pivote

print(lista)
