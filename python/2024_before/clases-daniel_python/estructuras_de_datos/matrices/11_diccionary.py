texto="hola mundo"
diccionario=dict()
constador = 0
for x,y in enumerate(texto.split()):
	diccionario[y]=constador
	constador+=1

print(diccionario)


enumerate(['la', 'vida', 'es', 'bella', 'faveriana', 'terminal'])

print("************************")
for x in ((0,'la'),(1,'vida'),(2,'es'),(3,'bella'),(4,'faverian'),(5,'terminal')):
 print(x[0], x[1]) 