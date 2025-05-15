require 'pry'
class Name
	attr_accessor :name, :random_number
	def initialize(name)
		@name = name
		@random_number = self.random 
	end
	def random
		rand 0..25
	end
end
name = Name.new("ruby")

binding.pry