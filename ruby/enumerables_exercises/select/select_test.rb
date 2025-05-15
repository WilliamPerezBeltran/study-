
class SelectTest

  def test_pick_even_numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers.select{|item| item%2 ==0}
  end

  def test_pick_odd_numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers.select{|item| item.odd?}
  end

  def test_pick_words_with_three_letters
    words = ["pill", "bad", "finger", "cat", "blue", "dog", "table", "red"]
    words.select{|item| item.length == 3}
  end

  def test_pick_words_with_more_than_three_letters
    words = ["pill", "bad", "finger", "cat", "blue", "dog", "table", "red"]
     words.select{|item| item.length >=4}
  end

  def test_pick_words_ending_in_e
    words = ["are", "you", "strike", "thinking", "belt", "piece", "warble", "sing", "pipe"]
    words.select{|item| item.end_with?("e")}
   end

  def test_pick_words_ending_in_ing
    words = ["bring", "finger", "drought", "singing", "bingo", "purposeful"]
    words.select{|item| item.end_with?("ing")}
  end

  def test_pick_words_containing_e
    words = ["four", "red", "five", "blue", "pizza", "purple"]
    words.select{|item| item.include?("e")}
  end

  def test_pick_dinosaurs
    animals = ["tyrannosaurus", "narwhal", "eel", "achillesaurus", "qingxiusaurus"]
    animals.select{|item| item.end_with?("saurus")}
  end

  def test_pick_floats
    numbers = [3, 1.4, 3.5, 2, 4.9, 9.1, 8.0]
    numbers.select{|item| item.class == Float}
  end

  def test_pick_arrays
    elements = ["CAT", ["dog"], 23, [56, 3, 8], "AIMLESS", 43, "butter"]
    elements.select{|item| item.is_a?(Array)}
  end

  def test_pick_hashes
    elements = ["cat", {:dog=>"fido"}, 23, {:stuff=>"things"}, "aimless", 43]
    elements.select{|item| item.is_a?(Hash)}
  end

end