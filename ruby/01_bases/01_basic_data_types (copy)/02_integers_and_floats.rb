=begin
Integers and Floats
There are two main types of numbers in Ruby. 
Integers are whole numbers, such as 10. 
Floats are numbers that contain a decimal point, 
such as 10.5, 10.0, or 0.25.

It’s important to keep in mind that when doing 
arithmetic with two integers in Ruby, the result 
will always be an integer.
=end

puts 17/5 #=> 3, not 3.4

# To obtain an accurate answer, just replace one of the integers in the expression with a float.

puts 17/5.0 #=> 3.4