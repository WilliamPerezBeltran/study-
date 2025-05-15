require 'pry'

alphabet = ('a'..'z')

def ask_data
	p "give a word"
	word = gets.chomp
	p "gime a shift"
	shift_move = gets.chomp.to_i
	return word, shift_move
end

def alphabet_method(alphabet)
	alphabet_hash = {}
	alphabet.each_with_index{|letter,index| alphabet_hash[letter]=index}
	p "alphabet" 
	p alphabet_hash.keys
	return alphabet_hash 
end

def alphabet_caesar_method(alphabet, alphabet_method,shift_move)
	alphabet_hash_caesar = {}
	alphabet.each_with_index do |value,index|
		caesar = (index+shift_move)%26
		alphabet_hash_caesar[alphabet_method.key(caesar)] = index
	end
	p "alphabet_hash_caesar"
	p alphabet_hash_caesar.keys
	return alphabet_hash_caesar
end

def print_rta(word,shift_move,alphabet_hash,alphabet_caesar)
	word_array_index = word.chars.map{|letter| alphabet_hash[letter] }
	rta = word_array_index.map{|value, index| alphabet_caesar.key(value)}
	rta = rta.map.with_index(){|element,index| element.nil? ? rta[index]="-"  : element}
	rta = rta.join().split("-")
	rta.each do |word|
		print "#{word} "
	end
	puts ""
end

data = ask_data

alphabet_hash = alphabet_method(alphabet)
alphabet_caesar = alphabet_caesar_method(alphabet,alphabet_hash,data[1])
print_rta(data[0],data[1],alphabet_hash,alphabet_caesar)

