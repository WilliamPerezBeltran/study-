require "pry"

class CountEnumerableMethod

  def test_count_count_words_with_e
    words = ["thing", "phone", "bark", "belt", "shoe", "bath"]
    words.count{|item| item.include?('e') }
    # assert_equal 3, tally
  end


  def test_count_numbers_greater_than_17
    numbers = [9, 18, 12, 17, 1, 3, 99]
    numbers.count{|item| item > 17 }
    # assert_equal 2, tally
  end

  def test_count_words_that_are_uppercase
    words = ["trousers", "SOCKS", "sweater", "Cap", "SHOE", "TIE"]
    words.count{|item| item.upcase == item }
    # assert_equal 3, tally
  end

  def test_count_words_ending_in_ing
    words = ["thought", "brake", "shin", "juice", "trash"]
    words.count{|item| item.start_with?('ing') }
    # assert_equal 0, tally
  end

  def test_count_even_numbers
    numbers = [9, 2, 1, 3, 18, 39, 71, 4, 6]
    numbers.count{|item| item.even?}
    # assert_equal 4, tally
  end
  def test_count_multiples_of_5
    numbers = [2, 5, 19, 25, 35, 67]
    numbers.count{|item| item%5==0 }
    # assert_equal 3, tally
  end

  def test_count_round_prices
    prices = [1.0, 3.9, 5.99, 18.5, 20.0]
    prices.count{|item| item.to_s.split(".")[1].to_i == 0 }
    # assert_equal 2, tally
  end

  def test_count_four_letter_words
    words = ["bake", "bark", "corn", "apple", "wart", "bird", "umbrella", "fart"]
    words.count{|item| item.length == 4}
    # assert_equal 6, tally
  end

end