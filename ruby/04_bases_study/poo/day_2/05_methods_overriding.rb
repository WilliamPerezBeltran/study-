

# Methods Overriding
# Though you can add new functionality in a derived class, 
# but sometimes you would like to change the behavior of already
#  defined method in a parent class. You can do so simply by keeping 
#  	the method name same and overriding the functionality of the method as 
#  	shown below in the example −



class Box
	def initialize(w,h)
		@width, @height = w,h		
	end

	def get_area
		@width*@height
	end
end

class BigBox < Box
 	def get_area
 		@area = @width*@height
 		puts "area: #{@area}" 		
 	end
end


b =BigBox.new(23,34)
b.get_area