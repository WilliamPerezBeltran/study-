#!/usr/bin/python -tt
# coding=utf-8


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
import pdb

def verbing(s):
  if len(s)>=3:
    return s+"ing"
    if s[-3:]=="ing":
      return s+"ly"
  else:
    return s

  pass

# dado un string , encontrar la primera aparicion the 
# la subcadena 'not' and 'bad'. Si the palabra 'bad'  le sigue
# la cadena 'not', reemplaze toda la subcadena 'not'...'bad'
# con 'good'
# retorne el string resultante 
# ejemplo: 
# 'This dinner is not that bad!' yields This dinner is good!
def not_bad(s):

  find_not = s.find('not')
  find_bad = s.find('bad')
  if find_not<find_bad:
    return s.replace(s[find_not:find_bad+3],"good")
  else:
    return s




# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the ront half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

# considere divifir un string en dos mitades s
# si la longitud es par, las dos mitades son de la misma longitud 
# si la longitud es impar diremos que el caracter extra va en la mitad de adelante
# ejemplo 
# 'abcde' front_half is 'abc'
# retorne el string de la forma 
#  a-front + b-front + a-back + b-back

def front_back(a, b):
  if len(a)%2 == 0 :
    mitad_a=len(a)//2 
    front_a=a[mitad_a:]
    back_a=a[:mitad_a]
  else:
    inpar_a=(len(a)//2)+1
    front_a=a[inpar_a:]
    back_a=a[:inpar_a]

  if len(b)%2 == 0:
    mitad_b=len(b)//2
    front_b=b[mitad_b:]
    back_b=b[:mitad_b]
  else:
    inpar_b=(len(b)//2)+1
    front_b=b[inpar_b:]
    back_b=b[:inpar_b]

  return back_a+back_b+front_a+front_b






def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s'%(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
