"""
This program calculates the sum of the natural numbers less than 1000 that are divisible by either 3 or 5
"""
sum = 0
for i in range(3,1000):
   if i%3 == 0:
      sum = sum + i  
   elif i%5 == 0: 
      sum = sum + i

print sum
