"""
TTT
"""
def validation():


	validation = True
	while validation:
		entrada = input("deme un numero ")
		if entrada.isdigit() == True:
			validation = False
	print(entrada)

	validation = True
	while validation:
		entrada1 = input("deme una palabra")
		if entrada1.isalpha():
			validation = False
	print(entrada1)

	validation = True
	while validation:
		try:
			entrada2 = int(input("deme un numero: "))
		except Exception as e: 
			print("Error al ingrear el dato ")
			print(e)
		else:
			validation = False
			print("gracias")

	
def main():
	validation()

if __name__=="__main__":
	main()