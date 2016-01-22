def l(n):
	a, b = 1, 1
	seq = [a,b]
	i = 2

	while i < n:
		times = seq[i-1]
		t1 = apply_func(seq, i, 1, seq[i-1])
		t2 = apply_func(seq, i, 2, seq[i-2])

		c = t1+t2
		seq.append(c)
		i = i+1
		print c
	print seq

def apply_func(seq, i, r, times):
	for index in range(0,times):
		r = seq[i-r]
	return r

#q(1000)
l(5000)