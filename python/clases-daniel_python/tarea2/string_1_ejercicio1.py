
def carros(num):
	resultado = num
	if num >= 10:
		resultado = 'many'
	else:
		resultado = num

	return resultado

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print("%s got: %s expected: %s"%(prefix, repr(got), repr(expected))) 

def main():
	test(carros(3),3)
	test(carros(23),'many')
	
if __name__=="__main__":
	main()