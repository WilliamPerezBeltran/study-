#!/usr/bin/python -tt
# coding=utf-8

def validacion_dinamica():

	n_estudiantes=int(input("cuantos estudiantes haran la encuesta: "))
			
	for n in range(n_estudiantes):
		validacion=True
		nombre = validar(nombre_apellido)
		while validacion:
			nombre=str(input("diga su nombre: "))
			if nombre.isalpha()==True:
				validacion=False
			else:
				print("no se permiten numeros en los nombres")

		validacion1=True
		while validacion1:
			nombre1=str(input("diga su apellido: "))
			if nombre1.isalpha()==True:
				validacion1=False
			else:
				print("no se permiten numeros en los apellidos")

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
