def getSumOfSq(x):
    sum = 0
    oneSq = 0
    for j in range(1,x+1):
        oneSq = j * j
        sum = sum + oneSq
    return sum

def getSqOfSum(x):
    sum = 0
    for j in range(1,x+1):
        sum = sum + j
    sum = sum * sum
    return sum

print "Find diff of sum of squares and squares of sum of all natural numbers 1 - n"
n = int(raw_input("Enter n: "))
print getSqOfSum(n)
print getSumOfSq(n)

diff = getSqOfSum(n) - getSumOfSq(n)
print "Diff is: " + str(diff)