import math

_in = [402328, 864247]

def foo(n):
	r,q = True,False
	
	t = n % 10
	n = math.floor(n/10)
	
	while(n != 0 and r):
		r = r and (n%10 <= t)
		if not q:
			q = (t == n%10)
		t = n%10
		n = math.floor(n/10)
	
	return r and q

def bar(n):
	r = True
	
	t = n % 10
	n = math.floor(n/10)
	
	acc_li = []
	acc = 1
	
	
	while(n != 0 and r):
		r = r and (n%10 <= t)
		
		if t == n%10:
			acc += 1
		elif acc > 1:
			acc_li.append(acc)
			acc = 1
		
		t = n%10
		n = math.floor(n/10)
	
	if acc > 1:
		acc_li.append(acc)
	#print(acc_li)
	
	return r and all(map(lambda x: x%2 == 0, acc_li))

count = 0
for i in range(_in[0], _in[1]):
	if bar(i):
		count += 1

print(count)
#print(bar(111122))