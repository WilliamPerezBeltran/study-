# 📝 Python Technical Test with Statements and Solutions

## Part 1: Basic

### 1. Reverse a string
**Statement:** Write a function that reverses a string.  
Example: `"python"` → `"nohtyp"`

**Solution:**
```python
def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("python"))  # "nohtyp"
```

---

### 2. Remove duplicates from a list
**Statement:** Given a list of integers, return another list without duplicates but keeping the original order.  
Example: `[1, 2, 2, 3, 1]` → `[1, 2, 3]`

**Solution:**
```python
def remove_duplicates(nums: list[int]) -> list[int]:
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

print(remove_duplicates([1, 2, 2, 3, 1]))  # [1, 2, 3]
```

---

## Part 2: Intermediate

### 3. Prime number check
**Statement:** Implement a function that receives an integer and determines if it is a **prime number**.  

**Solution:**
```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False
```

---

### 4. Highest grade
**Statement:** Given a dictionary of students with their grades, return the name of the student with the highest grade.  

```python
grades = {"Ana": 85, "Luis": 90, "Pedro": 78}
# Expected output: "Luis"
```

**Solution:**
```python
def highest_grade(grades: dict) -> str:
    return max(grades, key=grades.get)

print(highest_grade(grades))  # "Luis"
```

---

### 5. Longest word
**Statement:** Implement a function that receives a list of strings and returns the longest word.  
Example: `["python", "java", "javascript"]` → `"javascript"`

**Solution:**
```python
def longest_word(words: list[str]) -> str:
    return max(words, key=len)

print(longest_word(["python", "java", "javascript"]))  # "javascript"
```

---

## Part 3: Advanced

### 6. Execution time decorator
**Statement:** Implement a **decorator** in Python that measures the execution time of a function.  

**Solution:**
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "done"

print(slow_function())  # prints execution time + "done"
```

---

### 7. Fibonacci generator
**Statement:** Write a **generator** that produces the first `n` numbers of the Fibonacci sequence.  

**Solution:**
```python
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### 8. Functional programming
**Statement:** Using functional programming (`map`, `filter`, and `reduce`), calculate the product of all even numbers in a list.  

**Solution:**
```python
from functools import reduce

def product_of_evens(nums: list[int]) -> int:
    evens = filter(lambda x: x % 2 == 0, nums)
    return reduce(lambda a, b: a * b, evens, 1)

print(product_of_evens([1, 2, 3, 4, 5, 6]))  # 48 (2*4*6)
```

---

## Part 4: Bonus (Optional)

### 9. Average age from CSV
**Statement:** You have a CSV file with the following content:  
```
name,age
Ana,23
Luis,30
Pedro,25
```
Write a Python script that reads the file and calculates the average age.  

**Solution:**
```python
import csv

def average_age_from_csv(filename: str) -> float:
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        ages = [int(row["age"]) for row in reader]
    return sum(ages) / len(ages)

# Suppose "people.csv" contains the given data
print(average_age_from_csv("people.csv"))  # 26.0
```
