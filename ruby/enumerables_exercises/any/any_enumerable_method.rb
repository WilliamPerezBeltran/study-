
require "pry"


class AnyEnumerableMethod 

  def test_has_at_least_one_zero
    numbers = [2, 0, 9, 3, 0, 1]
    numbers.any?{|item| item.zero? }
    # rta true
  end

  def test_does_not_have_any_zeros
    numbers = [3, 1, 3, 2, 4, 9, 8]
    numbers.any?{|item| item.zero? }
    # rta false
  end

  def test_has_at_least_one_alice
    names = ["Bill", "Bob", "Burton", "Alice", "Brandon"]
    names.any?{|item| item == "Alice" }
    # rta true 
  end

  def test_no_alices
    names = ["Chuck", "Charlene", "Cory", "Chris", "Carl"]
    names.any?{|item| item == "Alice" }
    # rta false
  end

  def test_has_a_multi_word_phrase
    phrases = ["Sure!", "OK.", "I have no idea.", "Really?Whatever."]
     phrases.any?{|item| item.include?(" ") }
    # rta true 
  end

  def test_no_monkeys
    animals = ["elephant", "hippo", "jaguar", "python"]
    animals.any?{|item| item == "monkey" }
    # rta false
  end

  def test_no_multiples_of_five
    numbers = [3, 1, 3, 2, 4, 9, 8]
    numbers.any?{|item| item%5==0 }
    # rta false
  end

end