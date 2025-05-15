import pdb

def inverso_funcion(palabra):
	new_list=[]
	for i in range(len(palabra),0,-1):
		new_list.append(palabra[i-1])

	return "".join(new_list)

palabra=[]
can_palabra=int(input("cuantas palabras quiere revisar: "))

for i in range(can_palabra):
	pal=input("escriba la palabra: ")
	palabra.append(pal)

for j in range(len(palabra)):
	inverso=inverso_funcion(palabra[j])
	if palabra[j]==inverso:
		print(f" la posicion {j} es palindromo")
	else:
		print('no es palindromo')
