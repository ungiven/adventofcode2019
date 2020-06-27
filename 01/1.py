import math

f = open("input.txt", "r")

r,s = 0,0

for i in f.readlines():
	i = int(i)
	r += math.floor(i/3)-2
	
	while(i>0):
		i = math.floor(i/3)-2
		if (i>0):
			s += i
		
print("First answer: " , r)
print("Second answer: " , s)
