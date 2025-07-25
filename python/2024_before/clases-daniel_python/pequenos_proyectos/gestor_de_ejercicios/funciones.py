import ayuda
import pdb


def suma():
	acumulador = 0
	cantidad = ayuda.numbers_limit(2,100,'sumar:')

	for sam in range(cantidad):
		numeros = int(input("deme los numeros: "))
		acumulador += numeros

	print("el resultado de la suma es:",acumulador)

def resta():
	acumulador=0
	cantidad = ayuda.numbers_limit(2,100,'restar:')

	for res in range(cantidad):
		numeros=int(input("deme los numeros: "))
		acumulador-=numeros

	print("el resultado de la resta es:",acumulador)

def multiplicacion():
	acumulador=1
	cantidad = ayuda.numbers_limit(2,100,'multiplicar:')

	for mul in range(cantidad):
		numeros=int(input("deme los numeros: "))
		acumulador=acumulador*numeros

	print("el resultado de la multiplicacion es:",acumulador)
	
def division():
	dividendo=int(input("deme el numerador: "))
	divisor=int(input("deme el divisor: "))
	print("el resultado de la division es:",dividendo/divisor)

def sumatoria():
	inferior = int(input("deme el limite inferior"))
	superior = int(input("deme el limite superior"))
	repeticiones = superior-inferior

	acomulador = inferior
	acomuladorTotal = 0
	for x in range(repeticiones+1):
		acomuladorTotal+=acomulador 
		print(acomuladorTotal)
		acomulador+=1  
	print(f"rta: {acomuladorTotal}")             

def sumatoria1():
	inferior = int(input("deme el limite inferior"))
	superior = int(input("deme el limite superior"))
	repeticiones = superior-inferior
	acomulador = 0

	for item in range(inferior,superior+1):
		acomulador+=item
	
	print(f"rta: {acomulador}")           

def promedio():
	numeros = int(input("cuantos numeros va promediar: "))
	acomulador = 0
	for x in range(numeros):
		numero_pedido =int(input(f"deme el numero {x+1}"))
		acomulador+=numero_pedido
	promedio = acomulador/numeros
	print(f"el promedio es: {promedio}")