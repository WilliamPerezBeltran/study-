require "pry"

class ReduceUsingEach 
  
 def test_sum_a_list_of_numbers
    numbers = [32, 1, 21, 5, 81, 333]
    sum = 0
    numbers.each do |number|
      sum = sum + number
    end
    sum
    # rta 473
  end

  def test_subtract_list_of_numbers
    numbers = [28, 12, 38, 1, 91]
    difference = 0
    numbers.each do |number|
      difference+=-number
    end
    difference
    # rta -170
  end

  def test_multiply_list_of_numbers
    numbers = [2, 3, 5, 7]
    product = 1
    numbers.each do |item|
      product*=item
    end 
    product
    # rta 210
  end

  def test_capitalize_keywords_in_phrase_one_fish_two_fish_red_fish_blue_fish
  keywords = ["fish", "blue"]
  phrase = 'one fish two fish red fish blue fish'
  keywords.each do |item|
    phrase = phrase.gsub(item,item.upcase)
  end
  phrase

  # rta 'one FISH two FISH red FISH BLUE FISH'
  end

  def test_divide_560_by_a_bunch_of_numbers
    numbers = [2, 2, 2, 5, 7]
    quotient = 560
    numbers.each do |item|
       quotient/=item
    end
    quotient
    # rta 2
  end

  def test_subtract_smallest_values_from_100
    elements = [[8, 5, 3], [1, 9, 11], [4, 7, 2], [19, 34, 6]]
    difference = 100
    elements.each do|item|
      difference-=item.min
    end
    difference
    # rta 88, 
  end

  def test_add_all_the_second_values_together
    elements = [["a", 1], ["b", 9], ["c", 21]]
    sum = 0
    elements.each do | item |
      sum+=item[1]
    end
    sum 
    # rta 31
  end

end