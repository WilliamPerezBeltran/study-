gem 'minitest'
require 'minitest/autorun'
require 'minitest/pride'

class ReduceEnumerableMethod

  def test_sum_a_list_of_numbers
    numbers = [32, 1, 21, 5, 81, 333]
    numbers.reduce(0){|acco, item| acco + item }
    # rta 473
  end

  def test_subtract_list_of_numbers
    numbers = [28, 12, 38, 1, 91]
    numbers.reduce(0){|acco, item| acco + (-item) }
    # rta -170, 
  end

  def test_multiply_list_of_numbers
    numbers = [2, 3, 5, 7]
    numbers.reduce(1){|acco,item| acco*item}
    # initial value is 1
    # rta 210, 
  end

  def test_capitalize_keywords_in_phrase_one_fish_two_fish_red_fish_blue_fish
    keywords = ["fish", "blue"]
    keywords.reduce('one fish two fish red fish blue fish'){|acco,item| acco.gsub(item,item.upcase)}
    # initial value is 'one fish two fish red fish blue fish'
    # rta 'one FISH two FISH red FISH BLUE FISH', 
  end

  def test_divide_560_by_a_bunch_of_numbers
    numbers = [2, 2, 2, 5, 7]
    numbers.reduce(560){|acco,item| acco/item}
    # initial value is 560
    # rta 2, 
  end

  def test_subtract_smallest_values_from_100
    elements = [[8, 5, 3], [1, 9, 11], [4, 7, 2], [19, 34, 6]]
    elements.reduce(100){|acco,item| acco-item.min}
    # initial value is 100
    # rta 88, 
  end

  def test_add_all_the_second_values_together
    elements = [["a", 1], ["b", 9], ["c", 21]]
    # initial value is 0
    elements.reduce(0){|acco,item| acco+item[1]}
    # rta 31, 
  end

end