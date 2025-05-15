puts """

The loop loop (say what????) is Ruby’s loop that just won’t quit. 
It’s an infinite loop that will keep going unless you specifically 
request for it to stop, using the break command. Most commonly, 
break is used with a condition, as illustrated in the example below.

"""

i = 0
loop do
	puts "i is #{i}"
	i+=1
	break if i == 10  
end
============================================================================
puts """

A while loop is similar to the loop loop except that you declare the 
condition that will break out of the loop up front.

"""

i = 0
while i < 10 do 
	puts "i is #{i}"
	i+=1
	break if i == 10  
end

while gets.chomp != "yes" do
	puts "go to run "	
end
============================================================================
puts """
The until loop is the opposite of the while loop. 
A while loop continues for as long as the condition is true, 
whereas an until loop continues for as long as the condition is false.
"""
# example 1
i = 0
until i > 10 do 
	puts "#{i > 10} => i is #{i} "
	i+=1
	break if i == 10  
end

# example 2


until gets.chomp == "yes" do
  puts "Will you go to prom with me?"
end
============================================================================
puts """
Ruby lets us use something called a range to define an interval. 
All we need to do is give Ruby the starting value, the ending value, 
and whether we want the range to be inclusive or exclusive.
"""
# example 1

(1..5) # => inclusive range: 1 2 3 4 5
(1...10) # => exluisiveinclusive range: 1 2 3 4 

# We can make ranges of letters, too!
('a'..'d')  # a, b, c, d



============================================================================
puts """
A for loop is used to iterate through a collection of information 
such as an array or range. These loops are useful if you need to do 
something a given number of times while also using an iterator.
"""
# example 1

puts "works with 'do' or without it"
for i in (0..5)
 puts "#{i} data"	
end

# example 2
for i in ('a'..'j') do
 puts "#{i} data"	
end

============================================================================
puts """
If you need to run a loop for a specified number of times, 
then look no further than the trusty #times loop. 
It works by iterating through a loop a specified number of 
times and even throws in the bonus of accessing the number it’s 
currently iterating through.
"""
# example 1
5.times do |number|
	puts number
end

============================================================================
puts """
A for loop is used to iterate through a collection of information 
such as an array or range. These loops are useful if you need to do 
something a given number of times while also using an iterator.
"""
# example 1
5.upto(10){|num| print "#{num} "}
puts ""
10.downto(5){|num| print "#{num} "}
puts ""
============================================================================
puts """
A do/while loop works in a similar way to a while loop;
if the condition is tru the block is repeted again  
"""
# example 1
loop do
	puts "what's your age"
	answer = gets.chomp.to_i
	if answer < 18
		break
	end
end 

# example 2
begin
  puts "gime your age "
  answer = gets.chomp.to_i
end while answer < 18
============================================================================

# example 1
names = ['Bob', 'Joe', 'Steve', 'Janice', 'Susan', 'Helen']
names.each{|name| puts name}

# example 2 A each block 
x = 1
names.each do |name|
 puts "#{x} => #{name}"
 x+=1
end

============================================================================

# example 1
names = ['Bob', 'Joe', 'Steve', 'Janice', 'Susan', 'Helen']
names.each_with_index{|val,index| puts "#{index} => #{val}"}
 puts "----"
# example 2 A each block 
names.each_with_index do |val,index|
	puts "#{index} => #{val}"
end

3
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================
============================================================================