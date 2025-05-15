#!/usr/bin/python -tt
# coding=utf-8


print """
The way you decorated say_whee() above is a little clunky. 
First of all, you end up typing the name say_whee three times. 
In addition, the decoration gets a bit hidden away below the definition of the function.

Instead, Python allows you to use decorators in a simpler way with the @ symbol,
sometimes called the “pie” syntax. The following example does the exact same thing 
as the first decorator example:

So, @my_decorator is just an easier
way of saying say_whee = my_decorator(say_whee). 
It’s how you apply a decorator to a function.
-------------------------------------------------------
"""

def my_decorator(func):
	def wrapper():
		print "Something is happing before the function is called."
		func()
		print "Something is happing before the function is called."

	return wrapper 

@my_decorator
def say_whee():
	print "wheeeeeee"

# say_whee = my_decorator(say_whee) # con esa sixtaxis nos ahorramos esta linea de código
say_whee()