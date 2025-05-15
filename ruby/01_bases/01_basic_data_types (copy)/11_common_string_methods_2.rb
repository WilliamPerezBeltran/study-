# find the first caracter and replace it with the second argument given 
puts "he77o".sub("7", "l")           #=> "hel7o"
puts "rubyy".sub("y","_")
puts "------------------------------------"


#Returns a copy of str with all occurrences of 
# pattern substituted for the second argument.
puts "he77o".gsub("7", "l")      
puts "rubyy".gsub("y","_")    #=> "hello"
puts "------------------------------------"

puts "hello".insert(-1, " dude")     #=> "hello dude"
puts "ruby".insert(0, "learn ")     #=> "hello dude"
puts "ruby".insert(2, "learn")     #=> "hello dude"
puts "------------------------------------"

# return an array of its elements
puts "hello".split("")               #=> ["h", "e", "l", "l", "o"]
puts "------------------------------------"

puts "!".prepend("hello, ", "world") #=> "hello, world!"
puts " end".prepend("hi", " ruby") #=> "hello, world!"