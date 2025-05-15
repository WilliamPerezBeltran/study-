require 'pry'

puts """

Ruby tiene un atajo para no tener que escribir siempre el getter 
y setter de todos los atributos, el attr_accessor. El siguiente 
código es equivalente al anterior:

Si no quieres que el atributo pueda ser modificado utiliza attr_reader 
en vez de attr_accessor.

Si no quieres que el atributo pueda ser leído utiliza attr_writer 
en vez de attr_accessor.

attr_accessor
attr_reader
attr_writer

"""

# class
class Person
  attr_accessor :name
  def initialize(name)
    @name = name
  end
  def greet(other_person_name)
    "Hello #{other_person_name}, my name is #{@name}"
  end
end

#object
person = Person.new("jhon")
binding.pry