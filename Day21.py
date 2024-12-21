test21=["029A","980A","179A","456A","379A"]
day21=["789A","540A","285A","140A","189A"]

num={}
num['A']=(0,0)
num['0']=(0,1)
num['1']=(1,2)
num['4']=(2,2)
num['7']=(3,2)
num['2']=(1,1)
num['5']=(2,1)
num['8']=(3,1)
num['3']=(1,0)
num['6']=(2,0)
num['9']=(3,0)

def robot_1(a,b):
    x=num[b][0]-num[a][0]
    y=num[b][1]-num[a][1]
    if a in ('A','0') and b in ('1','4','7'):
        path="^"*x+"<"*y+"A"
    else:
        if b in ('A','0') and a in ('1','4','7'):
            path=">"*abs(y)+"v"*abs(x)+"A"
        else:    
            if y<=0: #prio is < ^ v >
                if x>=0:
                    path="^"*x+">"*abs(y)+"A"
                else:
                    path="v"*abs(x)+">"*abs(y)+"A"
            else:
                if x<=0:
                    path="<"*y+"v"*abs(x)+"A"
                else:
                    path="<"*y+"^"*x+"A"
    return path

dir={}
dir['A']=(0,0)
dir['<']=(2,1)
dir['>']=(0,1)
dir['^']=(1,0)
dir['v']=(1,1)

def robot_2(a,b):
    x=dir[b][0]-dir[a][0]
    y=dir[b][1]-dir[a][1]
    if a=="A" and b=="<":
        path="v<<A"
    else:
        if y<=0:
            if x<=0:
                path="^"*abs(y)+">"*abs(x)+"A"
            else:
                path="<"*x+"^"*abs(y)+"A"
        else:
            if x<=0:
                path="v"*y+">"*abs(x)+"A"
            else:
                path="<"*x+"v"*y+"A"
    return path

#s='A179A'
part_1=0
for i in day21:
    s="A"+i
    r=""
    for n in range(len(s)-1):
        r+=robot_1(s[n],s[n+1])
    r="A"+r
    #print(f"first robot path is {r[1::]}")
    r2=""
    for n in range(len(r)-1):
        r2+=robot_2(r[n],r[n+1])
    r2="A"+r2
    #print(f"second robot path is {r2[1::]}")
    r3=""
    for n in range(len(r2)-1):
        r3+=robot_2(r2[n],r2[n+1])
    l=len(r3)
    nb=int(i[0:3])
    prod=l*nb
    part_1+=prod
    print(f"{i}:")
    print(f"first robot path is {r[1::]}")
    print(f"second robot path is {r2[1::]}")
    print(f"third robot path is {r3}")
    print(f"{l} {nb}")
print(f"part 1 answer is: {part_1}")