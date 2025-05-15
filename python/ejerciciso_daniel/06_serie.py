"""
averiguar cuantas veces esta una palabra en un texto


valor suministrado 5
resultado 1 22 333 55555 88888888
"""

import sys 
import pdb

def way_one_serie():
	buscar_palabra = input("deme la palabra a buscar ")
	texto = """
		Las ideas local que comunica un texto están contenidas en lo que se suele denominar «macroproposiciones», 
		unidades estructurales de nivel superior o global, que otorgan coherencia al texto constituyendo su hilo central, 
		el esqueleto estructural que cohesiona elementos lingüísticos formales de alto nivel, 
		como los títulos local y subtítulos, la secuencia de párrafos, etc. En contraste, las «microproposiciones» son los
		elementos coadyuvantes de la cohesión de un texto, pero a nivel más particular o local. 
		Esta distinción fue realizada por Teun van Dijk en 1980.1​

		El nivel local microestructural o local está asociado con el concepto de cohesión.
		Se refiere a uno de los fenómenos propios de la coherencia, el de las relaciones 
		particulares y locales que se dan entre elementos lingüísticos, tanto los que remiten unos 
		a otros como los que tienen la función de conectar y organizar. También es un conjunto de 
		oraciones agrupadas en párrafos que habla de un tema determinado.
	"""

	acco = 0
	for x in texto.split(' '):
	 if x.lower() == buscar_palabra:
	  acco+=1
	
	return acco





def main():
	print(way_one_serie())

if __name__=='__main__':
	main()
