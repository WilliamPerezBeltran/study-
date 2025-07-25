from datetime import datetime

def not_during_the_night(func):
	def wrapper():
		if 7 <= datetime.now().hour < 22:
			func()
		else:
			pass # hush, the neighbrs aare asleep
	return wrapper

def say_whee():
	print("wheee")

say_whee = not_during_the_night(say_whee)

print say_whee()