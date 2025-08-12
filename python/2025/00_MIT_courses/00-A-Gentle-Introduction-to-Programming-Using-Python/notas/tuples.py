te = () # => empty tuple 
t = (2,"mit",3)
#print(t[0])
print(te + t)
print((2,3,4)+("mit","OLE"))

# ~~~~~~ swap ~~~~~
x = 2
y = 3
print(x,y)

temp = x
x = y 
y = temp
print(x,y)

(x,y) = (y,x)
print(x,y)

# return more than one value from a function 
def quotient_and_remainder(x,y):
    q = x // y 
    r = x % y 
    return (q,r)
(quot,rem) = quotient_and_remainder(23,3)
print(quot,rem)


# ~~~~~~ get-data ~~~~~
def get_data(atuple):
    nums = ()
    words = ()
    for x in atuple:
        nums = nums + (x[0],)
        if x[1] not in words:
            words = words + (x[1],)
    min_num = min(nums)
    max_num = max(nums)
    uniq_words = len(words)
    return (min_num, max_num, uniq_words)

result = get_data(((10, "dog"), (4, "cat"), (7, "dog"), (2, "cat")))
print(result)

# ~~~~~~ factorize get-data ~~~~~
def get_data_(atuple):
    nums, words = (), ()
    for x in atuple:
        nums += (x[0],)
        words += (x[1],) if x[1] not in words else ()
            
    return (min(nums),max(nums) ,len(words) )

result = get_data(((10, "dog"), (4, "cat"), (7, "dog"), (2, "cat")))
print(result)
