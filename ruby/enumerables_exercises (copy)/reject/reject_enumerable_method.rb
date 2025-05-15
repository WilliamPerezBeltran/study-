require "pry"

class RejectEnumerableMethod

  def test_remove_zeros
    numbers = [2, 93, 7, 0, 0, 1, 0, 31, 0, 368]
    numbers.reject{|item| item.zero? }
  end

  def test_remove_vowels
    letters = ["a", "l", "l", " ", "y", "o", "u", "r", " ", "b", "a", "s", "e", " ", "a", "r", "e", " ", "b", "e", "l", "o", "n", "g", " ", "t", "o", " ", "u", "s"]
    letters.reject{|item| ["a","e","i","o","u"].include?(item) }
  end

  def test_remove_numbers_divisible_by_3
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
     numbers.reject{|item| item%3==0 }
  end

  def test_remove_words_with_more_than_three_letters
    words = ["pill", "bad", "finger", "cat", "blue", "dog", "table", "red"]
     words.reject{|item| item.length > 3 }
  end

  def test_remove_words_ending_in_e
    words = ["are", "you", "strike", "thinking", "belt", "piece", "warble", "sing", "pipe"]
     words.reject{|item| item.end_with?("e") }
  end

  def test_remove_words_ending_in_ing
    words = ["bring", "finger", "drought", "singing", "bingo", "purposeful"]
     words.reject{|item| item.end_with?("ing") }
  end

  def test_remove_words_containing_e
    words = ["four", "red", "five", "blue", "pizza", "purple"]
     words.reject{|item| item.include?("e") }
  end

  def test_remove_dinosaurs
    animals = ["tyrannosaurus", "narwhal", "eel", "achillesaurus", "qingxiusaurus"]
     animals.reject{|item| item.end_with?("saurus") }
  end

  def test_remove_numbers
    elements = ["cat", "dog", 23, 81.1, 56, "aimless", 43]
     elements.reject{|item| item.is_a?(Integer) || item.class ==Float  }
  end

  def test_remove_floats
    elements = ["cat", "dog", 32.333, 23, 56, "aimless", 43.2]
     elements.reject{|item| item.is_a?(Float) }
  end

  def test_remove_animals_starting_with_vowels
    animals = ["aardvark", "bonobo", "cat", "dog", "elephant"]
     animals.reject{|item| ["a","e","i","o","u"].include?(item[0]) }
  end

  def test_remove_capitalized_words
    words = ["CAT", "dog", "AIMLESS", "Trevor", "butter"]
     words.reject{|item| item.upcase == item }
  end

  def test_remove_arrays
    elements = ["CAT", ["dog"], 23, [56, 3, 8], "AIMLESS", 43, "butter"]
     elements.reject{|item| item.is_a?(Array) }
  end

  def test_remove_hashes
    elements = ["cat", {:dog=>"fido"}, 23, {:stuff=>"things"}, "aimless", 43]
     elements.reject{|item| item.is_a?(Hash) }
  end

end