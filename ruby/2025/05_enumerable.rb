puts "=====recorrer elementos ======"

[1,2,3,4].each do |num|
 print " #{num}"
end
puts ""

[1,2,3,4,5].each_with_index do |value, index|
  puts "index:#{index} value:#{value} "
end


puts "===== encontrar  ======"

numer = [10,20,30,40,50,60,70].find{|num| num >= 50}
numerr = [10,20,30,40,50,60,70].detect{|num| num >= 50}
puts numer.inspect
puts numerr.inspect
ole = [10,20,30,40,50,60,70].select{|num| num >= 50}
puts ole.inspect

ole_even = [1,2,3,4,5,6,7,8,9,10].select{|num| num.even?}
ole_odd = [1,2,3,4,5,6,7,8,9,10].select{|num| num.odd?}

puts ole_even.inspect
puts ole_odd.inspect
ole_reject = [1,2,3,4,5,6,7,8,9,10].reject{|num| num.even?}
puts ole_reject.inspect

puts "====="
a = [1,2,3,4,5,6,7,9,10].group_by{|x| x.even?}
puts a.inspect



personas = [
  { nombre: "Ana", edad: 20 },
  { nombre: "Luis", edad: 30 },
  { nombre: "Marta", edad: 20 }
]

por_edad = personas.group_by { |p| p[:edad] }
puts por_edad.inspect
