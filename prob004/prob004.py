"""
This program searches for the largest palindromic number from the product of two three digit numbers
"""
multNumMax = 0
for i in range (100,999):
   for j in range (100,999):
       multNum = i*j     #Number to check
#if 1:      
#       multNum = 12321  #A test case
       n = str(multNum)  #Convert to a string
       nLen = len(n)     #Length of n
       checkNum = 0      #Number used to determine if palandromic or not

       
       for k in range (0,nLen/2):
          if n[k] == n[nLen-k-1]:
              checkNum = checkNum + 1
       
       if checkNum == nLen/2:#If true then the number is a palandromic
          if multNum > multNumMax:
             multNumMax = multNum
             iMax = i
             jMax = j
          


print "The max palandromic number you want is:"
print multNumMax
       
