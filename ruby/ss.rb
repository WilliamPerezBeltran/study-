
require "pry"

def sum(first, *rest)
	rest
end

p sum(1,"william")
p sum(1,"william","perez",3)
p sum(1,2,4)
p sum(1,2,[34])


def full_name(first, *rest)
    rest.insert(0,first).join(" ")
end

p full_name('Harsha', 'Bhogle')
p full_name('Harsha', 'Bhogle', 'perez')


def foo(str: "foo", num: 424242, **options)
  [str, num, options]
end

p foo(check: true) # => ['foo', 424242, {check: true}]


def other(str:"string", **options)
	[str,options]
end

p other(chec: true)
p other(noCheck: false)



def convert_temp(temp=0, **options)
    return temp if options[:input_scale] == options[:output_scale]
    str = options[:input_scale]+" to "+options[:output_scale]
    # binding.pry
    rta = 0.0
    case str
    when "kelvin to celsius"
        rta = temp.to_f - 273.15
    when "kelvin to fahrenheit"
        rta = 1.8*(temp.to_f - 273) + 32
    when "celsius to fahrenheit"
        rta = ((9.0*(temp.to_f))/5) + 32 
    when "celsius to kelvin"
        rta = temp.to_f + 273.15
    when "fahrenheit to celsius"
        rta = (temp.to_f - 32)/1.80
    when "fahrenheit to kelvin"
        rta = ((5*(temp.to_f - 32))/9) + 273.15
    else 
        "error"
    end
    rta.to_f
end
p convert_temp(0, input_scale: 'celsius', output_scale: 'kelvin')
# => 273.15 
p convert_temp(0, input_scale: 'celsius', output_scale: 'fahrenheit')
# => 32.0
p "--------------------------"

def defineZeros(str)
	if str.to_s.split(".")[1].to_s.length >= 6
		str = str.to_s.split(".")[1][0,6]
		str = "0."+str
		str = str.to_f
	else
		s =""
		1.upto(6-(str.to_s.split(".")[1].to_s.length)){|i| s+="0" }
		str = str.to_s.concat(s)
	end
	str
end


def plusMinus(arr)
    positivo = 0
    negativo = 0
    cero = 0
    len = arr.length
    arr.each do |item|
        if item.positive?
            positivo+=1
        elsif item.negative?
            negativo+=1
        else
            cero+=1            
        end
    end
    p positivo.fdiv(arr.length)
    p negativo.fdiv(arr.length)
    p cero.fdiv(arr.length)
end

# plusMinus([1,1,0,-1,-1])
plusMinus([-4, 3, -9, 0, 4, 1])


# def miniMaxSum(arr)
#     p arr.first(4).sum > arr.last(4).sum ?  '%d %d'%[arr.last(4).sum,arr.first(4).sum] : '%d %d'%[arr.first(4).sum,arr.last(4).sum]   
# end


def miniMaxSum(arr)
    # p arr.first(4).sum > arr.last(4).sum ?  arr.last(4).sum  arr.first(4).sum : arr.first(4).sum  arr.last(4).sum
    min = 0
    max = 0
    if arr.first(4).sum > arr.last(4).sum
        max = arr.first(4).sum
        min = arr.last(4).sum
    else
        max = arr.last(4).sum
        min = arr.first(4).sum
    end 
    print min
    print " "
    print max
end

p "-------"
# miniMaxSum([1,2,3,4,5])
miniMaxSum([7, 69, 2, 221, 8974])
p ""


def timeConversion(s)
    # Write your code here
    time = s.split(":")
    hora = time[0] 
    minutos = time[1]
    segundos = time[2].split("")
    horario = segundos.last(2) 
    segundo = segundos.first(2)
    p hora
    p minutos
    p horario
    p segundo

    if horario[0] == "P" || horario[0] == "p"
        hora
    end


end

p "-------"
timeConversion("07:05:45PM")
p "-------"
p "-------"
p "-------"
p "-------"

# https://medium.com/@noordean/understanding-ruby-blocks-3a45d16891f1


def age 
    p "ole1"
    yield
    p "ole2"
end 

age{puts 190}

class Array 
    def our_own_each
        for i in self
            yield i
        end
    end
end

[1, 2, 3].our_own_each { |n| puts n * 2 }

p " "
p " "
p " "
p " "
p " "
p " "
p " "


# def factorial(n)
#     return 1 if n == 0
#     factorial = 1
#     while n > 0
#         factorial*=n
#         n-=1
#     end
#     factorial
# end
#  p factorial(5)
#  p factorial(4)
#  p factorial(3)
#  p factorial(2)
#  p factorial(1)
#  p factorial(0)


# https://medium.com/@noordean/understanding-ruby-blocks-3a45d16891f1


def factorial
    yield 5
end

factorial do |n| 
    puts (1..n).reduce(:*)
end





def foo(a,b,my_proc)
    p my_proc.call(a,b)
end

add = proc{|a,b| a+b}
foo(2,3,add)

p "-----------"
p "-----------"
p "-----------"
def diagonalDifference(arr)
    diagonal_principal = 0
    diagonal_secundaria = 0
    for i in 0..arr.length-1
        for j in 0..(arr[i].length)-1
            if i == j
                diagonal_principal+=arr[i][j]
            end
            
            if i + j == arr.size-1
                diagonal_secundaria+=arr[i][j]
            end
        end
    end
    p diagonal_principal
    p diagonal_secundaria
    p (diagonal_principal-diagonal_secundaria).abs()

end
diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
# diagonalDifference([[1, 2, 3],[4, 5, 6],[9, 8, 9]])
p "-----------"
p "-----------"
p "-----------"
def countingSort(arr)
    array_result = Array.new(arr.max+1,0)
    for i in 0..arr.length-1
        array_result[arr[i]]+=1
    end
    array_result
end

def countingSort(arr)
    array_result = Array.new(arr.max+1,0)
    for i in arr
        array_result[i]+=1
    end
    array_result
end
def countingSort(arr)
    freq_arr =  Array.new(100,0)
    arr.each {|i| freq_arr[i] += 1}
    return freq_arr
end


p countingSort([1,1,3,2,1])

p "-----------"
p "-----------"
p "-----------"



def zigzagsequence(arr)
    arr
end
p zigzagsequence([2,3,5,1,4])



# def caesarCipher(s, k)
#     alphabet = "a".upto("z").map(&:to_s)
#     binding.pry
#     s.downcase.split("").map{|x| alphabet.include?("x")? alphabet[alphabet.index(x)+k-26]: x }

# end


def caesarCipher(s, k)
    factor = k
    if factor > 26
        factor = ((k/26)*26-k).abs()
    end
    alphabet_minusculas = "a".upto("z").map(&:to_s)
    alphabet_mayusculas = "A".upto("Z").map(&:to_s)
    rta = s.split("").map do |x| 
        if alphabet_minusculas.include?(x)
            alphabet_minusculas[alphabet_minusculas.index(x)+factor-26]
        elsif  alphabet_mayusculas.include?(x)
            alphabet_mayusculas[alphabet_mayusculas.index(x)+factor-26]
        else
             x
        end
    end
    rta.join("")

end

p caesarCipher("middle-Outz", 3)


# Lazy evaluation

power_array = ->(power,array_size)do
    1.upto(Float::INFINITY).lazy.map{|x| x**power }.first(array_size)
end

puts power_array.(2,10)

p "-----------"
p "-----------"
p "-----------"



# def is_prime n
#     prime = true
#     check = 0 
#     (2..n).each do |x|
#         if n%x == 0
#             check+=1
#         end
#     end
#     if check >= 2
#        prime = false 
#     end 
#     prime
# end

# p is_prime 2

# def is_prime n
#     prime = true
#     check = 0 
#     (2..n).each{|x| check+=1 if n%x == 0 }
#     prime = false  if check >= 2
#     prime
# end

def is_prime n
    check = 0 
    (2..n).each{|x| check+=1 if n%x == 0 }
    return false  if check >= 2
    true 
end

p is_prime 97
p "-----------"
p "-----------"
p "-----------"



p "-----------"
p "-----------"
p "-----------"



p "-----------"
p "-----------"
p "-----------"



# def generate_prime n
#      (2..Float::INFINITY).lazy.select{|x| is_prime(x) }.first(n)
# end

def generate_prime n
     (2.upto(Float::INFINITY)).lazy.select{|x| is_prime(x) }.first(n)
end
puts generate_prime 20


p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"


def is_prime_will(n)

    prime = true
    check = 0 
    (2..n).each{|x| check+=1 if n%x == 0 }
    prime = false  if check >= 2
    prime
end
def count_primes(n)
    # (1..n).select{|x| is_prime(x)}.count    
    (1..n).each{|x| p  is_prime_will(x)}    
end
# puts count_primes 10
puts is_prime_will 1
puts is_prime_will 2
puts is_prime_will 3
puts is_prime_will 4
puts is_prime_will 5
puts is_prime_will 6
puts is_prime_will 7
