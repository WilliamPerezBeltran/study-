require_relative '../cube.rb'


RSpec.describe Cube do 
	it "calculate it's volume", :smoke => true do
		cube = Cube.new(x: 3, y: 4, z: 5)
		expect(cube.volume). to eq(60) 
	end
end