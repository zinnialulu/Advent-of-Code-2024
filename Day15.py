file=open('day15.txt','r')
input=file.read()

######------read input instructions------#####
mapinput,instructioninput=input.split('\n\n')


######------generate instructions into 1 line------#####
instructions=instructioninput.splitlines()
instruction=""
for line in instructions:
    instruction+=line
#print(instruction)

######------generate map------#####
map=[]
for line in mapinput.splitlines():
    line_list=[]
    for i in range(len(line)):
        line_list.append(line[i])
    map.append(line_list)
xmax=len(map) #row
ymax=len(map[0]) #col

##find initial position
for i in range(xmax):
    for j in range(ymax):
        if map[i][j]=="@":
            x0=i
            y0=j


######------move function------#####
def move(position,direction:str):
    x,y=position
    if direction == "<":
        if map[x][y-1]=="#": #if encounter wall
            return (x,y)
        elif map[x][y-1]==".": #if free to move
            return (x,y-1)
        else: #if meet box
            for i in range((y-1),-1,-1):
                if map[x][i]==".": #exchange space with first box position
                    map[x][i]="O"
                    map[x][y-1]="."
                    return (x,y-1) #move robot
                elif map[x][i]=="#": #if meet wall before space, dont move and go on for next instruction
                    return (x,y)
    if direction == "^":
        if map[x-1][y]=="#": #if encounter wall
            return (x,y)
        elif map[x-1][y]==".": #if free to move
            return (x-1,y)
        else: #if meet box
            for i in range((x-1),-1,-1):
                if map[i][y]==".":
                    map[i][y]="O"
                    map[x-1][y]="."
                    return (x-1,y)
                elif map[i][y]=="#":
                    return (x,y)
    if direction == ">":
        if map[x][y+1]=="#": #if encounter wall
            return (x,y)
        elif map[x][y+1]==".": #if free to move
            return (x,y+1)
        else: #if meet box
            for i in range((y+1),ymax+1):
                if map[x][i]==".":
                    map[x][i]="O"
                    map[x][y+1]="."
                    return (x,y+1)
                elif map[x][i]=="#":
                    return (x,y)
    if direction == "v":
        if map[x+1][y]=="#": #if encounter wall
            return (x,y)
        elif map[x+1][y]==".": #if free to move
            return (x+1,y)
        else: #if meet box
            for i in range((x+1),xmax+1):
                if map[i][y]==".":
                    map[i][y]="O"
                    map[x+1][y]="."
                    return (x+1,y)
                elif map[i][y]=="#":
                    return (x,y)

######------Part 1------#####
pos=(x0,y0)
map[x0][y0]="."
for ins in instruction:
    pos=move(pos,ins)
    #print(f"after direction {ins} position at {pos} ")
#print(map)

######------Calculate GPS score------#####
GPS_tot=0
for row in range(ymax):
    for col in range(xmax):
        if map[row][col]=="O":
            score=100*row+col
            GPS_tot+=score
print(f"Total GPS is :{GPS_tot}")