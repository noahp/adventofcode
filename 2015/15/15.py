import re, sys, itertools, pprint
from operator import mul

def score(amount, props):
    ''' Score of a particular amount of an ingredient '''
    return [amount * c for c in props]

if __name__ == '__main__':
    a = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.search(r'(\w+): capacity (-*[0-9]+), durability (-*[0-9]+), flavor (-*[0-9]+), texture (-*[0-9]+), calories (-*[0-9]+)', line)
            if m:
                x = [m.group(1),] + [int(c) for c in m.groups()[1:]]
                a.append(x)
    pprint.pprint(a)

    # execute the permutations, ugly brute force search
    m = []
    m2 = []
    for i in itertools.permutations(xrange(0,100), len(a)):
        if sum(i) != 100:
            continue
        scores = zip(*[score(i[idx], x[1:]) for idx,x in enumerate(a)])
        total = reduce(mul,[max(0, sum(c)) for c in scores[:-1]])
        m.append(total)
        if sum(scores[4]) == 500:
            m2.append(total)

    print 'Answer to part 1: ' + str(max(m))
    print 'Answer to part 2: ' + str(max(m2))
