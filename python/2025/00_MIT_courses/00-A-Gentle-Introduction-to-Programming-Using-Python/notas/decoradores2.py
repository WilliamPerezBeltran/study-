# ======================= definicion real =======================

def mi_decorador(funcion_original):
    def nueva_funcion():
        print("ANTES de ejecutar la funcion")
        funcion_original()
        print("DESPUÉS de ejecutar la funcion")
    return nueva_funcion 

def saludar():
    print("saludar")

# aplicamos el decorador manualmente

salud = mi_decorador(saludar)

salud()

# ======================= definicion real =======================
print(" ======================= definicion real =======================")


def decorador(func):
    def mejorar_funcion():
        print("1")
        func()
        print("2")
    return mejorar_funcion

def say_hello():
    print("hello")

say_hello = decorador(say_hello)

say_hello()

print(" ==============================================")


def decorador(func):
    def wrapper():
        print("1")
        func()
        print("2")
    return wrapper

@decorador
def hi():
    print("hi")

hi()
print(" =======================  =======================")

@decorator
def salud():
    print("salud")

# sonlo mismo la funcion de arriba y la funcion de abajo 
# hacen lo mismo 


salud = decorator(salud)
