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




 puts "=============================================="


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


 puts "=============================================="


class Box
	attr_accessor :width, :height 
	@@count = 0

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

 puts "=============================================="
 puts "=============================================="
 puts "=============================================="

class Box
   # constructor method
   def initialize(w,h)
      @width, @height = w, h
   end

   # instance method by default it is public
   def getArea
      getWidth() * getHeight
   end

   # define private accessor methods
   def getWidth
      @width
   end
   def getHeight
      @height
   end
   # make them private
   private :getWidth, :getHeight

   # instance method to print area
   def printArea
      @area = getWidth() * getHeight
      puts "Big box area is : #@area"
   end
   # make it protected
   protected :printArea
end

# create an object
box = Box.new(10, 20)

# call instance methods
a = box.getArea()
puts "Area of the box is : #{a}"

puts """
 		va enviar este error porque el metodo printArea es protected
Area of the box is : 200
test.rb:42: protected method `printArea' called for #
<Box:0xb7f11280 @height = 20, @width = 10> (NoMethodError)
\n
"""
# try to call protected or methods
box.printArea()
