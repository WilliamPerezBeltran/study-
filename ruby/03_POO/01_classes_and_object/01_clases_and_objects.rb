require 'pry'
# class
class Person
	def initialize(name)
		@name = name
	end

	def greet(other_person_name)
		"Hello #{other_person_name}, my name is #{@name}"
	end

  # Método para que @name pueda ser leído desde afuera
  def name
  	@name
  end

  # Método para que @name pueda ser modificado desde afuera
  def name=(name)
  	@name = name
  end
end
#object
p person = Person.new("jhon")

p person.greet("george") # => Hello george my name is jhon 
p person.name # => jhon 
p person.name = "hotz" # => jhon 
p person.name  # => "hotz" 
binding.pry