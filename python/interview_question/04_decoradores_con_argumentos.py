def decorador(is_valid= True):

    def _decorador(func):
        def before_action():
            print("before_action")

        def after_action():
            print("after_action")

        def nueva_funcion(*args, **kwargs):
            if is_valid:
                before_action()
            resultado = func(*args, **kwargs) #la ejecuto
            after_action()
            return resultado
        return nueva_funcion

    return _decorador


@decorador( )
def suma(num_uno, num_dos):
    return num_uno + num_dos

resultado = suma(15,87)  
print(resultado)
