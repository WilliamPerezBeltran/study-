class Box
	@@count = 0
	def initialize(w,h)
		@width, @height = w,h
		@@count +=1
	end

	def width
		@width
	end

	def height
		@height
	end

	def setWidth=(value)
		@width = value
	end

	def setHeight=(value)
		@height =value
	end

	def self.printCount
		puts "box is #{@@count}"
		
	end

	def to_s
		"(w:#{@width}, h:#{@height})"		
	end
end


b = Box.new(23,45)

puts b.width
puts b.height

b.setWidth = 66
b.setHeight = 22 

puts b.width
puts b.height
puts b.to_s

Box.printCount

