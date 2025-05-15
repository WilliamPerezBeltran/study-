# abecedario=[]
# for num in range(97,123):
# 	letra=chr(num)
# 	abecedario.append(letra)

# print(abecedario)


abecedario=[]
abec=[ chr(ord('a')+num) for num in range(26)]
print(abec)
	
# [x for x in range(sdf)]




# contador= 0
# for x in range((3,9)):
# 	prin(contador, x)
# 	contador +=1


# for i, x in enumerate(range(3,9)):
# 	print(i,x) 










# valor suministrado 4
# resultado:  1 4 4 9 9 9 16 16 16 16 16
# repeticiones 1 2   3     4
# numero       1 2*2 3*3   4*4

print("***")


abecedario=[]
for num in range(97,123):
	letra=chr(num)
	abecedario.append(letra)

print(abecedario)


abec=[ chr(ord('a')+num) for num in range(26)]

for x in range(1,5):
	for y in range(x):
		print(x*x, end=" ")


[x*x for x in range(1,5) for y in range(x)]



for x in range(1,5):
	for y in range(x):
		for u in range(x):
			print(x*x, end=" ")

[x*x for x in range(1,5) for y in range(x) for u in range(x)]

		


nueva_lista = []
for x in range(3,20):
	if x > 10:
		nueva_lista.append(x)

print(nueva_lista) 

nueva_lista  = [x for x in range(3,20) if x >10]
[11, 12, 13, 14, 15, 16, 17, 18, 19]



lista=[]
for x in range(1,101):
	if x>=50:
		lista.append(x)
# print(lista)

c=[x for x in enumerate(range(1,15)) if x[1]>=5]
print(c)