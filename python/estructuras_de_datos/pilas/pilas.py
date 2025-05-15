import pdb
class Pila():

	def __init__(self,size):
		self.lista = []
		self.tope = 0
		self.size = size

	def empty(self):
		if self.tope == 0:
			return True
		else:
			return False

	def push(self,dato):
		if self.tope < self.size:
			self.lista += [dato]
			self.tope += 1
		else:
			print("la pila esta vacia")

	def pop(self):
		if self.empty():
			print("la pila esta vacia")
		else:
			self.tope -= 1
			self.lista = [self.lista[x] for x in range(self.tope)]

	def show(self):
		for x in range(len(self.lista)):
			print("[%d]   =>   %d  "%(x,self.lista[x]))

	def size(self):
		return self.tope

	def top(self):
		return self.lista[-1]

	def verTope(self):
		print("tope: %d"%(self.tope))