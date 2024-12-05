#find instruction or rule section
#find page section
file= open('day5.txt','r')
input=file.read()

allinput=input.split('\n\n')
#print(allinput)
rule=allinput[0].split('\n')
#print(rule)
instruction=allinput[1].split('\n')
#print(instruction)


###---Part I---###
#each xx|yy is a pattern, make a list of violation of pattern with yy|xx
#if there is any violation then it is incorrect = if none of violation found, it is correct

import re

violation=[]
wrong_instruction=[]
for item in rule:
    p=item.split('|')[1]+".*?"+item.split('|')[0]
    violation.append(p) #form a list of all violation rules

sum=0
for eachinstruction in instruction:
    for i in violation: #check if each violation rule appeared
        if bool(re.search(i,eachinstruction))==True: 
            wrong_instruction.append(eachinstruction)
            check="incorrect"
            break
        else:
            check="correct"
    if check=="correct":
        newlist=eachinstruction.split(',')
        l=len(newlist)
        index=l//2 #find index of middle number
        num=int(newlist[index])
        sum+=num
print(f"part 1 answer: {sum}")
#find the middle number of each 'correct' page instruction


###--Part II---###

#try to find a way to re=arrange each wrong instruction
#option 1: when you find the violation, reverse the numbers then continue
#option 2: magic sorting function => cmp
import functools

patterns=[]
for item in rule:
    p=(item.split('|')[0],item.split('|')[1]) #it needs to be a tuple
    patterns.append(p)

wrong_gen=(line.split(',') for line in wrong_instruction) #create a generator type for sorted()

def compare(n1,n2): #define a function to be used in cmp_to_key
    if (n1,n2) in patterns:
        return -1
    elif (n2,n1) in patterns:
        return 1
    else:
        return 0

sum_2=0
for x in wrong_gen:
    a=sorted(x,key=functools.cmp_to_key(compare)) 
    l=len(a)
    index=l//2
    mid=int(a[index])
    sum_2+=mid
print(f"part 2 answer: {sum_2}")