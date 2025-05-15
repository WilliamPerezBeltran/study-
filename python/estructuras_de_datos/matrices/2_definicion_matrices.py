
print("--------------por-posiciones---------------------------------------------------------------------")

matriz = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		print(matriz[i][j], end=" ")
	print()

print("--------------por-valores---------------------------------------------------------------------")


matriz = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for row in matriz:
	for element in row:
		print(element, end=" ")
	print()