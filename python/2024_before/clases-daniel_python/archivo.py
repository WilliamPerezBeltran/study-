#!/usr/bin/python -tt
# coding=utf-8

import sys

def main():
	pa = sys.argv[1]
	print(coger(pa))

def coger(pa):
	print(pa)
	return(pa[0:2] + pa[-2:])

 

if __name__=='__main__':
	main()