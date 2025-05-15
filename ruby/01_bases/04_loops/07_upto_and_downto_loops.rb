puts """
A for loop is used to iterate through a collection of information 
such as an array or range. These loops are useful if you need to do 
something a given number of times while also using an iterator.
"""
# example 1
5.upto(10){|num| print "#{num} "}
puts ""
10.downto(5){|num| print "#{num} "}
puts ""