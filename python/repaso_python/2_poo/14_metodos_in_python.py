#!/usr/bin/python -tt
# coding=utf-8

"""
documentation: 

https://docs.python.org/3.4/library/functions.html

https://docs.python.org/3.4/library/functions.html

https://docs.python.org/3.4/library/functions.html

"""

# -------------------------------any()-------------------------------

"""
any()
va retornar un booleano , verdadero o falso 
en caso de que el parametro que le enviarmos sea iterable y si contiene algun valor 
"""

string = "la vida es bella"
print any(string)

array = []
array1 = [1,2,3,5,6,4]

print any(array)
print any(array1)

# -------------------------------bin()-------------------------------
"""
bin(int)
convierte un entero a un numero binario en un string 
nos devuelve la vase binaria, la entreda es un numero 
"""
print bin(123)
print bin(1)
print bin(10)
print bin(100)
print bin(1000)

# -------------------------------chr()-------------------------------
"""
chr(int)
va retorna un carater del codigo asqui de nuestro ordenador 
el parametro es un numero 

"""

for x in range(120):
	print x, chr(x)

"""
resultado
0 
1 
2 
3 
4 
5 
6 
7 
8 
9 	
10 

11 

12 

13 
14 
15 
16 
17 
18 
19 
20 
21 
22 
23 
24 
25 
26 
27 
28 
29 
30 
31 
32  
33 !
34 "
35 #
36 $
37 %
38 &
39 '
40 (
41 )
42 *
43 +
44 ,
45 -
46 .
47 /
48 0
49 1
50 2
51 3
52 4
53 5
54 6
55 7
56 8
57 9
58 :
59 ;
60 <
61 =
62 >
63 ?
64 @
65 A
66 B
67 C
68 D
69 E
70 F
71 G
72 H
73 I
74 J
75 K
76 L
77 M
78 N
79 O
80 P
81 Q
82 R
83 S
84 T
85 U
86 V
87 W
88 X
89 Y
90 Z
91 [
92 \
93 ]
94 ^
95 _
96 `
97 a
98 b
99 c
100 d
101 e
102 f
103 g
104 h
105 i
106 j
107 k
108 l
109 m
110 n
111 o
112 p
113 q
114 r
115 s
116 t
117 u
118 v
119 w

"""

# -------------------------------enumerate(list)-------------------------------
"""
enumerate(list)
esta funcion lo que hace enumerar los elementos de la lista en forma de tupla  
"""
lista = [1,2,3,4,54,56,6,4,3,23]

for x in enumerate(lista):
	print x
print "---------------------"
"""

resultado:
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 54)
(5, 56)
(6, 6)
(7, 4)
(8, 3)
(9, 23)

"""

for index, x in enumerate(lista):
	print index,x

"""
resultado
0 1
1 2
2 3
3 4
4 54
5 56
6 6
7 4
8 3
9 23

"""

# -------------------------------help(function)-------------------------------
"""
help(function)
nos retorna una pequeña documentacion del metodo o la clase
"""

# -------------------------------list()-------------------------------
"""
list()
nos devuelve una lista en forma de caracter 

"""
a = "hola mundo de python"
print list(a)

"""
['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o', ' ', 'd', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']

"""

# -------------------------------hex()-------------------------------
"""
xx()

"""

# -------------------------------hex()-------------------------------
"""
hex(x)
convierte numeros enteros a base hexadecimal
Convert an integer number to a lowercase hexadecimal string prefixed with “0x”, for example:
>>>
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'

xx()

"""
# -------------------------------ord()-------------------------------
"""
ord()
se utiliza para convertir un caracter al numero del codigo asqui

"""
print ord("g")
print ord("*")
print ord(" ")

# -------------------------------sum()-------------------------------
"""
sum()
sumar todos los parametros que le enviemos y nos retorna la suma 
"""
print "---------"
print sum([1,2,2,4,23])
print sum([1,5,6,2])
# -------------------------------xxx()-------------------------------
"""
xx()

"""
x = [1,2,3,4,5,6]
y = ['a','s','d','f','g,'r'']
zipped = zip(x,y)

print zipped 

#[(1, 'a'), (2, 's'), (3, 'd'), (4, 'f'), (5, 'g,')]

for x,y in zipped: print x,y

"""
... 
1 a
2 s
3 d
4 f
5 g
>>> 

"""



# -------------------------------xxx()-------------------------------
"""
xx()

"""




