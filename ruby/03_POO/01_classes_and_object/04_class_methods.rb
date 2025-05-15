require 'pry'
class Name
	def self.my_class_method
		p "this is a method class"
	end
end
name = Name.my_class_method # => "this is a method class"
name1 = Name.new()
binding.pry