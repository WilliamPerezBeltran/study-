3.times  do |x|
  puts x
end

puts "===="

3.times {|x| puts x}

def saludar(name)
  puts "hey walo #{name}"
  yield if block_given?
  puts "despues del yield"
end
saludar "willly"
saludar("ooscar") {puts "bloqueeeeeee"} 


def operar(x,y)
  yield(x,y)
end

ole = operar(1,2){|a,b| a+b}
puts ole 
