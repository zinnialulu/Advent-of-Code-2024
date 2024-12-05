file=open('day4.txt','r')
input=file.read()

import re
#check horizontal
pattern="XMAS"
pattern_reversed="SAMX"
p=(pattern, pattern_reversed)

lines=input.splitlines()
sum_h=0
for row in lines:
    x_h=re.findall(pattern,row)
    y_h=re.findall(pattern_reversed,row)
    n_h=len(x_h)+len(y_h) #number of match in total per row
    sum_h+=n_h
print(f"horizontal match: {sum_h}")


#check vertical
t=[''.join(i) for i in zip(*input.split())] #transpose so column is now rows
#print(t)
sum_v=0
for col in t:
    x_v=re.findall(pattern,col)
    y_v=re.findall(pattern_reversed,col)
    n_v=len(x_v)+len(y_v) #number of match in total per row
    sum_v+=n_v
print(f"vertical match: {sum_v}")


#check diagnal
def searchdiagnal(mymatrix:list):
    diagright=""
    diagleft=""
    find=0
    for i in range(4):
        diagright+=mymatrix[i][i] #right direction diagnal in a 4x4 matrix
        diagleft+=mymatrix[i][3-i] #left direction diagnal in a 4x4 matrix
        if diagright in p:
            find+=1
        if diagleft in p:
            find+=1
    return find #number of find in the minimatrix


#change input into a matrix, turn each line into a list
matrix=[]
for eachline in lines:
    line_list=[]
    for i in range(len(eachline)):
        line_list.append(eachline[i])
    matrix.append(line_list)
#print(matrix)


#minimatrix

sum_diag=0
for col in range(len(matrix)-3):
    res=0
    for row in range(len(matrix)-3):
        minimatrix=[]
        for i in range(4):
            minimatrix.append(matrix[row+i][col:col+4])
        #print(minimatrix)
        res=searchdiagnal(minimatrix)
        sum_diag+=res
print(f"diagnal match: {sum_diag}")

sum_part1=sum_h+sum_v+sum_diag
print(f"part1 answer: {sum_part1}")


###---part 2---###
sum_part2=0
#option 1: find all character A then check its diagnal
p2=("MAS", "SAM")
for row in range(1,len(matrix)-1):
    for col in range(1,len(matrix)-1):
        if matrix[row][col]=="A":
            diag_1=matrix[row-1][col-1]+matrix[row][col]+matrix[row+1][col+1]
            diag_2=matrix[row-1][col+1]+matrix[row][col]+matrix[row+1][col-1]
            if (diag_1 in p2) and (diag_2 in p2):
                sum_part2+=1
print(f"part2 answer: {sum_part2}")

#option 2: check all 3x3 mini matrix (abandoned)