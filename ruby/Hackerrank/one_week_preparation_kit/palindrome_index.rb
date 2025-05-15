#!/bin/ruby

require 'pry'
require 'json'
require 'stringio'


def PalindromeIndex(s)
	return -1 if s == s.reverse
	arr = s.split("")
	
	for x in (0..s.length-1)
		return x if arr.select.with_index{|_,index| index != x }.join("") == arr.select.with_index{|_,index| index != x }.join("").reverse
	end
	return -1
end


p PalindromeIndex("aaab") #=> 3
p PalindromeIndex("baa") #=> 0
p PalindromeIndex("aaa") #=> -1



p "-----------------"
p "-----------------"
p "-----------------"
p "-----------------"
p "-----------------"
p "-----------------"
 # https://stackoverflow.com/questions/65435540/palindrome-index-hackerrank-with-javascript


# function isPalindrome(s) {
#       for (let i = 0; i < s.length/2; i++) {
#             if (s[i] !== s[s.length - 1 - i]) {
#                   return false;
#             }
#       }
#       return true;
# }



def reverse_str(str)
	str_reverse =""
	(str.length-1).downto(0) do |x|
		str_reverse<<str[x]
	end
	str_reverse

end

 reverse_str("abcd")
 reverse_str("repetir")
 reverse_str("la vida es bella william perez ")





# def reverse_str_ole(str)
# 	str.split("").each_with_index.reduce("") do |aco,(element,index)| 
# 		aco<<str[str.length-1-index]
# 	end
# end

def reverse_str_ole(str)
	str.split("").each_with_index.reduce(""){|aco,(element,index)| aco<<str[str.length-1-index] }  
end

puts "-------"
puts "-------"
puts "-------"
puts "-------"
puts "-------"
puts "-------"
 p reverse_str_ole("abcd")
 p reverse_str_ole("repetir")
 p reverse_str_ole("la vida es bella william perez ")

puts "-------"
puts "-------"
puts "-------"
puts "-------"
puts "-------"
puts "-------"


def rev(str)
	str.split("").each_with_index.reduce(""){|aco,(elem, index)| aco<<str[str.size-1-index]}
end

def PalinIndex(str)
	return -1 if str == rev(str)
	for x in (0..(str.length-1))
		s_1 = "" 
		for y in (0..(str.length-1))
			x == y ? next : s_1<<str[y] 
		end
		s_2 = rev(s_1)
		return x if  s_1 == s_2
	end
	return -1 
end

p PalinIndex("aaab") #=> 3
p PalinIndex("baa") #=> 0
p PalinIndex("aaa") #=> -1
p PalinIndex("aba") #=> -1



puts "-------"
puts "-------"
puts "-------"
puts "-------"
puts "-------"




# def theBest(str)
# 	return -1 if str == str.reverse
# 	for x in (0..(str.length-1))
# 		new_str = str[0...x] + str[x+1...str.length] 
# 		new_str_reverse = new_str.reverse 
# 		return x if new_str == new_str_reverse  
# 	end
# 	return -1 
# end


def theBest(str)
	return -1 if str == str.reverse
	(0..(str.length-1)).each{|x| return x if str[0...x] + str[x+1...str.length] == (str[0...x] + str[x+1...str.length]).reverse }
	return -1 
end

p theBest("aaab") #=> 3
p theBest("baa") #=> 0
p theBest("aaa") #=> -1
p theBest("aba") #=> -1

