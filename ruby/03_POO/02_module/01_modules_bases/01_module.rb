# example 1
module Cream
	def cream?
		true
	end
end

class Cookie
	include Cream 
end

cookie = Cookie.new
p cookie.cream?

# example 2
module MyModule
	MAX_CONNECTIONS = 5
	def method_one
		"method_one of my module"
	end
	def method_two
		"method_two of my module"
	end
end

class Name
	include MyModule
end

p MyModule::MAX_CONNECTIONS

# to gets access to methods of module we need to instances the class
# to reach it . 
name = Name.new
p name.method_one
p name.method_two

