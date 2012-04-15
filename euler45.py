import math

def generate_tri(x):
    return (x * (x +1)) / 2

def check_pentagonal(x):
    n = (math.sqrt((24 * x) + 1) + 1) / 6
    if int(n) == n:
        return n
    else:
        return 0

def check_hexagonal(x):
    n = (math.sqrt(((8 * x) + 1)) + 1) / 4
    if int(n) == n:
        return n
    else:
        return 0

cont = True
ctr = 285
cand = -1
pentp = 0
hexp = 0
while (cont):
    # print "Testing.. " + str(ctr)
    ctr = ctr + 1
    cand = generate_tri(ctr)
    pentp = check_pentagonal(cand)
    hexp = check_hexagonal(cand)
    if pentp > 0 and hexp > 0:
        print str(cand) + ": Triangular(" + str(ctr) + "), Pentagonal(" + \
        str(int(pentp)) + "), Hexagonal(" + str(int(hexp)) + ")" 
        cont = False