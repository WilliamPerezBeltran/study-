arr = [1,2,3]

for i in arr do
	a = 5 
end 
puts a       # is it accessible here?

puts """
	the variable a is it accessible here?
	The answer is yes. The reason is because the for...do/end 
	code did not create a new inner scope, 	since for is part 
	of Ruby language and not a method invocation. When we use each, 
	times and other method invocations, 
	followed by {} or do/end, that's when a new block is created.
"""