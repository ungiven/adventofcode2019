#import math

def parse_inst(s):
	return (s[0], int(s[1:]))

f = open("input.txt", "r")
f = f.readlines()
inst = [ a.split(",") for a in f]

print(parse_inst('R655'))


# (type, ID)
# type: 0 origin, 1 wire, 2 crossing
# ID of wire

orig = (0,0)
pek = (0,0)
id = None
for row in inst:
	if id != None: 
		id += 1
	else: 
		id = 0
	
	for col in row:
		mov = parse_inst(col)
		
		if mov[0] == 'U':
			
		



grid = list()
grid.append(list())





	

#print("First answer: " , r)