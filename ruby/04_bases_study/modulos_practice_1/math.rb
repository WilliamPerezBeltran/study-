module MathExample
	def sum x,y
		x+y		
	end

	def res x,y
		x-y		
	end

	def mul x,y
		x*y		
	end

	def div x,y
		x/y		
	end

	class Cryptography
		attr_accessor :caesar,:scytale,:pigpen,:polyalphabetic

		def initialize(caesar,scytale,pigpen,polyalphabetic)
			@caesar = caesar
			@scytale = scytale 
			@pigpen = pigpen 
			@polyalphabetic = polyalphabetic 
		end
	end 
end