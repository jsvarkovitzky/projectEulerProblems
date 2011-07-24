"""
This program sums up the even terms of the Fibonacci sequence that are less than four million
"""
import numpy
n = 4000000  #this is the max Fibonacci number we want to examine
a,b = 0,1
sum = 0

while b < n:
    print a
    a, b = b,a+b
    if a%2 == 0:
        sum = sum + a


print "The sum is:"
print sum
