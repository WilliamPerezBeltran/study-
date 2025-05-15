# POR SELECCIÓN
import random 
arr = []
for x in range(10):
	arr.append(random.randrange(10))

print(arr)
print("---")



for x in range(1,len(arr)):
	if arr[x] < arr[x-1]:
		for i in range(x,-1,-1):
			if i>0 and (arr[i] < arr[i-1]):
				aux = arr[i]
				arr[i] = arr[i-1]
				arr[i-1] = aux
				print(arr)

