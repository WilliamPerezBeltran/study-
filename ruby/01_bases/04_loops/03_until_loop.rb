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