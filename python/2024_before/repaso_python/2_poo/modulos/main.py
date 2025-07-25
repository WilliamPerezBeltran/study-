#!/usr/bin/python -tt
# coding=utf-8

"""
Modulos:
Los módulos en python son grupos de funciones alojadas dentro un archivo .py 
los modulos para que funcionen deben estar en la misma carpeta.

Para importar los modulos que deben estar en la misma carpeta se puede hacer
con la palabra reservada import.

En el momento de agregar el codigo "import xxxx" lo que hace import es ejecutar el archivo 
que se especifica en el import . Se ejecuta el archivo esto importante 

"""



import saludos 
import suma
import resta

saludos.manana()
print "Suma: ",suma.sum(12,34)
print "Resta: ",resta.rest(34,12)