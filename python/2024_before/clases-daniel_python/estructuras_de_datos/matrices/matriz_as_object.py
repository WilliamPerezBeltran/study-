import pdb

class Matriz():
	def __init__(self,fila,columna):
		self.fila = fila
		self.columna = columna

	def inicializar(self):
		""" inicializa la matriz con las filas i columnas dadas """
		sup=0
		inf=0
		matriz=[]
		for i in range(self.fila):
			matriz.append([])
			for j in range(self.columna):
				matriz[i].append(None)
		return matriz

	def imprimir_matriz(self):
		"""Imprime la matriz en el estado en el que esté la matriz"""
		for x in self.inicializar():
			print(x)

	def dar_valores_a_la_matriz(self):
		matriz = self.inicializar()
		for i in range(self.fila):
			for j in range(self.columna):
				matriz[i][j] = input(f"déme el valor de la fila {i} y la columna {j}: ")

		for i in range(self.fila):
			for j in range(self.columna):
				print(matriz[i][j], end=" ")
			print()

		return matriz

	def diagonal(self):
		if self.fila == self.columna:
			matriz = self.inicializar()
			for i in range(self.fila):
				for j in range(self.columna):
					if i == j:
						matriz[i][j] = 1
					else:
						matriz[i][j] = 0

			for i in range(self.fila):
				for j in range(self.columna):
					print(matriz[i][j], end=" ")
				print()

			return matriz
		else:
			print("""
				La matriz no es cuadrada por lo
				tanto no se puede hacer su diagonal
				""")
	def matriz_superior(self):
		matriz= self.inicializar()
		for i in range(len(matriz)):
			for j in range(len(matriz)):
				if i<j:
					matriz[i][j]=1
		
		for i in range(self.fila):
			for j in range(self.columna):
				print(matriz[i][j], end=" ")
			print()

	def matriz_inferior(self):
		matriz= self.inicializar()
		for i in range(len(matriz)):
			for j in range(len(matriz)):
				if i>j:
					matriz[i][j]=1

		for i in range(self.fila):
			for j in range(self.columna):
				print(matriz[i][j], end=" ")
			print()


class Daniel():
	print("estoy en la clase Daniel")



class William():
	print("estoy en la clase William")








