#uppg 6
from itertools import groupby
import printtree as pt

f = open("in_real.txt", "r")
f = f.read()

_in = f.split()

#print(_in)

class Node:
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value
	
def walk(root):
	if not root:
		return
	
	print(root.val)
	walk(root.left)
	walk(root.right)

def find(root, val):
	if not root:
		return False
	if root.val == val:
		return True
	
	return find(root.left, val) or find(root.right, val)

def size(root):
	if not root:
		return 0
	
	return 1 + size(root.left) + size(root.right)

def ipl(root):
	if not root:
		return 0
		
	return size(root) + ipl(root.left) + ipl(root.right)

def orbits(root):
	if not root:
		return 0
		
	return size(root) + orbits(root.left) + orbits(root.right) - 1



def insert(root, parent, val):
	if not root:
		return
	
	if root.val == parent:
		if not root.left:
			root.left = Node(val)
		else:
			root.right = Node(val)
	
	insert(root.left, parent, val)
	insert(root.right, parent, val)
	
# find children

def count_children(parent):
	r = 0
	for i in _in:
		a = i.split(")")
		if a[0] == parent:
			r += 1
	
	return r
	
def pop_child(parent):
	
	for i,data in enumerate(_in):
		data = data.split(")")
		if data[0] == parent:
			r = _in.pop(i)
			r = r.split(")")
			return r[1]


def tree(parent):
	if count_children(parent) == 0:
		return
	
	a = pop_child(parent)
	
	insert(root, parent, a)
	tree(a)
	
	if count_children(parent) > 0:
		a = pop_child(parent)
		insert(root, parent, a)
		tree(a)
	
def min_tree(root, v1, v2):
		if find(root.left, v1) and find(root.left, v2):
			return min_tree(root.left, v1, v2)
		
		elif find(root.right, v1) and find(root.right, v2):
			return min_tree(root.right, v1, v2)
		
		else:
			return root
	
def dist_from_root(root, val):	
	if not root:
		return 0
	
	if root.val == val:
		return 0
	
	if find(root.left, val):
		return 1 + dist_from_root(root.left, val)
	
	return 1 + dist_from_root(root.right, val)

# root: minimal tree containing both values
def dist_between(root, v1, v2):
	return dist_from_root(root, v1) + dist_from_root(root, v2)
	
	

a = _in.pop(240).split(")")
root = Node(a[0])
root.left = Node(a[1])

tree(root.left.val)


x = Node(5)
insert(x, 5, 7)
insert(x, 5, 8)
insert(x, 7, 6)
insert(x, 7, 3)
insert(x, 8, 9)
insert(x, 8, 1)
insert(x, 6, 10)
insert(x, 6, 11)

print(pt.print_tree(x))

print(dist_from_root(x, 11))


t = min_tree(root, "SAN", "YOU")
#print(pt.print_tree(t))
print("Size min_tree: ", size(t))

#print(pt.print_tree(root))
print("Size: ", size(root))
print("Orbits: ", orbits(root))
print("Distance between YOU and SAN: ", dist_between(t, "YOU", "SAN")-2)
g = open("printfile.txt", "w")
g.write(pt.print_tree(root))
h = open("printmintree.txt", "w")
h.write(pt.print_tree(t))

#a = sorted(_in, key=lambda x: x.split(")")[0])
#b = [len(list(group)) for key, group in groupby(map(lambda x: x.split(")")[1], a))]
#print(all(map(lambda x: x > 2, b)))

