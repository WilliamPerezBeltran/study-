#!/usr/bin/python -tt
# coding=utf-8
print """
It’s possible to define functions inside other functions.
Such functions are called inner functions.
Here’s an example of a function with 
two inner functions:
"""

def parent():
	print "parent function"

	def second_child():
		print "second_child function"
	def first_child():
		print "first_child function"
	

	first_child()
	second_child()

parent()
