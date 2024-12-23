with open('day23.txt') as file:
    input=file.read()
lines=input.splitlines()
ts=[(x,y) for line in lines for x,y in [line.split("-")]]
ts2=[(y,x) for line in lines for x,y in [line.split("-")]]
ts_all=set(ts+ts2)


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

nodesets=threenode(lib_ex)
#print(nodesets)
#print("number is", len(nodesets))

s1=0
for eachnodes in nodesets:
    #print(eachnodes)
    string="".join(x[0] for x in eachnodes)
    if "t" in string:
        s1+=1
print(f"part1 answer is {s1}")