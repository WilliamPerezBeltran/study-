

require 'date'
require 'pp'
require 'pry'
class ElectricityReadingGenerator
	def generate(hours)
		now = DateTime.now
		one_hour = Rational(1,24)
		now_reverse_time = now

		(0..hours).map do |n|
			puts now-= one_hour
			{
				# 'time' => (now).to_s,
				'time_converter' => DateTime.iso8601((now).to_s).to_time,
				'reading' =>"----------------------------"
				# 'reading' =>rand(0.0..0.5)
			}

		end 
		

	end
end

a = ElectricityReadingGenerator.new
pp a.generate(24*10)

# binding.pry



require 'date'
require 'pp'
require 'pry'
class ElectricityReadingGenerator
	def generate(hours)
		now = DateTime.now
		one_hour = Rational(1,24)

		(0..hours).map do |n|
			{
				# 'time' => (now).to_s,
				'time_converter' => DateTime.iso8601((now-(one_hour*n)).to_s).to_time,
				'reading' =>"----------------------------"
				# 'reading' =>rand(0.0..0.5)
			}

		end 
		

	end
end

a = ElectricityReadingGenerator.new
pp a.generate(24*10)

# binding.pry


