# Advent of code
# Day 14: Space Stoichiometry

import re
import math

f= open("input_test.txt", "r")
#f = f.readlines()

#s = "7 A, 1 B, 4 D => 1 C"
exp= "[=>]?\s?([0-9]*)\s([A-Z]*)\s?"
exp= re.compile(exp)

f= [exp.findall(a) for a in f.readlines()]

#print(f)

# def find_formula(st, di):
    # for i in di.keys():
        # if i[1] == st:
            # return True
    
    # return False

leftover = {}
#leftover['A'] = 1
def build(prod, n):
    r = 0
    
    if n == 0:
        return 0

    if prod == 'ORE':
        return 1
    
    x= formula[prod]
    min_n= int(x[0]) 
    
    if prod not in leftover:
        leftover[prod] = 0
    
    if n <= leftover[prod]:
        t_p = 0
        leftover[prod] -= n
    
    else:
        t_p = n - leftover[prod]
        leftover[prod]= 0
        t_p = math.ceil(t_p/min_n) * min_n
        leftover[prod] += t_p - n


    for key,val in x[1].items():
        r += build(key, int(val))

    return t_p*r

formula= {}
for ele in f:

    prod = ele.pop()
    formula[prod[1]] = [prod[0], {}]
    for n,val in ele:
        formula[prod[1]][1][val] = n


print(formula)

print(build('C', 1))

#print(any(map(lambda x: x[1] == 'x', formula.keys())))
# print(find_formula("C", formula))

