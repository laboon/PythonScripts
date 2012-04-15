# The Sieve of Eratasthones
import math

def isDivisible(x, y):
    if (x / float(y)) == int(x / float(y)):
        return True
    else:
        return False

max = int(raw_input("Enter highest number: "))
print "Calculating all primes from 2 to " + str(max)

nums = []
primes = []

for j in range(2,max):
    nums.append(j)

curNum = nums.pop(0)
while curNum < max:
    primes.append(curNum)
    for j in reversed(nums):
        if isDivisible(j, curNum):
            nums.remove(j)
    if len(nums) > 0:
        curNum = nums.pop(0)
    else:
        break
            
print "Primes = " 
print primes 