file=open('day3.txt','r')
input = file.readlines()

with open('day3.txt') as inputfile:
    input2=''.join(line.rstrip('\n') for line in inputfile) 


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

# p_2="do\(\).*?(?=don't\(\)|$)"
# sum_2=0
# #print(input)
# x=re.findall(p_2,input2)
# print(len(x))
# for eachstring in x:
#     sum_2+=mul(eachstring)
# print(sum_2)


# headline="where())what()@)select()why()?mul(371,776)/%how()'~+:how()mul(977,266)@$@mul(749,170)how()<;$^#what()select()mul(338,975)>from()+,{select()!!mul(626,938)%/>^{((}]mul(733,977)>)() +$)mul(695,376)!%#how()mul(767,788)<(mul(876,501)mul(18,72)[*when(625,65)<mul(515,137)>*('what()mul(491,884)from()?{>how()mul(645,385)/[when(){what()why()mul(802,476)#'select()who(327,719)+-,##mul(103,807)#(mul(192,909):@'^where(247,392)!who()</mul(305,182)[@[;!;mul(553,402)<%mul(247,89)!mul(91,152)$@mul(502,543)+why()what()[when()@>^mul(875,344)why()mul(205,505)?;?when()!],mul(165,670),#$++'>)'mul(503,815):mul(483,302)~+*}!$where()why()&mul(785,794)/,{why();where(218,722)}when()"
# sum_head=mul(headline)
# print(sum_head)


p_3="don't\(\).*?(?=do\(\)|$)"
string_replaced=re.sub(p_3,'',input2)
result=mul(string_replaced)
print(f"part2: {result}")