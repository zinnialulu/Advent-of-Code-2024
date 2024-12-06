###---Part I---###
file=open('test.txt','r')
lines=file.readlines()
matrix=[]
for line in lines:
    lst=[i for i in line.rstrip()]
    matrix.append(lst)
#print(matrix)
border_west=len(matrix[0])-1
border_south=len(matrix)-1

##find start position
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        if matrix[row][col]=="^":
            start_x=col
            start_y=row
            break
#print(f"start position is at (row:{start_y}; col:{start_x})")

##move functions
#4 move functions: up, right, down, left
def turtle_up(x,y,out,dir):
    if matrix[y-1][x] == "#":
        reach_ob=True
    else:
        reach_ob=False
    while reach_ob==False and y>0:
        matrix[y][x]="X" #leave X
        if matrix[y-1][x] == "#": #check the postion ahead
            reach_ob=True
            break
        else:
            y=y-1#go up
    if y==0: #at border
        out=True
        #print("out of map")
    if reach_ob==True:
        dir='right'
    return x,y,out,dir

def turtle_right(x,y,out,dir):
    if matrix[y][x+1] == "#":
        reach_ob=True
    else:
        reach_ob=False
    while reach_ob==False and x<border_west:
        matrix[y][x]="X" #leave X
        if matrix[y][x+1] == "#": #check the postion ahead
            reach_ob=True
            break
        else:
            x=x+1#go up
    if x==border_west: #at border
        out=True
        #print("out of map")
    if reach_ob==True:
        dir='down'
    return x,y,out,dir

def turtle_down(x,y,out,dir):
    if matrix[y+1][x] == "#":
        reach_ob=True
    else:
        reach_ob=False
    while reach_ob==False and y<border_south:
        matrix[y][x]="X" #leave X
        if matrix[y+1][x] == "#": #check the postion ahead
            reach_ob=True
            break
        else:
            y=y+1#go up
    if y==border_south: #at border
        out=True
        #print("out of map")
    if reach_ob==True:
        dir='left'
    return x,y,out,dir

def turtle_left(x,y,out,dir):
    if matrix[y][x-1] == "#":
        reach_ob=True
    else:
        reach_ob=False
    while reach_ob==False and x>0:
        matrix[y][x]="X" #leave X
        if matrix[y][x-1] == "#": #check the postion ahead
            reach_ob=True
            break
        else:
            x=x-1#go up
    if x==0: #at border
        out=True
        #("out of map")
    if reach_ob==True:
        dir='up'
    return x,y,out,dir

out=False
x=start_x
y=start_y
position=[]
sum=0
while out==False:
    (x,y,out,dir)=turtle_up(x,y,out,dir)
    if (x,y,dir) in position:
        sum+=1
        loop=True
        break
    position.append((x,y,dir))
    print(x,y,out,dir)
    if out==True:
        break
    (x,y,out,dir)=turtle_right(x,y,out,dir)
    position.append((x,y,dir))
    print(x,y,out,dir)
    if out==True:
        break
    (x,y,out,dir)=turtle_down(x,y,out,dir)
    position.append((x,y,dir))
    print(x,y,out,dir)
    if out==True:
        break
    (x,y,out,dir)=turtle_left(x,y,out,dir)
    position.append((x,y,dir))
    print(x,y,out,dir)
    if out==True:
        break




##condition: check border
#x, column number in range of (0,column length)
#y, row number in range of (0,row length) attention:reversed

# direction = up and y(row_no)=0: at N border
# direction = right and x=max=(column length): at W border
# direction = down and y=max=(row_length): at S border
# direction = left and x(col_no)=0: at E border

##change direction
#direction = a+bi
#direction * (-i) turn right 90degree


##find all "X" characters
count=0
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        if matrix[row][col]=="X":
            count+=1
print(f"number of X is: {count+1})")