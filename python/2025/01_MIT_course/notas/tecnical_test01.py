
"""
Write a function that reverses a string.
Example: "python" → "nohtyp"
"""
def reverse(s):
    pivote = len(s)-1
    n = list()
    while(pivote >= 0 ):
        n.append(s[pivote])
        pivote -= 1
    return "".join(n)

def reverse_(s):
    return "".join(list(reversed(s)))

def reverse__(s):
    return s[::-1]

"""
Given a list of integers, return another list without duplicates but keeping the original order.
Example: [1, 2, 2, 3, 1] → [1, 2, 3]
"""
def no_duplicates(l):
    new_list = list()
    for x in l:
        if x not in new_list:
            new_list.append(x)
    return new_list

def no_duplicates_(l):
     return [x for i,x in enumerate(l) if x not in l[:i]]

def no_duplicates__(l):
     return list(dict.fromkeys(l)) 
"""
Implement a function that receives an integer and determines if it is a prime number.

"""
# siendo n el numero y 2 <= d <= n-1
# if existe un d que cumpla n%d == 0 => n no es primo
# if no hay un d que cumpla n%d == 0 => es primo
def prime_number(n):
    array_of_residuos = [n%x for x in range(2,n)]
    return  not 0 in array_of_residuos 


def prime_number_(n):
    return  not 0 in [n%x for x in range(2,n)]

    

"""
Given a dictionary of students with their grades, return the name of the student with the highest grade.

grades = {"Ana": 85, "Luis": 90, "Pedro": 78}
# Expected output: "Luis"

"""
def highest_grade(grades): 
    masimo = max([x[1] for x in grades.items()])
    result = None  
    for nombre, nota in grades.items():
        if masimo == nota:
            return nombre 

def highest_grade_(grades):
        return max(grades,key=grades.get)

"""
Implement a function that receives a list of strings and returns the longest word.
Example: ["python", "java", "javascript"] → "javascript"

"""

"""
Implement a decorator in Python that measures the execution time of a function.

"""
""" Write a generator that produces the first n numbers of the Fibonacci sequence.
"""

"""
Using functional programming (map, filter, and reduce), calculate the product of all even numbers in a list.

"""
"""
Part 4: Bonus (Optional)

You have a CSV file with the following content:

name,age
Ana,23
Luis,30
Pedro,25


Write a Python script that reads the file and calculates the average age.

"""
