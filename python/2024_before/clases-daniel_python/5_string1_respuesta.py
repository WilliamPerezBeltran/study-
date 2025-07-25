#!/usr/bin/python -tt
# coding=utf-8

import pdb

# retornar el numero de carros:
# dado un entero que representa en numero de carros
# retornar un string de la forma "numero de carros <carros>"
# donde <carros> es el numero pasado como argumento. Sin embargo 
# si el numero de carros es mayor o igual a 10 entonces use la palabra
# "many" en vez de el <carros>

# entonces carros(5) retorna Numero de carros: 5
# carros(23) retorna Numero de carros: many

def carros(count):
  # '******codigo aqui******'
  pass

# B. ambos extremos
# Dada una cadena s, devuelve una cadena hecha de los primeros 2
# y los ultimos 2 caracteres de la cadena original,
# entonces 'spring' produce 'spng'. Sin embargo, si la longitud de la cadena
# es menor que 2, devuelve la cadena vacía.
def ambos_extremos(s):
   # '******codigo aqui******'
  pass

# C. ocurrencias
# Dada una cadena s, devuelve una cadena
# donde todas las ocurrencias de su primer caracter tienen
# que reemplazarse por '*', exceptuando el primer caracter en si.
# p.ej.  'babble' produce 'ba**le'
# Suponga que la cadena es de longitud 1 o más.

def ocurrencias(s):
   # '******codigo aqui******'
  pass

# D. combinar
# Dadas las cadenas a y b, devuelve una sola cadena con a y b separadas
# por un espacio '<a> <b>', excepto intercambiar los primeros 2 caracteres de cada cadena.
# p.ej.
# 'mix', pod '->' pox mid '
# 'perro', 'cena' -> 'cavar donner'
# Suponga que ayb tienen una longitud de 2 o más.

# 'mix', pod '->' pox mid '

def combinar(a, b):
   # '******codigo aqui******'
  pass

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
  print 'carros'
  test(carros(4), 'Numero de carros: 4')
  test(carros(9), 'Numero de carros: 9')
  test(carros(10), 'Numero de carros: many')
  test(carros(99), 'Numero de carros: many')

  print
  print 'ambos_extremos'
  test(ambos_extremos('spring'), 'spng')
  test(ambos_extremos('Hello'), 'Helo')
  test(ambos_extremos('a'), '')
  test(ambos_extremos('xyz'), 'xyyz')

  
  print
  print 'ocurrencias'
  test(ocurrencias('babble'), 'ba**le')
  test(ocurrencias('aardvark'), 'a*rdv*rk')
  test(ocurrencias('google'), 'goo*le')
  test(ocurrencias('donut'), 'donut')

  print
  print 'combinar'
  test(combinar('mix', 'pod'), 'pox mid')
  test(combinar('dog', 'dinner'), 'dig donner')
  test(combinar('gnash', 'sport'), 'spash gnort')
  test(combinar('pezzy', 'firm'), 'fizzy perm')

if __name__ == '__main__':
  main()
