#read the file
file=open('C:/Users/yingl/OneDrive/Bureau/AoC2024/day1.txt','r')
lines=file.readlines()
#print(lines[:5])

station1=[]
station2=[]
#convert the string to number and transpose to become two lists
for line in lines:
    num1=int(line[:5])
    num2=int(line[7:])
    station1.append(num1)
    station2.append(num2)

#arrange the list from smallest to biggest
station1.sort()
station2.sort()  

#distance = difference(absolute number) of list1[i] and list2[i]
sum=0
for i in range(len(station1)):
    distance=abs(station1[i]-station2[i])
    sum+=distance #total distance = sum distance
print(sum)

#similarity score = (num in list1) x (occurence of num in list2)
sum_sim=0
for i in range(len(station1)):
    simscore=station1[i] * station2.count(station1[i])
    sum_sim+=simscore
print(sum_sim)
