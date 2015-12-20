def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

print sum(factors(1100000)) * 10

for x in xrange(110000, 1200000):
    if sum(factors(x)) * 10 > 34000000:
        print x
        break
