file = open('day3.txt','r')
input = file. readlines()

with open('day3.txt') as inputfile:
    input2="".join(line.rstrip('\n') for line in inputfile)
print(type(input2))


import re

def mul(mystring:str):
    p="mul[(]\d{1,3}[,]\d{1,3}[)]" #set up pattern mul{any number between 1-digit number and 3-digit number}[symbol,]{any number between 1-digit number and 3-digit number}
    # result=re.findall(p,input[0])
    # print(result)
    sum=0
    list=re.findall(p,mystring)
    for item in list:
        num="\d{1,3}" #find the numbers
        mul=int(re.findall(num,item)[0])*int(re.findall(num,item)[1]) #change str to int type and multiple num1 and num2
        sum+=mul
    return sum

res1=0
for line in input:
    res1+=mul(line)
print(f"part1: {res1}")

p_2="don't\(\).*?(?=do\(\)|$)"   #pattern for second part: anything between dont and do should be removed --- ./? means any length of character ---(?=) means lookforward --- |$ means or nothing at end
newline=re.sub(p_2,"",input2)
res2=mul(newline)
print(f"part2: {res2}")