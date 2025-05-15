
class FindTest 

  def test_find_first_seven_letter_word
    words = ["capricious", "berry", "unicorn", "bag", "apple", "festering", "pretzel", "pencil"]
    words.find{|item| item.length == 7 }
  end

  def test_no_waldo
    words = ["scarf", "sandcastle", "flag", "pretzel", "crow", "key"]
    words.find{|item| item == "waldo"}
  end

  def test_find_waldo
    words = ["noise", "dog", "fair", "house", "waldo", "bucket", "fish"]
    words.find{|item| item == "waldo"}
  end

  def test_cannot_find_3_letter_words
    words = ["piglet", "porridge", "bear", "blueberry"]
    words.find{|item| item.length == 3}
  end

  def test_find_13
    numbers = [2, 13, 19, 8, 3, 27]
    found = numbers.find do |item|
      item == 13
    end
    found
  end

  def test_find_first_even_number
    numbers = [3, 7, 13, 11, 10, 2, 17]
    numbers.find{|item| item.even?}
  end

  def test_find_first_multiple_of_3
    numbers = [2, 8, 9, 27, 24, 5]
    numbers.find{|item| item%3 ==0}
  end

  def test_find_first_word_starting_with_q
    words = ["weirdo", "quill", "fast", "quaint", "quitter", "koala"]
    words.find{|item| item.start_with?("q")}
  end

  def test_find_first_word_ending_with_er
    words = ["biggest", "pour", "blight", "finger", "pie", "border"]
    words.find{|item| item.end_with?("er")}
  end

  def test_find_first_number_greater_than_20
    numbers = [1, 8, 19, 21, 29, 31, 34]
    numbers.find{|item| item>=20}
  end

end