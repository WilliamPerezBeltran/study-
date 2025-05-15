============================================
=begin

Let’s look at an example of this unexpected behavior, 
with two variables: desired_location, which is assigned to the string “Barcelona”,
 and johns_location, which is assigned to the desired_location variable. Both variables 
 are pointing to where “Barcelona” is stored in memory.

to understand the topic go to:

https://launchschool.com/blog/references-and-mutability-in-ruby
=end

============================================
# with gets.chomp you can capture the income data to the variable name 
name = gets.chomp
puts name 
============================================
# scope.rb

a = 5             # variable is initialized in the outer scope

3.times do |n|    # method invocation with a block
  puts a = 3           # is a accessible here, in an inner scope?
end
puts "--"
puts a

============================================
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
============================================
@@variable_de_clase =
@variable_de_instance=
$variable_global=
CONSTANTE =
============================================
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
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
age = 18
response = age < 17 ? "You still have your entire life ahead of you." : "You're all grown up."
puts response #=> "You're all grown up."
============================================
# example 1
age = 18
puts "Welcome to a life of debt." unless age < 17

unless age < 17
  puts "Down with that sort of thing."
else
  puts "Careful now!"
end



# example 2

puts "x is NOT 3" unless age == 3
============================================
if 10 < 2 || 5 < 6 #=> although the left expression is false, there is a party at Kevin's because the right expression returns true
  puts "Party at Kevin's!"
end

# This can also be written as
if 10 < 2 or 5 < 6
  puts "Party at Kevin's!"
end
============================================
if 1 < 2 && 5 < 6
  puts "Party at Kevin's!"
end


# This can also be written as
if 1 < 2 and 5 < 6
  puts "Party at Kevin's!"
end
============================================
if !false     #=> true

if !(10 < 5)  #=> truea
============================================
if statement_to_be_evaluated == true
  # do something awesome...
end

puts "---------------------------------"

if attack_by_land == true
  puts "release the goat"
else
  puts "release the shark"
end

puts "---------------------------------"

if attack_by_land == true
  puts "release the goat"
elsif attack_by_sea == true
  puts "release the shark"
else
  puts "release Kevin the octopus"
end
============================================
grade = 'F'

case grade
when 'A'
  puts "You're a genius"
  future_bank_account_balance += 5000000
when 'D'
  puts "Better luck next time"
  can_i_retire_soon = false
else
  puts "McDonald's is hiring!"
  fml = true
end

puts fml
============================================
note = "a"

did_i_pass = case note
	when 'a' then "string a"
	when 'b' then "string b"
	else "another string"
end
puts did_i_pass
============================================
grade = 'F'

case grade
when 'A'
  puts "You're a genius"
  future_bank_account_balance += 5000000
when 'D'
  puts "Better luck next time"
  can_i_retire_soon = false
else
  puts "McDonald's is hiring!"
  fml = true
end

puts fml
============================================
# example 1
puts "Hot diggity damn, 1 is less than 2" if 1 < 2

# example 2
x = 3

if x == 3 then puts "x is 3" end   

puts "x is 3" if x == 3
============================================

# <= (less than or equal to) returns true if the value on the left of the operator is smaller than or equal to the value on the right.
5 <= 5 #=> true
5 <= 7 #=> true


#eql? checks both the value type and the actual value it holds.
5.eql?(5.0) #=> false; although they are the same value, one is an integer and the other is a float
5.eql?(5)   #=> true

#equal? checks whether both values are the exact same object in memory. This can be slightly confusing because of the way computers store some values for efficiency. Two variables pointing to the same number will usually return true.
a = 5
b = 5
a.equal?(b) #=> true
# This expression is true because of the way computers store integers in memory. Although two different variables are holding the number 5, they point to the same object in memory. However, consider the next code example:


a = "hello"
b = "hello"
a.equal?(b) #=> false
# This happens because computers can’t store strings in the same efficient way they store numbers. 
# Although the values of the variables are the same, the computer has created two separate string objects in memory.
============================================
# <=> (spaceship operator) returns the following:

# -1 if the value on the left is less than the value on the right;
#  0 if the value on the left is equal to the value on the right; and
#  1 if the value on the left is greater than the value on the right.

5 <=> 10    #=> -1
10 <=> 10   #=> 0
10 <=> 5    #=> 1
# The spaceship operator is most commonly used in sorting funct
============================================
# example 1
age = 18
puts "Welcome to a life of debt." unless age < 17

unless age < 17
  puts "Down with that sort of thing."
else
  puts "Careful now!"
end



# example 2

puts "x is NOT 3" unless age == 3
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================
============================================