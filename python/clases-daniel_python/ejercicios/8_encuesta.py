#!/usr/bin/python -tt
# coding=utf-8


"""
TTT

realizar y procesar una encuesta a n estudiantes en donde se les solicita nombre, 
edad, sexo, cantidad de asignaturas que están cursando y carrera 
(ingeniería civil , electronica electrinica, sistemas, industrial, 
psicologigia, veterinaria y economia)
Los resultados que debe devolver el programa son los siguientes:

a) Número de hombres con menos de 18 años 
b) Número de mujeres con 18  o mas años
c) Edad y carrera del menor de los hombres
d) Edad y carrera de la mayor de las mujeres
e) Promedio de asignaturas que cursan los estudiantes 
, sin importar sexo , ni edad ni la carrera.

1. pedir la cantidad de estudiantes que haran la encuesta
2. hacer un ciclo que dure dependiendo de la cantidad de estudiantes cursando
3. dentro del mismo pedir nombre,edad,sexo,cantidad de asignaturas y carrera 


"""


n_estudiantes=int(input("cuantos estudiantes haran la encuesta: "))
		
h_menor_18=0
m_mayores_18=0
menor_carrera_h=0
mayor_carrera_m=0
total=0
carrera_actual_1=''
carrera_actual_2=''
for n in range(n_estudiantes):
	validacion=True
	while validacion:
		nombre=str(input("diga su nombre: "))
		if nombre.isalpha()==True:
			validacion=False
		else:
			print("no se permiten numeros en los nombres")

    validacion2=True
    while validacion2:
		edad=int(input("digite su edad "))
		if edad.isdigit()==True:
			validacion2=False
		else:
			print("esto no es un numero")
	sexo=str(input("escriba 'H' si es hombre y escriba 'M' si es mujer: "))
	c_asignatura=int(input("digite la cantidad de asignaturas que cursa: "))
	carrera=str(input("cual carrera esta dando "))

	if edad<18 and sexo=="H":
		h_menor_18+=1

	elif edad>=18 and sexo=="M":
		m_mayores_18+=1

	if edad<menor_carrera_h and sexo=="H":
		menor_carrera_h=edad
		carrera_actual_1=carrera

	if edad>mayor_carrera_m and sexo=="M":
		mayor_carrera_m=edad
		carrera_actual_2=carrera

	total+=c_asignatura



promedio=total/n_estudiantes

print("hay en total %d hombres con edades menores a 18"%(h_menor_18))
print("hay en total %d mujeres con edades mayores o iguales a 18"%(m_mayores_18))
print("el hombre mas joven tiene %d años y hace la carrera de %s"%(menor_carrera_h,carrera_actual_1))
print("la mujer mas vieja tiene %d años y hace la carrera de %s"%(mayor_carrera_m,carrera_actual_2))
print("el promedio de asignaturas que cursan los estudiantes es de %d"%(promedio))



