def l(n):
	a, b = 1, 1
	seq = [a,b]
	i = 2

	while i < n:
		t1 = apply_func(seq, i, 1, seq[i-1])
		t2 = apply_func(seq, i, 2, seq[i-2])
		c = t1+t2

		i = i+1
		seq.append(c)

		print c
	print seq

def apply_func(seq, i, r, times):
	for j in range(0,times):
		index = (i - r)
		r = seq[index]
	return r

l(100)