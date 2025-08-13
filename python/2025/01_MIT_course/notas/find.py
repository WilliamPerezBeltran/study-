import string 

def find(str, ch):
    index = 0 
    while index < len(str):
        if str[index] == ch:
            return index
        index =  index + 1
    return -1 

result = find("fiera de su amor loca", "a")
print result 

print "----------------------------" 

print string.find("fiera de su amor loca","a")
