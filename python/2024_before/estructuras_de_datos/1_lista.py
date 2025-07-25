lista = [12,432,33,34,35,56]

print("-------------------")
print("array")
print(lista)

for x in lista:
 print(x)

print("-------------------")

for x in range(len(lista)):
	print(str(x)+'--'+str(lista[x]))


print("-------------------")

for x in range(len(lista)):
	print("index[%d] => %d"%(x,lista[x]))


print("-------------------")
print("agrega elemento con ")

lista = lista + [12123]
print(lista)


print("-------------------")
print("retorna el último ")
print(lista[-1])




print("-------------------")
print(" ")




print("-------------------")
print(" imprime desde la posicion x hasta el final")
print(lista[1:])





print("-------------------")
print(" ")
print(lista[0:3])
print(lista[:5])





print("-------------------")
print(" ")




print("-------------------")
print(" truco imprime la lista otra vez")
print(lista[::-1])

