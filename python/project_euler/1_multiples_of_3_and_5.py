import pdb
import sys
"""
	If we list all the natural numbers below 10 that are 
	multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of 
	these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.
"""
def _1_multiples_3_and_5():
	sum_numbers = 0
	for number in range(1000):
		if number%3 == 0 or number%5 == 0:
			sum_numbers += number
	return sum_numbers

def _1_multiples_3_and_5_given_range(range_number):
	get_numbers = [number for number in range(range_number) if number%3 == 0 or number%5 == 0]
	return sum(get_numbers)

def test(got,expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = ' X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
	args = sys.argv[1:]
	if not args:
		print 'usage: 1_multiples_of_3_and_5.py {--withoutrange-default1000 | --given-specific-range [give numerical range] }'
		sys.exit(1)

	if args[0] == '--withoutrange-default1000':
		print 'range:',range(1000)
		print 'the sum is equal to : ', _1_multiples_3_and_5()
		test(_1_multiples_3_and_5(), 233168)
	elif args[0] == '--given-specific-range':
		try:
			range_number = args[1]
			print 'range:',range(int(range_number))
			print 'the sum is equal to : ', _1_multiples_3_and_5_given_range(int(range_number))
			test(_1_multiples_3_and_5_given_range(10), 23)
			test(_1_multiples_3_and_5_given_range(50), 543)
			test(_1_multiples_3_and_5_given_range(100), 2318)
			test(_1_multiples_3_and_5_given_range(150), 5175)
			test(_1_multiples_3_and_5_given_range(150), 5175)
			test(_1_multiples_3_and_5_given_range(500), 57918)

		except Exception as e:
			print 'please give a numerical range',e
	else: 
		print 'usage: 1_multiples_of_3_and_5.py {--withoutrange-default1000 | --given-specific-range [give numerical range] }'
		print 'try to give the correct arguments'


if __name__ == '__main__':
	main()