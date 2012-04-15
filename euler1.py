total = 0
j = 0
for j in range(1, 1000):
    print "checking " + str(j)
    if (j % 3 == 0) or (j % 5 == 0):
        print "adding " + str(j)
        total = total + j
print total