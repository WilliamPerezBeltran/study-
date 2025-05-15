# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000


#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

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


plusMinus [1,2,0,-1,-1]
