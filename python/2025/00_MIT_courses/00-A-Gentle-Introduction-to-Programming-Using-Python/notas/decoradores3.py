#1. Versión tradicional (sin @) 
def mi_decorador(message):
    def decorador(func):
        def nueva_funcion():
            print(f"mensaje enviado ANTES:{message} ") 
            func()
            print(f"mensaje enviado DESPUES:{message} ") 
        return nueva_funcion
    return decorador


def saludar():
    print("hi")

saludar = mi_decorador(" mi mensaje ")(saludar)
saludar()

print("===============================")


def deco(message):
    def decorador_(h):
        def improve_function(): 
            print(f"{message}")
            h()
            print(f"{message}")
        return improve_function
    return decorador_ 



@deco("trust the journey")
def h():
   print("ole") 

h()

print("===============================")

def funciontion(*args ,**kwargs):
    print(args)
    print(kwargs)

funciontion(1,2,3,4,name="william", number=2)


