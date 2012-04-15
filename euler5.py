def is_div(x):
    toReturn = True
    # Any int is div by 1 so ignore it
    # Any int div by 20 is div by 10, 5, 4, and 2
    # Any int div by 18 is div by 9, 6 and 3
    # Any int div by 16 is div by 8
    # Any int div by 14 is div by 7
    # So we need to check 11 and higher
    for j in (20, 19, 18, 17, 16, 15, 14, 13, 12, 11):
        # print "testing " + str(j)
        if (float(x) / j) != int(float(x) / j):
            #print "BEEP! " + str(x) + " / " + str(j) + " = " + str(float(x) / j)
            toReturn = False
            break
        else:
            pass
            # print "cool: " + str(x) + " / " + str(j) + " = " + str(float(x) / j)
    return toReturn
    
# Execution starts here
startNum = 2520
curNum = startNum
while (not(is_div(curNum))):
    #print "Tested " + str(curNum)
    curNum = curNum + 20
print "Smallest number divisible by all ints 1 - 20 is: " + str(curNum) 