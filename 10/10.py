# uppg 10
import math

f = open("input_real.txt", "r")
f = f.readlines()
f = [a.strip() for a in f]
_li = list(map(list, f))

#print(_in)

def angle(p1, p2):
	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]
	
	#return 1 if dx == 0 else dy/dx
	return math.atan2(dy, dx)

def dist(p1, p2):
	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]
	
	return math.sqrt(dx**2 + dy**2)

# Problem 1 solution
visible_count = 0
best_point = (0,0)
for i,row in enumerate(_li):
	for j,col in enumerate(row):
		if col == '#':
			point = (j,i)
			visible = []
			for y,irow in enumerate(_li):
				for x,icol in enumerate(irow):
					if icol == '#' and (x,y) != point:
						a = angle(point, (x,y))
						
						if a not in visible:
							visible.append(a)
			
			if len(visible) > visible_count:
				visible_count= len(visible)
				best_point = point

# Problem 2 solution
angles = []
point = (22,19)
asteroids = []
for y,row in enumerate(_li):
	for x, col in enumerate(row):
		if col == '#' and (x,y) != point:
			a = angle(point, (x,y))
			if a not in angles: angles.append(a)
			asteroids.append((x,y))

def find_by_angle(point, in_angle):
	r = []
	for y,row in enumerate(_li):
		for x, col in enumerate(row):
			if col == '#' and (x,y) != point:
				a = angle(point, (x,y))
				if a == in_angle:
					r.append((x,y))
	
	return r

# def find_by_angle(point, in_angle):
	# r = []
	
	# for x,y in asteroids:
		# a = angle(point, (x,y))
		# if a == in_angle:
			# r.append((x,y))
	
	# return r


# fidn the minimum angle between our starting point and two points
#min_angle= min([abs(a - b) for a in angles for b in angles if a != b])


#min_angle= 
start_angle= angle((22,19), (22,18))

count = 0



# search_angle = start_angle
# last_pop = (0,0)
# while(count < 200):
	# l = find_by_angle(point, search_angle)
	# #print(search_angle)
	# if len(l) > 0:
		# print(search_angle)
		# l.sort(key=lambda e : dist(point, e))
		# x,y = l.pop(0)
		# last_pop = (x,y)
		
		# _li[y][x] = '.'
		# count += 1
	
	# search_angle -= min_angle
	
	


# a = find_by_angle(point, start_angle)
# print(a)
# a.sort(key=lambda val : dist(point, val))
# print(a)



# print("start_angle:", start_angle)
# print("min_angle:", min_angle)
# print("Answer 1:",visible_count)
# print("Best point:", best_point)
# print("find by angle", len(find_by_angle((22,19), start_angle)))