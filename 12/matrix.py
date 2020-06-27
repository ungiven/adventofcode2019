

# A = [ [ 5 for a in range(3) ] for a in range(4) ]
# B = [ [ 8 for a in range(3) ] for a in range(4) ]
# print(A)
# print(B)

A= [[1, 5, 4], 
    [9, 16, 21], 
	[8, 13, -9] ]
	 
B= [[0, -3, -8], 
	[8, 91, 22], 
	[4, 3, 88] ]

# matrix addition of matrices A and B
AplusB= [[a[n]+b[n] for n in range(len(a))] for a,b in zip(A,B)]

print(AplusB)

