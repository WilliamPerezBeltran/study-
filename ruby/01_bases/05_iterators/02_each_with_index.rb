
# example 1
names = ['Bob', 'Joe', 'Steve', 'Janice', 'Susan', 'Helen']
names.each_with_index{|val,index| puts "#{index} => #{val}"}
 puts "----"
# example 2 A each block 
names.each_with_index do |val,index|
	puts "#{index} => #{val}"
end

