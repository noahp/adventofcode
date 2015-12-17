import re, sys, itertools

def findCombinations(containers, remainingEggnog, solvesFound):
    for i in containers:
        pass

if __name__ == '__main__':
    containers = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            containers.append(int(line.strip()))

    # find the minimum and maximum number of containers (bounds)
    b = sorted(containers)[::-1]
    minimum = 0
    for idx,i in enumerate(b):
        if sum(b[:idx]) >= 150:
            minimum = idx
            break

    b = sorted(containers)
    maximum = 0
    for idx,i in enumerate(b):
        if sum(b[:idx]) >= 150:
            maximum = idx
            break

    # run through possible combinations
    a = 0
    b = 0
    m = 0
    for x in xrange(minimum, maximum+1):
        for i in itertools.combinations(containers, x):
            if sum(i) == 150:
                if not m:
                    m = x
                    b = 1
                else:
                    if x == m:
                        b += 1
                a += 1

    print 'Answer to part 1: ' + str(a)
    print 'Answer to part 2: ' + str(b)
