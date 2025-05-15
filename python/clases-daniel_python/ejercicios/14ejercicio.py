#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

#0 + 1 = 1
#1 + 1 = 2
#2 + 1 = 3
#3 + 2 = 5
#5 + 3 = 8

# comm-section + tab





# def fibonacci(n):
# 	p=0
# 	s=1
# 	while p<=n:
# 		print(p)
# 		temp_p = p
# 		p = s
# 		s = temp_p +s




def fibonacci(n):
	p, s = 0, 1
	while p <= n:
		print(p,end=" ")
		p, s = s, p+s
		

def main():
	fibonacci(100)

if __name__ == '__main__':
	main()
