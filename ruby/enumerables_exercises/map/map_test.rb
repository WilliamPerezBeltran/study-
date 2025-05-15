require 'pry'

class MapTest

  def test_capitalize
    names = ["alice", "bob", "charlie"]
    names.map{|name| name.capitalize}
    # assert_equal ["Alice", "Bob", "Charlie"], capitalized_names
  end

 
  def test_doubles
    numbers = [1, 2, 3, 4, 5]
    numbers.map{|item| item*2}
  end

  def test_squares
    numbers = [1, 2, 3, 4, 5]
    numbers.map{|item| item**2}
  end

  def test_lengths
    names = ["alice", "bob", "charlie", "david", "eve"]
    names.map{|item| item.length}
  end

  def test_normalize_zip_codes
    numbers = [234, 10, 9119, 38881]
    numbers.map{|item| item.to_s.rjust(5,"0")}
  end

  def test_backwards
    names = ["alice", "bob", "charlie", "david", "eve"]
    names.map{|item| item.reverse}
  end

  def test_words_with_no_vowels
    words = ["green", "sheep", "travel", "least", "boat"]
    words.map{|item| item.delete("aeiou")}
  end

end