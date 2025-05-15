valor_1=int(input("digite el valor para comparar con los numeros en las posiciones impares: "))
valor_2=int(input("digite el valor para comparar con los numeros en las posiciones pares: "))
tamaño=int(input("digite el tamaño de la lista a comparar: "))
lista=[]
m=0

for i in range(tamaño):
	valores=int(input("digite valores a la lista: "))
	lista.append(valores)

for j in range(len(lista)):
	m=j+1
	if m%2==0:
		if lista[j]==valor_2:
			print(f"la posicion par {j+1} de la lista tiene el mismo valor que valor_2 que es: {valor_2}")
	else:
		if lista[j]==valor_1:
			print(f"la posicion impar {j+1} de la lista tiene el mismo valor que valor_1 que es: {valor_1}")

