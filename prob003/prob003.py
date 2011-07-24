"""
This program calculates the largest prime factors of n
"""
from numpy import *
def bigPrimeFinder(n):
   for i in range (3,floor(sqrt(n))):
      while n%i == 0:
         i_max = i
         n = n/i
         print i



n = 600851475143 #number from the problem
#n = 12195       #sample test
bigPrimeFinder(n);

