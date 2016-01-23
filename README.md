Generalized Hofstader Q sequence (Variation on Hofstader Q sequence: https://en.wikipedia.org/wiki/Hofstadter_sequence#Hofstadter_Q_sequence )

The Hofstader Q sequence is a meta-Fibonacci sequence. While the terms of the Fibonacci sequence are determined by summing the two preceding terms, the two preceding terms of a Q number determine how far to go back in the Q sequence to find the two terms to be summed.

Fibbonacci sequence:
F(1) = F(2) = 1
F(n) = F(n-1) + F(n-2)

Hofstader Q sequence:
Q(1) = Q(2) = 1
Q(n) = Q(n-Q(n-1)) + Q(n-Q(n-2))

GQ sequence:
GQ(1) = GQ(2) = 1
GQ(n) = GQ(n-GQ(n-GQ(...(GQ(n-1))) + GQ(n-GQ(n-GQ(...(GQ(n-2)))

The Fibonacci sequence performs a lookup once while the Hofstader Q sequence performs it twice. The GQ sequence or Generalized Q sequence uses the two preceding terms to determine how many times to perform the lookup operation in the sequence. This could eb once, twice or any value in the sequence. The first 55 terms are below.

1, 1, 2, 2, 4, 3, 6, 3, 5, 4, 9, 12, 10, 4, 15, 19, 16, 20, 18, 19, 21, 40, 22, 3, 7, 24, 6, 5, 29, 35, 27, 5, 40, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55...

Interestingly though this sequence starts chaotically it eventually becomes the sequence of integers from index 34. This is because the element 34 happened to be generated at index 34 and the element 35 happened to be generated at index 35.

The indexing for this sequence is circular. If there are 10 elements in the sequence and the lookup index is -4 it will return the element at index 6. This is necessary so the seqeunce doesn't die. There could still be an index out of bounds error, for example if there are 10 elements and we look up 12.