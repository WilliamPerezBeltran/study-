require 'pry'

class SelectPatternTest 

  def test_pick_even_numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = []
    numbers.each do |number|
      evens << number if number.even?
    end
    evens
    # assert_equal [2, 4, 6, 8, 10], evens
  end

  def test_pick_odd_numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odds = []
    numbers.each do |number|
      # binding.pry()
      odds<<number if number%2==1
      # Your code goes here
    end
    odds
    # assert_equal [1, 3, 5, 7, 9], odds
  end

  def test_pick_words_with_three_letters
    words = ["pill", "bad", "finger", "cat", "blue", "dog", "table", "red"]
    selected = []
    words.each do  |item|
      selected<<item if item.length == 3
    end
    selected
    # Your code goes here
    # assert_equal ["bad", "cat", "dog", "red"], selected
  end

  def test_pick_words_with_more_than_three_letters
    words = ["pill", "bad", "finger", "cat", "blue", "dog", "table", "red"]
    selected = Array.new
    # selected = []
    words.each do |word|
      selected<<word if word.length >= 4 
    end 
    selected
    # Your code goes here
    # assert_equal ["pill", "finger", "blue", "table"], selected
  end

  def test_pick_words_ending_in_e
    words = ["are", "you", "strike", "thinking", "belt", "piece", "warble", "sing", "pipe"]
    selected = Array.new
    # Your code goes here
    words.each do |item|
      selected<<item if item[item.length-1] == "e"
    end 
    selected
    # assert_equal ["are", "strike", "piece", "warble", "pipe"], selected
  end

  def test_pick_words_ending_in_ing
    words = ["bring", "finger", "drought", "singing", "bingo", "purposeful"]
    selected = []
    words.each do |word|
      selected<< word if word[word.length-3,word.length-1] == "ing"
    end
    selected
    # assert_equal ["bring", "singing"], selected
  end

  def test_pick_words_containing_e
    words = ["four", "red", "five", "blue", "pizza", "purple"]
    selected = Array.new
    words.each do |item |
      selected<<item if item.include?("e")
    end 
    selected
    # assert_equal ["red", "five", "blue", "purple"], selected
  end

  def test_pick_dinosaurs
    animals = ["tyrannosaurus", "narwhal", "eel", "achillesaurus", "qingxiusaurus"]
    dinosaurs = []

    animals.each do |item |
      dinosaurs<< item if item[item.length-4,item.length-1] == "aurus"
      # dinosaurs<< item if aurus.includes("aurus")
    end 
    # assert_equal ["tyrannosaurus", "achillesaurus", "qingxiusaurus"], dinosaurs
  end

  def test_pick_floats
    numbers = [3, 1.4, 3.5, 2, 4.9, 9.1, 8.0]
    floats = []
    numbers.each do |item|
      floats<<item if item.class == Float 
      end 
      floats
  end

  def test_pick_arrays
    elements = ["CAT", ["dog"], 23, [56, 3, 8], "AIMLESS", 43, "butter"]
    arrays = []
    elements.each do |item|
      # if item.class == Array then arrays.push(item) end 
      arrays<<item if item.is_a?(Array)
    end 
    arrays

  end

  def test_pick_hashes
    elements = ["cat", {:dog=>"fido"}, 23, {:stuff=>"things"}, "aimless", 43]
    hashes =[]
    # binding.pry()
    # elements.each{|item| hashes<<item if item.is_a?(Hash)}
    elements.each do |item|
      hashes<<item if item.class == Hash
    end 
    hashes
  end
end