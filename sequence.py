def q(n):
	a, b = 1, 1
	seq = [a,b]
	i = 2
	while i < n:
		c = seq[i - seq[i-1]] + seq[i - seq[i-2]]
		seq.append(c)
		i = i+1
	print seq

q(1000)