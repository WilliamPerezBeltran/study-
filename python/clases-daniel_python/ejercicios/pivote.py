a=[-56,1,3,25,6,3,25,5,35,3,53,9]

pivote = True
for n in a:
	if pivote:
		menor = n
		pivote = False
	elif n < menor:
		menor = n
print(menor)


