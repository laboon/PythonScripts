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

nthPrimeToFind = int(raw_input("Find nth prime, n = "))
maxPrime = 0
numPrimes = 1
cur = 2

while numPrimes <= nthPrimeToFind:
    if isPrime(cur):
        numPrimes = numPrimes + 1
        # print "Found prime # " + str(numPrimes) + ", " + str(cur)
    if numPrimes == nthPrimeToFind:
        break
    cur = cur + 1
    
print "Prime #" + str(nthPrimeToFind) + " = " + str(cur)