
def decorador(func):
    def before_action():
        print("before_action")

    def after_action():
        print("after_action")

    def nueva_funcion(*args, **kwargs):
        print("vamos a ejecutar la funcion")
        resultado = func(*args, **kwargs)
        print("se ejecuto la funcion")
        return resultado
    return nueva_funcion

@decorador
def saluda():
    print("hola mundo")

@decorador
def suma(num_uno, num_dos):
    return num_uno + num_dos

resultado = suma(15,87)  
print(resultado)