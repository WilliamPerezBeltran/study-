


a = [1,2,4,4,36,3,6,4,6,33,2,6,7,-89]
a = [3434,2,4,4,36,3,6,4,6,33,2,6,7,-89]
a = [98,2,4,4,36,3,6,4,6,33,2,6,7,-89]
verdad=True
for n in a:
	if verdad:
		menor=n
		verdad=False
	elif n<menor:
		menor=n
print(menor)

menor = 1
verdad = False
2 < 1 falso
4 < 1 falso
-89 < 1
menor = -89
