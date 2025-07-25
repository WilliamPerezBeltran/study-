#!/usr/bin/python -tt
# coding=utf-8

"""

x=int(input("digite el numero para x "))
y=int(input("digite el numero para y "))
m=int(input("digite el numero para m "))
n=int(input("digite el numero para n "))
k=int(input("digite el numero para k "))

if x <= 7 and y <= 7 and m <= 7 and n <= 7 and k <= 7:
	resultado= (x**m + y**n)**k
	print ("el resultado de (x^m + y^n)^k es",resultado)
else:
	print("no se puede, alguno de los valores es mayor a 7")

print("-------------")

num=int(input("deme un numero "))
dim = num
for x in range(1,num+1):
	for y in range(x):
		print(dim)
	dim -= 1
"""
 # 5 4 4 3 3 3 2 2 2 2 1 1 1 1 1  n=5
#gr 1 1   1     1       1     


#1335555777777779999999999999999 n=5


n=int(input("deme un numero "))
for x in range(1,n+1):
	for y in range(x*2):
		print(x+2)

#122333444455555

#for a in range(num,0,-1):
#	for b in range(a):
#		print (a)

print("-------------")


print("-------------")

p=string(input("deme una palabra"))

pali=p[::-1]

if pali==p:
	print("si es palindromo")
else:
	print("no es palindromo")

