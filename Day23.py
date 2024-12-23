with open('day23.txt') as file:
    input=file.read()
lines=input.splitlines()
ts=[(x,y) for line in lines for x,y in [line.split("-")]]
ts2=[(y,x) for line in lines for x,y in [line.split("-")]]
ts_all=set(ts+ts2)
nodes=[x for line in lines for t in [line.split("-")] for x in t]
nodes=list(set(nodes))
#print(nodes)
print(f"There are {len(nodes)} nodes")
print(f"There are {len(ts)} 2-node sets")
def lib_twonodes(mylist:list)->dict:
    lib_two={}
    for t in mylist: #list=[(x1,y1),(x2,y2),...]
        x=t[0]
        y=t[1]
        if x in lib_two:
            if y not in lib_two[x]:
                lib_two[x].append(y)
        else:
            lib_two[x]=[y]
        lib_two[x].sort()
        if y in lib_two:
            if x not in lib_two[y]:
                lib_two[y].append(x)
        else:
            lib_two[y]=[x]
        lib_two[y].sort()
    return lib_two

lib_ex=lib_twonodes(ts)
#print(lib_ex)

###part1
output=[]
def threenode(mydictionary:dict):
    for node1,node1_list in mydictionary.items():
        #print(f"1st node: {node1} and list is {node1_list}")
        for node2 in node1_list:
            if node2 in mydictionary:
                #print(f"2nd node: {node2} and list is {mydictionary[node2]}")
                for node3 in mydictionary[node2]:
                    if node3!=node1:
                        #print(f"3rd node: {node3}")
                        if node3 in node1_list:
                            #print(f"{node3} also linked to node1")
                            nnn=[node1,node2,node3]
                            nnn.sort()
                            #print(nnn)
                            if nnn not in output:
                                output.append(nnn)
                                #print(output)
                        #else:
                            #print(f"{node3} not linked to node1")
    return output

triplenodesets=threenode(lib_ex)
#print(nodesets)
print(f"There are {len(triplenodesets)} 3-node sets")



#s1=0
#for eachnodes in triplenodesets:
    #print(eachnodes)
    #string="".join(x[0] for x in eachnodes)
    #if "t" in string:
        #s1+=1
#print(f"part1 answer is {s1}")

###---------part 2 


#find unique 3 nodes sets:
import datetime

#find x nodes sets:
lanlist=triplenodesets
#print(lanlist)
n=len(lanlist)
x=3
print(datetime.datetime.now())
while n>1:
    #print("length is",n)
    newlist=[]
    for nodeset in lanlist:
        for eachnode in nodes:
            if (eachnode not in nodeset) and all((item, eachnode) in ts_all for item in nodeset):
                #print("to modify",nodeset)
                new=nodeset+[eachnode]
                new.sort()
                if new not in newlist:
                    newlist.append(new)
                #print("newlist is now",newlist)
    lanlist.clear()
    lanlist=newlist
    #print("lanlist is now",newlist)
    n=len(lanlist)
    x+=1
    print(f"{x} node set: {n}")
    print(datetime.datetime.now())
print(lanlist)

# ninenodesets=[]
# n=len(triplenodesets)
# count=0
# for i in range(n):
#     set1=set(triplenodesets[i])
#     #print("set1",set1)
#     for j in range(i+1,n):
#         set2=set(triplenodesets[j])
#         #print("set2",set2)
#         if set1.intersection(set2)==set():
#             for k in range(j+1,n):
#                 set3=set(triplenodesets[k])
#                 if set1.intersection(set2,set3)==set():
#                     check=triplenodesets[i]+triplenodesets[j]+triplenodesets[k]
#                     all_pairs_exist = all((item1, item2) in ts_all for item1 in check for item2 in check)
#                     if all_pairs_exist:
#                         count+=1
#                         print(count)
#                         check.sort()
#                         if check not in ninenodesets:
#                             ninenodesets.append(check)
# print(len(ninenodesets))
