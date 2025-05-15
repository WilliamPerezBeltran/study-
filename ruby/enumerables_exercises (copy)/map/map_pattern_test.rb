require 'pry'

class MapPatternTest 

  def test_capitalize
    names = ["alice", "bob", "charlie"]
    capitalized_names = []
    names.each do |name|
      capitalized_names << name.capitalize
    end
    capitalized_names
    # assert_equal ["Alice", "Bob", "Charlie"], capitalized_names
  end

  def test_doubles
  	numbers = [1,2,3,4,5]
  	doubles = []

  	numbers.each do  |n| 
  		doubles<<n*2
  	end
  	 # assert_equal [2, 4, 6, 8, 10], doubles
  	doubles
  end

  def test_squares
    numbers = [1, 2, 3, 4, 5]
    squares = []
    numbers.each do |number| 
      squares.push(number**2)
    end
    squares
    # assert_equal [1, 4, 9, 16, 25], squares
  end

  def test_lengths
    names = ["alice", "bob", "charlie", "david", "eve"]
    lengths = []
    # Your code goes here
    names.each{|item| lengths<<item.length }
    lengths
    # assert_equal [5, 3, 7, 5, 3], lengths
  end

   def test_normalize_zip_codes
    numbers = [234, 10, 9119, 38881]
    zip_codes = []

    numbers.each do |number|
    	# binding.pry

		zeros = 5 - number.to_s.length
		_zeros = ""
		if zeros < 5
			for x in (0..zeros-1)
			_zeros+="0" 
			end 
			_zeros<<number.to_s
			zip_codes<<_zeros
		else
			zip_codes<<number.to_s
		end
    end
    zip_codes
    # Your code goes here
    # assert_equal ["00234", "00010", "09119", "38881"], zip_codes
  end
  def test_normalize_zip_codes_1
    numbers = [234, 10, 9119, 38881]
    zip_codes = []

    numbers.each do |number|
    	zip_codes<<number.to_s.rjust(5,"0")
    end
    zip_codes
    # Your code goes here
    # assert_equal ["00234", "00010", "09119", "38881"], zip_codes
  end

   def test_backwards
    names = ["alice", "bob", "charlie", "david", "eve"]
    backwards = []
    names.each do |name|
      backwards << name.reverse
    end
    backwards
    # assert_equal ["ecila", "bob", "eilrahc", "divad", "eve"], backwards
  end

   def test_words_with_no_vowels
    words = ["green", "sheep", "travel", "least", "boat"]
    without_vowels = []
    words.each do |item|
    	without_vowels<<item.delete("aeiou")
    end
    without_vowels
    # Your code goes here
    # assert_equal ["grn", "shp", "trvl", "lst", "bt"], without_vowels
  end

end