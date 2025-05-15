module MyModule
	MAX = 34
	def method_one
		puts "method_one"		
	end

	def method_two
		puts "method_two"		
	end

	class Box
	end
end


# Para acceder a las clases y constantes escribes el nombre del módulo, 
# seguido de :: (doble dos puntos), seguido del nombre de la clase o la constante. Por ejemplo:
puts MyModule::MAX
puts MyModule::Box.new

# A los métodos que están definidos en un módulo no los podemos acceder directamente, 
# tenemos que mezclar el módulo dentro de una clase.

class Person
	include MyModule 
end

p = Person.new
p.method_two
p.method_one

# =========================================================================

# Esto va a incluir todos los métodos de MyModule dentro de Person, 
# así que podemos llamar los métodos method_one y method_two (que definimos dentro del módulo MyModule 
# en la sección anterior) sobre instancias de Person.

# Otra ventaja de incluir (o mezclar) un módulo dentro de una clase 
# es que podemos acceder a las clases y las constantes que están definidas dentro del módulo directamente:


class Person
	include MyModule

	def initialize
		puts MAX
		puts Box.new	 	
	 end 
end

p1 = Person.new
p1.method_two
p1.method_one