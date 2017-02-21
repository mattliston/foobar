def sort_ascending(n):
    if len(n)<2:
        return n
    mid = int(len(n)/2)
    result = ''
    y = sort_ascending(n[:mid])
    z = sort_ascending(n[mid:])
    (i,j) = (0,0)
    while i<len(y) and j<len(z):
        if int(y[i])>int(z[j]):
            result+=z[j]
            j+=1
        else:
            result+=y[i]
            i+=1
    result+=y[i:]
    result+=z[j:]
    return result

#print sort_ascending('53462')

def sort_descending(n):
    if len(n)<2:
        return n
    mid = int(len(n)/2)
    result = ''
    y = sort_descending(n[:mid])
    z = sort_descending(n[mid:])
    (i,j) = (0,0)
    while i<len(y) and j<len(z):
        if int(y[i])>int(z[j]):
            result+=y[i]
            i+=1
        else:
            result+=z[j]
            j+=1
    result+=y[i:]
    result+=z[j:]
    return result

#print sort_descending('53462')

def n2b(n,b):
    if n==0:
        return 0
    d=[]
    while n:
        d.append(int(n%b))
        n/=b
    foo = ''.join(map(str,d[::-1]))
    if len(foo)<len(str(n)):
        foo=foo.zfill(len(str(n))-len(foo))
    else:
        return foo
    return foo

#print n2b(15,3)        

def answer(n,b):
#    n_a = sort_ascending(n)
#    print n_a
#    exit(0)
    count=1
    sequence_dict={}
    while True:
        n_a = int(sort_ascending(n),b)
        n_d = int(sort_descending(n),b)
#        print 'n_a ', n_a
#        print 'n_d ', n_d
#        print 'n_d-n_a ', n_d-n_a
#        n_ascending = int(n_a)
#        n_descending = int(n_d)
#        print 'n ', n
#        print n2b(n_d-n_a,b)
        if (n2b((n_d-n_a),b)==int(n)):
            return 1
        elif (n2b((n_d-n_a),b) in sequence_dict):
            return count-sequence_dict[n2b((n_d-n_a),b)]+1
        else:
            sequence_dict[n] = count
            x=n2b(n_d-n_a,b)
            n=str(x)
            count+=1

print answer('1211',10)
print answer('210022',3)
        

