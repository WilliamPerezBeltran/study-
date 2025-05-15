#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix)
    # Write your code here
    n = matrix.length-1
    midle = n/2
    rta = 0  
    for x in (0..midle)
        for y in (0..midle)
            rta+=[matrix[x][y],matrix[x][n-y],matrix[n-x][y],matrix[n-x][n-y]].max
        end    
    end
    rta
end


# https://www.youtube.com/watch?v=KNj0L_Rqp7Q&ab_channel=MayCode
p flippingMatrix([[107, 54, 128, 15],[12, 75, 110, 138],[100, 96, 34, 85],[75, 15, 28, 112]])




# source
# https://www.hackerrank.com/challenges/flipping-the-matrix/problem#:~:text=Sean%20invented%20a%20game%20involving,left%20quadrant%20of%20the%20matrix.