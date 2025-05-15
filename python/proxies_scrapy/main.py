import sys
import pdb

def list_proxies():
	with open('./base_file_proxies.py') as f:
		text = f.read()
		array_proxies = text.split("\n")

	with open('execute_scrapy_with_proxie.txt','w') as f:
		scrapy_command = array_proxies[0]
		for data in array_proxies[1:]:
			line = "https_proxy='%s' %s \n" %(data,scrapy_command) 
			f.write(line)

def main():
	list_proxies()

if __name__== '__main__':
	main()
