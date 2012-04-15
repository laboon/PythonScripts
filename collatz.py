
def collatz(n):
    cnt = 0
    while n != 1:
        cnt = cnt + 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
    return cnt

print "Collatz Conjecture Tester"
    
numIters = int(raw_input("Enter max value: "))
hwm = 0
hwm_n = 0
for j in range(1, numIters):
    colNum = collatz(j)
    if colNum > hwm_n:
        hwm_n = colNum
        hwm = j
    # print str(j) + ": " + str(colNum)

print "High water mark: " + str(hwm) + " ( " + str(hwm_n) + " iterations) " 
