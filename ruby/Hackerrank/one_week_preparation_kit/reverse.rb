# Without using standard library functions, write the reverse function that takes an array 
# and returns an array in reverse order.

def reverse_vertion_1(arr)
	arrReversed = []
	l = arr.length - 1
	(0..l).each do |index|
		arrReversed[index] = arr[l - index] 
	end
	arrReversed
end

puts reverse_vertion_1([1, 2, 3, 4, 5, 6, 7, 8, 9]).to_s


def reverse_vertion_2(arr)
  new_arr = []
  arr.each_with_index do |_, i|
    new_arr << arr[(i+1) * -1]
  end
  new_arr
end

puts reverse_vertion_2([3,2,1])


def reverse_vertion_3(arr)
  arr.each_with_object([]) { |item, reversed| reversed.unshift(item) }
end

 reverse_vertion_3([3,2,1])



def reverse_vertion_mine(arr)
  arr.each_with_index.reduce([]){|acomulator,(element,index)| acomulator<<arr[arr.length-1-index]}
end

 p reverse_vertion_mine([1,2,3,4,5,6])
 p reverse_vertion_mine([10,20,30,40])
 p reverse_vertion_mine([90,80,58,12,1])
