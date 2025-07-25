# (x^m + y^n)^k 
# (2^3 + 3^3)^2
# (8+27)^2 
# (35)^2



def math_form():
	x = int(input("dame el x "))
	m = int(input("dame el m "))
	y = int(input("dame el y "))
	n = int(input("dame el n "))
	k = int(input("dame el k "))

	acconmu_x = 1
	for a in range(m):
		acconmu_x = acconmu_x * x

	acconmu_y = 1
	for b in range(n):
		acconmu_y*=y

	result_sum = acconmu_x + acconmu_y

	acconmu_k = 1

	for c in range(k):
		acconmu_k*=result_sum

	return acconmu_k

def main():
	print(math_form())

if __name__=='__main__':
	main()
