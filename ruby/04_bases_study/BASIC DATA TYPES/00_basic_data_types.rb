puts 1+1

puts 2*2*3
puts 3**2

puts 8%2
puts 9%2
puts 5/2
puts 5.0/2
puts 5/2.0
puts 23.to_f
puts 23.25.to_i

puts 6.even?
puts 7.even?

puts 6.odd?
puts 7.odd?

puts "welcome " +"to " +"paradise "
puts "welcome " <<"to " <<"paradise "
puts "Welcome ".concat("to ").concat("paradise") 

puts "hello"[0]
puts "hello"[0..4]
puts "hello"[0,4]
puts "hello"[-1]
puts "hello"[-3]


puts "programming"[-3]
puts "programming"[-1]
puts "programming"[0,5]
puts "programming"[0..5]

name  = "bla"

puts "la vida de #{name}"

puts "hello".capitalize #=> "Hello"
puts "hello".upcase #=> "Hello"
puts "HELLO".downcase #=> "Hello"
#include?

puts "hello".include?("lo")  #=> true

puts "hello".include?("z")   #=> false
puts "hello".empty?
puts "hello".reverse
x = "hello world".split
puts x[0]
puts x[1]
puts x.class
puts "hello".split("")


puts " hello, world   ".strip  #=> "hello, world"

puts "he77o".sub("7", "l")           #=> "hel7o"

puts "he77o".gsub("7", "l")          #=> "hello"

puts "hello".insert(-1, " dude")     #=> "hello dude"

puts "hello world".delete("l")       #=> "heo word"

puts "!".prepend("hello, ", "world") #=> "hello, world!"


puts "    william fsfl    flsfaf         ".strip
puts "he77o".sub("7", "l")           #=> "hel7o"
puts "wiill".sub("i", "A")           #=> "hel7o"
puts "wiiilll".gsub("i", "a") 

puts "???".prepend("hola ", "array")


puts 5.to_s        #=> "5"

puts nil.to_s      #=> ""

puts :symbol.to_s  #=> "symbol"

puts "string".object_id
puts "string".object_id
puts "string".object_id
puts "string".object_id

puts "string" == "string"  #=> true

puts "string".object_id == "string".object_id  #=> false

puts :symbol.object_id == :symbol.object_id    #=> true
puts :my_symbol

:my_symbol = "blaaaaaaaaaaaaaa"
puts :my_symbol