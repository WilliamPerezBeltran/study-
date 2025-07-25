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
  if count < 10:
    return str(count) 
  else: 
    return 'many'


# B. ambos extremos
# Dada una cadena s, devuelve una cadena hecha de los primeros 2
# y los ultimos 2 caracteres de la cadena original,
# entonces 'spring' produce 'spng'. Sin embargo, si la longitud de la cadena
# es menor que 2, devuelve la cadena vacía.
def ambos_extremos(s):
  if len(s)<2:
    return ""
  else:
    inicio=s[0:2]
    final=s[-2:]
    return inicio+final


# C. ocurrencias
# Dada una cadena s, devuelve una cadena
# donde todas las ocurrencias de su primer caracter tienen
# que reemplazarse por '*', exceptuando el primer caracter en si.
# p.ej.  'babble' produce 'ba**le'
# p.ej.  'cacccmincndac' produce 'ca***min*nda*'
# p.ej.  'tacanotianttta' produce 'tacano*ian***a'
# Suponga que la cadena es de longitud 1 o más.

#h e l l o
#0 1 2 3 4 
#s = "hello"
#s[0] = "h"
#s[4] = "o"
#s[1:] = "ello"

def ocurrencias(s):
  letra_1 = s[0:1]
  letra_2 = s[1:]
  asterisco = letra_2.replace(letra_1,"*")
  return letra_1+asterisco


#def ocurrencias(s):
  #return s[0:1]+s[1:].replace(s[0:1],"*")

# D. combinar
# Dadas las cadenas a y b, devuelve una sola cadena con a y b separadas
# por un espacio '<a> <b>', excepto intercambiar los primeros 2 caracteres de cada cadena.
# p.ej.
# 'mix', pod '->' pox mid '
# 'perro', 'cena' -> 'cerro pena'
# Suponga que ayb tienen una longitud de 2 o más.

# 'mix', pod '->' pox mid '

# 'mix', pod '
# 'mi', po'
# 'mi' => x
# 'po' => d
#  pox mid


def combinar(a, b):
  mix_1=a[0:2]
  mix_2=b[0:2]
  max_1=a[2:]
  max_2=b[2:]
  print("%s %s"%(mix_2 + max_1,mix_1 + max_2))
  pdb.set_trace()
  return "%s  %s"%(mix_2 + max_1,mix_1 + max_2)


   

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print("%s got: %s expected: %s"%(prefix, repr(got), repr(expected))) 

def main():
  print('carros')
  test(carros(4), '4')
  test(carros(9), '9')
  test(carros(10), 'many')
  test(carros(99), 'many')

  print
  print('ambos_extremos')
  test(ambos_extremos('spring'), 'spng')
  test(ambos_extremos('Hello'), 'Helo')
  test(ambos_extremos('a'), '')
  test(ambos_extremos('xyz'), 'xyyz')

  
  print
  print('ocurrencias')
  test(ocurrencias('babble'), 'ba**le')
  test(ocurrencias('aardvark'), 'a*rdv*rk')
  test(ocurrencias('google'), 'goo*le')
  test(ocurrencias('donut'), 'donut')

  print
  print('combinar')
  test(combinar('mix', 'pod'), 'pox mid')
  test(combinar('dog', 'dinner'), 'dig donner')
  test(combinar('gnash', 'sport'), 'spash gnort')
  test(combinar('pezzy', 'firm'), 'fizzy perm')

if __name__ == '__main__':
  main()
