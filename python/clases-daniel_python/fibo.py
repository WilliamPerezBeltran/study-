# a = 0
# b = 1
# while b<10:
# 	print(b)
# 	a=b
# 	b=a+b



# a,b = 0,1
# while b<10:
# 	print(b)
# 	a,b = b,a+b


a,b = 0,1
while b<10:
	print(b)
	a = b
	b = a+b

def test_var_args(f_arg, *args):
    print("first normal arg:", f_arg)
    for arg in args:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

print(test_var_args)

print("****")
f = test_var_args
f(1,2,3,4,5) 