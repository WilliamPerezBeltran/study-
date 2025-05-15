require "./math"
include MathExample

puts MathExample::sum 3,8

class Matematicas
	include MathExample

end

o =  Matematicas.new 

puts o.sum(3,6)