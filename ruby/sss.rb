
require "pry"
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def  is_prime(n)
    count_zero = 0
    (2..n).each{|x| count_zero+=1 if n%x == 0 }
    return false if count_zero > 1
    true 
end
def count_primes(n)
    count = 0  
   
    for x in (2...n)
        if is_prime(x)
            count += 1
        end
    end
    return count
end

p count_primes(100)

# La criba de Eratóstenes.
# La criba de Eratóstenes.
# La criba de Eratóstenes.
# La criba de Eratóstenes.
# La criba de Eratóstenes.
# La criba de Eratóstenes.

p "-------------------------"


# 204. Count Primes leetcode
# Given an integer n, return the number of prime numbers that are strictly less than n.



def count_primes(n)
   
    return 0 if n == 0
    return 0 if n == 1
    return 0 if n == 2
    return 1 if n == 3

    arr = (2...n).to_a 
    rta = []
    contador = 0
    loop do
        arr
        pivote = arr[contador]
        rta.push(pivote)
        arr.select!{|x| x%pivote != 0}
        # return rta if pivote*pivote>n
        return (rta+arr).count if pivote*pivote>n
    end
end

 p count_primes(1)
 p count_primes(10)
 p count_primes(100)
 p count_primes(1000)
 p count_primes(10000)
 p count_primes(999983)
 p count_primes(1500000)




def numeros_primos(n)
   
    return 0 if n == 0
    return 0 if n == 1
    return 0 if n == 2
    return 1 if n == 3

    arr = (2...n).to_a 
    rta = []
    contador = 0
    loop do
        arr
        pivote = arr[contador]
        rta.push(pivote)
        arr.select!{|x| x%pivote != 0}
        # return rta if pivote*pivote>n
        return (rta+arr).count if pivote*pivote>n
    end
end
p "--------------------"
p "--------------------"
p "--------------------"
 p numeros_primos(1)
 p numeros_primos(10)
 p numeros_primos(100)
 p numeros_primos(1000)
 p numeros_primos(10000)
 p numeros_primos(999983)
 p numeros_primos(1500000)






p "*************************"
p "*************************"
p "*************************"
p "*************************"








def is_prime(n)
    return false if n == 0
    return false if n == 1
    contador = 0
    for x in (2..n)
      contador+=1 if n%x == 0
    end
    
    return false if contador>=2
    true 
end

def is_palindromic_prime(str)
    str.to_s == str.to_s.split("").reverse.join("")
end


palindromic = ->(n)do
    2.upto(Float::INFINITY).lazy.select{|x| is_prime(x) && is_palindromic_prime(x)}.first(10)
end

puts palindromic.(100)

puts "**************"
puts "**************"
puts "**************"
puts "**************"
puts "**************"

print_array = ->(n)do
    2.upto(Float::INFINITY).lazy.select{|x| (((2.upto(n).select{|x| n%x == 0}.count) == 0) ? true : false) && (str.to_s == str.to_s.split("").reverse.join(""))}.first(100)
end


print print_array.(10)

# por finfinfinfinfinfinfin 
# por finfinfinfinfinfinfin 
# por finfinfinfinfinfinfin 
# por finfinfinfinfinfinfin 
# por finfinfinfinfinfinfin 
# por finfinfinfinfinfinfin 
# por finfinfinfinfinfinfin 
# por finfinfinfinfinfinfin 



 # Enter your code here. Read input from STDIN. Print output to STDOUT
# Your task is to print an array of the first n  palindromic prime numbers.
# For example, the first  10 palindromic prime numbers are 
# [2,3,5,7,11,101,131,151,181,191]
is_prime = ->(n)do
 ((2.upto(n).select{|x| n%x == 0}.size) == 1) ? true : false
end

print_array = ->(n)do
    1.upto(Float::INFINITY).lazy.select{|x| is_prime.(x) && x.to_s == x.to_s.reverse}.first(n.to_i)
end

# n = gets
# print print_array.(100)
print print_array.(3)


p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"


def serial_average(str)
    '002-10.00-20.00'
    rta = str.split("-")
    rta[0]+((rta[1].to_f+rta[2].to_f)/2.0).to_s
end