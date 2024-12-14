file=open('day14.txt','r')
robots=file.readlines()

#print(robots)

xmax=101
ymax=103

def robot_move(pos:list,v:list,t:int):
    xt=pos[0]+v[0]*t #xt=x+vx*t
    yt=pos[1]+v[1]*t
    xt=xt % xmax
    yt=yt % ymax
    return [xt,yt]

def quarter(p:list):
    if p[0]==xmax//2 or p[1]==ymax//2:
        return [0]
    elif p[0] in range(0,xmax//2):
        if p[1] in range(0,ymax//2):
            return [1]
        else:
            return [3]
    elif p[1] in range(0,ymax//2):
            return [2]
    else:
            return [4]

# q=[]
# allpos=[]

import re
def move(t:int):
    for robot in robots:
        x,y,vx,vy=re.findall("[-\d]+|[\d]+",robot)
        pos=[int(x),int(y)]
        v=[int(vx),int(vy)]
        #print(pos,v)
        new_pos=robot_move(pos,v,t)
        allpos.append(new_pos)
        q.append(quarter(new_pos))
      
part_1=1
# for i in range(1,5):
#     part_1*=q.count([i])
# print(f"part1: {part_1}")

def xmas(line:str):
    if re.search("*****",line) != "None":
        return True
    return False

find=False
t=7847
while find==False and t<7848:
    q=[]
    allpos=[]
    move(t)
    fo=open('D14.txt','w')
    for j in range(0,ymax):
        l=""
        for i in range(0,xmax):
            if [i,j] not in allpos:
                l=l+"."
            else:
                l=l+"a"
        fo.write(l)
        #if re.findall("aaaaa",l) == []:
        #    find=False
        #else:
        #    find=True
        #    break
        fo.write("\n")
    fo.close()
    fr=open('D14.txt','r')
    #lines=fr.readlines()
    #for line in lines:
    #    if re.findall("aaaaa",line) == []:
    #        find=False
    #    else:
    #        find=True
    #print(t)
    t+=1
print(f"time is at {t}")