# El método __init__ es un método especial y que equivale más o menos 
# a lo que se conoce como constructor en otros lenguajes. Su principal 
# función es establecer un estado inicial en el objeto nada más instanciarlo, 
# es decir, inicializar los atributos.

class pelota():
	def __init__(self):
		self.color= "rojo"
		self.material="plastico"
		self.redondes=10
		self.dureza=7

	def revotar(self):
		return "inicio a revotar"

	def inflar(self):
		return "se empezo a inflar"


intancia_pelota_1= pelota()
print(intancia_pelota_1.color)
print(intancia_pelota_1.material)
print(intancia_pelota_1.redondes)
print(intancia_pelota_1.dureza)

print(intancia_pelota_1.revotar())
print(intancia_pelota_1.inflar())
