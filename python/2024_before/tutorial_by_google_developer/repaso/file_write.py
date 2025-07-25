#!/usr/bin/python

import sys

def ole():
	file = open('new_file.txt','w')
 	for i in range(10):
 		file.write("oleeee: %d" %(i))
 	file.close()




def main():
	ole()

if __name__ == '__main__':
	main()