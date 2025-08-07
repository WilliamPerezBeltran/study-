def mi_decorador(func):
    def wrapper():
        print("antes de ejecutar la fucnión")
        func()
    return wrapper

@mi_decorador
def saludar():
    print("ole")

saludar()

