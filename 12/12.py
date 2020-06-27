# Per Bodå
# Advent of Code
# Day 12: N-Body problem
# Answer 1: 12070
# Answer 2: 500903629351944

import re

f= open("input.txt", "r")
_in= f.readlines()
exp= "<?[a-z]=(\-?[0-9]*),?\s?>?"
exp= re.compile(exp)
pos= [ exp.findall(a) for a in _in ]
pos= [ list(map(int, a)) for a in pos ] # position matrix
dis= [ [ 0 for a in range(3) ] for a in range(4) ] # disposition matrix

# for solution to answer 2
# p0= pos[0][2]
# p1= pos[1][2]
# p2= pos[2][2]
# p3= pos[3][2]

def compute_step(pos, dis):
	for i,a in enumerate(pos):
		for b in pos:
			if a == b:
				continue
			
			for j in range(3):
				if a[j] < b[j]:
					dis[i][j] += 1
				elif a[j] > b[j]:
					dis[i][j] -= 1
	
	pos= add_matrix(pos, dis)
	return pos, dis

def add_matrix(A, B):
	return [[a[n]+b[n] for n in range(len(a))] for a,b in zip(A,B)]

def gcd(a,b):
	return a if b == 0 else gcd(b, a % b)

def lcm(a,b):
	return abs(a*b)/gcd(a,b)

# Solution to part 1
for i in range(1000):
	pos, dis = compute_step(pos,dis)

# For solution to part 2
# if p0 == pos[0][2] and p1 == pos[1][2] and p2 == pos[2][2] and p3 == pos[3][2] and dis[0][2] == 0 and dis[1][2] == 0 and dis[2][2] == 0 and dis[3][2] == 0:

# Solution to part 1
pot= map(sum, [map(abs,a) for a in pos])
kin= map(sum, [map(abs,a) for a in dis])
print("Answer 1:",sum(map(lambda a,b: a*b, pot, kin)))
