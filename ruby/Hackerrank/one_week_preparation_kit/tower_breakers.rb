require 'pry'
require 'json'
require 'stringio'



def towerBreakers(n, m)
return m == 1 ? '2' : n % 2 == 0 ? 2 : 1;

end


p timeConversion("12:01:00AM") # => Return '00:01:00'.

