class Padre(object):
	def __init__(self,name):
		self.name = name

	def suma(self):
		return "tiene el nombre con la suam %s "%(self.name)


class hijo(Padre):
	pass


h1 = hijo("william hijo ")
print(h1.suma())