
"""

import sys 
n=int(input("deme un numero: "))
if n>20:
	print("no se puede")
	sys.exit(-1)
	
else:
	for i in range(1,n,2):
		print(i)


print("******")

multiplo=int(input("cual tabla de multiplicar quiere "))
for m in range(0,11):
	resultado=multiplo*m
	print("%d * %d = %d"%(multiplo,m,resultado))


"""
"""
print("***********")

entero=int(input("deme un numero "))
for x in range(1,entero+1):
	for a in range(x):
		print(x*x)

print("********")

"""
cantidad= int(input("cuantos numeros quiere colocar "))
num_selec=[]
for i in range(cantidad):
	num=int(input("diga los numeros que se usaran "))
	num_selec.append(num)
print (num_selec)

par=0
inpar=0
for n in num_selec:
	if n%2==0:
		par=par+1
	else:
		inpar=inpar+n

print("con la lista de numeros que coloco sabes que hay {} pares y que la suma de los impares da {}".format(par,inpar))