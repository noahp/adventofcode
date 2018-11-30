from math import sqrt

def factors(n):
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1) if n % i == 0)))

def presents(n):
    a = 0
    for i in xrange(1, 51):
        a += (n / i) * 11 if n%i == 0 else 0
    return a

if __name__ == '__main__':
    # 1. real nasty brute-forcey
    puzzle_input = 34000000
    for x in xrange(110000, puzzle_input/10):
        if sum(factors(x)) * 10 > puzzle_input:
            a = x
            break

    print 'Answer to part 1: ' + str(a)

    # 2. start at result from 1. as a lower bound
    for x in xrange(786240, puzzle_input/11):
        if presents(x) > puzzle_input:
            b = x
            break

    print 'Answer to part 2: ' + str(b)
