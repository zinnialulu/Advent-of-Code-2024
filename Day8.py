###---Part I---###
file=open('day8.txt','r')
input=file.read()

matrix=[]
for line in input.splitlines():
    line_list=[]
    for i in range(len(line)):
        line_list.append(line[i])
    matrix.append(line_list)
#print(matrix)

#each case, if it is letter or number (x1,y1), find another same one at (x2,y2)
#the "#" will be at (2x1-x2,2y1-y2),(2x2-x1,2y2-y1) if it is not a letter nor a number


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
antenna=set(antenna)
print(f"antenna is {antenna}")
for item in antenna:       
    item_pos=[]
    for match in re.finditer(item,single_line):
        start,end=match.span()
        item_pos.append(start) #generate all cordinates of 
    print(f"antenna {item} is found at {item_pos}")
    for i in range(len(item_pos)-1):
        for j in range(i+1,len(item_pos)):
            x1=int(item_pos[i])
            x2=int(item_pos[j])
            new_left_x=2*x1-x2
            if new_left_x in range(len(single_line)):
                pos.append(new_left_x)
            new_right_x=2*x2-x1
            if new_right_x in range(len(single_line)):
                pos.append(new_right_x)
                
print(f"antinode for all antenna found at {pos}")               
cnt=len(set(pos)) #find all "#"
print(cnt)