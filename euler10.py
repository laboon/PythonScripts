import math

def isPrime(n):
    foundPrime = True
    
    # maxCheck = n
    maxCheck = int(math.ceil(math.sqrt(n))) + 1
    
    for j in range(2, maxCheck):
        if (float(n) / float(j)) == int((float(n) / float(j))):
            foundPrime = False
            break
    return foundPrime

print "Determines sum of all primes < n"
n = int(raw_input("Enter n: "))
sum = 2
j = 3
while (j < n):
    if (isPrime(j)):
        sum = sum + j
    j = j + 2
    
print "Sum of all primes < ", n, " is : ", str(sum)
    