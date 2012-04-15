val = 2
last = 1
max = 4000000
# max = 40
evenTotal = 2

# print last
# print val

while val <= max:
    tmpLast = val    
    val = val + last
    last = tmpLast
    if val > max:
        break
    else:
        # print val
        if (val % 2 == 0):
            # print val
            evenTotal = evenTotal + val
            
print "Total of all evens: " + str(evenTotal)