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
#cannot be compressed into 1D as it might be out of 2D border

single_line="".join(line for line in input.splitlines())
line_list=list(single_line)
#print(l1)

import re

antenna=[]
pos=[]
for i in range(len(single_line)):
    if (single_line[i]!="."): #find all antenna
        pat=single_line[i]
        antenna.append(pat)
antenna=set(antenna) #remove duplicates
#print(f"antenna is {antenna}")

for item in antenna:       
    item_pos=[]
    for match in re.finditer(item,single_line):
        start,end=match.span()
        x=int(start//xmax)
        y=int(start%xmax)
        item_pos.append((x,y)) #generate all cordinates of the antenna x
    #print(f"antenna {item} is found at {item_pos}")
    for i in range(len(item_pos)-1):
        for j in range(i+1,len(item_pos)):
            x1=int(item_pos[i][0])
            y1=int(item_pos[i][1])
            x2=int(item_pos[j][0])
            y2=int(item_pos[j][1])
            new_left_x=2*x1-x2
            new_left_y=2*y1-y2
            if new_left_x in range(xmax) and new_left_y in range(ymax): #check if leftside antinode is within the map
                pos.append((new_left_x,new_left_y))
            new_right_x=2*x2-x1
            new_right_y=2*y2-y1
            if new_right_x in range(xmax) and new_right_y in range(ymax): #check if rightside antinode is within the map
                pos.append((new_right_x,new_right_y))
                
#print(f"antinode for all antenna found at {pos}")               
cnt=len(set(pos)) #find all unique values of "#" positions
print(f"count of unique antinodes positions are {cnt}")