# def two_sum(nums, target)
# 	pivote = false
# 	rta = [] 
# 	nums.each_with_index do |value_x,index_i|
# 		for y in (index_i+1..(nums.length-1))
# 			if value_x + nums[y] == target
# 				rta.push(index_i)
# 				rta.push(y)
# 				pivote = true 
# 				break
# 			end
# 		end 
# 		break if pivote 
# 	end
# 	rta
# end



class LeetCode
	def two_sum(nums, target)
		nums.each_with_index do |value_x,index_i|
			for y in (index_i+1...(nums.length))
				return [index_i,y] if value_x + nums[y] == target
			end 
		end
	end
end


