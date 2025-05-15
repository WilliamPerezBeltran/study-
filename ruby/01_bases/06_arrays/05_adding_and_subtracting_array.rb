a = [1, 2, 3]
b = [3, 4, 5]

a + b         #=> [1, 2, 3, 3, 4, 5]
a.concat(b)   #=> [1, 2, 3, 3, 4, 5]

puts "----"

puts  """
To find the difference between two arrays, you can subtract them using -. 
This method returns a copy of the first array, removing any elements that 
appear in the second array.
"""

[1, 1, 1, 2, 2, 3, 4] - [1, 4]  #=> [2, 2, 3]