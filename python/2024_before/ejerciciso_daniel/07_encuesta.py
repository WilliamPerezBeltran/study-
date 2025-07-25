#!/usr/bin/python -tt
# coding=utf-8


"""
realizar y procesar una encuesta a N estudiantes en donde se les solicita nombre, 
edad, sexo, cantidad de asignaturas que están cursando y carrera 
(ingeniería civil , electronica electrinca, sistemas, industrial, 
psicologigia, veterinaria y economia)
Los resultados que debe devolver el programa son los siguientes:

a) Número de hombres con menos de 18 años 
b) Número de mujeres con 18  o mas años
c) Edad y carrera del menos de los hombres
d) edad y carrera de la mayor de las mujeres
e) Promedio de signaturas que cursan los estudiantes 
, sin importar sexo , edad ni carrera.

"""
import pdb

def encuesta():
	sexo_hombres = []
	nombre_hombres = []
	edad_hombres = []
	carrera_hombres = []
	cantidad_asignaturas_hombres = []

	sexo_mujeres =[]
	nombre_mujeres =[]
	edad_mujeres =[]
	carrera_mujeres =[]
	cantidad_asignaturas_mujeres =[]
	
	validation_encuestados = True
	while validation_encuestados:
		try:
			encuestados = int(input("Ingrese el numero de encuestado: "))

		except Exception as e:
			print("Ingrese un número por favor")
		else:
			if encuestados <= 15 and encuestados >= 1:
				validation_encuestados = False
			else:
				print("el numero debe ser menor a 11 pero mayor a 1")

	for index, value in enumerate(range(encuestados)):
		print("encuestado numero {} ".format(index+1))
		validation_edad = True
		while validation_edad:
			try:
				edad = int(input("Ingrese su edad: "))
			except Exception as e:
				print("Ingrese por favor bien su edad debe ser un numero ")

			else:
				if edad >= 18 and edad <= 110:
					validation_edad = False
				else:
					print("su edad no valida") 

		validation = True
		while validation:
			sexo = input("digite su genero, m para masculino y f para femenino: ")
			if sexo == 'm' or sexo == 'f':
				validation = False

		validation_name = True
		while validation_name:
			name = input("deme su nombre ")
			if name.isalpha():
				validation_name = False

		validation_asignaturas = True
		while validation_asignaturas:
			asignaturas = input("deme el numero de asignaturas: ")
			if asignaturas.isdigit():
				validation_asignaturas = False

		validation_carrera = True
		while validation_carrera:
			print("""
					1. ingenieria civil 
					2. ingenieria electronica 
					3. ingenieria sistemas 
					4. ingenieria industrial
					5. psicologigia
					6. veterinaria
					7. economia
				""")
			carrera = input("Digite el número que corresponde a la carrera que estudio: ")
			if carrera.isdigit() and int(carrera) <=7 and int(carrera) >=1 :
				validation_carrera = False

		if sexo == 'm':
			sexo_hombres.append(sexo)
			nombre_hombres.append(name)
			edad_hombres.append(edad)
			carrera_hombres.append(carrera)
			cantidad_asignaturas_hombres.append(int(asignaturas))
		else:
			sexo_mujeres.append(sexo)
			nombre_mujeres.append(name)
			edad_mujeres.append(edad)
			carrera_mujeres.append(carrera)
			cantidad_asignaturas_mujeres.append(int(asignaturas))


			print('sexo_hombres',sexo_hombres)
			print('nombre_hombre',nombre_hombres)
			print('edad_hombres',edad_hombres)
			print('carrera_hombres',carrera_hombres)
			print('cantidad_asignaturas_hombres',cantidad_asignaturas_hombres)

			print('sexo_mujeres',sexo_mujeres)
			print('nombre_mujeres',nombre_mujeres)
			print('edad_mujeres',edad_mujeres)
			print('carrera_mujeres',carrera_mujeres)
			print('cantidad_asignaturas_mujeres',cantidad_asignaturas_mujeres)

def numero_Hombres_menos_18(arr):
	numero_hombres_menores_18 = 0
	for x in arr:
		if x < 18:
			numero_hombres_menores_18 += 1
	return numero_hombres_menores_18

def mujeres_mayores_18(arr):
	numero_hombres_mayores_18 = 0
	for x in range(arr):
		if x > 18:
			numero_hombres_mayores_18 += 1
	return numero_hombres_mayores_18

def edad_y_carrera_menor_hombres(arr_edad,arr_carrera,arr_nombre):
	pass

def edad_carrera_mayor_mujeres(arr_edad):
	pass

def promedio_de_asignaturas_estudiantes(arr_aignaturas_h,arr_aignaturas_m):
	total_array_asignaturas = arr_aignaturas_h + arr_aignaturas_m
	
	acco = 0
	for x in arr_aignaturas_h + arr_aignaturas_m:
		acco += x
	return acco/len(arr_aignaturas_h + arr_aignaturas_m)  


# a) Número de hombres con menos de 18 años 
# b) Número de mujeres con 18  o mas años
# c) Edad y carrera del menor de los hombres
# d) edad y carrera de la mayor de las mujeres
# e) Promedio de signaturas que cursan los estudiantes 
# , sin importar sexo , edad ni carrera.
	






def main():
	encuesta()


if __name__=='__main__':
	main()
