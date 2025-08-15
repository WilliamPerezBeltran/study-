import random 
from collections import Counter

# 1. Create a dictionary with 5 countries and their capitals.
# 2. Add a new country.
# 3. Update the capital of an existing country.
# 4. Remove one country.
# 5. Print all keys and values.

countries = {
    "Spain": "Madrid",
    "France": "Paris",
    "Italy": "Rome",
    "Germany": "Berlin",
    "Portugal": "Lisbon"
}

countries["Colombia"] = "Bogota"
countries.update({"Mexico":"Ciudad de mexico"})
countries.update({"Portugal": "zxxx"})
del countries["Spain"]

for key, value in countries.items():
    print(key,value)

from collections import Counter

c = Counter("banana")
print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})
print("~~~~~~~ method_1~~~~~~~")
# Count how many times each letter appears in the word 'programming'
word = "programming"

def count_word(word):
    new = list()
    for x in list(word):
        if x not in new:
            new.append(x)

    dict_count = dict()
    for x in new:
        count = 0
        for y in word:
            if x == y:
               count += 1
        dict_count[x] = count
    return dict_count

print(count_word("programming"))

print("~~~~~~~ method_2~~~~~~~")

# Count how many times each letter appears in the word 'programming'
def unique_array(word):
    new = list()
    for x in list(word):
        if x not in new:
            new.append(x)
    return new


def count_word(new, word):
    dict_count = dict()
    for x in new:
        count = 0
        for y in word:
            if x == y:
               count += 1
        dict_count[x] = count
    return dict_count


def count_(word):
    return count_word(unique_array(word), word)

print(count_("mmaakkssddadsf"))


print("~~~~~~~ method_2~~~~~~~")

# 3. List comprehension
# Create a list with the squares of even numbers from 1 to 20
def even_squares_number():
    list_ = list() 
    for x in range(1,21):
        if x%2 == 0:
            list_.append((x*x))
    return list_

def even_squares_number_():
    return [ x*x for x in range(0,21) if x%2 == 0]

def even_squares_number_map():
    return map(lambda x:x*x,list(range(0,21)))


print(even_squares_number())
print(even_squares_number_())
print(even_squares_number_map())



# ~~~~~~~~~~ 4. Dictionary comprehension ~~~~~~~~~~
# Create a dictionary with numbers 1 to 5 as keys and their cubes as values
def cubes():
    return  {x: x**3 for x in range(1,6)}
print(cubes())
# ~~~~~~~~~~ 5. map and filter
# Use map to convert all names in a list to uppercase
# Use filter to keep only names with more than 5 letters
names = ["John", "Ana", "Christine", "Peter", "Sebastian"]
def convert_name_map(names):
    return map(lambda x:x.upper(),names) 

def filter_name(names):
    return list(filter(lambda x: len(x) > 5,names)) 
# ~~~~~~~~~~ 6. reduce ~~~~~~~~~~
# Use reduce to calculate the product of all elements in a list
from functools import reduce
numbers = [2, 3, 4, 5]
# ~~~~~~~~~~ 7. Tuples and sets ~~~~~~~~~~
# Create a tuple with 5 fruits and:
#   - Print the second fruit
#   - Check if "mango" is in the tuple
# Create a set with repeated numbers and display it without duplicates
tuple_ = ("orange","apple","lemon","otra","bla","papaya")
print(tuple_[1])
print("mango" in tuple_)

def random_():
    n = list()
    for x in range(30):
        n.append(random.randint(0,10))
    return tuple(n)
print(random_())


def random__():
    return [tuple(random.randint(0,10)) for x in range(30)]
        
def unique_random_():
    w = list()
    for x in [tuple(random.randint(0,10)) for x in range(30)]:
        if x not in w:
            w.append(x)


     
print(random_())
print(unique_random_())


#8. ~~~~~~~~~~ Slicing ~~~~~~~~~~
# From the string "abcdefghijklmnopqrstuvwxyz":
#   - Extract only the vowels using slicing
#   - Reverse the string using slicing
#9. ~~~~~~~~~~ Built-in modules ~~~~~~~~~~
# Use the math module to:
#   - Calculate the square root of 144
#   - Calculate the sine of 90 degrees








