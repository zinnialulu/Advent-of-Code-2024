file=open('test19.txt','r')
input=file.read()

pattern_input,design_input=input.split("\n\n")

patterns=pattern_input.split(", ")
designs=design_input.splitlines()

memo={}
def check(design:str):
    if design=="":
        #print("ok")
        return True
    else:
        for p in patterns:
            if design.startswith(p):
                if check(design.removeprefix(p)):
                    return True
    return False

sum=0
for design in designs:
    if check(design):
        sum+=1
        
print(f"part1 answer is {sum}")