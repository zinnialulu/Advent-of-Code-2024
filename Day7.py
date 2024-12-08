#find test value of each line
file=open('day7.txt','r')
lines=file.readlines()

def check(value:int, numlist:list):
    if len(numlist)==0:
        return value==0
    if value%numlist[-1]==0: #if last operator is a "*"
        if check(value//numlist[-1],numlist[:-1]):
            return True
    if (value-numlist[-1])>=0: #if last operator is a "+"
        if check(value-numlist[-1], numlist[:-1]):
            return True
    v_str=str(value)
    l=len(str(numlist[-1]))
    if v_str[(-l):]==str(numlist[-1]):        #if last operator is a "||" fking elephant reeeee, last x digits to numlist[-1]
        #new value= value-numlist[-1] / (10**l)
        if check(((value-numlist[-1])/(10**l)),numlist[:-1]):
            return True
    return False




#max_len=0
#to_check=0
sum=0
for line in lines:
    value=int((line.split(":"))[0])
    num=[]
    num+=(int(x) for x in (line.split(" "))[1:])
    # print(f"{value}: {num}")
    # if check(value, num):
    #     print('true')
    # if len(num)>max_len:
        # max_len=len(num)
    #print(max_len) maximum there are 12 numbers in the equation
    if check(value,num):
        #print(f"{value}: {num}")
        sum+=value
print(sum)





