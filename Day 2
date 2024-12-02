#read file
file=open('day2.txt','r')
input = file.readlines()

#check increase or decrease
def check_safe(mylist:list):
    cond=range(1,4) #check if the diff of adjacent is within (1,2,3)
    check_increase=all(((i<j) and (abs(i-j) in cond)) for i,j in zip(mylist,mylist[1:]))
    check_decrease=all(((i>j) and ((i-j) in cond)) for i,j in zip(mylist,mylist[1:]))
    if check_increase==True or check_decrease==True:
        safe=True
    else:
        safe=False
    return safe

#check dampner
def dampener(mylist2:list):
    damp = False
    for ind in range(len(mylist2)):
        newlist=mylist2[:ind]+mylist2[ind+1:]
        if check_safe(newlist) == True:
            damp=True
            break
    return damp

#transform into list
sum_safe=0
sum_safe2=0
for line in input:
    list=[int(num) for num in line.split(" ")]
    if check_safe(list)==True or dampener(list)==True:
        sum_safe2+=1
print(sum_safe2)

file.close()
