import time 
"""
Implement a decorator in Python that measures the execution time of a function.

"""
def mi_decorator(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion = func(*args, **kwargs) 
        final = time.time()
        print(f"Tiempo de ejecucion: {final-inicio:.4f} segundos ")
        return funcion 
    return wrapper

@mi_decorator
def ejemplo():
    for x in range(1_000_000):
        pass
    return "Terminado"

print(ejemplo())
