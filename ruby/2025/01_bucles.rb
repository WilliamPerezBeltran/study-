# bucles 


#while
i = 0
while(i <= 10 )
  i+=1
  puts i
end
puts "===="
ii = 0
until ii == 5
  puts ii
  ii+=1
end

puts "===="
for a in 1..3
  print a 
end
puts "\n"
puts "===="

[1,2,3,4,5].each do |x|
  puts x
end

puts "===="
3.times do |x|
  puts x
end
puts "===="
for a in 1..3
  print a 
end
puts "\n"
puts "\n"
puts "===="
for a in 1...3
  print a 
end
puts "\n"
puts "\n"

cuadrados = [1,2,3,54].map{|x| x*x}
puts cuadrados.inspect
