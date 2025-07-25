#!/usr/bin/python -tt
# coding=utf-8
import sys 

def names(filename):
	f = open(filename,'r')
	for line in f:
		print(line)
	f.close()
def main():
	names(sys.argv[1])


if __name__ == '__main__':
	main()