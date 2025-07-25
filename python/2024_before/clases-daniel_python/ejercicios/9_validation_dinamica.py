#!/usr/bin/python -tt
# coding=utf-8

def validacion_dinamica():
	n_estudiantes=int(input("cuantos estudiantes haran la encuesta: "))
			
	for n in range(n_estudiantes):
		validacion=True
		nombre = validar("nombre")
		apellido = validar("apellido")

		print("el nombre es {}".format(nombre))
		print("el apellido es {}".format(apellido))

def validar(nombre_apellido):
	validacion = True
	while validacion:
		nombre=str(input("diga su %s: "%(nombre_apellido)))
		if nombre.isalpha()==True:
			validacion=False
		else:
			print("no se permiten numeros en los %s"%(nombre_apellido))

	return nombre


def main():
	validacion_dinamica()


if __name__=='__main__':
	main()
