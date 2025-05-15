
class Box
	attr_accessor :width, :height 
	@@count = 0
	# constructor method
   def initialize(w,h)
      @width, @height = w, h
   end

	def self.printCount
		puts "box is #{@@count}"		
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
