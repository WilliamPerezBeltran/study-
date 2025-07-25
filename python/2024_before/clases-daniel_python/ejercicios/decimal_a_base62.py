import sys 

def base10_to_base62(num):
	alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	array_shortener = []
	resultado = ''

	while num>0:
		array_shortener.append(num%62)
		num = num//62

	for x in reversed(array_shortener):
		resultado+=alphabet[x]

	return resultado
#54437310210532555530946764694913124100







def main():
	arg = sys.argv[1:]
	print(base10_to_base62(int(arg[0])))

if __name__=='__main__':
	main()




