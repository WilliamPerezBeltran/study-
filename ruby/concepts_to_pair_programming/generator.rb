require 'date'
require 'pp'
require 'pry'

class ElectricityReadingsGenerator
  def generator(number)
    now = DateTime.now
    one_second = Rational(1, 24 * 60 * 60)
    (0..number-1).map do |n|
      { 'time' =>(now - (n*one_second)).to_s, 'readings' => rand(0.5..1.5) }
    end
  end

  def generator_per_hour(hours)
    now = DateTime.now
    one_hour = Rational(1, 24)

    (0..hours).map do |hour|
      { 'time' => (now - (one_hour * hour)).to_s, 'readings' => rand(0.1..5.0) }
    end
  end
end
