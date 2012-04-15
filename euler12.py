import math

def generate_tri(x):
    return (x * (x +1)) / 2

def factors(n):
    for x in xrange(1,n):
        if n%x == 0:
            return (x,) + factors(n/x)
    print n
    return (n,1)

def get_divisors(x):
    max = x
    numDivs = 0
    j = 1
    numDivs = len(factors(x))
    return numDivs

cont = True
cand = 0
ctr = 0
numDivisors = 0

while (cont):
    ctr = ctr + 1
    cand = generate_tri(ctr)
    numDivisors = get_divisors(cand)
    print "Checking " + str(cand) + " / divisors = " + str(numDivisors)
    if (numDivisors > 500 or cand > 100):
        print str(cand) + " has " + str(numDivisors) + " divisors."
        cont = False