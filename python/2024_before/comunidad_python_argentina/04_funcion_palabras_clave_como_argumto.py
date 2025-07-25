def loro(tension, estado="muerto", accion="explotar", tipo="Azul Nordico"):
    print("-- Este loro no va a", accion, end=" ")
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")


loro("252", "VIVO VIVO")
# LO DE ARRIBA ES LO MISMO QUE LO DE ABAJO
# VA DAR EL MISMO RESULTADO
loro("252", estado="VIVO VIVO")


print("*************")


def fun(*will):
    return "".join(will)


fun("a", "d", "b")
# 'adb'
def fun(*will):
    print(will)


fun("a", "d", "b")
# ('a', 'd', 'b')
def fun(*will):
    print(type(will))


fun("a", "d", "b")
# <class 'tuple'>


def fun(*will):
    print(will[0])
    print(will[1])


fun("a", "d", "b")

print("*************")


def fun1(*args, sep="/"):
    return sep.join(args)


print(fun1("fisica", "matematicas", "programacion"))
