###---Part 1---###
file=open('test10.txt','r')
input=file.read()

#define a function to find chain of 1 to 9

#op1: find 9 and record their positions; number = unique positions
#op2: find all nearby 9 and seek if there is a way to reach it, max in 9x9

matrix=[]
for line in input.splitlines():
    l=[]
    for num in line:
        l.append(int(num))
    matrix.append(l)
# print(matrix) 

xmax=len(matrix[0])
ymax=len(matrix)
# print(xmax,ymax)

pos_head=[] # find all positions of "0" -- trialhead
for row in range(ymax):
    for col in range(xmax):
        if matrix[row][col]==0:
            pos_head.append((row,col))
# print(pos_head)

end_x=0
end_y=0

def findnine(y,x,n):
    if n==9:
        end.append((x,y))
        return True
    else:
        for direction in ([1,0],[0,1],[-1,0],[0,-1]):       
            if matrix[y+direction[0]][x+direction[0]]==n+1:
                return findnine(y+direction[0],x+direction[0],n+1)
            if x==0 or x==xmax-1
            
            if y==0 or y==ymax-1
    return False

end=[]
for (a,b) in pos_head:
    findnine(a,b,0)
print(end)
