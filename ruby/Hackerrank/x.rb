require "pry"



def palindromeIndex(s)
    # Write your code here
    return -1 if s == s.reverse
    for x in (0..(s.size-1))
        s_new = ""
        for y in (0..(s.size-1))
            x == y ? next : s_new << s[x]     
        end
        return x if s_new == s_new.reverse
    end
    return -1
end
p palindromeIndex("bcbc")



# def palindromeIndex(str)
#     return -1 if str == str.reverse
#     for x in (0..(str.length-1))
#         s_1 = "" 
#         for y in (0..(str.length-1))
#             x == y ? next : s_1<<str[y] 
#         end
#         s_2 = s_1.reverse
#         return x if  s_1 == s_2
#     end
#     return -1 
# end


def findDigits(n)
    # Write your code here
    contador =0
     n.to_s.chars.each do |x|
        if (x.to_i != 0) and ( n%x.to_i== 0)
           contador+=1
        end

    end
    contador

end

p findDigits(124)
