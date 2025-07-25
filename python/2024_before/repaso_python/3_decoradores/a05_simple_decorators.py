#!/usr/bin/python -tt
# coding=utf-8


print """
By definition, a decorator is a function that takes another
function and extends the behavior  of the latter function
without explicitly modifying it.
"""

print """
Put simply: decorators wrap a function, modifying its behavior.
"""





def my_decorator(func):
	def wrapper():
		print "Something is happing before the function is called."
		func()
		print "Something is happing before the function is called."

	return wrapper 

def say_whee():
	print "wheeeeeee"

say_whee = my_decorator(say_whee)
say_whee()