#!/usr/bin/python -tt
# coding=utf-8

"""
el metodo listdir del modulo os se llama asi : os.listdir(le envio un path)
le envio un path como argumento y lo que retorna son todos los nombres de los 
archivos que hay en ese path 

nota 
obvimante el path que le envio lo hago con los argumentos de la consola
y se lo envio de esta forma 
 python2 utilities1.py ./
"""
import os 
import sys

def listar(dir="../"):
	lista_names = os.listdir(dir)
	print(lista_names)

def main():
	listar(sys.argv[1])

if __name__ == '__main__':
	main() 

