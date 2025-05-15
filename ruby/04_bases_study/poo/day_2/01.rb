

class Box
	attr_accessor :width, :height 
	@@count = 0
	def initialize(w,h)
		@width, @height = w,h
		@@count +=1
	end

	def self.printCount
		puts "box is #{@@count}"		
	end

	def to_s
		"(w:#{@width}, h:#{@height})"		
	end
end


b = Box.new(23,45)
a = Box.new(23,45)
s = Box.new(23,45)
f = Box.new(23,45)

puts b.width
puts b.height

b.width = 66
b.width = 22 

puts b.width
puts b.height
puts b.to_s

Box.printCount

