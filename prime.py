import psyco
pysco.full()
def answer(n):
    limit = 104730
    not_prime = set()
#    primes = []
    prime_string = ''
    for i in range(2,limit):
        if i in not_prime:
            continue
        for j in range(i*2,limit,i): #remove multiples
            not_prime.add(j)
#        primes.append(i)
        for j in range(i**2,limit,i**2):
            not_prime.add(j)
        prime_string += str(i)
#    print primes
#    print prime_string
    return prime_string[n:n+5]
print answer(100)
