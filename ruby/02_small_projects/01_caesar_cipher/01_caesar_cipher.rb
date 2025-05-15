require 'pry'

alphabet = ('a'..'z')
alphabet_array = alphabet.map {|letter| letter}

hash_alphabet = {}
alphabet_array.each_with_index{|letter,index| hash_alphabet[index] = letter}

hash_alphabet_caesar_cipher = {}
hash_alphabet.each_with_index do |value,key|
	value_caesar_cipher = (key+23)%26
	hash_alphabet_caesar_cipher[key] = hash_alphabet[value_caesar_cipher] 
end

word = "hello"
word_key_array = word.chars.map{|letter|hash_alphabet.key(letter)}
word_key_array = word_key_array.map{|number| hash_alphabet_caesar_cipher[number]}

puts word_key_array.join

