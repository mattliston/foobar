def answer(m):
    s=len(m) # number of states
    p=[1.]+[0.]*(s-1) # initial probability distribution = (1,0,0,...)

    # run markov chain for 1000 iterations, can increase if necessary
    for i in range(1000):
        x=[0.]*s # next probability distribution
        for j in range(s):
            if sum(m[j])>0: # transient state
                for k in range(s):
                    x[k] += p[j]*(m[j][k]/float(sum(m[j])))
            else: # terminal state
                x[j] += p[j]
        p=x

    # find best denominator
    ebest=10000000.
    for d in range(2,50): # limit denominators between 2,50, can increase if necessary
        e=0. # error
        for i in range(s):
            e += abs(p[i]*d - round(p[i]*d))
        if e < ebest:
            ebest=e
            dbest=d

    # form answer
    a=[]
    for i in range(s):
        if sum(m[i])==0:
            a.append(int(round(p[i]*dbest)))
    a.append(int(dbest))
    return a
 
print answer([[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
print answer([[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
