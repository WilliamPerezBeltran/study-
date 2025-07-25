def revisar(func):
    def otra_funcion(a,b):
        # revisar si esta dividiendo entre cero
        if(b == 0):
            print("no puedes dividir por cero")
            return 
        resultado = func(a,b)
        return resultado
    #retorna otra_funcion para ejecutar func 
    return otra_funcion 
     
@revisar
def division(a,b):
    return a/b

# definir una variable con el mismo nombre de nuestra funcion 
# asignar a la variable definida la funcion revisar y enviarle como parametro revisar (la funcion definida)
# con esto se agrega a una nuestra funcion original el hecho de que no se puede dividir entre cero

# division = revisar(division)


# print(division(10,2))
resultado =  division(10,0)
print(resultado)