###---Part I---###
file=open('day8.txt','r')
input=file.read()

matrix=[]
for line in input.splitlines():
    line_list=[]
    for i in range(len(line)):
        line_list.append(line[i])
    matrix.append(line_list)
ymax=len(matrix)
xmax=len(matrix[0])
#print(matrix)

#option 1: take x and y (2 dimention coordinates)
#each case, if it is letter or number (x1,y1), find another same one at (x2,y2)
#the "#" will be at (2x1-x2,2y1-y2),(2x2-x1,2y2-y1) if it is not a letter nor a number

#option 2: take it as a single line and find for each pair of antenna, find antinodes position left and right, so only need 1 position
#option 2 is wrong as it might be out of border in a 2-D map

import re

single_line="".join(line for line in input.splitlines())
line_list=list(single_line)
antenna=[]
for i in line_list:
    if i!=".":
        antenna.append(i)
antenna=set(antenna)
#print(antenna)

pos=[]
for p in antenna:
    item_pos=[]
    for match in re.finditer(p,single_line):
        start,end = match.span()
        x=int(start//xmax)
        y=int(start%xmax)
        item_pos.append((x,y)) #generate all x,y coordinates of the antenna
    for i in range(len(item_pos)-1):
        for j in range(i+1,len(item_pos)):
            x1=item_pos[i][0]
            y1=item_pos[i][1]
            x2=item_pos[j][0]
            y2=item_pos[j][1]
            new_left_x=2*x1-x2
            new_left_y=2*y1-y2
            new_right_x=2*x2-x1
            new_right_y=2*y2-y1
            if new_left_x in range(xmax) and new_left_y in range(ymax): #check if leftside antinode is within the map
                pos.append((new_left_x, new_left_y))
            if new_right_x in range(xmax) and new_right_y in range(ymax): #check if rightside antinode is within the map
                pos.append((new_right_x, new_right_y))
         
count=len(set(pos))                    
print(f"in total: {count}")