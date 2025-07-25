# El método __init__ es un método especial y que equivale más o menos 
# a lo que se conoce como constructor en otros lenguajes. Su principal 
# función es establecer un estado inicial en el objeto nada más instanciarlo, 
# es decir, inicializar los atributos.

class pelota():
	def __init__(self,color,material,redondes,dureza):
		self.color= color
		self.material=material
		self.redondes=redondes
		self.dureza=dureza

	def revotar(self):
		return "inicio a revotar"

	def inflar(self):
		return "se empezo a inflar"

	def quemar(self):
		return (f"el color {self.color} se esta quemando")


intancia_pelota_1= pelota("rojo","plastico",20,10)
print(intancia_pelota_1.color)
print(intancia_pelota_1.material)
print(intancia_pelota_1.redondes)
print(intancia_pelota_1.dureza)

print(intancia_pelota_1.revotar())
print(intancia_pelota_1.inflar())
print(intancia_pelota_1.quemar())

intancia_pelota_20= pelota("rojo","plastico",20,10)