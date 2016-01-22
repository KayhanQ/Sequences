def l(n):
	a, b = 1, 1
	seq = [a,b]
	i = 2

	stopper = 0
	while i < n:
		if i == stopper:
			print "*********************"
		
		times = seq[i-1]
		t1 = 1
		for index in range(0,times):
			if i == stopper:
				print "---"
				print t1
				print (i - t1)
			t1 = f(seq, i, t1, n)

		if i == stopper:
			print "---------------"

		times = seq[i-2]
		t2 = 2
		for index in range(0,times):
			if i == stopper:
				print "---"
				print t2
				print (i - t2)

			t2 = f(seq, i, t2, n)

		if i == stopper:
			print "*********************"

		#c = f(seq, i, f(seq, i, 1)) + f(seq, i, f(seq, i, 2))
		c = t1+t2


		seq.append(c)
		i = i+1
		print c
	print seq


def f(seq,i,r,n):
	index = abs(i-r)%i
	if index < 0:
		index = r-i

	return seq[index]




#q(1000)
l(3000)