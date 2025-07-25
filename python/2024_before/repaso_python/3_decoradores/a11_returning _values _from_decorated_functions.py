#!/usr/bin/python -tt
#coding=utf-8

print """

It si necessary make sure the wrapper function returns the return value of the decorated function 
in order to let it to return values 
"""


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_hi(name):
	print 'hi %s '%(name)
	print 'entro before %s '%(name)
	return 'hi is returning data %s '%(name)
	print 'entro after %s '%(name)

say_hi("william")


print "no esta retornando el valor revisar debe"