a = 5

3.times do |n|
	a = 3
	b = 5
end

puts a
# puts b #=> turn an error ,,,06_variable_scope_2.rb:9:in `<main>': undefined local variable or method `b' for main:Object (NameError)

# the result throw and error because the variable a is undefined 
# because was not declare before as a global variable.

# the variable b=5 is working in the scopet between block times 
# puts b


puts """
	NOTE:
	
	the for...do/end 
	code did not create a new inner scope, since for is part 
	of Ruby language and not a method invocation. When we use each, 
	times and other method invocations, followed by {} or do/end, 
	that's when a new block is created.

	the block is created when:
	1. When we use each, times and other method invocations,
	   followed by {} or do/end, 

 """
