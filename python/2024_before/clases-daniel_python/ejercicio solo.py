#!/usr/bin/python -tt
# coding=utf-8

def prueba(a,b):
	if a==b:
		print ("esta correcto")
	else:
		print ("esta incorrecto")

def carro(a):
	if a>=10:
		r=many
	else:
		r=a
	return r

def extremos(a):
	if len(a)<2:
		print("no se puede")
		break
	else:
		i=a[0:2]
		f=a[-2:]
	return i+f

def ocurrencia(a):
	f=a[1:]
	return a[0:1] + f.replace(a[0:1],"☺")

def combinar(c,d):
	if len(c)>=2 and len(d)>=2:
		c_inicio = c[0:2]
		c_final = c[2:]
		d_inicio = d[0:2]
		d_final = d[2:]
		return "%s %s"%(d_inicio + c_final , c_inicio + d_final)

	else:
		print ("muy corto")
		break

"""
coloque los valores a probar que quiera
"""
def main():
	prueba(carro(),)
	prueba(extremos(),)
	prueba(ocurrencia(),)
	prueba(combinar(),)

if __name__ == '__main__':
  main()
