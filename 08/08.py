f = open("input.txt", "r")

f = f.read().strip()

layers = []
o = []
w = 25
h = 6
r = []

count = 0
min_count = 26
min_layer = 0

for i,val in enumerate(f):
	r.append(val)
	if (i+1) % w == 0:
		r = "".join(r)
		o.append(r)
		r = []
	
	if (i+1) % (w*h) == 0:
		o = "".join(o)
		layers.append(o)
		o = []


for i,layer in enumerate(layers):
	for c in layer:
		if c == '0':
			count += 1
		
	if count < min_count:
		min_count = count
		min_layer = i
	
	count = 0

ones = 0
twos = 0

for i in layers[min_layer]:
	if i == '1':
		ones += 1
	if i == '2':
		twos += 1

#print(ones*twos)
final_image = ""
num_layers = len(layers)


for i,val in enumerate(layers[0]):
	if val == '0' or val == '1':
		final_image = final_image + val
	
	else:
		j=1
		while(layers[j][i] == '2'):
			j+=1
		
		final_image = final_image + layers[j][i]

ans2 = ""
for i,val in enumerate(final_image):
		ans2 += val
		if (i+1) % w == 0:
			ans2 += "\n"
	
print("Answer 1:", ones*twos)
print("Answer 2:")
print(ans2)

