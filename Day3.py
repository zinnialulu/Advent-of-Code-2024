file=open('day3.txt','r')
input = file.readlines()

#print(input[0])


import re

def mul(mystring:str):
    p="mul[(]\d{1,3}[,]\d{1,3}[)]" #set up pattern
    #result=re.findall(txt,input[0])
    #print(result)
    sum=0
    list = re.findall(p,mystring)
    for item in list:
        num="\d{1,3}"
        #newlist=re.findall(num,item)
        mult=int(re.findall(num,item)[0]) * int(re.findall(num,item)[1])
        sum+=mult
    return sum

sum_1=0
for line in input:
    sum_1+=mul(line)
print(f"part1: {sum_1}")

#all pattern after do() before don't() are 'enabled'
#find all sections between do() and don't() or after do() only then use the part1 prog

p_2="do\(\).*?(?=don't\(\)|$)"
megaline=""
for line in input:
    megaline=megaline.join(line)
length=len(megaline)
print(length)
sum_2=0
#print(input)
x=re.findall(p_2,str(input))
for i in x:
    sum_2+=mul(i)
print(sum_2)
# # #     newline=""
# # #     for i in re.findall(p_2,line):
# # #         newline+=i
# # #     print(newline)
# # #     print(mul(newline))
# # #     sum_2+=mul(newline)
# # # print(f"part 2: {sum_2}")