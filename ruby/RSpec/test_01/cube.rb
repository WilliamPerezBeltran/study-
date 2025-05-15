class Cube
	attr_reader :height, :width, :depth
	def initialize(args)
		@height = args[:height] || args[:y] || 1
		@width = args[:width] || args[:x] || 1
		@depth = args[:depth] || args[:z] || 1
	end
	def volume
		height * width * depth
	end
end