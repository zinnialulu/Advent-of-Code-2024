with open('day22.txt') as file:
    input=file.read()
    numbers=[int(i) for i in input.splitlines()]

def manipulation(secret_n:int):
    #step1: multiple 64, mix, prune
    a=secret_n*64
    b=a^secret_n
    c=b%16777216
    #step2: divide 32, round down, mix, prune
    d=c//32
    e=d^c
    f=e%16777216
    #step3: mul 2048, mix, prune
    g=f*2048
    h=g^f
    i=h%16777216
    return i

sum=0
example=[123]
sequence_total=[]
banana_list=[]
cnt=0
for n in numbers:
    cnt+=1
    print(cnt)
    price=[]
    for i in range(2000):
        price.append(n%10)
        n=manipulation(n)
    price.append(n%10)
    changes=list((j-i) for i,j in zip(price,price[1:])) #find changes
    sequence=list((a,b,c,d) for a,b,c,d in zip(changes,changes[1:],changes[2:],changes[3:])) #generate a list of all sequences
    #print(sequence)
    banana={}
    for i in range(len(sequence)):
        if sequence[i] not in sequence_total: #generate a gloable sequence list with unique values
            sequence_total.append(sequence[i])
        if sequence[i] not in banana: #generate a library for each buyer, key: sequence list, value: their first price
            banana[sequence[i]]=price[i+4]
    banana_list.append(banana) #generate a library containing all buyer
#now i have a global sequence [seq:tuple]
#now i have a global banana price [{seq:price}]
final=[]
for seq in sequence_total:
    sum_seq=0
    for lib in banana_list:
        if seq in lib:
            sum_seq+=lib[seq]
    final.append(sum_seq)
m=max(final)
print(m)
#print(sequence_total)
#sequence_max=max(sequence_total)
#a=sequence_total.count((-2,1,-1,3))
#a_banana=banana[a]
#b=sequence_total.count(sequence_max)
#b_banana=banana[b]
#print(a,a_banana,b,b_banana)
#print(sequence_max)
    #price_max=max(price)
    #index=price.index(price_max)
    #index2=price.index(price_max,index+1)
    #seq=change_list[(index2-4):index2]
    #print(price_max)
    #print(seq)
    #sum+=n
#print(f"sum is {sum}")
#print(f"values are {price}")