def recurse(m,state,depth,prev_state,prev_odds,prob):
    print 'm',m,'state',state,'depth',depth,'prev_state',prev_state,'prev_odds',prev_odds,'prob',prob
    if all(x==0 for x in m[state]):
#        print 'enter'
#        print (1/depth)
#        print (float(prev_odds)/float(prev_state))
#        print 'prev odds', prev_odds, 'prev state', prev_state
        prob[state]+=((1/float(depth))*(float(prev_odds)/float(prev_state)))
#        print 'prob[state]', prob[state]
        return prob
    else:
        prev_state=0
        for x in m[state]:
            prev_state+=x
        for i in range(0,len(m[state])):
#            print m[state][i]
            if m[state][i]>0:
                recurse(m,i,depth+1,prev_state,m[state][i],prob)
    return prob

def answer(m):
    return recurse(m,0,0,0,0,[0,0,0,0,0])

print answer([[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
                
            

