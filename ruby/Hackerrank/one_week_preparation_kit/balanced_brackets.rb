require "pry"




def isBalanced(s)
	arr = []
	s.chars.each do |item|
		if item == "(" ||item == "{" ||item == "[" 
			arr.push(item)	
		else
			h = case item
			when ")"
			  "("
			when "}" 
			  "{"
			when "]"
			  "["
			 end

			if arr[arr.size-1] == h
				arr.pop
			else
				return  "NO"
			end
		end
	end
	return "YES" if arr.empty?
	return "NO"
end

 isBalanced("{[()]}") #=> YES
 isBalanced("{[(])}") #=> NO
 isBalanced("{{[[(())]]}}") #=> YES

 isBalanced("{(([])[])[]}") #=> YES
 isBalanced("{(([])[])[]]}") #=> NO
 isBalanced("{(([])[])[]}[]") #=> YES

 

