def get_proper_divisors(n):
	return [x for x in range(1,n-2) if not divmod(n,x)[1]]
	
def get_aliquot_sum(x):
	return sum(get_proper_divisors(x))

n = int(raw_input("Enter starting value n (positive int): "))
init = n
max = int(raw_input("Enter maximum iterations: "))
print "Aliquot sequence for " + str(n)
cnt = 0
tmp_n = -1
tmp_n2 = -2
tmp_n3 = -3
aliquot_seq = []
print n
while cnt < max:
	tmp_n3 = tmp_n2
	tmp_n2 = tmp_n
	tmp_n = get_aliquot_sum(n)
	print tmp_n
	if tmp_n == 0:
			print "Aliquot sequence terminated at 0."
			break
	if tmp_n == tmp_n2:
		if tmp_n == init:
			print "Repeating initial non-zero aliqout sequence of period 1 found at " + str(tmp_n)
			print str(init) + " is a perfect number."
		elif tmp_n != init:
			print "Repeating non-initial non-zero aliquot sequence of period 1 found at " + str(n)
			print str(init) + " is an aspiring number."
		break
	elif tmp_n3 == tmp_n:
		print "Repeating non-zero aliqout sequence of period 2 found at " \
		+ str(tmp_n2) + " - " + str(tmp_n) 
		print str(init) + " is an amicable number."
		break
	elif aliquot_seq.count(tmp_n) > 0:
		pd = len(aliquot_seq) - aliquot_seq.index(tmp_n)
		print "Repeating non-zero aliquot sequence of period " + str(pd) + \
		" found at " + str(tmp_n)
		print str(init) + " is a sociable number of order " + str(pd) + "."
		break
	else:
		n = tmp_n
		aliquot_seq.append(n)
	cnt = cnt + 1
		