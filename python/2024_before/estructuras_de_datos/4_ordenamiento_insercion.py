import pdb;
arr = [4,2,6,8,5,7,0]
print(arr)
for x in range(1,len(arr)):
	if arr[x] < arr[x-1]:
		for i in range(x,-1,-1):
			if i>0 and (arr[i] < arr[i-1]):
				aux = arr[i]
				arr[i] = arr[i-1]
				arr[i-1] = aux
				print(arr)

