require 'date'

class ElectricityReadingsGenerator
  def generate(number)
    now = DateTime.now
    one_second = Rational(1, 24 * 60 * 60)
    
    (0..number-1).map do |n|
      {
        'time' => (now - n * one_second).to_s,
        'reading' => rand(0.5..1.5)
      }
    end
  end
end







# require 'date'

# class ElectricityReadingsGenerator
#  	def generate(number)
#  		now = DateTime.now
#  		one_second = Rational(1/24*60*60)



# 	# Basically, 1000 is used here just for converting seconds to milliseconds.
# 	# Number of seconds in a day = 24 * 60 * 60 = 86400 seconds.
# 	# 1 second = 1000 milliseconds.
# 	# So after calculating the expression, the result is in milliseconds.
# 	# days * 24 * 60 * 60 * 1000 = days * 86400000 ms


#     # Number of seconds in a day = 24 * 60 * 60 = 86400 seconds.

#  		(0..number-1).map do |n|
#  			{
#  				'time' => (now - n * one_second).to_s,
#  				 'reading' => rand(0.5..1.5)
#  			}
#  		end
 		
#  	end
# end

# ele =ElectricityReadingsGenerator.new
# resultado =  ele.generate 100


# # es un array 
# puts resultado.class
# puts resultado
# puts resultado[1]
# puts resultado[2]
# puts resultado[0]


# # [
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.4513283967421398}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.1663748667818332}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.2566636247956402}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.2303275765365091}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>0.8730605411842567}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>0.9905774508691987}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.120003933416804}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>0.8081299679574356}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>0.7938158627619054}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>0.606807315469696}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.0601316600844464}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.2145856391266792}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.1475674357718484}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.1217076086244795}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.2478823435567286}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>0.9617525426216486}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.4088641810907494}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.3742505870692674}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>0.8252085013723264}
# # 	{"time"=>"2021-10-20T11:37:20-05:00", "reading"=>1.0415330016188147}
# # ]