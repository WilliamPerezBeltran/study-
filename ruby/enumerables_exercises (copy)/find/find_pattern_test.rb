class FindPatternTest 

  def test_find_first_seven_letter_word
    words = ["capricious", "berry", "unicorn", "bag", "apple", "festering", "pretzel", "pencil"]
    found = nil
    words.each do |word|
      if word.length == 7
        found = word
        break
      end
    end
    found
    # assert_equal "unicorn", found
  end

  def test_no_waldo
    words = ["scarf", "sandcastle", "flag", "pretzel", "crow", "key"]
    found = nil
    words.each do |word|
      if word == "waldo"
        found =  word
        break
      end
    end
    found
  end

  def test_find_waldo
    words = ["noise", "dog", "fair", "house", "waldo", "bucket", "fish"]
    found = nil
    words.each do  |item|
      if item == "waldo"
        found = item 
        break
      end 
    end 
    found
  end

  def test_cannot_find_3_letter_words
    words = ["piglet", "porridge", "bear", "blueberry"]
    found = nil
    words.each do |item|
      if item.length === 3
        found = item
        break
      end 
    end
    found
  end

  def test_find_13
    numbers = [2, 13, 19, 8, 3, 27]
    found = nil
    numbers.each do |item|
      if item == 13
        found = item
        break
      end 
    end
    found
  end

  def test_find_first_even_number
    numbers = [3, 7, 13, 11, 10, 2, 17]
   found = nil 
   numbers.each do |item|
    if item.even?
      found = item 
      break
    end 
   end 
    found
  end

  def test_find_first_multiple_of_3
    numbers = [2, 8, 9, 27, 24, 5]
   found = nil 
   numbers.each do |item|
    if item%3 == 0
      found = item 
      break
    end 
    end 
    found
  end

  def test_find_first_word_starting_with_q
    words = ["weirdo", "quill", "fast", "quaint", "quitter", "koala"]
    found = nil 
    words.each do |item|
      if item.start_with?("q")
        found = item 
        break
      end 
    end 
    found
  end

  def test_find_first_word_ending_with_er
    words = ["biggest", "pour", "blight", "finger", "pie", "border"]
    found = nil 
    words.each do |item|
      if item.end_with?("er")
        found = item 
        break
      end 
    end 
    found
  end

  def test_find_first_number_greater_than_20
    numbers = [1, 8, 19, 21, 29, 31, 34]
    found = nil 
    numbers.each do |item|
      if item >= 20
        found = item 
        break
      end 
    end
    found
  end

end