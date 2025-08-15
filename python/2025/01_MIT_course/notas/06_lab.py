
def mult_iter(a,b):
    i = b 
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(2,5))


def mult(a, b):
	if b == 1:
		return a
	else:
		return a + mult(a, b-1)


print(mult(3,34))

print("~~~~~~~~~ dict ~~~~~~~~~ ")

d1 = {"a": 1, "b": 2}
b = dict(a=1,b=2)
d3 = {}
print(d1)
print(d1["a"])
print(d1.get("a"))
print(d1.get("c",None)) # si no existe returna None 

d1["a"] = 10 
print(d1)

print(b)
print(b)
valor = b.pop("b")
print(valor) 
b["z"] = 234
print(b)
c = b 
print(f"b: {b}")
print(f"c: {c}")
b.clear()
print(f"c: {c}")

asdf = d1.copy()
print(asdf)
asdf["z"] = 100 
print(asdf)
print(d1)

d2 = dict(a=1, b=2)

for x in d1:
    print(x)

for x,y in d1.items():
    print(x,y)

for x in d1:
    if "a" in x:
        print(True) 

cuadrados = {x: x**2 for x in range(5)}
print(cuadrados )





















