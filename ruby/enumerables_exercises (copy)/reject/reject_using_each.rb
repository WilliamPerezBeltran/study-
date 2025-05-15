require "pry"

class RejectUsingEach

  def test_remove_zeros
    numbers = [2, 93, 7, 0, 0, 1, 0, 31, 0, 368]
    filtered = []
    numbers.each do |number|
      filtered << number unless number.zero?
    end
    filtered
  end

  def test_remove_vowels
    letters = ["a", "l", "l", " ", "y", "o", "u", "r", " ", "b", "a", "s", "e", " ", "a", "r", "e", " ", "b", "e", "l", "o", "n", "g", " ", "t", "o", " ", "u", "s"]
    remaining = []
    letters.each do |letter|
      remaining<< letter unless ["a","e","i","o","u"].include?(letter)
    end
    remaining
  end

  def test_remove_numbers_divisible_by_3
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    remaining = []
    numbers.each do |number|
      remaining<< number unless number%3 ==0
    end
    remaining
  end

  def test_remove_words_with_more_than_three_letters
    words = ["pill", "bad", "finger", "cat", "blue", "dog", "table", "red"]
    selected = []
    words.each do |item|
      selected << item unless item.length > 3 
    end
    selected
  end

  def test_remove_words_ending_in_e
    words = ["are", "you", "strike", "thinking", "belt", "piece", "warble", "sing", "pipe"]
    selected = []
    words.each{|item| selected<<item unless item.end_with?("e") }
    selected
  end

  def test_remove_words_ending_in_ing
    words = ["bring", "finger", "drought", "singing", "bingo", "purposeful"]
    selected = []
    words.each{|item| selected<<item unless item.end_with?("ing") }
    selected
  end

  def test_remove_words_containing_e
    words = ["four", "red", "five", "blue", "pizza", "purple"]
    selected = []
    words.each{|item| selected<<item unless item.include?("e") }
    selected
  end

  def test_remove_dinosaurs
    animals = ["tyrannosaurus", "narwhal", "eel", "achillesaurus", "qingxiusaurus"]
    notasaurus = []
    animals.each{|item| notasaurus<<item unless item.end_with?("saurus") }
    notasaurus
  end

  def test_remove_numbers
    elements = ["cat", "dog", 23, 81.1, 56, "aimless", 43]
    selected = []
    elements.each{|item| selected<<item unless item.is_a?(Integer) || item.is_a?(Float) }
    selected
  end

  def test_remove_floats
    elements = ["cat", "dog", 32.333, 23, 56, "aimless", 43.2]
    selected = []
    elements.each{|item| selected<<item unless item.class == Float }
    selected
  end

  def test_remove_animals_starting_with_vowels
    animals = ["aardvark", "bonobo", "cat", "dog", "elephant"]
    selected = []
    animals.each{|item| selected<<item unless ["a","e","i","o","u"].include?(item[0]) }
    selected
  end

  def test_remove_capitalized_words
    words = ["CAT", "dog", "AIMLESS", "Trevor", "butter"]
    selected = []
    words.each{|item| selected<<item unless item.upcase == item }
    selected
  end

  def test_remove_arrays
    elements = ["CAT", ["dog"], 23, [56, 3, 8], "AIMLESS", 43, "butter"]
    selected = []
    elements.each{|item| selected<<item unless item.is_a?(Array) }
    selected
  end

  def test_remove_hashes
    elements = ["cat", {:dog=>"fido"}, 23, {:stuff=>"things"}, "aimless", 43]
    selected = []
    elements.each{|item| selected<<item unless item.is_a?(Hash) }
    selected
  end

end