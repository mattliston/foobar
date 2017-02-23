def next_steps(current_height,bricks_left,leafs):
    if bricks_left==0:
        return leafs+1
    valid=[]
    for i in range(1,bricks_left+1):
        if i > current_height and ((bricks_left-i > i) or (i == bricks_left and current_height > 0)):
            valid.append(i)
    for n in valid:
        leafs=next_steps(n,bricks_left-n,leafs)
    return leafs

def answer(n):
    return next_steps(0,n,0)

for k in range(3,201):
    print k,answer(k)



