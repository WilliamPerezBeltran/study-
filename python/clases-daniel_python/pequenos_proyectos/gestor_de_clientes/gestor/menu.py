import helpers 
import manager

def loop():
	while True:
		helpers.clear()

		print("=================")
		print("BIENVENIDO AL GESTOR")
		print("=================")
		print("[1] Listar clientes") # listeme todos los clientes 
		print("[2] Mostrar clientes")
		print("[3] Añadir clientes")
		print("[4] Modificar clientes")
		print("[5] Borrar clientes")
		print("[6] Salir ")

		option = input("> ")
		helpers.clear()

		if option== '1':
			print("Listando clientes")
			manager.show_all()

		if option== '2':
			print("Mostrando clientes")
			manager.find()

		if option== '3':
			print("Añadir clientes")
			if manager.add():
				print("cliente añadido correctamente")

		if option== '4':
			if manager.edit():
				print("cliente modificado correctamente")
		if option== '5':
			if manager.delete():
				print("cliente borrado")

		if option== '6':
			print("Saliendo...\n")
			break
		input("\n Presiona ENTER para continuar")

		