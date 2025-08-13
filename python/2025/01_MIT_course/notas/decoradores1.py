
print("=======================")

def decorador(funcion):
    def wrapper():
        print("inicio")
        funcion()
        print("final")

    return wrapper

@decorador
def saludar():
    print("ole")

saludar()

print("=======================")

def mayuscula(func):
    def wrapper(name):
        resultado = func(name)
        return resultado.upper()
    return wrapper

@mayuscula
def saludar(name):
    return f"hola {name}"

print(saludar("william"))

print("=======================")

def w(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
w(1,2,3,4,"ole",name="waldro", apellido="perez",number=2234,)

print("=======================")

import time

def medir_tiempo(func):
    def wrapper():
        inicio = time.time()
        resultado = func()
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def proceso_lento():
    time.sleep(1)
    print("Proceso terminado")

proceso_lento()

print("=======================")

