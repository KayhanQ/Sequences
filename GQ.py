def gq(n, seq):
	for seq_len in range(len(seq), n):
		a = gq_helper(seq, seq_len, 1, seq[seq_len-1])
		b = gq_helper(seq, seq_len, 2, seq[seq_len-2])
		seq.append(a + b)
	return seq

def gq_helper(seq, seq_len, r, times):
	for j in range(0, times):
		index = (seq_len - r) % seq_len
		r = seq[index % seq_len] if index >= 0 else seq[seq_len + index]
	return r

# Printing the last 200 elements of some interesting sequences.
print(gq(1000, [1, 1])[800:])
print(gq(1000, [2, 1])[800:])
print(gq(1000, [0, 1, 1])[800:])
print(gq(1000, [0, 0, 1])[800:])