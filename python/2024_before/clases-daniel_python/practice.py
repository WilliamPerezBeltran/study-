#!/usr/bin/python -tt
# coding=utf-8
import sys 

def names(nombre):
	cru=open(nombre,'r')
	files = cru.read()
	print(files)
	cru.close()

def main():
	names(sys.argv[1])

if __name__ == '__main__':
	main()