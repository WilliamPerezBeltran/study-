#!/usr/bin/python -tt
# coding=utf-8

print"""
teoría:
para pasar los argumentos en una funcion decorador 
es necesario utilizar *args, **kwargs

The solution is to use *args and **kwargs in the inner wrapper function. 
Then it will accept an arbitrary number of positional and keyword arguments.
Rewrite decorators.py as follows:

-----------------------------------------------
"""


def do_twice(func):
	def wrapper_do_twice(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper_do_twice

@do_twice
def say_hi(name):
	print "hi hi %s "%(name)

say_hi('william Perez')



print"""
-----------------------------------------------
teoría:

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


The wrapper_do_twice() inner function now 
accepts any number of arguments and passes them on to the function it decorates.

-----------------------------------------------
"""
