
# example 1
names = ['Bob', 'Joe', 'Steve', 'Janice', 'Susan', 'Helen']
names.each{|name| puts name}

# example 2 A each block 
x = 1
names.each do |name|
 puts "#{x} => #{name}"
 x+=1
end
