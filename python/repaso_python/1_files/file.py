import sys 
import pdb 

def copyfile(filename):
	print 'entro por aca'
	f = open(filename,'rU')
	text = f.read()
	print text
	f_write = open('newFile','w+')
	f_write.write(text)
	# f.close()
	# f_write.close()
def main():
	try:
		args = sys.argv[1:]
		# pdb.set_trace()
		copyfile(args[0])
	except Exception as e:
		print 'give a file in the console '

if __name__ == '__main__':
	main()