import sys 

def main():
	print if_statement(speed, mood)

def if_statment(speed,mood):
	if speed >= 80:
		print 'do something'
		if mood == 'terrible' or speed > 100:
			print 'do something'
		elif mood == 'bad' or speed >= 90:
			print 'i am going to have to writeyou a ticket'
			write_ticket()
		else:
			print "Let's try to keep it under 80 ok?"

	return ''

if __name__ == '__main__':
	main()