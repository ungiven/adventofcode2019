import math
import operator

def compute(li):
	#li[1] = j
	#li[2] = k
	
	i = 0
	while(li[i] != 99):
		# Normal mode
		#print(li[i], li[i+1], li[i+2])
		#print(li[i])

		if li[i] < 10:
			if li[i] < 3:
				if li[i] == 1:
					o = operator.add
				else:
					o = operator.mul
				
				li[li[i+3]] = o(li[li[i+1]], li[li[i+2]])
				
				i += 4
			
			# input
			elif li[i] == 3:
				adr = li[i+1]
				val = int(input("input>"))
				li[adr] = val
				i += 2
			
			# output
			elif li[i] == 4:
				adr = li[i+1]
				print(li[adr])
				i += 2
			
			# jump if true
			elif li[i] == 5:
				if li[li[i+1]] != 0:
					i = li[li[i+2]]
					#i = li[i+2]
				else:
					i += 3
			
			# jump if false
			elif li[i] == 6:
				if li[li[i+1]] == 0:
					i = li[li[i+2]]
					#i = li[i+2]
				else:
					i += 3
			
			# less than
			elif li[i] == 7:
				if li[li[i+1]] < li[li[i+2]]:
					li[li[i+3]] = 1
				else:
					li[li[i+3]] = 0
				i += 4
			
			# equals
			elif li[i] == 8:
				if li[li[i+1]] == li[li[i+2]]:
					li[li[i+3]] = 1
				else:
					li[li[i+3]] = 0
				
				i += 4
				
		# parameter mode
		else:
			# handle instruction parameters
			opcode = li[i] % 100
			inst = math.floor(li[i]/100)
			i_1 = inst % 10
			inst = math.floor(inst/10)
			i_2 = inst % 10
			inst = math.floor(inst/10)
			i_3 = inst % 10
			
			# add or multiply
			if opcode < 3:
				p_1 = li[i+1] if i_1 == 1 else li[li[i+1]]
				p_2 = li[i+2] if i_2 == 1 else li[li[i+2]]
				if opcode == 1:
					if i_3 == 0:
						li[li[i+3]] = p_1 + p_2
					else:
						li[i+3] = p_1 + p_2
				elif opcode == 2:
					if i_3 == 0:
						li[li[i+3]] = p_1 * p_2
					else:
						li[i+3] = p_1 * p_2
				
				i += 4
			
			# input
			elif opcode == 3:
				val = int(input("input>"))
				
				if i_1 == 0:
					li[li[i+1]] = val
				else:
					li[i+3] = val
				
				i += 2
			
			#output
			elif opcode == 4:
				if i_1 == 0:
					val = li[li[i+1]]
				else:
					val = li[i+1]
				
				print(val)
				i += 2
			
			# jump if true
			elif opcode == 5:
				p_1 = li[i+1] if i_1 == 1 else li[li[i+1]]
				
				if p_1 != 0:
					p_2 = li[i+2] if i_2 == 1 else li[li[i+2]]
					i = p_2
				else:
					i += 3
			
			# jump if false
			elif opcode == 6:
				p_1 = li[i+1] if i_1 == 1 else li[li[i+1]]
				
				if p_1 == 0:
					p_2 = li[i+2] if i_2 == 1 else li[li[i+2]]
					i = p_2
				else:
					i += 3
			
			# less than
			elif opcode == 7:
				p_1 = li[i+1] if i_1 == 1 else li[li[i+1]]
				p_2 = li[i+2] if i_2 == 1 else li[li[i+2]]
				
				if p_1 < p_2:
					if i_3 == 0:
						li[li[i+3]] = 1
					else:
						li[i+3] = 1
				else:
					if i_3 == 0:
						li[li[i+3]] = 0
					else:
						li[i+3] = 0
				i += 4
			
			# equals
			elif opcode == 8:
				p_1 = li[i+1] if i_1 == 1 else li[li[i+1]]
				p_2 = li[i+2] if i_2 == 1 else li[li[i+2]]
				
				if p_1 == p_2:
					if i_3 == 0:
						li[li[i+3]] = 1
					else:
						li[i+3] = 1
				else:
					if i_3 == 0:
						li[li[i+3]] = 0
					else:
						li[i+3] = 0
				
				i += 4
	
	return li

f = open("input.txt", "r")
f = f.read()
f = f.split(",")
in_list = list(map(int,f))
#in_list = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

compute(in_list)
