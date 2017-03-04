def gcd(a, b):
    if a==0:
        return b
    return gcd(b%a,a) # recursion
 
def addfrac(n1,d1,n2,d2):
    if d1==0:
        return n2,d2
    if d2==0:
        return n1,d1
    d=(d1*d2)/gcd(d1,d2)
    n=n1*(d/d1)+n2*(d/d2)
    lcf=gcd(n,d)
    return n/lcf,d/lcf

def answer(m):
    s=len(m) # number of states
    pn=[1]+[0]*(s-1) # initial probability distribution = (1,0,0,...), numerator
    pd=[1]+[0]*(s-1) # initial probability distribution = (1,0,0,...), denominator
    for i in range(20):
        print 'pn',pn
        print 'pd',pd
        for kk in range(s):
            if pd[kk]>0:
                print float(pn[kk])/float(pd[kk]),
            else:
                print '-',
        print
        xn=[0]*s # next probability distribution, numerator
        xd=[0]*s # next probability distribution, denominator
        for j in range(s):
            if sum(m[j])>0: # transient state
                for k in range(s):
                    xn[k],xd[k] = addfrac(xn[k],xd[k],pn[j]*m[j][k],pd[j]*sum(m[j]))
            else: # terminal state
                xn[j],xd[j] = addfrac(xn[j],xd[j],pn[j],pd[j])
        pn=xn
        pd=xd

print answer([[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
#print answer([[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
