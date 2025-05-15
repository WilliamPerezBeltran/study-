# def reverse_odd(sentence="hello world")
#     array =[]
#     sentence.split("").each_with_index  do |value,index|
#     	if index%2 == 1
#     		array.push(value)
#     	end
#     end
#     array.reverse()

# end

# p reverse_odd()
https://womanonrails.com/functional-programming-ruby

def reverse_odd(sentence="hello world")
    hash_h ={}
    sentence.split("").each_with_index  do |value,index|
    	if index%2 == 1
    		hash_h[index] = value 
    	end
    end
    hash_h.each_with_index do |value,index|

    	p value

    end

end

p reverse_odd()