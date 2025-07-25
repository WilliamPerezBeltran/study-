#!/usr/bin/python -tt
# coding=utf-8

"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer,n , find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10  characters
 of her infinite string. There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of
 occurrences of a in the prefix of length n in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .


Sample Input 0

aba
10
Sample Output 0

7

explicacion:

aba aba aba a
se repitio el string  3 veces enteras y un a 
y el numero de a es : 7
"""

# s = string
# n = el numero de repeticiones que tiene que hacer el string


import sys
 

def repeated_string(s, n):
    l = len(s)
    numbers_of_repetition = n // l
    numbers_a_partes_enteras = s.count("a") * numbers_of_repetition
    rest = n - (l * numbers_of_repetition)
    return numbers_a_partes_enteras + s[:rest].count("a")


def test(got, expected):
    if got == expected:
        prefix = " OK "

    else:

        prefix = " X "

    print("%s got %s expected %s " % (prefix, repr(got), repr(expected)))


def main():
    test(repeated_string("aba", 10), 7)
    test(repeated_string("abcac", 10), 4)
    test(repeated_string("a", 1000000000000), 1000000000000)


if __name__ == "__main__":
    main()
