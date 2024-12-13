file=open('Day13.txt','r')
input=file.read()

machines=input.split('\n\n')
#print(machines)


# ax+by=m
# cx+dy=n
# x=(m*d-n*b)/(a*d-b*c)


#find a,b,c,d,m,n

import re
pat_num="[\d]+"
token_tot=0
for machine in machines:
    nums=re.findall(pat_num,machine)
    #print(nums)
    a,c,b,d,m,n=re.findall(pat_num,machine)
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    m=int(m)
    n=int(n)
    m2=10000000000000+m
    n2=10000000000000+n
    # if (m*d-n*b)%(a*d-b*c)==0: # it means we have x as integer
    #     x=int(m*d-n*b)/(a*d-b*c)
    #     y=int((m-a*x)/b)
    #     #print(x,y)
    #     token_tot+=x*3+y
    if (m2*d-n2*b)%(a*d-b*c)==0: #this is for part 2
        x=int(m2*d-n2*b)/(a*d-b*c)
        y=int((m2-a*x)/b)
        #print(x,y)
        token_tot+=x*3+y
print(token_tot)      
        
#need to improve: if divide by zero, press?