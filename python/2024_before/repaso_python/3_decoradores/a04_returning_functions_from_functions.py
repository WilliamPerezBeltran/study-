#!/usr/bin/python -tt
# coding=utf-8

print """
Python also allows you to use functions as return values. 
The following example returns one of the
inner functions from the outer parent() function:
"""

def parent(num):
	def first_child():
		return "hi i am first_child"

	def second_child():
		return "hi i am second_child"

	if num == 1:
		return first_child
	else:
		return second_child



first = parent(1)
print first
print first()