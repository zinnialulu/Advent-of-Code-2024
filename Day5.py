#find instruction section
#find page section
file=open('day5.txt','r')
input=file.read()

allinput=input.split('\n\n')
#print(allinput)
rule=allinput[0].split('\n')
#print(rule)
instruction=allinput[1].split('\n')
#print(instruction)

import re

violation=[]
for item in rule:
    p1=item.split('|')[1]+".*?"+item.split('|')[0]
    #print(p1)
    violation.append(p1)
#print(violation)

sum=0
wrong_instruction=[]
for eachinstruction in instruction:
    for i in violation:
        if bool(re.search(i,eachinstruction))==True:
            #print(f"violated: {eachinstruction}")
            check="incorrect"
            wrong_instruction.append(eachinstruction)
            break
        else:
            #find middle page:
            check="correct"
    if check=="correct":
        newlist=eachinstruction.split(',')
        l=len(newlist)
        #print(eachinstruction)
        index=(l)//2
        #print(type(index))
        #print(f"correct: {eachinstruction}")
        if newlist[index]!= '':
            num=int(newlist[index])
            #print(num)
            sum+=num
print(f"part1 answer: {sum}")  




###---Part I---###

#each xx|yy is a pattern, make a list of violation of pattern which is yy|xx
#if there is any violation pattern found in the page instruction then it is incorrect = if none of violation found, it is correct

#find the middle page of all correct page instruction



import functools
###---Part II---###
#try to find a way to re-arrange wrong instruction
#option1: when you find the violation, reverse the numbers then begin from beginning? then continue
#option2: euhhhhh magic sorting?
#print(wrong_instruction)
#print(rule)
patterns=[]
for item in rule:
    p=(item.split('|')[0],item.split('|')[1])
    #print(p1)
    patterns.append(p)
#print(patterns)
#s=['75','97','47','61','53']

wrong_gen = (line.split(',') for line in wrong_instruction)
def compare_rule(n1,n2):
    if (n1,n2) in patterns:
        return -1
    elif (n1,n2) in patterns:
        return 1
    else:
        return 0

sum_2=0

for x in wrong_gen:
    a=sorted(x, key = functools.cmp_to_key(compare_rule))
    l=len(a)
        #print(eachinstruction)
    index=(l)//2
    if a[index]!= '':
            mid=int(a[index])
            #print(num)
            sum_2+=mid
    #print(f"s is {s}")
    #print(f"a is {a}")
print(f"part2 answer: {sum_2}")
