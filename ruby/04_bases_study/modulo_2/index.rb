module MyModule
  MAX_CONNECTIONS = 5

  def method_one
  end

  def method_two
  	puts "method_two"
  end

  class ThingOne
  end

  class ThingTwo
  end
end


puts MyModule::MAX_CONNECTIONS # Imprime 5

MyModule::ThingOne.new # Crea una instancia de la clase


class Person
  include MyModule

  def initialize
    puts MAX_CONNECTIONS # no hay necesidad de agregar el prefijo MyModule::
    ThingOne.new # no hay necesidad de agregar el prefijo MyModule::
  end
end

p = Person.new
puts p.method_two  # imprime method_two (definido en modulo MyModule)