num_array = [1, 2, 3, 4, 5]
str_array = ["This", "is", "a", "small", "array"]

puts """
An array can also be created by calling the Array.new method. 
When you call this method, you can also include up to 2 optional 
arguments (initial size and default value):
"""

Array.new               #=> []
Array.new(3)            #=> [nil, nil, nil]
Array.new(3, "Hello")   #=> ["Hello", "Hello", "Hello"]
Array.new(3, Array.new) #=> [[], [], []]