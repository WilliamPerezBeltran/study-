import funciones
import ayuda


def menu():

	while True:
		ayuda.limpiar()

		print("calculadora: ")
		print("digite 1 para sumar")
		print("digite 2 para resta")
		print("digite 3 para multiplicacion")
		print("digite 4 para division")
		print("digite 5 para sumatoria")
		print("digite 6 para promedio")
		print("digite 0 para cerrar la calculadora")

		opcion = input("digite su opcion: ")

		if opcion=="1":
			funciones.suma()

		if opcion=="2":
			funciones.resta()

		if opcion=="3":
			funciones.multiplicacion()

		if opcion=="4":
			funciones.division()

		if opcion=="5":
			funciones.sumatoria()

		if opcion=="6":
			funciones.promedio()
		if opcion == "7":
			funciones.sumatoria1()

		if opcion=="0":
			print("gracias por usar la calculadora")
			return False

		input("\nPresiona ENTER para continuar")
