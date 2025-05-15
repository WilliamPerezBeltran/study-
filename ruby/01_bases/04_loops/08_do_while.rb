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