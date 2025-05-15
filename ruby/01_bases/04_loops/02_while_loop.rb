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