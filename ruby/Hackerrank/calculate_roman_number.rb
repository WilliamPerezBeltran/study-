# https://www.hackerrank.com/contests/modena-coding-april-2017/challenges/roman-number/problem

require "pry"

ROMAN_NUMBERS = {
  1000 => "M",
  900 => "CM",
  500 => "D",
  400 => "CD",
  100 => "C",
  90 => "XC",
  50 => "L",
  40 => "XL",
  10 => "X",
  9 => "IX",
  5 => "V",
  4 => "IV",
  1 => "I"
}

def roman(number)
  return "" if number == 0

  ROMAN_NUMBERS.each do |value, letter|
    if value <= number
      binding.pry
      

      return (letter * (number / value)) << roman(number % value)
    end
  end

  roman(number % value)
end

# Tests
[47, 1910, 1954, 1990, 2008, 139, 7].each { |number| puts roman(number) }