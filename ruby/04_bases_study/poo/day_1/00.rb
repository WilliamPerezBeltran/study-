require pry 
class Person 
	attr_accessor :name

	def initialize name
		@name = name
	end

	def greet name

		"atributo de la funcion: #{name} y atributo de instancia #{@name}"		
	end

	def hello name
		"hola #{name}"		
	end

	def call
		self.secret_method
	end

	def muchos name, *other
		puts "este es el name: #{name}"

		for x in other
			puts x
		end
			
	end



	
	private 
	def secret_method
		puts "este es un metodo privado"		
	end
end

p1 = Person.new("william")
puts p1.greet "oscar"
puts p1.hello("william")
puts p1.hello "william"
puts p1.call
puts p1.name
p1.name = "oleeeeeee"
puts p1.name
puts p1.muchos "william",1,2,3,4,5,6,7,8,9

