# NAME	: vbp
# TYPE	: string -> bool
# IN	: a bracket string containing three different types of brackets (, [, or { and their matching closing bracket.
# OUT	: True if string is well formed[1], otherwise false
# INFO	: [1] A bracket string is considered to be well formed if all opened brackets are closed, an open bracket can only be closed by a closing bracket of the correct type (ie. [ can only be closed by ] etc.).

def vbp(s):
	stack= []
	
	for c in s:
		if c == '(' or c == '[' or c == '{':
			stack.append(c)
		
		else:
			
			if len(stack) < 1:
				return False
			
			a= stack.pop()
			
			if c == ')' and a != '(': 
				return False
			elif c == ']' and a != '[': 
				return False
			elif c == '}' and a != '{':
				return False
			
	return len(stack) < 1


test1= '({[{([])}((()))()()((([[[]]])))[[{}{}{()()}]]]})'

print(vbp(test1))
