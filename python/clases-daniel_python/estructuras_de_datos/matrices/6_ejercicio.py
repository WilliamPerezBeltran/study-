#!/usr/bin/python -tt
# coding=utf-8
import pdb
def triangulo():
	matriz=[[1,1],[1,1,1,1],[1,1,1],[1,1,1,1,1,1,1,1]]

	for item in matriz:
		print(len (item))
"""
	for i in range(len(matriz)):
		len(matriz[i])
"""
def main():
	triangulo()


if __name__=='__main__':
	main()



class matriz(object):
	"""docstring for ClassName"""
	def __init__(self, matriz):
		# super(ClassName, self).__init__()
		self.matriz = matriz

	def cuadrada():
		pass

	def diagonal():
		pass


nstance_matriz = matriz([[1,1],[1,1,1,1],[1,1,1],[1,1,1,1,1,1,1,1]])

nstance_matriz.diagonal() # True 
nstance_matriz.triangular_superior() # True 
