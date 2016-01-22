def q(n):
	a, b = 1, 1
	seq = [a,b]
	i = 2
	while i < n:
		c = seq[i - seq[i-1]] + seq[i - seq[i-2]]
		seq.append(c)
		i = i+1
	print seq


def l(n):
	a, b = 1, 1
	seq = [a,b]
	i = 2

	f = lambda seq, i, r: seq[i-r]
	while i < n:
		
		times = seq[i-1]
		t1 = 1
		for index in range(0,times):
			t1 = f(seq, i, t1)

		times = seq[i-2]
		t2 = 2
		for index in range(0,times):
			t2 = f(seq, i, t2)

		#c = f(seq, i, f(seq, i, 1)) + f(seq, i, f(seq, i, 2))
		c = t1+t2
		seq.append(c)
		i = i+1
		print c
	print seq




#q(1000)
l(5000)