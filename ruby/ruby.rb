a = {b:5}
b = {b:5}
a.merge!(b)
puts a


person = {name:"william", age:234, city:"bogota", status:"single" }
puts person 
person.each{|key, value| puts "#{key} #{value}"}



def contar_palabras(frase)
  new_hash = Hash.new(0)
  frase.split(" ").each do |x|
    new_hash[x] += 1
  end
  new_hash
end

puts contar_palabras("hola mundo hola")
# => {"hola"=>2, "mundo"=>1}

def seleccionar(product)
new_hash = Hash.new()
product.each do |key,value|
  if value > 100
    new_hash[key] = value
  end
end
  new_hash
end


productos = {
  laptop: 1200,
  mouse: 25,
  teclado: 70,
  monitor: 250
}
 puts seleccionar(productos)
# Resultado esperado:
# {:laptop=>1200, :monitor=>250}



puts productos.select{|_,value| value > 100}
