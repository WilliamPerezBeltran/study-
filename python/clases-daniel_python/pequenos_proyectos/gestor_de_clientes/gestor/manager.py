
import pdb
import helpers
import re

clients = []

martha = {'nombre': 'Martha','apellido': 'Pérez','dni': '15J'}

clients.append(martha)
clients.append({'nombre': 'Rocio','apellido': 'Gónzalez','dni': '48H'})
clients.append({'nombre': 'Ana','apellido': 'García','dni': '28Z'})

if __name__ == '__main__':
	print(clients)
	clients

def show(client):
	print(f"{client['dni']} {client['nombre']} {client['apellido']} ")

def show_all():
	for client in clients:
		show(client)

def find():

	dni = input("Introduce el DNI del cliente\n")
	dni = input("Introduce el DNI del cliente\n")

	for client in clients:
		if client['dni'] == dni:
			print(f'se ha encontrado el cliente con dni {dni} :')
			show(client)
			return client

	print("No se ha encontrao ningun cliente con el DNI {}".format(dni))
	print(f"No se ha encontrao ningun cliente con el DNI {dni}")

def is_valid(dni):
	"""
	>>> is_valid('48H')
	False
	>>> is_valid('X82')
	False
	>>> is_valid('21A')
	True
	"""

	if not re.match('[0-9]{2}[A-Z]',dni):
		return False

	for client in clients:
		if client['dni'] == dni:
			return False
	return True

if __name__ == '__main__':
	import doctest
	doctest.testmod()


def add():
	client = dict()
	client['nombre'] = helpers.input_text(2,30)
	client['apellido'] =  helpers.input_text(2,30)

	while True:
		print("Introduce DNI (2 números y carácter en mayúscula)")
		dni = helpers.input_text(3,3)
		if is_valid(dni):
			client['dni'] = dni
			break
		print("DNI incorrecto o en uso")
	clients.append(client)
	return client

def edit():
	dni = input("Introduce el dni del cliente que quiere modificar")

	for cliente in clients:
		if cliente['dni'] == dni:
			print("Introduce nuevo nombre")
			cliente['nombre'] = helpers.input_text(2,30)
			print("introduce el nuevo apellido")
			cliente['apellido'] = helpers.input_text(2,30)
		return True

	return False

def delete():
	dni = input("Introduce el dni del cliente que quiere borrar")

	for i, cliente in enumerate(clients):
		pdb.set_trace()
		if cliente['dni'] == dni:
			cliente = clients.pop(i)

		return True

	return False
	


