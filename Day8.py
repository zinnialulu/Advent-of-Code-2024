###---Part I---###
file=open('test3.txt','r')
input=file.read()

matrix=[]
for line in input.splitlines():
    line_list=[]
    for i in range(len(line)):
        line_list.append(line[i])
    matrix.append(line_list)
print(matrix)

#each case, if it is letter or number (x1,y1), find another same one at (x2,y2)
#the "#" will be at (2x1-x2,2y1-y2),(2x2-x1,2y2-y1) if it is not a letter nor a number


l1="".join(line for line in input.splitlines())
print(l1)


import re

ch="A"
print(re.search(ch,l1))

for match in re.finditer(ch,l1):
    print(match.span())
    (start,end)=match.span()
    print(start)
    print(end)
    col=start%12 #12=len(matrix[0])
    row=start//12
    print(row,col)


    
    

#p="[a-Z]|[0-9]"

# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         if re.match(p,matrix[row][col]






#find all "#"