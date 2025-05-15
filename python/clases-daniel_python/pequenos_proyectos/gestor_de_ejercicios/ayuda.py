import platform
import os

def limpiar():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system("clear")

def numbers_limit(minor, max,action):
	while True:
		cantidad = int(input(f"Cuantos numeros va {action} "))
		if (cantidad >= minor) and (cantidad <= max):
			return cantidad
		else:
			print("El número debe estar en el rango de 2 a 100")
