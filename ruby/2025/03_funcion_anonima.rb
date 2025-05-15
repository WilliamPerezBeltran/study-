asdf = lambda{|x| "hey #{x}"}

puts asdf.call("william")

saludo = ->(x){"hey #{x}"}
puts saludo.call("oscar") 
puts "================"

saludo = Proc.new{|x| "hey #{x}"}
puts saludo.call("rasta")

doble = ->(x){x*x}
dobles = [1,2,3,4,5].map(&doble)
puts dobles.inspect
