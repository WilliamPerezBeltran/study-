require 'pry'
class Name
	@@people_count = 0
	def initialize
		@@people_count += 1
	end
	def self.people_count
		@@people_count
	end
end

person1 = Name.new()
person2 = Name.new()
person3 = Name.new()
person4 = Name.new()
person5 = Name.new()
Name.people_count # => 5

binding.pry