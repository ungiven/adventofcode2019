import operator

def compute(li, j, k):
	li[1] = j
	li[2] = k
	
	i = 0
	while(li[i] != 99):
		
		if li[i] == 1:
			o = operator.add
		else:
			o = operator.mul
		
		li[li[i+3]] = o(li[li[i+1]], li[li[i+2]])
		
		i += 4
	return li[0]

f = open("input.txt", "r")
f = f.read()
f = f.split(",")
in_list = list(map(int,f))
ans1 = compute(in_list, 12, 2)

in_list = list(map(int,f))
j,k = 0,0
while(j<100 and compute(in_list, j, k) != 19690720):
	if k == 99:
		j += 1
		k = 0
	else:
		k += 1
	
	in_list = list(map(int,f))

print("Answer 1: ", ans1)
print("Answer 2: ", 100 * j + k)
