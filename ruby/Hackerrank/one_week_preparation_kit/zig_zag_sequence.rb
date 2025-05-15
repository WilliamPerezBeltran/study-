#!/bin/ruby

require 'pry'
require 'json'
require 'stringio'


def ZigZagSequence(arr)
    arr.sort!
    k = ((arr.length+1)/2)-1
    rta = []
    (arr[0,k]<<[arr.max]<<arr[k,k].reverse).flatten
end


p ZigZagSequence([4,3,2,1,5,6,7]) #=> [1,2,3,7,6,5,4]
p ZigZagSequence([4,3,2,1,5]) #=> [1,2,5,4,3]
p ZigZagSequence([4,3,2,1,5,6,7,8,9]) #=> [1,2,5,4,3]
p ZigZagSequence([1,2,3,4,5,6,7,8,9,10,11]) #=> [1,2,5,4,3]




# source
