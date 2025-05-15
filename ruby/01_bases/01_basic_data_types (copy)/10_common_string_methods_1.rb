#capitalize
puts "ruby".capitalize # => Ruby

#include?
puts "ruby".include?("ub") #=> true 
puts "study".include?("y") #=> true 

#upcase
puts "ruby".upcase # => RUBY

#downcase
puts  "RUBY".downcase # => ruby

#empty?
puts "ruby".empty? # => false 
puts "".empty? # => true 

#length
puts "ruby".length #=> 4

#reverse
puts "ruby".reverse # => ybur
puts "******"

#split
# split devuelve un array 
variable_split = "hello world".split
puts  variable_split #=> ["hello", "world"]
puts  variable_split[0] #=> "hello"
puts  variable_split[1] #=> "world"
puts  "hello".split("") #=> #=> ["h", "e", "l", "l", "o"]

puts "******"
#strip
puts " hello, world   ".strip  #=> "hello, world"
