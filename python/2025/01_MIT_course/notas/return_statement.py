import math 

def printLogarithm(x):
    if x < 0:
        print "only integer"
        return 
    result = math.log(x)
    print "The result: " + str(result)

printLogarithm(10)

