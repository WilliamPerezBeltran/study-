#!/usr/bin/python -tt
# coding=utf-8

"""
a) Número de hombres con menos de 18 años 
b) Número de mujeres con 18  o mas años
c) Edad y carrera del menor de los hombres
d) Edad y carrera de la mayor de las mujeres
e) Promedio de asignaturas que cursan los estudiantes 
, sin importar sexo , ni edad ni la carrera.
"""

import pdb
def encuesta():

	n_estudiantes=int(input("cuantos estudiantes haran la encuesta: "))

	l_eda_h = []
	l_eda_m = []
	carrera_h = []
	carrera_m = []
	l_asi = []
	lista_carreras = ["ingeniería civil","electronica","sistemas","industrial","psicología","veterinaria","economia"]


	for n in range(n_estudiantes):

		print("Encuestado numero {} ".format(n+1))

		edad=int(input("digite su edad: "))
		
		validacion=True
		while validacion:
			sexo=input("escriba 'H' si es hombre y escriba 'M' si es mujer: ")
			if sexo.isalpha()==True:
				validacion=False
			else:
				print("no se permiten numeros aqui")
		
		
		print("cual carrera esta cursando: ")
		print("1. ingeniería civil") 
		print("2. electronica") 
		print("3. sistemas")
		print("4. industrial") 
		print("5. psicologia") 
		print("6. veterinaria")  
		print("7. economia")
		
		opcion_carrera=int(input("digite su opcion: "))

		c_asignatura=int(input("digite la cantidad de asignaturas que cursa: "))
		l_asi.append(c_asignatura)

		if sexo == 'H':
			l_eda_h.append(edad)
			carrera_h.append(opcion_carrera)

		elif sexo == 'M':
			l_eda_m.append(edad)
			carrera_m.append(opcion_carrera)


	print("l_eda_h")
	print(l_eda_h)
	print("l_eda_m")
	print(l_eda_m)
	print("carrera_h")
	print(carrera_h)
	print("carrera_m")
	print(carrera_m)
	print("l_asi")
	print(l_asi)

	
	lista_carreras 
	contador_edad_h = 0
	for edad in l_eda_h:
		if edad < 18:
			contador_edad_h+=1
	
	contador_edad_m = 0
	for edad in l_eda_m:
		if edad >= 18:
			contador_edad_m += 1

	print("El número de encuestados hombres menores de 18 años son: {} ".format(contador_edad_h))
	print("El número de encuestadas mujeres mayores de 18 años son: {} ".format(contador_edad_m))

	pivote=True
	posicion_menor = 0
	for index, edad in enumerate(l_eda_h):
		if pivote:
			menor = edad
			pivote = False
		elif edad<menor:
			menor = edad
			posicion_menor = index

	carrera_menor_h=lista_carreras[carrera_h[posicion_menor]-1]

	print("El hombre mas joven tiene {} años y estudia {} ".format(menor, carrera_menor_h))

	pivote=True
	posicion_mayor = 0
	
	for index, edad in enumerate(l_eda_m):
		if pivote:
			mayor = edad
			pivote = False
		elif edad>mayor:
			mayor = edad
			posicion_mayor = index
	pdb.set_trace()

	carrera_mayor_m=lista_carreras[carrera_m[posicion_mayor]-1]

	print("la mujer mas vieja tiene {} años y estudia {} ".format(mayor, carrera_mayor_m))
	
	sumatoria=0
	for p in l_asi:
		sumatoria+=p

	promedio=sumatoria/n_estudiantes
	print("el numero promedio de asignaturas que cursan todos los estudiantes es {} ".format(promedio))

	

def main():

	encuesta()

if __name__=="__main__":
	main()






	