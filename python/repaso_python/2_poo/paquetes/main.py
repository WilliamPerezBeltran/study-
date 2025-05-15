#!/usr/bin/python -tt
# coding=utf-8

"""
paquetes:Un paquete, es una carpeta que contiene archivos .py.
Pero , para que una carpeta pueda ser considerada un paquete, 
debe contener un archivo de inicio lladado __init_.py (se inicializa el paqueto con ese archivo).
Este archivo no necesita contener ninguna instrucción. 

La forma de empaquetar los paquetes es muestra aqui. (note que cada carpeta titne su __init__.py)

para mas información vaya a este link :
https://docs.python.org/3/tutorial/modules.html

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""

"""
para poder importar modulos que ya estan impaquetados
lo que se requiere es usar la palabra "from"

cuando queremos import un modulo que esta empaquetado utilizadmos "from"
"""

from operaciones.suma import sum as s
from operaciones.resta import rest as r
from operaciones.operaciones2.elevado import elevado as potencia

"""
formula
from carpeta import modulo as funcion_dentro_del_modulo


"""


print "suma importada: ", s(12,5)
print "resta importada: ", r(12,5)
print "elevado importada: ", potencia(3,5)