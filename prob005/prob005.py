"""
This program test to see what the smallest number divisible by all the integers under 20
"""
from numpy import *
from scipy import factorial

n = 20 #number to check

#We only test numbers that don't factor into n to prevent repeated checking
#a = array([3,4,6,7,8]) #for n = 10
a = array([3,6,7,8,9,11,12,13,14,15,16,17,18]) #for n = 20

nfactorial = factorial(n)
print "n factorial is:"
print nfactorial

N = 10**9 #this is the max number we check, used to prevent overflow
for i in arange (n*(n-1),N,n*(n-1)):
   numPassed = 0
 
   percentDone = (i*100)/N #A crude % keeping methood
   print percentDone
   
   #Only loop over numbers in a to prevent unessisary checking 
   for j in range (0,a.shape[0]):
      
      if i%a[j] == 0:
         numPassed = numPassed + 1

   if numPassed == a.shape[0]:
      print "The number you are looking for is:"
      print i
      break




