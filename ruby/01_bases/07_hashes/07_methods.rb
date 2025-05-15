# https://ruby-doc.org/core-3.1.2/Enumerable.html
a = { "Bob" => 42, "Steve" => 31, "Joe" => 19} 
#=> {"Bob"=>42, "Steve"=>31, "Joe"=>19}

p a.key?("Bob")
p a.key?("will")
c = a.select{|k,v| k == "Bob"}
p c
d = a.select{|k,v| (k == "Bob") || (v == 19) }
p d

p a.fetch("Bob")
p a.to_a
p a.keys
p a.values
p a