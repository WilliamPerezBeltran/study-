nombre = "asdf"
edad = 30
pi = 3.14
activo = true

puts "==="
if edad >= 18
  puts "eres mayor de edad"
elsif edad == 20
  puts "tiene 20"
else
  puts "eres menor de edad"
end


puts "==="
for i in 1..5
  puts i
end

i=0
while i<3
  puts i
  i += 1
end
puts "==="
def saludar name
  puts "su nombre#{name}"
end


saludar("oscar")


puts "==="
class Persona 
  attr_accessor :nombre
  attr_reader
  def initialize(nombre)
    @nombre = nombre
  end

  def saludar
    puts "ole #{@nombre}"
  end
end


persona = Persona.new("william")

puts persona.saludar 
puts persona.nombre 
puts persona.nombre = "oscar"

puts persona.nombre 



