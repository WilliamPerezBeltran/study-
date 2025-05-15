require "./math"
include MathExample
# there two way to access the method 

p MathExample.sum(2,3)
p MathExample::sum(2,3)

class Calculus
	include MathExample
	include MathExample::Cryptography
	attr_accessor :square,:triangle,:rhomboid,:rectangle

	def initialize(square,triangle,rhomboid,rectangle)
		@square = square 
		@triangle = triangle 
		@rhomboid = rhomboid 
		@rectangle = rectangle 
	end
	def sin(angle)
		Math.sin(angle) 
	end
end

cal = Calculus.new("square","triangle","rhomboid","rectangle")
p cal.sin(23)
p cal.sum(15,5)
p cal.res(15,5)
p cal.mul(15,5)
p cal.div(15,5)
p cal.square
