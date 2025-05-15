#!/usr/bin/python -tt
# coding=utf-8

"""
Explicacion fibonachi con tuple assigment 
https://www.google.com/search?q=a%2C+b+%3D+b%2C+a%2Bb+python&oq=a%2C+b+%3D+b%2C+a%2Bb+python+&aqs=chrome..69i57j0l3.1534j0j7&sourceid=chrome&ie=UTF-8
https://stackoverflow.com/questions/21990883/python-a-b-b-a-b
https://stackoverflow.com/questions/21990883/python-a-b-b-a-b
https://stackoverflow.com/questions/21990883/python-a-b-b-a-b
"""
import sys
import pdb


def practicing():
    a, b = 0, 1
    while b < 10:
        print(b, end=",")
        a, b = b, a + b


def practicing1():
    a = 0
    b = 1
    while b < 10:
        print(b, end=",")

        temp_a = a
        a = b
        b = temp_a + b


def main():
    practicing()


if __name__ == "__main__":
    main()
