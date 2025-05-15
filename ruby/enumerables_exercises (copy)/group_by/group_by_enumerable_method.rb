require "pry"

class GroupByEnumerableMethod

  def test_group_words_by_length
    words = ["sue", "alice", "steve", "sally", "adam", "fort", "tops", "dog", "cat"]
    words.group_by{|item| item.length}
    # expected = {3=>["sue", "dog", "cat"], 4=>["adam", "fort", "tops"], 5=>["alice", "steve", "sally"]}
  end

  def test_group_numbers_by_odd_and_even
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    numbers.group_by{|item| item%2}
    # expected = {1=>[1, 1, 3, 5, 13, 21, 55], 0=>[2, 8, 34]}
  end

  def test_group_words_by_first_letter
    words = ["ant", "axis", "albatross", "bolt", "badge", "butter", "car", "cdr", "column"]
    words.group_by{|item| item[0]}
    # expected = {"a"=>["ant", "axis", "albatross"], "b"=>["bolt", "badge", "butter"], "c"=>["car", "cdr", "column"]}
  end

  def test_group_words_by_uniqueness
    words = ["one", "two", "one", "TWO", "three", "one", "three", "three", "three"]
    words.group_by{|item| item.downcase}
    # expected = {"one"=>["one", "one", "one"], "two"=>["two", "TWO"], "three"=>["three", "three", "three", "three"]}
  end

  def test_group_by_number_of_zeros
    numbers = [1, 3, 500, 200, 4000, 3000, 10000, 90, 20, 500000]
    numbers.group_by{|item| item.to_s.count("0")}
    # expected = {0=>[1, 3], 2=>[500, 200], 3=>[4000, 3000], 4=>[10000], 1=>[90, 20], 5=>[500000]}
  end

  def test_group_by_order_of_magnitude
    numbers = [1, 3, 503, 239, 4938, 3932, 19982, 93, 21, 501787]
    numbers.group_by{|item| item.to_s.length}
    # expected = {1=>[1, 3], 2=>[93, 21], 3=>[503, 239], 4=>[4938, 3932], 5=>[19982], 6=>[501787]}
  end

end