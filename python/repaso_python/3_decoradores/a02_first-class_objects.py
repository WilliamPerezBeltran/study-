#!/usr/bin/python -tt
# coding=utf-8

print """ 
In Python, functions are first-class objects. 
This means that functions can be passed around 
and used as arguments, just like any other object 
(string, int, float, list, and so on). 
"""

def say_hello(name):
	return 'hello %s'%(name)

def be_awesome(name):
	return 'Yo %s, together we are the awesomest!'%(name)

def greet_bob(greeter_func):
	return greeter_func('Bob')

# print say_hello("william")
print be_awesome
# print be_awesome("william")
print greet_bob(say_hello)
print greet_bob(be_awesome)

