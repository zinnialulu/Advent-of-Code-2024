input=[41078,18,7,0,4785508,535256,8154,447]

###---part 1---###

def stone(mylist:list):
    new_list=[]
    for n in mylist:
        if n ==0:
            new_list.append(1) ##if number is 0, replace by 1
        elif len(str(n))%2 !=0:
            new_list.append(n*2024)
        else:
            l=int(len(str(n))/2)
            n_str=str(n)
            new_list.append(int(n_str[:l]))
            new_list.append(int(n_str[l:]))
    return new_list
        
test=[125,17]

l=[0]
# for i in range(1,76):
#     l=stone(l)
#     print(i)
# print(len(l))
# stone_nb=len(input)
#print(f"The stone numbers are: {stone_nb}")



###---part 2---###
# memo = {}

# def memo_function(args):
#   if(args in memo):
#     return memo[args]
#   else:
#     # Do this and update memo.

def blink(n:int):
    if n ==0:
        return [1]
    elif len(str(n))%2 ==0:
        l=int(len(str(n))/2)
        n_str=str(n)
        return [int(n_str[:l]),int(n_str[l:])]
    return [n*2024] #return list


memo={}
def blink_stone(value,blink):
    if value in memo:
        return memo[value]
    
    memo[value] = blink(value)
    return memo[value]

l=0
for i in range(1,76):
    l=blink_stone(l)
    print(i)
print(len(l))


