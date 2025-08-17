# ~~~~~~~~~~~~~~~~~~~~~~~~~~

try:
    result = 10 / 0
except Exception as e:
    print("Error generico: ",e)

# ~~~~~~~~~~~~Full syntax with else and finallyi ~~~~~~~~~~~~~~

try:
    x = int("asdf")
except Exception as e:
    print("Error: ", e)
else:
    print("Run if no error happens")
finally:
    print("This always runs (cleanup, closing files, etc.")
print("""
In sumary: 
    - try: The code you want to run  
    - except: Handle specific errors 
    - else: Run if not exceptions accurs 
    - finally:Always run (good for cleanup, closing files, etc )
    """)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
print("""
Tipos de excepciones comunes
Algunos de los más usados son:
    ValueError → Conversión de tipos inválida
    TypeError → Operaciones con tipos incompatibles
    IndexError → Índice fuera de rango en listas o strings
    KeyError → Cuando no existe una clave en un diccionario
    ZeroDivisionError → División entre cero
    FileNotFoundError → Archivo inexistente al intentar abrir
    PermissionError → Permiso denegado al acceder a un archivo
    AttributeError → Intento de acceder a un atributo que no existe
    ImportError / ModuleNotFoundError → Problema al importar módulos
    RuntimeError → Errores generales en tiempo de ejecución
    Exception → Clase base para casi todas las excepciones

""")
